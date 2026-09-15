# ProvisioningGrounds — Progress Log

A personal, hands-on Data Engineering bootcamp. This file is the living record of
what the bootcamp is, how it is structured, and what has been built so far. It is
the source of truth across machines — keep it current.

---

## Why this exists

I am an Integration Engineer with 12 years in IT, currently at an iPaaS company
(Flowgear), working mostly in a low-code integration platform plus some C#. My
background is deep in SQL (SQL Server, PostgreSQL), ETL, data integration, and API
integration — I design and build complex data integrations professionally.

I recently interviewed for a Data Engineer role and was rejected for one specific
reason: a gap in Infrastructure as Code / Terraform experience. That is the direct
trigger for this bootcamp.

**Goal:** become genuinely job-ready for Data Engineer roles — solid modern
Python (not just scripting), working Terraform / IaC skills, and cloud data
platform skills (Azure, ADF, Databricks, PySpark) layered on top.

This repo is also meant to *be* a project in its own right — evidence of growth
and initiative, not a folder of throwaway scripts.

---

## How the bootcamp works

Learning is entirely by doing. Every exercise follows the same shape:

1. **The task** — a real problem, drawn from my own interests where possible.
2. **The tools** — the functions / methods / libraries / language features that
   are relevant.
3. **How they work** — enough to understand the tools, not the solution.

Then I attempt it myself. Claude reviews my attempt like a code review (correct /
fragile / Pythonic / how to improve), I revise, and only after I have it working
does Claude show an alternative approach as a comparison. Claude never writes the
solution for me.

Full mentoring instructions for Claude live in `CLAUDE.md`.

---

## Environment & tooling decisions

| Area | Decision |
|---|---|
| OS | Windows 11 |
| Python | 3.12, native install; `venv` + `pip` to start, `uv` introduced later |
| Editor | VS Code + Ruff extension |
| First Terraform target (M5) | Native PostgreSQL + Mosquitto (no containers); `postgresql`, `local`, `tls`, `random` providers |
| Container runtime (if ever needed) | Podman Desktop or Rancher Desktop — not required by the plan |
| Cloud | Azure free tier only, hard spending cap; no AWS/GCP |
| Git workflow | `main` for M0–M4; branches + PRs from M5 onward |

---

## Module map

Status: ✅ done · 🔨 in progress · ⬜ upcoming

### Phase 1 — Python foundations

| # | Module | Status | Notes |
|---|---|---|---|
| M0 | Set up Python from scratch (install, PATH, `py` vs `python`, `venv`, `pip`, editor, Ruff, repo skeleton) | ✅ | |
| M1 | Python basics I — values, variables, types, functions, control flow, strings | ✅ | |
| M2 | Python basics II — collections, comprehensions, iteration, file I/O; build a LoRa sensor-log parser | 🔨 | |
| M3 | Make it a real program — modules/packages, type hints, exceptions, `logging`, `argparse`, `pytest` | ⬜ | |

### Phase 2 — Working Python + first IaC

| # | Module | Status | Notes |
|---|---|---|---|
| M4 | Structured data & modelling — `pathlib`, `csv`, `json`, `datetime`, `collections`, `dataclasses`, `enum`; vintage hand-tool inventory | ⬜ | |
| M5 | First Terraform — providers / resources / **state**, `plan` / `apply` / `destroy`, variables / outputs; provision Postgres + device configs for the LoRa datastore | ⬜ | Switch to branch + PR workflow here |
| M6 | Python + a database — `psycopg` / SQLAlchemy, parameterised queries; first real Extract → Transform → Load into the Terraform-provisioned Postgres | ⬜ | |

### Phase 3 — Pipeline engineering

| # | Module | Status | Notes |
|---|---|---|---|
| M7 | APIs & ingestion — `requests`, pagination, retries, rate limits, auth | ⬜ | |
| M8 | Pipeline robustness & data quality — idempotency, incremental loads, `pydantic` validation, quality gates, integration tests, config | ⬜ | |
| M9 | Orchestration thinking — DAGs, dependencies, scheduling, backfills; a lightweight orchestrator | ⬜ | |

