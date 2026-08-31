# Independent Operator Checklist

> **Historical v0.1 checklist — do not issue to a new operator.** A replacement
> checklist is blocked until Objects 1–5 are apparatus-sourced and a distinct
> v0.2 packet is frozen.

Before data collection:

- Confirm you are not the theory author and are operating independently.
- Record your operator id or organization.
- Record a redacted stable device/source id hash.
- Choose the direction line in `PREREGISTRATION.md`.
- Freeze the packet hashes.
- Generate or record the randomized block order before collection.

During data collection:

- Do not inspect interim results to alter the block plan.
- Do not skip failed-looking blocks unless there is a documented acquisition failure.
- Record start/end time for every block.
- Preserve raw source output where possible.

After data collection:

- Produce one block JSON file per formal run.
- Record SHA-256 hashes of raw files and block JSON files.
- Run `scripts/analyze_blocks.py` exactly once for the primary report.
- Return raw files, block JSON files, report JSON, report Markdown, and hashes.

Promotion rule:

- Even a positive report is only `candidate_support_requires_attestation`.
- It cannot close final ToE status.
