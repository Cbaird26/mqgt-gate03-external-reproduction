# Historical v0.1 Results

These reports belong to the frozen v0.1 endpoint. They are retained for
provenance only. Do not re-score their bits under the blocked v0.2 apparatus
stub, and do not treat the recovered meditation-labeled report or synthetic
positive control as empirical support.

## Cross-check against the March 2026 report (resolved 14 October 2026)

`recovered_icloud_formal_meditation_report.md` re-scores the three formal runs of
14 March 2026 that were first reported in
[toe-2026-updates/docs/QRNG_MEDITATION_INTERVENTION_REPORT_MARCH_2026.md](https://github.com/Cbaird26/toe-2026-updates/blob/main/docs/QRNG_MEDITATION_INTERVENTION_REPORT_MARCH_2026.md).
Runs 1 and 2 agreed; run 3 did not (March report: I − C = −0.00064, p = 0.28;
here: +0.000447, p = 0.522), nor did the pooled values (March: +0.00033,
p = 0.41; here: +0.000693, p = 0.091).

**Resolution.** The raw run-3 block file (`data/formal_runs_2026-03-14/`, SHA-256
`2e985fee…8729`, the hash pinned above) contains its own same-night analysis:
control 0.499293, intervention 0.499740, difference +0.000447, p 0.522 — the
values in this report. Recomputing from its 20 blocks gives the same. No artifact
from the March sessions contains the −0.00064 row, which was a transcription
error in the March report; that report now carries an erratum with the corrected
table. Re-running `scripts/analyze_blocks.py` on the three files on 14 October
2026 reproduces this report exactly. Both scorings remain null; this report's
numbers are the values of record.