### Phase 4 — Cloud + Spark

| # | Module | Status | Notes |
|---|---|---|---|
| M10 | Azure + Terraform on Azure — resource groups, ADLS Gen2, service principals, remote state, spending cap | ⬜ | |
| M11 | PySpark I — Spark model, DataFrames, transformations / actions, SparkSQL; local then Databricks free tier | ⬜ | |
| M12 | ADF + Databricks — ingestion pipelines, jobs, Delta Lake, bronze / silver / gold | ⬜ | |
| M13 | Capstone — end-to-end DE project: ingest (API + files) → ADLS bronze → PySpark silver/gold → serve; all infra in Terraform; CI; data-quality gates; architecture write-up | ⬜ | |

### Stretch

| # | Module | Status | Notes |
|---|---|---|---|
| M14 | Streaming with Kafka — concepts, Python producer / consumer; Redpanda single-binary or Confluent Cloud free tier | ⬜ | |

The map is a guide, not a contract. Pace and scope adjust as we go.

---

## Exercise log

Newest entries at the top. Template:

```
### YYYY-MM-DD — <module> — <exercise title>
- **Built:** what I made
- **Learned:** concepts / tools that landed
- **Struggled with:** what was hard or still feels shaky
- **Follow-ups:** anything to revisit
```

```
### 2026-09-15 — m1 — LoRa packet builder
- **Built:** a packet builder/validator for a handheld LoRa device — cleans raw `(callsign, message)` pairs (strip/uppercase callsign, normalize whitespace in message), builds `"CALLSIGN:message"`, and reports fit against a payload-size budget.
- **Learned:** `str.split()`/`" ".join()` as the idiom for collapsing arbitrary whitespace runs (vs. `.replace()`, which only fixes exact-length matches); booleans as first-class values worth naming, not just inline `if` conditions; tuple unpacking in a `for` loop; `ruff check` vs `ruff format` are different tools with different feedback (silent vs. diagnostic).
- **Struggled with:** `.replace("  ", " ")` looked like it fixed whitespace but silently failed on 3+ space runs — only surfaced by deliberately testing an edge case, not from the original sample data.
- **Follow-ups:** N/A

### 2026-09-15 — m1 — vacuum auto-on decision logic
- **Built:** decision logic for a shop-vacuum auto-on relay — classifies a current reading as idle/running/fault against named thresholds and prints a readable status line per sample reading.
- **Learned:** splitting "decide" and "format" into separate functions; `elif` branches can assume earlier conditions already failed (no need to re-check the lower bound); tuple vs. list literals; named constants over magic numbers; `if __name__ == "__main__":` and how `__name__` actually gets set; type hints are unenforced at runtime.
- **Struggled with:** first attempt named a tuple `list_of_amps` — mismatch between the literal used and the name given to it.
- **Follow-ups:** N/A

### 2026-08-29 — m0 — setup
- **Built:** basic test file to check if ruff formatting and linting is working. An isolated .venv, a working `.vscode/settings.json` (interpreter pinning + format-on-save), a root-level .gitignore scoped across all future modules, and five exercise briefs + a module README
- **Learned:** Setup of python within venv. Troubleshooting of powershell execution policies. Also set up ruff formatter within vscode. py vs python resolution. gitignore pattern anchoring works across subfolders.
- **Struggled with:** Omitted the path when setting up a venv which mixed the venv internals with the module folders. Powershell execution-policy block. gitignore with a `*` within subfolders that ignored all within that folder.
- **Follow-ups:** N/A
```

---

## Session history

| Date | What happened |
|---|---|
| 2026-08-28 | Bootcamp planned: goals, teaching contract, environment decisions, module map. Created `CLAUDE.md` and this file. |
| 2026-09-14/15 | M1 completed — two exercises (vacuum auto-on logic, LoRa packet builder), each through several review/revise passes. Also picked up a second dev machine (CachyOS Linux, Code – OSS editor, fish shell) alongside the original Windows 11 box. |
