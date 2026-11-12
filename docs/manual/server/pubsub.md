# PubSub

Configure publisher/subscriber communication through the OPC UA information model.

## PubSub

PubSub has no separate Python configuration API. You configure it through the
standard namespace-zero information model: create `PubSubConnection`,
`WriterGroup`, `DataSetWriter` and reader components as address-space nodes, and
control them with the model's methods. The `o6.pubsub` module adds only the
runtime functions the model cannot express:

```python
import o6.pubsub

o6.pubsub.publish(writerGroup)                   # publish one message now
o6.pubsub.setStateMachine(component, callback)   # custom state transitions
table = o6.pubsub.offsetTable(writerGroup)       # fixed-layout byte offsets
```

`offsetTable` returns the encoded message with typed byte offsets
(`OffsetType`). This enables deterministic, pre-encoded publishing.
`setStateMachine` takes a callable `(current, target) -> (StatusCode, newState)`
and can be called from an implementation class's `__init__`. Disable a component
before you replace its state machine. PubSub requires a build and Credential
with the PubSub feature scope enabled; otherwise these calls raise
`PermissionError`.
