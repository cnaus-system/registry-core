# CNAUS Revocation Specification  
Version 1.0.0 (Normative)

## 1. Purpose

This specification defines the canonical semantics and schema requirements for
revocation events in CNAUS.

A revocation event represents an authoritative lifecycle transition that:

- terminates an entry’s validity,
- prevents further proof issuance,
- defines the final integrity boundary for the entry.

Revocation is binding and MUST be enforced by all validators.

---

## 2. Scope

This document defines:

- normative revocation semantics,
- required fields and schema constraints,
- allowed revocation reasons,
- binding rules to the CNAUS feed.

---

## 3. Normative Fields

A revocation MUST follow the canonical schema defined in
`schemas/revocation.schema.json`.

Required fields:

| Field | Meaning |
|-------|---------|
| `registry_id` | Identifier of revoked entry |
| `version` | Version at time of revocation |
| `revoked_at` | Timestamp of revocation event |
| `revocation_reason` | Normative classification (enum) |
| `proof_hash` | Proof hash of final valid version |
| `details` | Optional metadata |

---

## 4. Allowed Revocation Reasons (Enum)

- `license.expired`  
- `license.terminated`  
- `proof.compromised`  
- `content.replaced`  
- `regulatory.requirement`  
- `root-authority.action`  

These values are exhaustive for v1.0.0.

---

## 5. Feed Binding Rules

A revocation MUST be represented in the canonical feed as an event:

- `event_type = "revoke"`
- `registry_id` MUST match the revoked entry
- `version` MUST match the revoked version
- `proof_hash` MUST equal the terminal proof boundary (same as the revocation object `proof_hash`)
- `timestamp` MUST equal or exceed `revoked_at`

---

## 6. Validator Requirements

Validators MUST:

1. Reject any registry entry state that is revoked.
2. Reject proofs for any version at or after the revoked version.
3. Treat the revocation’s `proof_hash` as the final integrity boundary.
4. Enforce reason enums strictly.

---

## 7. Security Notes

- Revocation objects MUST NOT contain personal data in `details`.
- Revocation issuance is restricted to the Root Authority (see Root Authority Specification).
- Mirrors MAY cache revocation data but MUST NOT alter it.

---

## 8. References

- Feed Specification
- Root Authority Specification
- RFC0001 — Registry Framework
- RFC0003 — Proof Layer
- GOVERNANCE.md
- VERSIONING.md
