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
3. Editorial/non-normative clarifications → PATCH update.  
4. Deprecated endpoints **MUST** remain functional for at least one MINOR version.  
5. The API **MUST** declare its active version at:

```

GET /v1/version

````

---

## 3. Endpoint Overview (Normative)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/registry/{registry_id}` | GET | Retrieve canonical registry entry |
| `/v1/registry/{registry_id}/proof` | GET | Retrieve latest proof object |
| `/v1/registry/{registry_id}/events` | GET | Retrieve lifecycle event history |
| `/v1/feed` | GET | Retrieve global canonical CNAUS feed |
| `/v1/version` | GET | Retrieve version declarations |
| `/v1/validate/hash` | POST | Validate client-supplied hash |

All endpoints **MUST** be:

- idempotent  
- side-effect free  
- strongly consistent with the canonical `feed.json`

---

## 4. Endpoint Specifications

---

### 4.1 GET /v1/registry/{registry_id}

**Purpose**  
Return the canonical registry entry defined in RFC0001.

**Requirements**

- `registry_id` MUST be a valid ULID.
- Response schema MUST match RFC0001 exactly.

**Successful Response (200)**  
(MUST match Registry Data Model)

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
````

**Error Conditions**

- `400` invalid ULID
- `404` registry entry not found

---

### 4.2 GET /v1/registry/{registry_id}/proof

**Purpose**  
Return the canonical proof object (latest version), defined in RFC0003.

**Successful Response (200)**

```json
{
  "registry_id": "ulid",
  "version": "string",
  "proof": {
    "hash": "sha256 hex",
    "algorithm": "SHA-256",
    "timestamp": "RFC3339",
    "content_type": "json | text | binary",
    "canonicalization": "CNAUS-1.0",
    "source": "root-authority-id"
  }
}
```

**Normative Rules**

1. If `registry_id` is revoked → endpoint MUST return **410 Gone**.
2. The last valid proof MUST NOT be returned for revoked entries.
3. Proofs MUST match RFC0003 invariants.

**Error Conditions**

- `404` entry not found
- `410` entry revoked

---

### 4.3 GET /v1/registry/{registry_id}/events

**Purpose**  
Return lifecycle events associated with a registry entry, bound to `feed.json`.

**Successful Response (200)**

```json
{
  "registry_id": "ulid",
  "events": [
    {
      "event_id": "ulid",
      "event_type": "create | update | revoke",
      "version": "string",
      "proof_hash": "sha256 hex",
      "timestamp": "RFC3339"
    }
  ]
}
```

**Normative Requirements**

- Events MUST be identical to the canonical global feed.
- Events MUST be strictly chronological.
- Events MUST be immutable.

---

### 4.4 GET /v1/feed

**Purpose**  
Expose the canonical append-only event feed.

**Successful Response (200)**

```json
{
  "cnaus_feed_version": "1.0.0",
  "generated_at": "RFC3339",
  "events": [...]
}
```

**Normative Requirements**

1. Feed MUST include all `create`, `update`, and `revoke` events.
2. Feed MUST be append-only.
3. Feed MUST reflect the current Root Authority state.
4. Feed MUST be deterministic across mirrors.
5. Feed MUST follow hash-linked ordering as defined in the Feed Specification.

---

### 4.5 GET /v1/version

**Purpose**  
Expose version declarations for CNAUS components.

**Response (200)**

```json
{
  "cnaus_api_version": "1.0.0",
  "registry_spec_version": "1.0.0",
  "proof_layer_version": "1.0.0",
  "governance_version": "1.0.0"
}
```

Versions MUST match the SSOT (Repo + feed.json).

---

### 4.6 POST /v1/validate/hash

**Purpose**  
Validate a client-provided hash against the canonical registry entry.

**Request Schema**

```json
{
  "registry_id": "ulid",
  "hash": "sha256 hex"
}
```

**Validation Response (200 – valid)**

```json
{
  "valid": true,
  "reason": "hash matches canonical artifact",
  "registry_id": "ulid",
  "version": "string"
}
```

**Validation Response (200 – invalid)**

```json
{
  "valid": false,
  "reason": "hash does not match canonical artifact",
  "registry_id": "ulid",
  "version": "string"
}
```

**Normative Requirements**

- Validation MUST be stateless.
- Hash comparison MUST use canonicalization rules from RFC0003.

**Error Conditions**

- `400` malformed request
- `404` registry entry not found

---

## 5. Security Requirements

1. Endpoints MUST be served over HTTPS (TLS 1.2+).
2. Responses MUST NOT contain personal data (Zero-PII constraint).
3. Feed responses MAY be cached but MUST remain immutable.
4. Rate limits SHOULD mitigate abuse.
5. Root Authority cryptographic material MUST NOT be exposed.
6. API implementations MUST reject malformed or ambiguous requests.    

---

## 6. Compliance Requirements

A system is CNAUS-compliant if it:

- retrieves registry entries using this RFC
- validates proofs according to RFC0003
- respects lifecycle rules in RFC0001
- inspects revocation events and obeys terminal state rules
- respects version boundaries declared in `/v1/version`
- rejects inconsistent hashes or malformed entries    

---

## 7. Non-Normative Extensions

(Informative)

Optional extensions (not part of the normative API):

- `/v1/mirror` endpoint
- compressed feeds
- signed API responses
- enterprise-optimized read patterns    

Such extensions **MUST NOT** modify any normative requirement.

---

## 8. References

(Informative unless explicitly normative)

- RFC0001 — Registry Framework
- RFC0003 — Proof Layer
- Feed_Specification.md
- VERSIONING.md
- GOVERNANCE.md
- LICENSE.md    