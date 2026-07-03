# MQGT GATE-03 Lab Status

Status date: 2026-07-03

## Current State

This repo is a frozen external-reproduction packet for MQGT-SCF GATE-03.

The local archive contains recovered QRNG block evidence, but it is not independent external confirmation. The recovered formal meditation subset remains null under this packet:

- Formal runs: 3
- Control blocks: 30
- Intervention blocks: 30
- Difference I-C: +0.000692667
- Permutation p: 0.091291
- Decision: not_promotable

## What Can Move

This packet can move only GATE-03, and only after an independent operator collects data using the frozen preregistered design and returns raw block files plus attestation.

The analyzer can return:

- `not_promotable`
- `candidate_support_requires_attestation`

It cannot return final Theory-of-Everything closure.

## What Is Still Open

- Independent external QRNG/count-data reproduction.
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

The smoke test must show a null synthetic dataset as `not_promotable` and a deliberately positive synthetic dataset as `candidate_support_requires_attestation`.
