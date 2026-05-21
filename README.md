# pyo6 - Python bindings for open62541

## prequesites 

### build requirements

```
pip install --upgrade pip setuptools build wheel numpy cython black mypy
```

### build docs

Requirements:

```
pip install zensical, mkdocstrings-python
```



### open62541 library

By default the module build will use `deps/open62541` as a git submodule if present, or else clone open62541 into `deps/open62541`, build it, and install it into `deps/open62541/build/install`. The extension links against and bundles the local installation automatically.

If you want to use a submodule, initialize it with:

```
git submodule update --init --recursive deps/open62541
```

open62541 may also be installed system-wide (either from your package manager or by omitting `-DCMAKE_INSTALL_PREFIX` during cmake configuration). To make the module build link against the system library instead, use:

```
export O6_USE_SYSTEM_LIB=1
```

## building o6-python module

```
python3 setup.py build
```

*Optionally:* To pin a specific open62541 version, run `build_open62541` with `--open62541-ref` before the build, i.e.:

```
python3 setup.py build_open62541 --open62541-ref=v1.3.9 build
```

*Optionally:* To use a custom NodeSet2 XML for enum code generation, run `src_gen` with `--nodeset` before the build, i.e.:

```
python3 setup.py src_gen --nodeset path/to/custom_nodeset2.xml build
```

### build + install for testing

```
pip install -v --break-system-packages --editable . --no-build-isolation
```

Optional build configurations with `--open62541-ref` or `--nodeset` can be passed directly to the pip install command

```
pip install -v --break-system-packages --editable .  --no-build-isolation \
        --build-option="build_open62541 --open62541-ref=v1.3.9" \
        --build-option="src_gen --nodeset path/to/custom_nodeset2.xml"
```

## valgrind tests

Additionally requires:

```
pip install pytest
```

Run with:

```
PYTHONMALLOC=malloc valgrind --tool=memcheck   --suppressions=/usr/lib/valgrind/python3.supp   --leak-check=full --track-origins=yes   python3 ./tests/test_client.py
```
