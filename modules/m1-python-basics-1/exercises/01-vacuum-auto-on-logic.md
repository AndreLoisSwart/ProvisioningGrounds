# Vacuum auto-on decision logic

## Task

Model the decision logic for a shop-vacuum auto-on relay (current sensor +
relay project): given a current reading in amps, decide whether the vacuum
should be idle, running, or in fault (overcurrent), then print a
human-readable status line for a handful of sample readings.

## Tools

- `def` / `return` — function definition and return values
- `if` / `elif` / `else` — branching, evaluated top to bottom, first true
  branch wins
- Comparison operators (`<=`, `>`)
- Named constants for thresholds instead of magic numbers
- f-strings for building the status line
- `for` loop over a tuple of sample readings
- `if __name__ == "__main__":` guard (added on own initiative, not assigned)

## How it works

- Split the work into two functions: one decides the state, a separate one
  formats it as a string — keeping decision logic and presentation logic
  apart.
- Initially wrote `list_of_amps` as a tuple literal — parentheses + commas
  make a tuple, not a list; fixed the name to match what it actually held.
- Initially re-checked the lower bound inside the `elif` even though the
  preceding `if` had already ruled it out — simplified once it was clear
  `elif` branches only run after every earlier condition has failed, so the
  lower bound is already guaranteed.
- Pulled hardcoded thresholds (`0.4`, `15`) out into named module-level
  constants (`IDLE`, `RUNNING`).
- `__name__ == "__main__"`: every module gets a `__name__` attribute set by
  the interpreter — `"__main__"` when the file is run directly, the module's
  own name when it's imported elsewhere. The guard means the block only
  executes on direct execution.
- Type hints are documentation only — the interpreter doesn't enforce them at
  runtime. Confirmed this with a mixed `int`/`float` tuple entry (`20` instead
  of `20.0`) that ran fine despite the `float` type hint; a real type checker
  (`mypy`) would be needed to catch that mismatch.
