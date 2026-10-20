"""Validate static publication, real local links, store attribution and inline JS."""
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote, parse_qs
from collections import Counter
import json
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://notenrechnerapp.de/'
GROUPS = {'regional_calculators', 'general_calculators', 'app_pages'}
errors = []

def check(condition, message):
    if not condition: errors.append(message)

ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [node.text for node in ET.parse(ROOT / 'sitemap.xml').findall('s:url/s:loc', ns)]
check(len(urls) == len(set(urls)), 'Duplicate sitemap URLs')
for url in urls:
    target = ROOT / urlparse(url).path.lstrip('/') / 'index.html'
    check(target.exists(), f'Sitemap target missing: {url}')
    if not target.exists(): continue
    source = target.read_text()
    soup = BeautifulSoup(source, 'html.parser')
    relative = target.relative_to(ROOT)
    check(len(soup.select('h1')) == 1, f'{relative}: expected one H1')
    canonical = soup.select_one('link[rel="canonical"]')
    check(canonical is not None and canonical.get('href') == url, f'{relative}: incorrect canonical')
    counts = Counter(node['id'] for node in soup.select('[id]'))
    check(all(n == 1 for n in counts.values()), f'{relative}: duplicate element IDs')
    for node in soup.select('a[href], img[src], script[src], link[rel="stylesheet"]'):
        href = node.get('href') or node.get('src')
        parsed = urlparse(urljoin(url, href))
        if parsed.netloc != 'notenrechnerapp.de': continue
        local = ROOT / unquote(parsed.path.lstrip('/'))
        if local.is_dir(): local /= 'index.html'
        check(local.exists(), f'{relative}: broken internal target {href}')
        if parsed.fragment and local.exists() and local.suffix == '.html':
            fragment_soup = BeautifulSoup(local.read_text(), 'html.parser')
            check(fragment_soup.find(id=unquote(parsed.fragment)) is not None, f'{relative}: missing anchor {href}')
    for script in soup.select('script:not([src])'):
        text = script.string or script.get_text()
        if script.get('type') == 'application/ld+json':
            data = json.loads(text)
            def walk(node):
                if isinstance(node, list):
                    for item in node: walk(item)
                elif isinstance(node, dict):
                    if isinstance(node.get('@type'),str) and node.get('@type') in {'SoftwareApplication','MobileApplication'}:
                        offers = node.get('offers',[])
                        check(isinstance(offers,list), f'{relative}: missing platform-specific offers')
                        if isinstance(offers,list):
                            check({str(o.get('price')) for o in offers} == {'0','5.99'}, f'{relative}: incorrect platform prices')
                    for value in node.values(): walk(value)
            walk(data)
        else:
            with tempfile.NamedTemporaryFile(mode='w',suffix='.js') as handle:
                handle.write(text);handle.flush()
                result = subprocess.run(['node','--check',handle.name],capture_output=True,text=True)
                check(result.returncode == 0,f'{relative}: invalid inline JavaScript: {result.stderr[:120]}')
    for anchor in soup.select('a[href]'):
        parsed=urlparse(anchor['href']);params=parse_qs(parsed.query)
        if parsed.netloc == 'apps.apple.com' and '1662507346' in parsed.path:
            check(params.get('pt') == ['125935959'] and params.get('ct',[None])[0] in GROUPS,f'{relative}: incorrect Apple campaign')
        if parsed.netloc == 'play.google.com' and params.get('id') == ['com.notenrechner.App']:
            ref=parse_qs(params.get('referrer',[''])[0])
            check(ref.get('utm_source') == ['notenrechnerapp.de'] and ref.get('utm_campaign',[None])[0] in GROUPS,f'{relative}: incorrect Play campaign')
    if soup.select_one('#tableBody') and 'const PRESETS' in source:
        check(len(soup.select('#tableBody tr')) == 16, f'{relative}: no initial preset table')
    if url.endswith('/notenpunkte-tabelle/'):
        check(len(soup.select('#mainTable tr')) == 16, 'Missing static 15–0 table')

if errors:
    for error in errors: print(error)
    raise SystemExit(f'{len(errors)} validation errors')
print(f'{len(urls)} sitemap pages validated: headings, canonicals, anchors, assets, schema, campaigns, initial tables and inline JavaScript.')
