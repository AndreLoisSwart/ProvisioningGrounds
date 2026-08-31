# gitignore scoping

## Task: 
- Set up one `.gitignore` file to exclude at root level so that it only needs to be done once

## Tools:
- Git's `/gitignore` file

## How it works
- The `.gitignore` file recognizes folder patterns and ignores files or folder paths based on what you provide. 
    - Providing `.venv/` with no leading slash isn't anchored to the file's own directory. It matches the folder name at any depth within the tree below the `.gitignore` file.
    - Having a `.gitignore` with an `*` within it will ignore all files and folders where it is located. 