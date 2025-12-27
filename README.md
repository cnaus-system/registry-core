---
title: CNAUS Registry Core Standard - Repository Index
document_id: CNAUS-REGISTRY-CORE-REPO
status: Informative
current_series: v1.0.x
authority: CNAUS Root Authority
---
# CNAUS Registry Core Standard (Core Standard)

This repository publishes the canonical CNAUS Core Standard specifications, schemas, and the canonical public event feed.

This `README.md` is **informative**. Normative requirements are defined only in the documents listed in Section 2.

## 1. Scope

CNAUS Core Standard defines a minimal, globally verifiable registry and proof infrastructure providing deterministic:

- origin (authority-issued),
- integrity (canonical hashing),
- version binding (SemVer),
- lifecycle and revocation semantics,
- feed-based publication and change signaling.

## 2. Normative Conformance Set (Core Standard v1.0.x)

A system MAY claim conformance to **CNAUS Core Standard v1.0.x** only by implementing and enforcing the following normative artifacts:

- `RFCs/RFC0001_RegistryFramework.md`
- `RFCs/RFC0002_APISpecification.md`
- `RFCs/RFC0003_ProofLayer.md`
- `Feed_Specification.md`
- `Revocation_Specification.md`
- `Root_Authority_Specification.md`
- `Governance/GOVERNANCE.md`
- `VERSIONING.md`
- `schemas/` (normative JSON schemas)
- `feed.json` (canonical event feed snapshot, hash-chained per Feed Specification)

## 3. Non-Core Documents (Not part of Core conformance)

The following documents are **not** part of Core Standard conformance claims unless explicitly added by a future version and announced via standard events:

- `CNAUS_Protection_Charter.md`
- `CNAUS_Risk_Matrix.md`
- `CNAUS_Threat_Model.md`
- `CNAUS_Compliance_Guide.md`
- `PoC_Overview.md`
- `Pilot_Onboarding.md`
- `Pilot_License.md`
- `Pilot_Assessment.md`

These may be published as separate packages (e.g., “Root Protection Package”) but remain outside Core Standard v1.0.x.

## 4. Releases and Immutability

- Releases are identified by Git tags and GitHub Releases (e.g., `v1.0.0`, `v1.0.1`, `v1.0.2`).
- The canonical public event feed (`feed.json`) signals standard publication events and version updates.
- Past releases are immutable. Any change is published as a new version following `VERSIONING.md` and `Governance/GOVERNANCE.md`.

## 5. Root Authority

The CNAUS Root Authority is the sole authoritative issuer/publisher for:

- canonical registry issuance (conceptually),
- canonical proof issuance,
- canonical feed publication,
- standard release publication and version update signaling.

See `Root_Authority_Specification.md`.

## 6. Implementer Entry Points

- Conformance requirements: Section 2 above
- API surface: `RFCs/RFC0002_APISpecification.md`
- Feed processing: `Feed_Specification.md`
- Revocation processing: `Revocation_Specification.md`

