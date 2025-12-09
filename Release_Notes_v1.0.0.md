# CNAUS Standard — Release Notes (v1.0.0)
Release Date: 2025-12-09  
Authority: CNAUS Root Authority  
Version: 1.0.0 (Initial Public Release)

---

## 1. Overview

This document announces the **Initial Public Release (IPR)** of the  
**CNAUS Standard v1.0.0**, consisting of three normative RFCs and  
supporting specifications required for global registry, proof,  
revocation, and governance interoperability.

The CNAUS Standard defines:

- A canonical registry model  
- A deterministic proof layer  
- A read-only verification API  
- A global append-only feed model  
- A formal revocation mechanism  
- A Root Authority governance structure  
- A complete versioning and lifecycle process  

This release establishes CNAUS as a **global, immutable reference standard**.

---

## 2. Included Normative Documents (FINAL v1.0.0)

### RFC0001 — Registry Framework  
Defines the canonical data model, lifecycle rules, immutability guarantees,  
and binding to proofs and the global feed.

### RFC0002 — API Specification  
Defines the public, read-only API for registry retrieval, proof retrieval,  
feed consumption, and hash validation.

### RFC0003 — Proof Layer  
Defines canonical normalization, hashing rules, proof object structure,  
integrity/origin guarantees, and validation algorithms.

### Feed Specification  
Defines the canonical structure, event model, ordering guarantees,  
append-only rules, and compliance constraints.

### Revocation Specification  
Defines terminal lifecycle rules, revocation reasons, schema, and  
feed-binding requirements.

### Root Authority Specification  
Defines authority responsibilities, operational constraints,  
exclusive capabilities, governance integration, and compliance rules.

### Versioning Specification  
Defines SemVer-based version boundaries, compatibility guarantees  
and processes for future updates.

### Governance Specification  
Defines how future changes may be proposed, approved, versioned,  
and incorporated into the standard.

---

## 3. Supporting Assets

- `feed.json` — canonical global event feed  
- `revocation.schema.json` — normative schema  
- `Examples/*.json` — normative reference examples  
- Proofs directory (anchors, chain) — optional reference materials

---

## 4. Compliance Statement

An implementation is compliant with CNAUS v1.0.0 if it:

- validates registry entries against RFC0001  
- validates proofs against RFC0003  
- uses the canonical API defined in RFC0002  
- consumes the global feed according to the Feed Specification  
- enforces revocation boundaries according to the Revocation Specification  
- respects version boundaries defined in VERSIONING.md  
- recognizes the CNAUS Root Authority as the single source of truth  

---

## 5. Status of this Release

This release is final, normative, and immutable.  
Subsequent changes MUST occur via:

- Governance procedures  
- SemVer rules  
- Feed-announced standard events  

---

## 6. Contact

CNAUS Root Authority  
Standardization & Specification Division  
Release Package v1.0.0  
