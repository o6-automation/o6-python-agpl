# Set the Stage

Every client tutorial talks to the same example server: a small **automated still**, driven by a simulation. This page gets it running on your machine. It is a one-time setup — start the server, leave it running, and work through the [client tutorials](client/index.md) against it.

You do **not** need to understand the server code to follow the client tutorials. It is the stage, not the play. (The server tutorials, when they land, build exactly this server step by step, which is why it comes as two files rather than one.)

## 1. Save both files

The server is split in two: the OPC UA side, and the simulation it reports on.

| File | What it is |
|---|---|
| [`server.py`](server.py) | Builds the address space, then copies simulation state into it ten times a second and picks up client writes. |
| [`sim.py`](sim.py) | The still itself: a state machine with no OPC UA in it at all. `server.py` imports it. |

!!! warning "Both files, same folder"
    `server.py` does `import sim`, so the two have to sit **next to each other** in the same directory. If `sim.py` is missing or somewhere else, you get `ModuleNotFoundError: No module named 'sim'`.

    ```
    my-o6-tutorial/
    ├── server.py
    └── sim.py
    ```

## 2. Run the server

```bash
python server.py
```

```title="Output"
Server running at opc.tcp://localhost:4840
Address space:
  Objects/DistillingSystem/
    Identification/  Name, Manufacturer, ModelNumber
    Status/          State, Cycle, Operating, Setpoint
    Kettle/          Level, Temperature, WashStart
    Distillate/      Level
    Actuators/       FillValve, DrainValve, Heater
    Events/          EventCount, LastEventTime,
                     LastEventMessage, LastEventState
    Methods/         Start, Shutdown

Press Ctrl+C to stop.

  [event] cycle 1: Batch started: filling kettle with wash
  [event] cycle 1: Kettle full: heating wash to setpoint
```

That's it — the tutorials can now connect at `opc.tcp://localhost:4840`. Leave this terminal open and start with [Connect / disconnect](client/100_connect.md).

The simulation runs in a background thread inside this same process, so there is nothing else to start.

!!! info "The trial wheel stops after two hours"
    The evaluation build shuts down after two hours, server and client alike. If the tutorials suddenly stop connecting, check this terminal and start the server again.

Two options are worth knowing about:

```bash
python server.py --sim-speed 10   # ten batches in the time of one
python server.py --port 4841      # listen somewhere else
```

The tutorials all assume `4840`, so if you change the port, change the `endpointUrl` in the snippets to match. Turning the speed up is genuinely useful: at `1.0` a batch takes a couple of minutes, which is a long time to wait for a state change you are trying to watch.

!!! tip "Optional: a terminal dashboard"
    [`ui.py`](ui.py) is a small curses view of the running batch. Save it next to the other two, then either run `python server.py --ui`, or run `python ui.py` in a second terminal while the server runs. It reads the simulation through the shared-memory segment `sim.py` publishes, so all three files need to be in the same folder.

## What it exposes

The server publishes the following nodes under `Objects/`, alongside the standard `Server` object that open62541 adds automatically. The NodeIds are pinned, so they are stable across restarts and the tutorials can hard-code them.

```
Objects/
└── DistillingSystem                            (Object, ns=1;i=1000)
    ├── Identification                          (Object, ns=1;i=1100)
    │   ├── Name            (String, read-only)                 (ns=1;i=1101)
    │   ├── Manufacturer    (String, read-only)                 (ns=1;i=1102)
    │   └── ModelNumber     (String, read-only)                 (ns=1;i=1103)
    ├── Status                                  (Object, ns=1;i=1200)
    │   ├── State           (String, read-only)                 (ns=1;i=1201)
    │   ├── Cycle           (Int32, read-only)                  (ns=1;i=1202)
    │   ├── Operating       (Boolean, writable)                 (ns=1;i=1203)
    │   └── Setpoint        (Double °C, writable)               (ns=1;i=1204)
    ├── Kettle                                  (Object, ns=1;i=1300)
    │   ├── Level           (Double %, read-only)                (ns=1;i=1301)
    │   ├── Temperature     (Double °C, read-only)              (ns=1;i=1302)
    │   └── WashStart       (Double %, read-only)                (ns=1;i=1303)
    ├── Distillate                              (Object, ns=1;i=1400)
    │   └── Level           (Double %, read-only)                (ns=1;i=1401)
    ├── Actuators                               (Object, ns=1;i=1500)
    │   ├── FillValve       (Boolean, read-only)                (ns=1;i=1501)
    │   ├── DrainValve      (Boolean, read-only)                (ns=1;i=1502)
    │   └── Heater          (Boolean, read-only)                (ns=1;i=1503)
    ├── Events                                  (Object, ns=1;i=1600)
    │   ├── EventCount      (Int32, read-only)                  (ns=1;i=1601)
    │   ├── LastEventTime   (DateTime, read-only)               (ns=1;i=1602)
    │   ├── LastEventMessage(String, read-only)                 (ns=1;i=1603)
    │   └── LastEventState  (String, read-only)                 (ns=1;i=1604)
    ├── Start            (Method)                               (ns=1;i=2001)
    └── Shutdown         (Method)                               (ns=1;i=2002)
```

