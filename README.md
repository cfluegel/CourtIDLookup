# Court ID Lookup

Gerichte, Staatsanwaltschaften und weitere Justizbehörden besitzen eindeutige XJustiz-Kennungen. Die JSON-Codelisten im Ordner `data/` (Versionen 3.2 bis 3.6) enthalten diese Kennungen inklusive Kurzbeschreibung. Dieses Projekt stellt eine eigenständige HTML-Seite zur Verfügung, mit der sich die Kennungen komfortabel suchen lassen.

## Funktionsumfang

- Auswahl der gewünschten Codelisten-Version per Dropdown (Standard ist die neueste Version).
- Suche nach den ersten drei Zeichen oder vollständigen Kennungen.
- Trefferliste mit Kennung und Beschreibung in einem kompakten, aufgeräumten Layout.

## Dateien im Überblick

- `index.html` – Standalone-Seite mit eingebundenem CSS und JavaScript für Suche und Darstellung.
- `data/*.json` – Offizielle Codelisten-Versionen (`GDS.Gerichte_3.2.json` bis `GDS.Gerichte_3.6.json`).
- `serve.py` – Kleiner Helfer zum Starten eines lokalen HTTP-Servers.

## Nutzung

1. **Lokalen Server starten (empfohlen):**
   ```bash
   python3 serve.py
   ```
   Anschließend `http://127.0.0.1:8000/index.html` im Browser öffnen. Host, Port oder Wurzelverzeichnis lassen sich über `--host`, `--port` und `--directory` anpassen.

2. **Direktes Öffnen der Datei:** Ein Doppelklick auf `index.html` funktioniert nur in Browsern, die lokale Datei-Zugriffe per `fetch` zulassen. Für einen zuverlässigen Betrieb sollte deshalb Variante 1 verwendet werden.

## Entwicklung

Die Seite lädt die gewählte JSON-Datei dynamisch, filtert die Datensätze nach Präfix der Court-ID und zeigt die Treffer an. Die Daten werden im Browser gecacht, damit ein Wechsel zwischen Versionen ohne erneuten Netzwerkzugriff möglich ist. Änderungen an den Codelisten können vorgenommen werden, indem weitere JSON-Dateien in `data/` abgelegt und im `datasetConfig`-Array innerhalb von `index.html` ergänzt werden.

Weitere Hinweise zur Mitarbeit, Struktur und Tests findest du im Beitrag [`AGENTS.md`](AGENTS.md).
