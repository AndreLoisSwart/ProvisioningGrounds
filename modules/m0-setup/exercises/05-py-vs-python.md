# py vs python

## Task: 
- Test the difference between `py` and `python`

## Tools:
- Powershell
    - `python -c "import sys; print(sys.executable)"`
    - `py -c "import sys; print(sys.executable)"`

## How it works
- Within an active venv, running `python -c "import sys; print(sys.executable)"` returned the path to the current module's implementation folder, confirming that the isolation works.
- `py` is a single executable installed once, system-wide, independent of any individual Python version. It's more like a dispatcher that looks at a registry of every Python version and decides which one to hand control to (`py -3.11`, `py -3.13`).
    - Running `py -c "import sys; print(sys.executable)"` within an active venv also returned that the `py` executable is also aware of the active venv, which was not always the case with older python versions. 