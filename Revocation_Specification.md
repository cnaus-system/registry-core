# CNAUS Revocation Specification  
Version 1.0.0 (Normative)

## 1. Purpose

This specification defines the canonical structure, lifecycle rules, and
processing requirements for revocation events within the CNAUS Registry.

A revocation:

- terminates the active status of a registry entry,  
- freezes its final version state,  
- preserves auditability and proof integrity,  
- MUST NOT remove historical versions.

Revocation is an authoritative Root Authority action and MUST follow this
specification exactly.

---

## 2. Revocation Model

A revocation event is a **final, immutable lifecycle action** applied to a
registry entry.

A revocation MUST:

1. Set `license.status = "revoked"`.  
2. Emit a `revoke` event in the global feed.  
3. Preserve all historical versions.  
4. Bind the revocation to the final proof hash.  
5. Be timestamped with an RFC3339 value from the Root Authority.  

---

## 3. Normative Fields

A revocation MUST follow the canonical schema defined in
`revocation.schema.json`.

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

These values are exhaustive; no custom values may be introduced.

---

## 5. Feed Binding

A revocation MUST appear exactly once in `feed.json`:

```json
{
  "event_id": "ulid",
  "event_type": "revoke",
  "registry_id": "ulid",
  "version": "string",
  "proof_hash": "sha256 hex",
  "timestamp": "RFC3339",
  "details": { ... }
}
````

Rules:

1. Timestamp MUST be strictly monotonic for the registry entry.
2. `proof_hash` MUST match the proof of the last valid version.
3. Registry entries MUST NOT be deleted; they remain readable.
4. All future API responses MUST indicate `"status": "revoked"`.

---

## 6. Interaction with Registry Rules (RFC0001)

Upon revocation:

- Registry entry remains immutable.
- Version MUST NOT increment.
- Proof remains valid for historical verification.
- Clients MUST treat `"revoked"` as a terminal state.
- Verify operations MUST succeed for old versions, fail for new ones.

---

## 7. Interaction with Proof Layer (RFC0003)

Revocation MUST:

1. Bind to the final proof hash.
2. Preserve proof integrity.
3. Not generate new proofs.
4. Be treated as a terminal boundary for the artifact.

Validators MUST reject:

- proofs issued after revocation,
- new versions referencing revoked entries.

---

## 8. Compliance Rules

A client is compliant if it:

- enforces `"revoked"` as a terminal state,
- rejects any update after revocation,
- validates revocation events against the schema,
- respects timestamp ordering,
- uses feed.json as the source of truth.

---

## 9. Security Considerations

1. Only Root Authority MAY revoke.
2. Revocation reasons SHOULD be logged for auditability.
3. Timestamps SHOULD come from a trusted source.
4. revocation events MUST NOT leak personal data.

---

## 10. References

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- RFC0003 — Proof Layer
- Feed_Specification.md
- VERSIONING.md
- GOVERNANCE.md