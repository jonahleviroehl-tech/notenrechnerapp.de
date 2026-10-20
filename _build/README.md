# Statische Website prüfen und pflegen

Die HTML-Dateien sind die veröffentlichte Quelle. Änderungen betreffen ausschließlich dieses Website-Repository; die native App liegt im übergeordneten Projekt.

Lokale Vorschau:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Prüfungen:

```sh
node --test _build/calculations.test.cjs
python3 _build/verify_site.py
```

Für die Python-Prüfung wird `beautifulsoup4` benötigt. Die virtuelle Umgebung des benachbarten SEO-Workspaces enthält diese Abhängigkeit bereits.

`site_common.py` hält die gemeinsamen Plattformpreise, Store-Kampagnen, Navigationslinks und die anfänglichen Rechner-Tabellen konsistent. Die älteren `gen_*.py`-Skripte wenden diese Regeln beim Schreiben an. Ihre Inhalte stammen aus älteren Vorlagen: Generatoren nicht pauschal über die redaktionell ergänzten Seiten laufen lassen. Neue Seiten einzeln erzeugen und den Diff prüfen.

Die gemeinsamen Store-Links enthalten nur drei feste Seitengruppen, keine Nutzerkennung oder Formulareingabe. Apple-Provider-Token und Kampagnen-URLs wurden am 20.10.2026 in App Store Connect erzeugt. Android verwendet einen kodierten UTM-Referrer. Kampagnenwerte sind erst nach ausreichend Store-Daten sichtbar; Installationsklicks in Google Play sind von abgeschlossenen Akquisitionen zu unterscheiden.

Preisstand Deutschland am 20.10.2026: iOS/iPadOS 5,99 EUR, Android kostenlos. Vor Preisänderungen sichtbare Aussagen, strukturierte Daten und `llms.txt` zusammen aktualisieren.
