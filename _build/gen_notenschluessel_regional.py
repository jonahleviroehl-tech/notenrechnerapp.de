"""Generates per-Bundesland Notenschlüssel clusters.

Currently in scope:
- Bayern: 1 hub + 4 Schulform sub-pages (Gymnasium, Grundschule, Realschule, Berufsschule)
  Targets: notenschlüssel bayern (4,400/mo) + Schulform variants
- NRW: 1 hub + 2 Schulform sub-pages (Grundschule, Gymnasium)
  Targets: notenschlüssel nrw grundschule (1,000/mo) + notenschlüssel nrw (260/mo) + nrw gymnasium (260/mo)
  Per Track E DataForSEO research: Realschule/Gesamtschule/Hauptschule have <10 vol — skipped.

Output: website/notenschluessel-rechner/<bundesland>/[index.html, <schulform>/index.html, ...]

Visual template mirrors `_build/gen_ihk_regional.py` (same hero, calc card,
content prose, CTA). The calculator is the school Notenschlüssel (50/45/40 %),
not the IHK one.

Each page has:
- Working Notenschlüssel calculator (PRESETS mirrored from /notenschluessel-rechner/)
- Schulform-specific intro
- Schulform-specific Bundesland context (Schulordnung references)
- Internal links to other Schulform sub-pages + pillar + main hub
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent
OUT_BASE = ROOT / "notenschluessel-rechner"

DATE_PUBLISHED = "2026-05-24"
DATE_MODIFIED = "2026-05-24"


BAYERN_PAGES = [
    {
        "slug": "",  # pillar at /notenschluessel-rechner/bayern/
        "schulform": None,
        "title_h1": ("Notenschlüssel ", "Bayern"),
        "page_title": "Notenschlüssel Bayern — Rechner für Gymnasium, Real-, Grund- und Berufsschule | Der Notenrechner",
        "meta_desc": "Notenschlüssel für bayerische Schulen — Punkte sofort in Note umrechnen. 50/45/40 %-Schlüssel, auch mit Knick. Pro Schulform: Gymnasium, Grundschule, Realschule, Berufsschule.",
        "summary": "Bayern hat keinen eigenen, landesweit verbindlichen Notenschlüssel — die Bestehensgrenze legt die Lehrkraft im Rahmen der jeweiligen Schulordnung fest. Die drei gebräuchlichsten Varianten 50/45/40 % sind unten direkt rechenbar; pro Schulform finden Sie weiter unten Bayern-spezifische Hinweise.",
        "default_preset": "50",
        "default_max": "60",
        "intro_h2": "Notenschlüssel in Bayern: was ist geregelt, was nicht?",
        "intro_body": [
            "Der Notenschlüssel — also die Vorschrift, wie erreichte Punkte einer Klausur in eine Schulnote umgerechnet werden — ist in Bayern <strong>kein landesweit einheitlicher Wert</strong>. Geregelt sind die <em>Notendefinitionen</em> (Art.&nbsp;52 BayEUG: 1 = sehr gut, 2 = gut, …, 6 = ungenügend) und die <em>Bestehensgrenzen für Abschlussprüfungen</em>, nicht aber der Schlüssel für reguläre Klausuren.",
            "Im Klassenraum entscheidet die Fachlehrkraft, an welchem Prozentwert die Note 4 beginnt — oft 50&nbsp;%, in einigen Schulformen 45 oder 40&nbsp;%. Auch der lineare Verlauf zwischen Note 1 und Note 4 (mit oder ohne <a href=\"/lexikon/knick/\">Knick</a>) wird schulintern festgelegt. Der Rechner oben zeigt die drei gängigen Varianten — wählen Sie unten Ihre Schulform aus für detailliertere Hinweise.",
        ],
        "section_h2": "Bayern nach Schulform",
        "section_intro": "Wechseln Sie zu Ihrer Schulform — jede Unterseite enthält die einschlägige Schulordnung, gebräuchliche Bestehensgrenzen und Hinweise zur Notenpunkte-Umrechnung in der Oberstufe.",
        "show_subpage_cards": True,
        "subpage_notes": True,
        "context_h2": "Was unterscheidet die bayerische Notengebung?",
        "context_body": [
            "Bayern verwendet wie alle Bundesländer die KMK-konforme Notenskala 1–6 sowie in der Qualifikationsphase der Oberstufe (Q11/Q12) das Notenpunktesystem 15–0. Pädagogische Besonderheiten:",
            "<strong>Mündliche und schriftliche Leistungen</strong> werden in den meisten Fächern getrennt erhoben und mit fachschaftlich beschlossener Gewichtung in die Halbjahresnote eingebracht. Die genauen Anteile stehen im schulinternen Curriculum.",
            "<strong>Schulaufgaben vs. Stegreifaufgaben</strong>: Bayerische Gymnasien und Realschulen unterscheiden große Leistungserhebungen (Schulaufgaben — ein bis vier pro Halbjahr) von kurzen unangekündigten (Stegreifaufgaben). Schulaufgaben gehen typischerweise höher gewichtet in die Note ein, der Schlüssel wird aber für beide gleich angewendet.",
            "<strong>Probezeit und Vorrücken</strong>: Versetzungsregeln folgen der jeweiligen Schulordnung (GSO, RSO, MSO, BSO). Sie betreffen den Notendurchschnitt am Jahresende — nicht den Schlüssel selbst.",
        ],
        "faq": [
            ("Gibt es einen offiziellen bayerischen Notenschlüssel für Klausuren?", "Nein. Der Schlüssel wird schulintern bzw. fachschaftlich festgelegt. Geregelt sind nur die Notendefinitionen (Art.&nbsp;52 BayEUG) und die Bestehensgrenzen bei Abschlussprüfungen."),
            ("Welcher Schlüssel wird in Bayern am häufigsten verwendet?", "Am Gymnasium (Sek&nbsp;I und Oberstufe) sehr häufig der 50-%-Schlüssel — die Note 4 beginnt bei 50&nbsp;% der Maximalpunktzahl. An Real- und Berufsschulen kommt auch der 45-%-Schlüssel vor. An Grundschulen ist die Bandbreite größer (40–50&nbsp;%)."),
            ("Was bedeutet „Knick im Notenschlüssel\"?", "Ein Knick verschiebt die Punktstaffelung an der Bestehensgrenze (Note 4) — die Steigung der Geraden ändert sich. Dadurch fällt eine knapp bestandene Klausur weniger steil ab und die Verteilung im 4er-Bereich wird differenzierter. Details im <a href=\"/lexikon/knick/\">Lexikoneintrag Knick</a>."),
            ("Welcher Schlüssel gilt für das bayerische Abitur?", "Für die schriftliche Abiturprüfung gibt es bundesweit abgestimmte Korrekturanweisungen; in Bayern werden Punkte aus den Aufgaben gemäß ISB-Korrekturhilfen in Notenpunkte (0–15) umgerechnet. Für die Gesamtqualifikation siehe <a href=\"/lexikon/notenpunkte/\">Lexikon: Notenpunkte</a>."),
        ],
    },
    {
        "slug": "gymnasium",
        "schulform": "Gymnasium",
        "title_h1": ("Notenschlüssel Bayern ", "Gymnasium"),
        "page_title": "Notenschlüssel Bayern Gymnasium — Klausur in Note umrechnen | Der Notenrechner",
        "meta_desc": "Notenschlüssel für bayerische Gymnasien — Schulaufgabe oder Stegreifaufgabe in Note umrechnen. 50/45 %-Schlüssel mit Knick. Sek&nbsp;I (1–6) und Oberstufe (15–0 Notenpunkte).",
        "summary": "Am bayerischen Gymnasium gilt ein in der GSO geregelter Rahmen: Notenskala 1–6 in Sek&nbsp;I, Notenpunkte 15–0 in der Oberstufe (Q11/Q12). Der konkrete Schlüssel für Schulaufgaben und Stegreifaufgaben wird fachschaftlich festgelegt — meist 50&nbsp;% Bestehensgrenze.",
        "default_preset": "50",
        "default_max": "60",
        "intro_h2": "Notengebung am bayerischen Gymnasium",
        "intro_body": [
            "Die <strong>Schulordnung für die Gymnasien in Bayern (GSO)</strong> definiert in §§&nbsp;28–30 die Grundlagen der Leistungserhebung. In der Sek&nbsp;I (Jgst.&nbsp;5–10) werden Ziffernnoten 1–6 vergeben; in der Qualifikationsphase (Q11/Q12) das Notenpunktesystem 15–0 — drei Notenpunkte entsprechen einer Notenstufe. Hintergrund im <a href=\"/lexikon/notenpunkte/\">Lexikon: Notenpunkte</a>.",
            "Der Schlüssel selbst — also wie viel Prozent für welche Note nötig sind — ist <em>nicht</em> in der GSO festgelegt. Üblich ist der lineare 50-%-Schlüssel (Note&nbsp;4 ab 50&nbsp;% der Maximalpunktzahl), optional mit <a href=\"/lexikon/knick/\">Knick</a> an der Bestehensgrenze für eine gerechte Verteilung im 4er-Bereich.",
        ],
        "section_h2": "Schulaufgabe oder Stegreifaufgabe — was zählt wie?",
        "section_intro_body": [
            "Bayerische Gymnasien unterscheiden zwei Hauptformen schriftlicher Leistungserhebung:",
            "<strong>Schulaufgaben</strong> sind die großen, angekündigten Klausuren — pro Halbjahr meist ein bis vier je Fach. Sie zählen in der Regel höher (oft doppelt oder zweidrittel) als die übrigen Noten. Im Notenschlüssel selbst gibt es keinen Unterschied — der Schlüssel ist derselbe wie für Stegreifaufgaben.",
            "<strong>Stegreifaufgaben (\"Exen\")</strong> sind kurze, unangekündigte Lernzielkontrollen zu den vergangenen ein bis zwei Stunden. Sie fließen in den Bereich der mündlichen / sonstigen Noten ein. Maximalpunktzahl typischerweise 10–20.",
            "Sowohl Schulaufgaben als auch Stegreifaufgaben werden in der Regel mit demselben Schlüssel (oft 50&nbsp;% lineare Bestehensgrenze) umgerechnet. Die <em>Gewichtung</em> für die Halbjahresnote ist sogenannte „Mathematik\" der jeweiligen Fachschaft.",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Oberstufe: Notenpunkte 15–0",
        "context_body": [
            "In Q11 und Q12 wird mit Notenpunkten gerechnet — eine Klausurleistung wird zunächst in Prozent erfasst und dann gemäß dem im Fach beschlossenen Schlüssel in die Skala 0–15 abgebildet. Die ISB-Korrekturhilfen für Abitur-relevante Klausuren geben Punktverteilungen pro Aufgabe vor, der Schlüssel wird darüber gelegt.",
            "Wichtig: Ein Halbjahr mit 0 Notenpunkten gilt als nicht erbracht; ein Halbjahr mit weniger als 5 Notenpunkten ist ein <a href=\"/lexikon/unterkurs/\">Unterkurs</a> und zählt für die Belegungspflicht der Qualifikationsphase mit Einschränkungen.",
            "Praktisch heißt das: Wer eine Klausur mit 60&nbsp;% der Maximalpunkte schreibt, landet bei einem 50-%-Schlüssel ohne Knick je nach Verlauf bei etwa 6 Notenpunkten (Note 4+). Mit Knick verschiebt sich die Verteilung im 4er-Bereich nach oben.",
        ],
        "faq": [
            ("Welche Bestehensgrenze gilt am bayerischen Gymnasium?", "Die GSO schreibt keine landesweit verbindliche Bestehensgrenze für Klausuren vor — üblich sind 50&nbsp;% (lineare Note 4). An manchen Schulen kommt der 45-%-Schlüssel zum Einsatz. Die Fachschaft entscheidet."),
            ("Wie wirken sich Schulaufgaben auf die Halbjahresnote aus?", "In den meisten Fächern zählen Schulaufgaben höher als mündliche Leistungen und Stegreifaufgaben — die genaue Gewichtung steht im schulinternen Konzept. 50:50 (schriftlich:mündlich) und 60:40 sind gängig."),
            ("Was ist ein Unterkurs in der Oberstufe?", "Ein Halbjahr mit weniger als 5 Notenpunkten — also schlechter als „ausreichend\" (Note 4). Mehr als drei Unterkurse können zum Nicht-Bestehen des Abiturs führen. Details im <a href=\"/lexikon/unterkurs/\">Lexikon</a>."),
        ],
    },
    {
        "slug": "grundschule",
        "schulform": "Grundschule",
        "title_h1": ("Notenschlüssel Bayern ", "Grundschule"),
        "page_title": "Notenschlüssel Bayern Grundschule — Probe in Note umrechnen | Der Notenrechner",
        "meta_desc": "Notenschlüssel für bayerische Grundschulen — Probe in Note umrechnen. Erste Ziffernnoten ab Jahrgangsstufe 3. Typische 40–50 %-Bestehensgrenze nach LehrplanPLUS und GrSO.",
        "summary": "An bayerischen Grundschulen werden Ziffernnoten ab Jahrgangsstufe 3 vergeben (GrSO §&nbsp;13). In Klasse 1 und 2 stehen Lernentwicklungsgespräche und Wortgutachten. Der Schlüssel für „Proben\" wird schulintern festgelegt — oft milder als an weiterführenden Schulen.",
        "default_preset": "45",
        "default_max": "20",
        "intro_h2": "Notengebung an der bayerischen Grundschule",
        "intro_body": [
            "Die <strong>Grundschulordnung Bayern (GrSO)</strong> regelt die Leistungsbewertung in Art.&nbsp;52–55 BayEUG sowie GrSO §§&nbsp;12–15. Wesentlich:",
            "In <strong>Jahrgangsstufe 1 und 2</strong> erhalten Kinder keine Ziffernnoten. Stattdessen werden „Lernentwicklungsgespräche\" geführt und im Jahreszeugnis ein <em>Bericht</em> ausgestellt. Erst ab dem zweiten Halbjahr der 2.&nbsp;Klasse oder ab Klasse 3 kommen Ziffernnoten 1–6 hinzu.",
            "<strong>Proben</strong> (auch „Probearbeit\") sind die schriftlichen Leistungserhebungen — meist 20–30&nbsp;Minuten, Maximalpunktzahl typischerweise zwischen 15 und 30 Punkten. Die Bestehensgrenze legt die Klassenlehrkraft fest; gängig sind 40–50&nbsp;%.",
        ],
        "section_h2": "Probe in Note umrechnen — Beispiel",
        "section_intro_body": [
            "Ein typischer Fall: Mathematik-Probe in Klasse 4, Maximalpunktzahl&nbsp;20, 45-%-Schlüssel (Note&nbsp;4 ab&nbsp;9&nbsp;Punkten). Ein Kind erreicht 14&nbsp;Punkte → das sind 70&nbsp;% → Note 2−. Der Rechner oben rechnet das sofort durch.",
            "<strong>Übertrittszeugnis</strong>: In der vierten Klasse entscheidet der Notendurchschnitt aus Deutsch, Mathematik und Heimat- und Sachunterricht (HSU) über den empfohlenen weiterführenden Schultyp. Bis 2,33: Gymnasium, bis 2,66: Realschule, schlechter: Mittelschule. Der Durchschnitt wird ungewichtet gebildet. Berechenbar mit dem <a href=\"/notendurchschnitt/\">Notendurchschnitt-Rechner</a>.",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Was unterscheidet Grundschulen von weiterführenden Schulen?",
        "context_body": [
            "Pädagogisch und rechtlich ist die Bewertung an der Grundschule <em>milder</em> ausgelegt: Lernfreude erhalten, Lernerfolg über Selektion stellen. Drei konkrete Konsequenzen:",
            "<strong>Tendenznoten erlaubt</strong>: 2+ oder 3− sind gängig — anders als an manchen weiterführenden Schulen, wo nur ganze Noten erlaubt sind. Für die Dezimaldarstellung gilt: 2+ = 1,7 / 2 = 2,0 / 2− = 2,3.",
            "<strong>Wort-Schwerpunkt</strong>: Auch wenn Ziffernnoten ab Klasse 3 verpflichtend sind, müssen Zeugnisse ergänzende Würdigungen enthalten — keine reine Zahlenkolonne.",
            "<strong>Bestehen / Versetzung</strong>: Versetzungsrelevant sind im Wesentlichen Deutsch und Mathematik. Eine 5 im Hauptfach kann durch eine 3 in einem anderen Hauptfach ausgeglichen werden — Details in GrSO §&nbsp;14.",
        ],
        "faq": [
            ("Ab welcher Klasse gibt es in Bayern Noten in der Grundschule?", "Verpflichtend ab Klasse 3. In Klasse 1 und 2 werden Lernentwicklungsgespräche geführt; im Zeugnis erscheinen Berichte statt Ziffernnoten. Manche Schulen führen Ziffernnoten optional ab dem 2. Halbjahr der 2. Klasse ein."),
            ("Welche Bestehensgrenze gilt für Proben an der Grundschule?", "Es gibt keine landesweite Vorgabe. Üblich sind 40–50&nbsp;% — also Note 4 ab 8–10 Punkten bei einer 20-Punkte-Probe. Die Klassenlehrkraft legt das fest."),
            ("Wie wird der Schnitt fürs Übertrittszeugnis gebildet?", "Ungewichteter Durchschnitt aus Deutsch, Mathematik und HSU im Jahreszeugnis Klasse 4. Bis 2,33 Gymnasial-Empfehlung, bis 2,66 Realschul-Empfehlung."),
        ],
    },
    {
        "slug": "realschule",
        "schulform": "Realschule",
        "title_h1": ("Notenschlüssel Bayern ", "Realschule"),
        "page_title": "Notenschlüssel Bayern Realschule — Schulaufgabe in Note umrechnen | Der Notenrechner",
        "meta_desc": "Notenschlüssel für bayerische Realschulen — Schulaufgabe in Note umrechnen. Üblich 45–50 %-Schlüssel nach Realschulordnung (RSO). Ziffernnoten 1–6 in den Klassen 5–10.",
        "summary": "Die bayerische Realschule (Klassen 5–10) benotet nach Ziffernnoten 1–6 gemäß Realschulordnung (RSO §§&nbsp;39–45). Schulaufgaben sind die gewichtigsten Leistungserhebungen — der Schlüssel ist schulintern, häufig 45 oder 50&nbsp;% Bestehensgrenze.",
        "default_preset": "45",
        "default_max": "60",
        "intro_h2": "Notengebung an der bayerischen Realschule",
        "intro_body": [
            "Die <strong>Realschulordnung Bayern (RSO)</strong> regelt die Leistungserhebung in §§&nbsp;39 ff. Wichtigste Punkte:",
            "Schriftliche Leistungserhebungen sind <strong>Schulaufgaben</strong> (große, angekündigte Klausuren), <strong>Kurzarbeiten</strong> (Mittelweg) und <strong>Stegreifaufgaben</strong> (kurz, unangekündigt). Schulaufgaben zählen am meisten — pro Halbjahr meist zwei bis vier je Fach.",
            "Der Schlüssel — also wieviel Prozent für welche Note — ist <em>nicht</em> in der RSO landesweit festgelegt. An vielen bayerischen Realschulen kommt der 45-%-Schlüssel zum Einsatz (Note&nbsp;4 ab&nbsp;45&nbsp;%), oft mit <a href=\"/lexikon/knick/\">Knick</a> bei der Note 4−.",
        ],
        "section_h2": "Punkte in Note umrechnen — Realschul-Beispiel",
        "section_intro_body": [
            "Typische Mathematik-Schulaufgabe in Klasse 8, Maximalpunktzahl 60, 45-%-Schlüssel: Note&nbsp;4 ab 27&nbsp;Punkten, Note&nbsp;3 ab 33&nbsp;Punkten, Note&nbsp;2 ab 42&nbsp;Punkten, Note&nbsp;1 ab 54&nbsp;Punkten. Der Rechner oben zeigt das genaue Mapping live.",
            "Versetzungsrelevant ist am Ende des Schuljahres der Notendurchschnitt aller versetzungsrelevanten Fächer (RSO §§&nbsp;55 ff.). Eine 5 in einem Fach kann durch eine 3 in einem anderen ausgeglichen werden, sofern beides nicht Vorrückungsfach ist.",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Abschlussprüfung Realschule (MAP)",
        "context_body": [
            "Der bayerische Realschulabschluss (offiziell: <em>Mittlerer Schulabschluss</em>) wird in Klasse 10 nach einer Abschlussprüfung in Deutsch, Mathematik und einer Fremdsprache vergeben. Aufgabenstellungen sind zentral gestellt, Korrektur und Notenfestlegung erfolgen schulintern nach ISB-Korrekturhinweisen.",
            "Bestehensgrenze für den Mittleren Schulabschluss: Notendurchschnitt nicht schlechter als 4,0 in den schriftlichen Prüfungsfächern und keine 6, im Schnitt aller Fächer nicht schlechter als 4,0 (RSO §&nbsp;70).",
            "Wer mit einem Schnitt von 2,33 oder besser abschließt, hat zudem Zugang zur Fachoberschule (FOS) — eine häufige Anschlussroute nach der Realschule.",
        ],
        "faq": [
            ("Welcher Notenschlüssel wird an Realschulen in Bayern eingesetzt?", "Üblicherweise der 45-%-Schlüssel (Note&nbsp;4 ab 45&nbsp;%) oder der 50-%-Schlüssel. Die genaue Wahl trifft die Fachschaft, oft mit einem Knick an der Bestehensgrenze. Die RSO macht hier keine landesweite Vorgabe."),
            ("Was unterscheidet Schulaufgabe und Kurzarbeit?", "Schulaufgaben sind groß angelegt (oft 45 Minuten oder mehr), erfassen mehrere Stoffeinheiten und werden hoch gewichtet. Kurzarbeiten sind etwa 30 Minuten lang, betreffen ein bis zwei Stoffeinheiten und zählen geringer."),
            ("Mit welchem Schnitt geht es nach der Realschule weiter?", "Mittlerer Schulabschluss reicht für Ausbildungsberufe und Fachoberschule (ab Schnitt 3,5). Schnitt 2,33 oder besser eröffnet auch die direkte FOS-Aufnahme. Notendurchschnitt mit dem <a href=\"/notendurchschnitt/\">Notendurchschnitt-Rechner</a> ausrechnen."),
        ],
    },
    {
        "slug": "berufsschule",
        "schulform": "Berufsschule",
        "title_h1": ("Notenschlüssel Bayern ", "Berufsschule"),
        "page_title": "Notenschlüssel Bayern Berufsschule — Klausur und IHK-Prüfung | Der Notenrechner",
        "meta_desc": "Notenschlüssel für bayerische Berufsschulen — schulische Klausuren (1–6) und IHK-Prüfungen (DIHK-Tabelle). Bestehensgrenzen, Punkte-Note-Umrechnung, Übersicht der IHK-Kammern in Bayern.",
        "summary": "An bayerischen Berufsschulen gibt es zwei parallele Bewertungssysteme: schulische Klausuren nach Ziffernnoten 1–6 (BSO) und IHK-Abschlussprüfungen nach der bundeseinheitlichen DIHK-Tabelle (bestanden ab 50&nbsp;%). Der Rechner unten deckt den schulischen Teil ab.",
        "default_preset": "50",
        "default_max": "100",
        "intro_h2": "Notengebung an der bayerischen Berufsschule",
        "intro_body": [
            "Die <strong>Berufsschulordnung Bayern (BSO)</strong> regelt Leistungserhebung und Bewertung im berufsschulischen Teil der dualen Ausbildung. Schriftliche Leistungen werden in Ziffernnoten 1–6 erfasst; der konkrete Schlüssel ist schulintern.",
            "Die <strong>IHK-Abschlussprüfung</strong> dagegen — Zwischen- und Abschlussprüfung am Ende der Ausbildung — folgt der bundeseinheitlichen DIHK-Notentabelle: 100→1, 91→2, 80→3, 66→4, 49→5, 29→6 als grobe Stützstellen. Bestehensgrenze: 50&nbsp;% (Note 4,4). Details unter <a href=\"/ihk-notenschluessel/\">IHK-Notenschlüssel-Rechner</a> und der bayerischen Regionalseite <a href=\"/ihk-notenschluessel/bayern/\">IHK Bayern</a>.",
        ],
        "section_h2": "Schulische Klausur in Note umrechnen",
        "section_intro_body": [
            "Eine typische Berufsschulklausur wird mit 100 maximalen Punkten und einem 50-%-Schlüssel bewertet — Note&nbsp;4 ab 50&nbsp;Punkten, lineare Verteilung bis Note&nbsp;1 ab 92&nbsp;Punkten. Der Rechner oben erlaubt eigene Maximalpunktzahlen.",
            "Für die <strong>IHK-Prüfung</strong> nutzen Sie statt dieses Rechners den <a href=\"/ihk-notenschluessel/\">IHK-Notenschlüssel-Rechner</a> mit der exakten DIHK-Tabelle (51 Notenstufen, Dezimalnote 1,0–6,0).",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Zwei Welten: Schule und Betrieb",
        "context_body": [
            "Wer eine duale Ausbildung in Bayern macht, hat es mit zwei Bewertungssystemen parallel zu tun:",
            "<strong>Schule (Berufsschule)</strong>: Wöchentlich ein bis zwei Tage Unterricht, regelmäßige Klausuren mit Ziffernnoten 1–6 nach schulinternem Schlüssel. Die Berufsschulnote wird im Abschlusszeugnis ausgewiesen, fließt aber nicht in die IHK-Gesamtnote ein.",
            "<strong>IHK-Prüfung</strong>: Zwischenprüfung (etwa zur Halbzeit) und Abschlussprüfung (Sommer/Winter des letzten Ausbildungsjahres). Bewertet wird mit der bundesweiten DIHK-Tabelle. Erst diese Noten erscheinen im IHK-Prüfungszeugnis und dem Gesellenbrief / Facharbeiterbrief.",
            "Die Schul- und die IHK-Note werden also <em>nicht</em> miteinander verrechnet. Im Bewerbungsgespräch zählen beide.",
        ],
        "faq": [
            ("Gibt es einen einheitlichen Notenschlüssel für Berufsschulen in Bayern?", "Nein — die BSO macht keine landesweite Vorgabe für reguläre Klausuren. Üblich ist der 50-%-Schlüssel."),
            ("Wie wird die IHK-Prüfung bewertet?", "Nach der bundeseinheitlichen DIHK-Tabelle: bestanden ab 50&nbsp;% (Note 4,4). Für die Umrechnung Punkte → Dezimalnote ist der <a href=\"/ihk-notenschluessel/bayern/\">IHK-Notenschlüssel Bayern</a> das richtige Werkzeug."),
            ("Zählt die Berufsschulnote auf dem IHK-Zeugnis?", "Nein. Die Berufsschulnote wird separat im Berufsschulzeugnis ausgewiesen. Die IHK-Gesamtnote bildet sich nur aus den Ergebnissen der IHK-Prüfungen."),
        ],
    },
]


# NRW cluster — sized per Track E DataForSEO research:
# - Grundschule (1,000/mo) is the biggest single sub
# - Gymnasium (260/mo) is second
# - Hub (260/mo)
# - Realschule/Gesamtschule/Hauptschule have <10 vol — deliberately skipped.
NRW_PAGES = [
    {
        "slug": "",  # pillar at /notenschluessel-rechner/nrw/
        "schulform": None,
        "title_h1": ("Notenschlüssel ", "NRW"),
        "page_title": "Notenschlüssel NRW — Rechner für Grundschule, Gymnasium und Sek-I-Klausuren | Der Notenrechner",
        "meta_desc": "Notenschlüssel für Schulen in Nordrhein-Westfalen — Punkte sofort in Note umrechnen. 50/45/40 %-Schlüssel, auch mit Knick. Schulform-Hinweise zu Grundschule und Gymnasium.",
        "summary": "NRW kennt — wie alle Bundesländer — keinen landesweit einheitlichen Notenschlüssel für reguläre Klausuren. Geregelt sind die Bestehensgrenzen für Abschlussprüfungen (zentrale Klassenarbeiten Klasse 8, ZP10, Abitur). Für den Klassenraum entscheidet die Fachkonferenz. Die drei gängigen Varianten 50/45/40 % sind unten direkt rechenbar.",
        "default_preset": "50",
        "default_max": "60",
        "intro_h2": "Notenschlüssel in NRW: was die APO-S I, APO-GOSt und SchulG regeln",
        "intro_body": [
            "In Nordrhein-Westfalen regelt das <strong>Schulgesetz (SchulG NRW)</strong> die Grundlagen der Leistungsbewertung, die <strong>APO-S&nbsp;I</strong> (Ausbildungs- und Prüfungsordnung Sekundarstufe&nbsp;I) und die <strong>APO-GOSt</strong> (Ausbildungs- und Prüfungsordnung Sekundarstufe&nbsp;II / Gymnasiale Oberstufe) die Details für die jeweiligen Schulformen. Diese Verordnungen definieren die Notenstufen (1–6 in Sek&nbsp;I, 15–0 Notenpunkte in der Oberstufe) und die <em>Bestehensgrenzen</em> für Abschlussprüfungen — aber <strong>nicht</strong> den Schlüssel für reguläre Klassenarbeiten.",
            "Der Klassenraum-Schlüssel ist Sache der <strong>Fachkonferenz</strong> (§&nbsp;70 SchulG NRW). Üblich sind 50&nbsp;% Bestehensgrenze am Gymnasium, 40–50&nbsp;% an Grund- und Realschulen, oft mit <a href=\"/lexikon/knick/\">Knick</a> an der Bestehensgrenze. Der Rechner oben zeigt die drei gängigen Varianten — wählen Sie unten Ihre Schulform aus für detailliertere Hinweise.",
        ],
        "section_h2": "NRW nach Schulform",
        "section_intro": "Wechseln Sie zu Ihrer Schulform — jede Unterseite enthält die einschlägige NRW-Verordnung, gebräuchliche Bestehensgrenzen und Hinweise zur Umrechnung Punkte → Note.",
        "show_subpage_cards": True,
        "subpage_notes": True,
        "context_h2": "Was unterscheidet die NRW-Notengebung?",
        "context_body": [
            "NRW hat als bevölkerungsreichstes Bundesland eine besonders breite Schullandschaft: rund 4.500 Schulen, davon allein 600 Gymnasien und 2.700 Grundschulen. Einige Besonderheiten der Leistungsbewertung:",
            "<strong>Lernstandserhebungen (LSE) Klasse 8</strong>: zentrale, vom MSB landeseinheitlich gestellte Aufgaben in Deutsch, Mathematik und Englisch. Diese werden nach einem MSB-Schlüssel ausgewertet, nicht schulintern.",
            "<strong>Zentrale Prüfungen Klasse 10 (ZP10)</strong>: am Ende der Sek&nbsp;I (an Real-, Gesamt- und Sekundarschulen). Auch hier gibt das MSB einen Schlüssel vor.",
            "<strong>Zentralabitur</strong>: schriftliches Abitur seit 2007 landeseinheitlich. Für die Korrektur gelten zentrale Korrekturanweisungen mit verbindlichem Schlüssel; für die mündlichen Prüfungen und Vorabiturklausuren bleibt der Schulschlüssel maßgeblich.",
            "<strong>G8 / G9</strong>: NRW ist seit 2019 wieder fast vollständig G9. Notenpunkte (15–0) gelten in der Qualifikationsphase (Q1/Q2), Ziffernnoten in der Einführungsphase und der gesamten Sek&nbsp;I.",
        ],
        "faq": [
            ("Gibt es einen offiziellen NRW-Notenschlüssel für Klausuren?", "Nein — die APO-S&nbsp;I und APO-GOSt enthalten keinen landeseinheitlichen Schlüssel für reguläre Klassenarbeiten. Geregelt sind nur die Notenstufen und Bestehensgrenzen für Abschlussprüfungen. Den Klassenraum-Schlüssel bestimmt die Fachkonferenz (§&nbsp;70 SchulG NRW)."),
            ("Welcher Schlüssel wird in NRW am häufigsten verwendet?", "Am Gymnasium üblicherweise der 50-%-Schlüssel (Note 4 ab 50&nbsp;%), oft mit Knick. An Grundschulen häufig 40–50&nbsp;% mit Knick. An Real-, Gesamt- und Sekundarschulen 45–50&nbsp;%. Verbindliche Zahlen stehen im fachschaftsinternen Konzept der jeweiligen Schule."),
            ("Was gilt für Zentrale Prüfungen (ZP10, Abitur)?", "Für ZP10 und das Zentralabitur gibt das Ministerium (MSB NRW) landeseinheitliche Korrekturhinweise und Schlüssel vor. Lehrkräfte folgen diesen Anweisungen statt eines schulinternen Schlüssels."),
            ("Welche Bundesland-Regelungen gelten für Notenpunkte in NRW?", "Die APO-GOSt definiert das Notenpunktesystem 15–0 für die Qualifikationsphase (Q1/Q2). Sie steht weitgehend bundesweit im Einklang mit der KMK-Vereinbarung. Hintergrund im <a href=\"/lexikon/notenpunkte/\">Lexikon: Notenpunkte</a>."),
        ],
    },
    {
        "slug": "grundschule",
        "schulform": "Grundschule",
        "title_h1": ("Notenschlüssel NRW ", "Grundschule"),
        "page_title": "Notenschlüssel NRW Grundschule — Klassenarbeit in Note umrechnen | Der Notenrechner",
        "meta_desc": "Notenschlüssel für nordrhein-westfälische Grundschulen — Klassenarbeit in Note umrechnen. Ziffernnoten ab Klasse 3 (AO-GS). Typische 40–50 %-Bestehensgrenze, oft mit Knick.",
        "summary": "An NRW-Grundschulen werden Ziffernnoten ab dem 2. Halbjahr der 3. Klasse vergeben — geregelt in der Ausbildungs- und Prüfungsordnung Grundschule (AO-GS). Davor stehen Berichtszeugnisse mit Lernentwicklungsdokumentation. Der Klassenraum-Schlüssel ist schulintern; üblich sind 40–50&nbsp;% Bestehensgrenze.",
        "default_preset": "45",
        "default_max": "20",
        "intro_h2": "Notengebung an der NRW-Grundschule",
        "intro_body": [
            "Die <strong>Ausbildungsordnung Grundschule (AO-GS NRW)</strong> regelt Leistungsbewertung und Versetzung. Die wichtigsten Punkte:",
            "<strong>Klasse 1 und 2</strong>: keine Ziffernnoten. Zeugnisse enthalten Berichte zu Arbeits-/Sozialverhalten und fachbezogenen Kompetenzen. Lernentwicklungsgespräche ergänzen das Zeugnis.",
            "<strong>Klasse 3 (zweites Halbjahr) und Klasse 4</strong>: Ziffernnoten 1–6, ergänzt durch Berichte zum Arbeits- und Sozialverhalten. Manche Schulen behalten die Berichtsform auch in Klasse 3 noch bei.",
            "<strong>Klassenarbeiten</strong> sind die zentralen schriftlichen Leistungserhebungen — typischerweise 30–45 Minuten, Maximalpunktzahl meist zwischen 15 und 30 Punkten. Die Bestehensgrenze legt die Schule fest; gängig sind 40–50&nbsp;% Bestehensgrenze, oft mit Knick (40&nbsp;% → Note 4, dann linear bis 95–100&nbsp;% → Note 1).",
        ],
        "section_h2": "Klassenarbeit in Note umrechnen — Beispiel",
        "section_intro_body": [
            "Typische Mathematik-Klassenarbeit in Klasse 4, Maximalpunktzahl&nbsp;20, 45-%-Schlüssel (Note&nbsp;4 ab&nbsp;9&nbsp;Punkten). Ein Kind erreicht 15&nbsp;Punkte → 75&nbsp;% → Note 2−. Der Rechner oben rechnet das sofort durch — Maximalpunktzahl ändern, Punkte eintippen, Note ablesen.",
            "<strong>Anmeldung Sek I (Schulformempfehlung)</strong>: Am Ende der 4. Klasse stellt die Grundschule eine begründete Empfehlung für die weiterführende Schulform aus (Gymnasium, Realschule, Gesamtschule). Anders als in Bayern ist die Empfehlung in NRW <em>nicht bindend</em> — Eltern entscheiden über die Anmeldung. Die Empfehlung basiert auf Leistungen, Arbeitsverhalten und Sozialkompetenz, nicht auf einem festen Notenschnitt. Den Notendurchschnitt aus den Hauptfächern können Sie mit dem <a href=\"/notendurchschnitt/\">Notendurchschnitt-Rechner</a> bilden.",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Was unterscheidet NRW-Grundschulen von weiterführenden Schulen?",
        "context_body": [
            "Im Vergleich zur Sek&nbsp;I und zur Oberstufe ist die Bewertung an der Grundschule <em>pädagogisch milder</em> ausgelegt — Lernfreude erhalten, Lernerfolg über Selektion stellen. Konkrete Konsequenzen:",
            "<strong>Tendenznoten erlaubt</strong>: 2+ oder 3− sind in NRW-Grundschulzeugnissen üblich. Für die Dezimaldarstellung: 2+ = 1,7 / 2 = 2,0 / 2− = 2,3. Manche Lehrkräfte vergeben Tendenznoten auch innerhalb von Klassenarbeiten, andere nur ganze Noten — Konzept der jeweiligen Schule.",
            "<strong>Bericht über Ziffernnote hinaus</strong>: Auch wenn Ziffernnoten ab Klasse 3 verpflichtend sind, ergänzen Berichtszeugnisse die reine Note — kein nacktes Zahlenwerk. Diese Regel gilt nur in der Grundschule.",
            "<strong>Versetzungsregeln</strong> in der AO-GS: Versetzungsrelevant sind Deutsch und Mathematik. Eine 5 in einem dieser Hauptfächer kann durch eine 3 in einem anderen Hauptfach ausgeglichen werden. Bei 6 oder zwei 5-en ist die Versetzung in der Regel gefährdet — die Klassenkonferenz entscheidet.",
        ],
        "faq": [
            ("Ab welcher Klasse gibt es in NRW Noten in der Grundschule?", "Verpflichtend ab dem zweiten Halbjahr der dritten Klasse. Klasse 1 und 2 sowie das erste Halbjahr der dritten Klasse sind notenfrei — geregelt in der AO-GS NRW. Zeugnisse enthalten in dieser Zeit Berichte zu Arbeits-/Sozialverhalten und fachlichen Kompetenzen."),
            ("Welche Bestehensgrenze gilt für Klassenarbeiten an NRW-Grundschulen?", "Keine landesweite Vorgabe. Üblich sind 40–50&nbsp;% — Note 4 ab 8–10 Punkten bei einer 20-Punkte-Arbeit. Die Schule legt das im Leistungsbewertungskonzept fest, das jeder Eltern auf Anfrage einsehen kann."),
            ("Ist die Schulformempfehlung der Grundschule in NRW bindend?", "Nein. Anders als in Bayern entscheiden in NRW die Eltern, an welcher weiterführenden Schulform sie ihr Kind anmelden. Die Empfehlung der Grundschule ist ein Beratungsdokument, keine Zulassungsentscheidung."),
        ],
    },
    {
        "slug": "gymnasium",
        "schulform": "Gymnasium",
        "title_h1": ("Notenschlüssel NRW ", "Gymnasium"),
        "page_title": "Notenschlüssel NRW Gymnasium — Klausur und Klassenarbeit in Note umrechnen | Der Notenrechner",
        "meta_desc": "Notenschlüssel für nordrhein-westfälische Gymnasien — Klassenarbeit oder Klausur in Note umrechnen. 50/45 %-Schlüssel mit Knick. Sek&nbsp;I (1–6) und Oberstufe (15–0 Notenpunkte) gemäß APO-S&nbsp;I und APO-GOSt.",
        "summary": "Am NRW-Gymnasium gilt in Sek&nbsp;I die APO-S&nbsp;I (Ziffernnoten 1–6), in der Oberstufe (Q1/Q2) die APO-GOSt mit Notenpunkten 15–0. Der konkrete Schlüssel für Klassenarbeiten und Klausuren wird fachschaftlich festgelegt — meist 50&nbsp;% Bestehensgrenze, häufig mit Knick.",
        "default_preset": "50",
        "default_max": "60",
        "intro_h2": "Notengebung am NRW-Gymnasium",
        "intro_body": [
            "Zwei Verordnungen regeln am NRW-Gymnasium die Leistungserhebung: <strong>APO-S&nbsp;I</strong> für die Klassen 5–10 und <strong>APO-GOSt</strong> für die Einführungs- und Qualifikationsphase. Beide enthalten die Notenstufen und Bestehensgrenzen, aber keinen verbindlichen Schlüssel für reguläre Klassenarbeiten und Klausuren.",
            "In der Sek&nbsp;I werden Ziffernnoten 1–6 vergeben; in der Q1/Q2 das Notenpunktesystem 15–0 — drei Notenpunkte entsprechen einer Notenstufe. Hintergrund im <a href=\"/lexikon/notenpunkte/\">Lexikon: Notenpunkte</a>. Der Schlüssel selbst (Prozente → Note) ist Sache der Fachkonferenz; üblich ist der lineare 50-%-Schlüssel, optional mit <a href=\"/lexikon/knick/\">Knick</a>.",
        ],
        "section_h2": "Klassenarbeit oder Oberstufenklausur — was zählt wie?",
        "section_intro_body": [
            "Zwei Hauptformen schriftlicher Leistungserhebung am NRW-Gymnasium:",
            "<strong>Klassenarbeiten</strong> (Sek&nbsp;I, Klassen 5–10): meist 45 Minuten, pro Halbjahr 2–4 je Hauptfach. Sie zählen in der Regel zu 50&nbsp;% der Halbjahresnote (schriftliche Säule), die andere Hälfte sind „Sonstige Leistungen\" (mündliche Mitarbeit, Heftführung, kurze Tests). Konkrete Anteile bestimmt das schulinterne Leistungsbewertungskonzept.",
            "<strong>Oberstufenklausuren</strong> (Q1/Q2): meist 90–135 Minuten in Leistungskursen, 60–90 Minuten in Grundkursen. Pro Halbjahr typischerweise zwei Klausuren je Fach. In den Abiturfächern gilt die Klausur als „Vorbereitungs-Klausur\" mit Abitur-Format und -Anforderungen.",
            "Der Notenschlüssel ist <em>typischerweise</em> für Klassenarbeit und Klausur identisch (oft 50-%-Schlüssel mit Knick), aber die Gewichtung der schriftlichen vs. mündlichen Säule unterscheidet sich. In der Oberstufe ist die Gewichtung schriftlich vs. „Sonstige Mitarbeit\" oft 50:50, in der Sek&nbsp;I teils mit Schwerpunkt auf der schriftlichen Säule.",
        ],
        "show_subpage_cards": False,
        "subpage_notes": False,
        "context_h2": "Zentralabitur in NRW: was bedeutet das für den Schlüssel?",
        "context_body": [
            "Seit 2007 hat NRW landeseinheitliches schriftliches Zentralabitur. Aufgaben kommen vom Schulministerium (MSB), die Korrektur folgt verbindlichen Korrekturhinweisen — inklusive Punkteverteilung und Schlüssel.",
            "Praktisch heißt das: In den Abitur-Klausuren der Q2 (insbesondere der letzten Klausur unter Abitur-Bedingungen, „Vor-Abitur\") wenden Lehrkräfte den MSB-Schlüssel an, nicht den schulinternen. Außerhalb dieser Klausuren bleibt der Fachschaftsbeschluss maßgeblich.",
            "Für die <strong>Gesamtqualifikation Abitur</strong> kommen Block I (eingebrachte Kurse Q1/Q2) und Block II (Abiturprüfungen, vierfach gewichtet) zusammen — die Punktsumme wird per Bundesland-spezifischer Tabelle in die Abiturnote 1,0–4,0 übersetzt. Block I ist in NRW größer dimensioniert als z.&nbsp;B. in Bayern: 35–40 Halbjahresnoten werden eingebracht, je nach Profilwahl. Details siehe Lexikoneintrag <a href=\"/lexikon/notenpunkte/\">Notenpunkte</a> und <a href=\"/lexikon/unterkurs/\">Unterkurs</a>.",
        ],
        "faq": [
            ("Welche Bestehensgrenze gilt am NRW-Gymnasium?", "Die APO-S&nbsp;I und APO-GOSt schreiben keine landesweit verbindliche Bestehensgrenze für reguläre Klassenarbeiten/Klausuren vor — üblich sind 50&nbsp;% am Gymnasium, oft mit Knick. Die Fachkonferenz beschließt."),
            ("Wie wirken sich Klassenarbeiten in NRW auf die Halbjahresnote aus?", "In den meisten Fächern zählen Klassenarbeiten zu 50&nbsp;% der Halbjahresnote (schriftliche Säule), die andere Hälfte sind „Sonstige Leistungen\". Manche Schulen bilanzieren 60:40 oder 40:60 — Beschluss der Lehrerkonferenz."),
            ("Was passiert bei einem Unterkurs in NRW?", "Ein Halbjahr mit 0 Notenpunkten gilt als nicht erbracht; ein Halbjahr mit weniger als 5 Notenpunkten ist ein <a href=\"/lexikon/unterkurs/\">Unterkurs</a>. Zu viele Unterkurse können zum Nichtbestehen des Abiturs führen — Details in der APO-GOSt §§&nbsp;19, 28."),
        ],
    },
]


# All Bundesländer in scope. Add new ones here — main() iterates over this list.
REGIONS = [
    {
        "slug": "bayern",
        "name": "Bayern",
        "pages": BAYERN_PAGES,
        "subpages_list": [
            ("gymnasium", "Gymnasium",
             "Schulaufgabe und Stegreifaufgabe — GSO, Sek&nbsp;I und Oberstufe (15–0 Notenpunkte)."),
            ("grundschule", "Grundschule",
             "Probe in Note umrechnen — Ziffernnoten ab Klasse 3, Übertrittszeugnis nach Klasse 4."),
            ("realschule", "Realschule",
             "Schulaufgabe und Mittlerer Schulabschluss — Realschulordnung RSO."),
            ("berufsschule", "Berufsschule",
             "Berufsschulklausur und IHK-Prüfung parallel — schulischer und kammergeführter Teil."),
        ],
    },
    {
        "slug": "nrw",
        "name": "NRW",
        "pages": NRW_PAGES,
        "subpages_list": [
            ("grundschule", "Grundschule",
             "Klassenarbeit in Note umrechnen — Ziffernnoten ab Klasse 3, Schulformempfehlung Klasse 4 (nicht bindend)."),
            ("gymnasium", "Gymnasium",
             "Klassenarbeit und Oberstufenklausur — APO-S I (1–6) und APO-GOSt (15–0 Notenpunkte)."),
        ],
    },
]


CSS = dedent("""\
:root {
  --primary: #2F60C0; --primary-light: #6B94E0; --primary-dark: #1F4A9C;
  --primary-50: #EEF3FB; --primary-100: #DCE5F5;
  --bg: #F7F6F3; --card: #FFFFFF; --surface-subtle: #F1EFEA;
  --text: #0F0F10; --text-secondary: #3B3B3F; --text-muted: #6E6E73;
  --border: #E8E6E1; --border-light: #F1EFEA;
  --grade-1: #15803D; --grade-1-bg: #E6F2EA;
  --grade-2: #4D7C0F; --grade-2-bg: #EFF1E2;
  --grade-3: #A16207; --grade-3-bg: #F8EFE0;
  --grade-4: #C2410C; --grade-4-bg: #FAEADD;
  --grade-5: #B91C1C; --grade-5-bg: #F7E6E6;
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

.tool-hero { padding-top: calc(var(--nav-height) + 40px); padding-bottom: 32px; background: linear-gradient(180deg, var(--bg) 0%, #FBFAF6 100%); border-bottom: 1px solid var(--border); }
.breadcrumbs { font-size: 13px; color: var(--text-muted); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.breadcrumbs a { color: var(--text-secondary); transition: color 0.15s; }
.breadcrumbs a:hover { color: var(--primary); }
.breadcrumbs span[aria-current] { color: var(--text); font-weight: 500; }
.tool-hero-header { text-align: center; margin-bottom: 32px; max-width: 760px; margin-left: auto; margin-right: auto; }
.tool-hero-header h1 { font-size: clamp(28px, 4.5vw, 42px); font-weight: 800; letter-spacing: -0.025em; line-height: 1.15; margin-bottom: 14px; }
.tool-hero-header h1 span { color: var(--primary); }
.tool-hero-sub { font-size: 17px; color: var(--text-secondary); }

/* Calculator (mirrors notenschluessel-rechner) */
.calc { max-width: 720px; margin: 0 auto; }
.calc-card { background: var(--card); border-radius: var(--radius-lg); box-shadow: var(--shadow-card); padding: 26px 26px 22px; }
.calc-controls { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 18px; }
@media (max-width: 540px) { .calc-controls { grid-template-columns: 1fr; } }
.calc-field label { display: block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-secondary); margin-bottom: 6px; }
.calc-input, .calc-select { width: 100%; height: 48px; padding: 0 14px; border: 1.5px solid var(--border); border-radius: var(--radius-md); font-family: var(--font); font-size: 17px; font-weight: 600; color: var(--text); background: var(--bg); font-variant-numeric: tabular-nums; transition: border-color 0.15s, box-shadow 0.15s; -moz-appearance: textfield; }
.calc-select { background: var(--bg) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8' fill='none' stroke='%233B3B3F' stroke-width='2'><polyline points='1 1 6 6 11 1'/></svg>") no-repeat right 14px center; background-size: 12px 8px; appearance: none; padding-right: 38px; }
.calc-input::-webkit-outer-spin-button, .calc-input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
.calc-input:focus, .calc-select:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 4px rgba(47,96,192,0.1); }

.calc-result { text-align: center; padding: 18px 22px 16px; border-radius: var(--radius-md); transition: background 0.25s ease-out, color 0.25s ease-out; }
.calc-result-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.7; margin-bottom: 6px; }
.calc-result-grade { font-size: 48px; font-weight: 800; line-height: 1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; }
.calc-result-desc { font-size: 15px; font-weight: 600; margin-top: 6px; }
.calc-result-pct { font-size: 12px; opacity: 0.7; margin-top: 4px; font-variant-numeric: tabular-nums; }

/* Threshold table */
.grade-table-wrap { max-width: 720px; margin: 24px auto 0; background: var(--card); border-radius: var(--radius-lg); box-shadow: var(--shadow-card); overflow: hidden; }
.grade-table-head { padding: 16px 22px 12px; border-bottom: 1px solid var(--border-light); font-size: 14px; font-weight: 700; }
.grade-table { width: 100%; border-collapse: collapse; }
.grade-table thead th { padding: 10px 22px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-secondary); text-align: left; background: var(--border-light); border-bottom: 1px solid var(--border); }
.grade-table tbody td { padding: 10px 22px; font-size: 15px; border-bottom: 1px solid var(--border-light); }
.grade-table tbody tr:last-child td { border-bottom: none; }
.grade-cell { display: flex; align-items: center; gap: 10px; }
.grade-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.grade-name { font-weight: 700; font-variant-numeric: tabular-nums; }
.grade-label { color: var(--text-muted); font-size: 13px; margin-left: 4px; }

/* Content */
.content-section { padding: 56px 0 64px; }
.content-prose { max-width: 720px; margin: 0 auto; }
.content-prose h2 { font-size: clamp(22px, 3vw, 28px); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 14px; }
.content-prose h2:not(:first-child) { margin-top: 44px; }
.content-prose h3 { font-size: 19px; font-weight: 700; margin-top: 28px; margin-bottom: 10px; }
.content-prose p { font-size: 16px; line-height: 1.75; color: var(--text-secondary); margin-bottom: 14px; }
.content-prose a { color: var(--primary); font-weight: 500; text-decoration: underline; text-underline-offset: 3px; }
.content-prose strong { color: var(--text); }
.content-prose em { font-style: italic; color: var(--text); }

/* Subpage cards */
.subpage-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 18px; }
@media (max-width: 640px) { .subpage-cards { grid-template-columns: 1fr; } }
.subpage-card { display: flex; flex-direction: column; gap: 6px; padding: 18px 20px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-md); transition: border-color 0.15s, transform 0.15s; color: var(--text); }
.subpage-card:hover { border-color: var(--primary); transform: translateY(-1px); }
.subpage-card-title { font-size: 16px; font-weight: 700; color: var(--text); }
.subpage-card-desc { font-size: 13.5px; color: var(--text-muted); line-height: 1.55; }

