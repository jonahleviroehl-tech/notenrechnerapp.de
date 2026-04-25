"""Generates 16 per-Notenpunkt landing pages at /notenpunkte/{0..15}/.

Each page is a self-contained HTML doc that mirrors the v3 Neutral Workbench
design from the rest of the site. Per-NP content is curated below; the only
templated parts are head meta, hero numbers, and intra-cluster prev/next links.

Run:  python3 website/_build/gen_notenpunkte_pages.py
Output: website/notenpunkte/<N>/index.html  (16 files)
"""

from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent  # website/
OUT_ROOT = ROOT / "notenpunkte"

# ─────────────────────────────────────────────────────────────────────
# Per-NP curated content. The whole quality of the cluster lives here.
# Every "meaning"/"when"/"context" string is hand-written, not formulaic.
# ─────────────────────────────────────────────────────────────────────

NP_DATA = {
    15: dict(
        note="1+", desc="sehr gut", decimal="0,7",
        pct_50="95–100 %", pct_45="95–100 %", pct_40="95–100 %",
        tag="sehr gut",
        intro=(
            "15 Notenpunkte sind die Höchstpunktzahl im deutschen Oberstufen-System "
            "und entsprechen einer 1+ (\"sehr gut plus\"). In der Dezimalumrechnung — "
            "etwa für die Bewerbung an Universitäten — entsprechen 15 Notenpunkte 0,7."
        ),
        meaning=(
            "15 Punkte signalisieren eine herausragende Leistung. In Klausuren bedeutet "
            "das praktisch: keine inhaltlichen Fehler, eigenständige Argumentation, treffsichere "
            "Formulierung. Lehrkräfte vergeben 15 NP nur bei Arbeiten, die deutlich über die "
            "Erwartungen hinausgehen — nicht für reines „alles richtig\". Die Hürde liegt bei "
            "etwa 95 % der erreichbaren Punkte (Standard-Notenschlüssel)."
        ),
        when=(
            "Typisch sind 15 Notenpunkte in Klausuren, in denen der Schüler eigene Bezüge zieht, "
            "Quellen kritisch einordnet oder mathematische Beweise sauber strukturiert. In "
            "manchen Bundesländern werden 15 NP außerdem für besonders kreative Lösungswege "
            "oder über die Aufgabenstellung hinausgehende Eigenleistungen vergeben."
        ),
        studienrelevanz=(
            "15 Punkte entsprechen der Dezimalnote 0,7. Wer im Schnitt 15 NP erreicht, "
            "schließt das Abitur mit dem Maximalschnitt 1,0 ab — die zulassungsstärkste "
            "Position für NC-Studiengänge wie Medizin, Jura oder Psychologie."
        ),
    ),
    14: dict(
        note="1", desc="sehr gut", decimal="1,0",
        pct_50="90–94 %", pct_45="90–94 %", pct_40="90–94 %",
        tag="sehr gut",
        intro=(
            "14 Notenpunkte entsprechen einer glatten 1 — der mittleren Stufe innerhalb "
            "der Notenstufe „sehr gut\". Als Dezimalnote ergibt sich exakt 1,0, also der "
            "perfekte Bewerbungsschnitt für Universitäten."
        ),
        meaning=(
            "14 Punkte stehen für eine sehr gute Leistung ohne nennenswerte Mängel. Inhalte "
            "sind vollständig, die Argumentation ist klar, kleine sprachliche oder formale "
            "Schönheitsfehler werden hier toleriert — anders als bei 15 NP, wo praktisch "
            "perfekt erwartet wird. Im Standard-Notenschlüssel reicht eine 1 ab etwa 90 %."
        ),
        when=(
            "Klausuren mit 14 NP sind durchgängig richtig und gut strukturiert. Im "
            "Mathematik-Leistungskurs zum Beispiel: alle Aufgaben gelöst, kleine "
            "Rechenfehler im Detail, aber sauber dokumentiert. Im Deutsch-Grundkurs: "
            "stimmige Interpretation mit eigenen Bezügen, lediglich ein, zwei sprachliche "
            "Unschärfen."
        ),
        studienrelevanz=(
            "Eine Abinote von 1,0 wird oft mit einem Schnitt von ca. 14 NP erreicht "
            "(je nach Bundesland und Bonusregelung). Damit liegen alle NC-Fächer offen."
        ),
    ),
    13: dict(
        note="1-", desc="sehr gut", decimal="1,3",
        pct_50="85–89 %", pct_45="85–89 %", pct_40="85–89 %",
        tag="sehr gut",
        intro=(
            "13 Notenpunkte entsprechen einer 1- — die untere Tendenz innerhalb der "
            "Notenstufe „sehr gut\". Als Dezimalnote ergibt sich 1,3."
        ),
        meaning=(
            "13 Punkte sind eine sehr gute Leistung mit kleinen, klar erkennbaren Lücken. "
            "Der Schüler beherrscht den Stoff sicher, hat in einem Aspekt aber weniger "
            "tief argumentiert oder ist in einer Teilaufgabe oberflächlich geblieben. "
            "Üblich ab etwa 85 % der Punkte im Standard-Notenschlüssel."
        ),
        when=(
            "Eine 1- bekommt man in Klausuren, die fast vollständig auf hohem Niveau "
            "gelöst sind — mit einer einzelnen Schwachstelle, die nicht ganz die "
            "Spitzenklasse erreicht. Beispielsweise eine elegante Mathematik-Lösung, "
            "in der ein Beweisschritt nicht ausführlich genug begründet wurde."
        ),
        studienrelevanz=(
            "13 NP entsprechen 1,3 — eine extrem starke Dezimalnote. Für die meisten "
            "NC-Studiengänge ist das ausreichend, in besonders zulassungsstarken Fächern "
            "(z. B. Humanmedizin in Spitzenstandorten) reicht es allein über den Schnitt "
            "manchmal nicht ganz, mit Wartezeit oder Auswahlverfahren aber sicher."
        ),
    ),
    12: dict(
        note="2+", desc="gut", decimal="1,7",
        pct_50="80–84 %", pct_45="80–84 %", pct_40="80–84 %",
        tag="gut",
        intro=(
            "12 Notenpunkte entsprechen einer 2+ — die obere Tendenz im Bereich „gut\". "
            "Als Dezimalnote ergibt sich 1,7, was viele Studierende für Bewerbungen oder "
            "Stipendien benötigen."
        ),
        meaning=(
            "12 Punkte sind eine deutlich überdurchschnittliche Leistung. Der Schüler "
            "zeigt sicheres Sachwissen, kann eigene Schlüsse ziehen und macht nur "
            "einzelne, klar begrenzte Fehler. Hürde im Standard-Schlüssel: rund 80 % "
            "der erreichbaren Punkte."
        ),
        when=(
            "Klausuren mit 12 NP sind solide gut: alle Hauptaufgaben gelöst, eine "
            "Teilaufgabe etwas knapp oder mit kleinem Inhaltsfehler. Im Sprachfach "
            "typisch eine treffende Analyse mit einer thematisch unvollständigen "
            "Stelle. In Mathematik etwa: alle Aufgaben gelöst, in einer ein "
            "konzeptioneller Fehlgriff."
        ),
        studienrelevanz=(
            "12 NP entsprechen 1,7 als Dezimalnote. Für die meisten Bachelor-Studiengänge "
            "ohne strengen NC reicht das problemlos; auch viele NC-Fächer sind damit "
            "erreichbar."
        ),
    ),
    11: dict(
        note="2", desc="gut", decimal="2,0",
        pct_50="75–79 %", pct_45="75–79 %", pct_40="75–79 %",
        tag="gut",
        intro=(
            "11 Notenpunkte entsprechen einer glatten 2 — die mittlere Stufe innerhalb "
            "der Notenstufe „gut\". Als Dezimalnote ergibt sich exakt 2,0."
        ),
        meaning=(
            "11 Punkte stehen für eine voll erfüllende, gute Leistung. Es gibt erkennbare, "
            "aber nicht gravierende Mängel — eine Aufgabe mit deutlichen Unschärfen, oder "
            "mehrere kleine Fehler, die in Summe die 1er-Leistung verhindern. Standard-"
            "Schlüssel: ab etwa 75 %."
        ),
        when=(
            "11 NP sind ein sehr häufiges Klausurergebnis von engagierten Schülern, denen "
            "ein klarer Schwachpunkt — meist eine bestimmte Aufgabe oder ein nicht "
            "vollständig verstandenes Konzept — die Bestnote gekostet hat. In der "
            "mündlichen Mitarbeit: regelmäßige, gute Beiträge, ohne dass jede Aussage "
            "punktet."
        ),
        studienrelevanz=(
            "Eine glatte 2 (2,0) als Schnitt öffnet weiterhin viele Studiengänge. NC-Fächer "
            "mit hohem Andrang sind allein über die Note knapp, lassen sich aber häufig "
            "über Wartesemester, Auswahlverfahren oder Tests sichern."
        ),
    ),
    10: dict(
        note="2-", desc="gut", decimal="2,3",
        pct_50="70–74 %", pct_45="70–74 %", pct_40="70–74 %",
        tag="gut",
        intro=(
            "10 Notenpunkte entsprechen einer 2- — die untere Tendenz im Bereich „gut\". "
            "Die Dezimalumrechnung ergibt 2,3."
        ),
        meaning=(
            "10 Punkte sind eine gute Leistung, die in einzelnen Aspekten Schwächen zeigt. "
            "Der Schüler beherrscht die Hauptthemen, hat aber an einer prominenten Stelle "
            "einen größeren Fehler oder lässt eine Teilaufgabe deutlich unter Niveau "
            "stehen. Im Standard-Schlüssel ab ca. 70 %."
        ),
        when=(
            "Eine 2- bekommt man oft in Klausuren, in denen eine Aufgabe deutlich "
            "schwächer gelöst wurde — etwa eine vergessene Definition, ein nicht "
            "verstandener Aufgabentext oder eine inhaltlich gut, aber sprachlich "
            "schwache Argumentation. Mündlich: regelmäßige Beiträge mit gemischter "
            "Qualität."
        ),
        studienrelevanz=(
            "10 NP entsprechen 2,3. Für viele Studiengänge ohne harten NC ein guter Wert; "
            "für Medizin, Psychologie, Lehramt mit hohem NC eher knapp ohne weitere "
            "Bonus-Faktoren (Wartezeit, Test, Auswahlverfahren)."
        ),
    ),
    9: dict(
        note="3+", desc="befriedigend", decimal="2,7",
        pct_50="65–69 %", pct_45="65–69 %", pct_40="65–69 %",
        tag="befriedigend",
        intro=(
            "9 Notenpunkte entsprechen einer 3+ — die obere Tendenz im Bereich „befriedigend\". "
            "Als Dezimalnote ergibt sich 2,7."
        ),
        meaning=(
            "9 Punkte stehen für eine in den Grundzügen erfüllte Leistung mit einigen "
            "deutlichen Schwächen. Der Schüler kennt den Stoff, kann ihn aber nicht "
            "durchgängig sicher anwenden. Standard-Schlüssel: ab etwa 65 %."
        ),
        when=(
            "Eine 3+ entsteht oft, wenn ein paar Aufgaben sehr gut, andere nur "
            "oberflächlich gelöst wurden — typisch in Phasen mit ungleichmäßiger "
            "Vorbereitung. Mündlich: gelegentliche gute Beiträge, sonst eher passiv."
        ),
        studienrelevanz=(
            "Mit einem Schnitt um 9 NP (~2,7) lassen sich die meisten zulassungsfreien "
            "Studiengänge problemlos belegen. NC-Fächer sind ohne weitere Faktoren "
            "deutlich schwieriger zu erreichen."
        ),
    ),
    8: dict(
        note="3", desc="befriedigend", decimal="3,0",
        pct_50="60–64 %", pct_45="60–64 %", pct_40="60–64 %",
        tag="befriedigend",
        intro=(
            "8 Notenpunkte entsprechen einer glatten 3 — die mittlere Stufe der Notenstufe "
            "„befriedigend\" und gleichzeitig der häufigste Notendurchschnitt deutscher "
            "Schüler. Dezimalnote: 3,0."
        ),
        meaning=(
            "8 Punkte signalisieren eine durchschnittliche, im Wesentlichen ausreichende "
            "Leistung. Der Schüler hat den Stoff verstanden, zeigt aber an mehreren Stellen "
            "Lücken oder Unsicherheit. Üblich ab etwa 60 % der erreichbaren Punkte."
        ),
        when=(
            "Eine 3 ist die statistisch häufigste Klausurnote in der Oberstufe. "
            "Typisch: solides Grundverständnis, aber wiederkehrende Fehler bei "
            "Anwendungsaufgaben oder ein insgesamt eher knapper Lösungsumfang. "
            "Mündlich: ein paar Beiträge pro Stunde, qualitativ uneinheitlich."
        ),
        studienrelevanz=(
            "8 NP (3,0) reichen für fast alle zulassungsfreien Studiengänge. NC-Fächer "
            "sind nur über Wartezeit, hohe Hochschultest-Werte oder besondere Auswahl "
            "realistisch."
        ),
    ),
    7: dict(
        note="3-", desc="befriedigend", decimal="3,3",
        pct_50="55–59 %", pct_45="55–59 %", pct_40="55–59 %",
        tag="befriedigend",
        intro=(
            "7 Notenpunkte entsprechen einer 3- — die untere Tendenz im Bereich "
            "„befriedigend\". Als Dezimalnote ergibt sich 3,3."
        ),
        meaning=(
            "7 Punkte sind eine knappe befriedigende Leistung mit klar sichtbaren "
            "Lücken. Mehrere Aufgaben sind nicht oder nur teilweise gelöst, das "
            "Grundverständnis ist aber erkennbar. Standard-Schlüssel: ab etwa 55 %."
        ),
        when=(
            "Eine 3- entsteht, wenn die Hälfte bis zwei Drittel der Klausur richtig ist, "
            "der Rest aber inhaltlich schwach. Im Mündlichen: gelegentliche, eher "
            "fragliche Beiträge."
        ),
        studienrelevanz=(
            "7 NP (3,3) reichen für die meisten offenen Studiengänge. Bei Bewerbungen "
            "auf Stipendien oder NC-Fächer sind weitere Faktoren entscheidend."
        ),
    ),
    6: dict(
        note="4+", desc="ausreichend", decimal="3,7",
        pct_50="50–54 %", pct_45="55–59 %", pct_40="60–64 %",
        tag="ausreichend",
        intro=(
            "6 Notenpunkte entsprechen einer 4+ — die obere Tendenz im Bereich „ausreichend\". "
            "Als Dezimalnote ergibt sich 3,7. Für das Bestehen eines Kurses in der "
            "Oberstufe sind 5 NP nötig — 6 NP liegen also knapp darüber."
        ),
        meaning=(
            "6 Punkte sind eine deutlich unter dem Mittel liegende, aber noch ausreichende "
            "Leistung. Der Schüler beherrscht das Mindeste, ist aber in vielen Bereichen "
            "unsicher. Standard-Schlüssel: ab etwa 50 % beim 50er-Schlüssel; bei "
            "schwierigeren Klausuren mit 45er- oder 40er-Schlüssel entsprechend höher."
        ),
        when=(
            "Eine 4+ in einer Klausur bedeutet meist, dass die Hälfte richtig ist, der "
            "Rest stark lückenhaft. Im Mündlichen: wenige Beiträge, oft ungenau, aber "
            "kein echter Ausfall."
        ),
        studienrelevanz=(
            "6 NP allein reichen nicht für ein gutes Abitur. Die Note ist mit 3,7 als "
            "Dezimal recht schwach — für zulassungsbeschränkte Studiengänge ohne "
            "Wartezeit kaum realistisch."
        ),
    ),
    5: dict(
        note="4", desc="ausreichend", decimal="4,0",
        pct_50="45–49 %", pct_45="50–54 %", pct_40="55–59 %",
        tag="ausreichend",
        intro=(
            "5 Notenpunkte entsprechen einer glatten 4 — die mittlere Stufe „ausreichend\". "
            "Als Dezimalnote ergibt sich 4,0. <strong>Die magische Schwelle:</strong> "
            "5 NP ist die Mindestanforderung zum Bestehen eines Oberstufenkurses."
        ),
        meaning=(
            "5 Punkte sind das ausreichende Mindestmaß. Der Schüler hat die "
            "grundlegenden Inhalte verstanden, kann sie aber kaum sicher anwenden. "
            "Wer unter 5 NP fällt, gilt als „unterpunktet\" — was Konsequenzen "
            "für die Abi-Zulassung hat."
        ),
        when=(
            "Eine glatte 4 entsteht in Klausuren, in denen knapp die Hälfte der Punkte "
            "erreicht wird. Mündlich: wenige, oft korrekte aber nicht weiterführende "
            "Beiträge. Solide untere Mitte des Kurses."
        ),
        studienrelevanz=(
            "5 NP im Schnitt entspricht der Dezimalnote 4,0 — ein Schnitt, mit dem "
            "regulär kaum ein Studienplatz erreichbar ist. Für das reine Bestehen "
            "der Oberstufe und Erreichen des Abiturs aber ausreichend, sofern andere "
            "Kurse den Schnitt anheben."
        ),
    ),
    4: dict(
        note="4-", desc="ausreichend", decimal="4,3",
        pct_50="40–44 %", pct_45="45–49 %", pct_40="50–54 %",
        tag="ausreichend",
        intro=(
            "4 Notenpunkte entsprechen einer 4- — die untere Tendenz im Bereich "
            "„ausreichend\". Als Dezimalnote ergibt sich 4,3. <strong>Wichtig:</strong> "
            "4 Notenpunkte gelten in der gymnasialen Oberstufe bereits als "
            "<em>unterpunktet</em> — also als nicht bestanden für Zwecke der "
            "Abitur-Gesamtqualifikation."
        ),
        meaning=(
            "4 Punkte sind die schwächste Stufe der ausreichenden Leistung. Der Schüler "
            "hat fundamentale Lücken, kann aber einzelne Anteile lösen. Im Standard-"
            "Schlüssel ab etwa 40 %; bei strengeren Klausuren entsprechend höher."
        ),
        when=(
            "Eine 4- bekommen Schüler, die Klausuren nur knapp über der Hälfte der "
            "Aufgaben sinnvoll bearbeiten. Mündlich: kaum aktive Mitarbeit, einzelne "
            "korrekte Antworten."
        ),
        studienrelevanz=(
            "Mit 4 NP gilt der Kurs als unterpunktet. Eine bestimmte Anzahl unterpunkteter "
            "Kurse ist im Abitur erlaubt; wird sie überschritten, ist die Zulassung zur "
            "Abiturprüfung gefährdet."
        ),
    ),
    3: dict(
        note="5+", desc="mangelhaft", decimal="4,7",
        pct_50="33–39 %", pct_45="40–44 %", pct_40="45–49 %",
        tag="mangelhaft",
        intro=(
            "3 Notenpunkte entsprechen einer 5+ — die obere Tendenz im Bereich "
            "„mangelhaft\". Als Dezimalnote ergibt sich 4,7. <strong>Achtung:</strong> "
            "3 NP gelten als unterpunktet."
        ),
        meaning=(
            "3 Punkte stehen für eine Leistung, in der grundlegende Anforderungen "
            "weitgehend nicht erfüllt sind. Mängel im Sachverständnis dominieren, "
            "einzelne Teilaspekte sind aber erkennbar bearbeitet. Standard: ab ca. 33 %."
        ),
        when=(
            "Eine 5+ bekommt man in Klausuren mit klar überwiegend falschen Lösungen, "
            "in denen aber zumindest ein paar Punkte sicher erreicht werden. Mündlich: "
            "fast keine eigene Initiative."
        ),
        studienrelevanz=(
            "3 NP als Kursnote bedeutet einen unterpunkteten Kurs in der Oberstufe. "
            "Für die Abitur-Gesamtqualifikation problematisch."
        ),
    ),
    2: dict(
        note="5", desc="mangelhaft", decimal="5,0",
        pct_50="27–32 %", pct_45="33–39 %", pct_40="40–44 %",
        tag="mangelhaft",
        intro=(
            "2 Notenpunkte entsprechen einer glatten 5 — die mittlere Stufe „mangelhaft\". "
            "Als Dezimalnote ergibt sich 5,0. Auch hier gilt: unterpunktet."
        ),
        meaning=(
            "2 Punkte stehen für deutliche Mängel. Wesentliche Inhalte sind nicht "
            "verstanden, einzelne Teilaspekte zeigen aber, dass der Schüler nicht "
            "vollständig abgehängt ist."
        ),
        when=(
            "Eine 5 entsteht meist bei sehr lückenhafter Klausurbearbeitung — wenige "
            "Aufgaben sinnvoll begonnen, viele falsch oder leer. Mündlich: keine "
            "regelmäßige Beteiligung."
        ),
        studienrelevanz=(
            "2 NP zählen als Kursausfall im Sinne der Abi-Bewertung."
        ),
    ),
    1: dict(
        note="5-", desc="mangelhaft", decimal="5,3",
        pct_50="20–26 %", pct_45="27–32 %", pct_40="33–39 %",
        tag="mangelhaft",
        intro=(
            "1 Notenpunkt entspricht einer 5- — die untere Tendenz im Bereich "
            "„mangelhaft\". Als Dezimalnote ergibt sich 5,3."
        ),
        meaning=(
            "1 Punkt steht für überwiegend fehlerhafte Leistungen mit nur "
            "rudimentären richtigen Ansätzen. Standard-Schlüssel: ab etwa 20 %."
        ),
        when=(
            "Eine 5- entsteht typischerweise, wenn Klausuren zum Großteil unbearbeitet "
            "oder falsch gelöst sind, aber einzelne korrekte Detailantworten existieren."
        ),
        studienrelevanz=(
            "1 NP ist deutlich unterpunktet. Für die Abi-Zulassung hochkritisch."
        ),
    ),
    0: dict(
        note="6", desc="ungenügend", decimal="5,7",
        pct_50="0–19 %", pct_45="0–26 %", pct_40="0–32 %",
        tag="ungenügend",
        intro=(
            "0 Notenpunkte entsprechen einer 6 — die schlechtestmögliche Note im "
            "deutschen Bewertungssystem. Als Dezimalnote ergibt sich 5,7."
        ),
        meaning=(
            "0 Punkte werden vergeben, wenn keine ausreichend bearbeiteten Aufgaben "
            "vorliegen — entweder fast vollständig leer, vollständig falsch, oder "
            "die Klausur wurde ohne berechtigten Grund nicht abgegeben."
        ),
        when=(
            "Eine 6 entsteht praktisch nie aus Versehen — sie wird vergeben bei nicht "
            "abgegebenen Klausuren, vollständigen Themenverfehlungen oder Täuschungs-"
            "versuchen. Mündlich: durchgängige Verweigerung."
        ),
        studienrelevanz=(
            "Ein Kurs mit 0 NP ist nicht bestanden. Die Konsequenzen reichen je nach "
            "Bundesland von Wiederholung bis zur Versagung der Abi-Zulassung."
        ),
    ),
}

