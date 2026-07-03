# Claude/Fable Audit Prompt - GATE-03 External Reproduction Packet

You are reviewing a frozen MQGT-SCF GATE-03 external-reproduction packet.

Repository/package path:

`mqgt-gate03-external-reproduction`

Initial local freeze commit:

`7ffb5e8 Freeze GATE-03 external reproduction packet`

## Required Review Boundary

Do not treat this packet as a final Theory-of-Everything proof.

The packet can move only GATE-03, and only after independent external data collection plus raw-data/provenance attestation. Local synthetic tests and recovered self-archive data are not independent empirical confirmation.

## What To Inspect

1. Read `README.md`, `LAB_STATUS.md`, `PREREGISTRATION.md`, `DATA_SCHEMA.md`, and `INDEPENDENT_OPERATOR_CHECKLIST.md`.
2. Review `scripts/analyze_blocks.py` for statistical, schema, and gate-promotion errors.
3. Review `scripts/run_smoke_tests.py` and the reports in `results/`.
4. Confirm `PACKET_MANIFEST.json` is appropriate for a frozen handoff.
5. Identify any design weakness that could allow post-hoc promotion, block selection, direction switching, local/self data promotion, or final ToE overclaiming.

## Known Current Results

Recovered iCloud formal meditation subset:

- Formal runs: 3
- Control blocks: 30
- Intervention blocks: 30
- Difference I-C: +0.000692667
- Permutation p: 0.091291
- Decision: `not_promotable`

Synthetic smoke tests:

- synthetic null: `not_promotable`
- synthetic positive control: `candidate_support_requires_attestation`

The synthetic positive control only verifies analyzer sensitivity. It is not evidence for MQGT-SCF.

## Questions To Answer

1. Is the packet safe to give to an independent operator without creating ambiguity about final ToE closure?
2. Is the preregistration design specific enough to prevent post-hoc analytical drift?
3. Are the analyzer decisions correctly bounded to `not_promotable` and `candidate_support_requires_attestation`?
4. What minimal changes, if any, are required before external use?
5. Does any current artifact promote GATE-03 or final closure? If yes, cite exact file/line logic. If no, state the block clearly.

## Expected Output

Return:

- `PROMOTION_STATUS`: one of `no_gate03_promotion`, `gate03_candidate_only_after_external_attestation`, or `invalid_packet`.
- `FINAL_TOE_STATUS`: should remain `not_closed` unless you identify a valid independent final proof object.
- findings ordered by severity;
- required fixes before handoff;
- optional improvements after handoff;
- a short independent-operator readiness verdict.
