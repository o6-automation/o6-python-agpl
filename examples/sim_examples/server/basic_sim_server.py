from o6.server import Server

try:
    from . import gui_pump
except ImportError:
    import gui_pump

s = Server(port=4840)
tank_left = 50.0
tank_right = 100.0
tank_capacity = 150.0
flow_constant = 3.0

# --- OPC UA Variablen ---
# To use a variable as a client, you need the nodeid, which can be set explicitly when creating the variable.
# ns is the namespace index (always 1 for custom variables), i is the identifier (integer) and s is the identifier (string).
# first parameter is the name of the variable, second parameter is the parent node, third parameter is the initial value, and nodeid as an identifier.
# (There can't be any spaces in the nodeid string)

pump_li_open = s.add_variable(
    "pumpLiOpen", s.objects_node, 0.0, nodeid="ns=1;s=PumpLIOpen"
)  # Zulauf links
pump_lo_open = s.add_variable(
    "pumpLoOpen", s.objects_node, 0.0, nodeid="ns=1;s=PumpLOOpen"
)  # Ablauf links
pump_ri_open = s.add_variable(
    "pumpRiOpen", s.objects_node, 0.0, nodeid="ns=1;s=PumpRIOpen"
)  # Zulauf rechts
pump_ro_open = s.add_variable(
    "pumpRoOpen", s.objects_node, 0.0, nodeid="ns=1;s=PumpROOpen"
)  # Ablauf rechts
pump_c_open = s.add_variable(
    "pumpCOpen", s.objects_node, 0.0, nodeid="ns=1;s=PumpCOpen"
)  # Zentralpumpe


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