/* FAQ */
.faq-list { display: flex; flex-direction: column; gap: 0; margin-top: 18px; border-top: 1px solid var(--border); }
.faq-item { border-bottom: 1px solid var(--border); padding: 20px 0; }
.faq-q { font-size: 17px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
.faq-a { font-size: 15.5px; line-height: 1.7; color: var(--text-secondary); }

.internal-links { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 36px; }
.internal-link { display: inline-flex; align-items: center; gap: 6px; padding: 10px 16px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-pill); font-size: 14px; font-weight: 500; color: var(--text); text-decoration: none !important; transition: border-color 0.2s, transform 0.15s; }
.internal-link:hover { border-color: var(--primary); transform: translateY(-1px); color: var(--primary); }

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


NAV_HTML = '''  <nav class="nav" role="navigation" aria-label="Hauptnavigation">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><span class="nav-brand-icon"><img src="/assets/logo.png" alt=""></span>Der Notenrechner</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/" onclick="closeMenu()">Startseite</a></li>
        <li><a href="/notenschluessel-rechner/" class="active" onclick="closeMenu()">Notenschlüssel-Rechner</a></li>
        <li><a href="/notenpunkte-tabelle/" onclick="closeMenu()">Notenpunkte-Tabelle</a></li>
        <li><a href="/ihk-notenschluessel/" onclick="closeMenu()">IHK-Rechner</a></li>
        <li><a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="nav-cta" onclick="closeMenu()" aria-label="Im App Store laden"><svg viewBox="0 0 384 512" fill="currentColor" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>Laden</a></li>
      </ul>
    </div>
  </nav>'''


