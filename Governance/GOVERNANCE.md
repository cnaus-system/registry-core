---
title: CNAUS Registry Core Standard
document_id: Governance Framework
version: 1.0.0
status: Normative
document_class: Root Standard - Layer 1
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
dependencies:
  - RFC0001
  - RFC0002
  - RFC0003
  - VERSIONING.md
  - feed.json
references:
  - RFC0001
  - RFC0002
  - RFC0003
  - VERSIONING.md
  - LICENSE.md
---
## 1. Purpose

This document defines the **normative governance rules** for maintaining and evolving the  
**CNAUS Registry Core Standard**.

Governance decisions determine:

- normative content and revisions
- version boundaries and SemVer classification
- conformance conditions
- revocation authorization policy
- lifecycle invariants of the standard

This document is **normative** and binding for all implementers.

---

## 2. Governance Model (Normative)

### 2.1 Roles

- **Council**: decision and approval body for standard changes.
- **Root Authority**: execution and publication authority for canonical artifacts.

### 2.2 Decision vs Execution

- The Council **authorizes** changes and revocation actions.
- The Root Authority **executes and publishes** approved changes as canonical documents and feed events.

---

## 3. Change Control (Normative)

### 3.1 Change Proposal

Changes MUST be proposed via a formal change request including:

- change summary
- impacted documents
- SemVer classification (MAJOR/MINOR/PATCH)
- conformance impact statement

### 3.2 Approval

No normative change MAY be published without Council approval.

### 3.3 Publication

Approved changes MUST be published by the Root Authority as:

- updated canonical documents
- a standard event in `feed.json`
- a versioned release tag

---

## 4. Layer-1 Finality (Normative)

As of 2025-12-12, **CNAUS Core Standard v1.0.0** is declared **FINAL**.

### Core Standard (v1.0.0) — Normative Conformance Set

Core Standard conformance claims apply ONLY to the following normative artifacts:

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- RFC0003 — Proof Layer
- Feed Specification
- Revocation Specification
- Root Authority Specification
- Governance Framework (`Governance/GOVERNANCE.md`)
- Versioning Specification (`VERSIONING.md`)
- Canonical feed snapshot (`feed.json`)
- Normative schemas (`schemas/`)

### Root Protection Package (Non-Core)

The following documents MAY be published as a separate, normative **Root Protection Package**.
They are **NOT** part of Core Standard v1.0.0 conformance claims unless explicitly stated
in a future release and announced via standard events:

- Protection Charter
- Risk Matrix
- Threat Model
- Compliance Guide

No normative changes to **Core Standard v1.0.0** components are permitted except through:

- Council approval
- SemVer rules in VERSIONING.md
- publication by Root Authority
- feed-announced standard events

No release is valid without feed anchoring.

---

## 5. Revocation Policy (Normative)

The Council MAY authorize revocation actions when required to protect standard integrity. The CNAUS Root Authority MUST execute and publish revocation events in the canonical feed.

### Valid Reasons for Revocation:

- violation of registry invariants  
- invalid or compromised proofs  
- regulatory or legal requirement  
- root-authority action  

Revocation MUST follow the Revocation Specification and schema.

---

## 6. Conformance Claims (Normative)

A system may claim conformance to:

- **CNAUS Core Standard v1.0.0** (as defined in Section 4)
- Optional packages (e.g., Root Protection Package) only if explicitly stated and versioned separately

Conformance MUST be stated precisely with version.

---

## 7. References

- RFC0001
- RFC0002
- RFC0003
- Feed Specification
- Revocation Specification
- Root Authority Specification
- VERSIONING.md
- LICENSE.md
