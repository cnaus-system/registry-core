---
title: CNAUS Release Policy
status: Informative
conformance_scope: Non-Core

---

# CNAUS Release Policy (Non-Core)

## 1. Normative Reference

The normative reference for CNAUS is a published immutable release tag `vX.Y.Z`.

The most recent release marked as “Latest” on the official CNAUS repository is the
current recommended normative reference for new adopters. Implementations MAY
choose to pin an earlier tag for stability.

## 2. Immutability

Published release tags are immutable. The CNAUS Root Authority MUST NOT modify
the contents of a released tag retroactively. Corrections are made only through
new releases.

## 3. Semantic Versioning

CNAUS follows Semantic Versioning (`MAJOR.MINOR.PATCH`):

- PATCH (`X.Y.Z+1`): clarifications, corrections, and non-breaking updates.
- MINOR (`X.Y+1.0`): backward-compatible additions.
- MAJOR (`X+1.0.0`): incompatible changes.

## 4. Change Control and Errata

Changes to the CNAUS Standard follow the governance process and the errata process.
Errata do not retroactively change released tags; confirmed errata are resolved via
subsequent releases.

## 5. How to Cite CNAUS

When citing CNAUS, reference:
- the repository,
- the tag `vX.Y.Z`,
- and (if applicable) the specific document path within that tag.

Example:
“CNAUS Standard, v1.0.13, RFCs/RFC0003_ProofLayer.md”.

