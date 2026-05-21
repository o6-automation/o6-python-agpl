#!/usr/bin/env python3
"""
Simple OPC UA Server with bulk variables
==========================================

Creates:
  - 100 scalar variables of each type: Boolean, Int32, Double
  - 100 array variables (length 1024) of each type: Boolean, Int32, Double

Total: 600 variables organised under two folder objects.

Connect with any OPC UA client at:
    opc.tcp://localhost:4840
"""

import socket
import time
import numpy as np
from o6 import Server


def _find_free_port(preferred: int) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("", preferred))
            return preferred
        except OSError:
            s.bind(("", 0))
            return s.getsockname()[1]


def main():
    port = _find_free_port(4840)
    server = Server(port=port)

    # ── Scalar variables ──────────────────────────────────────────────────────
    scalars = server.add_object("Scalars", server.objects_node)

    bool_folder = server.add_object("BoolVariables", scalars)
    int32_folder = server.add_object("Int32Variables", scalars)
    double_folder = server.add_object("DoubleVariables", scalars)

    n_variables = 1 << 10
    bool_vars = [
        server.add_variable(f"Bool_{i:03d}", bool_folder, False)
        for i in range(n_variables)
    ]
    int32_vars = [
        server.add_variable(f"Int32_{i:03d}", int32_folder, 0)
        for i in range(n_variables)
    ]
    double_vars = [
        server.add_variable(f"Double_{i:03d}", double_folder, 0.0)
        for i in range(n_variables)
    ]

    # ── Array variables (length 1024) ─────────────────────────────────────────
    arrays = server.add_object("Arrays", server.objects_node)

    bool_arr_folder = server.add_object("BoolArrays", arrays)
    int32_arr_folder = server.add_object("Int32Arrays", arrays)
    double_arr_folder = server.add_object("DoubleArrays", arrays)

    array_len = 1 << 20

    bool_arr_vars = [
        server.add_variable(
            f"BoolArray", bool_arr_folder, np.zeros(array_len, dtype=np.bool_)
        )
    ]
    int32_arr_vars = [
        server.add_variable(
            f"Int32Array", int32_arr_folder, np.zeros(array_len, dtype=np.int32)
        )
    ]
    double_arr_vars = [
        server.add_variable(
            f"DoubleArray", double_arr_folder, np.zeros(array_len, dtype=np.float64)
        )
    ]

    # ── Start ─────────────────────────────────────────────────────────────────
    server.start()
    print(f"Server running at opc.tcp://localhost:{port}")
    print(f"  {len(bool_vars) + len(int32_vars) + len(double_vars)} scalar variables")
    print(
        f"  {len(bool_arr_vars) + len(int32_arr_vars) + len(double_arr_vars)}"
        f" array variables ({array_len} elements each)"
    )
    print("Press Ctrl+C to stop.\n")

    try:
        i = 0
        while True:
            i += 1
            # Update first variable of each type so clients can see live data
            bool_vars[0].value = bool(i % 2)
            int32_vars[0].value = i
            double_vars[0].value = float(i) * 0.1
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
