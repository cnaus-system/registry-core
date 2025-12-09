---
title: "CNAUS Registry API Specification"
document_id: "RFC0002"
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

# RFC0002 — CNAUS Registry API Specification
# **1. Purpose**

This RFC defines the **normative CNAUS Registry API** used by external clients to:

- retrieve registry entries
- retrieve cryptographic proofs
- inspect lifecycle events
- validate artifact integrity
- determine specification versions in use

The CNAUS API is intentionally:

- **minimal**
- **read-only**
- **stable across versions**
- **implementation-neutral**

No write operation is publicly exposed.  
All write operations are performed **exclusively by the CNAUS Root Authority**.

---

# **2. API Versioning Model**

All endpoints MUST begin with a version prefix:

```
/v1/...
```

Rules:

- Breaking changes → `/v2/...`
- Additive changes → minor version update
- Editorial/clarifications → patch version update
- Deprecated endpoints MUST remain functional for at least one MINOR version

The API MUST always report its running version at `/v1/version`.

---

# **3. Endpoint Overview (Normative)**

|Endpoint|Method|Description|
|---|---|---|
|`/v1/registry/{registry_id}`|GET|Retrieve canonical registry entry|
|`/v1/registry/{registry_id}/proof`|GET|Retrieve proof object|
|`/v1/registry/{registry_id}/events`|GET|Retrieve lifecycle event history|
|`/v1/feed`|GET|Retrieve the global CNAUS event feed|
|`/v1/version`|GET|Retrieve CNAUS version declarations|
|`/v1/validate/hash`|POST|Validate a client-supplied hash|

All endpoints MUST be idempotent, side-effect free, and strongly consistent with `feed.json`.

---

# **4. Endpoint Specifications**

## **4.1 GET /v1/registry/{registry_id}**

**Purpose**  
Return the canonical registry entry defined in RFC0001.

**Inputs**  
`registry_id` — ULID format, MUST be validated.

**Successful Response (200)**  
Schema MUST match the canonical Registry Data Model:

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

**Error Cases**

- `400` invalid ULID
- `404` registry entry not found

---

## **4.2 GET /v1/registry/{registry_id}/proof**

**Purpose**  
Return the proof object (latest version) as defined in RFC0003.

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

**Error Cases**

- `404` entry not found
- `410` entry revoked

If the entry is revoked, the proof endpoint MUST NOT return the last known proof.

---

## **4.3 GET /v1/registry/{registry_id}/events**

**Purpose**  
Return lifecycle events matched against `feed.json`.

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

Events MUST be:

- strictly chronological
- identical to their representation in the global feed
- immutable

---

## **4.4 GET /v1/feed**

**Purpose**  
Expose the **canonical global append-only event feed**.

**Successful Response (200)**

```json
{
  "cnaus_feed_version": "1.0.0",
  "generated_at": "RFC3339",
  "events": [ ... ]
}
```

Rules:

- MUST include all create/update/revoke events
- MUST be append-only
- MUST reflect Root Authority state
- MUST be deterministic across mirrors

---

## **4.5 GET /v1/version**

**Purpose**  
Expose version declarations for all relevant CNAUS components.

**Response (200)**

```json
{
  "cnaus_api_version": "1.0.0",
  "registry_spec_version": "1.0.0",
  "proof_layer_version": "1.0.0",
  "governance_version": "1.0.0"
}
```

The API MUST return versions consistent with the SSOT.

---

## **4.6 POST /v1/validate/hash**

**Purpose**  
Validate a client-supplied hash against the registry entry.

**Request Schema**

```json
{
  "registry_id": "ulid",
  "hash": "sha256 hex"
}
```

**Response (200 – valid)**

```json
{
  "valid": true,
  "reason": "hash matches canonical artifact",
  "registry_id": "ulid",
  "version": "string"
}
```

**Response (200 – invalid)**

```json
{
  "valid": false,
  "reason": "hash does not match canonical artifact",
  "registry_id": "ulid",
  "version": "string"
}
```

**Error Cases**

- `400` malformed request
- `404` registry entry not found

Validation MUST be stateless.

---

# **5. Security Requirements**

1. Endpoints MUST be served over HTTPS (TLS 1.2+).
2. Responses MUST NOT contain personal data.
3. Feed MUST be cacheable but immutable.
4. Rate limits SHOULD protect against abuse.
5. Root Authority cryptographic material MUST NOT be exposed.

---

# **6. Compliance Requirements**

A client is compliant if it:

- retrieves registry entries using this RFC
- validates proofs according to RFC0003
- respects lifecycle constraints in RFC0001
- inspects and obeys revocation events
- respects version boundaries
- rejects inconsistent hashes or malformed entries    

---

# **7. Non-Normative Extensions**

These MAY be added without violating the standard:

- `/v1/mirror` endpoint
- compressed feeds
- signed API responses
- enterprise-optimized access patterns    

These are NOT part of the core standard and MUST NOT appear in the normative sections.

---

# **8. References**

- RFC0001 — Registry Framework
- RFC0003 — Proof Layer
- VERSIONING.md
- GOVERNANCE.md
- LICENSE.md