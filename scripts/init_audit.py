#!/usr/bin/env python3
"""Create a safe, repeatable SaaS audit workspace."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-").lower()
    if not slug:
        raise ValueError("Application name must contain at least one letter or number.")
    return slug


def build_workspace(root: Path, app_name: str, environment: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    workspace = root / f"{slugify(app_name)}-{slugify(environment)}-{stamp}"

    folders = [
        "reports",
        "data",
        "evidence/discovery",
        "evidence/authentication",
        "evidence/rbac",
        "evidence/tenancy",
        "evidence/functional",
        "evidence/ui-ux",
        "evidence/accessibility",
        "evidence/security",
        "evidence/api",
        "evidence/database",
        "evidence/infrastructure",
        "evidence/performance",
        "evidence/privacy",
        "evidence/ai-llm",
        "logs",
        "working",
    ]
    for folder in folders:
        (workspace / folder).mkdir(parents=True, exist_ok=True)

    manifest = {
        "application": app_name,
        "environment": environment,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "INITIALIZED",
        "safety": {
            "destructive_tests": False,
            "production_changes": False,
            "test_data_prefix": "AUDIT_TEST_",
        },
        "artifacts": [],
    }
    (workspace / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    coverage = {
        "statuses": ["PASS", "FAIL", "BLOCKED", "NOT_TESTED", "NOT_APPLICABLE"],
        "domains": {},
    }
    (workspace / "data" / "coverage.json").write_text(
        json.dumps(coverage, indent=2) + "\n", encoding="utf-8"
    )
    (workspace / "data" / "findings.json").write_text("[]\n", encoding="utf-8")
    (workspace / "logs" / "execution-log.md").write_text(
        "# Audit Execution Log\n\nRecord commands, tools, versions, timestamps, results, limitations and evidence references.\n",
        encoding="utf-8",
    )
    return workspace


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("application", help="Application or product name")
    parser.add_argument("--environment", default="staging", help="Target environment")
    parser.add_argument("--output", default="saas-audit-output", help="Output root")
    args = parser.parse_args()

    try:
        workspace = build_workspace(Path(args.output).expanduser().resolve(), args.application, args.environment)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
        return 2

    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
