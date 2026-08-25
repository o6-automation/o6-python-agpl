import o6
import numpy as np
import socket
import time
from o6 import Client, Server


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


PORT = get_free_port()

server = Server(port=PORT)

server.ns.append(o6.ns.di)

# ---------------------------------------------------------------------------
# Variables — created live on the server via ``server.addVariable(...)``.
# (The old imperative ``o6.variable(...)`` decorator was removed in Tier 4;
# for declarative authoring in a nodeset module, call its type marker.)
# ---------------------------------------------------------------------------

# Read/write scalar under the Objects folder.
counter = server.addVariable("counter", server.objectsNode, 0, writable=True)
# Read-only scalar.
server.addVariable("pi", server.objectsNode, 3.14, writable=False)
# In namespace index 2.
greeting = server.addVariable("greeting", server.objectsNode, "hello o6", ns=2)

print(f"counter  NodeId : {counter.nodeId}  browseName={counter._browse_name}")
print(f"greeting NodeId : {greeting.nodeId}  browseName={greeting._browse_name}")

# ---------------------------------------------------------------------------
# Custom DataTypes — `@o6.datatype(...)`.
# ---------------------------------------------------------------------------


mytypes = o6.ns.make_namespace("http://example.org/MyTypes/", shortname="mytypes", version="1.0")


@o6.datatype(ns=mytypes)
class Point:
    x: float
    y: float
    label: str = "origin"


@o6.datatype(ns=o6.ns.mytypes)
class Reading:
    label: str
    samples: list[o6.Double] = o6.field(description="window of recent samples")
    point: Point  # reference to another class in the same namespace


@o6.datatype(ns=o6.ns.mytypes)
class Device:
    name: str
    health: o6.ns.di.datatypes.DeviceHealthEnumeration


# Demonstrates explicit `nodeid`, `browsename`, and every FieldSpec property.
# `browsename` sets the UA node's QualifiedName (defaults to the class name).
# `nodeid` pins the DataType node to a known address; the binary-encoding
# node is automatically placed at i=5002.
@o6.datatype(
    ns=mytypes,
    browseName="SensorCfg",  # UA browse name — intentionally differs from the Python class name
    nodeId="ns=1;i=5001",  # explicit NodeId; encoding node gets i=5002
)
class SensorConfig:
    name: str = o6.field(maxStringLength=64, description="human-readable sensor name")
    channels: list[float] = o6.field(description="four ADC channel readings", arrayDimensions=[4])
    firmware: str = o6.field(description="firmware version tag", isOptional=True)

    def __init__(self, name: str, channels: list[float], firmware: str | None = None):
        self.name = name
        self.channels = channels
        self.firmware = firmware


print(f"mytypes  metadata : {mytypes.metadata}")

# Add python declared datatypes to the server
server.ns.append(mytypes)
origin = Point()
origin.x = 1.0
origin.y = 2.0
origin.label = "unit"
origin_var = server.addVariable(
    "Origin",
    server.objectsNode,
    origin,
)
print(f"origin   NodeId : {origin_var.nodeId}  dataType=Point")

reading = Reading()
reading.label = "first"
reading.samples = [0.1, 0.2, 0.3]
reading.point = Point()
reading.point.x = 3.0
reading.point.y = 4.0
reading.point.label = "nested"
reading_var = server.addVariable(
    "LatestReading",
    server.objectsNode,
    reading,
)
print(f"reading  NodeId : {reading_var.nodeId}  dataType=Reading")

device = Device()
device.name = "pump-1"
device.health = o6.ns.di.datatypes.DeviceHealthEnumeration.NORMAL
device_var = server.addVariable(
    "Device1",
    server.objectsNode,
    device,
)
print(f"device   NodeId : {device_var.nodeId}  dataType=Device")

