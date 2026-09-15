# M2 — Python basics II

**Status:** completed

## Goal

Read and structure real file-based data — the way a lot of data-engineering
work actually starts, from raw text/log files rather than a clean database —
by building a small LoRa sensor-gateway log parser.

## Scope

- Collections — `list`, `dict`, `set`
- Comprehensions — list and set comprehensions
- Iteration — `for` loops, line-by-line file iteration
- File I/O — `pathlib.Path`, `open()` as a context manager

## Covered in completed module

- Exercise 1 — LoRa sensor-log parser: reads a gateway log file
  (`readings.txt`), parses each line into a `dict` record, and reports a
  summary (reading count, distinct nodes, average battery voltage)
    - Used `pathlib.Path` + `open()`/`with` for reading a file line by line
    - Built a `list[dict]` of parsed records with a plain `for` loop
    - Used a set comprehension (`{item["node"] for item in data}`) to dedupe
      node IDs
    - Used a list comprehension to pull out just the battery voltages before
      averaging
    - First version hardcoded an absolute path tied to one specific
      machine's home directory — broke portability across the multi-machine
      setup; fixed by deriving the data file's location from
      `Path(__file__).resolve().parent...`, so the script finds its own data
      regardless of which machine or working directory it's run from
    - Learned `float()` strips surrounding whitespace (including a trailing
      `\n` left on a line read from a file) as part of parsing — a missing
      `.strip()` on each line happened not to break anything, but only
      because the affected field was last on the line
    - Learned `set` iteration order isn't guaranteed — wrapped the deduped
      node set in `sorted()` before joining, for stable/deterministic output
    - Removed a redundant `float(...)` wrapping a call that already returned
      `float`
    - Recurring naming lesson (third time across M1/M2): a variable should
      describe what it actually holds, not what produced it or what you
      expect it to hold (`lines` holding one line, `voltage` holding a whole
      record, `current_script` holding a directory)

## Small mistakes

- Hardcoded a machine-specific absolute path in the first draft.
- Reused the name `line` for both the raw line and its split fields —
  confusing to read back in a short block.
