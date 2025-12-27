---
title: CNAUS Versioning Policy
document_id: CNAUS-VERSIONING
status: Normative
version: 1.0.0
conformance_scope: Core
authority: CNAUS Root Authority
---
# CNAUS Registry Core Standard — Versioning Policy  
version: 1.0.0  
status: Normative  
document_id: VERSIONING  
document_class: Root Standard – Layer 1  
issued: 2025-12-11  
updated: 2025-12-11  
authority: CNAUS Root Authority  
dependencies: RFC0001, RFC0002, RFC0003, GOVERNANCE.md, feed.json  
references: RFC0001, RFC0002, RFC0003, GOVERNANCE.md  

---

## 1. Purpose

This document defines the **normative versioning, release, and change-management policy**  
governing all components of the **CNAUS Registry Core Standard**.

It ensures:

- stability  
- predictability  
- forward compatibility  
- auditability via the canonical feed  
- conformance across all implementations  

This specification is **normative**.

---

## 2. Semantic Versioning Model

CNAUS uses a **strict semantic versioning scheme**:

```

MAJOR.MINOR.PATCH

```

### MAJOR  
Breaking changes to **normative rules**, **canonical data models**, **proof semantics**,  
or **API invariants**.  
Implementations **MUST** update accordingly.

### MINOR  
Additive, backward-compatible enhancements.  
No existing proofs, registry entries, or feed events may be invalidated.

### PATCH  
Editorial corrections, clarifications, corrections of non-normative text.  
No implementation changes required.

**Examples**  
- `1.2.0` = backward-compatible extension  
- `2.0.0` = introduction of a new mandatory requirement  

---

## 3. Release Classifications

### Draft  
- Work-in-progress  
- Not authoritative  
- Not intended for public conformance  

### Version B (Public Release)  
- Canonical, authoritative release  
- Must comply with governance and feed requirements  

### LTS (Long-Term Stable)  
- For regulators, enterprises, and large deployments  
- MUST remain stable for a defined lifecycle under GOVERNANCE.md  

---

## 4. Change Control (Normative)

All normative changes **MUST**:

1. be proposed through the CNAUS Governance Council,  
2. document rationale, scope, and compatibility impact,  
3. undergo version assessment per SemVer rules,  
4. be recorded as **root events** in `feed.json`,  
5. include timestamps, version numbers, and the associated diff scope,  
6. be tagged in the repository at the time of release.

Patch updates **MAY** bypass full review if strictly editorial.

---

## 5. Compatibility Requirements

Implementations:

- **MUST** support all normative rules of the active **MAJOR** version,  
- **SHOULD** migrate to the latest **MINOR** version within reasonable operational windows,  
- **MAY** apply PATCH updates without operational modifications.

### Backward Compatibility Rules

- MINOR and PATCH updates **MUST NOT** invalidate existing registry entries, proofs, or feed events.  
- MAJOR updates **MAY** introduce new required fields or processing rules.

### Forward Compatibility

Implementations **SHOULD** ignore unknown MINOR-version fields  
as long as canonical semantics remain intact.

---

## 6. Deprecation Policy

Deprecated fields or behaviors **MUST**:

1. be documented explicitly in the RFCs,  
2. be recorded in `feed.json` as a `update` event,  
3. remain functional for at least **one MINOR release**,  
4. include clear migration guidance.

Deprecated fields MUST NOT break validation.

---

## 7. Release Publication (Normative)

Every normative release **MUST** be published simultaneously via:

1. **GitHub tag** (authoritative SSOT)  
2. **root-level version reference in VERSIONING.md**  
3. **corresponding canonical event in feed.json**  

Feed entries MUST include:

- event_type = "update"  
- updated version  
- prev_hash linkage  
- timestamp  
- change summary  

Releases without feed anchoring are **invalid**.

---

## 8. Binding to Root Authority

Version declarations **MUST** be issued only by the CNAUS Root Authority.

No delegated authority MAY publish normative versions unless explicitly ratified.

Implementations MUST reject any version not represented in the canonical feed.

---

## 9. References  
(Informative unless explicitly marked normative in other RFCs)

- RFC0001 — Registry Framework  
- RFC0002 — API Specification  
- RFC0003 — Proof Layer  
- GOVERNANCE.md  
- feed.json  