cfg = SensorConfig()
cfg.name = "temp-sensor-01"
cfg.channels = [1.1, 2.2, 3.3, 4.4]
cfg.firmware = "v1.2.3"
cfg_var = server.addVariable("SensorConfig1", server.objectsNode, cfg)
print(f"cfg      NodeId : {cfg_var.nodeId}  dataType=SensorConfig (browseName='SensorCfg')")


# ---------------------------------------------------------------------------
# Methods — `server.addMethod(name, parent, callback, ...)`.
# ---------------------------------------------------------------------------

calc = server.addObject("Calc", server.objectsNode)
print(f"calc     NodeId : {calc.nodeId}  browseName={calc._browse_name}")


# Simple no-argument no-return method.
# No output values are required here; the client receives only the StatusCode.
def greet(node):
    print("[server] greet() called")
    return (o6.StatusCode.GOOD,)


greet = server.addMethod("greet", calc, greet)


def add_values(node, a, b):
    return (o6.StatusCode.GOOD, a + b)


add = server.addMethod(
    "Add",
    calc,
    add_values,
    inputArgs=[
        ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
        ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
    ],
    outputArgs=[
        ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
    ],
)

_running_total: list[float] = [0.0]


def accumulate(node, delta):
    _running_total[0] += delta
    return (o6.StatusCode.GOOD, _running_total[0])


accumulate = server.addMethod(
    "accumulate",
    calc,
    accumulate,
    inputArgs=[
        ns0.datatypes.Argument(name="Delta", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="RunningTotal", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR
        )
    ],
)


# `async def` callbacks work too — anything you can `await` on the
# server's event loop is fair game (e.g. `await server.read(...)`).
import asyncio


async def ping_server_side_state(node):
    # Yield once to give the event loop a chance to schedule, then read
    # the live value of `counter` and return it.  Note the `await` is
    # required because `Server.read` is async.
    await asyncio.sleep(0)
    current = await server.read(counter.nodeId)
    return (o6.StatusCode.GOOD, float(current))


