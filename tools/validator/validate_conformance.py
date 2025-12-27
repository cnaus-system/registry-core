#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Conformance" / "manifest.json"
VECTORS_DIR = ROOT / "Conformance" / "vectors"

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

    # Basic structural validations only (Non-Core runner).
    for v in vectors:
        vid = v.get("id")
        name = v.get("name")
        input_path = v.get("input_path")
        expected = v.get("expected")

        if not vid or not name or not input_path or not expected:
            fail(f"vector missing required fields: {v}")

        if expected.get("result") not in {"pass", "fail"}:
            fail(f"{vid}: expected.result must be pass|fail")

        p = (ROOT / "Conformance" / input_path).resolve()
        if not p.exists():
            fail(f"{vid}: input file missing: {p}")

        _ = load_json(p)  # ensure parseable JSON

        ok(f"{vid}: loaded {p.name}")

    ok("all vectors loaded and JSON-parseable")
    print("PASS")

if __name__ == "__main__":
    main()
