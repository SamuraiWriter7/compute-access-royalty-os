#!/usr/bin/env python3
"""
Validate example YAML files against their corresponding JSON Schemas.
"""

from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

# Correct __file__ usage
ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Compute Access Right",
        "schema": ROOT / "schemas" / "compute-access-right.schema.json",
        "example": ROOT / "examples" / "compute-access-right.example.yaml",
    },
    {
        "name": "Contribution to Access Policy",
        "schema": ROOT / "schemas" / "contribution-to-access-policy.schema.json",
        "example": ROOT / "examples" / "contribution-to-access-policy.example.yaml",
    },
    {
        "name": "Multi-Wing Compute Pool",
        "schema": ROOT / "schemas" / "multi-wing-compute-pool.schema.json",
        "example": ROOT / "examples" / "multi-wing-compute-pool.example.yaml",
    },
]

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def format_error_path(error) -> str:
    if not error.absolute_path:
        return "<root>"
    return ".".join(str(part) for part in error.absolute_path)

def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        print(f"[error] {name} validation failed")
        for error in errors:
            print(f"  - path: {format_error_path(error)}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {name} example is valid")
    return True

def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_valid = all_valid and is_valid

    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())

