"""Generates the Lexikon (glossary): /lexikon/ index + 6 entry pages.

Slugs:
  /lexikon/
  /lexikon/notenpunkte/
  /lexikon/notenschluessel/
  /lexikon/knick/
  /lexikon/bestehensgrenze/
  /lexikon/maximalpunktzahl/
  /lexikon/unterkurs/

Each entry is hand-curated below (definition, context, examples, related links).
Output: website/lexikon/<slug>/index.html plus website/lexikon/index.html
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "lexikon"

# ─────────────────────────────────────────────────────────────────────
# Entries — order matters (used for prev/next + index listing).
# ─────────────────────────────────────────────────────────────────────

ENTRIES = [
    {
        "slug": "notenpunkte",
        "title": "Notenpunkte",
        "h1": "Notenpunkte",
        "summary": "Das 16-stufige Punktesystem (15 bis 0) der gymnasialen Oberstufe. Genauere Bewertung als die klassischen Schulnoten 1 bis 6.",
        "meta": "Notenpunkte (15–0): Bedeutung, Umrechnung in Noten und Dezimalnoten, Anwendung in der gymnasialen Oberstufe und im Abitur.",
        "sections": [
            ("Was sind Notenpunkte?",
             "Notenpunkte sind das Bewertungssystem der gymnasialen Oberstufe in Deutschland. "
             "Statt der klassischen Schulnoten 1 bis 6 wird eine 16-stufige Skala von 15 (beste "
             "Leistung) bis 0 (ungenügend) verwendet. Jede der fünf Hauptnotenstufen wird in "
             "drei Bereiche unterteilt — Plus, glatt, Minus —, woraus sich insgesamt 16 Stufen "
             "ergeben."),
            ("Warum 15 Punkte und nicht 1 bis 6?",
             "Das Punktesystem ermöglicht eine feinere Differenzierung. Eine 2 kann je nach "
             "Tendenz 12, 11 oder 10 Notenpunkte bedeuten — drei voneinander unterscheidbare "
             "Leistungsstufen, die mit der Note „2 bis 3\" oder einfach „2\" sonst nicht "
             "präzise dargestellt werden könnten. Für die Abitur-Berechnung, in der "
             "Hunderte Klausurnoten zu einem Schnitt verrechnet werden, ist diese "
             "Granularität wichtig."),
            ("Umrechnung in Schulnoten und Dezimalnoten",
             "Jeder Notenpunkt entspricht genau einer Schulnote: 15 = 1+, 14 = 1, 13 = 1-, "
             "12 = 2+ und so weiter bis 0 = 6. Für die Dezimalnote — etwa für Hochschul-"
             "bewerbungen — gilt die Formel <em>Dezimalnote = (17 − Notenpunkte) / 3</em>. "
             "So entsprechen 14 NP der Dezimalnote 1,0, und 5 NP der Dezimalnote 4,0."),
            ("Wo werden Notenpunkte verwendet?",
             "Ausschließlich in der gymnasialen Oberstufe (Qualifikationsphase Q1 bis Q4). "
             "In der Sekundarstufe I, an Realschulen, Hauptschulen und Berufsschulen werden "
             "weiterhin die Schulnoten 1 bis 6 vergeben. Im Studium werden meist Dezimalnoten "
             "verwendet."),
        ],
        "related": [
            ("Notenpunkte-Tabelle (Tool)", "/notenpunkte-tabelle/"),
            ("Notenschlüssel", "/lexikon/notenschluessel/"),
            ("Bestehensgrenze", "/lexikon/bestehensgrenze/"),
            ("Unterkurs", "/lexikon/unterkurs/"),
        ],
    },
    {
        "slug": "notenschluessel",
        "title": "Notenschlüssel",
        "h1": "Notenschlüssel",
        "summary": "Die Vorschrift, wie erreichte Punkte in einer Klausur in Schulnoten oder Notenpunkte umgerechnet werden. Lehrkräfte legen ihn vor jeder Arbeit fest.",
        "meta": "Notenschlüssel: Definition, Arten (linear, mit Knick), Standardprozente und wie ein Notenschlüssel für eine Klausur erstellt wird.",
        "sections": [
            ("Was ist ein Notenschlüssel?",
             "Ein Notenschlüssel legt fest, ab wie vielen Prozent der erreichbaren Punkte "
             "welche Note vergeben wird. Er ist die Brücke zwischen den objektiven Klausur-"
             "Punkten und der subjektiv vergebenen Note. Lehrkräfte stellen ihn vor jeder "
             "Klausur fest und müssen ihn den Schülerinnen und Schülern in der Regel mit der "
             "Klausur transparent machen."),
            ("Standardprozente in der Oberstufe",
             "Drei Standard-Notenschlüssel sind weit verbreitet: der 50 %-Schlüssel (Note 4 "
             "ab 50 %), der 45 %-Schlüssel (Note 4 ab 45 %, etwas leichter) und der "
             "40 %-Schlüssel (Note 4 ab 40 %, deutlich entlasten­d). Welcher genutzt wird, "
             "entscheidet die Lehrkraft basierend auf Schwierigkeit und Bedeutung der Arbeit."),
            ("Linear oder mit Knick?",
             "Ein <strong>linearer Notenschlüssel</strong> verteilt die Punkte gleichmäßig über alle "
             "Noten. Ein <a href=\"/lexikon/knick/\">Notenschlüssel mit Knick</a> setzt zusätzlich "
             "eine Bestehensgrenze (Sockel), oberhalb derer die Notenstufen feiner abgestuft sind. "
             "Damit kann die Lehrkraft sicherstellen, dass eine bestandene 4 nicht zu eng an die "
             "5 grenzt — gerade bei schwierigen Klausuren."),
            ("Wie wird ein Notenschlüssel berechnet?",
             "Praktisch: Die Lehrkraft wählt einen Schlüssel (z. B. 50 %), bestimmt die "
             "Maximalpunktzahl der Klausur und berechnet daraus für jede Notenstufe (15 NP "
             "bis 0 NP) die Mindestpunktzahl. Wer 80 Punkte von 100 erreicht hat, liegt bei "
             "12 Notenpunkten (2+) — gemäß dem 50 %-Schlüssel. Mit dem "
             "<a href=\"/notenschluessel-rechner/\">Notenschlüssel-Rechner</a> geht das in Sekunden."),
        ],
        "related": [
            ("Notenschlüssel-Rechner (Tool)", "/notenschluessel-rechner/"),
            ("Knick im Notenschlüssel", "/lexikon/knick/"),
            ("Maximalpunktzahl", "/lexikon/maximalpunktzahl/"),
            ("Bestehensgrenze", "/lexikon/bestehensgrenze/"),
        ],
    },
    {
        "slug": "knick",
        "title": "Knick im Notenschlüssel",
        "h1": "Knick im Notenschlüssel",
        "summary": "Eine zusätzliche Stützstelle, an der der Notenschlüssel seine Steigung ändert — meist an der Bestehensgrenze. Macht schwierige Klausuren fairer.",
        "meta": "Knick im Notenschlüssel: Funktion, Beispiele und warum Lehrkräfte ihn bei Klausuren mit höherem Schwierigkeitsgrad einsetzen.",
        "sections": [
            ("Was bedeutet „Knick im Notenschlüssel\"?",
             "Ein Knick ist eine zusätzliche Stützstelle in der Notenkurve, an der die Steigung "
             "wechselt. Üblich ist ein Knick an der Bestehensgrenze (Note 4): unterhalb dieser "
             "Grenze verteilen sich die Notenstufen 4-, 5+, 5, 5-, 6 auf einen großzügigeren "
             "Punktebereich, oberhalb verlaufen die guten Noten linear bis zur 1+. Damit wird "
             "verhindert, dass eine noch knapp ausreichende Leistung sofort zur 5 wird."),
            ("Wozu dient der Knick?",
             "Ein linearer Schlüssel verteilt jede Notenstufe gleichmäßig — was bei einer "
             "schweren Klausur dazu führen kann, dass schon kleine Fehler die Note "
             "unverhältnismäßig stark drücken. Mit einem Knick „atmet\" der Schlüssel: "
             "Die Lehrkraft kann den Anspruch im oberen Bereich (1er- und 2er-Bereich) "
             "hochhalten und gleichzeitig im Bestehensbereich angemessen werten."),
            ("Beispiel mit Sockel von 50 % bei 100 Punkten",
             "Bei einem klassischen Knick liegt der Sockel — also die Bestehensgrenze für "
             "Note 4 — bei 50 % (50 von 100 Punkten). Von 0 bis 50 Punkten verteilen sich "
             "die fünf Notenstufen 4-, 5+, 5, 5- und 6. Von 50 bis 100 Punkten verteilen "
             "sich die zehn Notenstufen 4 bis 1+ — feiner abgestuft, jeder Punkt zählt mehr."),
            ("Wer entscheidet über den Knick?",
             "Die Lehrkraft. In manchen Bundesländern und Schulformen gibt es Empfehlungen "
             "der Schulaufsicht oder Vereinbarungen im Fachbereich, aber rechtlich liegt die "
             "Entscheidung über den konkreten Notenschlüssel bei der unterrichtenden Lehrkraft. "
             "Die App <em>Der Notenrechner</em> erstellt Notenschlüssel mit Knick in Sekunden."),
        ],
        "related": [
            ("Notenschlüssel", "/lexikon/notenschluessel/"),
            ("Bestehensgrenze", "/lexikon/bestehensgrenze/"),
            ("Notenschlüssel-Rechner", "/notenschluessel-rechner/"),
        ],
    },
    {
        "slug": "bestehensgrenze",
        "title": "Bestehensgrenze",
        "h1": "Bestehensgrenze",
        "summary": "Die Mindestpunktzahl, ab der eine Klausur mit Note 4 (ausreichend) bestanden ist. Üblich sind 50, 45 oder 40 Prozent.",
        "meta": "Bestehensgrenze in Schule und Oberstufe: Was bedeutet sie, welche Prozentwerte sind üblich, und wann gilt eine Klausur als bestanden?",
        "sections": [
            ("Was ist die Bestehensgrenze?",
             "Die Bestehensgrenze ist der Prozentwert, ab dem eine Klausur mit der Note 4 "
             "(ausreichend) bewertet wird. Wer diese Schwelle erreicht, hat die Arbeit "
             "bestanden. Wer darunterliegt, erhält eine 5 oder 6. In der gymnasialen "
             "Oberstufe entspricht die Bestehensgrenze 5 Notenpunkten."),
            ("Welche Werte sind üblich?",
             "Drei Standardwerte: <strong>50 %</strong> (klassisch, anspruchsvolle Klausuren), "
             "<strong>45 %</strong> (etwas entlastet, häufig) und <strong>40 %</strong> "
             "(stark entlastet, bei besonders schweren Arbeiten). Die Wahl liegt bei der "
             "Lehrkraft. Bei der IHK liegt die Bestehensgrenze für die meisten Prüfungen "
             "ebenfalls bei genau 50 %."),
            ("Was passiert bei Unterschreiten?",
             "In Klausurnoten: Wer unter der Bestehensgrenze liegt, erhält eine 5 oder 6. "
             "In der Oberstufe gilt der Kurs als „<a href=\"/lexikon/unterkurs/\">unterkurs</a>\" "
             "(unterpunktet), wenn die Halbjahresnote unter 5 NP fällt — mit Konsequenzen für "
             "die Abitur-Zulassung. Bei IHK-Prüfungen bedeutet ein Wert unter 50 % regulär: "
             "nicht bestanden — eventuell mit Möglichkeit zur Wiederholung."),
            ("Bestehensgrenze und Knick",
             "An der Bestehensgrenze setzen Lehrkräfte häufig einen "
             "<a href=\"/lexikon/knick/\">Knick im Notenschlüssel</a>. Damit lässt sich der "
             "Bestehensbereich großzügiger gestalten, ohne den Anspruch in den oberen Noten "
             "abzusenken."),
        ],
        "related": [
            ("Notenschlüssel", "/lexikon/notenschluessel/"),
            ("Knick", "/lexikon/knick/"),
            ("Unterkurs", "/lexikon/unterkurs/"),
            ("IHK-Notenschlüssel", "/ihk-notenschluessel/"),
        ],
    },
    {
        "slug": "maximalpunktzahl",
        "title": "Maximalpunktzahl",
        "h1": "Maximalpunktzahl",
        "summary": "Die höchste in einer Klausur erreichbare Punktzahl — die Basis für jeden Notenschlüssel. Üblich sind 100, 60, 30 oder andere Werte.",
        "meta": "Maximalpunktzahl in Klausuren: Definition, übliche Werte und wie sie für die Notenberechnung genutzt wird.",
        "sections": [
            ("Was bedeutet Maximalpunktzahl?",
             "Die Maximalpunktzahl ist die höchste Punktzahl, die in einer Klausur theoretisch "
             "erreichbar ist. Sie ergibt sich aus der Summe aller Aufgabenwerte. Eine Klausur "
             "kann zum Beispiel aus drei Aufgaben mit 30, 40 und 30 Punkten bestehen — die "
             "Maximalpunktzahl wäre 100."),
            ("Welche Werte sind üblich?",
             "100 Punkte ist klassisch und ermöglicht eine direkte Prozentablesung. Aber auch "
             "60 (für 60 Minuten Klausurzeit), 30, 50 oder krumme Werte wie 47 sind häufig — "
             "abhängig von Aufgabengestaltung und Schwierigkeit. Bei Abiturklausuren werden "
             "in einigen Bundesländern feste Maximalwerte vorgegeben."),
            ("Maximalpunktzahl und Notenschlüssel",
             "Ohne Maximalpunktzahl gibt es keinen sinnvollen Notenschlüssel. Aus der "
             "Maximalpunktzahl und dem gewählten <a href=\"/lexikon/notenschluessel/\">"
             "Notenschlüssel</a> (z. B. 50 %) ergeben sich die Mindestpunktzahlen für jede "
             "Note. Wer 80 von 100 Punkten erreicht (80 %), liegt im 50er-Schlüssel bei der "
             "Note 2+ (12 NP)."),
            ("Halbe Punkte erlaubt?",
             "Ja — halbe Punkte sind in vielen Klausuren üblich. Die Maximalpunktzahl darf "
             "krumm sein (z. B. 56,5). Notenschlüssel-Rechner wie der von <em>Der Notenrechner</em> "
             "rechnen mit Dezimalwerten."),
        ],
        "related": [
            ("Notenschlüssel", "/lexikon/notenschluessel/"),
            ("Notenschlüssel-Rechner", "/notenschluessel-rechner/"),
            ("Bestehensgrenze", "/lexikon/bestehensgrenze/"),
        ],
    },
    {
        "slug": "unterkurs",
        "title": "Unterkurs (unterpunktet)",
        "h1": "Unterkurs",
        "summary": "Ein Kurs in der Oberstufe, in dem die Halbjahresnote unter 5 Notenpunkten liegt — also nicht bestanden. Hat Konsequenzen für die Abi-Zulassung.",
        "meta": "Unterkurs / unterpunktet: Definition, wie viele Unterkurse im Abitur erlaubt sind und welche Konsequenzen drohen.",
        "sections": [
            ("Was ist ein Unterkurs?",
             "Ein Unterkurs (auch: „unterpunktet\") ist ein Kurs in der gymnasialen Oberstufe, "
             "in dem die Halbjahresnote unter 5 Notenpunkten liegt. 5 NP entspricht der "
             "Note 4 (ausreichend) — wer also weniger als ausreichend abschließt, hat den "
             "Kurs unterkurs."),
            ("Welche Notenpunkte zählen als unterkurs?",
             "Alle Noten von 4 NP bis 0 NP gelten als unterkurs. Konkret: 4 NP (4-), 3 NP "
             "(5+), 2 NP (5), 1 NP (5-) und 0 NP (6). Eine glatte 4 (5 NP) ist gerade noch "
             "bestanden — kein Unterkurs."),
            ("Wie viele Unterkurse sind im Abitur erlaubt?",
             "Die Regelung variiert nach Bundesland. Üblich sind in der Qualifikationsphase "
             "höchstens 7 oder 8 Unterkurse von rund 36 bis 40 anrechenbaren Kursen — bei "
             "Überschreitung droht Nichtzulassung zur Abiturprüfung. In den Abiturprüfungen "
             "selbst gelten zusätzlich strengere Regeln (mindestens 5 Punkte in mindestens "
             "drei Prüfungsfächern). Bitte direkt bei der Oberstufenkoordination nachfragen."),
            ("Konsequenzen eines Unterkurses",
             "Über einen einzelnen Unterkurs muss man sich nicht sorgen — solange das "
             "Bundeslandlimit nicht überschritten wird. Mehrfach unterpunktete Kurse, "
             "insbesondere in Leistungsfächern, können aber dazu führen, dass die Q-Phase "
             "nicht abgeschlossen werden kann oder das Abitur gefährdet ist."),
        ],
        "related": [
            ("Bestehensgrenze", "/lexikon/bestehensgrenze/"),
            ("Notenpunkte", "/lexikon/notenpunkte/"),
            ("Notenpunkte-Tabelle", "/notenpunkte-tabelle/"),
        ],
    },
]


# ─────────────────────────────────────────────────────────────────────
# Shared CSS — same v3 Neutral Workbench tokens
# ─────────────────────────────────────────────────────────────────────

CSS = dedent("""
:root {
  --primary: #2F60C0; --primary-light: #6B94E0; --primary-dark: #1F4A9C;
  --primary-50: #EEF3FB; --primary-100: #DCE5F5; --primary-900: #15336B;
  --bg: #F7F6F3; --card: #FFFFFF; --surface-subtle: #F1EFEA;
  --text: #0F0F10; --text-secondary: #3B3B3F; --text-muted: #6E6E73;
  --border: #E8E6E1; --border-light: #F1EFEA;
  --shadow-card: 0 1px 2px rgba(15,15,16,0.04), 0 0 0 1px rgba(15,15,16,0.04);
  --radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --radius-pill: 999px;
  --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --nav-height: 72px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font); color: var(--text); background: var(--bg); line-height: 1.6; -webkit-font-smoothing: antialiased; }
