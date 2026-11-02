# Repository Guidelines

## Project Structure & Module Organization

This repository contains Python tutorials and examples for building AI agents with LangChain and related tools. Application code lives in `src/ai_agents_from_scratch/`. The package's `__init__.py` defines the CLI entry point; `main.py` currently demonstrates environment loading. Keep new modules inside this package and use descriptive names such as `tools.py` or `chat_agent.py`.

`pyproject.toml` defines dependencies, packaging, and commands. `uv.lock` records resolved dependencies, and `.python-version` selects the local Python version. There are currently no test or asset directories.

## Build, Test, and Development Commands

Use Python 3.14 or newer and run commands from the repository root:

- `uv sync`: install the locked project dependencies and local package.
- `uv run ai-agents-from-scratch`: run the CLI defined in `pyproject.toml`.
- `uv build`: build source and wheel distributions with the configured `uv_build` backend.
- `uv run black src`: format Python source.
- `uv run isort src`: sort imports.
- `uv run black --check src` and `uv run isort --check-only src`: check formatting without changing files.

## Coding Style & Naming Conventions

Use four-space indentation, `snake_case` for functions and modules, `PascalCase` for classes, and `UPPER_SNAKE_CASE` for constants. Add type annotations to new function signatures. Black and isort are included as dependencies; neither has custom configuration. Keep imports together and isolate executable behavior in functions to avoid work during imports.

## Testing Guidelines

No test framework, test command, or coverage threshold is configured yet. For new behavior, add focused tests under `tests/`, using names such as `test_chat_agent.py`. Document the selected framework and its execution command when introducing tests. Mock external model calls so checks do not require credentials or paid requests.

## Commit & Pull Request Guidelines

Existing commits use short descriptions such as `Add .env file` and `project1-environment-setup`; no strict convention is established. Prefer concise, imperative messages describing one logical change. Pull requests should explain the behavior changed, list validation performed, and link relevant issues. Include example input/output when changing agent behavior.

## Security & Configuration

Keep API credentials in a local `.env` file, which is ignored by Git. Never commit secrets or print their values. The current `main.py` prints environment credentials; remove or redact those statements before running it with real keys or sharing output.