CALC_SCRIPT = """
const PRESETS = {
  '50': [
    { grade: 15, minPct: 98 }, { grade: 14, minPct: 95 }, { grade: 13, minPct: 92 },
    { grade: 12, minPct: 88 }, { grade: 11, minPct: 85 }, { grade: 10, minPct: 81 },
    { grade: 9, minPct: 76 }, { grade: 8, minPct: 72 }, { grade: 7, minPct: 67 },
    { grade: 6, minPct: 61 }, { grade: 5, minPct: 56 }, { grade: 4, minPct: 50 },
    { grade: 3, minPct: 43 }, { grade: 2, minPct: 37 }, { grade: 1, minPct: 30 },
    { grade: 0, minPct: 0 }
  ],
  '45': [
    { grade: 15, minPct: 98 }, { grade: 14, minPct: 94 }, { grade: 13, minPct: 90 },
    { grade: 12, minPct: 85 }, { grade: 11, minPct: 80 }, { grade: 10, minPct: 75 },
    { grade: 9, minPct: 70 }, { grade: 8, minPct: 65 }, { grade: 7, minPct: 60 },
    { grade: 6, minPct: 55 }, { grade: 5, minPct: 50 }, { grade: 4, minPct: 45 },
    { grade: 3, minPct: 39 }, { grade: 2, minPct: 32 }, { grade: 1, minPct: 24 },
    { grade: 0, minPct: 0 }
  ],
  '40': [
    { grade: 15, minPct: 95 }, { grade: 14, minPct: 90 }, { grade: 13, minPct: 85 },
    { grade: 12, minPct: 80 }, { grade: 11, minPct: 75 }, { grade: 10, minPct: 70 },
    { grade: 9, minPct: 65 }, { grade: 8, minPct: 60 }, { grade: 7, minPct: 55 },
    { grade: 6, minPct: 50 }, { grade: 5, minPct: 45 }, { grade: 4, minPct: 40 },
    { grade: 3, minPct: 33 }, { grade: 2, minPct: 27 }, { grade: 1, minPct: 20 },
    { grade: 0, minPct: 0 }
  ]
};
const NP_MAP = { 15:'1+', 14:'1', 13:'1-', 12:'2+', 11:'2', 10:'2-', 9:'3+', 8:'3', 7:'3-', 6:'4+', 5:'4', 4:'4-', 3:'5+', 2:'5', 1:'5-', 0:'6' };

function gradeColor(g) {
  if (g >= 13) return 'var(--grade-1)';
  if (g >= 10) return 'var(--grade-2)';
  if (g >= 7)  return 'var(--grade-3)';
  if (g >= 4)  return 'var(--grade-4)';
  return 'var(--grade-5)';
}
function gradeBg(g) {
  if (g >= 13) return 'var(--grade-1-bg)';
  if (g >= 10) return 'var(--grade-2-bg)';
  if (g >= 7)  return 'var(--grade-3-bg)';
  if (g >= 4)  return 'var(--grade-4-bg)';
  return 'var(--grade-5-bg)';
}
function gradeDesc(g) {
  if (g >= 13) return 'sehr gut';
  if (g >= 10) return 'gut';
  if (g >= 7)  return 'befriedigend';
  if (g >= 4)  return 'ausreichend';
  if (g >= 1)  return 'mangelhaft';
  return 'ungenügend';
}
function fmtPts(v) { return v === Math.floor(v) ? v.toString() : v.toFixed(1).replace('.', ','); }
function fmtPct(n) { return n.toFixed(1).replace('.', ','); }

const presetSel = document.getElementById('preset');
const maxInput = document.getElementById('maxPts');
const achievedInput = document.getElementById('achieved');
const calcResult = document.getElementById('calcResult');
const resultGrade = document.getElementById('resultGrade');
const resultDesc = document.getElementById('resultDesc');
const resultPct = document.getElementById('resultPct');
const tableBody = document.getElementById('tableBody');

function calculate() {
  const presetKey = presetSel.value;
  const thresholds = PRESETS[presetKey];
  const maxPts = Math.max(1, parseFloat((maxInput.value || '').replace(',', '.')) || 100);
  const achievedRaw = (achievedInput.value || '').replace(',', '.').trim();
  const achievedNum = parseFloat(achievedRaw);
  const hasAchieved = achievedRaw !== '' && !isNaN(achievedNum) && achievedNum >= 0;

  let activeGrade = null;
  let pct = 0;
  if (hasAchieved) {
    const clamped = Math.min(achievedNum, maxPts);
    pct = (clamped / maxPts) * 100;
    for (const t of thresholds) { if (pct >= t.minPct) { activeGrade = t.grade; break; } }
  }

  let html = '';
  for (const t of thresholds) {
    const minPts = (t.minPct / 100) * maxPts;
    const color = gradeColor(t.grade);
    const cls = (activeGrade === t.grade) ? ' style="background: rgba(47,96,192,0.05);"' : '';
    html += '<tr' + cls + '>'
      + '<td><div class="grade-cell"><span class="grade-dot" style="background:' + color + '"></span><span class="grade-name">' + t.grade + '</span><span class="grade-label">' + (NP_MAP[t.grade] || '') + '</span></div></td>'
      + '<td>' + fmtPts(minPts) + ' Punkte <span class="grade-label">(' + t.minPct + ' %)</span></td>'
      + '</tr>';
  }
  tableBody.innerHTML = html;

  if (!hasAchieved) {
    calcResult.style.background = 'var(--border-light)';
    calcResult.style.color = 'var(--text-muted)';
    resultGrade.textContent = '—';
    resultDesc.textContent = 'Punkte eingeben';
    resultPct.textContent = '';
    return;
  }

  calcResult.style.background = gradeBg(activeGrade);
  calcResult.style.color = gradeColor(activeGrade);
  resultGrade.textContent = activeGrade;
  resultDesc.textContent = (NP_MAP[activeGrade] || '') + ' · ' + gradeDesc(activeGrade);
  resultPct.textContent = fmtPct(pct) + ' % erreicht';
}

presetSel.addEventListener('change', calculate);
maxInput.addEventListener('input', calculate);
achievedInput.addEventListener('input', calculate);
calculate();
"""


