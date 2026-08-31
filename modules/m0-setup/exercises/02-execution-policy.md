# execution policy

## Task: 
- Use powershell to adjust the appropriate execution policy so that we can run powershell scripts. 
    - Get the list of execution policies
    - Set CurrentUser's scope to RemoteSigned

## Tools:
- Powershell 
    - `Get-ExecutionPolicy -List`
    - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## How it works
- `Get-ExecutionPolicy -List` provides a list of scopes
- `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` adjusts the scope to a safe enough policy that allows a user to run scripts that the user wrote, or came with tools like `venv` locally, but blocks scripts that was downloaded from the internet, rather than running Powershell as admin, which will let you change the LocalMachine scope, affecting every user and every script on the machine. This is more than what is needed for running scripts within a venv within my own project. 