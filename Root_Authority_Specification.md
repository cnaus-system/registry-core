# CNAUS Root Authority Specification (RAS)  
Version 1.0.0 (Normative)

---
## 1. Purpose

This specification defines the **formal role**, **responsibilities**,  
**operational constraints**, and **governance boundaries** of the  
**CNAUS Root Authority**.

The Root Authority is the **single controlling entity** responsible for:

- issuing registry entries,  
- generating proofs,  
- generating and publishing the global feed,  
- enforcing lifecycle transitions (create, update, revoke),  
- maintaining the integrity of the CNAUS standard,  
- publishing new standard versions,  
- ensuring global consistency and compliance.

All compliant CNAUS implementations MUST recognize the Root Authority as  
the unique and authoritative source of truth for registry data, proofs,  
feed events, and standard updates.

---

## 2. Definition of the Root Authority

The Root Authority is defined as:

- the **sole issuer** of registry entries,  
- the **sole issuer** of canonical proofs,  
- the **sole publisher** of `feed.json`,  
- the **sole maintainer** of CNAUS standard specifications,  
- the **sole operator** permitted to execute revocation events.

No other entity MAY perform these actions.

Delegation, mirroring, caching, or replication MAY occur,  
but MUST NOT alter authority or authorship.

---

## 3. Authorities and Controls

The Root Authority MUST operate under strict controls:

### 3.1 Exclusive Capabilities (MUST NOT be delegated)

1. Create registry entries  
2. Update registry entries  
3. Revoke registry entries  
4. Generate canonical proofs (RFC0003)  
5. Sign and publish new standard versions  
6. Generate and publish the global feed  
7. Maintain normative documents (RFC0001, RFC0002, RFC0003, Feed, Revocation, Versioning, Governance)  

### 3.2 Delegable (read-only) Capabilities

These MAY be delegated, but MUST NOT modify state:

- feed mirroring  
- data replication  
- cache hosting  
- public read-only interfaces  
- compliance validation tools

Delegates MUST NOT modify registry state.

---

## 4. Operational Requirements

### 4.1 Environment Requirements

The Root Authority MUST operate within:

- controlled infrastructure  
- audit-logged systems  
- secure cryptographic environments  
- stable time sources (NTP/PTP)

### 4.2 Determinism Requirements

The Root Authority MUST:

1. ensure deterministic proof generation,  
2. ensure canonical normalization is strictly applied,  
3. ensure feeds are append-only,  
4. ensure timestamps are RFC3339 and monotonic,  
5. ensure no state is modified retroactively.

### 4.3 Availability Requirements

The Root Authority SHOULD:

- maintain high availability for feed delivery,  
- maintain stability of endpoints defined in RFC0002,  
- ensure version compatibility across standard updates.

---

## 5. Key Material and Cryptographic Policy

### 5.1 Key Ownership

If cryptographic signatures are used in future versions:

- private keys MUST be held exclusively by the Root Authority,  
- keys MUST be stored in secure HSM or equivalent,  
- keys MUST NOT leave controlled systems,  
- key compromise MUST trigger immediate revocation events.

### 5.2 Signing Policy (Future-Oriented)

Future extensions MAY introduce:

- signature-layer for proofs,  
- signature-layer for feed.json,  
- signature-layer for RFC packages.

These MUST be backward compatible and MUST NOT break v1.0.0.

---

## 6. Governance Interaction

The Root Authority MUST comply with:

- GOVERNANCE.md  
- VERSIONING.md  
- Feed_Specification.md  
- Revocation_Specification.md  

Governance rules define:

- how standards are updated,  
- how changes are proposed,  
- how versioning boundaries apply (SemVer),  
- how revocations are documented,  
- how amendments become normative.

The Root Authority MUST NOT bypass Governance rules.

---

## 7. Responsibilities of the Root Authority

The Root Authority MUST:

1. Maintain and publish the CNAUS standard specifications.  
2. Ensure global consistency of registry state.  
3. Publish feed updates in strict chronological order.  
4. Ensure proofs are deterministic and reproducible.  
5. Maintain tamper-evident history.  
6. Prevent unauthorized modifications.  
7. Apply revocations only via the normative revocation process.  
8. Preserve long-term accessibility of registry information.  
9. Maintain audit logs for all state transitions.  
10. Ensure stability and continuity of the CNAUS standard.

---

## 8. Limitations of the Root Authority

The Root Authority MUST NOT:

- introduce non-standard APIs,  
- introduce non-standard fields,  
- modify historical feed entries,  
- modify historical registry entries,  
- generate proofs inconsistent with RFC0003,  
- create lifecycle actions outside the normative set  
  (`create`, `update`, `revoke`),  
- introduce new event types without updating the standard  
  (`standard.version_update` required).

Any violation immediately invalidates canonical CNAUS compliance.

---

## 9. Compliance Requirements

A system or client is compliant with the Root Authority Specification if it:

1. Treats the Root Authority as the exclusive source of state changes.  
2. Rejects any feed or registry data not issued by the Root Authority.  
3. Validates all lifecycle events according to RFC0001 and RFC0003.  
4. Validates feed correctness according to the Feed Specification.  
5. Rejects unauthorized signatures or alternate authority claims.  
6. Recognizes only the normative CNAUS standard versions published by the Root Authority.  

---

## 10. Security Considerations

1. Root Authority infrastructure SHOULD use strict access control.  
2. All lifecycle actions MUST be auditable.  
3. Compromise of Root Authority systems MUST trigger emergency revocation.  
4. Mirrored feeds MUST NOT be treated as authoritative unless verified.  
5. Time synchronization MUST be maintained to prevent timestamp drift.

---

## 11. References

- RFC0001 — Registry Framework  
- RFC0002 — API Specification  
- RFC0003 — Proof Layer  
- Feed_Specification.md  
- Revocation_Specification.md  
- VERSIONING.md  
- GOVERNANCE.md  
- LICENSE.md  