a { color: inherit; text-decoration: none; }
button { font-family: inherit; cursor: pointer; border: none; background: none; }
:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: 4px; }

.nav { position: fixed; top: 0; left: 0; right: 0; height: var(--nav-height); z-index: 1000; }
.nav::before { content: ''; position: absolute; inset: 0; background: rgba(255,255,255,0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); box-shadow: 0 1px 0 var(--border); z-index: -1; }
.nav-inner { max-width: 1120px; margin: 0 auto; padding: 0 24px; height: 100%; display: flex; align-items: center; justify-content: space-between; }
.nav-brand { font-size: 18px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 10px; z-index: 1001; }
.nav-brand-icon { width: 32px; height: 32px; border-radius: var(--radius-sm); overflow: hidden; flex-shrink: 0; }
.nav-brand-icon img { width: 100%; height: 100%; object-fit: cover; }
.nav-links { display: flex; align-items: center; gap: 28px; list-style: none; }
.nav-links a { font-size: 15px; font-weight: 500; color: var(--text-secondary); transition: color 0.2s; padding: 8px 0; min-height: 44px; display: flex; align-items: center; }
.nav-links a:hover { color: var(--primary); }
.nav-links a.active { color: var(--primary); font-weight: 600; }
.nav-links a.nav-cta { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 0 22px 0 18px; height: 36px; min-height: 0; line-height: 1; white-space: nowrap; background: var(--primary); color: white !important; border-radius: var(--radius-pill); font-size: 15px; font-weight: 700; transition: background 0.15s, transform 0.15s; }
.nav-links a.nav-cta svg { width: 13px; height: 15px; flex-shrink: 0; display: block; }
.nav-links a.nav-cta:hover { background: var(--primary-dark); color: white !important; transform: translateY(-1px); }
.nav-toggle { display: none; flex-direction: column; gap: 5px; padding: 10px; min-width: 44px; min-height: 44px; justify-content: center; align-items: center; z-index: 1001; }
.nav-toggle span { display: block; width: 22px; height: 2px; background: var(--text); border-radius: 2px; transition: transform 0.3s, opacity 0.3s; }
.nav-toggle.active span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.nav-toggle.active span:nth-child(2) { opacity: 0; }
.nav-toggle.active span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
@media (max-width: 768px) {
  .nav-toggle { display: flex; }
  .nav-links { position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 999; background: rgba(255,255,255,0.98); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); flex-direction: column; justify-content: center; gap: 24px; opacity: 0; pointer-events: none; transition: opacity 0.3s; }
  .nav-links.open { opacity: 1; pointer-events: all; }
  .nav-links a { font-size: 20px; font-weight: 600; }
  .nav-links a.nav-cta { height: 46px; padding: 0 30px 0 26px; font-size: 17px; gap: 10px; }
  .nav-links a.nav-cta svg { width: 15px; height: 17px; }
}

