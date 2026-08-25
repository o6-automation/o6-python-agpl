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

"""Run the UAFX single-controller AutomationComponent acceptance gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from check_uafx_gate0 import validate  # noqa: E402


TESTS = (
    "tests/server/test_fx_runtime.py",
    "tests/server/test_fx_example.py",
)


def main() -> int:
    errors, _statuses = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *TESTS],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        return result.returncode
    print("Gate 1 passed: single-controller AutomationComponent behavior is ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
