#!/usr/bin/env python3
"""
Demonstrates OPC UA triggering: one monitored item (A) controls when another
(B) delivers its data to the client.

Setup:
  A  monitors IntegerVariable  — MonitoringMode.Reporting  (the trigger)
  B  monitors DoubleVariable   — MonitoringMode.Sampling   (triggered, silent by itself)

Phase 1 — write only DoubleVariable:
  B is sampling but never reports on its own because its mode is Sampling.
  No callbacks arrive for B.

Phase 2 — write IntegerVariable (A):
  A fires → the server also delivers B's queued sample in the same publish.
  Both callbacks arrive.
"""

import asyncio
import socket
import o6
from o6 import types

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

NODE_A = "ns=1;s=IntegerVariable"
NODE_B = "ns=1;s=DoubleVariable"


async def main():
    async with o6.Client(endpoint_url) as client:
        a_received: list = []
        b_received: list = []

        def on_a(value):
            a_received.append(value)
            print(f"  [A] IntegerVariable = {value}")

        def on_b(value):
            b_received.append(value)
            print(f"  [B] DoubleVariable  = {value}")

        sub = await client.create_subscription(publishing_interval=500.0)

        # A: normal reporting trigger item
        a = await sub.monitor(NODE_A, on_a, sampling_interval=500.0)

        # B: sampling only — silent until triggered by A
        b = await sub.monitor(NODE_B, on_b, sampling_interval=500.0)
        await b.set_monitoring_mode(types.MonitoringMode.SAMPLING)

        # Link A → B: whenever A reports, also deliver B's queued sample
        await a.set_triggering(links_to_add=[b])

        # --- Phase 1: write only B, expect no callbacks ---
        print("\nPhase 1: writing DoubleVariable only — B should stay silent...")
        await asyncio.sleep(0.2)
        b_received.clear()
        await client.write(NODE_B, types.Double(1.23))
        await asyncio.sleep(1.5)  # wait longer than the publishing interval
        assert len(b_received) == 0, f"Expected no B callbacks, got {len(b_received)}"
        print("  ✓ No callbacks for B (as expected)")

        # --- Phase 2: write A, expect both A and B callbacks ---
        print("\nPhase 2: writing IntegerVariable — both A and B should fire...")
        # Write a value distinct from whatever A last reported to guarantee a data-change
        last_a = int(a_received[-1]) if a_received else 0
        phase2_val = (last_a + 1) % 10000
        a_received.clear()
        b_received.clear()
        await client.write(NODE_A, types.UInt32(phase2_val))
        await asyncio.sleep(1.5)
        assert len(a_received) >= 1, f"Expected A callback, got {len(a_received)}"
        assert (
            len(b_received) >= 1
        ), f"Expected B callback (triggered by A), got {len(b_received)}"
        print(f"  ✓ A callbacks: {len(a_received)}, B callbacks: {len(b_received)}")

        await sub.delete()

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
