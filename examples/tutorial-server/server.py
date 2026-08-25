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

# BEGIN MD
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
# END MD

from __future__ import annotations

# BEGIN CODE
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

# END CODE

# --- Constants mirrored from sim.py ---------------------------------------

# BEGIN MD
# ## 1. Process states, polling, and event messages
#
# The sim publishes a small set of state strings; we mirror them
# here so the server can produce human-readable event messages
# without importing ``sim`` at every callsite. ``POLL_INTERVAL``
# matches the sim's ``TICK`` (0.1 s) so one server update happens
# per sim tick at 1.0x speed.
# END MD

# BEGIN CODE
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
# END CODE


# --- Address space construction -------------------------------------------

# BEGIN MD
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
# END MD


# BEGIN CODE
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


# END CODE


# --- Sim bridge ------------------------------------------------------------
#
# The sim lives in this process (a thread, not a subprocess) when
# ``--sim`` is given. The bridge is a thin wrapper around
# ``sim.get_state()`` / ``sim.write_state()`` plus a startup wait.

# BEGIN MD
# ## 3. Sim bridge and child helpers
#
# ``wait_for_sim`` blocks until the sim publishes its first state
# to shared memory (which happens almost immediately when the sim
# runs in-process; the timeout is mostly defensive). ``spawn_child``
# and ``terminate_child`` are used by ``--ui`` to attach the curses
# dashboard in its own process group so a Ctrl+C in the server
# doesn't kill the UI.
# END MD


# BEGIN CODE
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


# END CODE


# BEGIN MD
# ## 4. Argument parsing and lifecycle
#
# ``--sim`` runs the simulator in a background thread in this
# process (the default for development). ``--ui`` additionally
# spawns ``ui.py`` as a child process and ties its lifetime to
# the server. ``--sim-speed`` is a multiplier on the sim's wall
# clock (``10.0`` runs ten batches in the time of one).
# END MD


# BEGIN CODE
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


# END CODE

# --- Server main loop ------------------------------------------------------

# BEGIN MD
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
# END MD


# BEGIN CODE
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
# END CODE