### What the simulation does

Wash goes in, gets heated to the setpoint, vapour turns into spirit on the way through the condenser, the spent wash drains out, and the still goes back to idle to wait for the next batch. Rinse, repeat. `State` walks through `Idle` → `Filling` → `Heating` → `Distilling` → `Draining` and back, and `Cycle` counts completed batches.

A few things worth knowing before you start poking:

- **Mostly read-only.** The only two variables you can write are `Status/Operating` and `Status/Setpoint`, and both feed back into the simulation rather than controlling anything directly: clearing `Operating` parks the still in `Idle` after the current batch, and `Setpoint` moves the temperature at which `Heating` gives way to `Distilling`. The actuators (`FillValve`, `DrainValve`, `Heater`) look tempting — they sound like switches — but they are **not** writable: the simulation drives them itself as part of the batch state machine. If a tutorial tells you to write `Setpoint`, it means it; if it tells you to write `Heater`, it's lying and you should open an issue.
- **Methods.** `Start` acknowledges a start request and returns `Good` — the simulation runs batches on its own, so there is nothing for it to kick off. `Shutdown` stops the server process.
- **Events.** The high-level Server API does not currently expose `UA_Server_createEvent` at the Python level, so the server fakes events with a small "writable event log" pattern: every state transition bumps `EventCount` and rewrites the `Events` sub-object. From a client point of view you treat these exactly like any other monitored variables — the [subscriptions](client/210_subscriptions.md) tutorials show how. When `o6` grows a real event API the server will switch to proper `BaseEventType` notifications behind the scenes, and existing client code will keep working.

## The code

Nothing here is required reading — the download links above are all you need. Each listing is exactly what its download link gives you, so you can also just copy the code straight out of the page.

