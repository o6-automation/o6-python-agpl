#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""Build the distilling binary with PyInstaller."""

import os
import subprocess
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))


def find_open62541_lib():
    """Find the open62541 .so. The o6 package prints its banner via
    C-level writes to fd 1, which Python can't redirect. So we
    redirect fd 1 to /dev/null and have the subprocess write the
    lib path to a tempfile.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        out_path = f.name
    script = (
        "import os\n"
        "os.dup2(os.open(os.devnull, os.O_WRONLY), 1)\n"
        "import o6\n"
        f"open({out_path!r}, 'w').write(os.path.realpath(\n"
        "    os.path.join(os.path.dirname(o6.__file__), 'libopen62541.so.1.5')\n"
        "))\n"
    )
    subprocess.run([sys.executable, "-c", script], check=True)
    with open(out_path) as f:
        return f.read().strip()


lib_path = find_open62541_lib()
print(f"open62541 lib: {lib_path}")

cmd = [
    sys.executable,
    "-m",
    "PyInstaller",
    "--onefile",
    "--name",
    "distilling",
    "--distpath",
    here,
    "--workpath",
    os.path.join(here, "build"),
    "--specpath",
    tempfile.gettempdir(),
    "--add-data",
    f"{os.path.join(here, 'ui.py')}:.",
    "--collect-all",
    "o6",
    "--collect-all",
    "asyncio",
    "--collect-all",
    "numpy",
    "--hidden-import",
    "uuid",
    "--hidden-import",
    "_uuid",
    "--hidden-import",
    "mmap",
    f"--add-binary={lib_path}:o6",
    os.path.join(here, "server.py"),
    "--clean",
    "-y",
]
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)
print()
print(f"Build complete. Binary at: {os.path.join(here, 'distilling')}")
