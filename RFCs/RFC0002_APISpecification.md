---
title: CNAUS Registry API Specification
document_id: RFC0002
version: 1.0.0
status: Normative
layer: Layer 1 – Core Standard
type: Normative Specification
issued: 2025-12-11
updated: 2025-12-11
authority: CNAUS Root Authority
dependencies:
  - RFC0001
  - RFC0003
  - GOVERNANCE.md
  - VERSIONING.md
  - LICENSE.md
references:
  - VERSIONING.md
  - Feed_Specification.md
  - RFC0001
  - RFC0003
---
# RFC0002 — CNAUS Registry API Specification

## 1. Purpose

This document specifies the **normative CNAUS Registry API**, used by external clients to:

- retrieve canonical registry entries  
- retrieve cryptographic proofs  
- inspect lifecycle events  
- validate artifact integrity  
- determine active CNAUS specification versions  

The CNAUS API is:

- minimal  
- read-only for external clients  
- stable across versions  
- implementation-neutral  

All write operations (create, update, revoke) are exclusively performed by the **CNAUS Root Authority**  
and MUST NOT be exposed to external clients.

This document is **normative**.

---

## 2. API Versioning Model

All endpoints **MUST** begin with a version prefix:

```

/v1/...

```

### Versioning Rules

1. Breaking changes → new major prefix (`/v2/...`).  
2. Additive changes → MINOR version update.  
3. Editorial corrections → PATCH update.  

---

## 3. Endpoint Definitions (Normative)

All responses **MUST** be deterministic and canonical.

---

### 4.1 GET /v1/registry/{registry_id}

**Purpose**  
Retrieve a canonical registry entry.

**Successful Response (200)**

```json
{
  "registry_id": "ulid",
  "version": "string",
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
```

---

### 4.2 GET /v1/proof/{registry_id}/{version}

**Purpose**  
Retrieve the canonical proof object for a given registry version.

**Successful Response (200)**
```json
{
  "registry_id": "ulid",
  "version": "semver",
  "canonical_hash": "sha256 hex",
  "algorithm": "SHA-256",
  "issued_at": "RFC3339",
  "issuer": "CNAUS Root Authority",
  "feed_binding": {
    "event_id": "ulid",
    "timestamp": "RFC3339"
  }
}
```

---

### 4.3 GET /v1/revocation/{registry_id}/{version}

**Purpose**  
Retrieve revocation information for a registry version.

**Successful Response (200)**
```json
{
  "registry_id": "ulid",
  "version": "semver",
  "revoked": true,
  "revoked_at": "RFC3339",
  "revocation_reason": "enum",
  "proof_hash": "sha256 hex",
  "details": {}
}
```

---

### 4.4 GET /v1/feed

**Purpose**  
Expose the canonical append-only event feed.

**Successful Response (200)**

```json
{
  "version": "1.0.0",
  "feed_generated_at": "RFC3339",
  "events": [
    {
      "event_id": "01JH0V1QW3A5B7C9D2E4F6G8H0",
      "event_type": "create | update | revoke | standard.initial_public_release | standard.version_update",
      "registry_id": "ulid or null",
      "version": "semver or null",
      "proof_hash": "sha256 hex or null",
      "timestamp": "RFC3339",
      "prev_hash": "sha256 hex or null",
      "details": {}
    }
  ]
}
```

**Normative Requirements**
1. Feed MUST follow the CNAUS Feed Specification exactly.
2. Feed MUST include all `create`, `update`, and `revoke` events.
3. Feed MUST be append-only.
4. Feed MUST reflect the current Root Authority state.
5. Feed MUST be deterministic across mirrors.

---

### 4.5 POST /v1/verify

**Purpose**  
Validate a proof and registry entry combination.

**Request Body**
```json
{
  "registry_id": "ulid",
  "version": "semver",
  "proof_hash": "sha256 hex"
}
```

Validation Response (200 – valid)
```json
{
  "valid": true,
  "reason": "hash matches canonical artifact",
  "registry_id": "ulid",
  "version": "semver"
}
```

**Validation Response (200 – invalid)**
```json
{
  "valid": false,
  "reason": "proof not found in feed or hash mismatch",
  "registry_id": "ulid",
  "version": "semver"
}
```

---

## 5. Error Model (Normative)

Errors MUST be deterministic.
```json
{
  "error": "string",
  "message": "string",
  "status": 400
}
```

---

## 6. Security Notes

- This API is read-only for implementers.
- Only the Root Authority operates write paths.
- Rate limiting and caching MAY be applied, but responses MUST remain canonical.

---

## 7. References

- RFC0001 — Registry Framework
- RFC0003 — Proof Layer
- Feed Specification
- Revocation Specification
- Root Authority Specification
- VERSIONING.md
- GOVERNANCE.md