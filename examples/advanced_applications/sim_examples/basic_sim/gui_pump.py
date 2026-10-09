#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk

# constants

INITIAL_TANK_LEFT = 50.0
INITIAL_TANK_RIGHT = 100.0
tank_left = INITIAL_TANK_LEFT
tank_right = INITIAL_TANK_RIGHT
tank_capacity = 150.0
flow_constant = 3.0


# --- GUI Setup ---
root = tk.Tk()
root.title("Pump Simulation")

canvas = tk.Canvas(root, width=520, height=320, bg="white")
canvas.pack()

COLOR_ON = "green3"
COLOR_OFF = "gray60"

s = None
pump_li_open = None
pump_lo_open = None
pump_ri_open = None
pump_ro_open = None
pump_c_open = None
dt = 1.0
_syncing_from_server = False
reset_button = None

# --- Pump changes ---


def on_scale_change(_=None):
    global pump_li_open, pump_lo_open, pump_ri_open, pump_ro_open, pump_c_open
    if s is None:
        return
    if _syncing_from_server:
        return
    s.write(pump_li_open, float(scale_li.get())).check()
    s.write(pump_lo_open, float(scale_lo.get())).check()
    s.write(pump_ri_open, float(scale_ri.get())).check()
    s.write(pump_ro_open, float(scale_ro.get())).check()
    s.write(pump_c_open, float(scale_c.get())).check()
    refresh_controls()
    draw_system()


def reset_tank_levels():
    global tank_left, tank_right

    tank_left = INITIAL_TANK_LEFT
    tank_right = INITIAL_TANK_RIGHT
    if pump_li_open is not None:
        refresh_controls()
        draw_system()


controls = tk.Frame(root)
controls.pack(fill="x", padx=6, pady=4)

lbl_li = tk.Label(controls, text="")
lbl_li.pack(side="left", padx=(2, 0))
scale_li = tk.Scale(
    controls,
    from_=0.0,
    to=1.0,
    resolution=0.05,
    orient="horizontal",
    length=100,
    command=on_scale_change,
)
scale_li.pack(side="left", padx=2)

lbl_lo = tk.Label(controls, text="")
lbl_lo.pack(side="left", padx=(8, 0))
scale_lo = tk.Scale(
    controls,
    from_=0.0,
    to=1.0,
    resolution=0.05,
    orient="horizontal",
    length=100,
    command=on_scale_change,
)
scale_lo.pack(side="left", padx=2)

lbl_ri = tk.Label(controls, text="")
lbl_ri.pack(side="left", padx=(8, 0))
scale_ri = tk.Scale(
    controls,
    from_=0.0,
    to=1.0,
    resolution=0.05,
    orient="horizontal",
    length=100,
    command=on_scale_change,
)
scale_ri.pack(side="left", padx=2)

lbl_ro = tk.Label(controls, text="")
lbl_ro.pack(side="left", padx=(8, 0))
scale_ro = tk.Scale(
    controls,
    from_=0.0,
    to=1.0,
    resolution=0.05,
    orient="horizontal",
    length=100,
    command=on_scale_change,
)
scale_ro.pack(side="left", padx=2)

lbl_c = tk.Label(controls, text="")
lbl_c.pack(side="left", padx=(8, 0))
scale_c = tk.Scale(
    controls,
    from_=-1.0,
    to=1.0,
    resolution=0.05,
    orient="horizontal",
    length=100,
    command=on_scale_change,
)
scale_c.pack(side="left", padx=2)

reset_button = tk.Button(
    controls, text="Reset Levels", command=reset_tank_levels, state=tk.DISABLED
)
reset_button.pack(side="left", padx=(12, 2))


def set_scales_to_pump_values():
    global _syncing_from_server

    if pump_li_open is None:
        return

    _syncing_from_server = True
    try:
        # Pull current server-side values so the GUI reflects external client writes.
        scale_li.set(pump_li_open())
        scale_lo.set(pump_lo_open())
        scale_ri.set(pump_ri_open())
        scale_ro.set(pump_ro_open())
        scale_c.set(pump_c_open())
    finally:
        _syncing_from_server = False


