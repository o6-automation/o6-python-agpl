# o6.server

High-level OPC UA Server implementation.

This module provides a pythonic, high-level interface to OPC UA server functionality,
wrapping the low-level _o6 C extension module.

Basic usage:
    from o6 import Server

    server = Server(port=4840)
    with server:
        # Add a variable
        temp = server.add_variable("Temperature", server.objects_node,
                                   value=25.0)
        # Read/write
        print(server.read_value(temp.nodeid))
        server.write(temp.nodeid, 30.0)

::: o6.server
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true