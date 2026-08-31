# M0 — Set up Python from scratch

**Status:** completed

## Goal

End with a working Python environment I understand, not one I copied — and the
repo skeleton to build the rest of the bootcamp in.

## Scope

- Install Python 3.13 on Windows; understand PATH and `py` vs `python`
- Virtual environments — what `venv` is and why, creating and activating one
- `pip` and a dependency file
- VS Code + the Ruff extension
- Repo skeleton and a `.gitignore` for Python
- A small script that confirms the environment works


## Covered in completed module

 - Python installation globally and scoped to a venv completed along with a package
    - Used Set-ExecutionPolicy to correct CurrentUser's permissions on running venv
    - Used Get-Command to double check where the packages are installed
    - Used Get-ChildItem to view files and folders within my current folder/venv
 - Discussed and set up gitignore file and learned about excluding the same file/folder within sub folders from one root gitignore file 
    - Excluded:
        - .venv/
        - __pycache__/
        - .ruff_cache/
 - Set up the ruff formatter within vscode's settings.json file to format on save, and point it to the interpreter
 - Set up the python interpreter scoped to the venv for module 0
 - Tested the ruff extension in test.py; 
    - It corrected the spacing issues and underlined the unused import
    - It also corrected the assigned but not used x variable
- Learnt that if you have multiple python.exe installed, without venv, the first python.exe in the PATH list will be used
- py is a single executable installed once and can be used to target a specific version, but also checks for an active venv

## Small mistakes

- First installed venv without a dedicated .venv folder. I did not specify the dir path when I set up the venv
    - Resolved it by wiping the venv implementation files
    - Redid the venv setup