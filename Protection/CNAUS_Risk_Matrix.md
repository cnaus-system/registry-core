---
title: CNAUS Risk Matrix
status: Informative
conformance_scope: Non-Core
authority: CNAUS Root Authority
---
# CNAUS Risk Matrix  

## 1. Purpose
This document defines the **normative risk classification system** for the  
CNAUS Registry Core Standard.  
It enables consistent risk identification, severity scoring, mitigation  
planning, and regulatory-grade integrity protection.

The matrix is binding for all CNAUS-compliant systems.

---

## 2. Risk Scoring Model (Normative)

Each risk is scored by two metrics:

### **Likelihood (L)**
1 – Very Low  
2 – Low  
3 – Moderate  
4 – High  
5 – Very High  

### **Impact (I)**
1 – Minimal  
2 – Limited  
3 – Significant  
4 – Critical  
5 – Catastrophic (system integrity compromised)

### **Risk Score = L × I**
- 1–5: Low  
- 6–10: Medium  
- 12–15: High  
- 16–25: Severe  

Severe risks require mandatory mitigation.

---

## 3. CNAUS Core Risk Matrix (Normative)

| ID  | Category     | Description                                                    | L   | I   | Score       | Required Mitigation                                              |
| --- | ------------ | -------------------------------------------------------------- | --- | --- | ----------- | ---------------------------------------------------------------- |
| R1  | Structural   | Registry forking or alternative definitions of CNAUS semantics | 4   | 5   | 20 (Severe) | Enforce Root Authority exclusivity; reject non-canonical mirrors |
| R2  | Integrity    | Modification of historical feed entries                        | 3   | 5   | 15 (High)   | Append-only feed enforcement; monotonic timestamps               |
| R3  | Integrity    | Incorrect canonicalization or hashing                          | 3   | 4   | 12 (High)   | Enforce RFC0003; mandatory validator checks                      |
| R4  | Security     | Unauthorized registry updates                                  | 2   | 5   | 10 (Medium) | Root Authority access control; audit logging                     |
| R5  | Compliance   | Zero-PII violation in registry or feed events                  | 3   | 3   | 9 (Medium)  | Automated PII detection and strict metadata filters              |
| R6  | Lifecycle    | Invalid or missing revocation handling                         | 2   | 4   | 8 (Medium)  | Mandatory revocation algorithm checks                            |
| R7  | Versioning   | Version regression or inconsistent SemVer                      | 2   | 4   | 8 (Medium)  | Strict SemVer validation; validator enforcement                  |
| R8  | Governance   | Unauthorized normative amendments                              | 2   | 5   | 10 (Medium) | Governance Council approval; feed anchoring                      |
| R9  | Operational  | Non-compliant client integrations                              | 3   | 2   | 6 (Medium)  | Compliance Guide enforcement; integration certification          |
| R10 | Availability | Loss of Root Authority infrastructure                          | 1   | 5   | 5 (Low)     | Secure backups; redundant storage; sealed release packages       |

---

## 4. Mitigation Requirements (Normative)

1. Severe risks (Score ≥ 16) MUST have enforceable, Root-Authority-level controls.  
2. High risks MUST be mitigated at validator and governance layers.  
3. Medium risks MUST be monitored and documented in compliance workflows.  
4. Low risks MAY be addressed operationally but must not break invariants.

---

## 5. Compliance

Conformance requires:

- maintaining the latest CNAUS Risk Matrix  
- documenting residual risk  
- rejecting any integration that increases severity without mitigation
- residual risk documentation MUST be retained for audit purposes

---

## 6. Status of This Document

Final, normative, included in CNAUS v1.1.0, hash-ready.
