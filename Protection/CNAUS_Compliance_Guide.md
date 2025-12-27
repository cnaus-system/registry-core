---
title: CNAUS Compliance Guide
status: Informative
conformance_scope: Non-Core
authority: CNAUS Root Authority
---
# CNAUS Compliance Guide

## 1. Purpose

This document defines the **mandatory compliance requirements** for all systems  
claiming CNAUS compatibility.

It ensures:

- alignment with Root Authority invariants  
- correct registry, proof, and feed semantics  
- prevention of misuse or silent divergence  
- consistent global interoperability  

This guide is normative.

---

## 2. Mandatory Compliance Criteria

A system may claim CNAUS compliance ONLY if all of the following are met:

### 2.1 Registry Compliance (RFC0001)
- Implements canonical registry data model  
- Enforces immutability and lifecycle rules  
- Rejects invalid or inconsistent entries  
- Enforces revocation finality  

### 2.2 Proof Compliance (RFC0003)
- Performs canonicalization (UTF-8, sorted JSON, cleaned whitespace)  
- Recomputes SHA-256 hashes  
- Validates proof timestamps  
- Confirms feed consistency  
- Rejects conflicting or unverifiable proofs  

### 2.3 Feed Compliance
- Consumes the canonical append-only feed  
- Enforces monotonic timestamps  
- Rejects tampered or missing events  
- Enforces prev_hash linkage for versioned updates  

### 2.4 Zero-PII Compliance
- No personal data MAY appear in registry fields, proof metadata, or feed entries  

### 2.5 Version Compliance
- Must track the latest MAJOR version  
- Should track the latest MINOR version  
- Must reject version regressions  

---

## 3. Forbidden Behaviors (Normative)

The following actions are strictly prohibited:

1. Forking the standard or representing altered semantics as CNAUS  
2. Non-canonical hashing or alternative proof formats  
3. Silent deviation from lifecycle rules  
4. Tampering with historical feed entries  
5. Generating unanchored registry entries  
6. Ignoring revocation boundaries  
7. Adding personal data to any canonical structure  

Violations MUST be treated as non-compliance.

---

## 4. Compliance Process

Conformant systems MUST:

1. Document their CNAUS integration  
2. Pass validator conformance tests  
3. Provide hash-matching evidence for registry operations  
4. Demonstrate correct revocation handling  
5. Track feed.json as the authoritative source  
6. Validator conformance tests MUST align with RFC0003 §9

---

## 5. Enforcement

Non-compliant systems MAY be:

- flagged by Root Authority  
- added to non-compliance notices in feed  
- subject to revocation events  
- denied permission to claim CNAUS compatibility
- enforcement actions SHOULD be recorded via feed.json

---

## 6. Status of This Document
Final, normative, hash-ready, included in CNAUS v1.1.0.
