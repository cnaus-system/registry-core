# CNAUS PoC — Minimal Proof of Concept (Layer-1)

Status: PoC Definition  
Scope: Registry Core, Proof Layer, Feed (read-only)  
Audience: Pilot partners, auditors, regulators

## 1. Purpose
This PoC demonstrates the minimal, verifiable operation of the CNAUS
Registry Core Standard without introducing new semantics.

It proves:
- deterministic registration,
- cryptographic proof binding,
- feed-anchored lifecycle transparency,
- offline verifiability.

## 2. Scope (Strict)
Included:
- Registry entry creation (Root Authority only)
- Proof generation and binding
- Public verification
- Public feed consumption

Excluded:
- UI, dashboards
- Authentication flows
- SDKs or client libraries
- Payments or monetization
- Delegated authorities

## 3. PoC Functions

### 3.1 Register (Authority)
Input:
- canonical artifact
- metadata (non-PII)

Process:
- canonicalize artifact (RFC0003)
- compute SHA-256 hash
- create registry entry (RFC0001)
- emit feed event

Output:
- registry_id
- version
- proof_hash

### 3.2 Verify (Public)
Input:
- registry_id
- artifact hash

Process:
- retrieve registry entry
- recompute hash
- validate proof
- validate feed consistency

Output:
- valid: true | false
- reason

### 3.3 Feed (Public)
- exposes canonical `feed.json`
- append-only
- identical across mirrors

## 4. Success Criteria
The PoC is successful if:
- verification is deterministic,
- revoked entries fail verification,
- feed events are consistent,
- no private data is present.

## 5. Non-Goals
The PoC does not attempt to:
- scale performance,
- provide UX,
- integrate external systems.

Signed,
CNAUS Root Authority
