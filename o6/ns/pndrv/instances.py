# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Generated OPC UA pndrv namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pnenc as pnenc
from . import vartypes as pndrv_vartypes
from . import objtypes as pndrv_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

pndrv_objtypes.TraversingTaskType(nodeId="ns=pndrv;i=5023", browseName="ns=pndrv;TraversingTask")
o6.reference(o6.ns["ns=pndrv;i=5023"], "i=47", o6.ns["ns=pndrv;i=6092"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPDRVSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pndrv;i=5000",
    browseName="ns=pndrv;http://opcfoundation.org/UA/PDRV/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6000", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6001", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-07-04T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PDRV/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6003", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6004", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6005", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6006", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6007", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6008", browseName="ns=pndrv;JogSpeed1", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6008"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6010",
    browseName="ns=pndrv;JogSpeed2",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6013", browseName="ns=pndrv;RfgRampDownTime", dataType=o6.Float)
ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6014", browseName="ns=pndrv;QuickStopRampDownTime", dataType=o6.Float)
ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6015", browseName="ns=pndrv;LimitFollowingError", dataType=ns0.datatypes.Number)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6016", browseName="ns=pndrv;PositionFollowingError", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6016"], "i=46", "i=17502")
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6017",
    browseName="ns=pndrv;ControlMode",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6018",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    o6.LocalizedText("TORQUE_CONTROL", "en"),
                    o6.LocalizedText("FORCE_CONTROL", "en"),
                    o6.LocalizedText("SPEED_CONTROL", "en"),
                    o6.LocalizedText("SPEED_CONTROL_DSC", "en"),
                    o6.LocalizedText("POSITION_CONTROL", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6012",
    browseName="ns=pndrv;RfgRampUpTime",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6022",
    browseName="ns=pndrv;RfgAcceleration",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6023", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6024",
    browseName="ns=pndrv;MinimumVelocity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6025", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6029",
    browseName="ns=pndrv;AxisState",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6009",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[13],
                value=[
                    o6.LocalizedText("S1_SWITCHING_ON_INHIBITED", "en"),
                    o6.LocalizedText("S2_READY_FOR_SWITCHING_ON", "en"),
                    o6.LocalizedText("S3_SWITCHED_ON", "en"),
                    o6.LocalizedText("S4_OPERATION", "en"),
                    o6.LocalizedText("S51_RAMP_STOP", "en"),
                    o6.LocalizedText("S52_QUICK_STOP", "en"),
                    o6.LocalizedText("S41_POS_BASIC_STATE", "en"),
                    o6.LocalizedText("S42_POS_JOGGING", "en"),
                    o6.LocalizedText("S43_POS_BRAKING_WITH_RAMP", "en"),
                    o6.LocalizedText("S44_POS_HOMING_PROCEDURE", "en"),
                    o6.LocalizedText("S451_POS_TRAVERSING_TASK_ACTIVE", "en"),
                    o6.LocalizedText("S452_POS_BRAKING_WITH_RAMP", "en"),
                    o6.LocalizedText("S453_POS_INTERMEDIATE_STOP", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6030", browseName="ns=pndrv;OutputCurrent", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6030"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6031", browseName="ns=pndrv;Torque", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6031"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6032", browseName="ns=pndrv;Power", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6032"], "i=46", "i=17502")
pndrv_vartypes.TemperatureVariableType(nodeId="ns=pndrv;i=6033", browseName="ns=pndrv;MotorTemperature", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6033"], "i=46", "i=17502")
pndrv_vartypes.TemperatureVariableType(nodeId="ns=pndrv;i=6034", browseName="ns=pndrv;ConverterTemperature", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6034"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6035", browseName="ns=pndrv;DcBusVoltage", dataType=o6.UInt16)
o6.reference(o6.ns["ns=pndrv;i=6035"], "i=46", "i=17502")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pndrv;i=6040",
    browseName="ns=pndrv;<SignalName>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6041", browseName="ns=pndrv;SignalNumber", dataType=o6.UInt16))],
    dataType=ns0.datatypes.Number,
)
ns0.objtypes.FolderType(nodeId="ns=pndrv;i=5004", browseName="ns=pndrv;PNSignals", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=pndrv;i=6040"])])
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5004"])
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5012",
    browseName="ns=pndrv;STO",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6028", browseName="ns=pndrv;STOSelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6042", browseName="ns=pndrv;STOActive")),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5013",
    browseName="ns=pndrv;SS1",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6043", browseName="ns=pndrv;SS1Selection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6044", browseName="ns=pndrv;SS1Active")),
    ],
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6046", browseName="ns=pndrv;VelocitySetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6046"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5015",
    browseName="ns=pndrv;SS2",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6045", browseName="ns=pndrv;SS2Selection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6047", browseName="ns=pndrv;SS2Active")),
    ],
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6048", browseName="ns=pndrv;VelocityCommandValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6048"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6049", browseName="ns=pndrv;VelocityActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6049"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6050", browseName="ns=pndrv;OutputFrequency", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6050"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6051", browseName="ns=pndrv;OutputVoltage", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6051"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5014",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6046"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6048"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6049"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6050"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6051"]),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6052", browseName="ns=pndrv;OutputCosPhi", dataType=o6.Float)),
    ],
)
o6.reference(pndrv_objtypes.VelocityDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5014"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6015"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6029"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6030"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6031"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6032"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6033"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6034"])
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6035"])
pndrv_vartypes.TemperatureVariableType(nodeId="ns=pndrv;i=6053", browseName="ns=pndrv;DeviceTemperature", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6053"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6039",
    browseName="ns=pndrv;InputConverterAcInputVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6056", browseName="ns=pndrv;MotorCurrentLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6056"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6057", browseName="ns=pndrv;MotorCurrentLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6057"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6058", browseName="ns=pndrv;TorqueLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6058"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6059", browseName="ns=pndrv;TorqueLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6059"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5016",
    browseName="ns=pndrv;LimitSupervision",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6056"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6057"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6058"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6059"]),
    ],
)
o6.reference(pndrv_objtypes.VelocityDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5016"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6055",
    browseName="ns=pndrv;OutputConverterPulseFrequency",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
o6.reference(o6.ns["ns=pndrv;i=5035"], "i=47", o6.ns["ns=pndrv;i=6055"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6061",
    browseName="ns=pndrv;MaximumVelocity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6062", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5010",
    browseName="ns=pndrv;VelocityProfile",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6008"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6010"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6012"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6022"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6024"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6061"]),
    ],
)
o6.reference(pndrv_objtypes.FrequencyDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5010"])
o6.reference(o6.ns["ns=pndrv;i=5010"], "i=47", o6.ns["ns=pndrv;i=6013"])
o6.reference(o6.ns["ns=pndrv;i=5010"], "i=47", o6.ns["ns=pndrv;i=6014"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6063", browseName="ns=pndrv;JogSpeed1", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6063"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6064",
    browseName="ns=pndrv;JogSpeed2",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6068", browseName="ns=pndrv;FrequencyCommandValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6068"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6069", browseName="ns=pndrv;VelocityActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6069"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6070", browseName="ns=pndrv;FrequencySetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6070"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6071", browseName="ns=pndrv;OutputFrequency", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6071"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6072", browseName="ns=pndrv;OutputVoltage", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6072"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5017",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6068"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6069"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6070"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6071"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6072"]),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6073", browseName="ns=pndrv;OutputCosPhi", dataType=o6.Float)),
    ],
)
o6.reference(pndrv_objtypes.FrequencyDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5017"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6015"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6029"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6030"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6031"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6032"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6033"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6034"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6035"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6074", browseName="ns=pndrv;Force", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6074"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6077", browseName="ns=pndrv;MotorCurrentLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6077"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6078", browseName="ns=pndrv;MotorCurrentLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6078"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6079", browseName="ns=pndrv;TorqueLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6079"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6080", browseName="ns=pndrv;TorqueLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6080"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5019",
    browseName="ns=pndrv;LimitSupervision",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6077"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6078"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6079"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6080"]),
    ],
)
o6.reference(pndrv_objtypes.FrequencyDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6076",
    browseName="ns=pndrv;ContouringError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6083", browseName="ns=pndrv;UnitOfLength", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6083"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5024", browseName="ns=pndrv;CharacteristicsMotorAndControl", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=pndrv;i=6083"])]
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5024"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6066",
    browseName="ns=pndrv;JogPosInc1",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5038",
    browseName="ns=pndrv;SOS",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6067", browseName="ns=pndrv;SOSSelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6086", browseName="ns=pndrv;SOSActive")),
    ],
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6087", browseName="ns=pndrv;PositionActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6087"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6088", browseName="ns=pndrv;PositionSetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6088"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6089", browseName="ns=pndrv;VelocityActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6089"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6090", browseName="ns=pndrv;AccelerationActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6090"], "i=46", "i=17502")
pndrv_vartypes.HomingDirectionType(nodeId="ns=pndrv;i=6091", browseName="ns=pndrv;HomingDirection", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6091"], "i=46", o6.ns["ns=pndrv;i=6257"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6085",
    browseName="ns=pndrv;JogPosInc2",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5011",
    browseName="ns=pndrv;VelocityProfile",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6063"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6064"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6066"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6085"]),
    ],
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5011"])
o6.reference(o6.ns["ns=pndrv;i=5011"], "i=47", o6.ns["ns=pndrv;i=6013"])
o6.reference(o6.ns["ns=pndrv;i=5011"], "i=47", o6.ns["ns=pndrv;i=6014"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6099", browseName="ns=pndrv;HomingSpeedToCam", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6099"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6101", browseName="ns=pndrv;JogSpeed1", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6101"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6102", browseName="ns=pndrv;MotorCurrentLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6102"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6103", browseName="ns=pndrv;MotorCurrentLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6103"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6104", browseName="ns=pndrv;TorqueLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6104"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6105", browseName="ns=pndrv;TorqueLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6105"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6106", browseName="ns=pndrv;SoftwareUpperPosLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6106"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6107", browseName="ns=pndrv;SoftwareLowerPosLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6107"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6108", browseName="ns=pndrv;Gearfactor", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6108"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6109", browseName="ns=pndrv;SpindlePitch", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6109"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6100",
    browseName="ns=pndrv;HomingSpeedToMark",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6113", browseName="ns=pndrv;VelocitySetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6113"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6114", browseName="ns=pndrv;VelocityCommandValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6114"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6115", browseName="ns=pndrv;VelocityActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6115"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6116", browseName="ns=pndrv;AccelerationActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6116"], "i=46", "i=17502")
