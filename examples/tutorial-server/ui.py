#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""Curses dashboard for the distilling-system simulator.

This script imports ``sim`` as a library and calls
``sim.get_state()`` on every tick. The sim library is responsible
for publishing state to shared memory; this script is a pure
read-only viewer.

The sim runs in the server's process (or, in dev mode, in
whatever process invoked sim.start()). The UI is a separate
process; it never starts the sim itself.

Press ``q`` to quit.
"""

import curses
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim

# Poll cadence for redraws.
WAIT_INTERVAL = 0.5
TICK_INTERVAL = 0.1

# State -> human-readable label and a color pair index (set up in main())
STATE_LABELS = {
    "Idle": ("IDLE", None),
    "Filling": ("FILLING", None),
    "Heating": ("HEATING", None),
    "Distilling": ("DISTILLING", 2),
    "Draining": ("DRAINING", 3),
}


def draw_bar(width: int, pct: float) -> tuple[str, str]:
    """Return (bar, label) for a progress bar of given width."""
    pct = max(0.0, min(100.0, pct))
    filled = int(round(width * pct / 100.0))
    bar = "[" + "#" * filled + "-" * (width - filled) + "]"
    label = f" {pct:5.1f}%"
    return bar, label


def render(stdscr, state: dict) -> None:
    stdscr.erase()
    maxy, maxx = stdscr.getmaxyx()
    safe_maxx = maxx - 1
    if maxy < 18 or maxx < 60:
        stdscr.addnstr(0, 0, "screen too small", safe_maxx)
        stdscr.refresh()
        return

    title = f" Automated Distilling System  -  batch #{state['cycle']} "
    stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
    stdscr.addnstr(0, 0, title.ljust(safe_maxx), safe_maxx)
    stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)

    state_name = state["state"]
    state_text, state_color = STATE_LABELS.get(state_name, (state_name, None))
    stdscr.addstr(2, 2, "State: ")
    state_attr = curses.A_BOLD if state_name != "Idle" else curses.A_DIM
    if state_color is not None:
        state_attr |= curses.color_pair(state_color)
    stdscr.attron(state_attr)
    stdscr.addstr(2, 9, state_text)
    stdscr.attroff(state_attr)

    op = state["operating"]
    stdscr.addstr(2, 25, "Operating: ")
    stdscr.attron(curses.color_pair(4 if op else 3) | curses.A_BOLD)
    stdscr.addstr(2, 36, "ON " if op else "OFF")
    stdscr.attroff(curses.color_pair(4 if op else 3) | curses.A_BOLD)

    y = 4
    stdscr.addstr(y, 2, "Kettle level")
    bar, label = draw_bar(30, state["kettle_level"])
    stdscr.addstr(y, 30, bar)
    stdscr.addstr(y, 30 + len(bar), label)

    y = 5
    stdscr.addstr(y, 2, "Distillate Yield")
    bar, label = draw_bar(30, state["distillate_level"])
    stdscr.addstr(y, 30, bar)
    stdscr.addstr(y, 30 + len(bar), label)

    y = 7
    setpoint = state["setpoint"]
    temp = state["kettle_temp"]
    stdscr.addstr(y, 2, f"Kettle temp:  {temp:6.1f} C   (setpoint {setpoint:.1f} C)")

    scale_width = 40
    temp_clamped = max(0.0, min(120.0, temp))
    setpoint_pos = int(scale_width * setpoint / 120.0)
    temp_pos = int(scale_width * temp_clamped / 120.0)

    y = 8
    scale = "0" + "-" * (scale_width - 2) + "120 C"
    stdscr.addstr(y, 2, scale)

    y = 9
    line = [" "] * scale_width
    line[setpoint_pos] = "|"
    stdscr.addstr(y, 2, "setpoint ")
    stdscr.addstr(y, 2 + 9, "".join(line))

    y = 10
    line = [" "] * scale_width
    line[temp_pos] = "x"
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(y, 2, "actual   ")
    stdscr.addstr(y, 2 + 9, "".join(line))
    stdscr.attroff(curses.A_BOLD)

    y = 12
    stdscr.addstr(y, 2, "Actuators:")

    def actuator(y, name, on):
        stdscr.addstr(y, 4, f"  {name:<14}")
        stdscr.attron(curses.color_pair(4 if on else 1) | curses.A_BOLD)
        stdscr.addstr(y, 20, "[ ON ]" if on else "[OFF ]")
        stdscr.attroff(curses.color_pair(4 if on else 1) | curses.A_BOLD)

    actuator(13, "Fill valve", state["fill_valve"])
    actuator(14, "Drain valve", state["drain_valve"])
    actuator(15, "Heater", state["heater"])

    footer = " q: quit "
    stdscr.attron(curses.A_REVERSE)
    stdscr.addnstr(maxy - 1, 0, footer.ljust(safe_maxx), safe_maxx)
    stdscr.attroff(curses.A_REVERSE)

    stdscr.refresh()


def main(stdscr) -> None:
    curses.curs_set(0)
    stdscr.nodelay(True)

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, -1, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_RED, -1)
    curses.init_pair(4, curses.COLOR_GREEN, -1)

    last_signature = None
    while True:
        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            break

        state = sim.get_state()
        if state is None:
            stdscr.erase()
            stdscr.addnstr(0, 0, " Automated Distilling System ", max(0, curses.COLS - 1))
            stdscr.addstr(2, 2, "waiting for sim to start...")
            stdscr.addstr(4, 2, "(start the server with --sim)")
            stdscr.refresh()
            time.sleep(WAIT_INTERVAL)
            continue

        signature = (
            state["state"],
            round(state["kettle_level"], 1),
            round(state["kettle_temp"], 1),
            round(state["distillate_level"], 1),
            state["fill_valve"],
            state["drain_valve"],
            state["heater"],
            state["operating"],
            state["cycle"],
        )
        if signature != last_signature:
            render(stdscr, state)
            last_signature = signature

        time.sleep(TICK_INTERVAL)


if __name__ == "__main__":
    curses.wrapper(main)
