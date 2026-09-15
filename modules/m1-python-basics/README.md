# M1 — Python basics I

**Status:** completed

## Goal

Get comfortable writing real Python from a blank file — variables, core types,
functions, control flow, and string handling — by building small pieces of real
embedded/radio logic instead of textbook drills.

## Scope

- Variables, values, and core types (`str`, `float`, `bool`, `tuple`)
- Functions — parameters, return values, composing small functions together
- Control flow — `if` / `elif` / `else` branching
- Strings — f-strings, `.strip()`, `.upper()`, `.split()`, `.join()`

## Covered in completed module

- Exercise 1 — vacuum auto-on decision logic: three-state threshold branching
  (idle / running / fault) for a current-sensor + relay circuit
    - Split "decide the state" and "format it as a string" into two separate
      functions rather than one doing both
    - Wrote `list_of_amps` as a tuple literal by mistake — parentheses + commas
      make a tuple, not a list; renamed to match what it actually held
    - Had a redundant re-check of the lower bound inside an `elif` — once the
      preceding `if` fails to match, that condition is already known true
    - Pulled hardcoded thresholds out into named module-level constants instead
      of leaving magic numbers inline
    - Added `if __name__ == "__main__":` unprompted — every module gets a
      `__name__` set by the interpreter (`"__main__"` when run directly, the
      module's own name when imported); the guard means the block only runs on
      direct execution
    - Confirmed type hints are documentation only — the interpreter doesn't
      enforce them at runtime (a mixed `int` in a tuple typed as `float` ran
      fine); a real type checker (`mypy`) would be needed to catch that
- Exercise 2 — LoRa packet builder: clean and validate raw `(callsign,
  message)` pairs against a payload-size budget
    - First pass used `.replace("  ", " ")` to collapse double spaces — this
      only fixes runs of exactly two, since `.replace()` scans for
      non-overlapping matches; a run of three-plus spaces doesn't fully
      collapse
    - Fixed with `" ".join(message.split())` — `.split()` with no separator
      treats any run of whitespace as one delimiter, so this normalizes to
      single spaces regardless of run length
    - Verified the fix by deliberately adding triple-space runs to the sample
      data and re-checking the output
    - Split cleaning and packet-building into three focused functions
      (`format_callsign`, `clean_message`, `build_payload`) instead of one
      function doing both — same decision/presentation split as Exercise 1
    - Learned `ruff check` (linter, reports diagnostics) and `ruff format`
      (formatter, silently rewrites on save) are different things — no lint
      complaint doesn't mean nothing happened

## Small mistakes

- Tuple literal named like a list (Exercise 1) — caught in review, renamed.
- `.replace()` whitespace bug (Exercise 2) — only surfaced once triple-space
  test data was added; the original sample data happened not to expose it.
