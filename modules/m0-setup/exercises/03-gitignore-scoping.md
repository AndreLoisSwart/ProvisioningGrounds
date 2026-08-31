# gitignore scoping

## Task: 
- Diagnosing/fixing of leftover stray `.gitignore` file
- Set up `.gitignore` file to exclude at root level

## Tools:
- Git's `.gitignore` file
- Git
    - `git status --ignored`
    - `git check-ignore -v <path>`

## How it works
- The `.gitignore` file recognizes folder patterns and ignores files or folder paths based on what you provide. 
    - Providing `.venv/` with no leading slash isn't anchored to the file's own directory. It matches the folder name at any depth within the tree below the `.gitignore` file.
    - Botched first venv attempt left a `.gitignore` with an `*` inside it, which silently swalled some files. Using `git status --ignored` and `git check-ignore -v <path>` assisted in norrowing it down.