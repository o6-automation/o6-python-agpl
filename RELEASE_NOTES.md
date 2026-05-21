# Release Notes

## 1.0.6 (unreleased)

### Breaking Changes

- `o6.ns.<ns>.datatypes.<X>()` now **instantiates** the concrete datatype. 

    | | returns |
    | --- | --- |
    | `o6.ns.ns0.datatypes.BaseDataType.Number.Integer.Int32()` | `numpy.int32(0)` |
    | `o6.ns.ns0.datatypes.BaseDataType.Structure.Argument()` | `o6.Argument` |

    To obtain the NodeId, use `o6.NodeId(o6.ns.<ns>.datatypes.<X>)`. 
    Abstract datatypes (e.g. `BaseDataType`, `Number`, `Integer`) will throw when tried to instantiate.

### New Features

- OPC UA Browser, now built in feature of the `o6.Client` available through `client.browse_interactive`
- Cleaned up Client API
    * removed `client.fully_connected`, `client.connected` is now only true when there's a secure channel and a session
    * removed `client.disconnect_secure_channel` in favor of client.disconnect function parameters `close_session` and `delete_subscriptions`
    * added range parameter for `client.read` and `client.write`, that lets one read into a slice of an array variable with e.g. "1:10"
    * StatusCode is now a proper Python `IntFlag` with full bitwise support:
        ```python
        if o6.StatusCode.Bad in status_code:
            #...

        my_status_code = o6.StatusCode.Good | o6.StatusCode.UncertainLastUsableValue
        ```
    * added support for browse continuation point, i.e. `client.browse` now guarantees to return the complete list of references
    * cleand up and simplified history access through the client
    * revised `client.add_*_node` function parameters, added useful default values for 
        + `parent_reference` - `o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent`
        + `type_definition` - `o6.ns.ns0.vartypes.BaseVariableType.BaseDataVariableType`
    * added callbacks for subscriptions
        + `on_created` - fires when this subscription was created on the server
        + `on_status_changed` - fires when the server reports a status change for this subscription (e.g. keepalive timeout exceeded, session transfer on reconnect), receives the new `StatusCode`
        + `on_deleted` - fires when this subscription was deleted on the server
    * added callbacks for monitored item
        + `on_created` - fires when this monitored item was created on the server
        + `on_deleted` - fires when this monitored item was deleted on the server

### Bug Fixes