??? note "server.py — the OPC UA side"

    <!-- BEGIN GENERATED: server.py -->
    ```python title="server.py"
    #!/usr/bin/env python3
    # Copyright 2026 (c) o6 Automation GmbH
    """
    Distilling-System OPC UA Server
    ===============================

    End-to-end example showing how to build an address space
    with the high-level ``o6.Server`` API:

    * Nested object hierarchy (``DistillingSystem`` with six sub-objects)
    * Mixed read-only and writable variables of different data types
    * Two callable methods (``Start`` / ``Shutdown``)
    * A "writable event log" pattern in lieu of proper ``BaseEventType``
      notifications
    * A polling-based update loop that mirrors an external simulation
      into the address space and feeds client writes back into the sim

    This is the server the client tutorials talk to. The simulation itself
    is a separate library (``sim.py``) that runs as a daemon thread in this
    process and publishes its state, so **``sim.py`` has to sit in the same
    folder as this file**. Pair the two with ``ui.py`` for a terminal
    dashboard, or with any OPC UA client.

    Run::

        # Sim in-thread + OPC UA server
        python server.py

        # Add the terminal dashboard as a child process
        python server.py --ui

        # Or split across terminals
        python server.py               # terminal 1
        python ui.py                   # terminal 2

    Connect at ``opc.tcp://localhost:4840``.
    """

    # This file is laid out in five parts:
    #
    # 1. **Imports and constants**:the o6 entry point we use, the sim
    #    library, and the state strings the sim publishes.
    # 2. **Address-space construction**: ``build_address_space`` adds
    #    every node once at startup and returns a dict of
    #    ``VariableNode`` handles for the update loop.
    # 3. **Sim bridge and child helpers**: startup wait, plus
    #    ``spawn_child`` / ``terminate_child`` for the optional UI.
    # 4. **Argument parsing and lifecycle**: ``parse_arguments``,
    #    ``start_sim`` / ``stop_sim``.
    # 5. **Main update loop**: poll the sim, detect client writes,
    #    mirror sim state into OPC UA variables, fire event-log entries.

    from __future__ import annotations

    import argparse
    import contextlib
    import datetime
    import os
    import subprocess
    import sys
    import time

    from o6 import DateTime, Server, StatusCode

    # Sim is a library: the state machine, shared-memory bridge, and
    # thread management live in sim.py. The server starts/stops the
    # sim in-process thread and reads its state via
    # sim.get_state(). The UI is a separate process and
    # reads via the same sim.get_state().
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import sim

    # --- Constants mirrored from sim.py ---------------------------------------

    # ## 1. Process states, polling, and event messages
    #
    # The sim publishes a small set of state strings; we mirror them
    # here so the server can produce human-readable event messages
    # without importing ``sim`` at every callsite. ``POLL_INTERVAL``
    # matches the sim's ``TICK`` (0.1 s) so one server update happens
    # per sim tick at 1.0x speed.

    # Process state strings the sim publishes. Mirrored here so the
    # server can produce human-readable event messages without
    # importing sim at every callsite.
    STATE_IDLE = "Idle"
    STATE_FILLING = "Filling"
    STATE_HEATING = "Heating"
    STATE_DISTILLING = "Distilling"
    STATE_DRAINING = "Draining"

    # Polling interval: how often the server pulls a new sim tick and
    # pushes it into the address space. Matches the sim's TICK (0.1 s)
    # so a 1.0x-speed sim tick becomes a single server update.
    POLL_INTERVAL = 0.1

    # Maximum time to wait for sim.py before giving up.
    SIM_START_TIMEOUT = 30.0

    # Human-readable messages for each state transition. The sim's
    # state machine is a small set, so an explicit dict is the
    # clearest way to document what each transition means.
    STATE_MESSAGES = {
        STATE_FILLING: "Batch started: filling kettle with wash",
        STATE_HEATING: "Kettle full: heating wash to setpoint",
        STATE_DISTILLING: "At setpoint: distilling wash into spirit",
        STATE_DRAINING: "Yield target reached: draining spent wash",
        STATE_IDLE: "Kettle empty: idle, awaiting next batch",
    }


    # --- Address space construction -------------------------------------------

    # ## 2. Address space
    #
    # The high-level API mirrors the address-space tree directly:
    # ``add_object`` creates an ``ObjectNode`` (a folder),
    # ``add_variable`` creates a ``VariableNode`` (a leaf with a
    # value), and ``add_method`` creates a ``MethodNode`` (a
    # callable).
    #
    # Every node has a parent: usually the server's
    # ``objects_node`` for top-level entries, or another
    # ``ObjectNode`` for nested ones.  We pin stable ``nodeid``s
    # (``ns=1;i=...``) for every node so clients can hard-code
    # addresses and survive server restarts.
    #
    # The function returns a dict of ``VariableNode`` handles used by
    # the update loop to push new values without re-browsing.


    def build_address_space(server: Server) -> dict:
        """Build the address space and return handles for the update loop.

        Returns a dict mapping internal names (matching the sim's dict
        keys) to the variable nodes. The update loop uses these to push
        values without having to look them up on every tick.
        """
        sys_obj = server.addObject(
            "DistillingSystem",
            server.objectsNode,
            nodeId="ns=1;i=1000",
        )

        # Identification ----------------------------------------------------
        ident = server.addObject(
            "Identification",
            sys_obj,
            nodeId="ns=1;i=1100",
        )
        server.addVariable(
            "Name",
            ident,
            "Distilling Demo Still",
            nodeId="ns=1;i=1101",
            writable=False,
        )
        server.addVariable(
            "Manufacturer",
            ident,
            "o6 Tutorials",
            nodeId="ns=1;i=1102",
            writable=False,
        )
        server.addVariable(
            "ModelNumber",
            ident,
            "DS-1000",
            nodeId="ns=1;i=1103",
            writable=False,
        )

        # Status ------------------------------------------------------------
        status = server.addObject("Status", sys_obj, nodeId="ns=1;i=1200")
        state_v = server.addVariable(
            "State",
            status,
            STATE_IDLE,
            nodeId="ns=1;i=1201",
            writable=False,
        )
        cycle_v = server.addVariable(
            "Cycle",
            status,
            0,
            nodeId="ns=1;i=1202",
            writable=False,
        )
        operating_v = server.addVariable(
            "Operating",
            status,
            True,
            nodeId="ns=1;i=1203",
            writable=True,
        )
        setpoint_v = server.addVariable(
            "Setpoint",
            status,
            85.0,
            nodeId="ns=1;i=1204",
            writable=True,
        )

        # Kettle -----------------------------------------------------------
        kettle = server.addObject("Kettle", sys_obj, nodeId="ns=1;i=1300")
        kettle_level = server.addVariable(
            "Level",
            kettle,
            0.0,
            nodeId="ns=1;i=1301",
            writable=False,
        )
        kettle_temp = server.addVariable(
            "Temperature",
            kettle,
            20.0,
            nodeId="ns=1;i=1302",
            writable=False,
        )
        kettle_wash = server.addVariable(
            "WashStart",
            kettle,
            0.0,
            nodeId="ns=1;i=1303",
            writable=False,
        )

        # Distillate --------------------------------------------------------
        distillate = server.addObject(
            "Distillate",
            sys_obj,
            nodeId="ns=1;i=1400",
        )
        dist_level = server.addVariable(
            "Level",
            distillate,
            0.0,
            nodeId="ns=1;i=1401",
            writable=False,
        )

        # Actuators --------------------------------------------------------
        actuators = server.addObject(
            "Actuators",
            sys_obj,
            nodeId="ns=1;i=1500",
        )
        fill_v = server.addVariable(
            "FillValve",
            actuators,
            False,
            nodeId="ns=1;i=1501",
            writable=False,
        )
        drain_v = server.addVariable(
            "DrainValve",
            actuators,
            False,
            nodeId="ns=1;i=1502",
            writable=False,
        )
        heater_v = server.addVariable(
            "Heater",
            actuators,
            False,
            nodeId="ns=1;i=1503",
            writable=False,
        )

        # Events -----------------------------------------------------------
        events = server.addObject("Events", sys_obj, nodeId="ns=1;i=1600")
        event_count = server.addVariable(
            "EventCount",
            events,
            0,
            nodeId="ns=1;i=1601",
            writable=False,
        )
        event_time = server.addVariable(
            "LastEventTime",
            events,
            DateTime(datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)),
            nodeId="ns=1;i=1602",
            writable=False,
        )
        event_msg = server.addVariable(
            "LastEventMessage",
            events,
            "",
            nodeId="ns=1;i=1603",
            writable=False,
        )
        event_state = server.addVariable(
            "LastEventState",
            events,
            "",
            nodeId="ns=1;i=1604",
            writable=False,
        )

        # Methods ----------------------------------------------------------
        #
        # ``Start`` and ``Shutdown`` are convenience methods. ``Start`` is
        # a no-op acknowledgement (the server is already running and the
        # sim is autonomous). ``Shutdown`` flips a flag that the main
        # loop checks and exits cleanly on.

        shutdown_requested = {"stop": False}

        def start(node):
            """Acknowledge a client-side start request. No-op at the
            server level: the server is already running. The sim is
            autonomous and cannot be paused from here."""
            return (StatusCode.GOOD,)

        server.addMethod(
            "Start",
            sys_obj,
            start,
            nodeId="ns=1;i=2001",
        )

        def shutdown(node):
            """Schedule a clean shutdown of this server."""
            print("  [Method] Shutdown called -> server will stop", flush=True)
            shutdown_requested["stop"] = True
            return (StatusCode.GOOD,)

        server.addMethod(
            "Shutdown",
            sys_obj,
            shutdown,
            nodeId="ns=1;i=2002",
        )

        return {
            # status (read)
            "state_v": state_v,
            "cycle_v": cycle_v,
            # status (writable, polled for client changes)
            "operating_v": operating_v,
            "setpoint_v": setpoint_v,
            # kettle
            "kettle_level": kettle_level,
            "kettle_temp": kettle_temp,
            "kettle_wash": kettle_wash,
            # distillate
            "distillate_level": dist_level,
            # actuators
            "fill_v": fill_v,
            "drain_v": drain_v,
            "heater_v": heater_v,
            # events
            "event_count": event_count,
            "event_time": event_time,
            "event_msg": event_msg,
            "event_state": event_state,
            # method handle
            "shutdown_requested": shutdown_requested,
        }


    # --- Sim bridge ------------------------------------------------------------
    #
    # The sim lives in this process (a thread, not a subprocess) when
    # ``--sim`` is given. The bridge is a thin wrapper around
    # ``sim.get_state()`` / ``sim.write_state()`` plus a startup wait.

    # ## 3. Sim bridge and child helpers
    #
    # ``wait_for_sim`` blocks until the sim publishes its first state
    # to shared memory (which happens almost immediately when the sim
    # runs in-process; the timeout is mostly defensive). ``spawn_child``
    # and ``terminate_child`` are used by ``--ui`` to attach the curses
    # dashboard in its own process group so a Ctrl+C in the server
    # doesn't kill the UI.


    def wait_for_sim(timeout: float) -> bool:
        """Block until the sim publishes its first state, or timeout.

        Returns True if the sim is up, False on timeout.
        """
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if sim.get_state() is not None:
                return True
            time.sleep(0.2)
        return False


    def spawn_child(
        label: str, args: list[str], quiet: bool = False, env: dict | None = None
    ) -> subprocess.Popen:
        """Start a child process and return the Popen handle.

        The child is detached into its own process group so that a
        Ctrl+C in the parent only affects the parent, not the child.

        If ``quiet`` is True, the child's stdout and stderr are
        redirected to DEVNULL.

        If ``quiet`` is False, the child inherits the parent's
        stdout/stderr. This is the right choice for the UI, which
        must own the terminal to render.
        """
        print(f"  [child] starting {label}: {' '.join(args)}")
        sink = subprocess.DEVNULL if quiet else None
        return subprocess.Popen(
            args,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=sink,
            stderr=sink,
            start_new_session=True,
        )


    def terminate_child(proc: subprocess.Popen | None, label: str, grace: float = 2.0) -> None:
        """Terminate a child process gracefully, then kill if needed."""
        if proc is None or proc.poll() is not None:
            return
        print(f"  [child] stopping {label} (pid={proc.pid})")
        with contextlib.suppress(ProcessLookupError):
            proc.terminate()
        try:
            proc.wait(timeout=grace)
            return
        except subprocess.TimeoutExpired:
            pass
        with contextlib.suppress(ProcessLookupError):
            proc.kill()
        proc.wait()


    # ## 4. Argument parsing and lifecycle
    #
    # ``--sim`` runs the simulator in a background thread in this
    # process (the default for development). ``--ui`` additionally
    # spawns ``ui.py`` as a child process and ties its lifetime to
    # the server. ``--sim-speed`` is a multiplier on the sim's wall
    # clock (``10.0`` runs ten batches in the time of one).


    def parse_arguments() -> argparse.Namespace:
        """Parse command-line arguments and return the Namespace."""
        parser = argparse.ArgumentParser(
            description="OPC UA server for the distilling-system simulator",
        )
        parser.add_argument(
            "--port",
            type=int,
            default=4840,
            help="OPC UA TCP port (default 4840)",
        )
        parser.add_argument(
            "--no-sim",
            dest="sim",
            action="store_false",
            help="don't run the sim here; attach to one already publishing state",
        )
        parser.add_argument(
            "--sim-speed",
            type=float,
            default=1.0,
            help="sim speed factor (only used with --sim, default 1.0)",
        )
        parser.add_argument(
            "--ui",
            action="store_true",
            help="spawn ui.py as a child process and stop it on shutdown",
        )
        args = parser.parse_args()

        # Validate the speed factor before doing anything else
        if args.sim_speed <= 0:
            print(
                f"--sim-speed must be > 0, got {args.sim_speed}",
                file=sys.stderr,
            )
            sys.exit(1)

        return args


    def start_sim(args: argparse.Namespace):
        """Start the sim (in this process) and the UI (as a child).

        Returns the UI child process handle, or None if --ui was not
        requested or no TTY is attached.
        """
        if args.sim:
            sim.start(speed=args.sim_speed, silent=True)

        if not wait_for_sim(SIM_START_TIMEOUT):
            print(f"sim did not publish state within " f"{SIM_START_TIMEOUT:.0f}s; exiting.")
            sim.stop()
            sys.exit(1)


    def stop_sim(ui_proc: subprocess.Popen | None) -> None:
        """Stop the UI child and the in-process sim."""
        terminate_child(ui_proc, "ui.py")
        sim.stop()


    # --- Server main loop ------------------------------------------------------

    # ## 5. Main update loop
    #
    # On every tick (``POLL_INTERVAL`` seconds) the loop does four
    # things:
    #
    # 1. **Detect client writes.** The high-level Python API has no
    #    on-write callback, so we poll the two writable variables and
    #    compare against the value we last wrote. A change is treated
    #    as a client write and pushed into the sim's state dict.
    # 2. **Push any client writes back into the sim** via
    #    ``sim.write_state`` so the sim thread picks them up on its
    #    next tick.
    # 3. **Mirror sim state into OPC UA variables** (only when the
    #    sim's *signature* changed (i.e. any visible field moved)
    #    to avoid spamming subscriptions with updates).
    # 4. **Fire an event-log entry** on every state or cycle change
    #    by bumping ``EventCount`` and writing the message into
    #    ``LastEventMessage``.
    #
    # The ``Shutdown`` method sets ``shutdown_requested['stop']``;
    # the next loop iteration checks it and exits.


    def main() -> None:
        args = parse_arguments()

        start_sim(args)

        server = Server(port=args.port)
        vars = build_address_space(server)

        server.start()

        if not args.ui:
            print(f"Server running at opc.tcp://localhost:{args.port}", flush=True)
            print("Address space:")
            print("  Objects/DistillingSystem/")
            print("    Identification/  Name, Manufacturer, ModelNumber")
            print("    Status/          State, Cycle, Operating, Setpoint")
            print("    Kettle/          Level, Temperature, WashStart")
            print("    Distillate/      Level")
            print("    Actuators/       FillValve, DrainValve, Heater")
            print("    Events/          EventCount, LastEventTime,")
            print("                     LastEventMessage, LastEventState")
            print("    Methods/         Start, Shutdown")
            print()
            print("Press Ctrl+C to stop.\n", flush=True)

        # Track the *value the server last wrote* to each writable
        # variable. Comparing the polled value to this -- rather than to
        # the previously-polled value -- makes the detection immune to
        # the echo of the sim's value back into the variable.
        last_written_operating = vars["operating_v"]()
        last_written_setpoint = vars["setpoint_v"]()

        last_state = None
        last_cycle = -1
        last_signature = None

        try:
            while not vars["shutdown_requested"]["stop"]:
                sim_state = sim.get_state()

                if sim_state is not None:
                    # 1. Detect client writes by polling the writable vars.
                    cur_operating = vars["operating_v"]()
                    cur_setpoint = vars["setpoint_v"]()

                    changed = False
                    if cur_operating != last_written_operating:
                        sim_state["operating"] = bool(cur_operating)
                        last_written_operating = cur_operating
                        changed = True
                        print(f"  [client write] Operating = {cur_operating}", flush=True)
                    if cur_setpoint != last_written_setpoint:
                        sim_state["setpoint"] = float(cur_setpoint)
                        last_written_setpoint = cur_setpoint
                        changed = True
                        print(f"  [client write] Setpoint = {cur_setpoint:.1f} °C", flush=True)

                    # 2. Push the sim state back (with any client writes).
                    if changed:
                        sim.write_state(sim_state)

                    # 3. Mirror sim state into the OPC UA variables.
                    sig = (
                        sim_state["state"],
                        round(sim_state["kettle_level"], 1),
                        round(sim_state["kettle_temp"], 1),
                        round(sim_state["distillate_level"], 1),
                        sim_state["fill_valve"],
                        sim_state["drain_valve"],
                        sim_state["heater"],
                        sim_state["operating"],
                        sim_state["cycle"],
                    )
                    if sig != last_signature:
                        vars["state_v"](sim_state["state"])
                        vars["cycle_v"](int(sim_state["cycle"]))
                        vars["operating_v"](bool(sim_state["operating"]))
                        vars["setpoint_v"](float(sim_state["setpoint"]))
                        vars["kettle_level"](float(sim_state["kettle_level"]))
                        vars["kettle_temp"](float(sim_state["kettle_temp"]))
                        vars["kettle_wash"](float(sim_state["wash_start"]))
                        vars["distillate_level"](float(sim_state["distillate_level"]))
                        vars["fill_v"](bool(sim_state["fill_valve"]))
                        vars["drain_v"](bool(sim_state["drain_valve"]))
                        vars["heater_v"](bool(sim_state["heater"]))
                        # Update the "last written" tracker to the values
                        # we just wrote, so the next iteration's poll
                        # doesn't see them as new client writes.
                        last_written_operating = bool(sim_state["operating"])
                        last_written_setpoint = float(sim_state["setpoint"])
                        last_signature = sig

                    # 4. Fire an event-log entry on state / cycle change.
                    cycle_changed = sim_state["cycle"] != last_cycle
                    state_changed = sim_state["state"] != last_state
                    if state_changed or cycle_changed:
                        last_state = sim_state["state"]
                        last_cycle = sim_state["cycle"]

                        msg = STATE_MESSAGES.get(
                            sim_state["state"],
                            f"state = {sim_state['state']}",
                        )
                        if state_changed:
                            msg = f"cycle {sim_state['cycle']}: " + msg

                        vars["event_count"](vars["event_count"]() + 1)
                        vars["event_time"](
                            DateTime(datetime.datetime.now(datetime.timezone.utc)),
                        )
                        vars["event_msg"](msg)
                        vars["event_state"](sim_state["state"])
                        if not args.ui:
                            print(f"  [event] {msg}", flush=True)

                time.sleep(POLL_INTERVAL)

        except KeyboardInterrupt:
            print("\nShutting down…")
        finally:
            server.stop()
            print("Server stopped.")


    if __name__ == "__main__":
        main()
    ```
    <!-- END GENERATED: server.py -->