assert set(NP_DATA.keys()) == set(range(16)), "must have all 16 NP entries"

# Earth-tone bg + dot tokens per NP value (matches gradeColor() in JS)
def grade_tokens(np: int):
    if np >= 13: return ("--grade-1", "--grade-1-bg")
    if np >= 10: return ("--grade-2", "--grade-2-bg")
    if np >= 7:  return ("--grade-3", "--grade-3-bg")
    if np >= 4:  return ("--grade-4", "--grade-4-bg")
    return ("--grade-5", "--grade-5-bg")


# ─────────────────────────────────────────────────────────────────────
# Page template — single self-contained HTML doc per NP page.
# Placeholders use {NAME} substitution via .format().
# ─────────────────────────────────────────────────────────────────────

TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc_meta}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc_meta}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="Der Notenrechner">
  <meta property="og:image" content="https://notenrechnerapp.de/assets/og-notenpunkte.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc_meta}">
  <meta name="twitter:image" content="https://notenrechnerapp.de/assets/og-notenpunkte.png">
  <meta name="theme-color" content="#2F60C0">
  <meta name="apple-itunes-app" content="app-id=1662507346">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="de" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc_meta}",
    "url": "{canonical}",
    "datePublished": "2026-04-25",
    "dateModified": "2026-04-25",
    "author": {{ "@type": "Organization", "name": "Der Notenrechner", "url": "https://notenrechnerapp.de" }},
    "publisher": {{ "@type": "Organization", "name": "Der Notenrechner", "url": "https://notenrechnerapp.de", "logo": {{ "@type": "ImageObject", "url": "https://notenrechnerapp.de/assets/logo.png" }} }},
    "mainEntityOfPage": "{canonical}"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Der Notenrechner", "item": "https://notenrechnerapp.de/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Notenpunkte-Tabelle", "item": "https://notenrechnerapp.de/notenpunkte-tabelle/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{np} Notenpunkte", "item": "{canonical}" }}
    ]
  }}
  </script>

  <style>
    {css}
  </style>
