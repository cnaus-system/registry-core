# CNAUS Feed Specification  
Version 1.0.0 (Normative)

## 1. Purpose

This document defines the canonical format and processing rules for the CNAUS
event feed (`feed.json`).  
The feed is the authoritative, append-only record of:

- registry lifecycle events,
- proof bindings,
- standard publication events,
- version updates governed by the Root Authority.

All compliant CNAUS implementations MUST follow this specification exactly.

---

## 2. Feed Structure

The feed is a JSON object containing global metadata and a chronological list of
events:

```json
{
  "version": "1.0.0",
  "feed_generated_at": "RFC3339 timestamp",
  "events": [ ... ]
}
````

### 2.1 Normative Field Schema (Root Object)

|Field|Type|Requirement|
|---|---|---|
|`version`|string (semver)|MUST match the CNAUS Registry Core Standard version.|
|`feed_generated_at`|string (RFC3339)|MUST reflect the time of feed generation.|
|`events`|array of EventObject|MUST contain all lifecycle events in chronological order.|

---

## 3. Event Object Specification (Normative)

Each entry in `events[]` MUST follow this structure:

```json
{
  "event_id": "ulid",
  "event_type": "string",
  "registry_id": "ulid or null",
  "version": "string (semver)",
  "proof_hash": "sha256 hex or null",
  "timestamp": "RFC3339",
  "details": "object or null"
}
```

### 3.1 Field-Level Schema

#### `event_id`

- **Type:** ULID
- **Requirement:** MUST be globally unique.

#### `event_type`

- **Type:** string
- **Allowed Values (enum):**
    - `"create"`
    - `"update"`
    - `"revoke"`
    - `"standard.initial_public_release"`
    - `"standard.version_update"`
- **Rule:** Custom event types MUST NOT be introduced.    

#### `registry_id`

- **Type:** ULID or `null`
- **Rule:**
    - MUST be `null` for standard events.
    - MUST be a ULID for registry events.

#### `version`

- **Type:** string (semver)
- **Rule:** MUST match the registry entry version for create/update/revoke events.
    - For standard events: MUST match the standard version referenced in the event.

#### `proof_hash`

- **Type:** string (SHA-256 hex)
- **Rule:**
    - MUST match the proof hash from the corresponding registry event (for create/update).
    - MUST be `null` for standard events.

#### `timestamp`

- **Type:** string (RFC3339)
- **Rule:**
    - MUST be strictly monotonic per `registry_id`.
    - MUST represent the authoritative timestamp issued by the Root Authority.

#### `details`

- **Type:** object or `null`
- **Rule:**
    - MAY contain metadata for standard events (e.g., list of updated RFCs).
    - MUST NOT contain personal data.

---

## 4. Ordering and Append-Only Rules

1. Events MUST be sorted in **strict chronological order**.
2. For each `registry_id`, timestamps MUST be **strictly monotonic**.
3. The feed MUST be **append-only**; historical entries MUST never be modified.
4. Removal or mutation of previously published events invalidates compliance.
5. Event IDs MUST be globally unique and MUST NOT be reused.

---

## 5. Proof and Hash Binding Rules

For registry-level events (`create`, `update`, `revoke`):

1. `proof_hash` MUST equal the SHA-256 hash produced by the Proof Layer.
2. The event MUST reflect the correct version for that change.
3. All events MUST correspond to valid registry operations defined in RFC0001.
4. Revocation events MUST carry the final authoritative version of the entry.

For standard-level events:

- `registry_id` MUST be `null`.
- `proof_hash` MUST be `null`.
- Additional metadata MAY be included in `details`.

---

## 6. Feed Consistency Requirements

A compliant feed MUST:

- contain all events from the beginning of system operation,
- reflect all registry operations exactly once,
- maintain internal consistency between timestamps, hashes, and versions,
- remain immutable over time.

Consumers MUST:

- reject feeds with missing events,
- reject feeds that violate monotonicity,
- reject feeds containing unknown fields or event types,
- reject feeds that contain malformed timestamps or hashes.

---

## 7. Compliance Criteria for Feed Consumers

A consumer is compliant if it:

1. Validates event ordering and timestamp monotonicity.
2. Verifies `proof_hash` values against proof objects in registry entries.
3. Enforces version boundaries from RFC0001 and RFC0003.
4. Rejects revoked proofs and superseded events.
5. Rejects feeds that violate constraints in this specification.
6. Treats `feed.json` as the **single source of truth** for lifecycle ordering.

---

## 8. Security Considerations

1. Only the CNAUS Root Authority MAY generate or publish the feed.
2. Feed generation SHOULD occur inside secured, auditable infrastructure.
3. Time synchronization SHOULD rely on reliable NTP/PTP sources.
4. Mirrors MUST NOT modify or reorder events; they may only cache the feed.
5. Validators MUST treat mutation of old events as a fatal error.

---

## 9. References

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- RFC0003 — Proof Layer
- VERSIONING.md
- GOVERNANCE.md    
- LICENSE.md
