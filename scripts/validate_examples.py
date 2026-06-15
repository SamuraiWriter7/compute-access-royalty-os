#!/usr/bin/env python3
"""
Auto-repair YAML examples to match their JSON Schemas.
This is the "structural immune system" for Royalty OS / Compute Access OS.

- Removes fields not allowed by schema
- Adds missing required fields
- Fixes type mismatches when possible
- Ensures example structure matches schema structure

This is v1.0: deterministic, conservative, schema-driven repair.
"""

from __future__ import annotations
from pathlib import Path
import json
import yaml
import sys
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(path: Path, data: dict):
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


# ------------------------------
# IMMUNE SYSTEM CORE
# ------------------------------

def repair_value(schema: dict, value: Any) -> Any:
    """Repair a value according to schema type."""
    t = schema.get("type")

    if t == "string":
        return str(value)

    if t == "integer":
        try:
            return int(value)
        except Exception:
            return 0

    if t == "number":
        try:
            return float(value)
        except Exception:
            return 0.0

    if t == "boolean":
        if isinstance(value, bool):
            return value
        if str(value).lower() in ("true", "1", "yes"):
            return True
        return False

    if t == "array":
        if not isinstance(value, list):
            return []
        item_schema = schema.get("items", {})
        return [repair_value(item_schema, v) for v in value]

    if t == "object":
        if not isinstance(value, dict):
            return {}
        return repair_object(schema, value)

    return value


def repair_object(schema: dict, obj: dict) -> dict:
    """Repair an object according to schema."""
    repaired = {}

    props = schema.get("properties", {})
    required = schema.get("required", [])

    # 1. Keep only allowed properties
    for key, val in obj.items():
        if key not in props:
            continue  # remove unknown field
        repaired[key] = repair_value(props[key], val)

    # 2. Add missing required fields
    for key in required:
        if key not in repaired:
            repaired[key] = repair_value(props.get(key, {}), None)

    return repaired


# ------------------------------
# PAIR DISCOVERY
# ------------------------------

def discover_pairs():
    schema_map = {}
    example_map = {}

    for s in SCHEMAS_DIR.glob("*.schema.json"):
        key = s.name.replace(".schema.json", "")
        schema_map[key] = s

    for e in EXAMPLES_DIR.glob("*.example.yaml"):
        key = e.name.replace(".example.yaml", "")
        example_map[key] = e

    pairs = []
    for key, schema_path in schema_map.items():
        if key in example_map:
            pairs.append((key, schema_path, example_map[key]))

    return pairs


# ------------------------------
# MAIN REPAIR LOOP
# ------------------------------

def repair_pair(key: str, schema_path: Path, example_path: Path):
    print(f"[repair] {key}")
    schema = load_json(schema_path)
    example = load_yaml(example_path)

    # Top-level schema is always object
    repaired = repair_object(schema, example)

    save_yaml(example_path, repaired)
    print(f"[ok] repaired → {example_path.relative_to(ROOT)}")


def main():
    pairs = discover_pairs()
    if not pairs:
        print("[warn] no schema/example pairs found")
        return 1

    for key, schema_path, example_path in pairs:
        repair_pair(key, schema_path, example_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
