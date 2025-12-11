---
title: CNAUS Registry Core Standard
version: B (Public Release)
status: Normative
layer: Root Standard – Layer 1
document_id: CNAUS-ROOT-STD-B
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
repository: https://github.com/cnaus-system/registry-core
hash: assigned in Phase C
---
## 1. Scope

This document specifies the canonical CNAUS Registry Core Standard.  
It defines the normative mechanisms for:

- asset registration  
- integrity proof  
- verification  
- versioning  
- governance  
- revocation  

The CNAUS Registry functions as a root standard similar to recognized international frameworks  
(IETF RFC series, W3C Technical Reports, ISO/IEC conformance documents).

All CNAUS-compliant systems **MUST** implement the semantics and invariants defined in this repository.

Non-normative extensions, UI layers, applications, or product features are out of scope and  
**MUST NOT** redefine, weaken, or override any normative requirements of this standard.

---

## 2. Standard Components

The CNAUS Registry Core consists of the following normative components:

### 2.1 Registry Framework  
Defines the data model, lifecycle, invariants, and registration semantics.  
→ `RFCs/RFC0001_RegistryFramework.md`

### 2.2 API Specification  
Defines the minimal interface for register, verify, revoke, and list.  
→ `RFCs/RFC0002_APISpecification.md`

### 2.3 Proof Layer  
Defines hash-linked proof structures, anchors, verification invariants, and deterministic proof logic.  
→ `RFCs/RFC0003_ProofLayer.md`

### 2.4 Governance  
Defines policy framework for change control, versioning, and revocation processes.  
→ `Governance/GOVERNANCE.md`

### 2.5 Feed Mechanism  
Defines the canonical public event feed (root updates, proofs, revocations).  
→ `feed.json`

### 2.6 Versioning Rules  
Defines release policy, semantic versioning, compatibility rules, and escalation logic.  
→ `VERSIONING.md`

---

## 3. Directory Structure  
(Informative)

```

/ (root)  
├── README.md  
├── LICENSE.md  
├── VERSIONING.md  
├── feed.json  
│  
├── RFCs/  
│ ├── RFC0001_RegistryFramework.md  
│ ├── RFC0002_APISpecification.md  
│ └── RFC0003_ProofLayer.md  
│  
├── Governance/  
│ └── GOVERNANCE.md  
│  
├── Proofs/  
│ ├── anchors/  
│ └── chain/  
│  
└── Examples/  
├── example_register.json  
├── example_verify.json  
└── example_proof.json

```

This directory structure is minimal, self-contained, and aligned with established standardization practice.

---

## 4. Normative Requirements (MUST / SHOULD / MAY)

### 4.1 Registry Invariants  
- Assets **MUST** contain an identifier, version, hash, timestamp, and signature.  
- Registration records **MUST** be immutable once anchored.  
- Registry operations **MUST** be deterministic and side-effect free.  

### 4.2 Proof Layer  
- Proof records **MUST** be hash-linked.  
- Verification **MUST** yield a deterministic boolean result.  
- Anchors **MUST NOT** contain personal data (**Zero-PII constraint**).  
- Proof computation **MUST** follow RFC0003 invariants.  

### 4.3 Hash Chain Requirements  
- All root events **MUST** be included in `feed.json`.  
- Events **MUST** follow canonical ordering.  
- Each entry **MUST** include a `prev_hash` linking to its predecessor (except the genesis entry).  

### 4.4 Revocation  
- A registered asset **MAY** be revoked through a valid revocation record.  
- Revocation events **MUST** be published via `feed.json`.  
- Revocation semantics **MUST** follow RFC0001 and RFC0002.  

### 4.5 Governance  
- All normative changes **MUST** follow the procedures defined in `GOVERNANCE.md`.  
- Version increments **MUST** comply with `VERSIONING.md`.  

---

## 5. Interoperability and Compliance

The CNAUS Registry Core Standard is designed to be:

- technology-agnostic  
- implementation-neutral  
- forward-compatible  
- regulator-aligned (EU AI Act, OECD AI Principles, NIST AI RMF)

Any system claiming CNAUS compatibility **MUST** implement all normative requirements and invariants defined in this repository and corresponding RFCs.

---

## 6. Non-Normative Examples  
(Informative)

Canonical JSON examples for conformant operations are provided in `/Examples`.  
These examples clarify minimal expected behavior but do not introduce any new normative requirements.

---

## 7. Public Change Log

Normative changes and root events are tracked via:

- `feed.json` – machine-readable event log  
- `VERSIONING.md` – human-readable release notes  

---

## 8. Status of This Document

This document is an authoritative **Version-B** release of the CNAUS Registry Core Standard.  
Future revisions will follow the governance and versioning rules defined in this repository.
