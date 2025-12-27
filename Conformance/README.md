---
title: CNAUS Conformance Pack
status: Informative
conformance_scope: Non-Core
authority: CNAUS Root Authority
---

# CNAUS Conformance Pack (Informative)

This folder provides test vectors and a machine-readable manifest to support implementers and reviewers.

This pack is **not** part of the CNAUS Core Standard conformance set. The normative requirements remain in the Core specifications referenced by the repository root `README.md`.

## Contents

- `manifest.json` — list of test vectors with expected outcomes
- `vectors/` — JSON inputs used by the test vectors

## How to use

Implementations SHOULD:
1. Load each vector input JSON.
2. Apply the corresponding validation rules described in the referenced Core specification(s).
3. Compare the observed result to the expected outcome in `manifest.json`.
