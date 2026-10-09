# Aggregation server

This example demonstrates an aggregation server: two independent source OPC UA
servers each publish a custom struct value that is updated in a background
thread. The aggregator server connects to both sources as a client, reads their
changing values, and exposes them as a combined aggregated payload.

The custom struct types are defined in the NodeSet2 XML files next to
`server.py` (`position2d_nodeset2.xml`, `direction2d_nodeset2.xml`,
`matrix3d_nodeset2.xml`). `o6` does not parse nodeset XML at runtime, so each
one is compiled ahead of time into a Python package (`position2d/`,
`direction2d/`, `matrix3d/`) via `tools.nodeset_compiler.backend_python`;
`server.py` imports those packages and publishes them with `server.ns.append(...)`.
Regenerate them after editing an XML file, e.g.:

```bash
python -m tools.nodeset_compiler.backend_python \
    examples/advanced_applications/aggregation_server/position2d_nodeset2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --shortname position2d \
    --out examples/advanced_applications/aggregation_server/position2d
```

Run the example directly (it locates its generated packages next to itself,
so it must be run as a script, not with `python -m`):

```bash
python examples/advanced_applications/aggregation_server/server.py
```
