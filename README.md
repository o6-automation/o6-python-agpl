# o6\Python - OPC UA for Python (AGPL version)

This is the AGPL-licensed version of o6\Python. It provides deep Python
integration of OPC UA.

o6 Automation GmbH, the author of the library, provides o6\Python under a commercial license as well:

https://www.o6-automation.com

## Building the library

o6\Python consists of a native Python module with additional definitions in the
Python language itself.

On many systems, a single command will build and install the library:

```
pip install
```

On Debian-based systems you might have to do more convincing:

```
pip install -v --break-system-packages --editable . --no-build-isolation
```