def initialize_from_server(server, li, lo, ri, ro, c, dt_value):
    global s, pump_li_open, pump_lo_open, pump_ri_open, pump_ro_open, pump_c_open, dt
    s = server
    pump_li_open = li
    pump_lo_open = lo
    pump_ri_open = ri
    pump_ro_open = ro
    pump_c_open = c
    dt = dt_value
    reset_button.config(state=tk.NORMAL)
    set_scales_to_pump_values()


def refresh_controls():
    lbl_li.config(text=f"Input L {pump_li_open():.2f}")
    lbl_lo.config(text=f"Output L {pump_lo_open():.2f}")
    lbl_ri.config(text=f"Input R {pump_ri_open():.2f}")
    lbl_ro.config(text=f"Output R {pump_ro_open():.2f}")
    lbl_c.config(text=f"Central {pump_c_open():.2f}")


# --- Draw Tanks, Pipes, and Pumps ---
def draw_system():
    canvas.delete("all")

    # Tanks with border
    left_height = (tank_left / tank_capacity) * 200
    canvas.create_rectangle(80, 60, 180, 260, outline="black", width=2)
    canvas.create_rectangle(80, 260 - left_height, 180, 260, fill="blue")
    canvas.create_text(130, 270, text=f"{tank_left:.1f} L")

    right_height = (tank_right / tank_capacity) * 200
    canvas.create_rectangle(340, 60, 440, 260, outline="black", width=2)
    canvas.create_rectangle(340, 260 - right_height, 440, 260, fill="blue")
    canvas.create_text(390, 270, text=f"{tank_right:.1f} L")

    # Inflow left (top)
    color_li = COLOR_ON if pump_li_open() > 0 else COLOR_OFF
    canvas.create_line(60, 30, 133, 30, width=6, fill=color_li)
    canvas.create_line(130, 30, 130, 60, width=6, fill=color_li, arrow=tk.LAST)

    # Outflow left (bottom)
    color_lo = COLOR_ON if pump_lo_open() > 0 else COLOR_OFF
    canvas.create_line(110, 240, 50, 240, width=6, fill=color_lo, arrow=tk.LAST)

    # Inflow right (top)
    color_ri = COLOR_ON if pump_ri_open() > 0 else COLOR_OFF
    canvas.create_line(460, 30, 387, 30, width=6, fill=color_ri)
    canvas.create_line(390, 30, 390, 60, width=6, fill=color_ri, arrow=tk.LAST)

    # Outflow right (bottom)
    color_ro = COLOR_ON if pump_ro_open() > 0 else COLOR_OFF
    canvas.create_line(410, 240, 470, 240, width=6, fill=color_ro, arrow=tk.LAST)

    # Central pipes
    color_c = COLOR_ON if pump_c_open() != 0 else COLOR_OFF
    canvas.create_rectangle(180, 150, 340, 200, fill=color_c, outline="black", width=1)

    # --- Simulation Step ---


def update_simulation():
    global tank_left, tank_right

    # Keep sliders synchronized with external updates coming from OPC UA clients.
    set_scales_to_pump_values()

    # Inflow pumps fill tanks
    inflow_left = flow_constant * pump_li_open()
    inflow_right = flow_constant * pump_ri_open()
    tank_left = min(tank_left + inflow_left * dt, tank_capacity)
    tank_right = min(tank_right + inflow_right * dt, tank_capacity)

    # Outflow pumps empty tanks
    out_left = min(flow_constant * pump_lo_open() * dt, tank_left)
    out_right = min(flow_constant * pump_ro_open() * dt, tank_right)
    tank_left -= out_left
    tank_right -= out_right

    if pump_c_open() > 0:
        flow = min(flow_constant * pump_c_open() * dt, tank_left)
        tank_left -= flow
        tank_right += flow
    elif pump_c_open() < 0:
        flow = min(flow_constant * -pump_c_open() * dt, tank_right)
        tank_right -= flow
        tank_left += flow

    # Prevent tanks from overflowing or underflowing
    tank_left = min(max(tank_left, 0), tank_capacity)
    tank_right = min(max(tank_right, 0), tank_capacity)

    refresh_controls()
    draw_system()
    root.after(500, update_simulation)
