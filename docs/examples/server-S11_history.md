# History

Demonstrates how to record a Variable's history and configure the
server's history database.

Start any OPC UA client (e.g. ``C02_firststeps.py`` or
``C12_browser.py``) against this server to read and (for the
writable variables) write the values. Read the recorded history back
with the client's ``historyRead``::

    data = client.historyRead("ns=1;i=1001", start, end)
    for dv in data.dataValues:
        print(dv.sourceTimestamp, dv.value)

A history database has to be configured before `server.start()`.
`capacity` bounds how many samples each historizing Variable keeps —
once a Variable's store is full, the oldest sample is evicted to make
room for the newest. `maxResponseSize` is a different kind of limit: a
server-wide cap, unrelated to `capacity`, on how many samples *one*
`historyRead` response carries. A request spanning more values than
that gets back only the first `maxResponseSize` of them plus a
continuation point — a client is expected to call `historyRead` again
with that token until it comes back empty. The high-level
`client.historyRead(...)` does not do that on its own, so a client that
ignores continuation points sees a silently truncated result rather
than an error.

```python
print("--- 1. History Database ---")

server.config.setHistoryDatabase(capacity=1000, maxResponseSize=200)
```

## 2. Historizing variables
`historizing=True` is short for `historizing=o6.History()`: record a
sample on every Write, keeping the database's default capacity.
`o6.History(...)` customizes that per Variable — `capacity=` overrides
the default store size, and `strategy="poll"` samples the Variable's
value every `interval` seconds through an internal MonitoredItem
instead of hooking into the Write service call. That is what a
Variable whose value changes some other way — a read callback, a
lower-level update — needs in order to be historized at all, since
there is no Write for an on-write strategy to hook into.

```python
print()
print("--- 2. Historizing Variables ---")

temperature = server.addVariable(
    "Temperature",
    server.objectsNode,
    22.5,
    nodeId="ns=1;i=1001",
    historizing=True,
)

pressure = server.addVariable(
    "Pressure",
    server.objectsNode,
    1013.25,
    nodeId="ns=1;i=1002",
    historizing=o6.History(capacity=500, strategy="poll", interval=0.5),
)
```

## 3. Run and update loop
`server.start()` blocks until `server.stop()`. Both Variables change
once per cycle here, so either strategy would capture them just the
same — `pressure` uses `poll` only to show how it is configured. A
data-source-backed Variable (see `S07_data_source.py`), whose value
changes through a read callback and never through a Write, is the
case that actually needs it.

```python
    print()
    print("--- 3. Run and Update Loop ---")

    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1
            temperature(22.5 + (cycle % 50) * 0.1)
            pressure(1013.25 + (cycle % 20) * 0.5)

            if cycle % 10 == 0:
                print(
                    f"Cycle {cycle}: Temp = {temperature():.1f}°C, "
                    f"Pressure = {pressure():.1f}hPa"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
```

## Source Code

Download [`S11_history.py`](server-S11_history/S11_history.py) to run it locally.
