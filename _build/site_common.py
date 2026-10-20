"""Shared, idempotent publishing rules for the static pages and legacy generators.

Run with the SEO workspace's Python environment (beautifulsoup4 dependency).
Store prices were checked against the German listings on 2026-10-20.
"""
from pathlib import Path
from urllib.parse import urlencode
import html
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
APPLE = 'https://apps.apple.com/de/app/der-notenrechner/id1662507346'
PLAY = 'https://play.google.com/store/apps/details?id=com.notenrechner.App'
PRICE_TEXT = 'iPhone &amp; iPad: 5,99 € im deutschen App Store · Android: kostenlos bei Google Play. Stand: 20.10.2026.'
NP_MAP = dict(zip(range(15, -1, -1), ['1+','1','1-','2+','2','2-','3+','3','3-','4+','4','4-','5+','5','5-','6']))

def replace_element(source, selector, replacement, required=True):
    node = BeautifulSoup(source, 'html.parser').select_one(selector)
    if node is None:
        if required:
            raise ValueError(f'Missing element: {selector}')
        return source
    start = sum(len(line) for line in source.splitlines(keepends=True)[:node.sourceline - 1]) + node.sourcepos
    if node.name in {'input','meta','link','img','br','hr'}:
        end = source.index('>', start) + 1
    else:
        depth = 0
        for match in re.finditer(rf'</?{re.escape(node.name)}\b[^>]*>', source[start:], re.I):
            depth += -1 if match.group().startswith('</') else 1
            if depth == 0:
                end = start + match.end()
                break
        else:
            raise ValueError(f'Unclosed element: {selector}')
    return source[:start] + replacement + source[end:]

def campaign_for(path):
    rel = str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
    if re.match(r'(?:notenschluessel-rechner|ihk-notenschluessel)/.+/index.html', rel):
        return 'regional_calculators'
    if rel in {'index.html','android/index.html','tablet/index.html','ipad/index.html','notenverwaltungs-apps-vergleich/index.html'}:
        return 'app_pages'
    return 'general_calculators'

def store_links(campaign):
    return (
        APPLE + '?' + urlencode({'pt':'125935959','ct':campaign,'mt':'8'}),
        PLAY + '&' + urlencode({'referrer':urlencode({'utm_source':'notenrechnerapp.de','utm_medium':'website','utm_campaign':campaign})})
    )

