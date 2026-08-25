# write

Canonical path: `o6.write`

`@o6.write` marks an ordinary VariableType instance method as its value-write
implementation. The decorator preserves the method and its Python signature;
subclasses can override it without repeating the decorator.

`@o6.write("member.child")` instead resolves a Python member path when the
containing Object finishes. It stores the implementation and containing Object
on that concrete Variable. The callback receives the requested `DataValue`
plus `range` and `session` keyword arguments.

See [Server callbacks](../server-callbacks.md#one-resolution-rule) for the
shared `read`/`write`/`call` precedence and reset behavior.