ping_server_side_state = server.addMethod(
    "ping_server_side_state",
    calc,
    ping_server_side_state,
    inputArgs=[],
    outputArgs=[
        ns0.datatypes.Argument(name="Echo", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
    ],
)


server.start()
print(f"\nServer listening on opc.tcp://localhost:{PORT}")
time.sleep(0.1)

# ---------------------------------------------------------------------------
# Client side: connect, read/write variables, and call methods.
# ---------------------------------------------------------------------------

client = Client(f"opc.tcp://localhost:{PORT}")
client.connect()

print("\nInitial values:")
print(f"  counter  = {client.read(counter.nodeId)!r}")
print(f"  greeting = {client.read(greeting.nodeId)!r}")

client.write(counter.nodeId, 42)
print(f"\nAfter client.write(counter, 42):  counter = {client.read(counter.nodeId)!r}")

# ------------------- methods -------------------
print("\nMethod calls:")

# greet() — no inputs, no outputs -> 1-tuple of just StatusCode.
(status,) = client.call(calc.nodeId, greet.nodeId, [])
print(f"  greet()             -> status={int(status):#x}")

# Add(a, b) -> Sum
status, sum_ = client.call(calc.nodeId, add.nodeId, [o6.Double(17.0), o6.Double(25.0)])
print(f"  Add(17, 25)         -> status={int(status):#x} sum={sum_!r}")

# accumulate(Delta) -> RunningTotal  (state lives on the server in a closure)
status, total1 = client.call(calc.nodeId, accumulate.nodeId, [o6.Double(3.5)])
print(f"  accumulate(3.5)     -> status={int(status):#x} running={total1!r}")
status, total2 = client.call(calc.nodeId, accumulate.nodeId, [o6.Double(2.5)])
print(f"  accumulate(2.5)     -> status={int(status):#x} running={total2!r}")

# ping_server_side_state() — async def callback, returns the live counter.
status, echo = client.call(calc.nodeId, ping_server_side_state.nodeId, [])
print(f"  ping_server_side_*  -> status={int(status):#x} echo={echo!r}")


# ------------------- custom datatypes -------------------

# why does this work after connect?
client.ns.append(mytypes)

# Read back the Point we published.  The client's namespace mapping
# resolves the server-side NodeId and returns an instance of the
client_origin = client.read(origin_var.nodeId)
print(f"\nCustom-typed readback:")
print(f"  Origin        = {client_origin!r}")
print(f"  type(Origin)  = {type(client_origin).__name__}")
print(f"  Origin.x      = {client_origin.x}")
print(f"  Origin.y      = {client_origin.y}")
print(f"  Origin.label  = {client_origin.label!r}")

client_reading = client.read(reading_var.nodeId)
print(f"  LatestReading = {client_reading!r}")
print(f"  Reading.samples = {client_reading.samples!r}")
print(f"  Reading.point.x = {client_reading.point.x}")
print(f"  Reading.point.y = {client_reading.point.y}")
print(f"  Reading.point.label = {client_reading.point.label!r}")

# Read the Device back; the health field comes back as the DI enum
# instance, confirming the cross-namespace reference round-trips.
client_device = client.read(device_var.nodeId)
print(f"  Device1      = {client_device!r}")
print(f"  type(health) = {type(client_device.health).__name__}")
print(f"  Device.health = {int(client_device.health)}")

client_cfg = client.read(cfg_var.nodeId)
print(f"  SensorConfig  = {client_cfg!r}")
print(f"  cfg.name      = {client_cfg.name!r}")
print(f"  cfg.channels  = {client_cfg.channels!r}")
print(f"  cfg.firmware  = {client_cfg.firmware!r}")


## Verbose dump of the Python-side StructureDescription that was registered
## for SensorConfig.  This shows every FieldSpec property (description,
## is_optional, array_dimensions, max_string_length) and the resolved UA
## DataType NodeId for each field.
# print("\nSensorConfig struct metadata:")
# sc_desc = next(sd for sd in SensorConfig._ns._structure_descriptions if sd.name.name == "SensorCfg")
# print(f"  type nodeid  : {sc_desc.dataTypeId}")
# print(f"  browse name  : {sc_desc.name}")
# for f in sc_desc.structureDefinition.fields:
#    parts = [f"dataType={f.dataType}", f"valueRank={f.valueRank}"]
#    try:
#        raw = f.description
#        desc = raw.text if hasattr(raw, "text") else str(raw)
#        if desc:
#            parts.append(f"description={desc!r}")
#    except Exception:
#        pass
#    if f.isOptional:
#        parts.append("is_optional=True")
#    try:
#        dims = list(f.arrayDimensions) if f.arrayDimensions else None
#        if dims:
#            parts.append(f"arrayDimensions={dims}")
#    except Exception:
#        pass
#    try:
#        if f.maxStringLength:
#            parts.append(f"max_string_length={f.maxStringLength}")
#    except Exception:
#        pass
#    print(f"    {f.name!r:<14} : {', '.join(parts)}")

# ------------------- discovery -------------------


from o6.ns import ns0

mask = (
    ns0.datatypes.BrowseResultMask.BROWSE_NAME
    | ns0.datatypes.BrowseResultMask.NODE_CLASS
    | ns0.datatypes.BrowseResultMask.TYPE_DEFINITION
)
refs = client.browse(
    server.objectsNode,
    nodeClassMask=ns0.datatypes.NodeClass.VARIABLE,
    resultMask=mask,
)
print("\nVariables in Objects folder:")
for ref in refs:
    name = ref.browseName.name
    if name not in ["counter", "greeting", "pi"]:
        continue
    val = client.read(ref.nodeId)
    print(f"  {name:<10} browseName={str(ref.browseName):<22}  value={val!r}")

pi_ref = next(r for r in refs if r.browseName.name == "pi")
status = client.write(pi_ref.nodeId, 2.71)
print(f"\nWrite to read-only 'pi' returned status: {int(status):#x}")

client.disconnect()
server.stop()

print("\nDone.")
