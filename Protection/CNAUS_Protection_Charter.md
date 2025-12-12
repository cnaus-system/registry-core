---
title: CNAUS Protection Charter
document_id: PROTECTION-CHARTER
version: 1.0.0
status: Normative Charter
layer: Root Protection Layer – Core Standard
type: Normative Charter
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
dependencies:
  - RFC0001
  - RFC0002
  - RFC0003
  - GOVERNANCE.md
  - VERSIONING.md
  - Feed_Specification.md
  - Revocation_Specification.md
references:
  - RFC0001-0003
  - VERSIONING.md
  - GOVERNANCE.md
---
# CNAUS Protection Charter  
## 1. Purpose

The CNAUS Protection Charter defines the **normative protection guarantees**,  
**security invariants**, and **operational restrictions** required to protect the  
**CNAUS Registry Core Standard** from misuse, corruption, unauthorized  
modification, and non-compliant integrations.

This Charter ensures that:

- the CNAUS Root Authority retains exclusive control over the standard,  
- all implementations remain verifiable, reproducible, and immutable,  
- no third party can weaken, bypass, fork, or distort the standard,  
- regulatory-grade integrity and global interoperability are preserved.

This document is **normative** and binding for all systems claiming CNAUS compliance.

---

## 2. Protection Principles (Normative)

All CNAUS components MUST adhere to the following principles:

### 2.1 Integrity Supremacy  
No operation may compromise registry integrity, proof binding, lifecycle  
semantics, or feed chronology.

### 2.2 Root Authority Exclusivity  
Only the CNAUS Root Authority may:

- create, update, or revoke registry entries,  
- issue normative versions,  
- modify the feed,  
- authorize extensions to the standard.

No delegation is permitted unless explicitly defined in GOVERNANCE.md.

### 2.3 Immutability  
Historical versions, proofs, events, and revocations MUST remain permanently  
readable and verifiable.

### 2.4 Zero-Bypass Constraint  
Implementations MUST NOT bypass standard invariants via proprietary logic,  
alternative hashing, metadata injection, or non-canonical storage.

### 2.5 Zero-PII Protection  
Registry entries, proofs, feed events, and metadata MUST NOT contain personal  
data.  
This rule may not be waived or weakened.

---

## 3. Security Invariants (Normative)

The following invariants MUST always hold true:

1. **Append-Only Feed** — No event may be removed or rewritten.  
2. **Monotonic Timestamps** — All lifecycle events for a given `registry_id` MUST  
   increase monotonically.  
3. **Canonical Hashing** — All artifacts MUST follow RFC0003 canonicalization.  
4. **Non-Repudiation** — Every root action MUST be traceable to a feed event.  
5. **Revocation Finality** — Revocation is terminal; no reinstatement allowed.  
6. **Version Boundary Integrity** — Version regressions MUST be rejected.  
7. **Single-Source-Truth** — Public Repository + feed.json = authoritative source.

If any invariant is violated, the system MUST treat the entry as invalid.

---

## 4. Threat Protection Model (High-Level Normative Requirements)

The CNAUS Root Authority MUST ensure protection against:

### 4.1 Structural Threats  
- registry forking  
- alternative, conflicting versions  
- non-canonical mirrors  
- unauthorized registry mutation

### 4.2 Cryptographic & Integrity Threats  
- hash collisions or malformed canonicalization inputs  
- unauthorized modification of proof metadata  
- feed tampering  
- unanchored proof issuance

### 4.3 Operational Threats  
- misuse by non-compliant integrators  
- silent standard deviation  
- injection of metadata violating Zero-PII  
- revocation circumvention attempts

### 4.4 Governance Threats  
- unauthorized governance amendments  
- unapproved normative rule changes  
- attempts to bypass Root Authority exclusivity

---

## 5. Compliance Obligations (Normative)

A system is **CNAUS-Compliant** only if it:

1. Implements all rules in RFC0001–RFC0003.  
2. Enforces lifecycle immutability and revocation finality.  
3. Uses the canonical append-only feed as its verification backbone.  
4. Rejects any non-canonical registry or proof data.  
5. Ensures strict Zero-PII compliance.  
6. Maintains full version compatibility and rejects outdated version logic.  
7. Performs validator checks exactly as defined in RFC0003.

Any deviation MUST be treated as non-compliance.

---

## 6. Enforcement Rules

### 6.1 Non-Compliant Systems  
The Root Authority MAY issue:

- formal revocation events,  
- public non-compliance notices published via feed.json,  
- feed-anchored invalidation entries.

### 6.2 Unauthorized Registry Mutations  
Any system attempting mutation, forgery, backdating, or timeline rewrites:

- MUST be rejected,  
- MUST be marked via revocation or invalidation feed entries,  
- MUST NOT continue using CNAUS identifiers.

### 6.3 Forking Prohibition  
No system MAY present an altered, extended, or reduced version of:

- registry semantics,  
- proof semantics,  
- canonicalization rules,  
- feed requirements  
as a replacement CNAUS standard.

Forks MUST be treated as non-compliant.

---

## 7. Protection of the Root Authority

The Root Authority infrastructure MUST:

- operate on a secure, isolated, controlled environment,  
- never expose private cryptographic material,  
- log all proof generation and lifecycle decisions,  
- follow strict operational governance boundaries,  
- maintain secure backups of all normative documents and feed history.

Mirrors MAY exist but MUST NOT publish conflicting entries.

---

## 8. Publication & Versioning (Normative)

### 8.1 Publication Rules  
This Charter becomes normative only when:

- published in the main branch of the public CNAUS repository,  
- anchored in `feed.json`,  
- included in the corresponding version tag (v1.1.0 or later).

### 8.2 Versioning  
Any amendment MUST follow:

- semantic versioning (VERSIONING.md),  
- governance approval (GOVERNANCE.md),  
- feed anchoring requirements.

---

## 9. Legal & Regulatory Alignment (Normative)

This Charter aligns with:

- regulator-grade auditability (EU AI Act, OECD AI Principles, ISO/IEC 42001),  
- global software integrity requirements,  
- cryptographic non-repudiation norms.

CNAUS MAY be adopted by regulators and enterprises without modification.

---

## 10. Amendments (Normative)

This Charter may be amended only if:

1. approved by the CNAUS Governance Council,  
2. version increment assigned (per VERSIONING.md),  
3. feed event published with timestamp & prev_hash,  
4. updated file included in the authoritative SSOT.

Unauthoritative modifications MUST be rejected.

---

## 11. Status of This Document

This Protection Charter is:

- final,  
- normative,  
- immutable in its applied version,  
- globally binding for all CNAUS-compliant implementations.

---
