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
  - LICENSE.md
references:
  - RFC0001
  - RFC0002
  - Feed_Specification.md
  - Revocation_Specification.md
---
# RFC0003 — CNAUS Proof Layer

## 1. Purpose

This document defines the **canonical cryptographic foundation** of the CNAUS Registry.

The Proof Layer guarantees:

- deterministic hashing  
- canonical artifact normalization  
- stable, verifiable proof objects  
- strict version-boundary enforcement  
- hash-linked feed integration  
- offline verifiability  
- integrity and origin guarantees  

This specification is **normative** and **MUST** be implemented unchanged.

---

## 2. Definitions

**Artifact**  
Digital content represented by a canonical SHA-256 hash.

**Canonical Representation**  
The normalized artifact form ensuring deterministic hashing.

**Proof**  
A cryptographic commitment linking a canonical hash, timestamp, and metadata to a registry entry.

**Validator**  
A client verifying registry entries, proofs, feed consistency, and lifecycle constraints.

**Proof Event**  
A feed entry binding a proof hash to a lifecycle transition.

---

## 3. Canonical Representation Rules

Artifacts **MUST** be normalized prior to hashing.

### 3.1 Normalization Rules (Normative)

1. Encoding **MUST** be UTF-8.  
2. Trailing whitespace **MUST** be removed.  
3. Line endings **MUST** normalize to `\n`.  
4. JSON artifacts **MUST** be lexicographically sorted by key.  
5. Binary artifacts **MUST** be hashed using raw bytes.  
6. Compression **MUST NOT** be applied before hashing.  
7. Canonicalization rules **MUST** be identical across all implementations.

Deviation invalidates the proof.

---

## 4. Hash Algorithm (Normative)

CNAUS **mandates** a single deterministic algorithm:

- **Algorithm:** SHA-256  
- **Encoding:** lowercase hexadecimal  
- **Length:** 64 characters  

Requirements:

- Hash MUST be computed on canonical representation.  
- Identical artifacts MUST yield identical hashes.  
- Any content modification MUST produce a different hash.  
- No alternate algorithms are permitted in v1.0.0.

---

## 5. Proof Object Model

Every proof MUST follow the canonical schema:

```json
{
  "hash": "sha256 hex",
  "algorithm": "SHA-256",
  "timestamp": "RFC3339",
  "content_type": "json | text | binary",
  "canonicalization": "CNAUS-1.0",
  "source": "root-authority-id"
}
````

### 5.1 Field Requirements

- `hash` MUST reflect canonical artifact representation.
- `timestamp` MUST be issued by the Root Authority.
- `content_type` MUST accurately describe the artifact.
- `canonicalization` MUST reference an approved CNAUS canonicalization version.
- `source` MUST identify the Root Authority instance.
- Proof objects MUST be embedded inside registry entries (RFC0001).

---

## 6. Proof-of-Integrity Rules

A proof guarantees integrity when:

1. `hash == SHA256(canonical artifact)`
2. Timestamp aligns with feed event
3. Proof binds to a valid registry entry
4. No conflicting proof exists for same version
5. Proof hash appears in the canonical feed
6. Revocation boundary is respected

### Revocation Boundary

For revoked entries, the final `proof_hash`:

- **MUST** be directly bound to the revocation event
- **MUST** be treated as the terminal integrity boundary

Validators **MUST** reject proofs that:

- mismatch canonical hash
- mismatch timestamps
- mismatch registry_id
- appear after revocation
- are missing in feed.json
- reference outdated or conflicting proofs

---

## 7. Proof-of-Origin Rules

A proof guarantees origin when:

1. It is Root Authority–issued
2. It binds to a specific `registry_id`
3. Timestamp matches the first lifecycle event
4. Hash represents earliest valid version
5. No older valid proof exists

### Revocation Boundaries for Origin

- No new proofs MAY be issued for revoked entries.
- Validators MUST treat revocation as the final origin boundary.
- In case of conflicting proofs, the earliest valid proof is authoritative unless revoked.

---

## 8. Version Boundary Rules

Proofs enforce version transitions:

- New proof → new version
- Artifact content change → MINOR or MAJOR
- Metadata-only → PATCH

Version MUST match the corresponding feed event.  
Validators **MUST** reject:

- backwards version jumps
- absent or malformed version numbers
- version conflicts within feed history

Versioning rules defer to `VERSIONING.md`.

---

## 9. Proof Validation Algorithm

(Normative and MUST be implemented exactly)

**Step 1 — Registry Entry Validation**

- Schema validity
- Entry exists
- Entry not revoked (for active-use queries)

**Step 2 — Canonicalization + Hash Recalculation**

- Compute canonical artifact
- SHA-256 → compare to `proof.hash`

**Step 3 — Timestamp Verification**

- Ensure timestamp aligns with associated feed event

**Step 4 — Feed Consistency Validation**

- Matching event MUST exist
- `registry_id` and `version` MUST match feed
- `proof_hash` MUST match event

**Step 5 — Version Boundary Validation**

- Apply SemVer
- No regressions allowed

**Step 6 — Historical / Revocation Consistency**

- No older conflicting proofs
- No new proofs after revocation

Any failure → validator MUST reject.

---

## 10. Feed Binding Requirements

Every proof MUST appear in **exactly one** feed event:

```json
{
  "event_type": "create | update | revoke",
  "registry_id": "ulid",
  "version": "string",
  "proof_hash": "sha256 hex",
  "timestamp": "RFC3339"
}
```

Rules:

1. Feed MUST be strictly chronological.
2. MUST be append-only.
3. Timestamps MUST be monotonic per registry entry.
4. A proof MUST NOT be referenced by multiple events.

---

## 11. Security Requirements

1. Only the Root Authority MAY generate proofs.
2. Proof generation MUST occur inside controlled, trusted infrastructure.
3. Keys or signing material (future extensions) MUST NOT leave secure boundaries.
4. Validators MUST reject malformed or unverifiable proofs.
5. Proof generation MUST be audit-logged.
6. Proofs, artifacts, and feed events MUST NOT contain personal data (Zero-PII).

---

## 12. Compliance Requirements

A client is compliant if it:

- canonicalizes artifacts per Section 3
- computes hashes per Section 4
- validates proofs and feed alignment
- respects version and revocation boundaries
- rejects conflicting or malformed proofs
- logs validation results deterministically

---

## 13. Non-Normative Future Extensions

(Informative)

Potential future enhancements include:

- signature-anchored proofs
- HSM-backed generation
- multi-authority issuance
- zero-knowledge-bound proofs
- compressed proof formats

These MUST NOT affect v1.0.0 compliance.

---

## 14. References

(Informative unless explicitly normative)

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- Feed_Specification.md
- Revocation_Specification.md
- VERSIONING.md
- GOVERNANCE.md    
- LICENSE.md
