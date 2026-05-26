# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
make test
# or: poetry run pytest tests

# Run a single test
poetry run pytest tests/test_true_or_false.py::test_list

# Lint
poetry run flake8 true_or_false/

# Build the distribution package
make build

# Publish to PyPI (runs build first)
make publish
```

## Architecture

This is a single-function Python package published to PyPI as `true-or-false`.

- `true_or_false/true_or_false.py` — contains the two public functions:
  - `true_or_false(s, none_is_false=True, blank_is_false=True)` — converts bool/int/str/list/dict/None to a Python bool using hardcoded TRUES/FALSES string lists (multilingual: English, French, German, Russian, etc.). Returns `None` for unrecognized input.
  - `environ_true_or_false(env_var, default=None)` — thin wrapper that reads an env var and delegates to `true_or_false` with `none_is_false=False`.
- `true_or_false/__init__.py` — re-exports both functions; this is the public API.
- `tests/test_true_or_false.py` — parametrized pytest suite covering string variants, booleans, int, None, list, dict, and blank string inputs.

When adding new recognized strings (e.g., a new language's word for yes/no), update both `TRUES` and `FALSES` lists in `true_or_false.py` and add corresponding test cases in the parametrize block.
