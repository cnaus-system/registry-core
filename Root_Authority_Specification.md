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

---

## 2. Definition of the Root Authority

The Root Authority is defined as:

- the **sole issuer** of canonical registry entries,
- the **sole issuer** of canonical proofs,
- the **sole publisher** of the canonical global feed (`feed.json`),
- the **sole publisher** of the canonical normative document set for a given released version,
- the **sole operator** permitted to execute and publish revocation events.

No other entity MAY perform these actions.

Normative changes to the standard MUST be approved via the Governance Framework.
The Root Authority executes and publishes approved changes as canonical artifacts.

Delegation, mirroring, caching, or replication MAY occur,  
but MUST NOT alter authority or authorship.

---

## 3. Operational Requirements (Normative)

The Root Authority MUST operate under strict controls:

### 3.1 Exclusive Capabilities (MUST NOT be delegated)

1. Create registry entries  
2. Update registry entries  
3. Revoke registry entries  
4. Generate canonical proofs (RFC0003)  
5. Sign and publish new standard versions  
6. Generate and publish the global feed  
7. Publish the canonical normative document set for each released version (RFC0001, RFC0002, RFC0003, Feed, Revocation, Root Authority, Versioning, Governance), following Governance approval  

### 3.2 Delegable (read-only) Capabilities

These MAY be delegated:

- read-only API mirrors  
- caching of feed snapshots  
- distribution of proofs  
- replication of released documents

Delegation MUST NOT create ambiguity about canonical authority.

---

## 4. Release Authority (Normative)

A CNAUS release is authoritative only if:

- it is tagged and published by the Root Authority,  
- it is anchored in the canonical feed via a standard event,  
- it follows Governance approval procedures,  
- it complies with SemVer rules.

---

## 5. Revocation Authority (Normative)

Only the Root Authority MAY publish revocation events in the canonical feed.

Council authorization policy for revocation is defined in the Governance Framework.

---

## 6. Integrity and Immutability (Normative)

The Root Authority MUST:

- preserve immutability of prior releases,  
- ensure feed integrity via hash-linked ordering (`prev_hash`),  
- prevent retroactive mutation of events or documents,  
- provide deterministic artifact hashes for released content.

---

## 7. References

- GOVERNANCE.md
- VERSIONING.md
- Feed Specification
- Revocation Specification
- RFC0001
- RFC0002
- RFC0003
