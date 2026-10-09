# o6\Python bindings for open62541

o6\Python is a Python interface to the [open62541](https://open62541.org/)
OPC UA stack, with support for both clients and servers. It provides tools for
connecting laboratory and industrial equipment, exposing simulated processes,
and developing information models. Protocol processing runs in native C;
Python provides the application logic and typed representations of the data
and models exchanged between systems.

## Install from source

**Start here for the AGPL distribution.** These instructions build open62541
and the Python extension locally. The `o6` package on PyPI is a separate
commercial distribution; installing it does not install the AGPL build.

Use **CPython 3.11–3.14 with the standard GIL build**. The commands below target
Debian and Ubuntu and assume that `python3` is a supported version.

Install the system build dependencies:

```bash
sudo apt install git build-essential cmake pkg-config \
                 libssl-dev libjitterentropy3-dev libzstd-dev \
                 python3-dev python3-venv
```

> On Ubuntu 22 and earlier use `libjitterentropy-dev` instead of `libjitterentropy3-dev`.

Get the AGPL source, or use your existing checkout. Run the remaining commands
from the repository root:

```bash
git clone https://github.com/o6-automation/o6-python-agpl.git
cd o6-python-agpl
```

Initialize the build dependencies, create a virtual environment, and install:

```bash
git submodule update --init --recursive deps/open62541 deps/UA-Nodeset

python3 -m venv .venv
source .venv/bin/activate

python -m pip install 'setuptools>=65.4.1' wheel 'numpy>=2.0,<3' 'Cython>=3.0' packaging
python -m pip install --editable . --no-build-isolation

python -c "import o6; print(o6.__version__)"
```

The Python build dependencies must be installed explicitly because
`--no-build-isolation` uses the active environment. The editable installation
keeps Python source changes available from the checkout; changes to compiled
code require rebuilding.

## Run an example

From the repository root with the virtual environment activated, start the
example server:

```bash
python examples/server/S03_firststeps.py
```

Once it reports that it is running, open a second terminal in the same
repository, activate the environment, and run the client:

```bash
source .venv/bin/activate
python examples/client/C02_firststeps.py
```

The server exposes a simulated plant at `opc.tcp://localhost:4840`. The client
reads and writes variables, calls a method, subscribes to changes, and browses
the address space. Stop the server with **Ctrl+C** when finished.

The commented [server](examples/server/S03_firststeps.py) and
[client](examples/client/C02_firststeps.py) sources provide a starting point for
lab exercises and experiments. Further examples are in [examples/](examples/).

## From protocol services to domain models

OPC UA represents a system as an *address space*: a graph of typed nodes and
references describing data, operations, and their relationships. An
*information model* defines the types and semantics used in that address space.
The protocol therefore communicates both values and descriptions of what those
values represent.

For example, a temperature measurement has a value and a data type, but it also
belongs to a device and may have properties describing its units. An
application needs access to these relationships to interpret the measurement.
OPC UA encodes them in the address space; o6\Python exposes them through Python
objects, attributes, and classes.

This mapping reduces the application code needed to associate NodeIds with
domain concepts, convert `Variant` values, and decode extension objects. The
same interface supports two levels of work: direct NodeId and service access
for studying protocol behavior, and model-based access for implementing a
device interface or an experiment.

| OPC UA concept | Python representation |
|---|---|
| Address-space nodes and references | Objects navigated by browse name, with names and descriptions available during interactive exploration |
| Typed values carried in `Variant` containers | Values with the corresponding Python or NumPy types |
| Enumerated data types | Named members such as `DeviceHealthEnumeration.NORMAL` |
| Structured data carried in extension objects | Classes with typed fields and generated `.pyi` stubs |
| Information models described in NodeSet2 XML | Compiled namespace packages, such as `o6.ns.di` |
| Application-specific type definitions | Python declarations or packages compiled from custom NodeSet2 XML |

The type mapping preserves information needed by editors and static analysis:
builtin OPC UA scalar types use NumPy, structure fields have generated type
stubs, and annotated signatures can be checked with `mypy`. Standard and custom
models use the same namespace mechanism and can be composed through Python
inheritance.

### Execution and service coverage

The native open62541 stack handles protocol processing, while the Python API
covers browsing, reads and writes, method calls, subscriptions, events, and
historical access. Client and server applications share data types and modeling
conventions. Client operations can be called synchronously or awaited within
`asyncio`, allowing the communication layer to be used in both sequential
scripts and applications that coordinate concurrent tasks.

The documented [benchmarks](https://docs.o6-automation.com/o6-python/performance/)
report client and server performance. They provide a basis for evaluating the
implementation against the communication workload of a particular experiment.

Security configuration includes encrypted channels, security policies and
modes, certificate and username authentication, and role- and permission-based
access control. These mechanisms allow applications to specify both how a
connection is authenticated and which operations a participant may perform.

## Qickstrart

The following examples progress from individual service calls to navigation
and subscriptions. They use the server started in
[Run an example](#run-an-example), whose `Plant` object contains temperature,
pressure, and counter variables and an `Add` method. The node identifiers and
browse names below refer to that example's address space.

### Addressing values and grouping requests

A NodeId identifies a node within a server's address space. The client accepts
the OPC UA string form wherever a NodeId is expected. In this example,
`ns=1;i=1001` identifies the temperature variable.

The `Client` context manager bounds the connection's lifetime: entering the
`with` block opens the secure channel and session; leaving it closes them,
including when an exception is raised.

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    temperature = client.read("ns=1;i=1001")
    client.write("ns=1;i=1001", o6.Double(25.0))
```

For batch operations, pass a list to `read` or a dictionary to `write`. Each
batch uses one service request, reducing network round trips when acquiring or
updating several variables:

```python
with Client("opc.tcp://localhost:4840") as client:
    temperature, pressure = client.read(["ns=1;i=1001", "ns=1;i=1002"])
    client.write({"ns=1;i=1001": 25.0, "ns=1;i=1002": 1013.25})
```

### Relating identifiers to the address space

The same temperature variable can be reached through its position in the
address space. A connected client exposes four entry points: `client.root`,
`client.objects`, `client.types`, and `client.views`. Attribute access follows
browse names, and REPL completion helps explore the nodes a server publishes.
Calling a variable with no argument reads it; passing a value writes it.
Method nodes expose operations with callable arguments and results.

```python
with Client("opc.tcp://localhost:4840") as client:
    plant = client.objects.Plant
    print(plant.Temperature())     # Read a variable.
    plant.Temperature(25.0)        # Write a value.
    print(plant.Add(3.0, 4.0))      # Invoke a method.
```

Bracket syntax also accepts paths, for example `client.objects["Plant/Temperature"]`.
It can address browse names containing spaces or other characters that are not
valid Python identifiers, such as `client.objects["MyDevice/Temperature Setpoint"]`
on a server that exposes that path.

### Observing changes over time

Repeated reads let the application choose when to request a value.
Subscriptions instead ask the server to monitor a variable and send change
notifications. The example below observes the simulated plant's counter for
five seconds, with a requested sampling interval of 500 milliseconds.

```python
import time

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1004",  # The example server's counter.
        lambda item, value: print(value),
        samplingInterval=500.0,  # Milliseconds.
    )
    time.sleep(5)  # Keep the session open while notifications arrive.
    item.delete()
```

Sampling intervals, publishing intervals, and queue settings are separate
parameters. Varying them provides a practical exercise in the relationship
between acquisition frequency, notification delivery, and communication load.
Use `client.monitorEvent` for event notifications.

### Providing a server for a device or simulation

Constructing and starting a server creates an OPC UA endpoint with the standard
address space. Run this in an interactive Python session after stopping the
earlier example server, since both use port 4840:

```python
from o6 import Server

server = Server(port=4840)
server.start()
```

Add application content through methods such as `addObject` and `addVariable`,
or instantiate declared types as shown below. The server runs in its own
thread while the application updates values or performs other work. Call
`server.stop()` when finished; a standalone application must keep its process
alive for as long as it should serve clients.

### Integrating communication with concurrent tasks

An experiment may need to coordinate communication with several devices or
other asynchronous work. The client API supports this through `asyncio`, using
`async with` for connection lifetime and `await` for operations:

```python
import asyncio
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840") as client:
        print(await client.read("i=2258"))  # Server time.

asyncio.run(main())
```

## Reusing standardized information models

A *companion specification* defines the types and semantics used to describe
devices, machines, or processes in a particular domain. Implementations that
follow the same specification expose a shared model. For a research setup,
this provides a defined interface against which equipment, client software,
and simulated devices can be developed and compared.

o6\Python includes more than 130 companion specifications as Python namespaces
under `o6.ns`, including Devices, Machinery, Robotics, Machine Tools (umati),
PackML, EUROMAP, Machine Vision, and UAFX.

### Compilation and typed access

NodeSet2 XML describes a model for exchange between tools. o6\Python compiles
these definitions ahead of time into importable Python packages; applications
do not need to load and parse the model's XML at startup. Each package groups
its content into `datatypes`, `objtypes`, `vartypes`, `reftypes`, and
`instances`.

```python
import o6
from o6.ns import di  # OPC UA for Devices

# Generated structures retain the OPC UA types of their fields.
result = di.datatypes.TransferResultDataDataType()
result.sequenceNumber = 42

# Enumerations expose named members.
health = di.datatypes.DeviceHealthEnumeration.NORMAL

# Model types carry their NodeIds.
device_type = o6.NodeId(di.objtypes.DeviceType)  # ns=di;i=1002
```

Generated `.pyi` stubs make structure fields available to editor completion
and static analysis. See the
[list of packaged specifications](https://docs.o6-automation.com/o6-python/types-addrspace/namespace/namespace-mapping-in-o6/#packaged-companion-specs)
for the available models.

### Namespace identity across servers

A namespace carries its URI, version, index, and shortname. Symbolic NodeIds
such as `o6.NodeId("ns=di;i=1002")` use the shortname to resolve the namespace
against the connected server. Application code can therefore refer to the
same type even when different servers assign different numeric namespace
indices.

To publish a specification on a server, append the namespace module with
`server.ns.append(di)`. On connection, a client matches the server's advertised
namespace URIs to its compiled namespaces, using version metadata when the
server provides it, including exact version matching when that metadata is
available.

### Preparing additional models

Custom NodeSet2 XML files can be compiled into packages with the same structure.
Model translation becomes a build step, and the resulting package can be
versioned with the application or experimental setup that uses it. The compiler
reports constructs it cannot represent faithfully as errors, making such
limitations visible during model preparation.

## Defining a model

An application-specific model can describe the state, measurements, and
operations of an apparatus. Such a model can be declared directly in Python,
without an intermediate XML authoring or generation step. The declarations
remain source code that can be reviewed and versioned alongside the experiment.

First register a namespace. Decorators then define structures, enumerations,
variable types, and object types within it; `hasProperty` and `hasComponent`
declare their children. The following model describes a test rig with an
operating state, a temperature, and a reset method. Save it as `test_rig.py`:

```python
import o6
from o6.ns import ns0

o6.ns.namespace("test_rig", uri="urn:example:TestRig", version="1.0")

@o6.enumtype(ns="test_rig", description="Test rig operating state")
class RigState:
    IDLE = 0
    RUNNING = 1
    FAULT = 2

@o6.variabletype(ns="test_rig", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=str)
    )

@o6.objecttype(ns="test_rig", browseName="TestRigType")
class TestRigType(ns0.objtypes.BaseObjectType):
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=RigState)
    )
    temperature: TemperatureType = o6.hasComponent(TemperatureType())
    reset: o6.node.MethodNode = o6.hasComponent(o6.call())
