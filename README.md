# o6\Python bindings for open62541

## Install

```bash
sudo apt install build-essential cmake pkg-config \ 
                 libssl-dev libjitterentropy3-dev libzstd-dev \
                 python3-dev python3-venv

python3 -m venv .venv 
source .venv/bin/activate

pip install --editable . --no-build-isolation
```

> On Ubuntu 22 and earlier use `libjitterentropy-dev` instead of `libjitterentropy3-dev`.

## Run an example

```bash
python examples/nodes.py
```