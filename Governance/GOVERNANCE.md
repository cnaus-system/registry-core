# CNAUS Registry Core Standard – Governance Framework 
Version B (Public Release)

## 1. Purpose
This document defines the governance structures, decision processes, and
procedural requirements for maintaining the CNAUS Registry Core Standard.  
It provides institutional stability analogous to recognized governance
structures in the IETF, W3C, and ISO ecosystems.

## 2. Governance Principles
All governance processes MUST adhere to the following principles:

- **Neutrality**: CNAUS does not promote specific technologies or vendors.  
- **Integrity**: All changes are validated through the proof and versioning
  mechanisms.  
- **Transparency**: Public visibility is ensured via `feed.json`.  
- **Minimalism**: Only essential rules for registry, proof, and verification are
  maintained.  
- **Backward Compatibility**: Stability is prioritized for implementers and
  regulators.

---

## 3. Governance Council
A CNAUS Governance Council oversees all normative decisions related to:

- RFC creation and modification  
- versioning and release approvals  
- registry invariants  
- proof semantics  
- revocation standards  
- conformance requirements  

Council responsibilities:

1. Maintain normative consistency across RFCs.  
2. Approve or reject proposed changes to the standard.  
3. Publish authoritative updates through `feed.json`.  
4. Enforce the CNAUS License and conformance rules.  

---

## 4. Change Proposal Workflow
Normative changes follow this required process:

1. **Proposal Submission**  
   A formal change request referencing affected sections and rationale.

2. **Compatibility Review**  
   Assessment of backward/forward compatibility, registry invariants, and proof
   stability.

3. **Governance Review**  
   Council evaluates proposal according to CNAUS principles.

4. **Approval and Version Assignment**  
   Upon approval, a version increment is assigned according to `VERSIONING.md`.

5. **Publication**  
   All changes MUST be reflected in:
   - Updated RFC(s)  
   - Updated version tag  
   - `feed.json` entry with timestamp  
   - Repository release notes  

---

## 5. Revocation Policy
The Council MAY issue revocation entries under the following conditions:

- violation of registry invariants  
- invalid proofs or compromised anchors  
- intentional misuse or non-compliant implementations  
- required technical corrections to protect standard integrity  

Revocations MUST:

- be recorded in `feed.json`  
- include a timestamp, asset identifier, and revocation reason  
- remain immutable once published  

---

## 6. Conformance Requirements
Systems claiming CNAUS compliance MUST implement:

- all normative rules in RFC0001–RFC0003  
- the verification semantics defined in the Proof Layer  
- the versioning and revocation rules  
- Zero-PII constraints in proof and asset metadata  

Implementations MAY add optional layers, provided they do not alter or bypass
core semantics.

---

## 7. Governance Amendments
This governance document MAY be amended only through:

- Council approval  
- Updated version assignment  
- Publication in `feed.json`  
- Reference update in `VERSIONING.md`  

No amendment is valid unless all above conditions are met.

---

## 8. References
This governance framework cooperates with:

- RFC0001 Registry Framework  
- RFC0002 API Specification  
- RFC0003 Proof Layer  
- VERSIONING.md  
- LICENSE.md  

It is binding for all public and private implementations claiming CNAUS
compatibility.
