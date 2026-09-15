# LoRa sensor-log parser

## Task

Parse a small LoRa gateway log file (comma-separated
`timestamp,node,temp=X,batt=Y` lines) into structured records, then report
how many readings there are, which distinct nodes sent them, and the average
battery voltage across all readings.

## Tools

- `pathlib.Path`, including `Path(__file__).resolve().parent` to build a
  path relative to the script itself rather than hardcoding one
- `open(path)` used with a `with` block
- Iterating a file object line by line — `for line in f:`
- `str.split(",")` / `str.split("=")` for pulling fields out of each line
- Building a `list[dict]` of records
- A set comprehension for deduplicating node IDs
- A list comprehension for pulling out just the battery voltages
- `sorted()` to get deterministic output from something that came out of a
  `set`

## How it works

- `Path(__file__).resolve().parent` (chained with further `.parent`s as
  needed) gives a path anchored to wherever the script file itself lives on
  disk — independent of which machine or working directory the script is
  run from. Fixed a first version that hardcoded an absolute path tied to
  one specific machine's home directory.
- `float()` strips leading/trailing whitespace as part of converting a
  string — including a trailing `\n` left over from a line that wasn't
  stripped first. Confirmed this is why an un-stripped line still parsed
  correctly, though only because the numeric field happened to be last on
  the line.
- A `set` guarantees distinct values but not order — `sorted()` converts it
  (or any iterable) into a new, ordered `list`.
- `average()` was written once as a standalone function and reused for the
  battery-voltage calculation rather than duplicating the sum/len logic
  inline.
