# GATE-03 External Reproduction Packet v0.1

Purpose: restart the lab on the one path that can actually move the MQGT-SCF evidence boundary: an independently reproducible empirical QRNG/count-data run.

This packet is intentionally narrower than the full Theory-of-Everything corpus. It tests only GATE-03. It cannot promote final closure by itself.

## Repo Quick Start

Run the local smoke tests:

```bash
make smoke
make verify
```

Equivalent direct commands:

```bash
python3 scripts/run_smoke_tests.py
python3 scripts/verify_manifest.py
```

The smoke test regenerates a synthetic null set and a deliberately positive synthetic set. Expected decisions:

- synthetic null: `not_promotable`
- synthetic positive: `candidate_support_requires_attestation`

## What This Packet Does

- Defines a preregistered QRNG/control-vs-intervention block design.
- Defines a minimal block-level data schema.
- Provides a standalone stdlib-only analyzer.
- Produces hash-logged output for raw block files and the analysis report.
- Blocks post-hoc gate promotion unless the run is independent and the missing externality requirement is satisfied.

## What This Packet Does Not Do

- It does not solve UV completion.
- It does not prove uniqueness.
- It does not validate interpretive bridge claims.
- It does not close final ToE status.
- It does not use local archived data as independent external reproduction.

## Directory Layout

- `PREREGISTRATION.md` - frozen analysis plan.
- `DATA_SCHEMA.md` - block JSON schema.
- `INDEPENDENT_OPERATOR_CHECKLIST.md` - operator instructions.
- `scripts/analyze_blocks.py` - deterministic block-level analyzer.
- `scripts/make_synthetic_blocks.py` - synthetic smoke-test generator.
- `scripts/run_smoke_tests.py` - local null/positive smoke-test runner.
- `scripts/verify_manifest.py` - SHA-256 manifest verifier.
- `tests/` - generated synthetic smoke-test data.
- `results/` - generated analysis reports.

## Smoke Test

From this directory:

```bash
python3 scripts/make_synthetic_blocks.py --out tests/synthetic_formal_null
python3 scripts/analyze_blocks.py tests/synthetic_formal_null/*.json --out results/synthetic_formal_null_report.json --md-out results/synthetic_formal_null_report.md
```

Expected: the analyzer should report a null/not-promotable result for the synthetic null set.

## Real Independent Run

1. Freeze this packet by recording SHA-256 hashes for every file.
2. Send the frozen packet to an independent operator.
3. Operator collects data without changing this analysis plan.
4. Operator returns block JSON files and raw provenance.
5. Run:

```bash
python3 scripts/analyze_blocks.py independent_blocks/*.json --out results/independent_gate03_report.json --md-out results/independent_gate03_report.md
```

## Decision Boundary

The analyzer can produce only these statuses:

- `not_promotable`: formal criteria are not met or signal is null.
- `candidate_support_requires_attestation`: formal statistical criteria are met, but external attestation/raw-data review is still required.

No output of this packet is allowed to become `final_toe_closure_complete`.
