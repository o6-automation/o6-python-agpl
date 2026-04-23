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


simulation = s.add_object("Simulation", s.objects_node)
water_left = s.add_object("PumpLeft", simulation)
water_right = s.add_object("PumpRight", simulation)

pump_li_open = s.add_variable("pumpLiOpen", water_left, 0.0, nodeid="ns=1;s=pumpLiOpen")
pump_lo_open = s.add_variable("pumpLoOpen", water_left, 0.0, nodeid="ns=1;s=pumpLoOpen")
pump_ri_open = s.add_variable(
    "pumpRiOpen", water_right, 0.0, nodeid="ns=1;s=pumpRiOpen"
)
pump_ro_open = s.add_variable(
    "pumpRoOpen", water_right, 0.0, nodeid="ns=1;s=pumpRoOpen"
)
pump_c_open = s.add_variable("pumpCOpen", simulation, 0.0, nodeid="ns=1;s=pumpCOpen")


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
