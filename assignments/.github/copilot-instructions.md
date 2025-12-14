<!-- Copilot instructions for PFDA assignments workspace -->
# Repository-specific guidance for AI coding agents

This repository contains short teaching assignments (Python script(s) and Jupyter notebooks). The guidance below focuses on the concrete, discoverable patterns needed to be immediately productive in this workspace.

## Big picture
- Purpose: a small collection of student assignments. Key artifacts are `assignment02-bankholidays.py` (script) and `assignment03-pie.ipynb` (notebook). There is no complex service architecture or CI configured.
- Code layout: top-level Python scripts and Jupyter notebooks live in the repository root. Data files (if any) will typically be read by notebooks/scripts using relative paths.

## Key files to inspect
- `assignment03-pie.ipynb` — example notebook that imports `pandas`, `matplotlib.pyplot`, and `collections.Counter`. Use it as the canonical example for notebook style and data visualization patterns.
- `assignment02-bankholidays.py` — a standalone Python script (script-style conventions apply: run with `python3`).
- `README.md` — currently empty; do not assume it contains setup instructions.

## Developer workflows (concrete commands)
- Install runtime dependencies (not all dependencies are listed in the repo):

```
python3 -m pip install pandas matplotlib
```

- Run a script:

```
python3 assignment02-bankholidays.py
```

- Open and run notebooks with Jupyter or VS Code's notebook runner. There is no automated test runner in this repo.

## Project-specific conventions and patterns
- Notebooks are used for assignments; prefer small, self-contained cells that import only what they need. Example imports from `assignment03-pie.ipynb`:

```
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
```

- Visualization code uses `matplotlib`. When adding new notebooks, follow the same import style and prefer clear inline figures (e.g., `%matplotlib inline` in notebook top cell if required by the environment).
- Prefer explicit relative paths for any CSV/data used by notebooks so students can run code without changing working directories.

## Integration points & external dependencies
- External dependencies are standard Python packages (pandas, matplotlib). There are no web services, databases, or CI hooks to integrate with.

## When modifying or adding files
- Notebooks: keep narrative text in markdown cells and code in code cells; follow the existing assignment style (brief header, short explanation, then code). See `assignment03-pie.ipynb` for an example header and import block.
- Scripts: keep them runnable with `python3 scriptname.py` and avoid relying on environment-specific paths.

## What the agent should avoid
- Do not invent missing CI/test config or make assumptions about required packages beyond what is discoverable in code or direct user instructions.

## Example suggested edits (how to be helpful)
- If adding installation help, add a `requirements.txt` with pinned versions and update `README.md` with the install/run commands.
- If enhancing the notebook, ensure plots render inline and add a short explanation cell for each major step.

## Questions to ask the user when unclear
- Where should data files live (root, `data/`, or external)?
- Do you want a `requirements.txt` or a `pyproject.toml` added for reproducible installs?

---
If you'd like, I can (1) add a minimal `requirements.txt`, (2) update `README.md` with install/run instructions, or (3) convert the notebook imports to include an inline `%matplotlib inline` cell — tell me which and I'll proceed.
