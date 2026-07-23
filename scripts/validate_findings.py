#!/usr/bin/env python3
"""Validate SaaS audit findings against the repository JSON schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def fallback_validate(findings: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(findings, list):
        return ["Findings document must be a JSON array."]

    required = {
        "id",
        "title",
        "status",
        "domain",
        "severity",
        "priority",
        "environment",
        "description",
        "expected",
        "actual",
        "reproduction",
        "risk",
        "evidence",
        "remediation",
        "retest",
    }
    valid_severities = {"Critical", "High", "Medium", "Low", "Informational"}
    valid_priorities = {"P0", "P1", "P2", "P3", "P4"}

    for index, finding in enumerate(findings):
        prefix = f"finding[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = sorted(required - set(finding))
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
        if finding.get("severity") not in valid_severities:
            errors.append(f"{prefix}.severity is invalid")
        if finding.get("priority") not in valid_priorities:
            errors.append(f"{prefix}.priority is invalid")
        if not isinstance(finding.get("reproduction"), list) or not finding.get("reproduction"):
            errors.append(f"{prefix}.reproduction must be a non-empty array")
        if not isinstance(finding.get("evidence"), list) or not finding.get("evidence"):
            errors.append(f"{prefix}.evidence must be a non-empty array")
    return errors


def validate(findings_path: Path, schema_path: Path) -> list[str]:
    findings = load_json(findings_path)
    schema = load_json(schema_path)
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return fallback_validate(findings)

    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    for finding_index, finding in enumerate(findings if isinstance(findings, list) else [findings]):
        for error in sorted(validator.iter_errors(finding), key=lambda item: list(item.path)):
            path = ".".join(str(part) for part in error.path)
            location = f"finding[{finding_index}]"
            if path:
                location += f".{path}"
            errors.append(f"{location}: {error.message}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("findings", type=Path, help="Findings JSON array")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "finding.schema.json",
        help="Finding schema path",
    )
    args = parser.parse_args()

    try:
        errors = validate(args.findings, args.schema)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {args.findings}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
