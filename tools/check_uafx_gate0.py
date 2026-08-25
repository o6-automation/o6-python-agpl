#!/usr/bin/env python3
# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Validate the frozen UAFX C2C Gate 0 baseline and claim definition."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "dev_docs/uafx_c2c_profile.json"
MATRIX_PATH = ROOT / "dev_docs/uafx_c2c_conformance_matrix.csv"
ALLOWED_STATUS = {"implemented", "partial", "missing", "external", "not_selected"}
EXPECTED_SPECIFICATIONS = {
    "OPC 10000-80": "1.00.03",
    "OPC 10000-81": "1.00.04",
    "OPC 10000-82": "1.00.03",
    "OPC 10000-83": "1.00.03",
    "OPC 10000-84": "1.00.04",
}


def _bool(value: str, field: str, row_id: str, errors: list[str]) -> bool:
    if value not in {"true", "false"}:
        errors.append(f"{row_id}: {field} must be true or false")
    return value == "true"


def _model_metadata(path: Path) -> tuple[str, str, str]:
    root = ET.parse(path).getroot()
    models = next(child for child in root if child.tag.endswith("Models"))
    model = next(child for child in models if child.tag.endswith("Model"))
    return (
        model.attrib["ModelUri"],
        model.attrib["Version"],
        model.attrib["PublicationDate"],
    )


def validate(require_ready: bool = False) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    if manifest.get("schema_version") != 1:
        errors.append("manifest schema_version must be 1")
    claim = manifest.get("claim", {})
    if claim.get("profile") != "UAFX Controller 2024 Profile":
        errors.append("claim profile must be UAFX Controller 2024 Profile")
    if claim.get("status") != "target_not_claimed":
        errors.append("Gate 0 must not assert conformance; status must be target_not_claimed")

    actual_specs = {item["part"]: item["revision"] for item in manifest["specifications"]}
    if actual_specs != EXPECTED_SPECIFICATIONS:
        errors.append(f"specification BOM differs from {EXPECTED_SPECIFICATIONS}")

    source = manifest["nodeset_source"]
    try:
        head = subprocess.run(
            ["git", "-C", str(ROOT / "deps/UA-Nodeset"), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        if head != source["commit"]:
            errors.append(f"UA-Nodeset HEAD {head} differs from manifest {source['commit']}")
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"cannot verify UA-Nodeset commit: {exc}")

    for model in source["models"]:
        path = ROOT / model["path"]
        if not path.is_file():
            errors.append(f"{model['shortname']}: missing {model['path']}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != model["sha256"]:
            errors.append(f"{model['shortname']}: SHA-256 differs from manifest")
        metadata = _model_metadata(path)
        expected = (model["uri"], model["version"], model["publication_date"])
        if metadata != expected:
            errors.append(f"{model['shortname']}: model metadata {metadata} differs from {expected}")

    with MATRIX_PATH.open(newline="", encoding="utf-8") as matrix_file:
        rows = list(csv.DictReader(matrix_file))
    row_ids = [row["id"] for row in rows]
    duplicates = sorted(item for item, count in Counter(row_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate matrix ids: {', '.join(duplicates)}")
    by_id = {row["id"]: row for row in rows}

    required_ids = {
        item["id"] for item in manifest["mandatory_included_profiles"]
    } | {
        item["id"] for item in manifest["mandatory_direct_conformance_units"]
    } | {
        item["id"] for item in manifest["optional_selections"]
    }
    missing_rows = sorted(required_ids - by_id.keys())
    if missing_rows:
        errors.append(f"manifest entries missing from matrix: {', '.join(missing_rows)}")

    for row in rows:
        row_id = row["id"]
        mandatory = _bool(row["mandatory"], "mandatory", row_id, errors)
        selected = _bool(row["selected"], "selected", row_id, errors)
        if row["status"] not in ALLOWED_STATUS:
            errors.append(f"{row_id}: unknown status {row['status']!r}")
        if mandatory and not selected:
            errors.append(f"{row_id}: a mandatory row cannot be unselected")
        if selected and row["status"] == "not_selected":
            errors.append(f"{row_id}: selected row is marked not_selected")
        if not selected and row["status"] != "not_selected":
            errors.append(f"{row_id}: unselected row must be marked not_selected")
        if selected and not row["owner"]:
            errors.append(f"{row_id}: selected row has no owner")
        if not row["requirement_summary"]:
            errors.append(f"{row_id}: requirement_summary is empty")

    for option in manifest["optional_selections"]:
        row = by_id.get(option["id"])
        if row and _bool(row["selected"], "selected", row["id"], errors) != option["selected"]:
            errors.append(f"{row['id']}: manifest and matrix selections differ")

    if not manifest["functional_entity_decision"].get("required"):
        errors.append("FunctionalEntity must be explicitly required by the selected profile")
    selected_options = {
        item["id"] for item in manifest["optional_selections"] if item["selected"]
    }
    if not {"CU-FE-INPUT-DATA", "CU-FE-OUTPUT-DATA"}.issubset(selected_options):
        errors.append("the bidirectional C2C target must select FunctionalEntity InputData and OutputData")

    statuses = Counter(row["status"] for row in rows if row["selected"] == "true")
    if require_ready:
        unresolved = [
            row["id"]
            for row in rows
            if row["selected"] == "true" and row["status"] != "implemented"
        ]
        if unresolved:
            errors.append(
                "profile is not implementation-ready; unresolved selected rows: "
                + ", ".join(unresolved)
            )
    return errors, statuses


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-ready",
        action="store_true",
        help="also fail until every selected matrix row is implemented",
    )
    args = parser.parse_args()
    errors, statuses = validate(require_ready=args.require_ready)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    summary = ", ".join(f"{key}={statuses[key]}" for key in sorted(statuses))
    print(f"Gate 0 baseline valid ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
