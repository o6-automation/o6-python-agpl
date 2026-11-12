# o6 package

Python API backed by the `o6._o6` extension.

| Module | Responsibility |
| --- | --- |
| `__init__.py` | Public exports, builtin types, decorators |
| `client.py`, `server.py` | Client/server lifecycle and services |
| `node.py`, `_node_backend.py` | Node handles and service adapters |
| `subscription.py` | Subscriptions and monitored items |
| `_declarations.py`, `_decorators.py`, `_references.py` | Portable information-model declarations |
| `_datatype_registration.py` | Python/native datatype registration |
| `_server_types.py`, `_server_construction.py`, `_server_materialization.py` | Server behavior binding and node construction |
| `_history.py`, `_notifications.py`, `pubsub.py` | History, notifications, PubSub runtime hooks |
| `util.py` | Certificates and shared private helpers |
| `ns/` | Namespace registry and generated companion specifications |

```python
import o6

with o6.Client("opc.tcp://localhost:4840") as client:
    namespaces = client.read("i=2255")
    print(namespaces)
```

- Services support synchronous calls and asynchronous use; see [client lifecycle](../docs/manual/client/lifecycle.md).
- Batch operations use `client.read([...])` and `client.write({node: value})`.
- `client.monitor(node, callback)` creates a monitored item; see [subscriptions](../docs/manual/client/subscriptions.md).
- Status failures and return shapes are documented per service; see [address-space operations](../docs/manual/client/read-write-call.md).
- Model declarations and server construction are documented in the [manual](../docs/manual/index.md).
