# Handle bad data gracefully — custom exceptions + logging

## Task

Make the LoRa parser fail honestly instead of crashing on a raw built-in
exception or silently continuing: detect a malformed log line, raise a
custom exception type for it, decide (and justify) whether parsing should
stop entirely or skip and continue, and replace ad-hoc diagnostic `print()`s
with the `logging` module.

## Tools

- A custom exception — `class MalformedLogLineError(ValueError): pass`
- `try` / `except SomeSpecificError:` — catching one named type, not a bare
  `except:`
- `raise` inside an `except` block, to translate a caught error into a more
  specific one
- `logging.getLogger(__name__)` per module, `logging.basicConfig(...)` once
- Log levels (`.info()`, `.error()`) vs. plain `print()`

## How it works

- Subclassing `ValueError` means `except ValueError` will also catch a
  `MalformedLogLineError` (it *is* one) — but the reverse doesn't hold.
  `except MalformedLogLineError` will **not** catch a plain `ValueError` from
  somewhere else (like `float("")`), because Python has no way to know a
  generic `ValueError` should be treated as your custom type unless your own
  code explicitly raises it as one. This was the source of an early bug:
  trying to catch the custom type directly around code that only ever
  raises the generic one.
- First attempt at "stop processing" caught the error internally and
  returned `None` instead of raising. This is generally the wrong direction
  in Python — the language favors letting a specific, informative exception
  propagate (EAFP: attempt the operation, catch what actually goes wrong,
  translate/re-raise) over converting a failure into a sentinel value
  (`None`) that every caller has to remember to check. In this case the
  `None` didn't even stop anything — it flowed downstream into
  `sensor_summary`, where `len(None)` raised an unrelated `TypeError` several
  calls away from the real problem, which a bare `except Exception: return`
  in `main()` then silently swallowed entirely (exit code 0, no visible
  error — the opposite of the "fail loudly" goal).
- Fix: raise `MalformedLogLineError` from inside `except ValueError` in
  `read_sensor_data` (translating the built-in error into the domain-specific
  one) and removed *all* exception handling from `main()`. Propagation
  through an uncaught exception is Python's default behavior — nothing extra
  is needed to make an exception "climb out" of a function; what was needed
  was to stop catching-and-suppressing it at two separate levels.
- Design decision: parsing stops entirely on the first malformed line, not
  skip-and-continue — reasoning being that without a retry/continue strategy
  or an idempotency key for a downstream write (e.g. into a database), a
  partial run followed by a re-run risks duplicating data. (Ties directly
  into M8's idempotency/incremental-load territory, much earlier.)
- `logging.basicConfig()` only takes effect on its *first* call in a
  process — calling it from more than one module is order-dependent and
  fragile. The fix: only the entry point (`__main__.py`) calls
  `basicConfig()`; library-ish modules (`parser.py`, `reporter.py`) only ever
  call `getLogger(__name__)` and emit messages, leaving the decision of
  *where those messages go* to the application, not the library.
- Logging an error and also raising it isn't true duplication as a design —
  they serve different purposes (a persistent record vs. immediate flow
  control to the caller). It reads as duplicated right now only because both
  currently render to the same place (console) with no distinct destination
  (e.g. a file handler) configured yet for the log side.
- `sensor_summary`'s `print()` calls were kept as-is (the report is the
  program's actual output/result), while a `logger.info(...)` marks the
  start of building it — diagnostics via logging, the deliverable itself via
  `print()`.

## Small mistakes

- Tried to catch the custom exception type directly around code that only
  ever raised the generic built-in one.
- Used `None` as a "did this fail" signal instead of letting the exception
  propagate — and it didn't even achieve the intended "stop" behavior, since
  nothing was actually checking for it downstream.
- Called `logging.basicConfig()` from more than one module.
