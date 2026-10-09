#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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

r"""
Server Tutorial: History with a custom backend
================================================

``S11_history.py`` records into o6's own in-memory ring. This example
records into a real time-series database (InfluxDB) instead, by subclassing
``o6.HistoryBackend`` — see ``o6/_history.py`` for the base class.

Prerequisites::

    pip install influxdb-client

    docker run -d --name o6-influx-demo -p 8086:8086 \
        -e DOCKER_INFLUXDB_INIT_MODE=setup \
        -e DOCKER_INFLUXDB_INIT_USERNAME=admin \
        -e DOCKER_INFLUXDB_INIT_PASSWORD=adminadmin \
        -e DOCKER_INFLUXDB_INIT_ORG=o6-demo \
        -e DOCKER_INFLUXDB_INIT_BUCKET=history \
        -e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=o6-demo-token-0123456789 \
        influxdb:2

Start any OPC UA client (e.g. ``C02_firststeps.py`` or ``C12_browser.py``,
or UaExpert) against this server and read the recorded history back with
``historyRead``::

    data = client.historyRead("ns=1;s=Temperature", start, end)
    for dv in data.dataValues:
        print(dv.sourceTimestamp, dv.value)
"""

from __future__ import annotations

import datetime as dt
import math
import time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import o6
from o6 import Server

NODE = "ns=1;s=Temperature"

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "o6-demo-token-0123456789"
INFLUX_ORG = "o6-demo"
INFLUX_BUCKET = "history"

# BEGIN MD
# ## 1. A custom `o6.HistoryBackend`
#
# `server.config.setHistoryDatabase(backend=...)` takes an `o6.HistoryBackend`
# instance instead of `capacity=`/`maxResponseSize=` and swaps out o6's
# in-memory ring for whatever `onWrite`/`getHistoryData`/etc. do — one call,
# nothing else about the server changes. Subclass and override only what you
# need: `onWrite` and `getHistoryData` are the two that matter for basic
# recording and reading; `insertDataValue`/`replaceDataValue`/
# `updateDataValue`/`removeDataValue` (HistoryUpdate) and
# `boundSupported`/`timestampsToReturnSupported` (ReadRaw capability flags)
# are all optional — an unoverridden HistoryUpdate op answers
# `BadHistoryOperationUnsupported` on its own, without ever reaching Python.
# END MD

# BEGIN CODE
class InfluxHistoryBackend(o6.HistoryBackend):
    """Records history into InfluxDB instead of o6's in-memory ring.

    One InfluxDB measurement (``o6_history`` by default) holds every
    historized node, distinguished by a ``nodeId`` tag — the usual InfluxDB
    schema shape (one measurement, many series by tag) rather than one
    measurement per node, which keeps a single Flux query parameterizable by
    `nodeId` instead of needing to be rebuilt per node.
    """

    def __init__(
        self,
        url: str,
        token: str,
        org: str,
        bucket: str,
        measurement: str = "o6_history",
    ) -> None:
        self._client = InfluxDBClient(url=url, token=token, org=org)
        self._write_api = self._client.write_api(write_options=SYNCHRONOUS)
        self._query_api = self._client.query_api()
        self._delete_api = self._client.delete_api()
        self._org = org
        self._bucket = bucket
        self._measurement = measurement

    def close(self) -> None:
        """Release the InfluxDB client. Call once, after `server.stop()`."""
        self._client.close()
    # END CODE

    # BEGIN MD
    # ## 2. Recording and reading
    #
    # `onWrite` fires for every sample the server wants recorded, whether the
    # node's strategy is `"on-write"` (a client Write) or `"poll"` (an
    # internal MonitoredItem) — the name follows open62541's own
    # `serverSetHistoryData`, which does the same. `getHistoryData` serves
    # ReadRaw entirely: no generic paging or `timestampsToReturn` filtering
    # happens on the result afterward, so both are this method's own
    # responsibility if you need them (this example implements neither, and
    # says so).
    #
    # Two InfluxDB-specific gotchas worth knowing regardless of which
    # database you end up using: Flux's `range()` needs `stop` strictly after
    # `start`, so a single-instant read (`start == end`, which `ReadRaw`
    # legitimately allows, and which some clients — UaExpert's history/trend
    # view among them — send) has to be widened by a tiny margin rather than
    # forwarded as an error (`_fluxRange` below). And a client requesting
    # `returnBounds=True` wants the one value immediately before `start` and
    # after `end` in addition to the range itself — checked against
    # open62541's own reference backend rather than guessed: no special
    # status marking, just two extra `DataValue`s.
    # END MD

    # BEGIN CODE
    def onWrite(self, nodeId: "o6.NodeId", value: "o6.DataValue") -> None:
        point = (
            Point(self._measurement)
            .tag("nodeId", str(nodeId))
            .field("value", _scalar(value.value))
            .time(str(value.sourceTimestamp), WritePrecision.NS)
        )
        self._write_api.write(bucket=self._bucket, record=point)

    # HistoryUpdate Insert is just another write; InfluxDB does not
    # distinguish "insert" from "overwrite" the way the OPC UA service does
    # (a point at an existing timestamp is silently replaced), so this
    # reference implementation does not separately enforce Insert's
    # "must not already exist" / Replace's "must already exist" semantics —
    # a production backend that needs that distinction would query first.
    insertDataValue = onWrite
    replaceDataValue = onWrite
    updateDataValue = onWrite

    def getHistoryData(
        self,
        nodeId: "o6.NodeId",
        start,
        end,
        maxSize: int,
        numValues: int,
        returnBounds: bool,
        timestampsToReturn,
        range,
    ) -> list:
        fluxStart, fluxStop = _fluxRange(start, end)
        values = self._queryValues(nodeId, fluxStart, fluxStop)

        if returnBounds:
            # Only meaningful against a real bound - querying [epoch, epoch)
            # or [now(), now()) is the same empty range _fluxRange exists to
            # avoid, hence the None guards.
            if start is not None:
                values = self._queryValues(nodeId, "1970-01-01T00:00:00Z", fluxStart, last=True) + values
            if end is not None:
                values = values + self._queryValues(nodeId, fluxStop, "now()", first=True)

        return values

    def boundSupported(self, nodeId) -> bool:
        return True

    def timestampsToReturnSupported(self, nodeId, timestampsToReturn) -> bool:
        return True  # every InfluxDB point carries its own _time

    def _queryValues(self, nodeId: "o6.NodeId", fluxStart: str, fluxStop: str,
                     *, first: bool = False, last: bool = False) -> list:
        selector = "|> first()" if first else "|> last()" if last else ""
        flux = f"""
        from(bucket: "{self._bucket}")
          |> range(start: {fluxStart}, stop: {fluxStop})
          |> filter(fn: (r) => r._measurement == "{self._measurement}"
                            and r.nodeId == "{nodeId!s}"
                            and r._field == "value")
          |> sort(columns: ["_time"])
          {selector}
        """
        tables = self._query_api.query(flux, org=self._org)
        values = []
        for table in tables:
            for record in table.records:
                dv = o6.DataValue()
                dv.value = record.get_value()
                dv.sourceTimestamp = o6.DateTime(record.get_time())
                values.append(dv)
        return values
    # END CODE

    # BEGIN MD
    # ## 3. HistoryUpdate delete, and wiring it into a server
    #
    # `removeDataValue` is the only HistoryUpdate op this backend implements
    # beyond "write a point" — deleting is genuinely different in InfluxDB
    # (a predicate over a time range, not a per-value operation), so it earns
    # its own method rather than aliasing `onWrite`.
    #
    # Wiring it in is the one line that differs from `S11_history.py`:
    # `setHistoryDatabase(backend=...)` instead of
    # `setHistoryDatabase(capacity=..., maxResponseSize=...)`. Everything
    # else — `historizing=True`, the write loop, `server.start()`/`stop()` —
    # is unchanged.
    # END MD

    # BEGIN CODE
    def removeDataValue(self, nodeId: "o6.NodeId", start, end) -> None:
        fluxStart, fluxStop = _fluxRange(start, end)
        self._delete_api.delete(
            start=fluxStart,
            stop=fluxStop,
            predicate=f'_measurement="{self._measurement}" AND nodeId="{nodeId!s}"',
            bucket=self._bucket,
            org=self._org,
        )
    # END CODE