ns0.vartypes.MultiStateDiscreteType(nodeId="ns=pndrv;i=6117", browseName="ns=pndrv;BrakeStatus", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6117"], "i=46", "i=2377")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5028",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6113"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6114"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6115"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6116"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6117"]),
    ],
)
o6.reference(pndrv_objtypes.VelocityServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5028"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6015"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6029"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6030"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6031"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6032"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6033"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6034"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6035"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6118", browseName="ns=pndrv;TorqueLimitHigh", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6118"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6119", browseName="ns=pndrv;TorqueLimitLow", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6119"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5029",
    browseName="ns=pndrv;LimitSupervision",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6075", browseName="ns=pndrv;TorqueLimiting", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=pndrv;i=6118"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6119"]),
    ],
)
o6.reference(pndrv_objtypes.VelocityServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5029"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6111",
    browseName="ns=pndrv;HomingPointOffset",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6120", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
pndrv_vartypes.HomingModeType(nodeId="ns=pndrv;i=6121", browseName="ns=pndrv;HomingMode", dataType=o6.Byte)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5030",
    browseName="ns=pndrv;Homing",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6091"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6099"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6100"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6111"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6121"]),
    ],
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5030"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6125", browseName="ns=pndrv;PositionCommandValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6125"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6126", browseName="ns=pndrv;VelocitySetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6126"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6122",
    browseName="ns=pndrv;JogSpeed2",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6127", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6128", browseName="ns=pndrv;PositionActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6128"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6129", browseName="ns=pndrv;VelocityActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6129"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6130", browseName="ns=pndrv;PositionSetpoint", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6130"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6131", browseName="ns=pndrv;AccelerationActualValue", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6131"], "i=46", "i=17502")
