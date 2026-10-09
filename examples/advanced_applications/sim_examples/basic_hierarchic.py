# Copyright (c) 2026 o6 Automation GmbH
#
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

from o6.server import Server

try:
    from . import gui_pump
except ImportError:
    import gui_pump

s = Server(port=4840)

# --- OPC UA Variablen ---
# objects can be used to create a hierarchy in the address space, which can be helpful for organization and readability.
# simulation ---
#               | -- Water Left
#                            | -- Pump Left Inflow
#                            | -- Pump Left Outflow
#               | -- Water Right
#                            | -- Pump Right Inflow
#                            | -- Pump Right Outflow
#               | -- Pump Central


simulation = s.addObject("Simulation", s.objectsNode)
water_left = s.addObject("PumpLeft", simulation)
water_right = s.addObject("PumpRight", simulation)

pump_li_open = s.addVariable("pumpLiOpen", water_left, 0.0, nodeId="ns=1;s=pumpLiOpen")
pump_lo_open = s.addVariable("pumpLoOpen", water_left, 0.0, nodeId="ns=1;s=pumpLoOpen")
pump_ri_open = s.addVariable("pumpRiOpen", water_right, 0.0, nodeId="ns=1;s=pumpRiOpen")
pump_ro_open = s.addVariable("pumpRoOpen", water_right, 0.0, nodeId="ns=1;s=pumpRoOpen")
pump_c_open = s.addVariable("pumpCOpen", simulation, 0.0, nodeId="ns=1;s=pumpCOpen")


dt = 1.0  # Zeitschritt

gui_pump.initialize_from_server(
    s,
    pump_li_open,
    pump_lo_open,
    pump_ri_open,
    pump_ro_open,
    pump_c_open,
    dt,
)


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
