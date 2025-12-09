# CNAUS Registry Core Standard  
Version B (Public Release)

## 1. Scope
This repository defines the canonical CNAUS Registry Core Standard.  
It specifies the normative mechanisms for registration, integrity proof,
verification, versioning, governance, and revocation of digital assets.

The CNAUS Registry functions as a root-standard similar to recognized
international frameworks (IETF RFC series, W3C Technical Reports, ISO/IEC
conformance documents).  
All CNAUS-compliant systems MUST implement the rules defined in this
repository.

Non-normative extensions, UI layers, applications, or product features are
explicitly out of scope.

---

## 2. Standard Components
The CNAUS Registry Core consists of the following normative components:

1. **Registry Framework**  
   Data model, lifecycle, invariants, and registration semantics  
   → Defined in `RFCs/RFC0001_RegistryFramework.md`

2. **API Specification**  
   Minimal interface definitions for register, verify, revoke, and list  
   → Defined in `RFCs/RFC0002_APISpecification.md`

3. **Proof Layer**  
   Hash-linked log structure, proof records, anchors, and verification logic  
   → Defined in `RFCs/RFC0003_ProofLayer.md`

4. **Governance**  
   Policy framework for change control, versioning, and revocation  
   → Defined in `Governance/GOVERNANCE.md`

5. **Feed Mechanism**  
   Public machine-readable event feed (root updates, proofs, revocations)  
   → Implemented in `feed.json`

6. **Versioning Rules**  
   Release policy, semantic versioning, and backward/forward compatibility  
   → Defined in `VERSIONING.md`

---

## 3. Directory Structure

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

This structure is minimal, self-contained, and compliant with established
standardization practices.

---

## 4. Normative Requirements (MUST / SHOULD / MAY)

### Registry
- Assets **MUST** contain an identifier, version, hash, timestamp, and signature.
- Registration **MUST** be immutable once anchored.

### Proof Layer
- Proof records **MUST** be hash-linked.  
- Verification **MUST** succeed deterministically.  
- Anchors **MUST NOT** contain personal data (Zero-PII constraint).

### Revocation
- A registered asset **MAY** be revoked through an issued revocation record.  
- Revocation **MUST** be published via `feed.json`.

### Governance
- All changes to the standard **MUST** follow the procedures in GOVERNANCE.md.

---

## 5. Interoperability and Compliance
The CNAUS Registry Core Standard is designed to be:

- technology-agnostic  
- implementation-neutral  
- forward-compatible  
- regulator-aligned (EU AI Act, OECD Principles, NIST AI RMF)

Any system claiming CNAUS compatibility **MUST** implement the semantics and
invariants defined in this repository.

---

## 6. Non-Normative Examples
Canonical JSON examples for conformant operations are provided in `/Examples`.
These examples clarify minimal expected behavior but do not define additional
requirements beyond the normative RFCs.

---

## 7. Public Change Log
All normative changes, amendments, and errata are tracked in:

- `feed.json` (machine-readable root events)  
- `VERSIONING.md` (human-readable release notes)

---

## 8. Status of This Document
This is a public, authoritative Version-B release of the CNAUS Registry Core
Standard. Future revisions will follow the governance and versioning rules
defined in this repository.