```

`RigState` gives the operating states explicit names and values.
`TemperatureType` defines a scalar measurement with a units property, and
`TestRigType` brings these definitions together in an object type. The reset
declaration creates a method node; application code supplies its behavior.
Here, `engineeringUnits` is a simple string property for the example.

Python inheritance can extend types from existing companion specifications,
including Devices and Machinery. This supports domain-specific extensions
while retaining the structure defined by the standard model.

### From type definition to live instance

Publishing the module registers the model on a server. Instantiating its object
type then creates a particular apparatus with that structure. Run the following
in a separate interactive session in the same directory, after stopping any
other server on port 4840:

```python
import o6
import test_rig

server = o6.Server(port=4840)
server.ns.append(test_rig)
server.start()

rig = test_rig.TestRigType(
    parent=server.objectsNode,
    browseName="Rig-01",
    values={"state": int(test_rig.RigState.RUNNING)},
)

print(rig.state())                      # 1
rig.temperature(23.5)                   # Write the variable.
rig.temperature.engineeringUnits("degC")
print(rig.temperature.engineeringUnits())  # Read its property.
```

Instantiating `TestRigType` creates the object and its declared subtree in the
server's address space. The resulting Python attributes refer to live nodes,
so reads and writes use the same syntax as client-side access. Call
`server.stop()` at the end of the session.

The distinction between a type and an instance is visible here: `TestRigType`
defines a reusable interface, while `Rig-01` is one instance with live values.
The same type could describe several rigs, or a physical apparatus and its
simulation. When a model also declares structured data types, importing the
module in a client makes received structures available as those Python
classes, preserving the shared data definitions on both sides of the exchange.

## Runtime and build requirements

- **Python:** CPython 3.11–3.14, standard GIL build.
- **Runtime dependency:** NumPy ≥ 2.0 and < 3.
- **Platforms:** Linux, macOS, and Windows on x86-64 or ARM64.
- **Source build:** a C toolchain, CMake, Python development headers, and
  OpenSSL development libraries. The Debian/Ubuntu package list and submodule
  setup are given in [Install from source](#install-from-source).
- **Python build dependencies:** setuptools ≥ 65.4.1, wheel, Cython ≥ 3.0,
  packaging, and NumPy ≥ 2.0 and < 3, as declared in `pyproject.toml`.

The AGPL distribution is built locally. The platform floors listed for the
commercial wheels (glibc ≥ 2.28 on Linux, macOS ≥ 15, and Windows 10 LTSC 2021 /
Server 2022 or newer) describe those prebuilt artifacts; source builds also
depend on the available compiler and system libraries. The installation recipe
above covers Debian and Ubuntu.

## Documentation and licensing

The [full documentation](https://docs.o6-automation.com/o6-python/) covers the
API, information modeling, security configuration, and further examples.

o6\Python is dual-licensed. The
[AGPL source distribution](https://github.com/o6-automation/o6-python-agpl)
is available under AGPL-3.0-or-later and has no Credential requirement or Script
Mode timer. The commercial PyPI distribution uses a separate licensing model;
see [commercial build documentation](https://docs.o6-automation.com/o6-python/home/commercial-build/).
For a research or education license, contact
[o6 Automation](https://www.o6-automation.com/contact).

o6\Python is developed and maintained by
[o6 Automation](https://www.o6-automation.com/). Training, long-term support, and
certification assistance are available through
[contact@o6-automation.com](mailto:contact@o6-automation.com).
