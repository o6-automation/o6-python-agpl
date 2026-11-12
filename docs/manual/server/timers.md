# Timers & Periodic Updates

Schedule periodic application work on the server event loop.

## Timers

Use a timer for short periodic updates. This fragment assumes a configured
`server`; the callback runs while its event loop is running:

```python
counter = server.addVariable("Counter", server.objects, 0)

def tick():
    counter(counter() + 1)

callbackId = server.addRepeatedCallback(tick, 500.0)      # every 500 ms
```

Later, change the interval or remove the timer:

```python
server.changeRepeatedCallbackInterval(callbackId, 1000.0)
server.removeCallback(callbackId)
```

Intervals are in milliseconds. The callback runs on the loop thread, so keep
it short. Blocking device I/O here delays client requests and other callbacks.
An `async def` timer callback is scheduled as a task on that loop. The timer
does not wait for it before scheduling the next tick, so invocations can
overlap. Removing the timer prevents future ticks; it does not wait for work
already started by a tick.

## Slow device reads

For a device with a blocking Python API, move the read to a worker thread and
publish its result on the server loop. A sequential polling loop bounds the
work to one outstanding device read, even if the device is slower than expected.
This complete example simulates the device with `time.sleep()`:

```python
import asyncio
import time
import o6

def read_sensor():
    time.sleep(0.2)          # replace with device I/O that has a finite timeout
    return 22.5

async def main():
    async with o6.Server(port=4840) as server:
        temperature = await server.addVariable("Temperature", server.objects, 0.0)
        while True:
            value = await asyncio.to_thread(read_sensor)
            await temperature(value)
            await asyncio.sleep(0.5)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```

Only `read_sensor()` runs in the thread; node updates stay on the server loop.
The half-second pause follows each completed update, so this is not a fixed
sampling interval. A read exception leaves the loop and stops the server;
this example does not retry or turn a failed read into a valid measurement.
If the application should continue on errors, define how it reports a stale
or unavailable value to clients.

Ctrl+C cancels the async wait and leaves the server context. `asyncio.run()`
also shuts down its worker pool. Cancellation does not stop a device call
already running in a thread: give the device API a finite timeout so shutdown
can finish. Open and close any device connection around this polling lifetime.

For a read callback that needs fresh data on every request, the same
`await asyncio.to_thread(...)` handoff works inside `async def`. Concurrent
client reads can then start concurrent device calls. Use periodic polling
and a stored Variable, as above, when the device must be accessed serially.
