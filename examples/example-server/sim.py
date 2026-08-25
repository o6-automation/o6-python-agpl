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

        if s["kettle_temp"] >= SETPOINT_TEMP:
            _transition(s, STATE_DISTILLING, timer)

    elif s["state"] == STATE_DISTILLING:
        s["fill_valve"] = False
        s["drain_valve"] = False

        if s["kettle_temp"] < SETPOINT_TEMP:
            s["heater"] = True
            s["kettle_temp"] += HEAT_RATE * dt
        else:
            s["heater"] = False
            s["kettle_temp"] = max(
                SETPOINT_TEMP,
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