# BEGIN MD
# `_scalar` and `_fluxRange` are plain helpers, not part of the
# `HistoryBackend` contract — factored out because `getHistoryData` and
# `removeDataValue` both need the same range-widening fix.
# END MD

# BEGIN CODE
def _scalar(value):
    """InfluxDB fields are int / float / str / bool. o6's builtin scalars
    already behave like their Python equivalents, so this only exists to be
    explicit about the mapping rather than relying on isinstance fallthrough."""
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        return float(value)
    return str(value)


def _fluxRange(start, end) -> tuple[str, str]:
    """(start, end) -> Flux `range()` bounds, as RFC3339 strings or `now()`.

    `o6.HistoryBackend` passes `None` for an open end in either direction;
    Flux needs an explicit bound, so an open start becomes the Unix epoch and
    an open end becomes `now()`. Flux also requires `stop` strictly after
    `start` - a degenerate window (`start == end`, or narrower) is widened
    by the smallest useful margin instead of forwarding InfluxDB's
    "cannot query an empty range" error.
    """
    if start is None:
        return "1970-01-01T00:00:00Z", (str(end) if end is not None else "now()")
    if end is None:
        return str(start), "now()"
    startTime = dt.datetime.fromisoformat(str(start))
    endTime = dt.datetime.fromisoformat(str(end))
    if endTime <= startTime:
        endTime = startTime + dt.timedelta(microseconds=1)
    return str(start), endTime.isoformat()


def main() -> None:
    backend = InfluxHistoryBackend(
        url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG, bucket=INFLUX_BUCKET
    )

    server = Server(port=4840)

    print("--- 1. History Database (InfluxDB) ---")
    server.config.setHistoryDatabase(backend=backend)

    print()
    print("--- 2. Historizing Variable ---")
    temperature = server.addVariable(
        "Temperature",
        server.objectsNode,
        20.0,
        nodeId=NODE,
        historizing=o6.History(strategy="on-write"),
    )

    print()
    print("--- 3. Run and update loop ---")
    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print(f"historizing {NODE} into InfluxDB bucket {INFLUX_BUCKET!r}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1
            temperature(20.0 + 5.0 * math.sin(cycle / 5.0))
            if cycle % 10 == 0:
                print(f"Cycle {cycle}: Temperature = {temperature():.1f}°C")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        backend.close()
        print("Server stopped.")


if __name__ == "__main__":
    main()
    # END CODE