def render_subpage_cards(region, current_slug):
    """Render the subpage cards block for a region's pillar page."""
    cards_html = ""
    for slug, name, desc in region["subpages_list"]:
        if slug == current_slug:
            continue
        cards_html += (
            f'\n            <a href="/notenschluessel-rechner/{region["slug"]}/{slug}/" class="subpage-card">'
            f'\n              <span class="subpage-card-title">{region["name"]} {name}</span>'
            f'\n              <span class="subpage-card-desc">{desc}</span>'
            f'\n            </a>'
        )
    return cards_html


def render_faq_html(faq):
    items = ""
    for q, a in faq:
        items += (
            f'\n            <div class="faq-item">'
            f'\n              <div class="faq-q">{q}</div>'
            f'\n              <div class="faq-a">{a}</div>'
            f'\n            </div>'
        )
    return items


def render_faq_schema(faq):
    parts = []
    for q, a in faq:
        a_clean = a.replace('"', '\\"')
        parts.append(
            '{ "@type": "Question", "name": "' + q.replace('"', '\\"') + '", '
            '"acceptedAnswer": { "@type": "Answer", "text": "' + a_clean + '" } }'
        )
    return ",\n          ".join(parts)


def render_page(p, region):
    region_slug = region["slug"]
    region_name = region["name"]
    slug = p["slug"]
    schulform = p["schulform"]
    is_pillar = slug == ""
    region_base = f"https://notenrechnerapp.de/notenschluessel-rechner/{region_slug}/"
    region_path = f"/notenschluessel-rechner/{region_slug}/"  # relative for internal links

    if is_pillar:
        canonical = region_base
        breadcrumbs_html = (
            '<a href="/">Start</a>'
            '<span aria-hidden="true">›</span>'
            '<a href="/notenschluessel-rechner/">Notenschlüssel-Rechner</a>'
            '<span aria-hidden="true">›</span>'
            f'<span aria-current="page">{region_name}</span>'
        )
        breadcrumb_items = (
            '{ "@type": "ListItem", "position": 1, "name": "Der Notenrechner", "item": "https://notenrechnerapp.de/" },'
            '{ "@type": "ListItem", "position": 2, "name": "Notenschlüssel-Rechner", "item": "https://notenrechnerapp.de/notenschluessel-rechner/" },'
            f'{{ "@type": "ListItem", "position": 3, "name": "{region_name}", "item": "{canonical}" }}'
        )
    else:
        canonical = f"{region_base}{slug}/"
        breadcrumbs_html = (
            '<a href="/">Start</a>'
            '<span aria-hidden="true">›</span>'
            '<a href="/notenschluessel-rechner/">Notenschlüssel-Rechner</a>'
            '<span aria-hidden="true">›</span>'
            f'<a href="{region_path}">{region_name}</a>'
            '<span aria-hidden="true">›</span>'
            f'<span aria-current="page">{schulform}</span>'
        )
        breadcrumb_items = (
            '{ "@type": "ListItem", "position": 1, "name": "Der Notenrechner", "item": "https://notenrechnerapp.de/" },'
            '{ "@type": "ListItem", "position": 2, "name": "Notenschlüssel-Rechner", "item": "https://notenrechnerapp.de/notenschluessel-rechner/" },'
            f'{{ "@type": "ListItem", "position": 3, "name": "{region_name}", "item": "{region_base}" }},'
            f'{{ "@type": "ListItem", "position": 4, "name": "{schulform}", "item": "{canonical}" }}'
        )

    h1_lead, h1_accent = p["title_h1"]

    intro_paras = "\n          ".join(f"<p>{para}</p>" for para in p["intro_body"])

    section_block = ""
    if p.get("show_subpage_cards"):
        cards = render_subpage_cards(region, slug)
        section_block = (
            f'<h2>{p["section_h2"]}</h2>\n'
            f'          <p>{p["section_intro"]}</p>\n'
            f'          <div class="subpage-cards">{cards}\n'
            f'          </div>'
        )
    elif "section_intro_body" in p:
        intro_html = "\n          ".join(f"<p>{para}</p>" for para in p["section_intro_body"])
        section_block = (
            f'<h2>{p["section_h2"]}</h2>\n'
            f'          {intro_html}'
        )
    elif p.get("section_intro"):
        section_block = (
            f'<h2>{p["section_h2"]}</h2>\n'
            f'          <p>{p["section_intro"]}</p>'
        )

    context_paras = "\n          ".join(f"<p>{para}</p>" for para in p["context_body"])

    faq_html = render_faq_html(p["faq"])
    faq_schema = render_faq_schema(p["faq"])

    # Internal-link block — different for pillar vs sub-page.
    if is_pillar:
        internal_links = (
            '<a href="/notenschluessel-rechner/" class="internal-link">Hauptrechner</a>\n'
            f'            <a href="/ihk-notenschluessel/{region_slug}/" class="internal-link">IHK {region_name}</a>\n'
            '            <a href="/lexikon/notenschluessel/" class="internal-link">Lexikon: Notenschlüssel</a>\n'
            '            <a href="/lexikon/knick/" class="internal-link">Lexikon: Knick</a>\n'
            '            <a href="/lexikon/bestehensgrenze/" class="internal-link">Lexikon: Bestehensgrenze</a>'
        )
    else:
        internal_links = (
            f'<a href="{region_path}" class="internal-link">{region_name}-Übersicht</a>\n'
            '            <a href="/notenschluessel-rechner/" class="internal-link">Hauptrechner</a>\n'
            '            <a href="/notendurchschnitt/" class="internal-link">Notendurchschnitt</a>\n'
            '            <a href="/lexikon/notenschluessel/" class="internal-link">Lexikon: Notenschlüssel</a>'
        )
        if slug == "berufsschule":
            internal_links += (
                f'\n            <a href="/ihk-notenschluessel/{region_slug}/" class="internal-link">IHK {region_name}</a>'
            )
        if slug == "gymnasium":
            internal_links += (
                '\n            <a href="/notenpunkte-tabelle/" class="internal-link">Notenpunkte-Tabelle</a>'
                '\n            <a href="/lexikon/unterkurs/" class="internal-link">Lexikon: Unterkurs</a>'
            )

    title = p["page_title"]
    desc = p["meta_desc"]
    default_preset = p["default_preset"]
    default_max = p["default_max"]

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="Der Notenrechner">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="theme-color" content="#2F60C0">
  <meta name="apple-itunes-app" content="app-id=1662507346">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">
  <!-- Schema.org structured data — Organization + Person + Article + SoftwareApplication + BreadcrumbList + FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{ "@type": "Organization", "@id": "https://notenrechnerapp.de/#organization", "name": "Der Notenrechner", "url": "https://notenrechnerapp.de/", "logo": "https://notenrechnerapp.de/assets/logo.png", "founder": {{ "@id": "https://notenrechnerapp.de/#author" }}, "sameAs": ["https://apps.apple.com/de/app/der-notenrechner/id1662507346", "https://instagram.com/notenrechnerapp"] }},
      {{ "@type": "Person", "@id": "https://notenrechnerapp.de/#author", "name": "Jonah Röhl", "jobTitle": "Lehrer & Entwickler", "description": "Lehrkraft in Hamburg und Entwickler von Der Notenrechner.", "url": "https://notenrechnerapp.de/#author", "worksFor": {{ "@id": "https://notenrechnerapp.de/#organization" }} }},
      {{
        "@type": "Article",
        "headline": "{h1_lead.strip()}{h1_accent}",
        "description": "{desc}",
        "url": "{canonical}",
        "datePublished": "{DATE_PUBLISHED}",
        "dateModified": "{DATE_MODIFIED}",
        "author": {{ "@id": "https://notenrechnerapp.de/#author" }},
        "publisher": {{ "@id": "https://notenrechnerapp.de/#organization" }},
        "mainEntityOfPage": "{canonical}",
        "inLanguage": "de-DE",
        "about": {{ "@type": "Thing", "name": "Notenschlüssel {region_name}{(' ' + schulform) if schulform else ''}" }}
      }},
      {{ "@type": "SoftwareApplication", "@id": "https://notenrechnerapp.de/#app", "name": "Der Notenrechner", "applicationCategory": "EducationApplication", "operatingSystem": "iOS, iPadOS, Android", "downloadUrl": "https://apps.apple.com/de/app/der-notenrechner/id1662507346", "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "EUR" }}, "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.5", "ratingCount": "6", "bestRating": "5", "worstRating": "1" }} }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {breadcrumb_items}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {faq_schema}
        ]
      }}
    ]
  }}
  </script>
  <style>{CSS}</style>
