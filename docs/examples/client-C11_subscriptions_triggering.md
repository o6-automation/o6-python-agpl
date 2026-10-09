# Subscription Triggering

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

## 1. Set up the trigger link
`setMonitoringMode(SAMPLING)` puts item B in a mode where the server keeps
its latest value queued but never reports it on its own. `a.setTriggering
(linksToAdd=[b])` links A as B's trigger: whenever A reports a data
change, the server also flushes B's queued sample into the same publish.

```python
async def main():
    async with o6.Client(endpoint_url) as client:
        print("--- 1. Set Up the Trigger Link ---")
        a_received: list = []
        b_received: list = []

        def on_a(value):
            a_received.append(value)
            print(f"A (IntegerVariable) -> {value}")

        def on_b(value):
            b_received.append(value)
            print(f"B (DoubleVariable) -> {value}")

        sub = await client.createSubscription(publishingInterval=500.0)

        # A: normal reporting trigger item
        a = await client.monitor(NODE_A, on_a, samplingInterval=500.0, subscription=sub)

        # B: sampling only — silent until triggered by A
        b = await client.monitor(NODE_B, on_b, samplingInterval=500.0, subscription=sub)
        await b.setMonitoringMode(ns0.datatypes.MonitoringMode.SAMPLING)

        # Link A → B: whenever A reports, also deliver B's queued sample
        await a.setTriggering(linksToAdd=[b])
```

## 2. Phase 1 — writing B alone stays silent
Because B is in Sampling mode, changing DoubleVariable updates its
queued sample but produces no callback until something triggers it.

```python
print()
print("--- 2. Phase 1: Writing B Alone ---")
await asyncio.sleep(0.2)
b_received.clear()
await client.write(NODE_B, o6.Double(1.23))
await asyncio.sleep(1.5)  # wait longer than the publishing interval
assert len(b_received) == 0, f"Expected no B callbacks, got {len(b_received)}"
print("No callbacks for B, as expected.")
```

## 3. Phase 2 — writing A fires both
Writing IntegerVariable makes A report, and the server piggybacks
B's queued DoubleVariable sample onto the same publish response —
both callbacks fire even though only A was written this time.

```python
    print()
    print("--- 3. Phase 2: Writing A ---")
    # Write a value distinct from whatever A last reported to guarantee a data-change
    last_a = int(a_received[-1]) if a_received else 0
    phase2_val = (last_a + 1) % 10000
    a_received.clear()
    b_received.clear()
    await client.write(NODE_A, o6.UInt32(phase2_val))
    await asyncio.sleep(1.5)
    assert len(a_received) >= 1, f"Expected A callback, got {len(a_received)}"
    assert len(b_received) >= 1, f"Expected B callback (triggered by A), got {len(b_received)}"
    print(f"A callbacks = {len(a_received)}, B callbacks = {len(b_received)}, as expected.")

    await sub.delete()

print()
print("=== Example completed ===")
```

## Source Code

Download [`C11_subscriptions_triggering.py`](client-C11_subscriptions_triggering/C11_subscriptions_triggering.py) to run it locally.
