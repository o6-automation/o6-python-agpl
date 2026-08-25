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

"""Generated OPC UA ijt_base namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as ijt_base_datypes
from . import vartypes as ijt_base_vartypes
from . import objtypes as ijt_base_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5046", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5047", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningResultMetaDataType, o6.ns["ns=ijt_base;i=5047"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5048", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.CalibrationDataType, o6.ns["ns=ijt_base;i=5048"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5049", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5050", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningResultDataType, o6.ns["ns=ijt_base;i=5050"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5051", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.DesignValueDataType, o6.ns["ns=ijt_base;i=5051"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5053", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5054", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.ErrorInformationDataType, o6.ns["ns=ijt_base;i=5054"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5055", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.EntityDataType, o6.ns["ns=ijt_base;i=5055"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5056", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5057", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.ResultValueDataType, o6.ns["ns=ijt_base;i=5057"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5058", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.ErrorInformationDataType, o6.ns["ns=ijt_base;i=5058"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5059", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5060", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.StepResultDataType, o6.ns["ns=ijt_base;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5061", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningProcessDataType, o6.ns["ns=ijt_base;i=5061"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5062", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5063", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.TraceDataType, o6.ns["ns=ijt_base;i=5063"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5064", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningProcessIdentificationDataType, o6.ns["ns=ijt_base;i=5064"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5065", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5066", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningTraceDataType, o6.ns["ns=ijt_base;i=5066"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5067", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningProcessMetaDataType, o6.ns["ns=ijt_base;i=5067"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5068", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5069", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.StepTraceDataType, o6.ns["ns=ijt_base;i=5069"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5070", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningResultDataType, o6.ns["ns=ijt_base;i=5070"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5071", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5072", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.TraceContentDataType, o6.ns["ns=ijt_base;i=5072"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5073", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JointComponentDataType, o6.ns["ns=ijt_base;i=5073"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5075", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.CalibrationDataType, o6.ns["ns=ijt_base;i=5075"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5076", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JointDataType, o6.ns["ns=ijt_base;i=5076"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5079", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5081", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5082", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5083", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.DesignValueDataType, o6.ns["ns=ijt_base;i=5083"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5084", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.EntityDataType, o6.ns["ns=ijt_base;i=5084"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5085", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JointDesignDataType, o6.ns["ns=ijt_base;i=5085"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5086", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.KeyValueDataType, o6.ns["ns=ijt_base;i=5086"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5089", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5090", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.ResultCounterDataType, o6.ns["ns=ijt_base;i=5090"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5091", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.ReportedValueDataType, o6.ns["ns=ijt_base;i=5091"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5095", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5096", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.ReportedValueDataType, o6.ns["ns=ijt_base;i=5096"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5097", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.ResultCounterDataType, o6.ns["ns=ijt_base;i=5097"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5099", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningResultMetaDataType, o6.ns["ns=ijt_base;i=5099"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5103", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.ResultValueDataType, o6.ns["ns=ijt_base;i=5103"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5104", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5105", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JointComponentDataType, o6.ns["ns=ijt_base;i=5105"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5106", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.SignalDataType, o6.ns["ns=ijt_base;i=5106"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5107", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5108", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JointDesignDataType, o6.ns["ns=ijt_base;i=5108"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5109", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.StepResultDataType, o6.ns["ns=ijt_base;i=5109"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5110", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5111", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JointDataType, o6.ns["ns=ijt_base;i=5111"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5112", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.StepTraceDataType, o6.ns["ns=ijt_base;i=5112"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5115", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5116", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningProcessDataType, o6.ns["ns=ijt_base;i=5116"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5117", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.TraceContentDataType, o6.ns["ns=ijt_base;i=5117"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5118", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5119", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningProcessMetaDataType, o6.ns["ns=ijt_base;i=5119"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5120", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.TraceDataType, o6.ns["ns=ijt_base;i=5120"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5121", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5122", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.JoiningProcessIdentificationDataType, o6.ns["ns=ijt_base;i=5122"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5123", browseName="Default JSON")
o6.hasEncoding(ijt_base_datypes.JoiningTraceDataType, o6.ns["ns=ijt_base;i=5123"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5125", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.SignalDataType, o6.ns["ns=ijt_base;i=5125"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5148", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ijt_base;i=5149", browseName="Default XML")
o6.hasEncoding(ijt_base_datypes.KeyValueDataType, o6.ns["ns=ijt_base;i=5149"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6013",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6014",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6021",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6022",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=ijt_base;i=5003",
    browseName="ns=ijt_base;Calibration",
    description="The Calibration Object provides a set of parameters related to the calibration operations performed on a given asset.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6019",
                browseName="ns=ijt_base;LastCalibration",
                description="LastCalibration is the date when the last calibration was completed.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("2000-01-01T00:00:00Z"),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6020",
                browseName="ns=ijt_base;NextCalibration",
                description="NextCalibration is the date of the next planned calibration.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("2000-01-01T00:00:00Z"),
            )
        ),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6028",
                browseName="ns=ijt_base;CalibrationValue",
                description="CalibrationValue is the configured value of the calibration.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6036",
                browseName="ns=ijt_base;SensorScale",
                description="SensorScale is the nominal scale of the sensor. It corresponds also with the measurement range of the sensor.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6037",
                browseName="ns=ijt_base;CalibrationPlace",
                description="CalibrationPlace is the location where the last calibration was completed.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6038",
                browseName="ns=ijt_base;CertificateUri",
                description="CertificateUri contains the URI of a certificate of the calibration target in case the calibration target is certified and the information available. Otherwise, the Variable should be omitted. The String shall be a URI as defined by RFC 3986. Example: MCE test document.",
                dataType=ns0.datatypes.UriString,
                value="",
            )
        ),
    ],
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6035",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6045",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6060",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6065",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6073",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6074",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=ijt_base;i=5045",
    browseName="ns=ijt_base;Health",
    description="The Health Object is an instance of FunctionalGroupType to group health related parameters for all the assets in a Joining System.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5114", browseName="ns=di;DeviceHealthAlarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6005",
                browseName="ns=di;DeviceHealth",
                description="DeviceHealth indicates the status as defined by NAMUR Recommendation NE107. Clients can read or monitor this Variable to determine the device condition.",
                dataType=di.datatypes.DeviceHealthEnumeration,
                value=di.datatypes.DeviceHealthEnumeration.NORMAL,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6077",
                browseName="ns=ijt_base;ErrorMessage",
                description="ErrorMessage is the user readable text of the error reported by the given asset.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6082",
                browseName="ns=ijt_base;ErrorTimestamp",
                description="ErrorTimestamp is the timestamp when the error occurred in the given asset.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("2000-01-01T00:00:00Z"),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6083",
                browseName="ns=ijt_base;ErrorCode",
                description="ErrorCode is the system specific code for the error occurred.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6090",
                browseName="ns=ijt_base;Temperature",
                description="Temperature is the measured temperature of the asset.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5045"])
o6.reference(o6.ns["ns=ijt_base;i=5045"], "i=17603", "ns=di;i=15051")
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5015",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6008",
                browseName="ns=ijt_base;Enabled",
                description="Enabled indicates if a given asset is enabled or disabled. It can change by EnableAsset method or by some other external interface.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6044",
                browseName="ns=ijt_base;IOSignals",
                description="IOSignals is an array of signals available for the asset.",
                dataType=ijt_base_datypes.SignalDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6091",
                browseName="ns=ijt_base;Connected",
                description="Connected indicates if a given asset is connected or disconnected. It can change by DisconnectAsset method or by some other external interface.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5015"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=ijt_base;i=5020",
    browseName="ns=ijt_base;Service",
    description="The Service Object provides a set of parameters related to the service operations performed on a given asset.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6049",
                browseName="ns=ijt_base;ServiceReminderCycles",
                description="ServiceReminderCycles is the configured threshold for the number of remaining cycles before the service reminder is sent. This is calculated based on the RemainingCycles.",
                dataType=o6.Int32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6050",
                browseName="ns=ijt_base;ServiceOperationCycles",
                description="ServiceOperationCycles is the value of the 2:OperationCycleCounter when the last service was performed.",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6075",
                browseName="ns=ijt_base;LastService",
                description="LastService is the date when the last service was completed.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("2000-01-01T00:00:00Z"),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6076",
                browseName="ns=ijt_base;ServicePlace",
                description="ServicePlace is the location where the last service was completed.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6089",
                browseName="ns=ijt_base;NextService",
                description="NextService is the date of the next planned service.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("2000-01-01T00:00:00Z"),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6092",
                browseName="ns=ijt_base;ServiceCycleSpan",
                description="ServiceCycleSpan is the maximum allowed number of cycles between two services.",
                dataType=o6.Int32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6093",
                browseName="ns=ijt_base;ServiceCycleCount",
                description="ServiceCycleCount is the total cycle counter since the last service.",
                dataType=o6.Int32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6094",
                browseName="ns=ijt_base;NumberOfServices",
                description="NumberOfServices is the total number of services taken place.",
                dataType=o6.Int32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6109",
                browseName="ns=ijt_base;ServiceReminderDays",
                description="ServiceReminderDays is the number of days before a service reminder should be sent.",
                dataType=o6.Int16,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6110",
                browseName="ns=ijt_base;RemainingCycles",
                description="RemainingCycles is the remaining cycles before the service or maintenance. It can go negative if a service is skipped to indicate overshoot cycles.",
                dataType=o6.Int32,
                value=0,
            )
        ),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=ijt_base;i=5027",
    browseName="ns=di;Maintenance",
    description="The Maintenance Object is an instance of FunctionalGroupType to group maintenance related parameters for the given asset in a Joining System.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5003"]), o6.hasComponent(o6.ns["ns=ijt_base;i=5020"])],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5027"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5024",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6117",
                browseName="ns=ijt_base;Type",
                description="Type is a user readable open string to describe the type of accessory such as socket selector, operator panel, etc.",
                dataType=o6.String,
                value="",
            )
        )
    ],
)
o6.reference(ijt_base_objtypes.IAccessoryType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5024"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5007",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6118",
                browseName="ns=ijt_base;NodeNumber",
                description="NodeNumber is the node identifier in multiple configurations. Examples: Cabinet with one controller and multiple servo/modules.",
                dataType=o6.Int16,
                value=0,
            )
        )
    ],
)
o6.reference(ijt_base_objtypes.IServoType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5007"])
ijt_base_vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_base;i=6119",
    browseName="ns=ijt_base;NominalVoltage",
    description="NominalVoltage is the nominal DC voltage of the battery.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6015",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6021"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=ijt_base;i=5002",
    browseName="ns=di;OperationCounters",
    description="It provides information about the duration something is turned on and how long it performs an activity.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6017",
                browseName="ns=di;OperationCycleCounter",
                description="OperationCycleCounter is counting the times the component switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the component and shall not be reset when the component is restarted.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6108",
                browseName="ns=di;OperationDuration",
                description="OperationDuration is the duration the MachineryItem has been powered and performing an activity. This counter is intended for machines and components where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for machines or components always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6120",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5002"])
o6.reference(o6.ns["ns=ijt_base;i=5002"], "i=17603", "ns=di;i=480")
o6.reference(o6.ns["ns=ijt_base;i=5080"], "i=17604", o6.ns["ns=ijt_base;i=5002"])
ijt_base_vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_base;i=6121",
    browseName="ns=ijt_base;Capacity",
    description="Capacity is the nominal capacity of the battery.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6012",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6013"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5009",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=6119"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6121"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6122",
                browseName="ns=ijt_base;ChargeCycleCount",
                description="ChargeCycleCount is the number of times the battery has been charged since the initial operation date.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6123",
                browseName="ns=ijt_base;StateOfCharge",
                description="StateOfCharge is the state of charge (SOC) indicator functions as a sort of fuel gauge that displays the usable amount of energy. This helps determine optimal charging and discharging. It is given in percentage.",
                dataType=o6.Byte,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6125",
                browseName="ns=ijt_base;StateOfHealth",
                description="StateOfHealth is the State of Health is a measurement that reflects the general condition of a battery and its ability to deliver the specified performance compared with a fresh battery. It considers such factors as charge acceptance, internal resistance, voltage, and self-discharge. It is given in percentage.",
                dataType=o6.Byte,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6126",
                browseName="ns=ijt_base;Type",
                description="Type is a user readable text to determine the type of battery such as pack type, technology, chemical composition, battery standard, etc.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IBatteryType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5009"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6128",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of a Controller.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6129",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("SUPERVISORY_CONTROLLER"),
                    o6.LocalizedText("PLC"),
                    o6.LocalizedText("COMPUTER"),
                    o6.LocalizedText("JOINING_PROCESS_CONTROLLER"),
                    o6.LocalizedText("COMMUNICATION_CONTROLLER"),
                    o6.LocalizedText("FEEDING_CONTROLLER"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5006",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=6128"])],
)
o6.reference(ijt_base_objtypes.IControllerType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5006"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6130",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of the cable.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6131",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[7],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TOOL_CABLE"),
                    o6.LocalizedText("SENSOR_CABLE"),
                    o6.LocalizedText("COMMUNICATION_CABLE"),
                    o6.LocalizedText("POWER_CABLE"),
                    o6.LocalizedText("IO_CABLE"),
                    o6.LocalizedText("BUS_CABLE"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5010",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=6130"]),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6132", browseName="ns=ijt_base;CableLength", description="CableLength is the length of the cable.", dataType=o6.Double, value=0.0
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.ICableType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5010"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6133",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of a Tool.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6134",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("OTHER"), o6.LocalizedText("FIXTURED"), o6.LocalizedText("HANDHELD"), o6.LocalizedText("MANUAL")],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5008",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=6133"])],
)
o6.reference(ijt_base_objtypes.IToolType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5008"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5052",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6006",
                browseName="ns=ijt_base;Description",
                description="Description is the system specific description of the asset.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6016",
                browseName="ns=ijt_base;JoiningTechnology",
                description="JoiningTechnology is a human readable text to identify the joining technology.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6018",
                browseName="ns=ijt_base;SupplierCode",
                description="SupplierCode is the SAP or ERP Supplier Code of the asset.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6142",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6143",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5052"])
o6.reference(o6.ns["ns=ijt_base;i=5052"], "i=17603", ijt_base_objtypes.IJoiningAdditionalInformationType)
o6.reference(o6.ns["ns=ijt_base;i=5080"], "i=17604", o6.ns["ns=ijt_base;i=5052"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6146",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of a Feeder.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6147",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("BOWL"),
                    o6.LocalizedText("BUNKER"),
                    o6.LocalizedText("CONVEYOR"),
                    o6.LocalizedText("DRUM"),
                    o6.LocalizedText("LINEAR"),
                    o6.LocalizedText("SWORD"),
                    o6.LocalizedText("TAPE"),
                    o6.LocalizedText("MAGAZINE"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ijt_base_vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_base;i=6149",
    browseName="ns=ijt_base;FeedingSpeed",
    description="FeedingSpeed indicates the output in parts per time. Example: fasteners / second.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6033",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6035"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5011",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6145",
                browseName="ns=ijt_base;Material",
                description="Material is the type or name of the part which is supplied by the feeder.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6146"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6148",
                browseName="ns=ijt_base;FillLevel",
                description="FillLevel is the fill level in the feeder in percentage [%]. (0%=empty, 100% = full).",
                dataType=o6.Byte,
                value=0,
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6149"]),
    ],
)
o6.reference(ijt_base_objtypes.IFeederType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5011"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5013",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6150",
                browseName="ns=ijt_base;Type",
                description="Type is the type of memory device. It may define the form factor, interface, or technology. Examples: Flash, CFAST, USB, etc.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6154",
                browseName="ns=ijt_base;StorageCapacity",
                description="StorageCapacity is the static information on size of the storage in Bytes.",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6155",
                browseName="ns=ijt_base;UsedSpace",
                description="UsedSpace is the static information on size of the used space in Bytes.",
                dataType=o6.UInt64,
                value=0,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IMemoryDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5013"])
ijt_base_vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_base;i=6157",
    browseName="ns=ijt_base;NominalPower",
    description="NominalPower is the maximum output power of the power supply.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6066",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6073"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
ijt_base_vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_base;i=6158",
    browseName="ns=ijt_base;ActualPower",
    description="ActualPower is the actual load consumption of the power supply.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6054",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6060"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=ijt_base;i=6164",
    browseName="ns=machinery;<LifetimeVariable>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6165", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6166",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6167",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=ijt_base;i=5147",
    browseName="ns=machinery;LifetimeCounters",
    description="It provides an entry point to various lifetime variables.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=6164"])],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5147"])
o6.reference(o6.ns["ns=ijt_base;i=5080"], "i=17604", o6.ns["ns=ijt_base;i=5147"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6169",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of a Sensor.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6170",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[27],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6172", browseName="ns=ijt_base;CalibrationDataType", dataType=o6.String, value="CalibrationDataType")
o6.reference(o6.ns["ns=ijt_base;i=5017"], "i=39", o6.ns["ns=ijt_base;i=6172"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ijt_base;i=6003",
    browseName="ns=machinery_result;ResultMetaData",
    modellingRule="Mandatory",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6010",
                browseName="ns=ijt_base;OperationMode",
                description="It provides information on how the joining operation was performed.",
                dataType=o6.Byte,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6098",
                browseName="ns=ijt_base;JoiningTechnology",
                description="It is a human readable text to identify the joining technology.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6099",
                browseName="ns=ijt_base;SequenceNumber",
                description="It is a human readable text to identify the joining technology.",
                dataType=o6.Int64,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6100", browseName="ns=ijt_base;Name", description="It is the user-friendly name of the result.", dataType=o6.String, value=""
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6101",
                browseName="ns=ijt_base;Description",
                description="It is the additional information associated with the result. It can contain information on the ResultContent.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6124",
                browseName="ns=ijt_base;Classification",
                description="It provides information on the classification of the result in the joining system.",
                dataType=o6.Byte,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6135",
                browseName="ns=ijt_base;InterventionType",
                description="It provides information on type of intervention which has occurred during the joining operation.",
                dataType=o6.Byte,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6136",
                browseName="ns=ijt_base;IsGeneratedOffline",
                description="It indicates that the result is generated when the asset was offline. The default value is false.\nNote: The definition of offline status is application specific.\nExample: Wireless tool performing joining in radio shadow.",
                dataType=o6.Boolean,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6137",
                browseName="ns=ijt_base;AssociatedEntities",
                description="It is a list of identifiers associated to the given result. \nExamples: ProductId, VIN, SocketId, JointId, JoiningProcessId, etc.",
                dataType=ijt_base_datypes.EntityDataType,
                valueRank=1,
                arrayDimensions=[0],
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6138",
                browseName="ns=ijt_base;ResultCounters",
                description="It is a list of counters associated to the given result. \nExamples: Batch Counter, Retry Counter, Channel Counter, etc.",
                dataType=ijt_base_datypes.ResultCounterDataType,
                valueRank=1,
                arrayDimensions=[0],
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6139", browseName="ns=ijt_base;AssemblyType", description="It provides the type of joining operation.", dataType=o6.Byte, value=0
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6160",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                value="",
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6173",
                browseName="ns=ijt_base;ExtendedMetaData",
                description="It is used to send any additional meta data which cannot be sent using the existing properties. It shall be used only for sending meta data but not any content.",
                dataType=ijt_base_datypes.KeyValueDataType,
                valueRank=1,
                arrayDimensions=[0],
            ),
            "i=24136",
        ),
    ],
    dataType=ijt_base_datypes.JoiningResultMetaDataType,
)
o6.reference(ijt_base_vartypes.JoiningSystemResultType, ns0.reftypes.HasStructuredComponent, o6.ns["ns=ijt_base;i=6003"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6174", browseName="ns=ijt_base;CalibrationDataType", dataType=o6.String, value="//xs:element[@name='CalibrationDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5075"], "i=39", o6.ns["ns=ijt_base;i=6174"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6178", browseName="ns=ijt_base;DesignValueDataType", dataType=o6.String, value="DesignValueDataType")
o6.reference(o6.ns["ns=ijt_base;i=5082"], "i=39", o6.ns["ns=ijt_base;i=6178"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6179", browseName="ns=ijt_base;DesignValueDataType", dataType=o6.String, value="//xs:element[@name='DesignValueDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5083"], "i=39", o6.ns["ns=ijt_base;i=6179"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6180", browseName="ns=ijt_base;EntityDataType", dataType=o6.String, value="EntityDataType")
o6.reference(o6.ns["ns=ijt_base;i=5079"], "i=39", o6.ns["ns=ijt_base;i=6180"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6181", browseName="ns=ijt_base;EntityDataType", dataType=o6.String, value="//xs:element[@name='EntityDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5084"], "i=39", o6.ns["ns=ijt_base;i=6181"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6182", browseName="ns=ijt_base;ErrorInformationDataType", dataType=o6.String, value="ErrorInformationDataType")
o6.reference(o6.ns["ns=ijt_base;i=5053"], "i=39", o6.ns["ns=ijt_base;i=6182"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5019",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6185",
                browseName="ns=ijt_base;Type",
                description="Type is a user readable open string to describe the type of subcomponent such as network module, etc.",
                dataType=o6.String,
                value="",
            )
        )
    ],
)
o6.reference(ijt_base_objtypes.ISubComponentType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5019"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6187", browseName="ns=ijt_base;ErrorInformationDataType", dataType=o6.String, value="//xs:element[@name='ErrorInformationDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5054"], "i=39", o6.ns["ns=ijt_base;i=6187"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6188", browseName="ns=ijt_base;JoiningProcessDataType", dataType=o6.String, value="JoiningProcessDataType")
o6.reference(o6.ns["ns=ijt_base;i=5115"], "i=39", o6.ns["ns=ijt_base;i=6188"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6189", browseName="ns=ijt_base;JoiningProcessDataType", dataType=o6.String, value="//xs:element[@name='JoiningProcessDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5116"], "i=39", o6.ns["ns=ijt_base;i=6189"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6190", browseName="ns=ijt_base;JoiningProcessIdentificationDataType", dataType=o6.String, value="JoiningProcessIdentificationDataType"
)
o6.reference(o6.ns["ns=ijt_base;i=5121"], "i=39", o6.ns["ns=ijt_base;i=6190"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6198",
    browseName="ns=ijt_base;JoiningProcessIdentificationDataType",
    dataType=o6.String,
    value="//xs:element[@name='JoiningProcessIdentificationDataType']",
)
o6.reference(o6.ns["ns=ijt_base;i=5122"], "i=39", o6.ns["ns=ijt_base;i=6198"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6199", browseName="ns=ijt_base;JoiningProcessMetaDataType", dataType=o6.String, value="JoiningProcessMetaDataType")
o6.reference(o6.ns["ns=ijt_base;i=5118"], "i=39", o6.ns["ns=ijt_base;i=6199"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6200", browseName="ns=ijt_base;JoiningProcessMetaDataType", dataType=o6.String, value="//xs:element[@name='JoiningProcessMetaDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5119"], "i=39", o6.ns["ns=ijt_base;i=6200"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6201", browseName="ns=ijt_base;JoiningResultDataType", dataType=o6.String, value="JoiningResultDataType")
o6.reference(o6.ns["ns=ijt_base;i=5049"], "i=39", o6.ns["ns=ijt_base;i=6201"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6202", browseName="ns=ijt_base;JoiningResultDataType", dataType=o6.String, value="//xs:element[@name='JoiningResultDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5050"], "i=39", o6.ns["ns=ijt_base;i=6202"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6203", browseName="ns=ijt_base;JointComponentDataType", dataType=o6.String, value="JointComponentDataType")
o6.reference(o6.ns["ns=ijt_base;i=5104"], "i=39", o6.ns["ns=ijt_base;i=6203"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6204", browseName="ns=ijt_base;JointComponentDataType", dataType=o6.String, value="//xs:element[@name='JointComponentDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5105"], "i=39", o6.ns["ns=ijt_base;i=6204"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6205", browseName="ns=ijt_base;JointDataType", dataType=o6.String, value="JointDataType")
o6.reference(o6.ns["ns=ijt_base;i=5110"], "i=39", o6.ns["ns=ijt_base;i=6205"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6206", browseName="ns=ijt_base;JointDataType", dataType=o6.String, value="//xs:element[@name='JointDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5111"], "i=39", o6.ns["ns=ijt_base;i=6206"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ijt_base;i=6002",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6004", browseName="ns=ijt_base;AssemblyType", description="It provides the type of joining operation.", dataType=o6.Byte, value=0
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6007",
                browseName="ns=ijt_base;AssociatedEntities",
                description="It is a list of identifiers associated to the given result. \nExamples: ProductId, VIN, SocketId, JointId, JoiningProcessId, etc.",
                dataType=ijt_base_datypes.EntityDataType,
                valueRank=1,
                arrayDimensions=[0],
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6009",
                browseName="ns=ijt_base;Classification",
                description="It provides information on the classification of the result in the joining system.",
                dataType=o6.Byte,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6011",
                browseName="ns=ijt_base;Description",
                description="It is the additional information associated with the result. It can contain information on the ResultContent.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6023",
                browseName="ns=ijt_base;InterventionType",
                description="It provides information on type of intervention which has occurred during the joining operation.",
                dataType=o6.Byte,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6032",
                browseName="ns=ijt_base;IsGeneratedOffline",
                description="It indicates that the result is generated when the asset was offline. The default value is false.\nNote: The definition of offline status is application specific.\nExample: Wireless tool performing joining in radio shadow.",
                dataType=o6.Boolean,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6048",
                browseName="ns=ijt_base;JoiningTechnology",
                description="It is a human readable text to identify the joining technology.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6052", browseName="ns=ijt_base;Name", description="It is the user-friendly name of the result.", dataType=o6.String, value=""
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6071",
                browseName="ns=ijt_base;ResultCounters",
                description="It is a list of counters associated to the given result. \nExamples: Batch Counter, Retry Counter, Channel Counter, etc.",
                dataType=ijt_base_datypes.ResultCounterDataType,
                valueRank=1,
                arrayDimensions=[0],
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6152",
                browseName="ns=ijt_base;SequenceNumber",
                description="It is a human readable text to identify the joining technology.",
                dataType=o6.Int64,
                value=0,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6207",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                value="",
            ),
            "i=24136",
        ),
    ],
    dataType=ijt_base_datypes.JoiningResultMetaDataType,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6209", browseName="ns=ijt_base;JointDesignDataType", dataType=o6.String, value="JointDesignDataType")
o6.reference(o6.ns["ns=ijt_base;i=5107"], "i=39", o6.ns["ns=ijt_base;i=6209"])
ijt_base_vartypes.JoiningSystemResultType(
    nodeId="ns=ijt_base;i=6001",
    browseName="ns=machinery_result;Result",
    modellingRule="Mandatory",
    references=[
        o6.reference(o6.ns["ns=ijt_base;i=6002"], "i=24136"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ijt_base;i=6210", browseName="ns=machinery_result;ResultContent", valueRank=1, arrayDimensions=[0]), "i=24136"),
    ],
    dataType=machinery_result.datatypes.ResultDataType,
    value=machinery_result.datatypes.ResultDataType(
        resultMetaData=machinery_result.datatypes.ResultMetaDataType(
            resultId="",
            hasTransferableDataOnFile=None,
            isPartial=None,
            isSimulated=None,
            resultState=None,
            stepId=None,
            partId=None,
            externalRecipeId=None,
            internalRecipeId=None,
            productId=None,
            externalConfigurationId=None,
            internalConfigurationId=None,
            jobId=None,
            creationTime=None,
            processingTimes=None,
            resultUri=[],
            resultEvaluation=None,
            resultEvaluationCode=None,
            resultEvaluationDetails=None,
            fileFormat=[],
        ),
        resultContent=[],
    ),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ijt_base_objtypes.JoiningSystemResultReadyEventType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=6001"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6212", browseName="ns=ijt_base;JointDesignDataType", dataType=o6.String, value="//xs:element[@name='JointDesignDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5108"], "i=39", o6.ns["ns=ijt_base;i=6212"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6213", browseName="ns=ijt_base;KeyValueDataType", dataType=o6.String, value="KeyValueDataType")
o6.reference(o6.ns["ns=ijt_base;i=5148"], "i=39", o6.ns["ns=ijt_base;i=6213"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6214", browseName="ns=ijt_base;KeyValueDataType", dataType=o6.String, value="//xs:element[@name='KeyValueDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5149"], "i=39", o6.ns["ns=ijt_base;i=6214"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6215", browseName="ns=ijt_base;ReportedValueDataType", dataType=o6.String, value="ReportedValueDataType")
o6.reference(o6.ns["ns=ijt_base;i=5095"], "i=39", o6.ns["ns=ijt_base;i=6215"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6216", browseName="ns=ijt_base;ReportedValueDataType", dataType=o6.String, value="//xs:element[@name='ReportedValueDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5096"], "i=39", o6.ns["ns=ijt_base;i=6216"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6217", browseName="ns=ijt_base;ResultCounterDataType", dataType=o6.String, value="ResultCounterDataType")
o6.reference(o6.ns["ns=ijt_base;i=5089"], "i=39", o6.ns["ns=ijt_base;i=6217"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6218", browseName="ns=ijt_base;ResultCounterDataType", dataType=o6.String, value="//xs:element[@name='ResultCounterDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5090"], "i=39", o6.ns["ns=ijt_base;i=6218"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6219", browseName="ns=ijt_base;JoiningResultMetaDataType", dataType=o6.String, value="JoiningResultMetaDataType")
o6.reference(o6.ns["ns=ijt_base;i=5046"], "i=39", o6.ns["ns=ijt_base;i=6219"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6220", browseName="ns=ijt_base;JoiningResultMetaDataType", dataType=o6.String, value="//xs:element[@name='JoiningResultMetaDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5047"], "i=39", o6.ns["ns=ijt_base;i=6220"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6221", browseName="ns=ijt_base;ResultValueDataType", dataType=o6.String, value="ResultValueDataType")
o6.reference(o6.ns["ns=ijt_base;i=5056"], "i=39", o6.ns["ns=ijt_base;i=6221"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6222", browseName="ns=ijt_base;ResultValueDataType", dataType=o6.String, value="//xs:element[@name='ResultValueDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5057"], "i=39", o6.ns["ns=ijt_base;i=6222"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ijt_base;i=6226",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6208",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                value="",
            ),
            "i=24136",
        )
    ],
    dataType=ijt_base_datypes.JoiningResultMetaDataType,
)
ijt_base_vartypes.JoiningSystemResultType(
    nodeId="ns=ijt_base;i=6225",
    browseName="ns=ijt_base;<ResultVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ijt_base;i=6211", browseName="ns=machinery_result;ResultContent", valueRank=1, arrayDimensions=[0]), "i=24136"),
        o6.reference(o6.ns["ns=ijt_base;i=6226"], "i=24136"),
    ],
    dataType=machinery_result.datatypes.ResultDataType,
    value=machinery_result.datatypes.ResultDataType(
        resultMetaData=machinery_result.datatypes.ResultMetaDataType(
            resultId="",
            hasTransferableDataOnFile=None,
            isPartial=None,
            isSimulated=None,
            resultState=None,
            stepId=None,
            partId=None,
            externalRecipeId=None,
            internalRecipeId=None,
            productId=None,
            externalConfigurationId=None,
            internalConfigurationId=None,
            jobId=None,
            creationTime=None,
            processingTimes=None,
            resultUri=[],
            resultEvaluation=None,
            resultEvaluationCode=None,
            resultEvaluationDetails=None,
            fileFormat=[],
        ),
        resultContent=[],
    ),
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6227", browseName="ns=ijt_base;SignalDataType", dataType=o6.String, value="SignalDataType")
o6.reference(o6.ns["ns=ijt_base;i=5081"], "i=39", o6.ns["ns=ijt_base;i=6227"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5014",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=6169"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6171",
                browseName="ns=ijt_base;OverloadCount",
                description="OverloadCount is the number of overloads of the sensor, where the permissible load of the sensor was exceeded.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6231",
                browseName="ns=ijt_base;MeasuredValue",
                description="MeasuredValue is the actual measured value reported from a sensor.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.ISensorType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5014"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashIJTSlashBaseSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=ijt_base;i=5102",
    browseName="ns=ijt_base;http://opcfoundation.org/UA/IJT/Base/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6111", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6112", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-10-06T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6113", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Base/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6114", browseName="NamespaceVersion", dataType=o6.String, value="1.01.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6115", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0], value=[])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6116", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6232", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6233", browseName="ns=ijt_base;SignalDataType", dataType=o6.String, value="//xs:element[@name='SignalDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5125"], "i=39", o6.ns["ns=ijt_base;i=6233"])
ijt_base_objtypes.JoiningSystemIdentificationType(
    nodeId="ns=ijt_base;i=5026",
    browseName="ns=di;Identification",
    description="The Identification Object provides identification parameters of the joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6193",
                browseName="ns=ijt_base;Name",
                description="Name is the name of the joining system. It can also be the standard browse name of the instance of JoiningSystemType.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6194",
                browseName="ns=ijt_base;Description",
                description="It is the description of the system which could be written by the customer to identify the system. It could be the purpose of the system in the assembly line.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6195",
                browseName="ns=ijt_base;IntegratorName",
                description="IntegratorName is the name of the system integrator.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6196",
                browseName="ns=ijt_base;JoiningTechnology",
                description="JoiningTechnology is a human readable text to identify the joining technology of the joining system.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6197",
                browseName="ns=machinery;Location",
                description="Location is the location of the given system in the given plant or factory in text format.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6223",
                browseName="ns=di;Manufacturer",
                description="Manufacturer provides a human-readable, localized name of the joining system manufacturer.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6224",
                browseName="ns=di;ManufacturerUri",
                description="ManufacturerUri provides a unique identifier for this company. This identifier should be a fully qualified domain name; however, it may be a GUID or similar construct that ensures global uniqueness.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6237",
                browseName="ns=di;Model",
                description="Model provides the type of the joining system. Examples: Fixtured System, Handheld System, etc.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6238",
                browseName="ns=di;ProductInstanceUri",
                description="ProductInstanceUri is a globally unique resource identifier provided by the manufacturer.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6239",
                browseName="ns=ijt_base;SystemId",
                description="SystemId is the system integrator specific identifier for the system. It represents a reference to the manufacturer ERP system.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5026"])
o6.reference(o6.ns["ns=ijt_base;i=5026"], "i=17603", "ns=di;i=15035")
o6.reference(o6.ns["ns=ijt_base;i=5074"], "i=17604", o6.ns["ns=ijt_base;i=5026"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6243", browseName="ns=ijt_base;StepResultDataType", dataType=o6.String, value="StepResultDataType")
o6.reference(o6.ns["ns=ijt_base;i=5059"], "i=39", o6.ns["ns=ijt_base;i=6243"])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5012",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6156",
                browseName="ns=ijt_base;InputSpecification",
                description="InputSpecification is the input specification of the power supply. Example: 230 V, 50/60 Hz, 10 A.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6157"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6158"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6249",
                browseName="ns=ijt_base;OutputSpecification",
                description="OutputSpecification is the output specification of the power supply.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IPowerSupplyType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5012"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6250", browseName="ns=ijt_base;StepResultDataType", dataType=o6.String, value="//xs:element[@name='StepResultDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5060"], "i=39", o6.ns["ns=ijt_base;i=6250"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6251", browseName="ns=ijt_base;StepTraceDataType", dataType=o6.String, value="StepTraceDataType")
o6.reference(o6.ns["ns=ijt_base;i=5068"], "i=39", o6.ns["ns=ijt_base;i=6251"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6252", browseName="ns=ijt_base;StepTraceDataType", dataType=o6.String, value="//xs:element[@name='StepTraceDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5069"], "i=39", o6.ns["ns=ijt_base;i=6252"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6253", browseName="ns=ijt_base;TraceContentDataType", dataType=o6.String, value="TraceContentDataType")
o6.reference(o6.ns["ns=ijt_base;i=5071"], "i=39", o6.ns["ns=ijt_base;i=6253"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6254", browseName="ns=ijt_base;TraceContentDataType", dataType=o6.String, value="//xs:element[@name='TraceContentDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5072"], "i=39", o6.ns["ns=ijt_base;i=6254"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6255", browseName="ns=ijt_base;TraceDataType", dataType=o6.String, value="TraceDataType")
o6.reference(o6.ns["ns=ijt_base;i=5062"], "i=39", o6.ns["ns=ijt_base;i=6255"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6256", browseName="ns=ijt_base;TraceDataType", dataType=o6.String, value="//xs:element[@name='TraceDataType']")
o6.reference(o6.ns["ns=ijt_base;i=5063"], "i=39", o6.ns["ns=ijt_base;i=6256"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ijt_base;i=6257", browseName="ns=ijt_base;JoiningTraceDataType", dataType=o6.String, value="JoiningTraceDataType")
o6.reference(o6.ns["ns=ijt_base;i=5065"], "i=39", o6.ns["ns=ijt_base;i=6257"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ijt_base;i=6024",
    browseName="ns=ijt_base;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IJT/Base/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6027", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Base/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6031",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6172"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6178"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6180"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6182"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6188"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6190"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6199"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6201"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6203"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6205"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6209"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6213"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6215"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6217"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6219"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6221"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6227"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6243"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6251"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6253"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6255"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6257"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/IJT/Base/" TargetNamespace="http://opcfoundation.org/UA/IJT/Base/" xmlns:ns1="http://opcfoundation.org/UA/Machinery/Result/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/Machinery/Result/"/>\n <opc:StructuredType Name="CalibrationDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure contains the Calibration information. It is used as an input argument in SetCalibration method.\nNote: The input data sent in SetCalibration shall be updated in the respective parameters of the asset under Maintenance/Calibration.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="CalibrationPlaceSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NextCalibrationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CalibrationValueSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SensorScaleSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CertificateUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="26"/>\n  <opc:Field TypeName="opc:DateTime" Name="LastCalibration"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="CalibrationPlaceSpecified" Name="CalibrationPlace"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="NextCalibrationSpecified" Name="NextCalibration"/>\n  <opc:Field TypeName="opc:Double" SwitchField="CalibrationValueSpecified" Name="CalibrationValue"/>\n  <opc:Field TypeName="opc:Double" SwitchField="SensorScaleSpecified" Name="SensorScale"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="CertificateUriSpecified" Name="CertificateUri"/>\n  <opc:Field TypeName="ua:EUInformation" SwitchField="EngineeringUnitsSpecified" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType Name="DesignValueDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the design value for a given physical quantity. It is used in JointDesignDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalQuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DesignValueSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="28"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="PhysicalQuantitySpecified" Name="PhysicalQuantity"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:Variant" SwitchField="DesignValueSpecified" Name="DesignValue"/>\n  <opc:Field TypeName="ua:EUInformation" SwitchField="EngineeringUnitsSpecified" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType Name="EntityDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the identification data for a given entity in the system.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EntityOriginIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsExternalSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="28"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="opc:CharArray" Name="EntityId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="EntityOriginIdSpecified" Name="EntityOriginId"/>\n  <opc:Field TypeName="opc:Boolean" SwitchField="IsExternalSpecified" Name="IsExternal"/>\n  <opc:Field TypeName="opc:Int16" Name="EntityType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="ErrorInformationDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure represents the errors occurred in the system which are outside the boundaries of the given program.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="ErrorIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LegacyErrorSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ErrorMessageSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="29"/>\n  <opc:Field TypeName="opc:Byte" Name="ErrorType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ErrorIdSpecified" Name="ErrorId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="LegacyErrorSpecified" Name="LegacyError"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="ErrorMessageSpecified" Name="ErrorMessage"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningProcessDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the base container for any joining process in a joining system. \nNote: This specification defines the meta data of a JoiningProcess, and the actual content of the Joining Process is application specific.</opc:Documentation>\n  <opc:Field TypeName="ua:ExtensionObject" Name="JoiningProcessMetaData"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfJoiningProcessContent"/>\n  <opc:Field TypeName="ua:Variant" Name="JoiningProcessContent" LengthField="NoOfJoiningProcessContent"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningProcessIdentificationDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure contains the identification information of a Joining Process. It is used in set of methods defined in JoiningProcessManagementType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="JoiningProcessIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JoiningProcessOriginIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SelectionNameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="29"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JoiningProcessIdSpecified" Name="JoiningProcessId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JoiningProcessOriginIdSpecified" Name="JoiningProcessOriginId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="SelectionNameSpecified" Name="SelectionName"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningProcessMetaDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the meta data which describes the joining process.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="JoiningProcessOriginIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CreationTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LastUpdatedTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JoiningTechnologySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ClassificationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AssociatedEntitiesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="24"/>\n  <opc:Field TypeName="opc:CharArray" Name="JoiningProcessId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JoiningProcessOriginIdSpecified" Name="JoiningProcessOriginId"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="CreationTimeSpecified" Name="CreationTime"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="LastUpdatedTimeSpecified" Name="LastUpdatedTime"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="JoiningTechnologySpecified" Name="JoiningTechnology"/>\n  <opc:Field TypeName="opc:Int16" SwitchField="ClassificationSpecified" Name="Classification"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="AssociatedEntitiesSpecified" Name="NoOfAssociatedEntities"/>\n  <opc:Field TypeName="tns:EntityDataType" SwitchField="AssociatedEntitiesSpecified" Name="AssociatedEntities" LengthField="NoOfAssociatedEntities"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningResultDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure represents the data associated with Joining Result and the corresponding measurement values.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="FailureReasonSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StepResultsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ErrorsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FailingStepResultIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TraceSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="27"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="FailureReasonSpecified" Name="FailureReason"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfOverallResultValues"/>\n  <opc:Field TypeName="tns:ResultValueDataType" Name="OverallResultValues" LengthField="NoOfOverallResultValues"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="StepResultsSpecified" Name="NoOfStepResults"/>\n  <opc:Field TypeName="tns:StepResultDataType" SwitchField="StepResultsSpecified" Name="StepResults" LengthField="NoOfStepResults"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ErrorsSpecified" Name="NoOfErrors"/>\n  <opc:Field TypeName="tns:ErrorInformationDataType" SwitchField="ErrorsSpecified" Name="Errors" LengthField="NoOfErrors"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="FailingStepResultIdSpecified" Name="FailingStepResultId"/>\n  <opc:Field TypeName="tns:JoiningTraceDataType" SwitchField="TraceSpecified" Name="Trace"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JointComponentDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure is the base container for any joint component such as Bolt, Rivet, Gasket, Glue string, etc. \nNote: The concrete definition of joint component is not defined in this version of the specification.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ManufacturerSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ManufacturerUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JointComponentContentSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="27"/>\n  <opc:Field TypeName="opc:CharArray" Name="JointComponentId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="ManufacturerSpecified" Name="Manufacturer"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ManufacturerUriSpecified" Name="ManufacturerUri"/>\n  <opc:Field TypeName="ua:Variant" SwitchField="JointComponentContentSpecified" Name="JointComponentContent"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JointDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the joint information. Joint is the physical outcome of the joining operation which determines the properties of the point where multiple parts are assembled.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="JointOriginIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JointDesignIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CreationTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LastUpdatedTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ClassificationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ClassificationDetailsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JointStatusSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AssociatedEntitiesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JoiningTechnologySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="21"/>\n  <opc:Field TypeName="opc:CharArray" Name="JointId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JointOriginIdSpecified" Name="JointOriginId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JointDesignIdSpecified" Name="JointDesignId"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="CreationTimeSpecified" Name="CreationTime"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="LastUpdatedTimeSpecified" Name="LastUpdatedTime"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="opc:Int16" SwitchField="ClassificationSpecified" Name="Classification"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="ClassificationDetailsSpecified" Name="ClassificationDetails"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JointStatusSpecified" Name="JointStatus"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="AssociatedEntitiesSpecified" Name="NoOfAssociatedEntities"/>\n  <opc:Field TypeName="tns:EntityDataType" SwitchField="AssociatedEntitiesSpecified" Name="AssociatedEntities" LengthField="NoOfAssociatedEntities"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="JoiningTechnologySpecified" Name="JoiningTechnology"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JointDesignDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the design information of a given joint.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JointDesignContentSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JointComponentIdListSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="28"/>\n  <opc:Field TypeName="opc:CharArray" Name="JointDesignId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="JointDesignContentSpecified" Name="NoOfJointDesignContent"/>\n  <opc:Field TypeName="tns:DesignValueDataType" SwitchField="JointDesignContentSpecified" Name="JointDesignContent" LengthField="NoOfJointDesignContent"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="JointComponentIdListSpecified" Name="NoOfJointComponentIdList"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JointComponentIdListSpecified" Name="JointComponentIdList" LengthField="NoOfJointComponentIdList"/>\n </opc:StructuredType>\n <opc:StructuredType Name="KeyValueDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure is similar to 0:KeyValuePair which uses 0:TrimmedString instead of 0:QualifiedName.</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Key"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType Name="ReportedValueDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure provides the given value and corresponding limits for a given physical quantity (if applicable).</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalQuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PreviousValueSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LowLimitSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HighLimitSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="26"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="PhysicalQuantitySpecified" Name="PhysicalQuantity"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:Variant" Name="CurrentValue"/>\n  <opc:Field TypeName="ua:Variant" SwitchField="PreviousValueSpecified" Name="PreviousValue"/>\n  <opc:Field TypeName="opc:Double" SwitchField="LowLimitSpecified" Name="LowLimit"/>\n  <opc:Field TypeName="opc:Double" SwitchField="HighLimitSpecified" Name="HighLimit"/>\n  <opc:Field TypeName="ua:EUInformation" SwitchField="EngineeringUnitsSpecified" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType Name="ResultCounterDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure is used to provide various types of counters associated to a Result. These counters are related to a joining process with sub-processes.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="31"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="opc:UInt32" Name="CounterValue"/>\n  <opc:Field TypeName="opc:Int16" Name="CounterType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningResultMetaDataType" BaseType="ns1:ResultMetaDataType">\n  <opc:Documentation>This structure is a subtype of ResultMetaDataType. It is used to define additional meta data of a Result in a joining system.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="HasTransferableDataOnFileSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsPartialSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsSimulatedSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultStateSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StepIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PartIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalRecipeIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InternalRecipeIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProductIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalConfigurationIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InternalConfigurationIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JobIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CreationTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProcessingTimesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationCodeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationDetailsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FileFormatSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JoiningTechnologySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SequenceNumberSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ClassificationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="OperationModeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AssemblyTypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AssociatedEntitiesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultCountersSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InterventionTypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsGeneratedOfflineSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExtendedMetaDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ResultId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Boolean" SwitchField="HasTransferableDataOnFileSpecified" Name="HasTransferableDataOnFile" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Boolean" SwitchField="IsPartialSpecified" Name="IsPartial" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Boolean" SwitchField="IsSimulatedSpecified" Name="IsSimulated" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ResultStateSpecified" Name="ResultState" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="StepIdSpecified" Name="StepId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="PartIdSpecified" Name="PartId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ExternalRecipeIdSpecified" Name="ExternalRecipeId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="InternalRecipeIdSpecified" Name="InternalRecipeId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ProductIdSpecified" Name="ProductId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ExternalConfigurationIdSpecified" Name="ExternalConfigurationId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="InternalConfigurationIdSpecified" Name="InternalConfigurationId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="JobIdSpecified" Name="JobId" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:DateTime" SwitchField="CreationTimeSpecified" Name="CreationTime" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="ns1:ProcessingTimesDataType" SwitchField="ProcessingTimesSpecified" Name="ProcessingTimes" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ResultUriSpecified" Name="NoOfResultUri" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ResultUriSpecified" Name="ResultUri" SourceType="ns1:ResultMetaDataType" LengthField="NoOfResultUri"/>\n  <opc:Field TypeName="ns1:ResultEvaluationEnum" SwitchField="ResultEvaluationSpecified" Name="ResultEvaluation" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Int64" SwitchField="ResultEvaluationCodeSpecified" Name="ResultEvaluationCode" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="ResultEvaluationDetailsSpecified" Name="ResultEvaluationDetails" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="FileFormatSpecified" Name="NoOfFileFormat" SourceType="ns1:ResultMetaDataType"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="FileFormatSpecified" Name="FileFormat" SourceType="ns1:ResultMetaDataType" LengthField="NoOfFileFormat"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="JoiningTechnologySpecified" Name="JoiningTechnology"/>\n  <opc:Field TypeName="opc:UInt64" SwitchField="SequenceNumberSpecified" Name="SequenceNumber"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ua:LocalizedText" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="ClassificationSpecified" Name="Classification"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="OperationModeSpecified" Name="OperationMode"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="AssemblyTypeSpecified" Name="AssemblyType"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="AssociatedEntitiesSpecified" Name="NoOfAssociatedEntities"/>\n  <opc:Field TypeName="tns:EntityDataType" SwitchField="AssociatedEntitiesSpecified" Name="AssociatedEntities" LengthField="NoOfAssociatedEntities"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ResultCountersSpecified" Name="NoOfResultCounters"/>\n  <opc:Field TypeName="tns:ResultCounterDataType" SwitchField="ResultCountersSpecified" Name="ResultCounters" LengthField="NoOfResultCounters"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="InterventionTypeSpecified" Name="InterventionType"/>\n  <opc:Field TypeName="opc:Boolean" SwitchField="IsGeneratedOfflineSpecified" Name="IsGeneratedOffline"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ExtendedMetaDataSpecified" Name="NoOfExtendedMetaData"/>\n  <opc:Field TypeName="tns:KeyValueDataType" SwitchField="ExtendedMetaDataSpecified" Name="ExtendedMetaData" LengthField="NoOfExtendedMetaData"/>\n </opc:StructuredType>\n <opc:StructuredType Name="ResultValueDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>It is used to report measurement values of the joining operation. Those are meant to characterize the quality of the process. It is used in JoiningResultDataType and StepResultDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ValueIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ValueTagSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TracePointIndexSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TracePointTimeOffsetSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ParameterIdListSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ViolationTypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ViolationConsequenceSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SensorIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LowLimitSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HighLimitSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TargetValueSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultStepSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalQuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="16"/>\n  <opc:Field TypeName="opc:Double" Name="MeasuredValue"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ns1:ResultEvaluationEnum" SwitchField="ResultEvaluationSpecified" Name="ResultEvaluation"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ValueIdSpecified" Name="ValueId"/>\n  <opc:Field TypeName="opc:Int16" SwitchField="ValueTagSpecified" Name="ValueTag"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="TracePointIndexSpecified" Name="TracePointIndex"/>\n  <opc:Field TypeName="opc:Double" SwitchField="TracePointTimeOffsetSpecified" Name="TracePointTimeOffset"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="ParameterIdListSpecified" Name="NoOfParameterIdList"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ParameterIdListSpecified" Name="ParameterIdList" LengthField="NoOfParameterIdList"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="ViolationTypeSpecified" Name="ViolationType"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="ViolationConsequenceSpecified" Name="ViolationConsequence"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="SensorIdSpecified" Name="SensorId"/>\n  <opc:Field TypeName="opc:Double" SwitchField="LowLimitSpecified" Name="LowLimit"/>\n  <opc:Field TypeName="opc:Double" SwitchField="HighLimitSpecified" Name="HighLimit"/>\n  <opc:Field TypeName="opc:Double" SwitchField="TargetValueSpecified" Name="TargetValue"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ResultStepSpecified" Name="ResultStep"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="PhysicalQuantitySpecified" Name="PhysicalQuantity"/>\n  <opc:Field TypeName="ua:EUInformation" SwitchField="EngineeringUnitsSpecified" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType Name="SignalDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure contains the signal information which is used in SetIOSignals and GetIOSignals methods.</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="SignalId"/>\n  <opc:Field TypeName="ua:Variant" Name="SignalValue"/>\n  <opc:Field TypeName="opc:CharArray" Name="SignalDescription"/>\n  <opc:Field TypeName="opc:Int16" Name="SignalType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="StepResultDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>This structure represents the measurement values corresponding to a given step in the program. It is used in JoiningResultDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="ProgramStepIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProgramStepSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StartTimeOffsetSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StepTraceIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StepResultValuesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="25"/>\n  <opc:Field TypeName="opc:CharArray" Name="StepResultId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ProgramStepIdSpecified" Name="ProgramStepId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="ProgramStepSpecified" Name="ProgramStep"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="ns1:ResultEvaluationEnum" SwitchField="ResultEvaluationSpecified" Name="ResultEvaluation"/>\n  <opc:Field TypeName="opc:Double" SwitchField="StartTimeOffsetSpecified" Name="StartTimeOffset"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="StepTraceIdSpecified" Name="StepTraceId"/>\n  <opc:Field TypeName="opc:Int32" SwitchField="StepResultValuesSpecified" Name="NoOfStepResultValues"/>\n  <opc:Field TypeName="tns:ResultValueDataType" SwitchField="StepResultValuesSpecified" Name="StepResultValues" LengthField="NoOfStepResultValues"/>\n </opc:StructuredType>\n <opc:StructuredType Name="StepTraceDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>It is to describe of the trace for a given program step. It is used in JoiningTraceDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="SamplingIntervalSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StartTimeOffsetSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="30"/>\n  <opc:Field TypeName="opc:CharArray" Name="StepTraceId"/>\n  <opc:Field TypeName="opc:CharArray" Name="StepResultId"/>\n  <opc:Field TypeName="opc:UInt32" Name="NumberOfTracePoints"/>\n  <opc:Field TypeName="opc:Double" SwitchField="SamplingIntervalSpecified" Name="SamplingInterval"/>\n  <opc:Field TypeName="opc:Double" SwitchField="StartTimeOffsetSpecified" Name="StartTimeOffset"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfStepTraceContent"/>\n  <opc:Field TypeName="tns:TraceContentDataType" Name="StepTraceContent" LengthField="NoOfStepTraceContent"/>\n </opc:StructuredType>\n <opc:StructuredType Name="TraceContentDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>It is to describe the trace samples for a given program step. It is used in StepTraceDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="SensorIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalQuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="Reserved1" Length="27"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfValues"/>\n  <opc:Field TypeName="opc:Double" Name="Values" LengthField="NoOfValues"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="SensorIdSpecified" Name="SensorId"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="NameSpecified" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" SwitchField="DescriptionSpecified" Name="Description"/>\n  <opc:Field TypeName="opc:Byte" SwitchField="PhysicalQuantitySpecified" Name="PhysicalQuantity"/>\n  <opc:Field TypeName="ua:EUInformation" SwitchField="EngineeringUnitsSpecified" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType Name="TraceDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>It is a base type to encapsulate common data for a Trace.</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="TraceId"/>\n  <opc:Field TypeName="opc:CharArray" Name="ResultId"/>\n </opc:StructuredType>\n <opc:StructuredType Name="JoiningTraceDataType" BaseType="tns:TraceDataType">\n  <opc:Documentation>This structure is to describe the content of traces for all the steps in the given program. It is used in JoiningResultDataType.</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="TraceId" SourceType="tns:TraceDataType"/>\n  <opc:Field TypeName="opc:CharArray" Name="ResultId" SourceType="tns:TraceDataType"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfStepTraces"/>\n  <opc:Field TypeName="tns:StepTraceDataType" Name="StepTraces" LengthField="NoOfStepTraces"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ijt_base;i=6258", browseName="ns=ijt_base;JoiningTraceDataType", dataType=o6.String, value="//xs:element[@name='JoiningTraceDataType']"
)
o6.reference(o6.ns["ns=ijt_base;i=5066"], "i=39", o6.ns["ns=ijt_base;i=6258"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ijt_base;i=6034",
    browseName="ns=ijt_base;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IJT/Base/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_base;i=6144", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Base/Types.xsd")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6168",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6174"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6179"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6181"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6187"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6189"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6198"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6200"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6202"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6204"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6206"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6212"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6214"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6216"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6218"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6220"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6222"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6233"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6250"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6252"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6254"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6256"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=6258"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ns5="http://opcfoundation.org/UA/Machinery/Result/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" targetNamespace="http://opcfoundation.org/UA/IJT/Base/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/IJT/Base/Types.xsd" elementFormDefault="qualified">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/Machinery/Result/Types.xsd"/>\n <xs:complexType name="CalibrationDataType">\n  <xs:annotation>\n   <xs:documentation>This structure contains the Calibration information. It is used as an input argument in SetCalibration method.\nNote: The input data sent in SetCalibration shall be updated in the respective parameters of the asset under Maintenance/Calibration.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:dateTime" name="LastCalibration" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="CalibrationPlace" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:dateTime" name="NextCalibration" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="CalibrationValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="SensorScale" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="CertificateUri" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:EUInformation" name="EngineeringUnits" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:CalibrationDataType" name="CalibrationDataType"/>\n <xs:complexType name="ListOfCalibrationDataType">\n  <xs:sequence>\n   <xs:element type="tns:CalibrationDataType" nillable="true" name="CalibrationDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCalibrationDataType" nillable="true" name="ListOfCalibrationDataType"/>\n <xs:complexType name="DesignValueDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the design value for a given physical quantity. It is used in JointDesignDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:unsignedByte" name="PhysicalQuantity" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="DesignValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:EUInformation" name="EngineeringUnits" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:DesignValueDataType" name="DesignValueDataType"/>\n <xs:complexType name="ListOfDesignValueDataType">\n  <xs:sequence>\n   <xs:element type="tns:DesignValueDataType" nillable="true" name="DesignValueDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDesignValueDataType" nillable="true" name="ListOfDesignValueDataType"/>\n <xs:complexType name="EntityDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the identification data for a given entity in the system.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="EntityId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="EntityOriginId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:boolean" name="IsExternal" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="EntityType" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:EntityDataType" name="EntityDataType"/>\n <xs:complexType name="ListOfEntityDataType">\n  <xs:sequence>\n   <xs:element type="tns:EntityDataType" nillable="true" name="EntityDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEntityDataType" nillable="true" name="ListOfEntityDataType"/>\n <xs:complexType name="ErrorInformationDataType">\n  <xs:annotation>\n   <xs:documentation>This structure represents the errors occurred in the system which are outside the boundaries of the given program.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:unsignedByte" name="ErrorType" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ErrorId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="LegacyError" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="ErrorMessage" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ErrorInformationDataType" name="ErrorInformationDataType"/>\n <xs:complexType name="ListOfErrorInformationDataType">\n  <xs:sequence>\n   <xs:element type="tns:ErrorInformationDataType" nillable="true" name="ErrorInformationDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfErrorInformationDataType" nillable="true" name="ListOfErrorInformationDataType"/>\n <xs:complexType name="JoiningProcessDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the base container for any joining process in a joining system. \nNote: This specification defines the meta data of a JoiningProcess, and the actual content of the Joining Process is application specific.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="ua:ExtensionObject" name="JoiningProcessMetaData" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:ListOfVariant" name="JoiningProcessContent" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JoiningProcessDataType" name="JoiningProcessDataType"/>\n <xs:complexType name="ListOfJoiningProcessDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningProcessDataType" nillable="true" name="JoiningProcessDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningProcessDataType" nillable="true" name="ListOfJoiningProcessDataType"/>\n <xs:complexType name="JoiningProcessIdentificationDataType">\n  <xs:annotation>\n   <xs:documentation>This structure contains the identification information of a Joining Process. It is used in set of methods defined in JoiningProcessManagementType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="JoiningProcessId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="JoiningProcessOriginId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="SelectionName" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JoiningProcessIdentificationDataType" name="JoiningProcessIdentificationDataType"/>\n <xs:complexType name="ListOfJoiningProcessIdentificationDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningProcessIdentificationDataType" nillable="true" name="JoiningProcessIdentificationDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningProcessIdentificationDataType" nillable="true" name="ListOfJoiningProcessIdentificationDataType"/>\n <xs:complexType name="JoiningProcessMetaDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the meta data which describes the joining process.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="JoiningProcessId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="JoiningProcessOriginId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:dateTime" name="CreationTime" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:dateTime" name="LastUpdatedTime" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="JoiningTechnology" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="Classification" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfEntityDataType" name="AssociatedEntities" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JoiningProcessMetaDataType" name="JoiningProcessMetaDataType"/>\n <xs:complexType name="ListOfJoiningProcessMetaDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningProcessMetaDataType" nillable="true" name="JoiningProcessMetaDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningProcessMetaDataType" nillable="true" name="ListOfJoiningProcessMetaDataType"/>\n <xs:complexType name="JoiningResultDataType">\n  <xs:annotation>\n   <xs:documentation>This structure represents the data associated with Joining Result and the corresponding measurement values.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:unsignedByte" name="FailureReason" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfResultValueDataType" name="OverallResultValues" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfStepResultDataType" name="StepResults" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfErrorInformationDataType" name="Errors" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="FailingStepResultId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:JoiningTraceDataType" name="Trace" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JoiningResultDataType" name="JoiningResultDataType"/>\n <xs:complexType name="ListOfJoiningResultDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningResultDataType" nillable="true" name="JoiningResultDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningResultDataType" nillable="true" name="ListOfJoiningResultDataType"/>\n <xs:complexType name="JointComponentDataType">\n  <xs:annotation>\n   <xs:documentation>This structure is the base container for any joint component such as Bolt, Rivet, Gasket, Glue string, etc. \nNote: The concrete definition of joint component is not defined in this version of the specification.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="JointComponentId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="Manufacturer" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ManufacturerUri" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="JointComponentContent" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JointComponentDataType" name="JointComponentDataType"/>\n <xs:complexType name="ListOfJointComponentDataType">\n  <xs:sequence>\n   <xs:element type="tns:JointComponentDataType" nillable="true" name="JointComponentDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJointComponentDataType" nillable="true" name="ListOfJointComponentDataType"/>\n <xs:complexType name="JointDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the joint information. Joint is the physical outcome of the joining operation which determines the properties of the point where multiple parts are assembled.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="JointId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="JointOriginId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="JointDesignId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:dateTime" name="CreationTime" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:dateTime" name="LastUpdatedTime" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="Classification" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="ClassificationDetails" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="JointStatus" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfEntityDataType" name="AssociatedEntities" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="JoiningTechnology" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JointDataType" name="JointDataType"/>\n <xs:complexType name="ListOfJointDataType">\n  <xs:sequence>\n   <xs:element type="tns:JointDataType" nillable="true" name="JointDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJointDataType" nillable="true" name="ListOfJointDataType"/>\n <xs:complexType name="JointDesignDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the design information of a given joint.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="JointDesignId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:LocalizedText" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfDesignValueDataType" name="JointDesignContent" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:ListOfString" name="JointComponentIdList" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JointDesignDataType" name="JointDesignDataType"/>\n <xs:complexType name="ListOfJointDesignDataType">\n  <xs:sequence>\n   <xs:element type="tns:JointDesignDataType" nillable="true" name="JointDesignDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJointDesignDataType" nillable="true" name="ListOfJointDesignDataType"/>\n <xs:complexType name="KeyValueDataType">\n  <xs:annotation>\n   <xs:documentation>This structure is similar to 0:KeyValuePair which uses 0:TrimmedString instead of 0:QualifiedName.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:string" name="Key" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="Value" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:KeyValueDataType" name="KeyValueDataType"/>\n <xs:complexType name="ListOfKeyValueDataType">\n  <xs:sequence>\n   <xs:element type="tns:KeyValueDataType" nillable="true" name="KeyValueDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfKeyValueDataType" nillable="true" name="ListOfKeyValueDataType"/>\n <xs:complexType name="ReportedValueDataType">\n  <xs:annotation>\n   <xs:documentation>This structure provides the given value and corresponding limits for a given physical quantity (if applicable).</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:unsignedByte" name="PhysicalQuantity" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="CurrentValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="PreviousValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="LowLimit" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="HighLimit" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:EUInformation" name="EngineeringUnits" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ReportedValueDataType" name="ReportedValueDataType"/>\n <xs:complexType name="ListOfReportedValueDataType">\n  <xs:sequence>\n   <xs:element type="tns:ReportedValueDataType" nillable="true" name="ReportedValueDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfReportedValueDataType" nillable="true" name="ListOfReportedValueDataType"/>\n <xs:complexType name="ResultCounterDataType">\n  <xs:annotation>\n   <xs:documentation>This structure is used to provide various types of counters associated to a Result. These counters are related to a joining process with sub-processes.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedInt" name="CounterValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="CounterType" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ResultCounterDataType" name="ResultCounterDataType"/>\n <xs:complexType name="ListOfResultCounterDataType">\n  <xs:sequence>\n   <xs:element type="tns:ResultCounterDataType" nillable="true" name="ResultCounterDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResultCounterDataType" nillable="true" name="ListOfResultCounterDataType"/>\n <xs:complexType name="JoiningResultMetaDataType">\n  <xs:annotation>\n   <xs:documentation>This structure is a subtype of ResultMetaDataType. It is used to define additional meta data of a Result in a joining system.</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="ns5:ResultMetaDataType">\n    <xs:sequence>\n     <xs:element type="ua:LocalizedText" name="JoiningTechnology" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:unsignedLong" name="SequenceNumber" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="ua:LocalizedText" name="Description" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:unsignedByte" name="Classification" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:unsignedByte" name="OperationMode" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:unsignedByte" name="AssemblyType" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="tns:ListOfEntityDataType" name="AssociatedEntities" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="tns:ListOfResultCounterDataType" name="ResultCounters" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:unsignedByte" name="InterventionType" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="xs:boolean" name="IsGeneratedOffline" minOccurs="0" maxOccurs="1"/>\n     <xs:element type="tns:ListOfKeyValueDataType" name="ExtendedMetaData" minOccurs="0" maxOccurs="1"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:JoiningResultMetaDataType" name="JoiningResultMetaDataType"/>\n <xs:complexType name="ListOfJoiningResultMetaDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningResultMetaDataType" nillable="true" name="JoiningResultMetaDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningResultMetaDataType" nillable="true" name="ListOfJoiningResultMetaDataType"/>\n <xs:complexType name="ResultValueDataType">\n  <xs:annotation>\n   <xs:documentation>It is used to report measurement values of the joining operation. Those are meant to characterize the quality of the process. It is used in JoiningResultDataType and StepResultDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:double" name="MeasuredValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ns5:ResultEvaluationEnum" name="ResultEvaluation" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ValueId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="ValueTag" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:int" name="TracePointIndex" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="TracePointTimeOffset" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:ListOfString" name="ParameterIdList" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="ViolationType" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="ViolationConsequence" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="SensorId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="LowLimit" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="HighLimit" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="TargetValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ResultStep" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="PhysicalQuantity" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:EUInformation" name="EngineeringUnits" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ResultValueDataType" name="ResultValueDataType"/>\n <xs:complexType name="ListOfResultValueDataType">\n  <xs:sequence>\n   <xs:element type="tns:ResultValueDataType" nillable="true" name="ResultValueDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResultValueDataType" nillable="true" name="ListOfResultValueDataType"/>\n <xs:complexType name="SignalDataType">\n  <xs:annotation>\n   <xs:documentation>This structure contains the signal information which is used in SetIOSignals and GetIOSignals methods.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:string" name="SignalId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:Variant" name="SignalValue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="SignalDescription" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:short" name="SignalType" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SignalDataType" name="SignalDataType"/>\n <xs:complexType name="ListOfSignalDataType">\n  <xs:sequence>\n   <xs:element type="tns:SignalDataType" nillable="true" name="SignalDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignalDataType" nillable="true" name="ListOfSignalDataType"/>\n <xs:complexType name="StepResultDataType">\n  <xs:annotation>\n   <xs:documentation>This structure represents the measurement values corresponding to a given step in the program. It is used in JoiningResultDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="StepResultId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ProgramStepId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ProgramStep" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ns5:ResultEvaluationEnum" name="ResultEvaluation" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="StartTimeOffset" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="StepTraceId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfResultValueDataType" name="StepResultValues" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:StepResultDataType" name="StepResultDataType"/>\n <xs:complexType name="ListOfStepResultDataType">\n  <xs:sequence>\n   <xs:element type="tns:StepResultDataType" nillable="true" name="StepResultDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStepResultDataType" nillable="true" name="ListOfStepResultDataType"/>\n <xs:complexType name="StepTraceDataType">\n  <xs:annotation>\n   <xs:documentation>It is to describe of the trace for a given program step. It is used in JoiningTraceDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:string" name="StepTraceId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="StepResultId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedInt" name="NumberOfTracePoints" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="SamplingInterval" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:double" name="StartTimeOffset" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="tns:ListOfTraceContentDataType" name="StepTraceContent" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:StepTraceDataType" name="StepTraceDataType"/>\n <xs:complexType name="ListOfStepTraceDataType">\n  <xs:sequence>\n   <xs:element type="tns:StepTraceDataType" nillable="true" name="StepTraceDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStepTraceDataType" nillable="true" name="ListOfStepTraceDataType"/>\n <xs:complexType name="TraceContentDataType">\n  <xs:annotation>\n   <xs:documentation>It is to describe the trace samples for a given program step. It is used in StepTraceDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="ua:ListOfDouble" name="Values" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="SensorId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Name" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="Description" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="PhysicalQuantity" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="ua:EUInformation" name="EngineeringUnits" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:TraceContentDataType" name="TraceContentDataType"/>\n <xs:complexType name="ListOfTraceContentDataType">\n  <xs:sequence>\n   <xs:element type="tns:TraceContentDataType" nillable="true" name="TraceContentDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTraceContentDataType" nillable="true" name="ListOfTraceContentDataType"/>\n <xs:complexType name="TraceDataType">\n  <xs:annotation>\n   <xs:documentation>It is a base type to encapsulate common data for a Trace.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:string" name="TraceId" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:string" name="ResultId" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:TraceDataType" name="TraceDataType"/>\n <xs:complexType name="ListOfTraceDataType">\n  <xs:sequence>\n   <xs:element type="tns:TraceDataType" nillable="true" name="TraceDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTraceDataType" nillable="true" name="ListOfTraceDataType"/>\n <xs:complexType name="JoiningTraceDataType">\n  <xs:annotation>\n   <xs:documentation>This structure is to describe the content of traces for all the steps in the given program. It is used in JoiningResultDataType.</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:TraceDataType">\n    <xs:sequence>\n     <xs:element type="tns:ListOfStepTraceDataType" name="StepTraces" minOccurs="0" maxOccurs="1"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:JoiningTraceDataType" name="JoiningTraceDataType"/>\n <xs:complexType name="ListOfJoiningTraceDataType">\n  <xs:sequence>\n   <xs:element type="tns:JoiningTraceDataType" nillable="true" name="JoiningTraceDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJoiningTraceDataType" nillable="true" name="ListOfJoiningTraceDataType"/>\n</xs:schema>\n',
)
ijt_base_vartypes.JoiningSystemEventContentType(
    nodeId="ns=ijt_base;i=6039",
    browseName="ns=ijt_base;JoiningSystemEventContent",
    description="JoiningSystemEventContent is the common payload of the event from a joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6275",
                browseName="ns=ijt_base;AssociatedEntities",
                description="AssociatedEntities is a list of identifiers of various entities/objects available in the given system. Example: An event maybe associated to Asset, Result, Joint, Error, etc.",
                dataType=ijt_base_datypes.EntityDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6276",
                browseName="ns=ijt_base;EventCode",
                description="EventCode is a system specific event code associated to the given event.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6277",
                browseName="ns=ijt_base;EventText",
                description="EventText is a human readable text related to the context of the event.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6278",
                browseName="ns=ijt_base;JoiningTechnology",
                description="JoiningTechnology is a human readable text to identify the joining technology which has triggered the event. Examples: Tightening, Gluing, Riveting, Flow Drill Fastening, etc.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6280",
                browseName="ns=ijt_base;ReportedValues",
                description="ReportedValues is a list of values associated with the given event payload. Example: If it is an over temperature event, then the ReportedValue can be the measured value along with the corresponding limits.",
                dataType=ijt_base_datypes.ReportedValueDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemEventType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=6039"])
ijt_base_vartypes.JoiningSystemEventContentType(
    nodeId="ns=ijt_base;i=6177",
    browseName="ns=ijt_base;JoiningSystemEventContent",
    description="JoiningSystemEventContent is the common payload of the event from a joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6281",
                browseName="ns=ijt_base;AssociatedEntities",
                description="AssociatedEntities is a list of identifiers of various entities/objects available in the given system. Example: An event maybe associated to Asset, Result, Joint, Error, etc.",
                dataType=ijt_base_datypes.EntityDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6282",
                browseName="ns=ijt_base;EventCode",
                description="EventCode is a system specific event code associated to the given event.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6283",
                browseName="ns=ijt_base;EventText",
                description="EventText is a human readable text related to the context of the event.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6284",
                browseName="ns=ijt_base;JoiningTechnology",
                description="JoiningTechnology is a human readable text to identify the joining technology which has triggered the event. Examples: Tightening, Gluing, Riveting, Flow Drill Fastening, etc.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6285",
                browseName="ns=ijt_base;ReportedValues",
                description="ReportedValues is a list of values associated with the given event payload. Example: If it is an over temperature event, then the ReportedValue can be the measured value along with the corresponding limits.",
                dataType=ijt_base_datypes.ReportedValueDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemConditionType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=6177"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6084",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6294",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
o6.reference(ijt_base_vartypes.JoiningDataVariableType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=6084"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5077",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6296",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6297",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5037",
    browseName="ns=ijt_base;<Controller>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5092",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5077"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5037"], "i=17603", ijt_base_objtypes.IControllerType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5018", browseName="ns=ijt_base;Controllers", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5037"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5093",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6298",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6299",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5034",
    browseName="ns=ijt_base;<Accessory>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5094",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5093"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5034"], "i=17603", ijt_base_objtypes.IAccessoryType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5032", browseName="ns=ijt_base;Accessories", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5034"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5127",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6300",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6301",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5129",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6302",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6341",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5036",
    browseName="ns=ijt_base;<Cable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5130",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5129"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5036"], "i=17603", ijt_base_objtypes.ICableType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5028", browseName="ns=ijt_base;Cables", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5036"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5131",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6342",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6343",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5133",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6344",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6345",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5039",
    browseName="ns=ijt_base;<MemoryDevice>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5134",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5133"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5039"], "i=17603", ijt_base_objtypes.IMemoryDeviceType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5023", browseName="ns=ijt_base;MemoryDevices", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5039"])])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5132",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6346",
                browseName="ns=ijt_base;Material",
                description="Material is the type or name of the part which is supplied by the feeder.",
                dataType=o6.String,
                value="",
            )
        )
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5038",
    browseName="ns=ijt_base;<Feeder>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5132"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5131"])],
)
o6.reference(o6.ns["ns=ijt_base;i=5038"], "i=17603", ijt_base_objtypes.IFeederType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5031", browseName="ns=ijt_base;Feeders", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5038"])])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5128",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    references=[
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6370",
                browseName="ns=ijt_base;NominalVoltage",
                description="NominalVoltage is the nominal DC voltage of the battery.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6371", browseName="ns=ijt_base;Capacity", description="Capacity is the nominal capacity of the battery.", dataType=o6.Double, value=0.0
            )
        ),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5035",
    browseName="ns=ijt_base;<Battery>",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5128"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5127"])],
)
o6.reference(o6.ns["ns=ijt_base;i=5035"], "i=17603", ijt_base_objtypes.IBatteryType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5029", browseName="ns=ijt_base;Batteries", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5035"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5135",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6372",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6373",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5136",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6390",
                browseName="ns=ijt_base;InputSpecification",
                description="InputSpecification is the input specification of the power supply. Example: 230 V, 50/60 Hz, 10 A.",
                dataType=o6.String,
                value="",
            )
        )
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5040",
    browseName="ns=ijt_base;<PowerSupply>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5136"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5135"])],
)
o6.reference(o6.ns["ns=ijt_base;i=5040"], "i=17603", ijt_base_objtypes.IPowerSupplyType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5030", browseName="ns=ijt_base;PowerSupplies", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5040"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5137",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6391",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6404",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5041",
    browseName="ns=ijt_base;<Sensor>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5138",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5137"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5041"], "i=17603", ijt_base_objtypes.ISensorType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5025", browseName="ns=ijt_base;Sensors", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5041"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5139",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6405",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6410",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5140",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6411",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6444",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5042",
    browseName="ns=ijt_base;<Servo>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5140"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5139"])],
)
o6.reference(o6.ns["ns=ijt_base;i=5042"], "i=17603", ijt_base_objtypes.IServoType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5022", browseName="ns=ijt_base;Servos", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5042"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5141",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6445",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6446",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5043",
    browseName="ns=ijt_base;<SubComponent>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5142",
                browseName="ns=ijt_base;Parameters",
                description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
            )
        ),
        o6.hasAddIn(o6.ns["ns=ijt_base;i=5141"]),
    ],
)
o6.reference(o6.ns["ns=ijt_base;i=5043"], "i=17603", ijt_base_objtypes.ISubComponentType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5033", browseName="ns=ijt_base;SubComponents", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5043"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5143",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6447",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6450",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5101", browseName="ns=ijt_base;<Software>", modellingRule="OptionalPlaceholder", references=[o6.hasAddIn(o6.ns["ns=ijt_base;i=5143"])]
)
o6.reference(o6.ns["ns=ijt_base;i=5101"], "i=17603", ijt_base_objtypes.ISoftwareType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5001", browseName="ns=ijt_base;SoftwareComponents", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5101"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5144",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6451",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6453",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5088", browseName="ns=ijt_base;<VirtualStation>", modellingRule="OptionalPlaceholder", references=[o6.hasAddIn(o6.ns["ns=ijt_base;i=5144"])]
)
o6.reference(o6.ns["ns=ijt_base;i=5088"], "i=17603", ijt_base_objtypes.IVirtualStationType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5087", browseName="ns=ijt_base;VirtualStations", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5088"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=ijt_base;i=5145",
    browseName="ns=di;Identification",
    description="The Identification Object, using the standardized name defined in OPC 10000-100, provides identification information about the asset. This is a mandatory place holder and any asset inheriting IJoiningSystemAssetType will replace it with MachineIdentificationType or MachineryComponentIdentificationType.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6454",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6455",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_base;i=6456",
    browseName="ns=ijt_base;Type",
    description="Type is the classification of a Tool.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_base;i=6457",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("OTHER"), o6.LocalizedText("FIXTURED"), o6.LocalizedText("HANDHELD"), o6.LocalizedText("MANUAL")],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5146",
    browseName="ns=ijt_base;Parameters",
    description="The Parameters Object is an instance of 0:FolderType to group set of common parameters of an asset in a joining system.",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=6456"])],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=ijt_base;i=5044",
    browseName="ns=ijt_base;<Tool>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5146"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5145"])],
)
o6.reference(o6.ns["ns=ijt_base;i=5044"], "i=17603", ijt_base_objtypes.IToolType)
ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5021", browseName="ns=ijt_base;Tools", references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5044"])])
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5016",
    browseName="ns=ijt_base;Assets",
    description="The Assets Object is an instance of FolderType to group set of assets available in the given system.",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=5001"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5018"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5021"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5022"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5023"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5025"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5028"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5029"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5030"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5031"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5032"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5033"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5087"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5165",
    browseName="ns=machinery;Health",
    description="Entry point of health information of the MachineryItem.",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5168", browseName="ns=di;DeviceHealthAlarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6465",
                browseName="ns=di;DeviceHealth",
                description="DeviceHealth indicates the status as defined by NAMUR Recommendation NE107. Clients can read or monitor this Variable to determine the device condition.",
                dataType=di.datatypes.DeviceHealthEnumeration,
                value=di.datatypes.DeviceHealthEnumeration.NORMAL,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6466",
                browseName="ns=ijt_base;ErrorCode",
                description="ErrorCode is the system specific code for the error occurred.",
                dataType=o6.Int64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6467",
                browseName="ns=ijt_base;ErrorMessage",
                description="ErrorMessage is the user readable text of the error reported by the given asset.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6468",
                browseName="ns=ijt_base;ErrorTimestamp",
                description="ErrorTimestamp is the timestamp when the error occurred in the given asset.",
                dataType=ns0.datatypes.UtcTime,
                value=o6.DateTime("1999-12-31T23:00:00Z"),
            )
        ),
        o6.hasComponent(
            ijt_base_vartypes.JoiningDataVariableType(
                nodeId="ns=ijt_base;i=6469",
                browseName="ns=ijt_base;Temperature",
                description="Temperature is the measured temperature of the asset.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
    ],
)
machinery.objtypes.MonitoringType(
    nodeId="ns=ijt_base;i=5162",
    browseName="ns=machinery;Monitoring",
    description="Entry point for monitoring information of a MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5164", browseName="ns=machinery;Consumption", description="Entry point for consumption information of the MachineryItem.")
        ),
        o6.hasComponent(o6.ns["ns=ijt_base;i=5165"]),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5166", browseName="ns=machinery;Process", description="Entry point for process information of the MachineryItem.")
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=ijt_base;i=5167",
                browseName="ns=machinery;Status",
                description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
            )
        ),
    ],
)
o6.reference(ijt_base_objtypes.IJoiningSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5162"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ijt_base;i=6472",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ijt_base;i=6473",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                value="",
            ),
            "i=24136",
        )
    ],
    dataType=ijt_base_datypes.JoiningResultMetaDataType,
)
ijt_base_vartypes.JoiningSystemResultType(
    nodeId="ns=ijt_base;i=6159",
    browseName="ns=ijt_base;<RequestedResultVariable>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(o6.ns["ns=ijt_base;i=6472"], "i=24136")],
    dataType=machinery_result.datatypes.ResultDataType,
    value=machinery_result.datatypes.ResultDataType(
        resultMetaData=machinery_result.datatypes.ResultMetaDataType(
            resultId="",
            hasTransferableDataOnFile=None,
            isPartial=None,
            isSimulated=None,
            resultState=None,
            stepId=None,
            partId=None,
            externalRecipeId=None,
            internalRecipeId=None,
            productId=None,
            externalConfigurationId=None,
            internalConfigurationId=None,
            jobId=None,
            creationTime=None,
            processingTimes=None,
            resultUri=[],
            resultEvaluation=None,
            resultEvaluationCode=None,
            resultEvaluationDetails=None,
            fileFormat=[],
        ),
        resultContent=[],
    ),
)
ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5098",
    browseName="ns=machinery_result;Results",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=6159"]), o6.hasComponent(o6.ns["ns=ijt_base;i=6225"])],
)
o6.reference(ijt_base_objtypes.JoiningSystemResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5098"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6106",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6107",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(name="Result", dataType=o6.NodeId("ns=machinery_result;i=3008"), valueRank=-1, description=o6.LocalizedText("The result including metadata.")),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors.\n"
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7001",
    browseName="ns=machinery_result;GetLatestResult",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6106"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6107"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6095",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("System-wide unique identifier for the result.")),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6096",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0."
            ),
        ),
        ns0.datatypes.Argument(
            name="Result",
            dataType=o6.NodeId("ns=machinery_result;i=3008"),
            valueRank=-1,
            description=o6.LocalizedText("The result including metadata. May be set to Null, if error is set to a value other than 0."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7002",
    browseName="ns=machinery_result;GetResultById",
    description="The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6095"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6096"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6097",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="Filter",
            dataType=ns0.datatypes.ContentFilter,
            valueRank=-1,
            description=o6.LocalizedText(
                "Filter used to filter for specific results based on the meta data of the results. Valid BrowsePaths used in the filter can be built from the fields of the ResultReadyEventType, the ResultType VariableType or the ResultDataType or corresponding subtypes."
            ),
        ),
        ns0.datatypes.Argument(
            name="OrderedBy",
            dataType=ns0.datatypes.RelativePath,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "An array of BrowsePaths (as array of QualifiedName) identifying the ordering criteria for the results. If the array is null or empty, no ordering is executed.\nIf several BrowsePaths are provided, the first entry in the array is used as first ordering criteria, etc.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="MaxResults",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("Defines how many resultIds the Client wants to receive at most. If no maximum should be provided, it is set to 0."),
        ),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6103",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle has to be used by the client to release the result set.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="ResultIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("List of resultIds of results matching the Filter."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7003",
    browseName="ns=machinery_result;GetResultIdListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6097"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6103"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6104",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText("Handle returned by GetResultById or GetResultIdListFiltered, identifying the result set/client combination."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6105",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        )
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7004",
    browseName="ns=machinery_result;ReleaseResultHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6104"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6105"]),
)

ijt_base_objtypes.JoiningSystemResultManagementType(
    nodeId="ns=ijt_base;i=5005",
    browseName="ns=machinery_result;ResultManagement",
    description="The ResultManagement Object is an instance of JoiningSystemResultManagementType which provides mechanisms to access results generated by the joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=ijt_base;i=5078", browseName="ns=machinery_result;Results")),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7001"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7002"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7003"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7004"]),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5005"])
o6.reference(o6.ns["ns=ijt_base;i=5074"], "i=17604", o6.ns["ns=ijt_base;i=5005"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6316",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="JointId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6317",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Joint", dataType=o6.NodeId("ns=ijt_base;i=3028"), valueRank=-1, description=o6.LocalizedText("It is the joint based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7031",
    browseName="ns=ijt_base;GetJoint",
    description="The Method GetJoint is used to get the joint based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6316"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6317"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6318",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointComponentId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint component.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6319",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointComponent", dataType=o6.NodeId("ns=ijt_base;i=3021"), valueRank=-1, description=o6.LocalizedText("It is the joint component based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7032",
    browseName="ns=ijt_base;GetJointComponent",
    description="The Method GetJointComponent is used to get the joint component based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6318"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6319"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6320",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6321",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointComponentList",
            dataType=o6.NodeId("ns=ijt_base;i=3021"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joint components available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7033",
    browseName="ns=ijt_base;GetJointComponentList",
    description="The Method GetJointComponentList is used to get the list of available joint components in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6320"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6321"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6322",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointDesignId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the joint design based on the input identifier.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6323",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointDesign", dataType=o6.NodeId("ns=ijt_base;i=3025"), valueRank=-1, description=o6.LocalizedText("It is the joint design based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7034",
    browseName="ns=ijt_base;GetJointDesign",
    description="The Method GetJointDesign is used to get the joint design based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6322"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6323"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6324",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6325",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointDesignList",
            dataType=o6.NodeId("ns=ijt_base;i=3025"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joint designs available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7035",
    browseName="ns=ijt_base;GetJointDesignList",
    description="The Method GetJointDesignList is used to get the list of available joint designs in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6324"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6325"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6326",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6327",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointList",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joints available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7036",
    browseName="ns=ijt_base;GetJointList",
    description="The Method GetJointList is used to get the list of available joints in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6326"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6327"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6328",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("It is the origin identifier of the joint which is used to manage the revisions of a given joint."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6329",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointList",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joints available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7037",
    browseName="ns=ijt_base;GetJointRevisionList",
    description="The Method GetJointRevisionList is used to get the list available revisions of a specific joint based on the JointOriginId.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6328"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6329"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6330",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the joint which should be selected for performing the next joining operation."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the common identifier of the joint which should be selected for performing the next joining operation.\n\nIt is optional and can be empty if the underlying system does not manage revisions of a joint. If JointId is provided, then this argument shall be ignored."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6331",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7038",
    browseName="ns=ijt_base;SelectJoint",
    description="The Method SelectJoint is used to select the joint and the associated joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6330"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6331"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6332",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Joint",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joint."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6333",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7039",
    browseName="ns=ijt_base;SendJoint",
    description="The Method SendJoint is used to send a joint to a joining system. If the input joint already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6332"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6333"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6334",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointComponent",
            dataType=o6.NodeId("ns=ijt_base;i=3021"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the joint component."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6335",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7040",
    browseName="ns=ijt_base;SendJointComponent",
    description="The Method SendJointComponent is used to send a joint component to a joining system. If the input joint component already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6334"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6335"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6336",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointDesign",
            dataType=o6.NodeId("ns=ijt_base;i=3025"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joint design."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6337",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7041",
    browseName="ns=ijt_base;SendJointDesign",
    description="The Method SendJointDesign is used to send a joint design to a joining system. If the input joint design already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6336"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6337"]),
)

ijt_base_objtypes.JointManagementType(
    nodeId="ns=ijt_base;i=5100",
    browseName="ns=ijt_base;JointManagement",
    description="The JointManagement Object is an instance of JointManagementType which provides mechanisms to manage joint and associated information.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=7031"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7032"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7033"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7034"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7035"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7036"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7037"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7038"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7039"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7040"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7041"]),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5100"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6376",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="AbortMessage",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText("It is an optional message sent from the Client to the joining system to indicate the reason for aborting the joining operation."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6377",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7057",
    browseName="ns=ijt_base;AbortJoiningProcess",
    description="The Method AbortJoiningProcess is used to abort the input joining process if it is under execution.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6376"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6377"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6378",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="DecrementCount",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("It is the number of decrements to be done for the joining process counter.\nThe default value is 1 if it is not provided."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6379",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7058",
    browseName="ns=ijt_base;DecrementJoiningProcessCounter",
    description="The Method DecrementJoiningProcessCounter used to decrement the counter of the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6378"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6379"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6380",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6381",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7059",
    browseName="ns=ijt_base;DeselectJoiningProcess",
    description="The Method DeselectJoiningProcess is used to deselect any selected joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6380"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6381"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6382",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6383",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JoiningProcessList",
            dataType=o6.NodeId("ns=ijt_base;i=3024"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joining process meta data available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7060",
    browseName="ns=ijt_base;GetJoiningProcessList",
    description="The Method GetJoiningProcessList is used to get the list of joining process meta data available in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6382"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6383"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6384",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7061",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("It is the origin identifier of the joining process which is used to manage the revisions of a given joining process."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6385",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7061",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JoiningProcessList",
            dataType=o6.NodeId("ns=ijt_base;i=3024"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joining process meta data available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7061",
    browseName="ns=ijt_base;GetJoiningProcessRevisionList",
    description="The Method GetJoiningProcessRevisionList is used to get the list available revisions of a specific joining process based on the joiningProcessOriginId.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6384"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6385"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6386",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7062",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="IncrementCount",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("It is the number of increments to be done for the joining process counter.\nThe default value is 1 if it is not provided."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6387",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7062",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7062",
    browseName="ns=ijt_base;IncrementJoiningProcessCounter",
    description="The Method IncrementJoiningProcessCounter is used to increment the counter of the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6386"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6387"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6388",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6389",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7063",
    browseName="ns=ijt_base;ResetJoiningProcess",
    description="The Method ResetJoiningProcess is used to reset/restart the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6388"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6389"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6392",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7065",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6393",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7065",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7065",
    browseName="ns=ijt_base;SelectJoiningProcess",
    description="The Method SelectJoiningProcess is used to select the joining process based on the input arguments.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6392"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6393"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6394",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7066",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcess",
            dataType=o6.NodeId("ns=ijt_base;i=3016"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joining process."),
        ),
        ns0.datatypes.Argument(
            name="SelectionName",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the required selection name for the given joining process. It is optional and can be empty."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6395",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7066",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7066",
    browseName="ns=ijt_base;SendJoiningProcess",
    description="The Method SendJoiningProcess is used to send a joining process to the joining system. It can be used to insert a joining program or joining batch or joining job or any other process applicable to a joining system. It shall overwrite the joining process if it already exists in the joining system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6394"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6395"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6396",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(name="CounterValue", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("It is the new counter value for the joining process.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6397",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7067",
    browseName="ns=ijt_base;SetJoiningProcessCounter",
    description="The Method SetJoiningProcessCounter is used to set the counter of a sequential joining processes (such as Job, etc.) to the given input value.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6396"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6397"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6398",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to map the respective joiningProcessId with selectionName and joiningProcessOriginId.\n\nIt shall at least contain the joiningProcessId and selectionName."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6399",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7068",
    browseName="ns=ijt_base;SetJoiningProcessMapping",
    description="The Method SetJoiningProcessMapping is used to set the mapping of the joining process in a joining system. It can be used to map a joining process to a selection name.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6398"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6399"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6400",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(name="MaxCounterSize", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("It is the maximum counter size for the joining process.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6401",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7069",
    browseName="ns=ijt_base;SetJoiningProcessSize",
    description="The Method SetJoiningProcessSize is used to set the size of the batch joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6400"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6401"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6402",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="AssociatedEntities",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers used for performing the joining operation. It is optional and can be empty."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6403",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7070",
    browseName="ns=ijt_base;StartJoiningProcess",
    description="The Method StartJoiningProcess is used to start the input joining process. \nNote: It is not intended to be used in a hard real-time use case.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6402"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6403"]),
)

ijt_base_objtypes.JoiningProcessManagementType(
    nodeId="ns=ijt_base;i=5113",
    browseName="ns=ijt_base;JoiningProcessManagement",
    description="The JoiningProcessManagement Object is an instance of JoiningProcessManagementType which provides mechanisms to manage joining processes in the joining system.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=7057"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7058"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7059"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7060"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7061"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7062"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7063"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7065"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7066"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7067"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7068"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7069"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7070"]),
    ],
)
o6.reference(ijt_base_objtypes.JoiningSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=ijt_base;i=5113"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6412",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7075",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Disconnect", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("If true, it will prepare the asset for disconnect. The default value is false.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6413",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7075",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7075",
    browseName="ns=ijt_base;DisconnectAsset",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6412"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6413"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6414",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Enable",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If true, it will enable the asset, else it will disable the asset. The default value is false.\nNote: If the asset is performing the joining operation when the method is executed, then it shall disable the asset after the current operation.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6415",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7076", browseName="ns=ijt_base;EnableAsset", inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6414"]), outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6415"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6416",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7077",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="OperationType",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the type of operation. The list of integer values corresponding to a specific operation is provided by the documentation or the joining system via some interface."
            ),
        ),
        ns0.datatypes.Argument(
            name="OperationText", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("It is the optional text to provide information on the type of operation.")
        ),
        ns0.datatypes.Argument(
            name="VendorName",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("It is the optional vendor&#8217;s name provided to identify the type of operations supported."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6417",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7077",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7077",
    browseName="ns=ijt_base;ExecuteOperation",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6416"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6417"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6418",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7078",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="ErrorId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identifier of the error. It could be available as part of the JoiningResult.\nNote: If it is empty, the Server is allowed to return the latest error available.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6419",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7078",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ErrorContent",
            dataType=ns0.datatypes.BaseDataType,
            valueRank=-1,
            description=o6.LocalizedText("It is the detailed error information.\nExamples: Log file, Detailed Error Information or Event Logs, etc.\n", ""),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7078",
    browseName="ns=ijt_base;GetErrorInformation",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6418"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6419"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6420",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6421",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="FeedbackFileList",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of feedback files available in the system. It contains the feedback filenames or the file paths which can be used as an input in SendFeedback method."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7079",
    browseName="ns=ijt_base;GetFeedbackFileList",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6420"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6421"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6422",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="SignalIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of signal identifiers requested. If it is empty, then all the available signals are returned from the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6423",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SignalList",
            dataType=o6.NodeId("ns=ijt_base;i=3019"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of signals which are available in the asset based on the input signalIdList. \nIf the signalIdList is empty, then all the available signals are sent from the asset."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7080",
    browseName="ns=ijt_base;GetIOSignals",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6422"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6423"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6424",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7081",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierNames",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The list of names of the identifiers which are requested. If it is empty, then all available identifiers are returned."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6425",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7081",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="EntityList",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers available in the joining system based on the input criteria."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7081",
    browseName="ns=ijt_base;GetIdentifiers",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6424"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6425"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6426",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6427",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7082", browseName="ns=ijt_base;RebootAsset", inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6426"]), outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6427"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6428",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of names of the identifiers which are requested to be reset. \nIf it is NOT empty, then resetAll and resetLatest flags are ignored.\nIf it is empty, then the resetAll or resetLatest flag is used."
            ),
        ),
        ns0.datatypes.Argument(
            name="ResetAll",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If True, it will reset all the identifiers available in the joining system and resetLatest flag is ignored.\nIf False and identifierList is empty then the resetLatest flag is used.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="ResetLatest",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If True, it will reset the latest identifier available in the system.\nNote: This is provided for supporting legacy systems. The criteria to determine which identifier is latest is application specific.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6429",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7083",
    browseName="ns=ijt_base;ResetIdentifiers",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6428"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6429"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6430",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7084",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="FeedbackType",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the type of feedback and has the following pre-defined values:\n0 &#8211; UNDEFINED\n1 &#8211; OTHER\n2 &#8211; TEXT\n3 &#8211; VISUAL\n4 &#8211; AUDIO\n5 &#8211; VIBRATE",
                "",
            ),
        ),
        ns0.datatypes.Argument(name="FeedbackText", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("It is the text feedback if the feedbackType is TEXT.")),
        ns0.datatypes.Argument(
            name="FeedbackFile",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the file available in the asset which needs to be run for different types of feedback such as AUDIO, VIBRATE, etc. This can be retrieved using the GetFeedbackFileList method.\nIt is optional and not applicable for text feedback."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6431",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7084",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7084",
    browseName="ns=ijt_base;SendFeedback",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6430"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6431"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6432",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="EntityList",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers sent to the joining system."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6433",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7085",
    browseName="ns=ijt_base;SendIdentifiers",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6432"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6433"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6434",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers sent to the joining system."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6435",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7086",
    browseName="ns=ijt_base;SendTextIdentifiers",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6434"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6435"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6436",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7087",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="CalibrationData",
            dataType=o6.NodeId("ns=ijt_base;i=3003"),
            valueRank=-1,
            description=o6.LocalizedText("It is the input calibration data which needs to be configured for the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6437",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7087",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7087",
    browseName="ns=ijt_base;SetCalibration",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6436"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6437"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6438",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="SignalList",
            dataType=o6.NodeId("ns=ijt_base;i=3019"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of signals which needs to be set in the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6439",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SignalStatusList",
            dataType=o6.Int32,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of status for each signal.\n0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7088",
    browseName="ns=ijt_base;SetIOSignals",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6438"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6439"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6440",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7089",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="OfflineTimer",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("It is the offlineTimer to be set. The behaviour of the asset when the timer is elapsed is application specific."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6441",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7089",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7089",
    browseName="ns=ijt_base;SetOfflineTimer",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6440"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6441"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6442",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7090",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="InputTime", dataType=ns0.datatypes.UtcTime, valueRank=-1, description=o6.LocalizedText("It is the input time to be configured in the asset.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6443",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7090",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7090", browseName="ns=ijt_base;SetTime", inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6442"]), outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6443"])
)

ijt_base_objtypes.JoiningSystemAssetMethodSetType(
    nodeId="ns=ijt_base;i=5124",
    browseName="ns=di;MethodSet",
    description="The MethodSet Object is an instance of JoiningSystemAssetMethodSetType which provides set of methods for various assets in a joining system.",
    references=[
        o6.hasComponent(o6.ns["ns=ijt_base;i=7075"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7076"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7077"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7078"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7079"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7080"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7081"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7082"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7083"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7084"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7085"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7086"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7087"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7088"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7089"]),
        o6.hasComponent(o6.ns["ns=ijt_base;i=7090"]),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=ijt_base;i=5004",
    browseName="ns=ijt_base;AssetManagement",
    description="The AssetManagement Object is an instance of FunctionalGroupType to group assets and related objects in the joining system.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=ijt_base;i=5016"]), o6.hasAddIn(o6.ns["ns=ijt_base;i=5124"])],
)
o6.reference(ijt_base_objtypes.JoiningSystemType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_base;i=5004"])


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, machinery_result, ns0, ijt_base_datypes, ijt_base_vartypes, ijt_base_objtypes