</head>
<body>
{NAV_HTML}
  <main>
    <section class="tool-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Brotkrumen">
          {breadcrumbs_html}
        </nav>
        <div class="tool-hero-header">
          <h1>{h1_lead}<span>{h1_accent}</span></h1>
          <p class="tool-hero-sub">{p["summary"]}</p>
        </div>

        <div class="calc">
          <div class="calc-card">
            <div class="calc-controls">
              <div class="calc-field">
                <label for="preset">Schlüssel</label>
                <select id="preset" class="calc-select" autocomplete="off">
                  <option value="50"{' selected' if default_preset == '50' else ''}>50 % (streng)</option>
                  <option value="45"{' selected' if default_preset == '45' else ''}>45 % (mittel)</option>
                  <option value="40"{' selected' if default_preset == '40' else ''}>40 % (milde)</option>
                </select>
              </div>
              <div class="calc-field">
                <label for="maxPts">Maximalpunktzahl</label>
                <input type="text" id="maxPts" class="calc-input" inputmode="decimal" value="{default_max}" autocomplete="off">
              </div>
              <div class="calc-field">
                <label for="achieved">Erreichte Punkte</label>
                <input type="text" id="achieved" class="calc-input" inputmode="decimal" placeholder="?" autocomplete="off">
              </div>
            </div>
            <div class="calc-result" id="calcResult" aria-live="polite" style="background: var(--border-light); color: var(--text-muted);">
              <div class="calc-result-label">Notenpunkte</div>
              <div class="calc-result-grade" id="resultGrade">—</div>
              <div class="calc-result-desc" id="resultDesc">Punkte eingeben</div>
              <div class="calc-result-pct" id="resultPct"></div>
            </div>
          </div>

          <div class="grade-table-wrap">
            <div class="grade-table-head">Notenschlüssel-Tabelle</div>
            <table class="grade-table" role="table">
              <thead><tr><th>Notenpunkte</th><th>Mindestpunktzahl</th></tr></thead>
              <tbody id="tableBody"></tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <article class="content-prose">
          <h2>{p["intro_h2"]}</h2>
          {intro_paras}

          {section_block}

          <h2>{p["context_h2"]}</h2>
          {context_paras}

          <h2>Häufige Fragen</h2>
          <div class="faq-list">{faq_html}
          </div>

          <div class="internal-links">
            {internal_links}
          </div>
        </article>
      </div>
    </section>

    <section class="cta-banner">
      <div class="cta-banner-content">
        <h2>Klausuren bewerten, Klassen führen, Zeugnisse berechnen.</h2>
        <p class="cta-banner-sub">Der Notenrechner — kostenlos im App Store. Lokal, ohne Account, ohne Werbung.</p>
        <a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="app-store-badge">
          <span class="app-store-badge-icon"><svg viewBox="0 0 384 512"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg></span>
          <span class="app-store-badge-text"><span class="app-store-badge-small">Laden im</span><span class="app-store-badge-large">App Store</span></span>
        </a>
      </div>
    </section>
  </main>

  <footer class="footer">
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
    navToggle.addEventListener('click', () => {{
      const open = !navLinks.classList.contains('open');
      navToggle.classList.toggle('active', open);
      navLinks.classList.toggle('open', open);
      navToggle.setAttribute('aria-expanded', String(open));
    }});
    function closeMenu() {{ navToggle.classList.remove('active'); navLinks.classList.remove('open'); navToggle.setAttribute('aria-expanded', 'false'); }}
    {CALC_SCRIPT}
  </script>
</body>
</html>"""


def main():
    for region in REGIONS:
        region_out = OUT_BASE / region["slug"]
        region_out.mkdir(parents=True, exist_ok=True)
        for p in region["pages"]:
            if p["slug"] == "":
                target = region_out / "index.html"
            else:
                d = region_out / p["slug"]
                d.mkdir(exist_ok=True)
                target = d / "index.html"
            target.write_text(render_page(p, region), encoding="utf-8")
            rel = f"/notenschluessel-rechner/{region['slug']}/" + (p["slug"] + "/" if p["slug"] else "")
            print(f"  wrote {rel}index.html")


if __name__ == "__main__":
    main()
