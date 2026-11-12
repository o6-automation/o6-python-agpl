# Aggregation server

This example demonstrates an aggregation server: two independent source OPC UA
servers each publish a custom struct value that is updated in a background
thread. The aggregator server connects to both sources as a client, reads their
changing values, and exposes them as a combined aggregated payload.

The custom struct types are defined in the NodeSet2 XML files next to
`server.py` (`position2d_nodeset2.xml`, `direction2d_nodeset2.xml`,
`matrix3d_nodeset2.xml`). `o6` does not parse nodeset XML at runtime, so each
one is compiled ahead of time into a Python package (`position2d/`,
`direction2d/`, `matrix3d/`) with the `o6-ncc` compiler (`pip install o6-ncc`);
`server.py` imports those packages and publishes them with `server.ns.append(...)`.
Regenerate them after editing an XML file, e.g.:

```bash
pyncc examples/advanced_applications/aggregation_server/position2d_nodeset2.xml \
    --shortname position2d \
    -e ns0 \
    -o examples/advanced_applications/aggregation_server
```

Run the example directly (it locates its generated packages next to itself,
so it must be run as a script, not with `python -m`):

```bash
python examples/advanced_applications/aggregation_server/server.py
```
