# Make it a real CLI — argparse

## Task

Replace the hardcoded file path and fixed logging level with actual
command-line options: an optional `-f`/`--file` to point at a different
sensor log, falling back to `build_path()` when omitted, and a `-v`/
`--verbose` flag that switches logging from `INFO` to `DEBUG`.

## Tools

- `argparse.ArgumentParser()`
- `parser.add_argument("-f", "--file", default=None, ...)` — an optional
  named argument
- `parser.add_argument("-v", "--verbose", action="store_true", ...)` — a
  value-less boolean flag
- `parser.parse_args()` — returns a `Namespace` with parsed values as
  attributes

## How it works

- `argparse` generates `--help`/`-h` output automatically from the
  `add_argument()` calls — confirmed by running `python -m lorapackage
  --help` and getting a usage summary with no help text written by hand
  beyond the `help=` strings.
- `required=False` on an optional (`-`/`--`-prefixed) argument is a no-op —
  that's already the default; removed it once pointed out.
- `args.file or build_path()` replaced an `if/else` ternary doing the same
  job — `None` is falsy, so `or` falls through to the default cleanly.
- Real bug caught by the log output itself, not by reasoning about it: the
  entry point's diagnostic messages showed up as `INFO:root:...` instead of
  `INFO:lorapackage.__main__:...`, because `logging.info()`/`logging.debug()`
  are top-level convenience functions **unconditionally bound to the root
  logger** — they ignore any `logger = logging.getLogger(__name__)` sitting
  right next to them. `parser.py`/`reporter.py` were already correctly using
  their own `logger.info(...)`; `__main__.py` had the same `logger` variable
  defined but wasn't actually calling it. Fixed by switching to
  `logger.info(...)` / `logger.debug(...)`.
- After that fix, the logger name for the entry point's own messages showed
  up as `__main__`, not `lorapackage.__main__` — full circle back to M1's
  `if __name__ == "__main__":` lesson: `__name__` is literally the string
  `"__main__"` specifically for the file being run as the entry point
  (here, via `python -m lorapackage`), while everything it *imports*
  (`parser.py`, `reporter.py`) keeps its normal dotted module name. Same
  rule, same variable, showing up in a new place.

## Small mistakes

- Left `logging.info()`/`logging.debug()` (root logger) in the entry point
  instead of the module's own named `logger` instance — only visible by
  actually reading the log output's logger-name field, not from the code
  alone.
