# The distillery server

This is the server the tutorials build towards. [Set the stage](../setup.md)
has the runnable version: save `server.py` and `sim.py`, then start it with
`python server.py`. The [client tutorials](../client/index.md) connect to the
same server, so keep it running while you work through either set.

!!! info "Why a separate simulation"
    There is no real distillery to drive, so the server is paired with
    `sim.py`: a small state machine that runs in a background thread and
    publishes the kettle level, temperature, valves, heater, state, cycle
    and event log into the address space. The split keeps the OPC UA code
    and the simulation readable on their own.

The address space is exactly what the earlier tutorials build: the hierarchy
from [Add a hierarchy](105_add-hierarchy.md), the variables from
[Add a variable](110_add-variable.md) and the methods from
[Add a method](120_add-method.md).

Getting values in and out is simpler than in
[Variables with sources](320_variables-with-sources.md) and
[Server callbacks](330_server-callbacks.md). Those pages use read/write
callbacks with `Server.implement(...)` and a periodic tick with
`addRepeatedCallback`, which scale to bigger servers. This server is small
enough to need neither. `server.py` uses plain `writable=True/False`
variables and a hand-written `while` loop (`time.sleep(POLL_INTERVAL)`). The
loop polls the two writable variables for client changes and pushes values
with call syntax (`some_var(new_value)`). The event log uses the
"writable event log" pattern from [Events](340_events.md).

The declared types ([200](200_declare-object-type.md)–[230](230_declare-data-type.md))
and the production topics ([350](350_timers.md), [400](400_access-control-roles.md)–[440](440_history.md))
are not part of this server. It stays small, insecure and unauthenticated:
`server.py`'s only flags are `--port`, `--no-sim`, `--sim-speed` and `--ui`,
none of them security-related. The file also contains CLI argument parsing
and the child-process/UI handling behind `--ui`. No tutorial covers these;
they make the example convenient to run and don't teach an `o6` concept.
