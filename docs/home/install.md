# Install

## Requirements

| | |
|---|---|
| Python | 3.11 – 3.15 (CPython) |
| Platforms | Linux `x86_64` / `aarch64`, macOS `x86_64` / `arm64`, Windows `AMD64` / `ARM64` |

Wheels bundle open62541 and OpenSSL, so no OPC UA stack or C toolchain is
needed. Windows ARM64 wheels start at Python 3.11.

## Install from PyPI

```sh
pip install o6
```

Verify the installation:

```sh
python -c "import o6; print(o6.__version__)"
```

!!! info

    PyPI ships the commercial build. Without a Credential, importing `o6`
    starts ten-minute Script Mode, which permits commercial use. See
    [Commercial build](commercial-build.md).

## AGPL build

o6\\Python is also released under AGPL-3.0-or-later at
[o6-automation/o6-python-agpl](https://github.com/o6-automation/o6-python-agpl).
You may use it freely for public research and education: no licence fee, no
Credential and no Script Mode timer. The AGPL build is not on PyPI. It compiles
open62541 from source and needs a C toolchain. On Debian or Ubuntu:

```sh
sudo apt install build-essential cmake pkg-config \
                 libssl-dev libjitterentropy3-dev libzstd-dev \
                 python3-dev python3-venv

git clone --recurse-submodules https://github.com/o6-automation/o6-python-agpl.git
cd o6-python-agpl

python3 -m venv .venv
source .venv/bin/activate
pip install . --no-build-isolation
```

For other platforms and build options, see the
[project README](https://github.com/o6-automation/o6-python-agpl#readme).
