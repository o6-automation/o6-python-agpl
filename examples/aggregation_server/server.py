"""
Aggregation server example.

This demo creates two source OPC UA servers, each publishing a custom struct
value. Each source server runs a background thread and updates its source
variable every half second with a new random value.

The aggregator server can then read those changing values and expose them as
part of a combined aggregated payload.
"""

import math
import os
import random
import socket
import threading
import time
from typing import Any

import o6
from o6 import Client, Server

example_dir = os.path.dirname(os.path.abspath(__file__))
position2d_path = os.path.join(example_dir, "position2d_nodeset2.xml")
direction2d_path = os.path.join(example_dir, "direction2d_nodeset2.xml")
matrix3d_path = os.path.join(example_dir, "matrix3d_nodeset2.xml")


def get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


# Simulates a data source with opcua server.
class Source:
    def __init__(self, nodeset_path: str, nodeid: str):
        self.port = get_free_port()
        self.srv = Server(port=self.port)
        self.nodeset = self.srv.ns.load(nodeset_path)
        self.nodeid = nodeid
        self.stop_event = threading.Event()
        self._thread = threading.Thread(target=self._update_loop, daemon=True)
        self.short_name = self.nodeset.metadata.short_name

    def _update_loop(self) -> None:
        pass

    def start(self) -> None:
        self.srv.start()
        self._thread.start()

    def stop(self) -> None:
        self.stop_event.set()
        self._thread.join(timeout=1.0)
        self.srv.stop()


# Updates a position data source with randomized speed
class PositionSource(Source):
    def __init__(self):
        self.nodeid = "ns=1;i=1001"
        super().__init__(position2d_path, nodeid=self.nodeid)

        self.node_type = self.nodeset.Position2DType
        self.browse_name = "SourcePosition"
        self.srv.add_variable(
            self.browse_name,
            self.srv.objects_node,
            self.srv.ns.position2d.Position2DType(0.0, 0.0),
            nodeid=self.nodeid,
        )

        self.speed = (random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))

    def _update_loop(self):
        while not self.stop_event.wait(1):
            v = self.srv.read(self.nodeid)
            v.x = v.x + self.speed[0]
            v.y = v.y + self.speed[1]
            self.srv.write_value(self.nodeid, v)


# Updates a direction data source with randomized angular velocity
class DirectionSource(Source):
    def __init__(self):
        self.nodeid = "ns=1;i=1002"
        super().__init__(direction2d_path, nodeid=self.nodeid)

        self.node_type = self.nodeset.Direction2DType
        self.browse_name = "SourceDirection"
        self.srv.add_variable(
            self.browse_name,
            self.srv.objects_node,
            self.srv.ns.direction2d.Direction2DType(1.0, 0.0),
            nodeid=self.nodeid,
        )

        self.speed = random.uniform(-0.1, 0.1)

    def _update_loop(self):
        while not self.stop_event.wait(1):
            v = self.srv.read(self.nodeid)
            angle = math.atan2(v.y, v.x) + self.speed
            v.x = math.cos(angle)
            v.y = math.sin(angle)
            self.srv.write_value(self.nodeid, v)


def main() -> None:
    # =============================
    # = Simulate two data sources =
    # =============================
    src_a = PositionSource()
    src_a.start()
    src_b = DirectionSource()
    src_b.start()

    # ==========================
    # = The aggregation server =
    # ==========================
    port = get_free_port()
    server = Server(port=port)
    server.ns.load(
        matrix3d_path
    )  # note: no interdependencies nodesets, can be loaded in any order
    server.ns.load(position2d_path)
    server.ns.load(direction2d_path)

    # add variables for the aggregated values
    pos_value = server.ns.position2d.Position2DType(0.0, 0.0)
    dir_value = server.ns.direction2d.Direction2DType(0.0, 0.0)
    pos_nodeid = server.add_variable(
        "position", server.objects_node, pos_value, nodeid="ns=1;i=1004"
    ).nodeid
    dir_nodeid = server.add_variable(
        "direction", server.objects_node, dir_value, nodeid="ns=1;i=1005"
    ).nodeid

    # we also add a more complex variable from the aggregated values to demonstrate the server's ability to combine multiple inputs into a more complex output.
    transform_value = server.ns.matrix3d.Matrix3dType()
    transform_value.rows = []
    for _ in range(3):
        row = server.ns.matrix3d.MatrixRowType()
        row.x = 0.0
        row.y = 0.0
        row.z = 0.0
        transform_value.rows.append(row)
    transform_nodeid = server.add_variable(
        "transform", server.objects_node, transform_value, nodeid="ns=1;i=1003"
    ).nodeid
    server.start()

    # compute a 3d transformation matrix with homogeneous coordinates from the position and direction values
    # write it to the server whenever either of them changes
    def update_transform():
        pos = server.read(pos_nodeid)
        dir = server.read(dir_nodeid)

        matrix_value = server.ns.matrix3d.Matrix3dType()
        matrix_value.rows = []

        row0 = server.ns.matrix3d.MatrixRowType()
        row0.x = dir.x
        row0.y = -dir.y
        row0.z = pos.x
        matrix_value.rows.append(row0)

        row1 = server.ns.matrix3d.MatrixRowType()
        row1.x = dir.y
        row1.y = dir.x
        row1.z = pos.y
        matrix_value.rows.append(row1)

        row2 = server.ns.matrix3d.MatrixRowType()
        row2.x = 0.0
        row2.y = 0.0
        row2.z = 1.0
        matrix_value.rows.append(row2)

        server.write(transform_nodeid, matrix_value)

    # The aggregation server needs to connect as a client to the data sources
    # We use substriction monitoring to get updates
    client_a = Client(f"opc.tcp://localhost:{src_a.port}")
    client_a.ns.load(position2d_path)
    client_a.connect()

    def update_position(data_value):
        pos = getattr(data_value, "value", data_value)
        server.write(pos_nodeid, pos)
        print(f"Client A: new position -> x = {pos.x:.2f}, y = {pos.y:.2f}")
        update_transform()

    client_a.monitor(src_a.nodeid, update_position)

    # Same pattern for the dircetion source
    client_b = Client(f"opc.tcp://localhost:{src_b.port}")
    client_b.ns.load(direction2d_path)
    client_b.connect()

    def update_direction(data_value):
        dir = getattr(data_value, "value", data_value)
        server.write(dir_nodeid, dir)
        print(f"Client B: new direction -> x = {dir.x:.2f}, y = {dir.y:.2f}")
        update_transform()

    client_b.monitor(src_b.nodeid, update_direction)

    # ===================================================
    # = Downstream client to read the aggregated values =
    # ===================================================
    downstream = Client(f"opc.tcp://localhost:{port}")
    downstream.ns.load(matrix3d_path)
    downstream.connect()
    downstream.default_subscription.modify(publishing_interval=2000.0)

    def pretty_matrix(data_value):
        matrix = getattr(data_value, "value", data_value)
        print("Downstream client: new transform matrix ->")
        for row in matrix.rows:
            print(f"  {row.x:7.2f} {row.y:7.2f} {row.z:7.2f}")

    downstream.monitor(transform_nodeid, pretty_matrix)

    # ==============================================
    # = Keep the servers running until interrupted =
    # ==============================================
    try:
        print("Source servers are running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Shutting down source servers...")
    finally:
        src_a.stop()
        src_b.stop()
        server.stop()
        client_a.disconnect()
        client_b.disconnect()
        downstream.disconnect()


if __name__ == "__main__":
    main()
