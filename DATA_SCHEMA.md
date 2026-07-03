# Data Schema - GATE-03 Block JSON v0.1

Each run is one JSON file.

```json
{
  "run_id": "operator-run-001",
  "operator_id": "independent-lab-or-person",
  "device_id_hash": "sha256-or-other-stable-redacted-id",
  "intervention": "meditation",
  "randomization_seed": 42,
  "direction": "two-sided",
  "blocks": [
    {
      "block_index": 0,
      "condition": "control",
      "bit_count": 100000,
      "ones": 50012,
      "p_hat": 0.50012,
      "start_time": "2026-07-03T00:00:00Z",
      "end_time": "2026-07-03T00:01:00Z"
    }
  ]
}
```

## Required Top-Level Fields

- `run_id`
- `operator_id`
- `device_id_hash`
- `intervention`
- `blocks`

## Required Block Fields

- `block_index`
- `condition`: exactly `control` or `intervention`
- `bit_count`
- either `ones` or `p_hat`

If both `ones` and `p_hat` are supplied, the analyzer recomputes P(1) from `ones / bit_count` and records that fact.

## Formal Criteria

For promotion eligibility, each formal run must have exactly:

- 20 blocks;
- 10 control;
- 10 intervention;
- every `bit_count >= 100000`.

Smaller pilot runs may be analyzed but are never promotable.