def normalize_html(source, path):
    replacements = {
        'Der Notenrechner — kostenlos im App Store.': 'Der Notenrechner für iPhone, iPad und Android.',
        'Der Notenrechner ist kostenlos im App Store.': 'Der Notenrechner für iPhone, iPad und Android.',
        'Der Notenrechner — kostenlos für iPhone, iPad und Android.': 'Der Notenrechner für iPhone, iPad und Android.',
        'Der Notenrechner für iPhone, iPad und Android — kostenlos im App Store.': 'Der Notenrechner für iPhone, iPad und Android.',
        'kostenlose App für iPhone, iPad und Android': 'App für iPhone, iPad und Android',
        'Der Notenrechner ist eine kostenlose App': 'Der Notenrechner ist eine App',
        'Kostenlos · Keine Werbung · Kein Abo': 'Ohne Werbung · Ohne Konto · Offline',
        'Kostenlos · App Store &amp; Google Play': 'Für Lehrkräfte · iOS &amp; Android',
        'Kostenlos · App Store & Google Play': 'Für Lehrkräfte · iOS &amp; Android',
        'Kostenlos. Keine Werbung. Keine In-App-Käufe.': 'Keine Werbung. Kein Konto. Keine Cloud.',
        'Kostenlos für iPhone, iPad und Android': 'Für iPhone, iPad und Android',
        'Jetzt kostenlos im App Store laden': 'Noten und Klassen in der App verwalten',
        'Jetzt kostenlos laden — App Store &amp; Google Play': 'Für iPhone, iPad und Android laden',
        'Erstellt mit notenrechnerapp.de — Kostenlose App im App Store laden': 'Erstellt mit notenrechnerapp.de — Online-Rechner kostenlos nutzen',
        'eine vollständige App-Lösung, kostenlos, ohne Tracking, offline.': 'eine App für Klassen und Noten, ohne Tracking und offline.',
        'Funktionsumfang, Datenschutz und Preis (kostenlos) entsprechen 1:1 der iOS-Version.': 'Auch auf Android stehen Notenberechnung, Klassenverwaltung und lokale Datenspeicherung zur Verfügung. Die Android-App ist kostenlos; die iOS-App kostet derzeit 5,99 € im deutschen Store.',
        'Funktionsumfang, Datenschutz-Architektur und Kosten entsprechen 1:1 der iOS-Version: vollständig lokal, ohne Cloud, ohne Werbung, kostenlos.': 'Die Android-App arbeitet lokal, ohne Cloud und ohne Werbung. Sie ist bei Google Play kostenlos erhältlich; die iOS-App kostet derzeit 5,99 € im deutschen Store.',
        'keine Werbung — derselbe Stand wie auf iOS.': 'keine Werbung. Die iOS-App kostet derzeit 5,99 € im deutschen App Store.',
        'Kostenlos. Offline. Ohne Cloud.': 'Offline. Ohne Werbung. Ohne Cloud.',
        '(Android in Kürze) speichert Klassen, Klausuren und Zeugnisnoten — auch das kostenlos, lokal, ohne Cloud.': 'für iPhone, iPad und Android speichert Klassen, Klausuren und Zeugnisnoten lokal, ohne Cloud.',
        'lädt die kostenlose App:': 'nutzt die App für iPhone, iPad oder Android:',
        'kostenloser Download im App Store, Android-Version in Kürze.': 'iPhone und iPad im App Store (5,99 €), Android kostenlos bei Google Play.',
        'Nichts. Web-Rechner und App sind kostenlos. Keine In-App-Käufe, kein „Pro"-Modell, kein Abonnement. Die App finanziert sich nicht — sie ist ein Projekt aus dem eigenen Schulalltag, kein Geschäftsmodell.': 'Der Web-Rechner ist kostenlos. Die App kostet für iPhone und iPad derzeit 5,99 € im deutschen App Store; auf Android ist sie kostenlos bei Google Play erhältlich.',
        'Entwickelt von einem Lehrer, für Lehrkräfte': 'Entwickelt für Lehrkräfte',
        '12 → 2-': '12 → 2+',
    }
    for before, after in replacements.items():
        source = source.replace(before, after)

    # Keep useful initial output even when JavaScript is unavailable or deferred.
    preset_match = re.search(r'const PRESETS\s*=\s*(\{.*?\n\s*\});', source, re.S)
    if preset_match and 'NP_MAP' in source:
        raw = re.sub(r'\b(grade|minPct)\s*:', r'"\1":', preset_match.group(1).replace("'", '"'))
        presets = json.loads(raw)
        soup = BeautifulSoup(source, 'html.parser')
        choice = soup.select_one('#preset option[selected], #gradeType option[selected]') or soup.select_one('#preset option, #gradeType option')
        maximum = soup.select_one('#maxPts, #maxPoints')
        if choice and maximum:
            primary = path.parent.name == 'grundschule'
            if primary:
                source = source.replace('<div class="calc-result-label">Notenpunkte</div>', '<div class="calc-result-label">Schulnote</div>').replace('<th>Notenpunkte</th>', '<th>Schulnote</th>')
                source = source.replace('resultGrade.textContent = activeGrade;', 'resultGrade.textContent = NP_MAP[activeGrade];')
                source = source.replace("resultDesc.textContent = (NP_MAP[activeGrade] || '') + ' · ' + gradeDesc(activeGrade);", "resultDesc.textContent = gradeDesc(activeGrade);")
                source = source.replace("+ t.grade + '</span><span class=\"grade-label\">' + (NP_MAP[t.grade] || '')", "+ NP_MAP[t.grade] + '</span><span class=\"grade-label\">' + ''")
            rows = []
            for threshold in presets[choice['value']]:
                points = threshold['minPct'] / 100 * float(maximum.get('value', '100'))
                points_text = f'{points:.4f}'.rstrip('0').rstrip('.').replace('.', ',')
                value = threshold['grade']
                display = NP_MAP[value] if primary or path.parent.name == 'punkte-in-noten' else str(value) + ' <span class="grade-label">' + NP_MAP[value] + '</span>'
                rows.append(f'<tr><td><div class="grade-cell"><span class="grade-name">{display}</span></div></td><td>{points_text} Punkte <span class="grade-label">({threshold["minPct"]} %)</span></td></tr>')
            source = replace_element(source, '#tableBody', '<tbody id="tableBody">\n' + '\n'.join(rows) + '\n</tbody>')
        if 'data-preset-validation' not in source:
            # Load the tiny local number parser before any inline calculator.
            source = source.replace('<script src="/assets/calculations.js"></script>', '')
            source = source.replace('</head>', '<script src="/assets/calculations.js" data-preset-validation></script>\n</head>')
            guard = """
      const suppliedMaximum = NotenrechnerMath.number((document.getElementById('maxPts') || document.getElementById('maxPoints')).value);
      if (suppliedMaximum === null || suppliedMaximum <= 0) {
        resultGrade.textContent = '—';
        resultDesc.textContent = 'Bitte eine positive Maximalpunktzahl eingeben.';
        resultPct.textContent = '';
        tableBody.innerHTML = '';
        return;
      }
"""
            source = re.sub(r'(function calculate\([^)]*\)\s*\{)', lambda m: m.group(1) + guard, source, count=1)
            source = source.replace('const achievedNum = parseFloat(achievedRaw);', 'const achievedNum = NotenrechnerMath.number(achievedRaw);')
            limit = 'maxPoints' if 'const maxPointsInput ' in source else 'maxPts'
            source = source.replace("const hasAchieved = achievedRaw !== '' && !isNaN(achievedNum) && achievedNum >= 0;", f"const hasAchieved = achievedNum !== null && achievedNum >= 0 && achievedNum <= {limit};")
            source = source.replace("resultDesc.textContent = 'Punkte eingeben';", "resultDesc.textContent = achievedRaw ? 'Bitte Punkte zwischen 0 und dem Maximum eingeben.' : 'Punkte eingeben';")
            source = source.replace("resultDesc.textContent = 'Erreichte Punkte eingeben';", "resultDesc.textContent = achievedRaw ? 'Bitte Punkte zwischen 0 und dem Maximum eingeben.' : 'Erreichte Punkte eingeben';")
            source = re.sub(r'function fmtPts\(v\)\s*\{[^}]+\}', "function fmtPts(v) { return v.toLocaleString('de-DE', {maximumFractionDigits: 4}); }", source)

    def schema(match):
        data = json.loads(match.group(1))
        def walk(node):
            if isinstance(node, list):
                for value in node: walk(value)
            elif isinstance(node, dict):
                if isinstance(node.get('@type'), str) and node.get('@type') in {'SoftwareApplication','MobileApplication'}:
                    node['offers'] = [
                        {'@type':'Offer','name':'iPhone und iPad','price':'5.99','priceCurrency':'EUR','url':APPLE},
                        {'@type':'Offer','name':'Android','price':'0','priceCurrency':'EUR','url':PLAY}
                    ]
                    node.pop('aggregateRating', None)
                if node.get('@type') == 'Person' and node.get('name') == 'Jonah Röhl':
                    node['jobTitle'] = 'Entwickler'
                if 'dateModified' in node: node['dateModified'] = '2026-10-20'
                for value in node.values(): walk(value)
        walk(data)
        return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n  </script>'
    source = re.sub(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', schema, source, flags=re.S)

    # The navigation is deliberately platform-neutral, including on mobile.
    soup = BeautifulSoup(source, 'html.parser')
    if soup.select_one('a.nav-cta'):
        source = replace_element(source, 'a.nav-cta', '<a href="/#app-download" class="nav-cta" onclick="closeMenu()" aria-label="App für iPhone, iPad und Android">App</a>')
    if 'nav-app-mobile' not in source and soup.select_one('.nav-toggle'):
        source = re.sub(r'(<button\b[^>]*class="[^"]*nav-toggle[^>]*>)', '<a class="nav-app-mobile" href="/#app-download" aria-label="App für iPhone, iPad und Android">App</a>\n        '+r'\1', source, count=1)
    if '/assets/site-enhancements.css' not in source:
        source = source.replace('</head>', '  <link rel="stylesheet" href="/assets/site-enhancements.css?v=20261020">\n</head>')

    # One factual, platform-specific price line accompanies each download area.
    soup = BeautifulSoup(source, 'html.parser')
    for selector in ['.cta-banner-content', '.hero-actions', '.knick-cta-row']:
        node = soup.select_one(selector)
        if node and not node.select_one('.store-prices'):
            segment = source[sum(len(l) for l in source.splitlines(keepends=True)[:node.sourceline - 1]) + node.sourcepos:]
            # replace_element calculates the full extent, preserving untouched source.
            placeholder = '<!-- site-price-slot -->'
            interim = replace_element(source, selector, placeholder)
            end_length = len(source) - (len(interim) - len(placeholder))
            start = source.index(segment)
            original = source[start:start + end_length]
            insert_at = original.rfind('</')
            replacement = original[:insert_at] + '<p class="store-prices">'+PRICE_TEXT+'</p>\n' + original[insert_at:]
            source = interim.replace(placeholder, replacement, 1)
            soup = BeautifulSoup(source, 'html.parser')

    apple, play = store_links(campaign_for(path))
    # Only anchor hrefs are decorated: schema URLs and canonical URLs stay clean.
    def store_anchor(match):
        url = html.unescape(match.group(2))
        if 'apps.apple.com/' in url and '1662507346' in url: url = apple
        elif 'play.google.com/store/apps/details' in url and 'com.notenrechner.App' in url: url = play
        return match.group(1) + html.escape(url, quote=True) + match.group(3)
    source = re.sub(r'(<a\b[^>]*\bhref=")([^"]+)(")', store_anchor, source)
    return source

def write_page(path, source):
    path.write_text(normalize_html(source, path), encoding='utf-8')

if __name__ == '__main__':
    for path in ROOT.rglob('*.html'):
        if '.git' not in path.parts:
            write_page(path, path.read_text())
