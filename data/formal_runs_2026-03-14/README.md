# Formal runs of 14 March 2026 — raw block files

The three block-summary files behind `results/recovered_icloud_formal_meditation_report.md`.
They were recovered from the archived `TOE_Corpus_2026/artifacts/` folder on 14 October 2026
and are byte-identical to the inputs pinned in that report:

| File | Blocks (C / I) | SHA-256 |
| --- | --- | --- |
| `qrng_experiment_20260314_001431_e259c51c_blocks.json` | 20 (10 / 10) | `59011fb33808c93d622ffdb041f73e87caa64cd18260c65cfd092f965cd35363` |
| `qrng_experiment_20260314_004101_c72a681e_blocks.json` | 20 (10 / 10) | `abc890d7b6a8ba9e33ae085e62dac64736f69d76d420a6f335839aaf261aacb6` |
| `qrng_experiment_20260314_010459_ccb8f429_blocks.json` | 20 (10 / 10) | `2e985fee7ae2a605cabfc57a9ae2c9b6034537c0df2267bacc9c01cdfb1a8729` |

Each block records its condition, start/end time, bit count, ones/zeros, `p_hat`, entropy and a
runs-test z (see `DATA_SCHEMA.md`). Runs 2 and 3 also carry the `block_comparison` written by
`anu_qrng_experiment.py --analyze-blocks` on the night of collection. The raw 100,000-bit
streams per block (`*.csv`, ~172 MB per run) are not included.

Reproduce the report:

```sh
python3 scripts/analyze_blocks.py data/formal_runs_2026-03-14/*_blocks.json \
  --out tmp/formal_rerun.json --md-out tmp/formal_rerun.md
```

Re-run on 14 October 2026: pooled I − C = +0.000693, permutation p = 0.0913, decision
`not_promotable` — identical to the July 2026 report.
