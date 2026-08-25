# read

Canonical path: `o6.read`

`@o6.read` marks an ordinary VariableType instance method as its value-read
implementation. The decorator preserves the method and its Python signature;
subclasses can override it without repeating the decorator.

`@o6.read("member.child")` instead resolves a Python member path when the
containing Object finishes. It stores the implementation and containing Object
on that concrete Variable. The callback receives `range`, `session`, and
`includeSourceTimestamp` as keyword arguments.

See [Server callbacks](../server-callbacks.md#one-resolution-rule) for the
shared `read`/`write`/`call` precedence and reset behavior.
