# ObjectType Implementation

The *implementer class* pattern: declare a UA ``ObjectType`` as a
contract, implement its behavior in a separate Python class, and
register that class with ``Server.implement``. Every instance the server
creates for the type then runs your code.

The pattern has three parts:

1. **Declare** a UA ``ObjectType`` (its Methods, Variables, ...) as a pure
   contract with ``@o6.objecttype``. The declaration carries no behavior.
2. **Implement** the contract in a subclass. Python methods decorated
   with ``@o6.call("<BrowseName>")`` implement the declared UA Methods.
   Ordinary instance attributes give each node its own state.
3. **Register** the implementation with ``server.implement(Declaration, Impl)``.
   The server then uses it for every instance of that UA type.

## 1. Declare the namespace and the ObjectType
A custom type needs a namespace. Once registered, the short name
``"tutorial"`` works as the ``ns=`` argument below.

``CounterType`` is an ``ObjectType`` with one ``Increment`` Method. It
takes an ``Int32`` step and returns the running ``Int32`` total. The
method is declared with ``o6.call(...)`` but not implemented: the
class is only the contract.

```python
print("--- 1. Declare the namespace and the ObjectType ---")

o6.ns.namespace(
    shortname="tutorial",
    uri="http://o6-automation.com/UA/Tutorial/",
    version="1.0",
)


@o6.objecttype(ns="tutorial", nodeId="ns=tutorial;i=1", browseName="CounterType")
class CounterType(ns0.objtypes.BaseObjectType):
    """A counter object type — declared only, implemented separately."""

    increment: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=tutorial;Increment",
            inputArgs=[
                ns0.datatypes.Argument(
                    name="step",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="Amount to add to the counter",
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="total",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="The counter value after incrementing",
                )
            ],
        )
    )
```

## 2. Implement the ObjectType
Subclass the declaration and bind Python behavior to the Method with
``@o6.call("Increment")``. The local name is enough: o6 matches it
against the type's declared Methods and resolves it to
``ns=tutorial;Increment``. Pass the fully-qualified BrowseName only
when the name is declared in more than one namespace; o6 rejects an
ambiguous bare name with an error. Each live node is an instance of
this class, so attributes such as ``self._count`` give every Counter
object its own state.

```python
print("\n--- 2. Implement the ObjectType ---")


class CounterImpl(CounterType):
    """Provide the behavior for :class:`CounterType`."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._count = 0

    @o6.call("Increment")
    def _increment(self, step: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        """Add ``step`` to this instance's counter and return the new total."""
        self._count += int(step)
        return (o6.StatusCode.GOOD, o6.Int32(self._count))
```

``Server.ns.append`` learns about a namespace defined in Python from a
module with ``__NAMESPACES__``. A generated NodeSet2 module has the same
shape. The module also exposes the declared type so the server can
publish it.

```python
def _tutorial_module() -> Any:
    import types

    module = types.ModuleType("tutorial_types")
    module.CounterType = CounterType
    module.__NAMESPACES__ = {o6.ns.tutorial}
    return module
```

```python
server = o6.Server(port=EXAMPLE_PORT)
server.ns.append(_tutorial_module())
```

## 3. Register the implementation
``server.implement(CounterType, CounterImpl)`` makes ``CounterImpl``
the Python class for every ``CounterType`` instance.

``addObject()`` with the declaration as type definition then returns
an implementation instance. The call site never names
``CounterImpl``.

```python
print("\n--- 3. Register the implementation ---")
server.implement(CounterType, CounterImpl)

counter = server.addObject(
    "Counter",
    server.objectsNode,
    typeDefinition=CounterType,
    nodeId="ns=tutorial;i=1000",
    ns=o6.ns.tutorial.index,
)
print(f"addObject(typeDefinition=CounterType) -> {type(counter).__name__}")
print(f"  isinstance(counter, CounterImpl) = {isinstance(counter, CounterImpl)}")
```

## 4. Dispatch, in-process and over the wire
Calling the Method attribute (``counter.Increment(...)``) runs the
implementation in-process. An OPC UA client calling the same node goes
through the full service stack. Both routes reach
``CounterImpl._increment`` and share the node's ``_count`` state.

```python
print("\n--- 4. Dispatch, in-process and over the wire ---")
print("In-process calls (counter.Increment):")
print(f"  Increment(5) -> {counter.Increment(o6.Int32(5))}")
print(f"  Increment(3) -> {counter.Increment(o6.Int32(3))}")

server.start()
print(f"Server running at {endpoint_url}")
time.sleep(0.2)

client = o6.Client(endpoint_url)
client.connect()
print("OPC UA client calls (client.call):")
method_id = counter.Increment
print(f"  Increment(10) -> {client.call(counter, method_id, [o6.Int32(10)])}")
print(f"  Increment(1)  -> {client.call(counter, method_id, [o6.Int32(1)])}")
client.disconnect()
server.stop()
```

## Source Code

Download [`S10_implement_objtype.py`](server-S10_implement_objtype/S10_implement_objtype.py) to run it locally.
