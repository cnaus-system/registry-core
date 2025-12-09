---
title: "CNAUS Registry Framework"
document_id: "RFC0001"
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
# RFC0001 — CNAUS Registry Framework

## 1. Purpose

This RFC defines the canonical CNAUS Registry Framework.  
It establishes:

- the **canonical data model** for registry entries  
- the **lifecycle rules** for all registry entries  
- the **immutability and integrity guarantees**  
- the **binding to the Proof Layer**  
- the **event semantics** reflected in `feed.json`  
- the **responsibility of the Root Authority**  
- the **versioning boundaries** required for compatibility  

This RFC is normative and MUST be implemented unchanged by all compliant systems.

---

## 2. Definitions

**Registry Entry**  
A structured, immutable record representing origin, integrity, licensing and versioning information for an artifact.

**Artifact**  
Any digital object represented through a canonical SHA-256 hash.

**Proof**  
A cryptographic commitment linking a hash, timestamp, and canonicalization metadata to a registry entry.

**Root Authority**  
The entity responsible for issuing, updating and revoking registry entries.

**Event**  
A state transition recorded in `feed.json`.

**Client**  
Any external verifier integrating CNAUS.

---

## 3. Canonical Registry Data Model

All registry entries MUST comply with the following schema:

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

1. `registry_id` MUST be globally unique (ULID).
2. `version` MUST follow Semantic Versioning (`X.Y.Z`).
3. `proof.hash` MUST be the SHA-256 hash of the canonical artifact representation (see RFC0003).
4. `created_at` MUST be immutable.
5. `updated_at` MUST change only for valid update events.
6. The registry MUST NOT store artifacts themselves (hash-only).
7. Metadata MUST NOT contain personal data (Zero-PII constraint).

---

## 4. Lifecycle of a Registry Entry

The CNAUS Registry lifecycle consists of three normative phases:

- **Create**
- **Update**
- **Revoke**

### 4.1 Create

A new registry entry MUST:

- generate a unique `registry_id`
- set `version = "1.0.0"`
- store the canonical proof object (see RFC0003)
- emit a `create` event to the feed (`event_type = "create"`)

### 4.2 Update

Updates MUST:

- preserve `registry_id`
- increment `version` according to `VERSIONING.md`
- generate a new `proof.hash`
- emit an `update` event to the feed (`event_type = "update"`)

Historical entries MUST remain valid and readable.

### 4.3 Revoke

Revocation is a **terminal lifecycle state**.

A revocation MUST:

- set `license.status = "revoked"`
- preserve all historical versions and proofs
- emit a `revoke` event in the global feed (`event_type = "revoke"`)
- follow the CNAUS Revocation Specification (v1.0.0)
- bind to the final `proof_hash` of the last valid version
- include a normative `revocation_reason` value

No further updates or new versions MAY be issued after revocation for the same `registry_id`.

---

## 5. Immutability Guarantees

The CNAUS Registry MUST ensure:

1. No deletion of registry entries.
2. All lifecycle events MUST be append-only.
3. Hashes MUST be deterministic and canonical.
4. Feed timestamps MUST be strictly monotonic per `registry_id`.
5. Major version changes MUST reflect breaking changes.
6. Historical versions MUST remain forever accessible.
7. **Revoked entries MUST remain permanently readable**; all historical proofs, versions and events MUST remain verifiable after revocation.

Clients MUST reject entries violating these guarantees.

---

## 6. Binding to Proof Layer

The Registry Framework is tightly bound to RFC0003:

1. Every registry entry MUST embed a proof object.
2. `proof.hash` MUST match the canonical artifact representation.
3. Proofs MUST be verifiable offline.
4. Proof changes MUST trigger a version increment.

For revoked entries, the final proof hash MUST correspond to the revocation event.

---

## 7. Event Model (feed.json)

All registry lifecycle transitions MUST be emitted to `feed.json`:

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

Rules:

- Events MUST be strictly chronological.
- Events MUST be append-only.
- For each `registry_id`, timestamps MUST be monotonic.

The feed is defined in detail in `Feed_Specification.md`.

---

## 8. Versioning Rules

CNAUS MUST follow `VERSIONING.md`:

- Major = breaking changes.
- Minor = additive, backward compatible.
- Patch = editorial / non-normative clarifications.
- All changes MUST be recorded as standard events in `feed.json`.

Registry version fields MUST reflect these rules.

---

## 9. Security Requirements

1. Only the Root Authority MAY create, update or revoke registry entries.
2. Registry modifications MUST require authenticated, controlled access.
3. Proof generation MUST occur on a trusted system.
4. Feed publication MUST be atomic and append-only.
5. Clients MUST validate hash consistency and lifecycle constraints before trusting data.
6. No personal data MAY be stored in registry entries, proofs or feed events.

---

## 10. Compliance Requirements

A system is CNAUS-compliant if it:

- stores registry entries according to this RFC
- enforces lifecycle and immutability rules
- binds proofs according to RFC0003
- emits events conforming to `Feed_Specification.md`
- respects revocation as a terminal state
- rejects malformed or non-conformant entries

---

## 11. Non-Normative Extensions

These MAY be introduced in later RFCs but are not required for v1.0.0:

- multi-tenant registries
- delegated authorities
- mirrored registries
- specialized views for regulators

---

## 12. References

- RFC0002 — API Specification
- RFC0003 — Proof Layer
- Feed_Specification.md
- Revocation_Specification.md
- VERSIONING.md
- GOVERNANCE.md
- LICENSE.md