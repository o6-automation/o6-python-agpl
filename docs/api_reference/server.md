# Server

Canonical path: `o6.server.Server`

`Server.implement(DeclarationType, ImplementationType)` binds an undecorated
Python behavior subclass to an existing ObjectType or VariableType on one
server. Future instances created through native APIs or AddNodes receive that
implementation without modifying or subclassing the UA information model.
Their implementation-selected children are created before native Mandatory
children, and their normal Python initializer runs once after the complete
subtree exists. Because AddNodes supplies no Python arguments, that initializer
must be callable without required arguments.

::: o6.server.Server
    options:
      show_root_heading: false
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true
      show_symbol_type_heading: true