.container { max-width: 1120px; margin: 0 auto; padding: 0 24px; }

/* HERO (entry & index) */
.lex-hero { padding-top: calc(var(--nav-height) + 48px); padding-bottom: 40px; background: linear-gradient(180deg, var(--bg) 0%, #FBFAF6 100%); border-bottom: 1px solid var(--border); }
.breadcrumbs { font-size: 13px; color: var(--text-muted); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.breadcrumbs a { color: var(--text-secondary); transition: color 0.15s; }
.breadcrumbs a:hover { color: var(--primary); }
.breadcrumbs span[aria-current] { color: var(--text); font-weight: 500; }

.lex-eyebrow { display: inline-block; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--primary); margin-bottom: 14px; }
.lex-h1 { font-size: clamp(28px, 4.5vw, 44px); font-weight: 800; letter-spacing: -0.025em; line-height: 1.15; margin-bottom: 14px; max-width: 720px; }
.lex-summary { font-size: 18px; color: var(--text-secondary); max-width: 680px; line-height: 1.6; }

/* ENTRY content */
.lex-content { padding: 56px 0 72px; }
.lex-prose { max-width: 720px; }
.lex-prose h2 { font-size: 22px; font-weight: 700; margin-top: 36px; margin-bottom: 12px; letter-spacing: -0.01em; }
.lex-prose h2:first-child { margin-top: 0; }
.lex-prose p { font-size: 16px; line-height: 1.75; color: var(--text-secondary); margin-bottom: 14px; }
.lex-prose strong { color: var(--text); font-weight: 600; }
.lex-prose em { font-style: normal; color: var(--text); font-weight: 500; background: var(--primary-50); padding: 1px 5px; border-radius: 4px; }
.lex-prose a { color: var(--primary); font-weight: 500; text-decoration: underline; text-underline-offset: 3px; }
.lex-prose a:hover { color: var(--primary-dark); }

/* RELATED (entry footer block) */
.lex-related { max-width: 720px; margin-top: 48px; padding: 24px 28px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-lg); }
.lex-related-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 14px; }
.lex-related-list { display: flex; gap: 10px; flex-wrap: wrap; }
.lex-related-link { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius-pill); font-size: 14px; font-weight: 500; color: var(--text); transition: border-color 0.2s, transform 0.15s; }
.lex-related-link:hover { border-color: var(--primary); transform: translateY(-1px); color: var(--primary); }
.lex-related-link::before { content: '›'; color: var(--primary); font-weight: 700; margin-right: 2px; }

