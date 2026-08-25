#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Run each example script and verify it printed the expected banner.

The ``EXAMPLES`` dict maps a path under ``examples/`` to
``(expected_output, timeout_seconds)``.  Each entry is launched as a
subprocess; if it has not finished within the timeout, ``SIGINT`` is
sent (matching what a Ctrl+C user would do) and we wait a few more
seconds for a clean exit.  The check passes when the expected output
appears on stdout.

Run from the repository root::

    .venv/bin/python3 examples/check_examples.py
"""

from __future__ import annotations

import signal
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Mapping

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_ROOT = REPO_ROOT / "examples"

# Pick the interpreter that has the ``o6`` package installed.  The repo
# ships a venv at ``.venv/``; fall back to whatever ``sys.executable``
# points at if it isn't there.
_VENV_PY = REPO_ROOT / ".venv" / "bin" / "python"
PYTHON = str(_VENV_PY if _VENV_PY.is_file() else Path(sys.executable))


# Port the embedded servers all bind to.  Used to wait until a freshly
# started server is actually accepting connections.
SERVER_PORT = 4840
SERVER_HOST = "127.0.0.1"


# ---------------------------------------------------------------------------
# Example registry
# ---------------------------------------------------------------------------
# Each entry maps ``rel_path`` (a path under ``examples/``) to a tuple
#   (expected_banner, timeout, requires_server, ready_marker)
#
# ``rel_path``         — path under ``examples/`` to the annotated ``.py``.
# ``expected``         — substring that must appear in stdout for the check
#                        to pass.  Use the trailing banner line printed by
#                        each example so the script only passes if every
#                        section ran to completion.  ``None`` for infinite
#                        examples that never exit on their own.
# ``timeout``          — seconds to wait before sending SIGINT.
# ``requires_server``  — path under ``examples/`` of a server script that
#                        must be started (and stopped) before the entry is
#                        run.  ``None`` means the example is self-contained
# ``ready_marker``     — for infinite-loop examples (servers, controllers,
#                        interactive clients) this is a stdout substring
#                        whose appearance proves the example got going
#                        cleanly.  The check passes when the marker is
#                        seen, even if the timeout fires later.  ``None``
#                        for finite examples where ``expected`` is enough.
#
# Servers double as the *source of truth* for the client→server dependency
# map: the runner only walks ``requires_server``, it does not execute the
# server entry directly.
EXAMPLES: Mapping[str, tuple[str | None, float, str | None, str | None]] = {
    # -----------------------------------------------------------------------
    # OPC UA FX vertical demonstrator
    # -----------------------------------------------------------------------
    "opcua_fx/client.py": (
        "=== OPC UA FX smoke scenario completed ===",
        30.0,
        "opcua_fx/server.py",
        None,
    ),
    "opcua_fx/server.py": (
        None,
        20.0,
        None,
        "OPC UA FX demo server running at opc.tcp://localhost:4840",
    ),
    # -----------------------------------------------------------------------
    # highlevel clients → need highlevel/basic_server.py
    # -----------------------------------------------------------------------
    "highlevel/client_basic.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client_browsing.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client_configuration.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client_modes.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client_nodemanagement.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client_usernamepw.py": (
        "=== Example completed ===",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    "highlevel/client/subscription.py": (
        "Done.",
        30.0,
        "highlevel/basic_server.py",
        None,
    ),
    # -----------------------------------------------------------------------
    # highlevel servers (self-contained, infinite loop → use ready_marker)
    # -----------------------------------------------------------------------
    "highlevel/basic_server.py": (
        None,
        15.0,
        None,
        "Server running at opc.tcp://localhost:4840",
    ),
    "highlevel/server_minimal.py": (
        None,
        15.0,
        None,
        "Server running",
    ),
    "highlevel/server_objects.py": (
        None,
        15.0,
        None,
        "Server running at",
    ),
    "highlevel/server_variables.py": (
        None,
        15.0,
        None,
        "Server running at",
    ),
    "highlevel/server_methods.py": (
        None,
        15.0,
        None,
        "Server running at opc.tcp://localhost:4840",
    ),
    "highlevel/server_async.py": (
        None,
        15.0,
        None,
        "Server running",
    ),
    # -----------------------------------------------------------------------
    # highlevel self-contained (server + client in one process, exits)
    # -----------------------------------------------------------------------
    "highlevel/implement_objtype.py": (
        "=== ObjectType implementation tutorial completed ===",
        30.0,
        None,
        None,
    ),
    "highlevel/implement_readwrite.py": (
        "=== Variable read/write tutorial completed ===",
        30.0,
        None,
        None,
    ),
    # -----------------------------------------------------------------------
    # sim_examples: client needs the sim server (lives at examples/sim_examples/)
    # -----------------------------------------------------------------------
    "sim_examples/client/basic_sim_client.py": (
        "=== Example completed ===",
        30.0,
        "sim_examples/server/basic_sim_server.py",
        None,
    ),
    "sim_examples/server/basic_sim_server.py": (
        None,
        15.0,
        None,
        "Server running at opc.tcp://localhost:4840",
    ),
    # -----------------------------------------------------------------------
    # example-server: client needs the distill server
    # -----------------------------------------------------------------------
    "example-server/client.py": (
        "=== Example completed ===",
        30.0,
        "example-server/server.py",
        None,
    ),
    "example-server/server.py": (
        None,
        15.0,
        None,
        "Server running at",
    ),
    # -----------------------------------------------------------------------
    # sortingline: controller + client need the sortingline server
    # -----------------------------------------------------------------------
    "highlevel/server_sortingline_vc.py": (
        None,
        15.0,
        None,
        "[SERVER] OPC UA Server online",
    ),
    "highlevel/controller_sortingline_vc.py": (
        None,
        15.0,
        "highlevel/server_sortingline_vc.py",
        "[CONTROLLER] Successfully connected to the OPC UA Server.",
    ),
    "highlevel/client_sortingline_vc.py": (
        None,
        15.0,
        "highlevel/server_sortingline_vc.py",
        "[o6 Python] Successfully connected to the Digital Twin",
    ),
}


# Examples that cannot be validated by an end-to-end harness.  ``opcua_browser``
# drives a curses TUI that needs a real terminal, so it is reported as SKIP rather than FAIL.
SKIP: frozenset[str] = frozenset(
    {
        "highlevel/opcua_browser.py",
    }
)


# ---------------------------------------------------------------------------
# Server lifecycle helpers
# ---------------------------------------------------------------------------
def _port_is_open(host: str, port: int, timeout: float = 0.25) -> bool:
    """Return ``True`` if a TCP connection to ``host:port`` succeeds."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _ensure_port_free() -> None:
    """Refuse to start if the OPC UA port is already bound"""
    if _port_is_open(SERVER_HOST, SERVER_PORT):
        raise RuntimeError(
            f"Port {SERVER_PORT} on {SERVER_HOST} is already in use. "
            f"Kill the lingering server (e.g. `pkill -f basic_server.py`) "
            f"and re-run."
        )


