# o6\Python

**High-performance OPC UA for Python — client and server — built on the native
[open62541](https://open62541.org/) SDK.**

[![PyPI version](https://img.shields.io/pypi/v/o6.svg)](https://pypi.org/project/o6/)
[![Python versions](https://img.shields.io/pypi/pyversions/o6.svg)](https://pypi.org/project/o6/)
[![Documentation](https://img.shields.io/badge/docs-docs.o6--automation.com-blue.svg)](https://docs.o6-automation.com/o6-python/)

You need to talk to industrial equipment — a robot cell, a CNC machine, a
packaging line — and it speaks OPC UA. With o6\Python that looks like this:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    print(client.objects.Machine.Speed())     # read it
    client.objects.Machine.Speed(1500)        # write it
    client.objects.Machine.Reset()            # call it
```

Every OPC UA server publishes an *information model*: a browsable tree of typed
nodes describing what the machine is and what it can do. o6\Python turns that
tree into Python objects, so you can point a REPL at a machine you have never
seen, type `client.objects.` and press Tab, and browse the real thing — no
vendor PDF, no NodeId spreadsheet.

The same principle runs through the rest of the library. o6\Python is a complete
OPC UA stack, client and server: the address space is Python objects, and the
protocol underneath is compiled C. Reads, writes, browsing, method calls,
subscriptions, events, historical access, custom information models, and the
full security stack are all first-class.

```bash
pip install o6
```

> **Note:** The wheel published here runs in evaluation mode. The full Client and
> Server API is available, with a two hours runtime. See
> [Licensing](#licensing).

**Full documentation: <https://docs.o6-automation.com/o6-python/>**

---

## Why this is different

OPC UA is a superb protocol wrapped in a miserable developer experience:
numeric node IDs carry the meaning, XML files have to be shipped and parsed at
startup, and every value arrives as a `Variant` to unwrap and cast by hand.

The promise of OPC UA is that the semantics travel with the protocol, so no
manual is needed to know what a value means. In practice one manual is often
traded for another, and the effort shifts from speaking N protocols to
understanding OPC UA itself. o6\Python is built to keep that promise: the
semantics are already there, and using them should not require studying the
protocol first.

| Typical OPC UA constraints | o6\Python |
|---|---|
| `ns=4;i=6021` with the meaning in a comment | `DeviceHealthEnumeration.NORMAL`, autocompleted |
| Ship the NodeSet2 XML, parse it on every start | `from o6.ns import di`, compiled into the package |
| A `Variant` you unwrap and cast to the right type | A plain, correctly-typed value |
| Read a vendor PDF to find a node's id | Press Tab in a REPL — names and descriptions included |
| Structures arrive as opaque extension objects | Structures arrive as your classes, with `.pyi` stubs |
| Commit to a process model up front | One call syntax, with or without `await` |
| Nodesets in cumbersome XML | Nodesets as readable Python, compiled from XML or written directly |

## What you get

**Native speed.** The protocol stack is compiled C, and it shows in both roles — 
see the [benchmark results](https://docs.o6-automation.com/o6-python/performance/).

**Client and server, one API.** Connect to existing servers or expose your own
address space, with the same types and conventions — and the same calls work
synchronously or with `await` inside `asyncio`, so an application never has to
commit to a concurrency model up front.

**More than 130 companion specifications, included.** Machinery, Robotics,
Machine Tools (umati), PackML, EUROMAP, Machine Vision, UAFX and many more ship
as importable, fully type-annotated Python namespaces, alongside a compiler for
your own NodeSet2 XML files.

**Information models written in Python.** Declare object types, variable types,
structures, enumerations, and methods with decorators. The server builds the
nodes, and from that point the classes are your API.

**Typed against the specification.** NumPy-backed builtin scalars, generated
`.pyi` stubs for structure fields, IDE autocompletion, `mypy`-checkable
signatures.

**Secure by default.** Encrypted channels, the full range of security policies
and modes, certificate and username authentication, and role- and
permission-based access control — a foundation intended for products that go
through official OPC UA certification.

**Prebuilt wheels.** CPython 3.11–3.14 on Linux, macOS, and Windows, for x86-64
and ARM64. No compiler, no CMake, no C toolchain.

## Quick start

A `Client` is a context manager: connect it in a `with` block, and the secure
channel and the session open on entry and close on the way out — including when
your code raises. Address values by NodeId; the familiar string form works
wherever a NodeId is accepted.

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    value = client.read("ns=1;s=IntegerVariable")
    client.write("ns=1;s=IntegerVariable", o6.UInt32(42))
```

Batch reads and writes: hand `read` a list or `write` a dict, and the whole
group travels in a single service call rather than one round trip per value.

### Walking the server as an object tree

Start from one of four entry points on a connected client — `client.root`,
`client.objects`, `client.types`, and `client.views` — and step one level deeper
into the live server with every `.`.

```python
variables = client.objects.MyVariables

print(variables.MyInteger())                      # read
variables.MyInteger(42)                           # write
print(client.objects.TestMethods.Hello("o6"))     # call a method
```

For browse names that are not valid Python identifiers, use bracket syntax — it
takes a whole path, as in `client.objects["MyDevice/Temperature Setpoint"]`.

### Subscribe, stop polling

Subscribe in a single line, and the server reports changes as they occur. Use
`client.monitorEvent` for events.

```python
client.monitor("ns=1;s=IntegerVariable", lambda v: print(v), samplingInterval=500.0)
```

### A full server in two calls

```python
from o6 import Server

server = Server(port=4840)
server.start()
```

That is a running OPC UA server with a standard address space. Add your own
content from there, imperatively at runtime or declared as types.

### The same client, asynchronously

Nothing changes but the `await`.

```python
import asyncio
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840") as client:
        print(await client.read("i=2258"))   # server time

asyncio.run(main())
```

## Companion specifications, with no XML at runtime

A *companion specification* is an information model agreed on by an industry
group. It fixes the model of a device, machine, or process, so that a robot from
one vendor and a robot from another expose the same types with the same
semantics.

Traditionally, using one means bundling its NodeSet2 XML file with your
application, parsing it at startup, and addressing everything inside through
numeric IDs. o6\Python compiles them ahead of time instead, so you just import
one. More than 130 ship as ordinary Python packages under `o6.ns`, each exposing
its content through five category modules: `datatypes`, `objtypes`, `vartypes`,
`reftypes`, and `instances`.

```python
import o6
from o6.ns import di            # OPC UA for Devices

# Structures are classes; their fields keep their exact OPC UA types,
# and the package ships .pyi stubs so your editor and mypy know them.
result = di.datatypes.TransferResultDataDataType()
result.sequenceNumber = 42

# Enumerations are enumerations, and inheritance is plain Python inheritance.
di.datatypes.DeviceHealthEnumeration.NORMAL

# Types carry their NodeId, so you never hand-write one.
o6.NodeId(di.objtypes.DeviceType)            # ns=di;i=1002
```

See the documentation for
[every packaged specification](https://docs.o6-automation.com/o6-python/types-addrspace/namespace/namespace-mapping-in-o6/#packaged-companion-specs).

Each one carries its own metadata: URI, version, index, and a shortname. Use the
shortname wherever a namespace index is expected, and `o6.NodeId("ns=di;i=1002")`
resolves correctly against servers that number their namespaces differently.

Publish a specification on a server by appending the module
(`server.ns.append(di)`). On a client, declare nothing at all — on connect it
matches the server's advertised namespace URIs against what it has compiled in,
down to the exact version when the server publishes its metadata.

Your own NodeSet2 XML files join them on equal footing: run the bundled compiler
and a `*.NodeSet2.xml` becomes exactly this kind of Python package — a build step
you pay for once, instead of an XML parse on every process start. The generator
fails on constructs it cannot represent faithfully, so an unsupported nodeset is
a compile error, not a silently incomplete address space.

## Information models written in Python

Write your own types the same way you use the packaged ones: declare a
namespace, then decorate a class per structure, enumeration, variable type, and
object type, using `hasProperty` and `hasComponent` for a type's children. There
is no XML editor, no modeling tool, and no generate-and-reload cycle between
having an idea and running a server that serves it.

```python
# plant.py
import o6
from o6.ns import ns0

o6.ns.namespace("plant", uri="http://example.org/Plant/", version="1.0")

@o6.enumtype(ns="plant", description="Machine state")
class MachineState:
    IDLE = 0
    RUNNING = 1
    FAULT = 2

@o6.variabletype(ns="plant", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=str)
    )

@o6.objecttype(ns="plant", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=MachineState)
    )
    temperature: TemperatureType = o6.hasComponent(TemperatureType())
    reset: o6.node.MethodNode = o6.hasComponent(o6.call())
```

That is a complete information model, carrying the same content a NodeSet2 XML
file carries in a few dozen lines a human can read, review in a diff, and
comment on in a pull request. Because these are ordinary classes, they compose
with the companion specifications: derive from a DI or Machinery type, and your
vendor-specific extension is plain subclassing with the standard parts included.

Publish the module on a server, and the classes are your API.

```python
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)
server.start()

machine = plant.MachineType(
    parent=server.objectsNode,
    browseName="M-101",
    values={"state": int(plant.MachineState.RUNNING)},
)

machine.state()                        # 1
machine.temperature(23.5)              # write
machine.temperature.engineeringUnits() # read a property of a property
```

One instantiation created the object, its properties, its methods, and its whole
subtree in the address space, and attribute access reads and writes live values.
Import the same module in a client process, and your structures decode as the
classes you declared rather than as opaque extension objects.

## Requirements

- CPython 3.11–3.14 (standard GIL build)
- NumPy ≥ 2.0, < 3
- Linux with glibc ≥ 2.28 (`manylinux_2_28`), macOS ≥ 15, or Windows 10 LTSC
  2021 / Server 2022 and newer — on x86-64 or ARM64

## Licensing

This PyPI package is the **commercial build** of o6\Python. It is licensed for
commercial use; an o6-issued Credential is required for production use.

Without a valid Credential, the package runs in **two-hour evaluation mode**:
the full Client and Server API is available, and the process is terminated
with a failure exit status when the two-hour timer expires. 
See also [Credential discovery and Feature Scope](https://docs.o6-automation.com/o6-python/home/commercial-build/)

- **Commercial (developer seat or volume):** see the
  [o6\Python product page](https://www.o6-automation.com/o6-python/) or contact
  [contact@o6-automation.com](mailto:contact@o6-automation.com)
- **Non-commercial, research and education:** o6\Python is dual-licensed and
  available under the AGPL at
  **<https://github.com/o6-automation/o6-python-agpl>**. For research and
  education, [get in touch](https://www.o6-automation.com/contact) and request a
  free research license.

## Support

o6\Python is developed, maintained, and supported by
[o6 Automation](https://www.o6-automation.com/), the SDK manufacturer. That
includes the associated CRA and cybersecurity obligations. Training, long-term
support, and certification assistance are available.

- Documentation: <https://docs.o6-automation.com/o6-python/>
- Product page: <https://www.o6-automation.com/o6-python/>
- Company: <https://www.o6-automation.com/>
- AGPL source: <https://github.com/o6-automation/o6-python-agpl>
- Contact: [contact@o6-automation.com](mailto:contact@o6-automation.com) or the
  [contact form](https://www.o6-automation.com/contact)
