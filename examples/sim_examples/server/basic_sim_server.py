#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Pump Simulation with a Tkinter GUI
==================================

An interactive OPC UA server that simulates two coupled tanks fed by a
central pump.  The address space exposes five writable float variables
(per-tank inlet/outlet valves plus a central pump).  A small Tkinter
window shows the live tank levels, lets the user drive the valves with
sliders, and advances the simulation at a fixed timestep.

![Pump Simulation](../assets/pump.png)

Connect to this server with any OPC UA client at::

    opc.tcp://localhost:4840
"""

# BEGIN MD
# This example combines the high-level ``o6.Server`` API with a
# desktop GUI: every slider movement is forwarded to the server via
# ``server.write(...)`` and the simulation tick reads the current
# values back through the ``VariableNode.value`` property.  A
# separate ``gui_pump`` module owns the Tkinter side so the address
# space wiring stays readable here.
# END MD

import os
import sys

# Allow running this script directly (``python basic_sim_server.py``)
# by adding the script's own directory to ``sys.path`` before the
# relative-style import of ``gui_pump`` below.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

try:
    from . import gui_pump
except ImportError:  # script executed outside a package
    import gui_pump

from o6.server import Server

# BEGIN MD
# ## 1. Address Space
# Each valve is a plain writable ``Double`` variable.  We pin a
# stable ``nodeid`` (``ns=1;s=...``) so OPC UA clients can hard-code
# the address and survive server restarts.
# END MD

# BEGIN CODE
s = Server(port=4840)

pump_li_open = s.addVariable(
    "pumpLiOpen", s.objectsNode, 0.0, nodeId="ns=1;s=PumpLIOpen"
)  # Zulauf links
pump_lo_open = s.addVariable(
    "pumpLoOpen", s.objectsNode, 0.0, nodeId="ns=1;s=PumpLOOpen"
)  # Ablauf links
pump_ri_open = s.addVariable(
    "pumpRiOpen", s.objectsNode, 0.0, nodeId="ns=1;s=PumpRIOpen"
)  # Zulauf rechts
pump_ro_open = s.addVariable(
    "pumpRoOpen", s.objectsNode, 0.0, nodeId="ns=1;s=PumpROOpen"
)  # Ablauf rechts
pump_c_open = s.addVariable(
    "pumpCOpen", s.objectsNode, 0.0, nodeId="ns=1;s=PumpCOpen"
)  # Zentralpumpe
# END CODE

# BEGIN MD
# ## 2. Simulation State
# ``dt`` is the simulation step in seconds.  ``flow_constant`` converts
# a normalized valve position (``0.0``-``1.0``) into litres per second.
# ``tank_capacity`` caps the volume of each tank.  The two initial
# levels live in ``gui_pump`` so the canvas and the script agree.
# END MD

# BEGIN CODE
dt = 1.0  # simulation step [s]
flow_constant = 3.0  # litres per second at full valve opening
tank_capacity = 150.0  # maximum volume per tank [L]
# END CODE

# BEGIN MD
# ## 3. Wiring up the GUI
# ``gui_pump`` owns the Tkinter window, the sliders and the canvas.
# We hand it the server plus the ``VariableNode`` handles so it can
# read the current values when redrawing and write new ones when a
# slider moves.
# END MD

# BEGIN CODE
gui_pump.initialize_from_server(
    s,
    pump_li_open,
    pump_lo_open,
    pump_ri_open,
    pump_ro_open,
    pump_c_open,
    dt,
)
# END CODE

# BEGIN MD
# ## 4. Lifecycle
# The server is started explicitly so we can interleave the GUI
# ``mainloop`` with the OPC UA event loop.  Closing the Tk window
# (or hitting Ctrl+C) calls ``server.stop()`` and joins the worker
# thread cleanly.
# END MD


# BEGIN CODE
def shutdown():
    gui_pump.root.quit()
    gui_pump.root.destroy()


gui_pump.refresh_controls()
gui_pump.draw_system()
gui_pump.update_simulation()
gui_pump.root.protocol("WM_DELETE_WINDOW", shutdown)

s.start()
print("Server running at opc.tcp://localhost:4840")
print("Close the window or press Ctrl+C to stop.\n")

try:
    gui_pump.root.mainloop()
except KeyboardInterrupt:
    print("\nShutting down...")
finally:
    s.stop()
    print("Server stopped.")
# END CODE
