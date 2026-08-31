# MQGT GATE-03 Lab Status

Status date: 2026-08-31

## Current State

This repo preserves the historical v0.1 external-reproduction packet at
`e72625cd`. It is not the active design and is not operator-ready.

The local archive contains recovered QRNG block evidence, but it is not independent external confirmation. The recovered formal meditation subset remains null under this packet:

- Formal runs: 3
- Control blocks: 30
- Intervention blocks: 30
- Difference I-C: +0.000692667
- Permutation p: 0.091291
- Decision: not_promotable

## Historical v0.1 Result

The old bits remain bound to the frozen v0.1 endpoint. They must not be
reinterpreted with a prospective v0.2 endpoint.

The analyzer can return:

- `not_promotable`
- `candidate_support_requires_attestation`

It cannot return final Theory-of-Everything closure.

## v0.2 Block

No v0.2 packet may be drafted or released until Objects 1–5 are
apparatus-sourced. Until then, only the non-operational boundary language in
`V0_2_APPARATUS_STUB.md` is permitted: live-time, $\hat y$, an
apparatus-defined $P(1)$ null, and no meditation source.

Object 5 is bound-only for this box. The apparatus cannot reach
$7\times10^{-14}$. No detection-power or sample-size claim may be made against
that scale or against a $0.006$ shift in $P(1)$.

## What Is Still Open

- Apparatus sourcing for Objects 1–5.
- A new, separately frozen v0.2 protocol after those sources exist.
- Raw data hash and provenance review.
- UV completion proof.
- Uniqueness proof.
- Bridge-map validation for interpretive claims.
- Final closure proof object.

## Local Controls

Run:

```bash
make smoke
make verify
```

The smoke test must show a null synthetic dataset as `not_promotable` and a deliberately positive synthetic dataset as `candidate_support_requires_attestation`. This verifies only the historical v0.1 code path.
