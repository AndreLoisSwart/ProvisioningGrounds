# editor integration

## Task: 
- Set up VSCode's formatter, default interpreter.

## Tools:
- `.vscode/settings.json`

## How it works
- `[python]` scopes the formatter to python files only
    - `"editor.defaultFormatter": "charliermarsh.ruff"` set's VSCode's formatter to the ruff extension.
    - `"editor.formatOnSave": true` formats your code within `.py` files upon saving.
    - `"python.defaultInterpreterPath": "./.venv/Scripts/python.exe"` is a relative path to a .venv so that the setting works on any machine trying to work on this course, regardless of the module worked on.