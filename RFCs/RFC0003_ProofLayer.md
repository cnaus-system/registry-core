---
title: "CNAUS Proof Layer"
document_id: "RFC0003"
version: "1.0.0"
status: "Final"
layer: "Layer 1 – Core Standard"
type: "Normative Specification"
issued: "2025-12-09"
updated: "2025-12-09"
authority: "CNAUS Registry Core Standard"
dependencies:
  - RFC0001
  - RFC0002
  - RFC0003
references:
  - GOVERNANCE.md
  - VERSIONING.md
  - LICENSE.md
---
# RFC0003 — CNAUS Proof Layer

## 1. Purpose

The CNAUS Proof Layer defines the **cryptographic foundation** of the CNAUS Registry.  
It ensures that every artifact can be verified through:

- deterministic hashing  
- canonical representation rules  
- stable proof objects  
- strict version-boundary enforcement  
- feed-backed event linkage  
- offline verifiability  

This RFC is normative and MUST be implemented unchanged.

---

## 2. Definitions

**Artifact**  
Digital content represented by a canonical hash.

**Canonical Representation**  
The normalized form of an artifact that guarantees deterministic hashing.

**Proof**  
A cryptographic commitment linking a hash, timestamp, and canonicalization metadata to a registry entry.

**Validator**  
A client verifying registry entries, proofs, and feed consistency.

**Proof Event**  
A feed entry binding a proof hash to a lifecycle event.

---

## 3. Canonical Representation Rules

To guarantee deterministic and reproducible hashing, all artifacts MUST be normalized prior to hashing.

### 3.1 Normalization Rules (Normative)

1. Encoding MUST be UTF-8 (binary artifacts MAY be base64-encoded before transport; hashing uses raw bytes).  
2. Trailing whitespace MUST be removed.  
3. Line endings MUST be normalized to `\n`.  
4. JSON artifacts MUST be lexicographically sorted by key.  
5. Binary artifacts MUST be hashed in their raw byte form.  
6. Compression MUST NOT be applied before hashing.  

Clients MUST implement these rules exactly.  
Deviation produces invalid proofs.

---

## 4. Hash Algorithm (Normative)

CNAUS mandates a single algorithm:

Algorithm: SHA-256  
Output: Hexadecimal, lowercase  
Length: 64 characters

Requirements:

- Hash MUST be computed on the canonical representation.  
- Identical artifacts MUST produce identical hashes.  
- Any content change MUST produce a different hash.  

No alternative algorithms are permitted in v1.0.0.

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
- `content_type` MUST describe the artifact type.
- `canonicalization` MUST reference the applicable normalization protocol.
- `source` MUST identify the issuing Root Authority instance.    

Proof objects MUST be embedded inside registry entries (see RFC0001).

---

## 6. Proof-of-Integrity Rules

A proof provides integrity guarantees when:

1. The hash equals SHA-256(canonical artifact).
2. The timestamp is valid and aligns with feed events.
3. The proof is bound to a valid registry entry.
4. No conflicting proof exists for the same registry version.
5. The proof hash appears in the corresponding feed event.

For **revoked entries**, the final `proof_hash`:

- MUST bind directly to the revocation event, and
- MUST be treated as the terminal integrity boundary for that artifact.

Validators MUST reject proofs that:

- mismatch hashes,
- mismatch timestamps,
- mismatch registry_id references,
- refer to revoked entries as if they were active,
- do not appear in `feed.json`,
- are issued after a revocation event.

---

## 7. Proof-of-Origin Rules

A proof guarantees origin when:

1. It is issued by the Root Authority.
2. It is bound to a specific `registry_id`.
3. Its timestamp aligns with the first corresponding lifecycle event.
4. The hash represents the earliest known version of the artifact.
5. There are no older valid proofs for the same registry entry.

Revocation establishes an **upper boundary on origin**:

- No new origins or proofs MAY be associated with a revoked `registry_id`.
- Validators MUST treat the revocation event as final for origin claims.

If two proofs conflict, the chronologically earlier one is authoritative unless revoked.

---

## 8. Version Boundary Rules

Proofs enforce version transitions:

1. **New proof = new version.**
2. Proof changes determine version bump:
    - Artifact content change → MINOR or MAJOR
    - Metadata-only change → PATCH
3. Version MUST appear in feed events.
4. Validators MUST reject version regressions.

All versioning rules delegate to `VERSIONING.md`.

---

## 9. Proof Validation Algorithm

Compliant validators MUST perform:

### Step 1 — Registry Entry Validation

- JSON schema correct.
- Entry exists and is not revoked (for active-use cases).

### Step 2 — Canonicalization + Hash Recalculation

- Compute SHA-256(canonical artifact).
- Compare to `proof.hash`.

### Step 3 — Timestamp Verification

- Verify that `timestamp` matches the associated feed event.

### Step 4 — Feed Consistency Validation

- Check that an event with matching `proof_hash` exists.
- Check that `registry_id` and `version` match.

### Step 5 — Version Boundary Validation

- Apply SemVer rules.
- Ensure no backward jumps.

### Step 6 — Historical and Revocation Consistency

- Ensure no conflicting proofs exist in earlier events.
- Ensure no proofs are used after revocation.

Any failure at any step MUST cause the validator to reject the artifact.

---

## 10. Feed Binding Requirements

Every proof MUST appear in exactly one feed event:

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

- Feed MUST be strictly chronological.
- Append-only, never mutable.
- Timestamps MUST be monotonic per registry entry.
- A proof MUST NOT be referenced by multiple events.

---

## 11. Security Requirements

1. Only the Root Authority MAY generate proofs.
2. Proof generation MUST occur within controlled, secure infrastructure.
3. Keys (future signing extensions) MUST NOT leave secure boundaries.
4. Validators MUST reject malformed or unverifiable proofs.
5. Proof generation MUST be audit-logged.

---

## 12. Compliance Requirements

A client is compliant with RFC0003 if it:

- canonicalizes artifacts correctly,
- computes SHA-256 hashes correctly,
- validates timestamps and feed alignment,
- enforces version boundaries,
- respects revocation boundaries,
- rejects revoked or conflicting proofs,
- logs validation outcomes deterministically.

---

## 13. Non-Normative Future Extensions

Potential future enhancements:

- signature-anchored proofs,
- HSM-generated proofs,
- distributed multi-authority proof issuance,
- zero-knowledge proof anchoring,
- compressed proof formats.

These are optional and MUST NOT affect v1.0.0 implementations.

---

## 14. References

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- Feed_Specification.md
- Revocation_Specification.md
- VERSIONING.md
- GOVERNANCE.md
- LICENSE.md