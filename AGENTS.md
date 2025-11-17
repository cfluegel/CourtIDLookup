# Repository Guidelines

## Project Structure & Module Organization
- `index.html` hosts the full UI stack (HTML, CSS, vanilla JS). Keep UI logic inside the embedded script block and extend `datasetConfig` whenever you add a new `data/*.json` file.
- `data/` stores the official codelists as `GDS.Gerichte_<version>.json`. Follow the existing naming scheme (e.g., `GDS.Gerichte_3.7.json`) so the dropdown can discover updates consistently.
- `serve.py` is the only Python component and simply wraps `http.server`. Prefer adjusting its CLI flags (`--host`, `--port`, `--directory`) over editing the script.

## Build, Test, and Development Commands
- `python3 serve.py` – starts the threaded HTTP server at `http://127.0.0.1:8000/index.html`; tweak `--host/--port` instead of editing code.
- `python3 serve.py --directory $(pwd)/data` – serves only the datasets so you can validate fetch paths or inspect responses with browser devtools.

## Coding Style & Naming Conventions
- HTML/CSS: keep the existing two‑space indentation, lowercase element names, and CSS custom properties for colors (`--pastel-green`).
- JavaScript: prefer `const` and `let`, camelCase for functions (`populateVersions`, `handleSearch`), and early returns for validation; avoid external dependencies to keep the page standalone.
- Data files: ensure UTF‑8 encoding and arrays shaped like `[code, description]` inside the `daten` key so the filtering logic continues to work.

## Testing Guidelines
- Smoke-test every change by running `python3 serve.py`, loading `index.html`, cycling through each version, and searching for known prefixes such as `A10`.
- After data or logic edits, confirm first/last entries render, watch the network tab to ensure caching prevents refetches, and rely on temporary `console.assert` statements that you delete before committing.

## Commit & Pull Request Guidelines
- Git history currently uses short sentence-style summaries (e.g., “Another Vibe Coding Session done”)—continue with concise, descriptive messages like `Add version 3.7 dataset`.
- In PR descriptions, cite issue numbers, credit the source of any new JSON, and attach screenshots when UI layout or palette changes.
- List the manual test steps you ran (`python3 serve.py`, browsers, search prefixes) so reviewers can replay them quickly.

## Data & Security Notes
- Only commit upstream XJustiz files obtained from trusted portals; include the publication date in the PR description for traceability.
- Avoid embedding secrets or external URLs—`fetch` must stay relative so the tool works from static hosting and local servers alike.
