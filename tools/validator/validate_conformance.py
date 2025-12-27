#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Conformance" / "manifest.json"

def fail(msg: str, code: int = 1):
    print(f"FAIL: {msg}")
    sys.exit(code)

def ok(msg: str):
    print(f"OK: {msg}")

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"cannot load JSON: {path} ({e})")

def _type_ok(expected, data):
    if isinstance(expected, list):
        return any(_type_ok(t, data) for t in expected)
    if expected == "object":
        return isinstance(data, dict)
    if expected == "array":
        return isinstance(data, list)
    if expected == "string":
        return isinstance(data, str)
    if expected == "integer":
        return isinstance(data, int) and not isinstance(data, bool)
    if expected == "number":
        return (isinstance(data, (int, float)) and not isinstance(data, bool))
    if expected == "boolean":
        return isinstance(data, bool)
    if expected == "null":
        return data is None
    return True  # unknown types: ignore

def validate_schema(schema, data, path="$"):
    errors=[]

    if "enum" in schema and data not in schema["enum"]:
        errors.append(f"{path}: value not in enum")

    if "const" in schema and data != schema["const"]:
        errors.append(f"{path}: value != const")

    if "type" in schema and not _type_ok(schema["type"], data):
        errors.append(f"{path}: type mismatch (expected {schema['type']})")
        return errors  # cannot descend reliably

    t = schema.get("type")

    if t == "object" and isinstance(data, dict):
        req = schema.get("required", [])
        for k in req:
            if k not in data:
                errors.append(f"{path}.{k}: missing required property")

        props = schema.get("properties", {})
        for k, subschema in props.items():
            if k in data:
                errors.extend(validate_schema(subschema, data[k], f"{path}.{k}"))

    if t == "array" and isinstance(data, list):
        if "minItems" in schema and len(data) < int(schema["minItems"]):
            errors.append(f"{path}: minItems violated")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for i, item in enumerate(data):
                errors.extend(validate_schema(item_schema, item, f"{path}[{i}]"))

    return errors

def main():
    if not MANIFEST.exists():
        fail(f"manifest missing: {MANIFEST}")

    manifest = load_json(MANIFEST)

    if manifest.get("manifest_version") != "1.0":
        fail("manifest_version must be 1.0")

    vectors = manifest.get("vectors")
    if not isinstance(vectors, list) or len(vectors) == 0:
        fail("manifest.vectors must be a non-empty list")

    ok(f"manifest loaded ({len(vectors)} vectors)")

    for v in vectors:
        vid = v.get("id")
        name = v.get("name")
        input_path = v.get("input_path")
        expected = v.get("expected")
        schema_path = v.get("schema_path")

        if not vid or not name or not input_path or not expected:
            fail(f"vector missing required fields: {v}")

        expected_result = expected.get("result")
        if expected_result not in {"pass", "fail"}:
            fail(f"{vid}: expected.result must be pass|fail")

        input_file = (ROOT / "Conformance" / input_path).resolve()
        if not input_file.exists():
            fail(f"{vid}: input file missing: {input_file}")

        data = load_json(input_file)

        passed = True
        if schema_path:
            schema_file = (ROOT / schema_path).resolve()
            if not schema_file.exists():
                fail(f"{vid}: schema missing: {schema_file}")
            schema = load_json(schema_file)
            errs = validate_schema(schema, data, "$")
            passed = (len(errs) == 0)
        else:
            # baseline: must be JSON object
            passed = isinstance(data, dict)

        if expected_result == "pass" and not passed:
            fail(f"{vid}: expected PASS but got FAIL")
        if expected_result == "fail" and passed:
            fail(f"{vid}: expected FAIL but got PASS")

        ok(f"{vid}: expected {expected_result.upper()} matched")

    ok("all vectors validated (schema-aware where provided)")
    print("PASS")

if __name__ == "__main__":
    main()
