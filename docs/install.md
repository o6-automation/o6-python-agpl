# Installing o6\\Python

## Requirements

| | |
|---|---|
| Python | 3.10 – 3.14 (CPython) |
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
    starts a two-hour evaluation period — see
    [Commercial build](commercial-build.md).


## Build from the AGPL repository

o6\\Python may by used freely for public research and in education —
no licence fee, no Credential, no evaluation timer counting down while you work. 
o6\\Python is released under AGPL-3.0-or-later at [o6-automation/o6-python-agpl](https://github.com/o6-automation/o6-python-agpl).

Building it compiles open62541 from source and requires a C toolchain.

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

Find out more on the official [github page](https://github.com/o6-automation/o6-python-agpl).
