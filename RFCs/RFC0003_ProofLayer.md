---
title: CNAUS Proof Layer
document_id: RFC0003
version: 1.0.0
status: Normative
layer: Layer 1 – Core Standard
type: Normative Specification
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
dependencies:
  - RFC0001
  - RFC0002
  - GOVERNANCE.md
  - VERSIONING.md
  - Root_Authority_Specification.md
  - Revocation_Specification.md
  - Feed_Specification.md
references:
  - RFC0001
  - RFC0002
  - Feed_Specification.md
  - Revocation_Specification.md
---
## 1. Purpose

This specification defines the canonical proof semantics for CNAUS.

A proof is a deterministic, globally verifiable integrity object that binds:

- a registry entry identifier (`registry_id`),
- a specific semantic version (`version`),
- a canonical hash derived from strict normalization rules.

---

## 2. Canonicalization (Normative)

Canonicalization MUST be deterministic and stable across platforms.

### 2.1 Canonical JSON

If the proof hashes a JSON artifact, canonicalization MUST follow:

- UTF-8 encoding
- lexicographic key ordering
- no insignificant whitespace
- stable numeric representation
- stable string encoding

The canonical form MUST be hashed with SHA-256.

---

## 3. Proof Object (Normative)

A proof object MUST contain:

- `registry_id` (ULID)
- `version` (SemVer)
- `canonical_hash` (SHA-256 hex)
- `algorithm` (fixed: SHA-256)
- `issued_at` (RFC3339)
- `issuer` (Root Authority identity)
- `feed_binding` (event identifier and timestamp)

---

## 4. Validator Requirements (Normative)

Validators MUST:

1. Recompute the canonical hash for a given artifact.
2. Compare it to the proof’s `canonical_hash`.
3. Confirm proof binds to a valid registry entry.
4. Reject if any conflicting proof exists for the same `registry_id` and `version`.
5. Confirm `proof_hash` appears in the canonical feed.
6. Enforce revocation boundaries (Revocation Specification).

---

## 5. Anti-Equivocation Rules (Normative)

For a given `registry_id` and `version`:

- there MUST exist at most one canonical proof hash.
- any conflict MUST be treated as fatal.

---

## 6. Revocation Boundary (Normative)

For revoked entries, the final `proof_hash`:

- MUST be directly bound to the revocation event,
- MUST be treated as the terminal integrity boundary.

Validators MUST reject proofs that occur after a revocation boundary.

---

## 7. Proof-of-Origin Rules (Normative)

A proof guarantees origin when:

1. It is Root Authority–issued.
2. It binds to a specific `registry_id`.
3. It is present in the canonical feed.
4. No older valid proof exists for the same version boundary.
5. No revocation boundary invalidates it.

---

## 8. Proof Publication (Normative)

Proofs MUST be published via:

- the canonical feed (proof binding),
- the canonical proof retrieval endpoint (`/v1/proof/...`) in RFC0002.

---

## 9. Proof Lifecycle (Normative)

Proof issuance MUST follow the registry lifecycle:

- `create` → proof MAY be issued for initial version
- `update` → proof MUST be issued for updated version
- `revoke` → proof issuance MUST stop

---

## 10. Feed Binding Requirements

Every proof MUST appear in **exactly one** feed event, as defined in the CNAUS Feed Specification.

```json
{
  "event_id": "01JH0V1QW3A5B7C9D2E4F6G8H0",
  "event_type": "create | update | revoke",
  "registry_id": "ulid",
  "version": "semver",
  "proof_hash": "sha256 hex",
  "timestamp": "RFC3339",
  "prev_hash": "sha256 hex or null",
  "details": {}
}
```

Rules:

1. Feed event objects MUST conform to the CNAUS Feed Specification.
2. Feed MUST be strictly chronological (oldest → newest).
3. Feed MUST be append-only.
4. The `prev_hash` chain MUST validate across the full feed snapshot.
5. A proof MUST NOT be referenced by multiple events.

---

## 11. Security Requirements

1. Only the Root Authority MAY generate proofs.
2. Proof generation MUST occur inside controlled, trusted infrastructure.
3. Keys or signing material (future extensions) MUST NOT leave secure boundaries.
4. Validators MUST reject malformed or ambiguous inputs.

---

## 12. References

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- Feed Specification
- Revocation Specification
- Root Authority Specification
- GOVERNANCE.md
- VERSIONING.md