# Preregistration - GATE-03 QRNG External Reproduction v0.1

## Hypothesis

Primary null hypothesis: the intervention condition and control condition have equal binary outcome probability P(1).

Primary alternative: P(1) differs between intervention and control in a preregistered direction or by a two-sided block-level test, depending on the operator's chosen preregistration line below.

Operator must choose before collection:

- Directional: intervention P(1) > control P(1)
- Directional: intervention P(1) < control P(1)
- Two-sided: intervention P(1) != control P(1)

If no direction is selected before collection, the analyzer treats the result as two-sided.

## Primary Endpoint

Difference in block-level mean P(1):

`mean(P1_intervention_blocks) - mean(P1_control_blocks)`

## Formal Run Definition

A formal run must have:

- 20 blocks.
- 10 control blocks.
- 10 intervention blocks.
- At least 100,000 bits per block.
- A recorded randomization seed or independently documented block order.
- A stable intervention label.

## Minimum Dataset

The packet requires at least 3 formal runs before any support candidate can be considered.

## Statistical Test

Primary test: block-label permutation test using block P(1) values.

Default permutations: 10,000.

Primary alpha: 0.01.

Support candidate requires:

- at least 3 formal runs;
- all formal runs in the preregistered direction, or same nonzero direction for two-sided exploratory mode;
- pooled permutation p < 0.01;
- all raw block files hash-logged;
- independent operator attestation.

## Multiplicity

Only the primary endpoint above is promotable. Any secondary analysis is exploratory and cannot promote GATE-03.

## Prohibited After Collection

- changing alpha;
- changing block inclusion rules;
- selecting only favorable blocks;
- replacing the primary endpoint;
- treating local self-generated data as independent external reproduction;
- promoting final ToE closure from this result alone.

## Required Report Fields

- operator id or organization;
- device/source id hash;
- acquisition date/time range;
- block order;
- block sizes;
- raw file SHA-256;
- analyzer version/hash;
- output report SHA-256.
