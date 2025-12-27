# CNAUS Feed Specification
Version: 1.0.0
Status: Normative
Layer: Layer 1 – Core Standard

## 1. Purpose

This document defines the canonical format and processing rules for the CNAUS
global event feed (`feed.json`).

The feed is the authoritative, append-only record of:

- registry lifecycle events (`create`, `update`, `revoke`),
- proof bindings (via `proof_hash` in lifecycle events),
- CNAUS standard publication events (`standard.initial_public_release`, `standard.version_update`),
- revocation semantics binding (see Revocation Specification).

All CNAUS implementations that claim conformance with CNAUS v1.0.0 MUST follow
this specification.

## 2. Conventions

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
are to be interpreted as described in RFC 2119.

Timestamps MUST be RFC 3339 / ISO-8601 `date-time` in UTC (`Z` suffix).

Hash algorithm identifiers in this version are fixed to `SHA-256`.

## 3. Top-Level Feed Object (Normative)

`feed.json` MUST be a JSON object with exactly these keys:

- `version` (string): the CNAUS feed schema version (for v1.0.0: `"1.0.0"`)
- `feed_generated_at` (string): RFC3339 timestamp when this feed snapshot was generated
- `events` (array): ordered list of feed event objects

No other top-level keys are permitted.

### 3.1 Ordering

`events` MUST be ordered from oldest to newest (chronological).

## 4. Feed Event Object (Normative)

Each element of `events` MUST be a JSON object with exactly these keys:

- `event_id` (string): ULID (26 chars, Crockford Base32)
- `event_type` (string): one of the allowed event types (Section 5)
- `registry_id` (string or null): ULID of the affected registry entry; MUST be null for standard events
- `version` (string or null): registry entry version (SemVer) for registry events; MUST be null for standard events
- `proof_hash` (string or null): SHA-256 hex (64 chars) for registry events that bind a proof; MUST be null for standard events
- `timestamp` (string): RFC3339 timestamp of the event (authority-issued)
- `prev_hash` (string or null): SHA-256 hex of the previous event object (Section 6); MUST be null for the first event
- `details` (object or null): event-type specific additional data (Section 7)

No other keys are permitted at the event object level.

## 5. Event Types (Normative)

Only the following `event_type` values are permitted:

### 5.1 Registry lifecycle events

- `create`
- `update`
- `revoke`

For `create|update|revoke`:

- `registry_id` MUST be a ULID.
- `version` MUST be a SemVer string (`MAJOR.MINOR.PATCH`).
- `proof_hash`:
  - MUST be a SHA-256 hex string for `create` and `update` events where a proof is bound.
  - MUST be a SHA-256 hex string for `revoke` events to denote the terminal proof boundary (see Revocation Specification).
- `details` MAY be null or an object.

### 5.2 Standard events

- `standard.initial_public_release`
- `standard.version_update`

For standard events:

- `registry_id` MUST be null.
- `version` MUST be null.
- `proof_hash` MUST be null.
- `details` MUST be an object (not null).

Custom event types MUST NOT be used.

## 6. Hash Chain (`prev_hash`) (Normative)

The feed MUST be tamper-evident via `prev_hash`.

### 6.1 Canonical JSON for hashing

For `prev_hash` calculation, an event object MUST be serialized to canonical JSON as:

- UTF-8 encoding
- JSON object keys sorted lexicographically
- no insignificant whitespace
- arrays preserved in order
- strings preserved exactly as in the event object
- no trailing newline

### 6.2 Calculation

For event `events[i]`:

- If `i == 0`: `prev_hash` MUST be null.
- If `i > 0`: `prev_hash` MUST equal `SHA256(canonical_json(events[i-1]))`.

Validators MUST verify the chain for the entire feed snapshot. Any mismatch is a fatal error and the feed MUST be rejected.

## 7. `details` Object Rules (Normative)

At the event-object level, `details` is the only extensibility point.

- If `details` is an object, its internal keys are event-type specific and MAY evolve.
- Consumers MUST NOT reject a feed solely due to unknown keys *inside* `details`.
- Consumers MUST reject unknown keys at the top-level feed object and at the event object level.

### 7.1 `details` for `standard.initial_public_release`

`details` MUST contain:

- `standard_name` (string)
- `standard_version` (string, SemVer)
- `release_date` (string, RFC3339)
- `tag` (string)
- `assets` (array) where each item MUST contain:
  - `path` (string)
  - `sha256` (string, 64 hex)

### 7.2 `details` for `standard.version_update`

`details` MUST contain:

- `standard_name` (string)
- `from_version` (string, SemVer)
- `to_version` (string, SemVer)
- `effective_date` (string, RFC3339)
- `tag` (string)
- `assets` (array) as in Section 7.1

## 8. Validation Rules (Normative)

A conformant validator MUST:

1. Enforce the schema rules in Sections 3–7 (including “no extra keys”).
2. Verify `prev_hash` chain (Section 6).
3. Enforce event-type rules (Section 5).
4. For registry events, enforce `proof_hash` binding semantics as required by RFC0003 and Revocation Specification.
5. Treat any mutation of historical events as a fatal integrity failure.

Mirrors MAY cache or replicate `feed.json` but MUST NOT modify events.

## 9. Security Considerations (Normative)

- `feed.json` is authoritative only when published by the CNAUS Root Authority (see Root Authority Specification).
- Validators MUST assume adversarial modification attempts and MUST enforce `prev_hash` integrity.
- Implementations SHOULD pin accepted hash algorithms to `SHA-256` for v1.0.0.
- Time synchronization SHOULD rely on reliable NTP/PTP sources.

## 10. References

- RFC0001 — Registry Framework
- RFC0002 — API Specification
- RFC0003 — Proof Layer
- Root Authority Specification
- Revocation Specification
- VERSIONING.md
- GOVERNANCE.md