def _wait_for_server(deadline_s: float = 10.0) -> bool:
    """Poll the server port until it accepts a connection or the deadline
    elapses.  Returns ``True`` on success."""
    end = time.monotonic() + deadline_s
    while time.monotonic() < end:
        if _port_is_open(SERVER_HOST, SERVER_PORT):
            return True
        time.sleep(0.1)
    return False


def _start_server(server_rel: str) -> subprocess.Popen:
    """Spawn a dependency server, wait until it accepts connections, and
    return the handle.  Caller owns the lifecycle."""
    print(f"        starting dependency server: {server_rel}", flush=True)
    proc = subprocess.Popen(
        [PYTHON, str(EXAMPLES_ROOT / server_rel)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(REPO_ROOT),
    )
    if not _wait_for_server():
        # Server didn't come up — capture its early output for the report.
        proc.kill()
        try:
            _stdout, stderr = proc.communicate(timeout=2.0)
        except subprocess.TimeoutExpired:
            stderr = ""
        raise RuntimeError(
            f"dependency server {server_rel} did not open port "
            f"{SERVER_PORT} within the deadline. stderr:\n{stderr}"
        )
    return proc


def _stop_server(proc: subprocess.Popen) -> None:
    """SIGINT (matches a Ctrl+C user) then a hard kill as a fallback."""
    if proc.poll() is not None:
        return
    proc.send_signal(signal.SIGINT)
    try:
        proc.wait(timeout=5.0)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5.0)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
def run_and_check(
    rel_path: str,
    expected: str | None,
    timeout: float,
    requires_server: str | None,
    ready_marker: str | None,
) -> bool:
    """Launch one example, kill with SIGINT on timeout, return ``True`` if
    the example is considered successful.  Success criteria:

    * If ``expected`` is set, the example must print it on stdout (use
      for finite client examples whose trailing banner is unique).
    * If ``ready_marker`` is set, the example must print it on stdout
      (use for infinite-loop examples; reaching the marker proves the
      example got going — the subsequent timeout kill is considered successfuls,
      not a failure).

    On failure, ``stderr`` is printed so the cause is visible without
    re-running by hand.  When ``requires_server`` is set, the named
    server script is started before the example and stopped after."""
    server_proc: subprocess.Popen | None = None
    if requires_server is not None:
        try:
            server_proc = _start_server(requires_server)
        except RuntimeError as exc:
            print(f"        {exc}")
            return False

    cmd = [PYTHON, str(EXAMPLES_ROOT / rel_path)]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(REPO_ROOT),
    )
    try:
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            # Still alive after the timeout — nudge it like Ctrl+C, then
            # give it a moment to flush its final prints before forcing
            # a hard kill.
            proc.send_signal(signal.SIGINT)
            try:
                stdout, stderr = proc.communicate(timeout=5.0)
            except subprocess.TimeoutExpired:
                proc.kill()
                stdout, stderr = proc.communicate()
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait(timeout=5.0)
        if server_proc is not None:
            _stop_server(server_proc)

    success = (expected is not None and expected in stdout) or (
        ready_marker is not None and ready_marker in stdout
    )
    if success:
        return True
    if stderr:
        print(f"        --- stderr from {rel_path} ---\n{stderr.rstrip()}")
        print(f"        --- end stderr ---")
    return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> int:
    try:
        _ensure_port_free()
    except RuntimeError as exc:
        print(f"[abort] {exc}")
        return 2

    failures: list[str] = []
    skips: list[str] = []
    for rel_path, (expected, timeout, requires_server, ready_marker) in EXAMPLES.items():
        if rel_path in SKIP:
            print(f"[skip] {rel_path}")
            skips.append(rel_path)
            continue
        suffix = f"  (needs {requires_server})" if requires_server else ""
        kind = "ready" if ready_marker and not expected else "banner"
        print(
            f"[run] {rel_path}  (timeout={timeout:.0f}s, " f"check={kind}){suffix} ...",
            flush=True,
        )
        ok = run_and_check(rel_path, expected, timeout, requires_server, ready_marker)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {rel_path}")
        if not ok:
            failures.append(rel_path)

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
    total = len(EXAMPLES) - len(skips)
    print(f"{total} example(s) passed; {len(skips)} example(s) skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