/* INDEX list */
.lex-index-grid { display: grid; gap: 16px; max-width: 760px; margin: 56px 0 72px; grid-template-columns: 1fr; }
@media (min-width: 720px) { .lex-index-grid { grid-template-columns: 1fr 1fr; } }
.lex-card { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 22px 24px 20px; transition: border-color 0.2s, transform 0.15s, box-shadow 0.2s; display: block; }
.lex-card:hover { border-color: var(--primary-100); transform: translateY(-1px); box-shadow: 0 4px 16px rgba(47,96,192,0.06); }
.lex-card-title { font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 6px; letter-spacing: -0.01em; }
.lex-card-summary { font-size: 14px; color: var(--text-secondary); line-height: 1.55; }

/* CTA */
.cta-banner { background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%); color: white; text-align: center; padding: 64px 24px; position: relative; overflow: hidden; }
.cta-banner::before { content: ''; position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px); background-size: 24px 24px; }
.cta-banner-content { position: relative; z-index: 1; max-width: 640px; margin: 0 auto; }
.cta-banner h2 { font-size: clamp(22px, 3.5vw, 28px); font-weight: 800; margin-bottom: 10px; letter-spacing: -0.02em; }
.cta-banner-sub { font-size: 15px; color: rgba(255,255,255,0.9); margin-bottom: 28px; }
.app-store-badge { display: inline-flex; align-items: center; gap: 12px; padding: 10px 22px 10px 18px; border-radius: 12px; min-height: 52px; background: #000; color: white; transition: transform 0.2s, box-shadow 0.2s; }
.app-store-badge:hover { transform: translateY(-2px); background: #1a1a1a; box-shadow: 0 10px 28px rgba(0,0,0,0.35); }
.app-store-badge-icon { width: 28px; height: 28px; flex-shrink: 0; }
.app-store-badge-icon svg { width: 100%; height: 100%; fill: currentColor; }
.app-store-badge-text { display: flex; flex-direction: column; line-height: 1; }
.app-store-badge-small { font-size: 11px; opacity: 0.9; margin-bottom: 4px; }
.app-store-badge-large { font-size: 20px; font-weight: 600; letter-spacing: -0.01em; }

.footer { background: var(--surface-subtle); padding: 36px 24px; border-top: 1px solid var(--border); }
.footer-inner { max-width: 1120px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.footer-links { display: flex; gap: 24px; list-style: none; flex-wrap: wrap; justify-content: center; }
.footer-links a { font-size: 14px; color: var(--text-secondary); transition: color 0.2s; }
.footer-links a:hover { color: var(--primary); }
.footer-tagline { font-size: 13px; color: var(--text-muted); font-style: italic; }
.footer-copy { font-size: 13px; color: var(--text-muted); }
""")


NAV_HTML = """  <nav class="nav" role="navigation" aria-label="Hauptnavigation">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><span class="nav-brand-icon"><img src="/assets/logo.png" alt=""></span>Der Notenrechner</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/" onclick="closeMenu()">Startseite</a></li>
        <li><a href="/notenschluessel-rechner/" onclick="closeMenu()">Notenschlüssel-Rechner</a></li>
        <li><a href="/notenpunkte-tabelle/" onclick="closeMenu()">Notenpunkte-Tabelle</a></li>
        <li><a href="/ihk-notenschluessel/" onclick="closeMenu()">IHK-Rechner</a></li>
        <li><a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="nav-cta" onclick="closeMenu()" aria-label="Im App Store laden"><svg viewBox="0 0 384 512" fill="currentColor" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>Laden</a></li>
      </ul>
    </div>
  </nav>"""

CTA_BANNER = """    <section class="cta-banner">
      <div class="cta-banner-content">
        <h2>Klausuren bewerten, Klassen führen, Zeugnisse berechnen.</h2>
        <p class="cta-banner-sub">Der Notenrechner — kostenlos im App Store. Lokal, ohne Account, ohne Werbung.</p>
        <a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="app-store-badge">
          <span class="app-store-badge-icon"><svg viewBox="0 0 384 512"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg></span>
          <span class="app-store-badge-text"><span class="app-store-badge-small">Laden im</span><span class="app-store-badge-large">App Store</span></span>
        </a>
      </div>
    </section>"""

FOOTER = """  <footer class="footer">
    <div class="footer-inner">
      <ul class="footer-links">
        <li><a href="/#datenschutz">Datenschutz</a></li>
        <li><a href="/#impressum">Impressum</a></li>
        <li><a href="https://instagram.com/notenrechnerapp" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
      <div class="footer-tagline">Entwickelt von einem Lehrer, für Lehrkräfte</div>
      <div class="footer-copy">&copy; 2026 Der Notenrechner. Alle Rechte vorbehalten.</div>
    </div>
  </footer>
  <script>
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    navToggle.addEventListener('click', () => {
      const open = !navLinks.classList.contains('open');
      navToggle.classList.toggle('active', open);
      navLinks.classList.toggle('open', open);
      navToggle.setAttribute('aria-expanded', String(open));
    });
    function closeMenu() { navToggle.classList.remove('active'); navLinks.classList.remove('open'); navToggle.setAttribute('aria-expanded', 'false'); }
  </script>"""


# ─────────────────────────────────────────────────────────────────────
# Render helpers
# ─────────────────────────────────────────────────────────────────────

def head(title, meta_desc, canonical, breadcrumb_label=None):
    bc_block = ""
    if breadcrumb_label:
        bc_block = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Der Notenrechner", "item": "https://notenrechnerapp.de/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Lexikon", "item": "https://notenrechnerapp.de/lexikon/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{breadcrumb_label}", "item": "{canonical}" }}
    ]
  }}
  </script>"""
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="Der Notenrechner">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="theme-color" content="#2F60C0">
  <meta name="apple-itunes-app" content="app-id=1662507346">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="de" href="{canonical}">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">{bc_block}
  <style>{CSS}</style>
</head>"""


def render_entry(entry):
    canonical = f"https://notenrechnerapp.de/lexikon/{entry['slug']}/"
    title = f"{entry['title']} — Lexikon | Der Notenrechner"
    sections_html = "\n          ".join(
        f"<h2>{h}</h2>\n          <p>{p}</p>" for h, p in entry["sections"]
    )
    related_html = "\n          ".join(
        f'<a class="lex-related-link" href="{href}">{label}</a>'
        for label, href in entry["related"]
    )
    return f"""{head(title, entry['meta'], canonical, entry['title'])}
<body>
{NAV_HTML}
  <main>
    <section class="lex-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Brotkrumen">
          <a href="/">Start</a>
          <span aria-hidden="true">›</span>
          <a href="/lexikon/">Lexikon</a>
          <span aria-hidden="true">›</span>
          <span aria-current="page">{entry['title']}</span>
        </nav>
        <span class="lex-eyebrow">Lexikon</span>
        <h1 class="lex-h1">{entry['h1']}</h1>
        <p class="lex-summary">{entry['summary']}</p>
      </div>
    </section>

    <section class="lex-content">
      <div class="container">
        <article class="lex-prose">
          {sections_html}
        </article>

        <aside class="lex-related" aria-label="Verwandt">
          <div class="lex-related-title">Verwandt</div>
          <div class="lex-related-list">
          {related_html}
          </div>
        </aside>
      </div>
    </section>

{CTA_BANNER}
  </main>

{FOOTER}
</body>
</html>"""


def render_index():
    canonical = "https://notenrechnerapp.de/lexikon/"
    title = "Lexikon — Begriffe rund um Noten und Notenschlüssel | Der Notenrechner"
    meta = "Notenpunkte, Notenschlüssel, Knick, Bestehensgrenze, Maximalpunktzahl, Unterkurs — kompakte Definitionen für Schule, Oberstufe und Ausbildung."
    cards_html = "\n          ".join(
        f'''<a class="lex-card" href="/lexikon/{e['slug']}/">
            <div class="lex-card-title">{e['title']}</div>
            <div class="lex-card-summary">{e['summary']}</div>
          </a>'''
        for e in ENTRIES
    )
    return f"""{head(title, meta, canonical)}
<body>
{NAV_HTML}
  <main>
    <section class="lex-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Brotkrumen">
          <a href="/">Start</a>
          <span aria-hidden="true">›</span>
          <span aria-current="page">Lexikon</span>
        </nav>
        <span class="lex-eyebrow">Lexikon</span>
        <h1 class="lex-h1">Begriffe rund um Noten und Notenschlüssel.</h1>
        <p class="lex-summary">Kompakte Definitionen für Lehrkräfte, Schülerinnen und Schüler — von Notenpunkten bis Bestehensgrenze. Alle Einträge sind sauber miteinander verlinkt und verweisen auf die passenden Rechner.</p>
      </div>
    </section>

    <section class="lex-content">
      <div class="container">
        <div class="lex-index-grid">
          {cards_html}
        </div>
      </div>
    </section>

{CTA_BANNER}
  </main>

{FOOTER}
</body>
</html>"""


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")
    print("  wrote /lexikon/index.html")
    for entry in ENTRIES:
        d = OUT / entry["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render_entry(entry), encoding="utf-8")
        print(f"  wrote /lexikon/{entry['slug']}/index.html")


if __name__ == "__main__":
    main()
