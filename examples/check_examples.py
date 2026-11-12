#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""
Run each example script and verify it printed the expected banner.

Every example is described by an :class:`~examples.manifest.ExampleSpec` in
``examples/manifest.py``.  Each group uses its own port. Finite examples must exit successfully with
the expected output; long-running examples stop after verified readiness.
Dependency readiness checks the child process owns the listening socket.
Logs from both processes are retained in a temporary directory.

Run from the repository root::

    .venv/bin/python3 examples/check_examples.py
"""

from __future__ import annotations

import os
import signal
import socket
import subprocess
import sys
import tempfile
from contextlib import ExitStack

import time
from pathlib import Path

import psutil

# This file is run as a script (``python examples/check_examples.py``), so
# ``sys.path[0]`` is ``examples/``.  A stale ``examples`` package may also
# exist in site-packages; make sure the repo tree wins before importing.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from examples.manifest import ALL_EXAMPLES, ExampleSpec, script_path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# Pick the interpreter that has the ``o6`` package installed.  The repo
# ships a venv at ``.venv/``; fall back to whatever ``sys.executable``
# points at if it isn't there.
_VENV_PY = REPO_ROOT / ".venv" / "bin" / "python"
PYTHON = str(_VENV_PY if _VENV_PY.is_file() else Path(sys.executable))

# Examples are launched as scripts, not with ``-m``, so cwd is never added
# to their sys.path. Prepend the repo root via PYTHONPATH so the same stale
# site-packages ``examples`` package this file guards against above can't
# shadow the live repo tree inside the subprocess either.
_SUBPROCESS_ENV = dict(os.environ)
_existing_pythonpath = _SUBPROCESS_ENV.get("PYTHONPATH", "")
_SUBPROCESS_ENV["PYTHONPATH"] = (
    f"{REPO_ROOT}{os.pathsep}{_existing_pythonpath}" if _existing_pythonpath else str(REPO_ROOT)
)


SERVER_HOST = "127.0.0.1"


def _free_port() -> int:
    with socket.socket() as listener:
        listener.bind((SERVER_HOST, 0))
        return listener.getsockname()[1]


def _owns_listener(proc: subprocess.Popen, port: int) -> bool:
    if proc.poll() is not None:
        return False
    try:
        return any(
            connection.status == psutil.CONN_LISTEN and connection.laddr.port == port
            for connection in psutil.Process(proc.pid).net_connections(kind="tcp")
        )
    except psutil.NoSuchProcess:
        return False


def _wait_for_server(
    proc: subprocess.Popen, port: int, log: Path, marker: str, deadline_s: float = 10.0
) -> bool:
    end = time.monotonic() + deadline_s
    while time.monotonic() < end:
        if proc.poll() is not None:
            return False
        if marker in log.read_text(errors="replace") and _owns_listener(proc, port):
            return proc.poll() is None
        time.sleep(0.05)
    return False


def _stop_server(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    try:
        proc.send_signal(signal.SIGINT)
    except ProcessLookupError:
        return
    try:
        proc.wait(timeout=5.0)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5.0)


def run_and_check(example_id: str, spec: ExampleSpec, log_dir: Path | None = None) -> bool:
    """Run an isolated example group and retain both processes' output."""
    if log_dir is None:
        log_dir = Path(tempfile.mkdtemp(prefix="o6-examples-"))
    log_dir.mkdir(parents=True, exist_ok=True)
    port = _free_port()
    env = {**_SUBPROCESS_ENV, "O6_EXAMPLE_PORT": str(port)}
    test = spec.test or {}
    expected = test.get("expected")
    marker = test.get("ready_marker", "").replace("4840", str(port))
    timeout = float(test["timeout"])
    log = log_dir / (example_id.replace("/", "_") + ".log")
    dependency_log = log.with_suffix(".dependency.log")
    dependency = None
    proc = None
    success = False

    def launch(entry_id: str, entry_spec: ExampleSpec, output):
        return subprocess.Popen(
            [PYTHON, "-u", str(script_path(entry_id, entry_spec))],
            stdin=subprocess.PIPE,
            stdout=output,
            stderr=subprocess.STDOUT,
            cwd=REPO_ROOT,
            env=env,
        )

    try:
        with ExitStack() as files:
            if spec.requires_server is not None:
                dependency_spec = ALL_EXAMPLES[spec.requires_server]
                dependency = launch(
                    spec.requires_server,
                    dependency_spec,
                    files.enter_context(dependency_log.open("w")),
                )
                dependency_marker = (dependency_spec.test or {}).get("ready_marker", "")
                if not _wait_for_server(
                    dependency, port, dependency_log, dependency_marker.replace("4840", str(port))
                ):
                    raise RuntimeError(
                        f"Dependency {spec.requires_server} did not become ready on port {port}"
                    )

            proc = launch(example_id, spec, files.enter_context(log.open("w")))
            deadline = time.monotonic() + timeout
            reached_marker = False
            while proc.poll() is None and time.monotonic() < deadline:
                if (
                    marker
                    and marker in log.read_text(errors="replace")
                    and (dependency is not None or _owns_listener(proc, port))
                ):
                    reached_marker = True
                    break
                time.sleep(0.05)
            interrupted = proc.poll() is None
            if interrupted:
                _stop_server(proc)
            output = log.read_text(errors="replace")
            if expected is not None:
                success = not interrupted and proc.returncode == 0 and expected in output
            else:
                success = reached_marker and (
                    proc.returncode == 0
                    or (reached_marker and proc.returncode in (-signal.SIGINT, 130))
                )
            if dependency is not None and dependency.poll() is not None:
                if not test.get("allow_server_exit", False) or dependency.returncode != 0:
                    success = False
    except (OSError, RuntimeError, psutil.Error) as exc:
        print(f"        {exc}")
    finally:
        if proc is not None:
            _stop_server(proc)
        if dependency is not None:
            _stop_server(dependency)
    if not success:
        for path in (log, dependency_log):
            if path.exists():
                print(f"        --- {path} ---\n{path.read_text(errors='replace').rstrip()}")
    return success


def main() -> int:
    log_dir = Path(tempfile.mkdtemp(prefix="o6-examples-"))
    print(f"Example logs: {log_dir}", flush=True)
    failures: list[str] = []
    skips: list[str] = []
    for example_id, spec in ALL_EXAMPLES.items():
        if spec.test is None:
            print(f"[skip] {example_id}  ({spec.skip_reason})")
            skips.append(example_id)
            continue
        test = spec.test
        suffix = f"  (needs {spec.requires_server})" if spec.requires_server else ""
        kind = "ready" if test.get("ready_marker") and not test.get("expected") else "banner"
        print(
            f"[run] {example_id}  (timeout={test['timeout']:.0f}s, " f"check={kind}){suffix} ...",
            flush=True,
        )
        ok = run_and_check(example_id, spec, log_dir)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {example_id}")
        if not ok:
            failures.append(example_id)

    print()
    if skips:
        print(f"{len(skips)} skipped:")
        for name in skips:
            print(f"  - {name}")
    if failures:
        print(f"{len(failures)} failure(s):")
        for name in failures:
            print(f"  - {name}")
        return 1
    total = len(ALL_EXAMPLES) - len(skips)
    print(f"{total} example(s) passed; {len(skips)} example(s) skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
