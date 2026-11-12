# Import standard definitions from companion specifications
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

import sys
import time

import o6
from o6.ns import ns0, di, irdi, padim, machinery_processvalues
 
# Create an OPC UA server
server = o6.Server()
for namespace in (di, irdi, padim, machinery_processvalues):
    server.ns.append(namespace)

# Define a custom ObjectType
o6.ns.namespace("snippet", uri="urn:o6:examples:snippet", version="1.0")

@o6.objecttype(ns="snippet")
class MyProcessValue(padim.objtypes.AnalogSignalType):
    pass
    #analogSignal: padim.vartypes.AnalogSignalVariableType | None
    #setpoint: machinery_processvalues.vartypes.ProcessValueSetpointVariableType | None
    #limitAlarm: ns0.objtypes.ExclusiveLimitAlarmType | None
 
# Publish the custom type before creating a live instance.
server.ns.append(sys.modules[__name__])

# Create an instance with its mandatory children.
print(server.objects)
tValue = MyProcessValue(
    server=server,
    browseName="ns=snippet;Temperature",
    parent=server.objects,
)
#tValue.setpoint(25.0)
 
# Go!
server.start()
print(f"Server running at {server.endpointUrl}")
print("Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
server.stop()
