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

"""Generated OPC UA machinery_jobs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=machinery_jobs;i=3003", browseName="ns=machinery_jobs;JobExecutionMode")
class JobExecutionMode(ns0.datatypes.Enumeration):
    SIMULATION_MODE = o6.enumfield(0, name="SimulationMode")
    TEST_MODE = o6.enumfield(1, name="TestMode")
    PRODUCTION_MODE = o6.enumfield(2, name="ProductionMode")


@o6.enumtype(nodeId="ns=machinery_jobs;i=3004", browseName="ns=machinery_jobs;ProcessIrregularity")
class ProcessIrregularity(ns0.datatypes.Enumeration):
    CAPABILITY_UNAVAILABLE = o6.enumfield(0, name="CapabilityUnavailable")
    DETECTED = o6.enumfield(1, name="Detected")
    NOT_DETECTED = o6.enumfield(2, name="NotDetected")
    NOT_YET_DETERMINED = o6.enumfield(3, name="NotYetDetermined")


@o6.enumtype(nodeId="ns=machinery_jobs;i=3006", browseName="ns=machinery_jobs;JobResult")
class JobResult(ns0.datatypes.Enumeration):
    UNKNOWN = o6.enumfield(0, name="Unknown")
    SUCCESSFUL = o6.enumfield(1, name="Successful")
    UNSUCCESSFUL = o6.enumfield(2, name="Unsuccessful")


@o6.optionsettype(nodeId="ns=machinery_jobs;i=3009", browseName="ns=machinery_jobs;OutputInfoType", base=o6.Byte)
class OutputInfoType:
    ORDER_NUMBER = o6.bitmask(0x01 << 0, name="OrderNumber")
    LOT_NUMBER = o6.bitmask(0x01 << 1, name="LotNumber")
    SERIAL_NUMBER = o6.bitmask(0x01 << 2, name="SerialNumber")


@o6.datatype(nodeId="ns=machinery_jobs;i=3012", browseName="ns=machinery_jobs;OutputInformationDataType", defaultEncodingId="ns=machinery_jobs;i=5003")
class OutputInformationDataType(ns0.datatypes.Structure):
    itemNumber: o6.String = o6.field(name="ItemNumber")
    outputInfo: OutputInfoType = o6.field(name="OutputInfo")
    orderNumber: o6.String | None = o6.field(name="OrderNumber")
    lotNumber: o6.String | None = o6.field(name="LotNumber")
    serialNumber: o6.String | None = o6.field(name="SerialNumber")


@o6.datatype(nodeId="ns=machinery_jobs;i=3015", browseName="ns=machinery_jobs;BOMComponentInformationDataType", defaultEncodingId="ns=machinery_jobs;i=5005")
class BOMComponentInformationDataType(ns0.datatypes.Structure):
    identification: OutputInformationDataType = o6.field(name="Identification")
    quantity: o6.Double = o6.field(name="Quantity")
    engineeringUnits: ns0.datatypes.EUInformation = o6.field(name="EngineeringUnits")


@o6.datatype(nodeId="ns=machinery_jobs;i=3018", browseName="ns=machinery_jobs;BOMInformationDataType", defaultEncodingId="ns=machinery_jobs;i=5007")
class BOMInformationDataType(ns0.datatypes.Structure):
    identification: OutputInformationDataType = o6.field(name="Identification")
    componentInformation: list[BOMComponentInformationDataType] = o6.field(name="ComponentInformation", arrayDimensions=[0])


@o6.datatype(nodeId="ns=machinery_jobs;i=3021", browseName="ns=machinery_jobs;OutputPerformanceInfoDataType", defaultEncodingId="ns=machinery_jobs;i=5009")
class OutputPerformanceInfoDataType(ns0.datatypes.Structure):
    identification: OutputInformationDataType = o6.field(name="Identification")
    startTime: o6.DateTime | None = o6.field(name="StartTime")
    endTime: o6.DateTime | None = o6.field(name="EndTime")
    parameters: list[isa95_jobcontrol_v2.datatypes.ISA95ParameterDataType] = o6.field(name="Parameters", arrayDimensions=[0])


del Any, TYPE_CHECKING, uuid, o6, isa95_jobcontrol_v2, ns0
