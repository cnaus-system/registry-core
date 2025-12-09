# CNAUS Registry Core Standard – Versioning Policy  
Version B (Public Release)

## 1. Purpose
This document defines the versioning, release, and change-management policy for
the CNAUS Registry Core Standard. It ensures stability, predictability, and
interoperability across all conformant implementations.

## 2. Semantic Versioning
The CNAUS Registry Core uses a modified semantic versioning scheme:

MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes to normative rules, data models, or proof
  semantics. Implementations MUST update accordingly.
- **MINOR**: Additive, backward-compatible enhancements to the standard.
- **PATCH**: Editorial changes, clarifications, and non-normative corrections.

Example:  
`1.2.0` → Minor extension with backward compatibility  
`2.0.0` → Introduction of a new mandatory constraint or normative rule  

## 3. Release Types
The standard recognizes the following release classifications:

- **Draft**: Work-in-progress, not for public conformance.  
- **Version B**: Public authoritative release.  
- **LTS**: Long-term stable version, recommended for regulators and large institutions.  

## 4. Change Control
All normative changes MUST:

1. be proposed through the CNAUS Governance Council;  
2. document rationale, scope, and compatibility impact;  
3. be assigned a version increment according to the SemVer rules;  
4. be recorded in `feed.json` and marked with timestamps.

## 5. Compatibility Requirements
Implementations:

- MUST support all normative definitions of the current MAJOR version;  
- SHOULD migrate to the newest MINOR version within a reasonable timeframe;  
- MAY apply PATCH updates without operational impact.

Backward compatibility rules:

- A MINOR or PATCH update MUST NOT invalidate existing proofs, assets, or
  anchors.  
- MAJOR updates MAY introduce new mandatory fields or processing rules.

## 6. Deprecation Policy
Deprecated fields or behaviors MUST:

- be documented in the RFCs and the feed,  
- remain functional for at least one MINOR release,  
- provide clear migration guidance.

## 7. Release Publication
Every release MUST be published simultaneously through:

- GitHub repository tag  
- root-level version reference in this file  
- corresponding entries in `feed.json`

## 8. References
This policy is binding for:

- RFC0001 Registry Framework  
- RFC0002 API Specification  
- RFC0003 Proof Layer  
- GOVERNANCE.md  
