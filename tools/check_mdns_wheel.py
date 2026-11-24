# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Run the mDNS and TCP release gate against an installed wheel outside the checkout."""

import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import socket
import subprocess
import sys
import sysconfig
import tempfile
import xml.etree.ElementTree as ET

PROBE = """
from importlib.metadata import distribution
import json
from pathlib import Path
import platform
import sys
import sysconfig
import o6
from o6 import _o6
from o6.discovery import MdnsConfig, mdnsAvailable

roots = {Path(sysconfig.get_path(key)).resolve() for key in ('purelib', 'platlib')}
for module in (o6, _o6):
    path = Path(module.__file__).resolve()
    assert any(path.is_relative_to(root) for root in roots), f'Not an installed wheel: {path}'
assert sys.platform in ('linux', 'darwin', 'win32'), sys.platform
expected = sys.platform in ('linux', 'darwin')
assert mdnsAvailable is expected, f'{sys.platform}: expected mDNS={expected}, got {mdnsAvailable}'
server = o6.Server(port=0)
server.setMdns(None)
if expected:
    config = MdnsConfig(listen=False, announce=False)
    server.setMdns(config)
    assert server.mdnsConfig is config
    server.setMdns(None)
else:
    try:
        server.setMdns(MdnsConfig())
    except NotImplementedError:
        pass
    else:
        raise AssertionError('Unsupported wheel accepted mDNS')
    assert server.mdnsConfig is None
print(json.dumps(dict(version=distribution('o6').version, python=sys.version,
                     platform=platform.platform(), machine=platform.machine(),
                     package=o6.__file__, extension=_o6.__file__, mdnsAvailable=mdnsAvailable)))
"""


def run_logged(command, *, cwd, env, log, timeout):
    """Retain output even when a test fails or exceeds its time limit."""
    with log.open("w", encoding="utf-8") as output:
        try:
            result = subprocess.run(
                command, cwd=cwd, env=env, stdout=output, stderr=subprocess.STDOUT, timeout=timeout
            )
        finally:
            output.flush()
            print(log.read_text(encoding="utf-8"), flush=True)
    if result.returncode:
        raise RuntimeError(f"Wheel validation failed ({result.returncode}); see {log}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--multicast", action="store_true", help="Require reception and withdrawal")
    args = parser.parse_args()
    source = args.source.resolve()
    # "t" keeps free-threaded (cp314t) evidence apart from the GIL build's (cp314).
    freethreaded = "t" if sysconfig.get_config_var("Py_GIL_DISABLED") else ""
    tag = f"{sys.platform}-{platform.machine()}-cp{sys.version_info.major}{sys.version_info.minor}{freethreaded}"
    evidence = args.evidence.resolve() / tag
    evidence.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key in ("PYTHONPATH", "PYTHONHOME", "PYTEST_ADDOPTS"):
        env.pop(key, None)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    with tempfile.TemporaryDirectory(prefix="o6-mdns-wheel-") as directory:
        work = Path(directory)
        run_logged(
            [sys.executable, "-I", "-c", PROBE],
            cwd=work,
            env=env,
            log=evidence / "capability.log",
            timeout=30,
        )
        supported = sys.platform in {"linux", "darwin"}
        files = ["test_mdns.py", "test_tcp_buffers.py"]
        if supported:
            files.append("test_registration_mdns.py")
            if args.multicast:
                files.append("test_mdns_multicast.py")
                if not env.get("O6_MDNS_INTERFACE"):
                    # Connecting a UDP socket selects the route without sending a packet.
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as route:
                        route.connect(("224.0.0.251", 5353))
                        env["O6_MDNS_INTERFACE"] = route.getsockname()[0]
                print(f"Multicast interface: {env['O6_MDNS_INTERFACE']}", flush=True)
        for package in ("tests", "tests/_support", "tests/connections"):
            (work / package).mkdir(parents=True, exist_ok=True)
            (work / package / "__init__.py").touch()
        # Copy every helper, so a new import between helpers cannot break the check
        for helper in (source / "tests/_support").glob("*.py"):
            shutil.copy2(helper, work / "tests/_support" / helper.name)
        for name in files:
            shutil.copy2(source / "tests/connections" / name, work / "tests/connections" / name)
        report = evidence / "junit.xml"
        command = [
            sys.executable,
            "-I",
            "-m",
            "pytest",
            "-p",
            "pytest_asyncio.plugin",
            "-o",
            "asyncio_mode=auto",
            "-o",
            "asyncio_default_fixture_loop_scope=function",
            "-o",
            "markers=server: server-only tests\nclient: client API tests",
            "-v",
            "-s",
            "--tb=short",
            f"--junitxml={report}",
            f"--basetemp={evidence / 'runtime'}",
        ]
        if not supported:
            command += [
                "-k",
                "defaults_and_immutable_snapshot or invalid_configuration or disabled_build_contract "
                "or tcp_receive_buffers",
            ]
        command += [f"tests/connections/{name}" for name in files]
        (evidence / "run.json").write_text(
            json.dumps(
                {
                    "command": command,
                    "interface": env.get("O6_MDNS_INTERFACE"),
                    "multicast_requested": args.multicast,
                    "source": str(source),
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        try:
            run_logged(command, cwd=work, env=env, log=evidence / "runtime.log", timeout=240)
        finally:
            # manylinux runs as root; the host artifact uploader must be able
            # to read pytest's otherwise private temporary directories.
            if sys.platform == "linux":
                for path in evidence.rglob("*"):
                    if not path.is_symlink():
                        path.chmod(0o755 if path.is_dir() else 0o644)
        cases = ET.parse(report).findall(".//testcase")
        if not cases or any(case.find("skipped") is not None for case in cases):
            raise RuntimeError(f"Wheel gate requires executed tests without skips; see {report}")
    print(f"mDNS and TCP wheel gate passed; evidence: {evidence}")


if __name__ == "__main__":
    main()
