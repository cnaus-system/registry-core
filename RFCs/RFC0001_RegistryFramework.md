---
title: CNAUS Registry Framework
document_id: RFC0001
version: 1.0.0
status: Normative
layer: Layer 1 – Core Standard
type: Normative Specification
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
dependencies:
  - RFC0002
  - RFC0003
  - GOVERNANCE.md
  - VERSIONING.md
  - LICENSE.md
references:
  - RFC0002
  - RFC0003
  - Feed_Specification.md
  - Revocation_Specification.md
---
# RFC0001 — CNAUS Registry Framework

## 1. Purpose

This document specifies the canonical CNAUS Registry Framework.  
It defines the normative rules for:

- the canonical data model for registry entries  
- lifecycle semantics  
- immutability and integrity guarantees  
- binding to the Proof Layer  
- event semantics reflected in `feed.json`  
- the responsibilities of the Root Authority  
- versioning and compatibility boundaries  

This document is normative and **MUST** be implemented unchanged by all CNAUS-compliant systems.

---

## 2. Definitions

**Registry Entry**  
A structured, immutable record representing origin, integrity, licensing, and version information for a digital artifact.

**Artifact**  
Any digital object represented through a canonical SHA-256 hash.

**Proof**  
A cryptographic commitment binding a canonical artifact hash, timestamp, and required metadata to a registry entry (defined in RFC0003).

**Root Authority**  
The entity responsible for issuing, updating, and revoking registry entries.

**Event**  
A state transition recorded in the canonical feed.

**Client**  
Any external verifier integrating CNAUS semantics.

---

## 3. Canonical Registry Data Model

All registry entries **MUST** comply with the following schema:

```json
{
  "registry_id": "ulid",
  "version": "string (semver)",
  "artifact": {
    "type": "string",
    "name": "string",
    "description": "string"
  },
  "proof": {
    "hash": "sha256 hex",
    "algorithm": "SHA-256",
    "timestamp": "RFC3339"
  },
  "license": {
    "license_id": "string",
    "valid_from": "RFC3339",
    "valid_to": "RFC3339 or null",
    "status": "active | expired | revoked"
  },
  "metadata": {
    "created_at": "RFC3339",
    "updated_at": "RFC3339",
    "created_by": "root-authority-id",
    "notes": "string or null"
  }
}
````

### 3.1 Normative Constraints

1. `registry_id` **MUST** be globally unique (ULID).
2. `version` **MUST** follow Semantic Versioning (`X.Y.Z`).
3. `proof.hash` **MUST** be the SHA-256 hash of the canonical artifact representation (RFC0003).
4. `created_at` **MUST** be immutable.
5. `updated_at` **MUST** change only for valid update events.
6. The registry **MUST NOT** store artifacts themselves (hash-only).
7. Metadata **MUST NOT** contain personal data (Zero-PII constraint).

---

## 4. Lifecycle of a Registry Entry

The CNAUS Registry lifecycle consists of three normative phases:

- **Create**
- **Update**
- **Revoke**

### 4.1 Create

A new registry entry **MUST**:

- generate a unique `registry_id`
- set `version = "1.0.0"`
- embed a canonical proof object (RFC0003)
- emit a `create` event to the feed (`event_type = "create"`)

### 4.2 Update

Updates **MUST**:

- preserve `registry_id`
- increment `version` according to `VERSIONING.md`
- generate a new `proof.hash`
- emit an `update` event (`event_type = "update"`)

Historical entries **MUST** remain permanently readable.

### 4.3 Revoke

Revocation is a **terminal lifecycle state**.

A revocation **MUST**:

- set `license.status = "revoked"`
- preserve all historical versions and proofs
- emit a `revoke` event (`event_type = "revoke"`)
- bind to the final valid proof hash
- include a normative `revocation_reason` value

No further changes **MAY** occur to a revoked `registry_id`.

---

## 5. Immutability Guarantees

The CNAUS Registry **MUST** ensure:

1. No deletion of registry entries.
2. Lifecycle events are strictly append-only.
3. Hashes are deterministic and canonical.
4. Feed timestamps MUST be monotonic per `registry_id`.
5. Major version increments reflect breaking changes.
6. Historical versions remain permanently accessible.
7. Revoked entries remain verifiable indefinitely.

Clients **MUST** reject any entry violating these invariants.

---

## 6. Binding to Proof Layer (RFC0003)

1. Every registry entry **MUST** embed a proof object.
2. `proof.hash` **MUST** match the canonical artifact hash.
3. Proofs **MUST** be verifiable offline.
4. Proof modifications **MUST** trigger a version increment.
5. For revoked entries, the final proof hash **MUST** correspond to the revocation event.

---

## 7. Event Model (feed.json)

All registry lifecycle transitions **MUST** be emitted to the canonical feed:

```json
{
  "event_id": "ulid",
  "event_type": "create | update | revoke",
  "registry_id": "ulid",
  "version": "string (semver)",
  "proof_hash": "sha256 hex",
  "timestamp": "RFC3339",
  "details": "object or null"
}
```

### Event Requirements

- Events **MUST** be strictly chronological.
- Events **MUST** be append-only.
- Timestamps **MUST** be monotonic per `registry_id`.
- `prev_hash` link semantics are defined in the Feed Specification.

---

## 8. Versioning Rules

Registry version semantics **MUST** follow `VERSIONING.md`:

- **Major** → breaking changes
- **Minor** → additive, backward-compatible changes
- **Patch** → editorial or non-normative clarifications

All normative changes **MUST** appear as root events in the feed.

---

## 9. Security Requirements

1. Only the Root Authority **MAY** create, update, or revoke registry entries.
2. Registry modifications **MUST** require authenticated, controlled access.
3. Proof generation **MUST** occur in a controlled, trusted environment.
4. Feed publication **MUST** be atomic and append-only.
5. Clients **MUST** validate all proofs, hashes, and lifecycle constraints.
6. Registry, proofs, and feed entries **MUST NOT** contain personal data.

---

## 10. Compliance Requirements

A system is CNAUS-compliant if it:

- stores entries according to this RFC
- enforces lifecycle and immutability invariants
- binds proofs according to RFC0003
- emits events conforming to the Feed Specification
- respects revocation as terminal
- rejects malformed or non-conformant entries

---

## 11. Non-Normative Extensions

(Informative)

Future RFCs **MAY** define optional extensions, including:

- multi-tenant registries
- delegated authorities
- mirrored registries
- regulator-specific views

---

## 12. References

(Informative unless specifically cited as normative)

- RFC0002 — API Specification
- RFC0003 — Proof Layer
- Feed_Specification.md
- Revocation_Specification.md
- VERSIONING.md
- GOVERNANCE.md
- LICENSE.md