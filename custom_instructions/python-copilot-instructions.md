# GitHub Copilot Instructions for This Repository (Python)

## General goals
- Write clear, maintainable Python code.
- Prefer readability and simplicity over clever one-liners.
- Follow existing patterns and conventions already present in this repo.

## Languages and stack
- Primary language: **Python**.
- Target Python version: **3.x** (see `pyproject.toml`, `setup.cfg`, or `requirements.txt` for exact version).
- Prefer using **standard library** and existing internal utilities before adding third-party dependencies.

## Code style
- Follow **PEP 8** unless the existing code clearly uses a different style.
- Respect configuration from:
  - `pyproject.toml`
  - `setup.cfg`
  - `tox.ini`
  - `.editorconfig`
  - Any lint/format configs (e.g. `ruff.toml`, `.flake8`, `black` config).
- Naming:
  - `snake_case` for functions, methods, and variables.
  - `PascalCase` for classes.
  - `CONSTANT_CASE` for constants.
- Prefer:
  - Type hints for all new public functions and methods.
  - `pathlib.Path` over raw string paths when practical.
  - `dataclasses` or `pydantic` models if they are already used in the repo.

## Architecture & patterns
- Follow the existing module and package layout.
- Place new modules/packages alongside similar existing ones.
- Reuse existing helpers, utilities, and base classes instead of duplicating logic.
- Keep functions small and focused; extract helpers when logic grows too complex.

## Error handling & logging
- Use existing logging setup (e.g. `logging.getLogger(__name__)`) instead of `print`.
- Raise specific exception types when possible.
- Avoid swallowing exceptions silently; log or re-raise with context.

## Testing
- Use the existing test framework:
  - If `pytest` is present, write **pytest-style** tests.
  - If `unittest` is used, follow the existing class-based test style.
- Put new tests:
  - In the `tests/` directory, mirroring the package structure, or
  - Next to the code if that pattern already exists.
- When adding features or fixing bugs:
  - Add at least one test that covers the new behavior or regression.
- Use fixtures, factories, and helpers that already exist in `tests/` instead of inventing new patterns.

## Documentation & comments
- Add docstrings for public functions, classes, and methods:
  - Follow the existing docstring style (e.g. Google, NumPy, Sphinx).
- Comment non-obvious code and tricky edge cases.
- Update any relevant `README.md` or module-level documentation when behavior changes.

## Dependencies
- Prefer using dependencies that are already in `requirements.txt` / `pyproject.toml`.
- Do **not** introduce new dependencies unless explicitly requested.
- If a new dependency is truly necessary, note it explicitly in the explanation and where to add it.

## CLI, scripts, and tools (if applicable)
- For CLI tools, reuse existing argument parsing style (`argparse`, `click`, `typer`, etc.).
- Keep scripts idempotent and safe to run multiple times where possible.

## What NOT to do
- Do not change public APIs or function signatures without calling this out clearly.
- Do not introduce large, generic boilerplate (e.g. unused classes, unused layers) that the repo does not already use.
- Avoid mixing unrelated refactors with functional changes in a single suggestion.

## When unsure
- Prefer small, composable changes.
- When there are multiple reasonable designs, outline 2–3 options briefly in comments or in the explanation so the user can choose.
