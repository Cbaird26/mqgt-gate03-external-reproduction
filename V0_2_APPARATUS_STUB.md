# GATE-03 v0.2 Apparatus Boundary Stub

> **Not a packet. Not a preregistration. Not operator-ready.** No v0.2 release
> may be created until Objects 1–5 are each backed by an apparatus source such
> as a manufacturer manual, acquisition specification, calibration record, or
> directly recorded apparatus metadata. The object definitions and evidence
> belong in the apparatus atlas; this repository does not invent them.

## Permitted Prospective Language

Before apparatus sourcing is complete, a future design may be described only
at this level:

- exposure is measured as apparatus live-time;
- the observed apparatus statistic is denoted $\hat y$;
- $P(1)$ is a null control and must remain consistent with $1/2$; it is not the primary hypothesis and not a v0.2 endpoint;
- no meditation source or intervention label is part of the prospective design.

This vocabulary does not define an endpoint, estimator, inclusion rule,
sampling plan, threshold, or promotion rule. Those require apparatus sources
and a separately reviewed freeze.

## Old-Bit Firewall

The v0.1 endpoint is immutable for v0.1 data. Old recovered, synthetic, pilot,
or formal bits must not be reanalyzed under $\hat y$, live-time, or a new
$P(1)$ null. A future v0.2 run starts with newly collected apparatus data after
the v0.2 freeze.

## Object 5 Honesty Boundary

Object 5 is **bound-only** for this box. The apparatus cannot reach
$7\times10^{-14}$. That quantity may be carried only as an external bound, not
as a detection target for this apparatus.

Do not compute or advertise detection power, required sample size, minimum
detectable effect, or a positive-detection design against either:

- $7\times10^{-14}$; or
- a $0.006$ shift in $P(1)$.

Any future quantitative sensitivity statement must be derived from sourced
apparatus characteristics and must be presented as a bound unless the sourced
apparatus capability independently supports a detection claim.

## Object 1 Honesty Boundary

No lab source $S$ is named (density, geometry, live-time, and boundary conditions unnamed). The working formula $J=\kappa_E S^2$ is therefore not a meter map. Do not invent $S$, a device, a density, a geometry, or a live-time to close that gap. Until Objects 1–5 are apparatus-sourced, v0.2 remains blocked and bound-only.