</head>
<body>
  <nav class="nav" role="navigation" aria-label="Hauptnavigation">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><span class="nav-brand-icon"><img src="/assets/logo.png" alt=""></span>Der Notenrechner</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/" onclick="closeMenu()">Startseite</a></li>
        <li><a href="/notenschluessel-rechner/" onclick="closeMenu()">Notenschlüssel-Rechner</a></li>
        <li><a href="/notenpunkte-tabelle/" class="active" onclick="closeMenu()">Notenpunkte-Tabelle</a></li>
        <li><a href="/ihk-notenschluessel/" onclick="closeMenu()">IHK-Rechner</a></li>
        <li><a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="nav-cta" onclick="closeMenu()" aria-label="Im App Store laden"><svg viewBox="0 0 384 512" fill="currentColor" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>Laden</a></li>
      </ul>
    </div>
  </nav>

  <main>
    <section class="np-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Brotkrumen">
          <a href="/notenpunkte-tabelle/">Notenpunkte-Tabelle</a>
          <span aria-hidden="true">›</span>
          <span aria-current="page">{np} Notenpunkte</span>
        </nav>
        <div class="np-hero-card">
          <div class="np-hero-tag" style="color: var({grade_dot}); background: var({grade_bg})">{tag}</div>
          <div class="np-hero-grid">
            <div class="np-hero-num"><span class="np-hero-pts" style="color: var({grade_dot})">{np}</span><span class="np-hero-pts-label">Notenpunkte</span></div>
            <div class="np-hero-equal" aria-hidden="true">=</div>
            <div class="np-hero-num"><span class="np-hero-trad">{note}</span><span class="np-hero-pts-label">Schulnote</span></div>
            <div class="np-hero-equal" aria-hidden="true">=</div>
            <div class="np-hero-num"><span class="np-hero-decimal">{decimal}</span><span class="np-hero-pts-label">Dezimal</span></div>
          </div>
          <p class="np-hero-intro">{intro}</p>
        </div>

        <div class="np-pct-strip">
          <div class="np-pct-cell"><span class="np-pct-label">50 %-Schlüssel</span><span class="np-pct-value">{pct_50}</span></div>
          <div class="np-pct-cell"><span class="np-pct-label">45 %-Schlüssel</span><span class="np-pct-value">{pct_45}</span></div>
          <div class="np-pct-cell"><span class="np-pct-label">40 %-Schlüssel</span><span class="np-pct-value">{pct_40}</span></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container">
        <article class="content-prose">
          <h2>Was bedeuten {np} Notenpunkte?</h2>
          <p>{meaning}</p>

          <h3>Wann bekommt man {np} Notenpunkte?</h3>
          <p>{when}</p>

          <h3>Bedeutung für Studium und Bewerbung</h3>
          <p>{studienrelevanz}</p>

          <h3>Reverse: Welche Notenpunkte entsprechen der Note {note}?</h3>
          <p>Die Schulnote {note} ({desc}) entspricht in der gymnasialen Oberstufe genau {np} Notenpunkten. Die zugehörige Dezimalnote — etwa für Hochschulbewerbungen — ist {decimal}.</p>

          <h3>Verwandte Werte</h3>
          <div class="np-related">
            {related_links}
          </div>

          <h3>Berechnung mit eigener Klausur</h3>
          <p>Wer einen konkreten Punktestand aus einer Klausur in Notenpunkte umrechnen möchte (z. B. „87 von 100 Punkten\"), nutzt den <a href="/notenschluessel-rechner/">Notenschlüssel-Rechner</a> mit dem passenden Schlüssel (50, 45 oder 40 Prozent). Für die komplette Tabelle aller Notenpunkte siehe <a href="/notenpunkte-tabelle/">Notenpunkte-Tabelle</a>.</p>
        </article>
      </div>
    </section>

    <section class="cta-banner">
      <div class="cta-banner-content">
        <h2>Klausuren, Klassen, Zeugnisse — alles in einer App.</h2>
        <p class="cta-banner-sub">Der Notenrechner ist kostenlos im App Store. Lokal, ohne Account, ohne Werbung.</p>
        <div class="cta-features">
          <div class="cta-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Klausurergebnisse für die ganze Klasse</div>
          <div class="cta-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Klassenschnitt + Verteilungs-Diagramm</div>
          <div class="cta-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Zeugnisnoten mit Mündlich &amp; Teilnoten</div>
          <div class="cta-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>PDF-Export für Konferenzen</div>
        </div>
        <a href="https://apps.apple.com/de/app/der-notenrechner/id1662507346" target="_blank" rel="noopener" class="app-store-badge">
          <span class="app-store-badge-icon"><svg viewBox="0 0 384 512"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184 4 273.5c0 26.2 4.8 53.3 14.4 81.2 12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg></span>
          <span class="app-store-badge-text">
            <span class="app-store-badge-small">Laden im</span>
            <span class="app-store-badge-large">App Store</span>
          </span>
        </a>
        <p class="cta-note">Kostenlos · Keine Werbung · Kein Abo</p>
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
  </script>
</body>
</html>
"""


CSS = dedent("""
:root {
  --primary: #2F60C0;
  --primary-light: #6B94E0;
  --primary-dark: #1F4A9C;
  --primary-50: #EEF3FB;
  --primary-100: #DCE5F5;
  --primary-900: #15336B;
  --bg: #F7F6F3;
  --card: #FFFFFF;
  --surface-subtle: #F1EFEA;
  --text: #0F0F10;
  --text-secondary: #3B3B3F;
  --text-muted: #6E6E73;
  --border: #E8E6E1;
  --border-light: #F1EFEA;
  --grade-1: #15803D; --grade-1-bg: #E6F2EA;
  --grade-2: #4D7C0F; --grade-2-bg: #EFF1E2;
  --grade-3: #A16207; --grade-3-bg: #F8EFE0;
  --grade-4: #C2410C; --grade-4-bg: #FAEADD;
  --grade-5: #B91C1C; --grade-5-bg: #F7E6E6;
  --shadow-card: 0 1px 2px rgba(15,15,16,0.04), 0 0 0 1px rgba(15,15,16,0.04);
  --radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --radius-xl: 24px; --radius-pill: 999px;
  --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --nav-height: 72px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
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
.nav-links a.nav-cta { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 0 22px 0 18px; height: 36px; min-height: 0; line-height: 1; white-space: nowrap; background: var(--primary); color: white !important; border-radius: var(--radius-pill); font-size: 15px; font-weight: 700; letter-spacing: 0.005em; transition: background 0.15s, transform 0.15s; }
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

/* HERO */
.np-hero { padding-top: calc(var(--nav-height) + 40px); padding-bottom: 56px; background: linear-gradient(180deg, var(--bg) 0%, #FBFAF6 100%); border-bottom: 1px solid var(--border); }
.breadcrumbs { font-size: 13px; color: var(--text-muted); margin-bottom: 20px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.breadcrumbs a { color: var(--text-secondary); transition: color 0.15s; }
.breadcrumbs a:hover { color: var(--primary); }
.breadcrumbs span[aria-current] { color: var(--text); font-weight: 500; }
.np-hero-card { max-width: 720px; margin: 0 auto; background: var(--card); border-radius: var(--radius-lg); box-shadow: var(--shadow-card); padding: 32px 28px 28px; text-align: center; }
.np-hero-tag { display: inline-block; padding: 4px 12px; border-radius: var(--radius-pill); font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 18px; }
.np-hero-grid { display: flex; align-items: center; justify-content: center; gap: 18px; margin-bottom: 22px; flex-wrap: wrap; }
.np-hero-num { display: flex; flex-direction: column; align-items: center; gap: 4px; min-width: 100px; }
.np-hero-pts { font-size: 64px; font-weight: 800; line-height: 1; letter-spacing: -0.025em; font-variant-numeric: tabular-nums; }
.np-hero-trad { font-size: 56px; font-weight: 800; line-height: 1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; color: var(--text); }
.np-hero-decimal { font-size: 56px; font-weight: 800; line-height: 1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; color: var(--text-secondary); }
.np-hero-pts-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); }
.np-hero-equal { font-size: 32px; font-weight: 300; color: var(--text-muted); align-self: center; padding-top: 16px; }
.np-hero-intro { font-size: 16px; color: var(--text-secondary); max-width: 540px; margin: 0 auto; line-height: 1.65; }
.np-hero-intro strong { color: var(--text); font-weight: 600; }
.np-hero-intro em { font-style: normal; color: var(--grade-4); font-weight: 600; }
@media (max-width: 600px) {
  .np-hero-pts, .np-hero-trad, .np-hero-decimal { font-size: 48px; }
  .np-hero-equal { font-size: 26px; padding-top: 10px; }
  .np-hero-num { min-width: 80px; }
  .np-hero-grid { gap: 12px; }
}

.np-pct-strip { max-width: 720px; margin: 24px auto 0; background: var(--card); border-radius: var(--radius-md); border: 1px solid var(--border-light); display: grid; grid-template-columns: 1fr 1fr 1fr; }
.np-pct-cell { padding: 14px 18px; text-align: center; border-right: 1px solid var(--border-light); }
.np-pct-cell:last-child { border-right: none; }
.np-pct-label { display: block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 4px; }
.np-pct-value { display: block; font-size: 16px; font-weight: 600; color: var(--text); font-variant-numeric: tabular-nums; }
@media (max-width: 540px) {
  .np-pct-cell { padding: 12px 10px; }
  .np-pct-value { font-size: 14px; }
}

/* CONTENT */
.content-section { padding: 56px 0 72px; }
.content-prose { max-width: 720px; margin: 0 auto; }
.content-prose h2 { font-size: clamp(24px, 3.5vw, 30px); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 14px; }
.content-prose h3 { font-size: 19px; font-weight: 700; margin-top: 36px; margin-bottom: 10px; letter-spacing: -0.01em; }
.content-prose p { font-size: 16px; line-height: 1.75; color: var(--text-secondary); margin-bottom: 14px; }
.content-prose a { color: var(--primary); font-weight: 500; text-decoration: underline; text-underline-offset: 3px; }
.content-prose a:hover { color: var(--primary-dark); }

.np-related { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 12px; }
.np-related-link { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-pill); font-size: 14px; font-weight: 500; color: var(--text); text-decoration: none !important; transition: border-color 0.2s, transform 0.15s; }
.np-related-link:hover { border-color: var(--primary); transform: translateY(-1px); }
.np-related-link strong { font-weight: 700; font-variant-numeric: tabular-nums; color: var(--primary); }
.np-related-link.np-related-back { border-color: var(--primary-100); background: var(--primary-50); }

/* CTA */
.cta-banner { background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%); color: white; text-align: center; padding: 72px 24px; position: relative; overflow: hidden; }
.cta-banner::before { content: ''; position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px); background-size: 24px 24px; }
.cta-banner-content { position: relative; z-index: 1; max-width: 680px; margin: 0 auto; }
.cta-banner h2 { font-size: clamp(24px, 4vw, 32px); font-weight: 800; margin-bottom: 12px; letter-spacing: -0.02em; }
.cta-banner-sub { font-size: 16px; color: rgba(255,255,255,0.9); margin-bottom: 32px; }
.cta-features { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px 24px; margin-bottom: 32px; font-size: 14px; }
.cta-feature { display: inline-flex; align-items: center; gap: 8px; color: rgba(255,255,255,0.95); }
.cta-feature svg { width: 16px; height: 16px; color: rgba(255,255,255,0.85); flex-shrink: 0; }
.app-store-badge { display: inline-flex; align-items: center; gap: 12px; padding: 10px 22px 10px 18px; border-radius: 12px; transition: transform 0.2s, box-shadow 0.2s; min-height: 52px; background: #000; color: white; }
.app-store-badge:hover { transform: translateY(-2px); background: #1a1a1a; box-shadow: 0 10px 28px rgba(0,0,0,0.35); }
.app-store-badge-icon { width: 28px; height: 28px; flex-shrink: 0; }
.app-store-badge-icon svg { width: 100%; height: 100%; fill: currentColor; }
.app-store-badge-text { display: flex; flex-direction: column; line-height: 1; }
.app-store-badge-small { font-size: 11px; font-weight: 400; letter-spacing: 0.02em; margin-bottom: 4px; opacity: 0.9; }
.app-store-badge-large { font-size: 20px; font-weight: 600; letter-spacing: -0.01em; }
.cta-note { font-size: 13px; color: rgba(255,255,255,0.7); margin-top: 16px; }

/* FOOTER */
.footer { background: var(--surface-subtle); padding: 36px 24px; border-top: 1px solid var(--border); }
.footer-inner { max-width: 1120px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.footer-links { display: flex; gap: 24px; list-style: none; flex-wrap: wrap; justify-content: center; }
.footer-links a { font-size: 14px; color: var(--text-secondary); transition: color 0.2s; }
.footer-links a:hover { color: var(--primary); }
.footer-tagline { font-size: 13px; color: var(--text-muted); font-style: italic; }
.footer-copy { font-size: 13px; color: var(--text-muted); }
""")


def related_links_html(np: int) -> str:
    """Produce 'previous / table / next' related links."""
    parts = []
    if np > 0:
        parts.append(
            f'<a class="np-related-link" href="/notenpunkte/{np-1}/">'
            f'<strong>{np-1}</strong> Notenpunkte</a>'
        )
    if np < 15:
        parts.append(
            f'<a class="np-related-link" href="/notenpunkte/{np+1}/">'
            f'<strong>{np+1}</strong> Notenpunkte</a>'
        )
    parts.append(
        '<a class="np-related-link np-related-back" href="/notenpunkte-tabelle/">'
        'Komplette Tabelle (15–0)</a>'
    )
    return "\n            ".join(parts)


def render_page(np: int) -> str:
    d = NP_DATA[np]
    grade_dot, grade_bg = grade_tokens(np)
    title = f"{np} Notenpunkte = Note {d['note']} ({d['decimal']}) | Der Notenrechner"
    desc_meta = (
        f"{np} Notenpunkte entsprechen der Schulnote {d['note']} und der Dezimalnote "
        f"{d['decimal']}. Bedeutung, Prozentbereich und Kontext für Klausuren in der "
        f"gymnasialen Oberstufe."
    )
    canonical = f"https://notenrechnerapp.de/notenpunkte/{np}/"

    return TEMPLATE.format(
        np=np,
        note=d["note"],
        desc=d["desc"],
        decimal=d["decimal"],
        tag=d["tag"],
        intro=d["intro"],
        meaning=d["meaning"],
        when=d["when"],
        studienrelevanz=d["studienrelevanz"],
        pct_50=d["pct_50"],
        pct_45=d["pct_45"],
        pct_40=d["pct_40"],
        grade_dot=grade_dot,
        grade_bg=grade_bg,
        related_links=related_links_html(np),
        title=title,
        desc_meta=desc_meta,
        canonical=canonical,
        css=CSS.strip(),
    )


def main():
    OUT_ROOT.mkdir(exist_ok=True)
    for np in range(16):
        d = OUT_ROOT / str(np)
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render_page(np), encoding="utf-8")
        print(f"  wrote /notenpunkte/{np}/index.html")
    print(f"\nGenerated 16 pages under {OUT_ROOT}")


if __name__ == "__main__":
    main()
