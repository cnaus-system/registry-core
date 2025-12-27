---
title: CNAUS Threat Model
status: Informative
conformance_scope: Non-Core
authority: CNAUS Root Authority
---
# CNAUS Threat Model  

## 1. Purpose

This document defines the **normative threat landscape** relevant to CNAUS  
Layer-1 Registry, Proof Layer, Feed, Versioning, and Root Authority operations.

It ensures:

- protection against structural, cryptographic, operational, and governance threats  
- integrity of registry entries  
- stability of canonical proofs  
- enforceability of lifecycle guarantees  

This document is normative.

---

## 2. Threat Classification

Threats are grouped into four classes:

- **T1 — Structural Threats**  
- **T2 — Integrity & Cryptographic Threats**  
- **T3 — Operational Threats**  
- **T4 — Governance Threats**

---

## 3. Threat Catalog (Normative)

### **T1 — Structural Threats**
| ID | Threat | Description | Required Protection |
|----|---------|-------------|----------------------|
| T1.1 | Registry Fork | Unofficial CNAUS clones with altered semantics | Enforce Root Authority exclusivity |
| T1.2 | Non-canonical Mirrors | Conflicting feeds or alternative registries | Canonical-feed enforcement |
| T1.3 | Version Drift | Silent divergence from official RFCs | SSOT enforcement |

---

### **T2 — Integrity & Cryptographic Threats**
| ID | Threat | Description | Required Protection |
|----|---------|-------------|----------------------|
| T2.1 | Hash Manipulation | Incorrect hashing or canonicalization | RFC0003 enforcement |
| T2.2 | Feed Tampering | Modification of historical events | Append-only feed |
| T2.3 | Proof Forgery | Unauthorized proof generation | Root-only proof issuance |

---

### **T3 — Operational Threats**
| ID | Threat | Description | Required Protection |
|----|---------|-------------|----------------------|
| T3.1 | Non-compliant Integrations | Clients ignoring invariants | Mandatory validator logic |
| T3.2 | PII Injection | Storing personal data in feed or registry | Zero-PII policy |
| T3.3 | Revocation Bypass | Ignoring terminal lifecycle events | RFC0001 enforcement |

---

### **T4 — Governance Threats**
| ID | Threat | Description | Required Protection |
|----|---------|-------------|----------------------|
| T4.1 | Unauthorized Normative Changes | Modifying RFCs without approval | Governance Council |
| T4.2 | Unanchored Releases | Versions without feed events | SSOT + mandatory feed anchoring |
| T4.3 | Authority Impersonation | Fake entity claiming Root Authority | Authority identity verification |

---

## 4. Threat Mitigation Rules (Normative)

1. All threats MUST be mitigated through Root Authority enforcement.  
2. All threat responses MUST align with the Protection Charter.  
3. Feed-based non-repudiation MUST cover all lifecycle events.  
4. Illegal proofs, entries, or events MUST be rejected.  
5. Violations MUST trigger revocation or invalidation via feed.json.

---

## 5. Validation Requirements

Conformant validators MUST:

- detect structural deviations  
- verify canonical hashing  
- enforce version and revocation boundaries  
- reject malformed or unauthorized entries  
- validator behavior MUST conform to RFC003 §9

---

## 6. Status of This Document
Final, normative, included in CNAUS v1.1.0.
