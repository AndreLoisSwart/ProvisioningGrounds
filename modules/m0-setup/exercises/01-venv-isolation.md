# venv isolation

## Task: 
- Set up a venv environment to scope the python implementation for this module. 
- Check if the implementation is indeed isolated. 

## Tools:
- Powershell 
    - Ran the Activate.ps1 to start the venv
    - Get-Command
    - pip show ruff
    - python -m venv <path>

## How it works
- Using the `python` command, Powershell does a PATH lookup, and whichever python.exe is first in your list of folders will be used. Running a venv exploits this mechanism by putting the current venv's Scripts folder to the front of the PATH list. 
- venv provides true isolation by having its own `site-packages` folder. pip show <package> outputs evidence that the package in question is indeed isolated to the specific venv folder.