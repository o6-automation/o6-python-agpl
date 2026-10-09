# The distillery server

This is the server the tutorials build towards. The full runnable version —
along with the simulation that drives it — is described in
[Set the stage](../setup.md): the page walks you through saving the two
files (`server.py` and `sim.py`) and starting the server with
`python server.py`. That is also the server the
[client tutorials](../client/index.md) connect to, so it is the one to
keep running while you work through either set.

!!! info "Why a separate simulation"
    We don't have a real distillery to drive, so the server is paired with
    `sim.py`: a small state machine that runs in a background thread and
    publishes the kettle level, temperature, valves, heater, state, cycle,
    and event log into the address space. The two-file split keeps the
    OPC UA side and the simulation side independently readable.

The address space in those two files is exactly what the earlier tutorials
put together — the hierarchy from [Add a hierarchy](105_add-hierarchy.md),
the variables from [Add a variable](110_add-variable.md), and the methods
from [Add a method](120_add-method.md).

Getting values in and out is deliberately simpler than what
[Variables with sources](320_variables-with-sources.md) and
[Server callbacks](330_server-callbacks.md) teach, though. Those pages
install proper read/write callbacks with `Server.implement(...)` and a
periodic tick with `addRepeatedCallback` — real, scalable mechanisms worth
knowing for a bigger server. This particular server is small enough that it
doesn't need either: `server.py` just keeps plain `writable=True/False`
variables and runs a hand-rolled `while` loop (`time.sleep(POLL_INTERVAL)`)
that polls the two writable variables for client-side changes and pushes
values with call-syntax (`some_var(new_value)`). The event log follows the
"writable event log" pattern from [Events](340_events.md).

The declared-type band ([200](200_declare-object-type.md)–[230](230_declare-data-type.md))
and the production band ([350](350_timers.md), [400](400_access-control-roles.md)–[440](440_history.md))
are genuinely useful once a server needs typed models or is exposed on a
real network — but neither is part of this particular reference server.
It stays deliberately small, and deliberately insecure and unauthenticated:
`server.py`'s only flags are `--port`, `--no-sim`, `--sim-speed`, and
`--ui`, with nothing security-related among them, matching what
[Set the stage](../setup.md) hands you. The file also carries a bit of
material no earlier tutorial covers at all — CLI argument parsing and the
child-process/UI orchestration behind `--ui` — which exists to make the
example pleasant to run, not to teach an `o6` concept.

To run it, jump straight to [Set the stage](../setup.md), save the two
files, and run `python server.py` from that folder.
