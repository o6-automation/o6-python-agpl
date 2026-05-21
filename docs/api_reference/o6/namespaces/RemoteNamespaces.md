# o6.namespaces.RemoteNamespaces

Discovered server-side namespaces accessible after :meth:`discover`.

Call :meth:`discover` on a connected client to browse and build types
for every namespace on the remote server that is not already loaded
locally.  Each discovered :class:`Namespace` is then stored as an
attribute keyed by its *short_name*.

::: o6.namespaces.RemoteNamespaces
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true