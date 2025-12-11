# CNAUS Registry Core Standard — Governance Framework  
version: 1.0.0  
status: Normative  
document_id: GOVERNANCE  
document_class: Root Standard – Layer 1  
issued: 2025-12-11  
updated: 2025-12-11  
authority: CNAUS Root Authority  
dependencies: RFC0001, RFC0002, RFC0003, VERSIONING.md, feed.json  
references: RFC0001, RFC0002, RFC0003, VERSIONING.md, LICENSE.md  

---

## 1. Purpose

This document defines the **normative governance rules** for maintaining and evolving the  
**CNAUS Registry Core Standard**.  
It ensures institutional stability comparable to IETF, W3C, and ISO governance models,  
while enforcing strict integrity via the CNAUS Proof and Versioning systems.

Governance decisions directly determine:

- normative RFC content  
- version boundaries  
- conformance rules  
- revocation authority  
- lifecycle invariants of the standard  

This document is **normative** and binding for all implementers.

---

## 2. Governance Principles (Normative)

All governance processes **MUST** adhere to:

### Neutrality  
CNAUS does not promote specific vendors, technologies, or commercial interests.

### Integrity  
All changes MUST be validated through canonical proof and versioning mechanisms.

### Transparency  
Updates MUST be published in the canonical `feed.json`.

### Minimalism  
Only essential registry, proof, and lifecycle invariants are standardized.

### Backward Compatibility  
Changes MUST preserve operability of existing implementations unless a  
**MAJOR** update authorizes a breaking change.

### Single Source of Truth (SSOT)  
The public CNAUS repository + feed.json form the authoritative SSOT.  
Mirrors MUST reflect the same feed chain.

---

## 3. Governance Council (Normative)

A **CNAUS Governance Council** oversees all normative decisions affecting:

- creation, modification, or removal of RFCs  
- registry invariants defined in RFC0001  
- proof semantics defined in RFC0003  
- API invariants defined in RFC0002  
- versioning boundaries and release classification  
- revocation policies  
- compliance and conformance criteria  

### Council Responsibilities

1. Maintain normative consistency across all documents.  
2. Ensure adherence to governance principles.  
3. Approve or reject normative change proposals.  
4. Publish authoritative updates through `feed.json`.  
5. Enforce CNAUS License and conformance rules.  
6. Protect zero-PII constraints throughout the entire standard.

No normative modification is valid without Council approval.

---

## 4. Change Proposal Workflow (Normative)

All normative changes **MUST** follow the process below:

### 1. Proposal Submission  
A formal change request referencing affected sections, rationale, and impact.

### 2. Compatibility Review  
Assessment of:

- backward/forward compatibility  
- registry invariants  
- proof stability  
- versioning impact  
- revocation boundaries  

### 3. Governance Review  
Council evaluates proposal according to CNAUS governance principles.

### 4. Approval + Version Assignment  
Upon approval, a version increment is assigned following `VERSIONING.md`.

### 5. Publication  
Changes **MUST** be published in:

- updated RFCs  
- a repository version tag  
- `feed.json` with timestamp + prev_hash linkage  
- release notes in SSOT repository  

No release is valid without feed anchoring.

---

## 5. Revocation Policy (Normative)

The Council MAY issue revocation entries when required to protect standard integrity.

### Valid Reasons for Revocation:

- violation of registry invariants  
- invalid or compromised proofs  
- malicious or non-compliant implementations  
- systemic errors affecting integrity or security  

### Revocation Requirements

Revocation entries MUST:

1. be recorded in `feed.json` with timestamp and `revocation_reason`  
2. include affected `registry_id` and final `proof_hash`  
3. be immutable once published  
4. establish a terminal lifecycle boundary for the affected entry  

No updates MAY occur to revoked entries.

---

## 6. Conformance Requirements (Normative)

Systems claiming CNAUS compliance **MUST** implement:

- all normative rules in RFC0001–RFC0003  
- proof and validation semantics defined in RFC0003  
- versioning and lifecycle rules in VERSIONING.md  
- revocation semantics  
- append-only feed consistency  
- Zero-PII constraints for proofs, metadata, and feed events  

Implementations MAY add optional, non-normative layers  
(proprietary APIs, UI, additional metadata)  
provided they do **NOT** modify or bypass core semantics.

Only systems conforming to all normative rules MAY use the term **“CNAUS-compliant.”**

---

## 7. Delegation & Authority Boundaries

- Only the **CNAUS Root Authority** MAY issue normative releases.  
- Mirrors MUST NOT publish independent versions.  
- Delegated authorities MAY exist for operational tasks but  
  MUST NOT alter normative content.

Any unanchored release is invalid.

---

## 8. Governance Amendments (Normative)

This document may be amended **only** via:

1. Council approval  
2. Assigned version increment per semantic rules  
3. Feed entry documenting the amendment  
4. Updated reference in `VERSIONING.md`  

Amendments without feed anchoring are invalid.

---

## 9. References  
(Informative unless defined as normative in other RFCs)

- RFC0001 — Registry Framework  
- RFC0002 — API Specification  
- RFC0003 — Proof Layer  
- VERSIONING.md  
- LICENSE.md  