ns0.vartypes.MultiStateDiscreteType(nodeId="ns=pndrv;i=6132", browseName="ns=pndrv;BrakeStatus", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6132"], "i=46", "i=2377")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5037",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6076"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6125"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6126"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6128"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6129"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6130"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6131"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6132"]),
    ],
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5037"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6015"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6029"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6030"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6031"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6032"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6033"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6034"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6035"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6133", browseName="ns=pndrv;TorqueLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6133"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6134", browseName="ns=pndrv;SoftwareUpperPosLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6134"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6135", browseName="ns=pndrv;SoftwareLowerPosLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6135"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5036",
    browseName="ns=pndrv;LimitSupervision",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6082", browseName="ns=pndrv;TorqueLimiting", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=pndrv;i=6133"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6134"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6135"]),
    ],
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5036"])
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5039",
    browseName="ns=pndrv;SLS",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6112", browseName="ns=pndrv;SLSSelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6124", browseName="ns=pndrv;SLSActive")),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6138", browseName="ns=pndrv;SLSLimit", dataType=ns0.datatypes.Number)),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5040",
    browseName="ns=pndrv;SDI",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6140", browseName="ns=pndrv;SDISelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6141", browseName="ns=pndrv;SDIActive")),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5041",
    browseName="ns=pndrv;SLA",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6142", browseName="ns=pndrv;SLASelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6143", browseName="ns=pndrv;SLAActive")),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6144", browseName="ns=pndrv;SLALimit", dataType=ns0.datatypes.Number)),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5042",
    browseName="ns=pndrv;SLP",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6145", browseName="ns=pndrv;SLPSelection")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6146", browseName="ns=pndrv;SLPActive")),
    ],
)
safety = ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5008",
    browseName="ns=pndrv;Safety",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=5012"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5013"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5015"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5038"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5039"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5040"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5041"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=5042"]),
    ],
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6139",
    browseName="ns=pndrv;ControlPriority",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6149",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    o6.LocalizedText("NONE", "en"),
                    o6.LocalizedText("PROFIBUS_PRIORITY", "en"),
                    o6.LocalizedText("PROFIBUS_CONTROL", "en"),
                    o6.LocalizedText("PROFINET_PRIORITY", "en"),
                    o6.LocalizedText("PROFINET_CONTROL", "en"),
                    o6.LocalizedText("LOCAL_CONTROL", "en"),
                    o6.LocalizedText("SETUP_TOOL_CONTROL", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
    value=0,
)
o6.reference(o6.ns["ns=pndrv;i=5014"], "i=47", o6.ns["ns=pndrv;i=6139"])
o6.reference(o6.ns["ns=pndrv;i=5017"], "i=47", o6.ns["ns=pndrv;i=6139"])
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6139"])
o6.reference(o6.ns["ns=pndrv;i=5037"], "i=47", o6.ns["ns=pndrv;i=6139"])
pnenc.objtypes.EncoderSensorType(
    nodeId="ns=pndrv;i=5055",
    browseName="ns=pnenc;Sensor",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6156", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number))],
)
pnenc.objtypes.EncoderChannelType(
    nodeId="ns=pndrv;i=5054", browseName="ns=pndrv;EncoderChannelMechanic", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=pndrv;i=5055"])]
)
o6.reference(pndrv_objtypes.VelocityServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5054"])
o6.reference(o6.ns["ns=pndrv;i=5054"], "i=41", "ns=pnenc;i=1006")
pnenc.objtypes.EncoderSensorType(
    nodeId="ns=pndrv;i=5057",
    browseName="ns=pnenc;Sensor",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6157", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number))],
)
pnenc.objtypes.EncoderChannelType(
    nodeId="ns=pndrv;i=5056", browseName="ns=pndrv;<EncoderChannelAuxiliary>", modellingRule="OptionalPlaceholder", references=[o6.hasComponent(o6.ns["ns=pndrv;i=5057"])]
)
o6.reference(pndrv_objtypes.VelocityServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5056"])
o6.reference(o6.ns["ns=pndrv;i=5056"], "i=41", "ns=pnenc;i=1006")
pnenc.objtypes.EncoderSensorType(
    nodeId="ns=pndrv;i=5059",
    browseName="ns=pnenc;Sensor",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6158", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number))],
)
pnenc.objtypes.EncoderChannelType(
    nodeId="ns=pndrv;i=5058", browseName="ns=pndrv;EncoderChannelMechanic", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=pndrv;i=5059"])]
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5058"])
o6.reference(o6.ns["ns=pndrv;i=5058"], "i=41", "ns=pnenc;i=1006")
pnenc.objtypes.EncoderSensorType(
    nodeId="ns=pndrv;i=5061",
    browseName="ns=pnenc;Sensor",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6159", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number))],
)
pnenc.objtypes.EncoderChannelType(
    nodeId="ns=pndrv;i=5060", browseName="ns=pndrv;EncoderChannelMotor", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=pndrv;i=5061"])]
)
o6.reference(pndrv_objtypes.PositionServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5060"])
o6.reference(o6.ns["ns=pndrv;i=5060"], "i=41", "ns=pnenc;i=1006")
pndrv_vartypes.TemperatureVariableType(nodeId="ns=pndrv;i=6160", browseName="ns=pndrv;BrakeResistorTemperature", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6160"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5005",
    browseName="ns=pndrv;Maintenance",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6027",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the Device has been powered. The main purpose is to determine the time in which degradation of the Device occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the Device has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6036",
                browseName="ns=di;OperationDuration",
                description="OperationDuration is the duration the Device has been powered and performing an activity. This counter is intended for Devices where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for Devices always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6037",
                browseName="ns=di;OperationCycleCounter",
                description="OperationCycleCounter is counting the times the Device switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted.",
                dataType=ns0.datatypes.UInteger,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6161", browseName="ns=pndrv;MotorCapacityUtilization", dataType=o6.UInt16)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6162", browseName="ns=pndrv;ConverterCapacityUtilization", dataType=o6.UInt16)),
    ],
)
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5005"])
o6.reference(o6.ns["ns=pndrv;i=5005"], "i=17603", "ns=di;i=480")
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6154",
    browseName="ns=pndrv;ActivationState",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6165",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[17],
                value=[
                    o6.LocalizedText("NONE", "en"),
                    o6.LocalizedText("POWER_REMOVED", "en"),
                    o6.LocalizedText("SS1_ACTIVE", "en"),
                    o6.LocalizedText("SS1_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SS2_ACTIVE", "en"),
                    o6.LocalizedText("SS2_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SOS_ACTIVE", "en"),
                    o6.LocalizedText("SOS_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SLS_ACTIVE", "en"),
                    o6.LocalizedText("SLS_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SDI_POS_ACTIVE", "en"),
                    o6.LocalizedText("SDI_NEG_ACTIVE", "en"),
                    o6.LocalizedText("SLA_ACTIVE", "en"),
                    o6.LocalizedText("SLA_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SLP_ACTIVE", "en"),
                    o6.LocalizedText("SLP_ACTIVE_FAULTED", "en"),
                    o6.LocalizedText("SLP_INOPERABLE", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
)
o6.reference(pndrv_objtypes.SafetyFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5046"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5047"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5048"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5049"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5050"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5051"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5052"], "i=47", o6.ns["ns=pndrv;i=6154"])
o6.reference(o6.ns["ns=pndrv;i=5053"], "i=47", o6.ns["ns=pndrv;i=6154"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6151",
    browseName="ns=pndrv;SelectionState",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6166",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[10],
                value=[
                    o6.LocalizedText("NONE", "en"),
                    o6.LocalizedText("SELECTED", "en"),
                    o6.LocalizedText("SELECTED_INTERN", "en"),
                    o6.LocalizedText("SELECTED_EXTERN", "en"),
                    o6.LocalizedText("SELECTED_LIMIT_1", "en"),
                    o6.LocalizedText("SELECTED_LIMIT_2", "en"),
                    o6.LocalizedText("SELECTED_LIMIT_3", "en"),
                    o6.LocalizedText("SELECTED_LIMIT_4", "en"),
                    o6.LocalizedText("SELECTED_POS", "en"),
                    o6.LocalizedText("SELECTED_NEG", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
)
o6.reference(pndrv_objtypes.SafetyFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5046"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5047"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5048"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5049"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5050"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5051"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5052"], "i=47", o6.ns["ns=pndrv;i=6151"])
o6.reference(o6.ns["ns=pndrv;i=5053"], "i=47", o6.ns["ns=pndrv;i=6151"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6097",
    browseName="ns=pndrv;PositioningMode",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6168",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    o6.LocalizedText("INACTIVE", "en"),
                    o6.LocalizedText("RELATIVE_POSITIONING", "en"),
                    o6.LocalizedText("ABSOLUTE_SHORTEST_PATH_MODULO_DIRECTION _POSITIONING", "en"),
                    o6.LocalizedText("ABSOLUTE_POSITIVE_MODULO_DIRECTION _POSITIONING", "en"),
                    o6.LocalizedText("ABSOLUTE_NEGATIVE_ MODULO_DIRECTION _POSITIONING", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
)
o6.reference(pndrv_objtypes.TraversingTaskType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=6097"])
o6.reference(o6.ns["ns=pndrv;i=5023"], "i=47", o6.ns["ns=pndrv;i=6097"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6169", browseName="ns=pndrv;IntermediateCircuitVoltageConfigured", dataType=o6.UInt16)
o6.reference(o6.ns["ns=pndrv;i=6169"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6173", browseName="ns=pndrv;ConverterThermalLoadLimitConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6173"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6174", browseName="ns=pndrv;ConverterExcessCurrentConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=5035"], "i=47", o6.ns["ns=pndrv;i=6174"])
o6.reference(o6.ns["ns=pndrv;i=6174"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6175", browseName="ns=pndrv;BrakeResistorExcessCurrentLimit", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6175"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5009",
    browseName="ns=pndrv;CharacteristicsConverter",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6039"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6055"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6169"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6173"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6174"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6175"]),
    ],
)
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5009"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6176", browseName="ns=pndrv;PowerRated", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=5024"], "i=47", o6.ns["ns=pndrv;i=6176"])
o6.reference(o6.ns["ns=pndrv;i=6176"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6177", browseName="ns=pndrv;SpeedRated", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6177"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6180", browseName="ns=pndrv;TorqueRated", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6180"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6181",
    browseName="ns=pndrv;MaxCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6182", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6184",
    browseName="ns=pndrv;RunUpVoltage",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6186",
    browseName="ns=pndrv;DcBrakingCurrent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6188",
    browseName="ns=pndrv;DcBrakingTime",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.UInt16,
)
ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6193", browseName="ns=pndrv;NominalSpeed", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=5010"], "i=47", o6.ns["ns=pndrv;i=6193"])
o6.reference(o6.ns["ns=pndrv;i=5011"], "i=47", o6.ns["ns=pndrv;i=6193"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6192",
    browseName="ns=pndrv;FeedbackMode",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6194",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("FEEDBACK_SENSOR_1"), o6.LocalizedText("FEEDBACK_SENSOR_2"), o6.LocalizedText("FEEDBACK_SENSOR_3"), o6.LocalizedText("SENSORLESS")],
            )
        )
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6195", browseName="ns=pndrv;SpeedMaxConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6195"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6196", browseName="ns=pndrv;TorqueMaxConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6196"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6197", browseName="ns=pndrv;MotorThermalLoadLimitConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6197"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6198", browseName="ns=pndrv;MotorExcessCurrentConfigured", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6198"], "i=46", "i=17502")
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6199",
    browseName="ns=pndrv;MotorType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6200",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[10],
                value=[
                    o6.LocalizedText("PM_SYNCHRONOUS_ROTARY"),
                    o6.LocalizedText("PM_SYNCHRONOUS_LINEAR"),
                    o6.LocalizedText("STEPPER_ROTARY"),
                    o6.LocalizedText("STEPPER_LINEAR"),
                    o6.LocalizedText("INDUCTION_ROTATORY"),
                    o6.LocalizedText("INDUCTION_LINEAR"),
                    o6.LocalizedText("HYDRAULIC_MOTOR_ROTARY"),
                    o6.LocalizedText("HYDRAULIC_CYLINDER_LINEAR"),
                    o6.LocalizedText("PNEUMATIC_MOTOR_ROTARY"),
                    o6.LocalizedText("PNEUMATIC_CYLINDER_LINEAR", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=pndrv;i=5024"], "i=47", o6.ns["ns=pndrv;i=6199"])
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5022",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=5023"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6087"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6088"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6089"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6090"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6202", browseName="ns=pndrv;Override", dataType=o6.Float)),
    ],
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5022"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6015"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6029"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6030"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6031"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6032"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6033"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6034"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6035"])
o6.reference(o6.ns["ns=pndrv;i=5022"], "i=47", o6.ns["ns=pndrv;i=6139"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6203", browseName="ns=pndrv;RampDeceleration", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=5010"], "i=47", o6.ns["ns=pndrv;i=6203"])
o6.reference(o6.ns["ns=pndrv;i=5011"], "i=47", o6.ns["ns=pndrv;i=6203"])
o6.reference(o6.ns["ns=pndrv;i=6203"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6204", browseName="ns=pndrv;QuickStopRampDeceleration", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=5010"], "i=47", o6.ns["ns=pndrv;i=6204"])
o6.reference(o6.ns["ns=pndrv;i=5011"], "i=47", o6.ns["ns=pndrv;i=6204"])
o6.reference(o6.ns["ns=pndrv;i=6204"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5044",
    browseName="ns=pndrv;VelocityProfile",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6013"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6014"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6193"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6203"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6204"]),
    ],
)
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5044"])
pndrv_vartypes.TemperatureVariableType(
    nodeId="ns=pndrv;i=6019",
    browseName="ns=pndrv;FeedbackSensor1Temperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
pndrv_vartypes.TemperatureVariableType(
    nodeId="ns=pndrv;i=6208",
    browseName="ns=pndrv;FeedbackSensor2Temperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
pndrv_vartypes.TemperatureVariableType(
    nodeId="ns=pndrv;i=6210",
    browseName="ns=pndrv;FeedbackSensor3Temperature",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6212",
    browseName="ns=pndrv;VelocityFollowingError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6213", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=pndrv;i=5028"], "i=47", o6.ns["ns=pndrv;i=6212"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6215",
    browseName="ns=pndrv;ForceRated",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6217",
    browseName="ns=pndrv;PositionFollowingErrorLimit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6218", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6219",
    browseName="ns=pndrv;VelocityFollowingErrorLimit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5003",
    browseName="ns=pndrv;CharacteristicsMotorAndControl",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6183", browseName="ns=pndrv;UfRatio", dataType=o6.Float)),
        o6.hasComponent(o6.ns["ns=pndrv;i=6176"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6177"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6180"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6181"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6184"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6186"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6188"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6192"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6195"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6196"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6197"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6198"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6199"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6215"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6217"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6219"]),
    ],
)
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5003"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6221",
    browseName="ns=pndrv;FeedbackMode",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6222",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    o6.LocalizedText("FEEDBACK_SENSOR_1", "en"),
                    o6.LocalizedText("FEEDBACK_SENSOR_2", "en"),
                    o6.LocalizedText("FEEDBACK_SENSOR_3", "en"),
                    o6.LocalizedText("SENSORLESS", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6170",
    browseName="ns=pndrv;RfgAcceleration",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6224",
    browseName="ns=pndrv;MinimumVelocity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6226",
    browseName="ns=pndrv;MaximumVelocity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6228", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5018",
    browseName="ns=pndrv;VelocityProfile",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6101"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6122"]),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pndrv;i=6137", browseName="ns=pndrv;RfgRampUpTime", dataType=o6.Float)),
        o6.hasComponent(o6.ns["ns=pndrv;i=6170"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6224"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6226"]),
    ],
)
o6.reference(pndrv_objtypes.VelocityDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5018"])
o6.reference(o6.ns["ns=pndrv;i=5018"], "i=47", o6.ns["ns=pndrv;i=6013"])
o6.reference(o6.ns["ns=pndrv;i=5018"], "i=47", o6.ns["ns=pndrv;i=6014"])
o6.reference(o6.ns["ns=pndrv;i=5018"], "i=47", o6.ns["ns=pndrv;i=6193"])
o6.reference(o6.ns["ns=pndrv;i=5018"], "i=47", o6.ns["ns=pndrv;i=6203"])
o6.reference(o6.ns["ns=pndrv;i=5018"], "i=47", o6.ns["ns=pndrv;i=6204"])
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5021",
    browseName="ns=pndrv;LimitSupervision",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6102"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6103"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6104"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6105"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6106"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6107"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6245", browseName="ns=pndrv;TorqueLimiting", dataType=o6.Boolean)),
    ],
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5021"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pndrv;i=6246",
    browseName="ns=pndrv;BrakeStatus",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pndrv;i=6247",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    o6.LocalizedText("NO_BRAKE", "en"),
                    o6.LocalizedText("OPEN_BRAKE", "en"),
                    o6.LocalizedText("MECHANIC_BRAKE_APPLIED", "en"),
                    o6.LocalizedText("DC_BRAKE_APPLIED", "en"),
                    o6.LocalizedText("ROTOR_SHORT_APPLIED", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5001",
    browseName="ns=pndrv;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6015"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6016"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6017"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6019"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6029"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6030"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6031"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6032"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6033"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6034"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6035"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6053"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6074"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6139"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6160"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6208"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6210"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6212"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6221"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6246"]),
    ],
)
o6.reference(pndrv_objtypes.DriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5001"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6255",
    browseName="ns=pndrv;UnitOfLength",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6256", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5026",
    browseName="ns=pndrv;CharacteristicsMechanics",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=pndrv;i=6108"]), o6.hasComponent(o6.ns["ns=pndrv;i=6109"]), o6.hasComponent(o6.ns["ns=pndrv;i=6255"])],
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5026"])
ns0.vartypes.PropertyType(
    nodeId="ns=pndrv;i=6258",
    browseName="EnumStrings",
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("ABSOLUTE"), o6.LocalizedText("REF_MARK"), o6.LocalizedText("DIST_CODE"), o6.LocalizedText("FLY")],
)
o6.reference(pndrv_vartypes.HomingModeType, "i=46", "ns=pndrv;i=6258")
o6.reference(o6.ns["ns=pndrv;i=6121"], "i=46", o6.ns["ns=pndrv;i=6258"])
pndrv_vartypes.HomingModeType(nodeId="ns=pndrv;i=6123", browseName="ns=pndrv;HomingMode", references=[o6.hasProperty(o6.ns["ns=pndrv;i=6258"])], dataType=o6.Byte)
ns0.objtypes.FolderType(nodeId="ns=pndrv;i=5032", browseName="ns=pndrv;Homing", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=pndrv;i=6123"])])
o6.reference(pndrv_objtypes.VelocityServoDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5032"])
pndrv_vartypes.HomingDirectionType(nodeId="ns=pndrv;i=6259", browseName="ns=pndrv;HomingDirection", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6259"], "i=46", o6.ns["ns=pndrv;i=6257"])
pndrv_vartypes.HomingModeType(nodeId="ns=pndrv;i=6260", browseName="ns=pndrv;HomingMode", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6260"], "i=46", o6.ns["ns=pndrv;i=6258"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6262", browseName="ns=pndrv;HomingSpeedToCam", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6262"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6264",
    browseName="ns=pndrv;HomingSpeedToMark",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6265", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pndrv;i=6266",
    browseName="ns=pndrv;HomingPointOffset",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6267", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5020",
    browseName="ns=pndrv;Homing",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=pndrv;i=6259"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6260"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6262"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6264"]),
        o6.hasComponent(o6.ns["ns=pndrv;i=6266"]),
    ],
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5020"])
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6274", browseName="ns=pndrv;UnitOfLength", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6274"], "i=46", "i=17502")
ns0.objtypes.FolderType(
    nodeId="ns=pndrv;i=5043", browseName="ns=pndrv;CharacteristicsMotorAndControl", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=pndrv;i=6274"])]
)
o6.reference(pndrv_objtypes.PositioningDriveAxisType, ns0.reftypes.HasComponent, o6.ns["ns=pndrv;i=5043"])
o6.reference(o6.ns["ns=pndrv;i=5043"], "i=47", o6.ns["ns=pndrv;i=6176"])
o6.reference(o6.ns["ns=pndrv;i=5043"], "i=47", o6.ns["ns=pndrv;i=6199"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnenc, pndrv_vartypes, pndrv_objtypes
