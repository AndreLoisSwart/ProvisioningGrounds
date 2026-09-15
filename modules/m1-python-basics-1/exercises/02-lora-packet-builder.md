# LoRa packet builder

## Task

Clean and validate a batch of raw `(callsign, message)` pairs for a handheld
LoRa messaging device: normalize whitespace and casing, build the on-air
packet as `"CALLSIGN:message"`, and report whether each packet fits a payload
budget (and by how much, either way).

## Tools

- String methods — `.strip()`, `.upper()`, `.split()` (no-arg), `" ".join(...)`
- `len()` for packet size
- Boolean values as a first-class type — a comparison stored in a named
  variable (`under_budget`) rather than only ever used inline in an `if`
- Tuple unpacking in a `for` loop — `for callsign, message in pairs:`
- Named constant for the payload budget

## How it works

- First pass used `.replace("  ", " ")` to collapse double spaces. This only
  fixes runs of exactly two spaces, because `.replace()` scans left to right
  for non-overlapping matches — a run of three or more spaces doesn't fully
  collapse in a single pass. The original sample data happened not to contain
  any 3+ space runs, so the bug was silent until deliberately tested for.
- Fixed with `" ".join(message.split())` — `.split()` called with no
  separator treats any run of whitespace as a single delimiter, so joining
  the result back with single spaces normalizes runs of any length.
- Verified the fix by adding triple-space runs to the sample messages and
  re-checking the output.
- Split cleaning and packet-building into three focused functions
  (`format_callsign`, `clean_message`, `build_payload`) instead of one
  function doing both — mirrors the decision/presentation split from
  Exercise 1.
- Confirmed `ruff check` (linter, reports diagnostics) and `ruff format`
  (formatter, silently rewrites on save) are different things — no lint
  complaint doesn't mean the formatter did nothing.
