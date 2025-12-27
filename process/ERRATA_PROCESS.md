---
title: CNAUS Errata Process
status: Informative
conformance_scope: Non-Core
authority: CNAUS Root Authority
---

# CNAUS Errata Process (Non-Core)

## Scope

This process applies to published CNAUS Core Standard tags and associated GitHub releases.

## Principles

- Published tags are immutable.
- Corrections are delivered via patch releases.
- The feed announces standard changes via `standard.version_update` events.

## Workflow

1. Report received (issue).
2. Triage:
   - editorial (no normative effect) OR
   - normative (affects conformance)
3. Decision:
   - reject (not an error) OR
   - accept (confirmed erratum)
4. Patch preparation:
   - implement fix on a dedicated branch
   - update `ERRATA.md` with:
     - erratum ID
     - affected versions
     - document + section
     - summary and resolution
5. Validation:
   - `make validate` MUST pass
6. Release:
   - patch tag `vX.Y.(Z+1)`
   - GitHub release created
   - feed receives a `standard.version_update` event (if applicable)

## Erratum Entry Format

- ID: E-YYYY-NNN
- Affected: vX.Y.Z
- Document: <path>
- Section: <identifier>
- Summary: <one line>
- Resolution: <one line>