??? note "sim.py — the simulation"

    <!-- BEGIN GENERATED: sim.py -->
    ```python title="sim.py"
    #!/usr/bin/env python3
    # Copyright 2026 (c) o6 Automation GmbH
    """Simulation of an automated distilling system.

    This is a library, not a script. Other modules import it and call
    ``sim.start()`` to launch the simulation in a daemon thread, then
    ``sim.get_state()`` to read the current state.

    When the sim runs in a process, it creates a file-backed shared
    memory segment in ``/dev/shm/`` when available, or in the platform's
    temporary directory otherwise, and publishes its path in
    ``shm_name.txt``. Other processes (the UI) can attach to the
    same segment and read the state.

    When ``get_state()`` is called from the same process that called
    ``start()``, it returns the in-memory state directly - no shm
    round-trip. When called from a different process, it reads from
    the published shm segment.

    The simulator is an autonomous state machine. The valves and
    heater are driven by the state machine; clients do not control
    the device directly. The two writable OPC UA variables
    (``Operating``, ``Setpoint``) feed back into the state via
    ``write_state()`` from the server.
    """

    import contextlib
    import mmap
    import os
    import pickle
    import tempfile
    import threading

    NAME_FILE = "shm_name.txt"

    # --- Process states --------------------------------------------------------

    STATE_IDLE = "Idle"
    STATE_FILLING = "Filling"
    STATE_HEATING = "Heating"
    STATE_DISTILLING = "Distilling"
    STATE_DRAINING = "Draining"

    # --- Simulation parameters -------------------------------------------------

    SETPOINT_TEMP = 85.0  # °C, target kettle temperature during distilling
    AMBIENT_TEMP = 20.0  # °C, room temperature
    YIELD_RATIO = 0.12  # fraction of kettle wash that becomes spirit

    # Rates per second of simulation time. With the defaults (TICK=0.1,
    # DT=0.1) the simulation runs in real time.
    FILL_RATE = 5.0  # kettle level %/s while the fill valve is open
    DRAIN_RATE = 10.0  # kettle level %/s while the drain valve is open
    HEAT_RATE = 2.0  # kettle temperature °C/s while the heater is on
    COOL_RATE = 0.5  # kettle temperature °C/s while the heater is off
    SPIRIT_RATE = 0.5  # spirit appearing in the distillate tank, %/s

    # Phase durations
    IDLE_HOLD = 2.0  # seconds of sim time to wait between batches

    # Wall-clock sleep between loop iterations.
    TICK = 0.1

    # Shared-memory segment size. Plenty of room for the pickled state
    # dict; 4 KB is enough to hold thousands of state updates.
    SHM_SIZE = 4096
    # Last 4 bytes of the segment hold the size of the current payload.
    TAIL_BYTES = 4

    # --- Module-level state ----------------------------------------------------
    #
    # These globals hold the sim's runtime state. ``_lock`` guards
    # ``state`` and ``_shm`` for the writer thread and the readers.
    # ``_local`` is True iff this process started the sim itself
    # (vs. just attaching to a shm published by another process).

    _lock = threading.RLock()
    state: dict | None = None
    _stop: threading.Event | None = None
    _thread: threading.Thread | None = None
    _shm: mmap.mmap | None = None
    _shm_fd: int | None = None
    _shm_path: str | None = None
    _local = False


    # --- State machine helpers -------------------------------------------------


    def _new_state() -> dict:
        """Return a fresh state dict in the Idle phase."""
        return {
            "state": STATE_IDLE,
            "kettle_level": 0.0,
            "kettle_temp": AMBIENT_TEMP,
            "fill_valve": False,
            "drain_valve": False,
            "heater": False,
            "distillate_level": 0.0,
            "setpoint": SETPOINT_TEMP,
            "operating": True,
            "wash_start": 0.0,
            "cycle": 0,
        }


    def _transition(s: dict, new_state: str, timer: list[float]) -> None:
        """Enter a new process state and reset its hold timer."""
        s["state"] = new_state
        timer[0] = 0.0
        if new_state == STATE_DISTILLING:
            s["wash_start"] = s["kettle_level"]
        print(f"  -> {new_state}")


    def _step(s: dict, dt: float, timer: list[float]) -> None:
        """Advance the state machine by ``dt`` seconds of sim time."""
        timer[0] += dt

        if s["state"] == STATE_IDLE:
            s["fill_valve"] = False
            s["drain_valve"] = False
            s["heater"] = False
            s["distillate_level"] = 0.0

            if s["kettle_temp"] > AMBIENT_TEMP:
                s["kettle_temp"] = max(
                    AMBIENT_TEMP,
                    s["kettle_temp"] - COOL_RATE * dt,
                )

            if s["operating"] and timer[0] >= IDLE_HOLD:
                s["cycle"] += 1
                _transition(s, STATE_FILLING, timer)

        elif s["state"] == STATE_FILLING:
            s["fill_valve"] = True
            s["drain_valve"] = False
            s["heater"] = False

            s["kettle_level"] = min(
                100.0,
                s["kettle_level"] + FILL_RATE * dt,
            )

            if s["kettle_level"] > 0:
                feed_frac = min(1.0, (FILL_RATE * dt) / s["kettle_level"])
                s["kettle_temp"] = s["kettle_temp"] * (1.0 - feed_frac) + AMBIENT_TEMP * feed_frac

            if s["kettle_level"] >= 100.0:
                _transition(s, STATE_HEATING, timer)

        elif s["state"] == STATE_HEATING:
            s["fill_valve"] = False
            s["drain_valve"] = False
            s["heater"] = True

            s["kettle_temp"] += HEAT_RATE * dt

            # ``setpoint`` is writable over OPC UA, so a client write moves the
            # temperature at which heating gives way to distilling.
            if s["kettle_temp"] >= s["setpoint"]:
                _transition(s, STATE_DISTILLING, timer)

        elif s["state"] == STATE_DISTILLING:
            s["fill_valve"] = False
            s["drain_valve"] = False

            if s["kettle_temp"] < s["setpoint"]:
                s["heater"] = True
                s["kettle_temp"] += HEAT_RATE * dt
            else:
                s["heater"] = False
                s["kettle_temp"] = max(
                    s["setpoint"],
                    s["kettle_temp"] - COOL_RATE * dt,
                )

            spirit = SPIRIT_RATE * dt
            wash_processed = spirit / YIELD_RATIO
            s["kettle_level"] = max(
                0.0,
                s["kettle_level"] - spirit,
            )
            s["distillate_level"] = min(
                100.0,
                s["distillate_level"] + spirit,
            )

            if s["heater"]:
                s["kettle_temp"] -= wash_processed * 0.05

            if s["distillate_level"] >= s["wash_start"] * YIELD_RATIO:
                _transition(s, STATE_DRAINING, timer)

        elif s["state"] == STATE_DRAINING:
            s["fill_valve"] = False
            s["drain_valve"] = True
            s["heater"] = False

            s["kettle_level"] = max(
                0.0,
                s["kettle_level"] - DRAIN_RATE * dt,
            )

            if s["kettle_level"] <= 0.0:
                _transition(s, STATE_IDLE, timer)


    def _publish(s: dict) -> None:
        """Serialize ``s`` into the shared memory segment."""
        raw = pickle.dumps(s)
        if len(raw) > SHM_SIZE - TAIL_BYTES:
            raise RuntimeError(f"state too large: {len(raw)} bytes")
        with _lock:
            if _shm is None:
                return
            _shm.seek(0)
            _shm.write(raw)
            _shm.seek(SHM_SIZE - TAIL_BYTES)
            _shm.write(len(raw).to_bytes(TAIL_BYTES, "little"))


    # --- Public API ------------------------------------------------------------


    def start(speed: float = 1.0, silent: bool = False) -> None:
        """Start the sim in a background thread.

        ``speed`` is a multiplier on simulation time (1.0 = real time).
        ``silent`` suppresses per-tick console output.

        The thread is a daemon: when the host process exits, the thread
        dies with it. The shared memory segment is cleaned up
        explicitly in ``stop()``, or by the OS on the next reboot.
        """
        global _stop, _thread, _shm, _shm_fd, _shm_path, _local, state

        if speed <= 0:
            raise ValueError(f"speed must be > 0, got {speed}")

        with _lock:
            if _thread is not None and _thread.is_alive():
                return  # already running

            # Prefer Linux shared memory, with a portable fallback for
            # platforms such as macOS that do not provide /dev/shm.
            shm_dir = "/dev/shm" if os.path.isdir("/dev/shm") else tempfile.gettempdir()
            fd, path = tempfile.mkstemp(prefix="distill_", dir=shm_dir)
            os.ftruncate(fd, SHM_SIZE)
            mm = mmap.mmap(fd, SHM_SIZE)

            _shm_fd = fd
            _shm_path = path
            _shm = mm
            _local = True
            _stop = threading.Event()
            state = _new_state()

            # Publish the shm path so other processes can attach.
            with open(NAME_FILE, "w") as f:
                f.write(path)

            if not silent:
                print(f"simulator started: {path}  (speed x{speed})")

        def _run():
            dt = speed * TICK
            timer = [0.0]
            try:
                while not _stop.is_set():
                    with _lock:
                        _step(state, dt, timer)
                        _publish(state)
                    _stop.wait(TICK)
            finally:
                with contextlib.suppress(Exception):
                    with _lock:
                        _publish(state)

        t = threading.Thread(target=_run, name="sim-thread", daemon=True)
        t.start()
        _thread = t


    def stop() -> None:
        """Stop the sim thread and release the shared memory segment."""
        global _stop, _thread, _shm, _shm_fd, _shm_path, _local, state

        with _lock:
            if _stop is not None:
                _stop.set()
            if _thread is not None:
                _thread.join(timeout=2.0)
            if _shm is not None:
                with contextlib.suppress(Exception):
                    _shm.close()
                _shm = None
            if _shm_fd is not None:
                with contextlib.suppress(OSError):
                    os.close(_shm_fd)
                _shm_fd = None
            if _shm_path is not None:
                with contextlib.suppress(FileNotFoundError):
                    os.unlink(_shm_path)
                _shm_path = None
            with contextlib.suppress(FileNotFoundError):
                os.remove(NAME_FILE)
            _stop = None
            _thread = None
            _local = False
            state = None


    def get_state() -> dict | None:
        """Return the latest sim state, or None if the sim is not running.

        If the sim is running in this process, returns a shallow copy
        of the in-memory state. If it's running in another process,
        attaches to the published shm and returns a fresh dict.
        """
        with _lock:
            if _local and state is not None:
                return dict(state)

        # Different process: attach to the shm and read.
        try:
            with open(NAME_FILE) as f:
                path = f.read().strip()
        except (OSError, FileNotFoundError):
            return None
        if not path:
            return None

        try:
            fd = os.open(path, os.O_RDONLY)
        except OSError:
            return None
        try:
            mm = mmap.mmap(fd, SHM_SIZE, access=mmap.ACCESS_READ)
            try:
                mm.seek(SHM_SIZE - TAIL_BYTES)
                size_bytes = mm.read(TAIL_BYTES)
                if len(size_bytes) < TAIL_BYTES:
                    return None
                size = int.from_bytes(size_bytes, "little")
                if size <= 0 or size > SHM_SIZE - TAIL_BYTES:
                    return None
                mm.seek(0)
                raw = mm.read(size)
                return pickle.loads(raw)
            finally:
                mm.close()
        except Exception:
            return None
        finally:
            os.close(fd)


    def write_state(new_state: dict) -> None:
        """Replace the sim's current state with ``new_state``.

        Used by the server to push client writes (Operating / Setpoint)
        into the sim thread. No-op if the sim is not running locally.
        """
        with _lock:
            if not _local or state is None:
                return
            for k, v in new_state.items():
                state[k] = v
    ```
    <!-- END GENERATED: sim.py -->

## Where to go next

- [Client tutorials](client/index.md) — start with [Connect / disconnect](client/100_connect.md).
- [Server manual](../manual/server/index.md) — how the server side above actually works.
- [Server tutorials](server/index.md) — coming soon; they will build this server step by step.
