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

"""Generated OPC UA pnrio namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnrio_reftypes
from . import datatypes as pnrio_datypes
from . import vartypes as pnrio_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=pnrio;i=1018", browseName="ns=pnrio;PnTelegramType", displayName="PnTelegramType")
class PnTelegramType(ns0.objtypes.BaseObjectType):
    input: PnIoTelegramType | None
    output: PnIoTelegramType | None


@o6.objecttype(nodeId="ns=pnrio;i=1020", browseName="ns=pnrio;PnIoSignalType", displayName="PnIoSignalType")
class PnIoSignalType(ns0.objtypes.BaseObjectType):
    offset: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6207", browseName="ns=pnrio;Offset", dataType=o6.UInt16))
    signalId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6206", browseName="ns=pnrio;SignalId", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=pnrio;i=1019", browseName="ns=pnrio;RioChannelDiagnosisEventType", displayName="RioChannelDiagnosisEventType")
class RioChannelDiagnosisEventType(ns0.objtypes.BaseEventType):
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6232", browseName="ns=pnrio;ApplicationTag", dataType=o6.String))
    helpText: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6234", browseName="ns=pnrio;HelpText", dataType=o6.LocalizedText))
    manufacturerData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6233", browseName="ns=pnrio;ManufacturerData", dataType=o6.ByteString)
    )
    pnChannelNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6228", browseName="ns=pnrio;PnChannelNumber", dataType=o6.UInt32)
    )
    reason: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6230", browseName="ns=pnrio;Reason", dataType=pnrio_datypes.RioChannelDiagnosisReasonEnumeration)
    )
    rioChannelNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6227", browseName="ns=pnrio;RioChannelNumber", dataType=o6.UInt16))
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6229", browseName="ns=pnrio;Status", dataType=pnrio_datypes.RioChannelDiagnosisStatusEnumeration)
    )


@o6.objecttype(nodeId="ns=pnrio;i=1004", browseName="ns=pnrio;RioChannelDiagnosisAlarmType", displayName="RioChannelDiagnosisAlarmType")
class RioChannelDiagnosisAlarmType(ns0.objtypes.AlarmConditionType):
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6109", browseName="ns=pnrio;ApplicationTag", dataType=o6.String))
    helpText: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6111", browseName="ns=pnrio;HelpText", dataType=o6.LocalizedText))
    manufacturerData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6110", browseName="ns=pnrio;ManufacturerData", dataType=o6.ByteString)
    )
    pnChannelNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6270", browseName="ns=pnrio;PnChannelNumber", dataType=o6.UInt32)
    )
    reason: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6108", browseName="ns=pnrio;Reason", dataType=pnrio_datypes.RioChannelDiagnosisReasonEnumeration)
    )
    rioChannelNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6107", browseName="ns=pnrio;RioChannelNumber", dataType=o6.UInt16))
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6271", browseName="ns=pnrio;Status", dataType=pnrio_datypes.RioChannelDiagnosisStatusEnumeration)
    )


@o6.objecttype(nodeId="ns=pnrio;i=1021", browseName="ns=pnrio;PnIoTelegramType", displayName="PnIoTelegramType")
class PnIoTelegramType(ns0.objtypes.BaseObjectType):
    consumerStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6279", browseName="ns=pnrio;ConsumerStatus", dataType=pnrio_datypes.PnIoTelegramStatusEnumeration)
    )
    ioTelegramImage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6276", browseName="ns=pnrio;IoTelegramImage", dataType=o6.ByteString)
    )
    langleNr_SignalNameRangle: PnIoSignalType
    length: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6277", browseName="ns=pnrio;Length", dataType=o6.UInt16))
    providerStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6278", browseName="ns=pnrio;ProviderStatus", dataType=pnrio_datypes.PnIoTelegramStatusEnumeration)
    )


@o6.objecttype(nodeId="ns=pnrio;i=1017", browseName="ns=pnrio;RioChannelGroupConfigType", displayName="RioChannelGroupConfigType")
class RioChannelGroupConfigType(ns0.objtypes.BaseObjectType):
    damping: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6200", browseName="ns=pnrio;Damping", dataType=o6.Float))
    faAnalogSubstituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pnrio;i=6290", browseName="ns=pnrio;FaAnalogSubstituteValue", dataType=pnrio_datypes.RioAnalogDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    faDigitalSubstituteValue: pnrio_vartypes.RioBitFieldVariableType | None = o6.hasComponent(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6204",
            browseName="ns=pnrio;FaDigitalSubstituteValue",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        )
    )
    highLimit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6201", browseName="ns=pnrio;HighLimit", dataType=pnrio_datypes.RioAnalogDataType)
    )
    inversionEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6192", browseName="ns=pnrio;InversionEnabled", dataType=o6.Boolean)
    )
    loadVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6196", browseName="ns=pnrio;LoadVoltageCheckEnabled", dataType=o6.Boolean)
    )
    lowLimit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6202", browseName="ns=pnrio;LowLimit", dataType=pnrio_datypes.RioAnalogDataType)
    )
    paAnalogSubstituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pnrio;i=6289", browseName="ns=pnrio;PaAnalogSubstituteValue", dataType=pnrio_datypes.RioAnalogDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    paDigitalSubstituteValue: pnrio_vartypes.RioBitFieldVariableType | None = o6.hasComponent(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6198",
            browseName="ns=pnrio;PaDigitalSubstituteValue",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        )
    )
    shortCircuitCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6193", browseName="ns=pnrio;ShortCircuitCheckEnabled", dataType=o6.Boolean)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6191", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6197", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteTime: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6199", browseName="ns=pnrio;SubstituteTime", dataType=o6.Float))
    supplyVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6195", browseName="ns=pnrio;SupplyVoltageCheckEnabled", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6194", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6072",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationTag", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7001", browseName="ns=pnrio;SetApplicationTag", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6072"]))


@o6.objecttype(nodeId="ns=pnrio;i=1012", browseName="ns=pnrio;RioChannelGroupType", displayName="RioChannelGroupType", isAbstract=True)
class RioChannelGroupType(ns0.objtypes.BaseObjectType):
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6164", browseName="ns=pnrio;ApplicationTag", dataType=o6.String))
    channelGroupConfig: RioChannelGroupConfigType | None = o6.reference(
        RioChannelGroupConfigType(nodeId="ns=pnrio;i=5045", browseName="ns=pnrio;ChannelGroupConfig"), "ns=pnrio;i=4007"
    )
    langleRioInputChannelRangle: RioChannelType | None
    langleRioOutputChannelRangle: RioChannelType | None
    lastParameterChange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6165", browseName="ns=pnrio;LastParameterChange", dataType=o6.DateTime)
    )
    lock: di.objtypes.LockingServicesType | None
    numberOfChannels: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6226", browseName="ns=pnrio;NumberOfChannels", dataType=o6.UInt16, valueRank=1, arrayDimensions=[5])
    )
    setApplicationTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7001"])


o6.reference(RioChannelGroupType, "i=41", RioChannelDiagnosisAlarmType)
o6.reference(RioChannelGroupType, "i=41", RioChannelDiagnosisEventType)


@o6.objecttype(nodeId="ns=pnrio;i=1014", browseName="ns=pnrio;RioFaAnalogChannelGroupType", displayName="RioFaAnalogChannelGroupType")
class RioFaAnalogChannelGroupType(RioChannelGroupType):
    inputImageQualifiers: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6174",
            browseName="ns=pnrio;InputImageQualifiers",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        ),
        "ns=pnrio;i=4006",
    )
    inputImageValues: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6173", browseName="ns=pnrio;InputImageValues", dataType=pnrio_datypes.RioAnalogDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pnrio;i=4006",
    )
    outputImageQualifiers: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6175",
            browseName="ns=pnrio;OutputImageQualifiers",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        ),
        "ns=pnrio;i=4006",
    )
    outputImageValues: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6176", browseName="ns=pnrio;OutputImageValues", dataType=pnrio_datypes.RioAnalogDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pnrio;i=4006",
    )


@o6.objecttype(nodeId="ns=pnrio;i=1016", browseName="ns=pnrio;RioFaDigitalChannelGroupType", displayName="RioFaDigitalChannelGroupType")
class RioFaDigitalChannelGroupType(RioChannelGroupType):
    inputImage: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6177", browseName="ns=pnrio;InputImage", dataType=pnrio_datypes.RioBitFieldDataType, value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0)
        ),
        "ns=pnrio;i=4006",
    )
    inputImageQualifiers: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6178",
            browseName="ns=pnrio;InputImageQualifiers",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        ),
        "ns=pnrio;i=4006",
    )
    outputImage: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6183", browseName="ns=pnrio;OutputImage", dataType=pnrio_datypes.RioBitFieldDataType, value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0)
        ),
        "ns=pnrio;i=4006",
    )
    outputImageQualifiers: pnrio_vartypes.RioBitFieldVariableType | None = o6.reference(
        pnrio_vartypes.RioBitFieldVariableType(
            nodeId="ns=pnrio;i=6184",
            browseName="ns=pnrio;OutputImageQualifiers",
            dataType=pnrio_datypes.RioBitFieldDataType,
            value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
        ),
        "ns=pnrio;i=4006",
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6186",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationTag", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7002", browseName="ns=pnrio;SetApplicationTag", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6186"]))


@o6.objecttype(nodeId="ns=pnrio;i=1005", browseName="ns=pnrio;RioChannelType", displayName="RioChannelType", isAbstract=True)
class RioChannelType(ns0.objtypes.BaseObjectType):
    applicationTag: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6113", browseName="ns=pnrio;ApplicationTag", dataType=o6.String))
    lastParameterChange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6274", browseName="ns=pnrio;LastParameterChange", dataType=o6.DateTime)
    )
    lock: di.objtypes.LockingServicesType | None
    rioChannelNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6112", browseName="ns=pnrio;RioChannelNumber", dataType=o6.UInt16))
    setApplicationTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7002"])


o6.reference(RioChannelType, "i=41", RioChannelDiagnosisAlarmType)
o6.reference(RioChannelType, "i=41", RioChannelDiagnosisEventType)


@o6.objecttype(nodeId="ns=pnrio;i=1003", browseName="ns=pnrio;RioFaAnalogInputChannelType", displayName="RioFaAnalogInputChannelType")
class RioFaAnalogInputChannelType(RioChannelType):
    config: pnrio_vartypes.RioFaAnalogInputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaAnalogInputConfigVariableType(
            nodeId="ns=pnrio;i=6121",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioFaAnalogInputConfigDataType,
            value=pnrio_datypes.RioFaAnalogInputConfigDataType(
                damping=0.0,
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                supplyVoltageCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
            ),
        )
    )
    processValue: pnrio_vartypes.RioFaAnalogProcessValueVariableType
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6120", browseName="ns=pnrio;SignalValue", dataType=o6.Double))


@o6.objecttype(nodeId="ns=pnrio;i=1007", browseName="ns=pnrio;RioFaAnalogOutputChannelType", displayName="RioFaAnalogOutputChannelType")
class RioFaAnalogOutputChannelType(RioChannelType):
    config: pnrio_vartypes.RioFaAnalogOutputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaAnalogOutputConfigVariableType(
            nodeId="ns=pnrio;i=6139",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioFaAnalogOutputConfigDataType,
            value=pnrio_datypes.RioFaAnalogOutputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                supplyVoltageCheckEnabled=False,
                loadVoltageCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
                substituteTime=0.0,
            ),
        )
    )
    processValue: pnrio_vartypes.RioFaAnalogProcessValueVariableType
    processValueReadback: pnrio_vartypes.RioFaAnalogProcessValueVariableType | None
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6137", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    signalValueReadback: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6138", browseName="ns=pnrio;SignalValueReadback", dataType=o6.Double)
    )


@o6.objecttype(nodeId="ns=pnrio;i=1009", browseName="ns=pnrio;RioFaDigitalInputChannelType", displayName="RioFaDigitalInputChannelType")
class RioFaDigitalInputChannelType(RioChannelType):
    config: pnrio_vartypes.RioFaDigitalInputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaDigitalInputConfigVariableType(
            nodeId="ns=pnrio;i=6149",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioFaDigitalInputConfigDataType,
            value=pnrio_datypes.RioFaDigitalInputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                supplyVoltageCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=False,
            ),
        )
    )
    processValue: pnrio_vartypes.RioFaDigitalProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6147",
            browseName="ns=pnrio;ProcessValue",
            dataType=pnrio_datypes.RioFaDigitalProcessValueDataType,
            value=pnrio_datypes.RioFaDigitalProcessValueDataType(value=False, qualifier=False, quality=0),
        )
    )
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6148", browseName="ns=pnrio;SignalValue", dataType=o6.Double))


@o6.objecttype(nodeId="ns=pnrio;i=1011", browseName="ns=pnrio;RioFaDigitalOutputChannelType", displayName="RioFaDigitalOutputChannelType")
class RioFaDigitalOutputChannelType(RioChannelType):
    config: pnrio_vartypes.RioFaDigitalOutputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaDigitalOutputConfigVariableType(
            nodeId="ns=pnrio;i=6163",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioFaDigitalOutputConfigDataType,
            value=pnrio_datypes.RioFaDigitalOutputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                supplyVoltageCheckEnabled=False,
                loadVoltageCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=False,
                substituteTime=0.0,
            ),
        )
    )
    processValue: pnrio_vartypes.RioFaDigitalProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioFaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6159",
            browseName="ns=pnrio;ProcessValue",
            dataType=pnrio_datypes.RioFaDigitalProcessValueDataType,
            value=pnrio_datypes.RioFaDigitalProcessValueDataType(value=False, qualifier=False, quality=0),
        )
    )
    processValueReadback: pnrio_vartypes.RioFaDigitalProcessValueVariableType | None = o6.hasComponent(
        pnrio_vartypes.RioFaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6160",
            browseName="ns=pnrio;ProcessValueReadback",
            dataType=pnrio_datypes.RioFaDigitalProcessValueDataType,
            value=pnrio_datypes.RioFaDigitalProcessValueDataType(value=False, qualifier=False, quality=0),
        )
    )
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6161", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    signalValueReadback: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6162", browseName="ns=pnrio;SignalValueReadback", dataType=o6.Double)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6133",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Value used to set the Value of one SimulationEnabled array element.")
        ),
        ns0.datatypes.Argument(
            name="Index",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("Index of array element to set. If -1, the SimulationEnabled parameter is assigned to all array elements."),
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7005", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6133"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6169",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Value used to set the Value of one SimulationEnabled array element.")
        ),
        ns0.datatypes.Argument(
            name="Index",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("Index of array element to set. If -1, the SimulationEnabled parameter is assigned to all array elements."),
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7006", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6169"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6292",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Value", dataType=o6.NodeId("ns=pnrio;i=3020"), valueRank=-1, description=o6.LocalizedText("Value used to set the Value member of the array element.")
        ),
        ns0.datatypes.Argument(name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Value used to set the Qualifier member of the array element.")),
        ns0.datatypes.Argument(
            name="Index", dataType=o6.Int16, valueRank=-1, description=o6.LocalizedText("Index of array element to set. If -1, the parameters are assigned to all array elements.")
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7023", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6292"]))


@o6.objecttype(nodeId="ns=pnrio;i=1013", browseName="ns=pnrio;RioPaAnalogChannelGroupType", displayName="RioPaAnalogChannelGroupType")
class RioPaAnalogChannelGroupType(RioChannelGroupType):
    inputValues: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6170",
            browseName="ns=pnrio;InputValues",
            dataType=pnrio_datypes.RioPaAnalogValueDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[pnrio_datypes.RioPaAnalogValueDataType(value=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0), qualifier=0)],
        ),
        "ns=pnrio;i=4006",
    )
    outputValues: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6171",
            browseName="ns=pnrio;OutputValues",
            dataType=pnrio_datypes.RioPaAnalogValueDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[pnrio_datypes.RioPaAnalogValueDataType(value=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0), qualifier=0)],
        ),
        "ns=pnrio;i=4006",
    )
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7005"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7023"])
    simulationEnabled: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6010", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0])
    )
    simulationValues: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pnrio;i=6291",
            browseName="ns=pnrio;SimulationValues",
            dataType=pnrio_datypes.RioPaAnalogValueDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[pnrio_datypes.RioPaAnalogValueDataType(value=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0), qualifier=0)],
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6293",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.NodeId("ns=pnrio;i=3007"), valueRank=-1, description=o6.LocalizedText("Desired content of the Mode Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7024", browseName="ns=pnrio;SetMode", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6293"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6294",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ManualProcessValue", dataType=o6.NodeId("ns=pnrio;i=3020"), valueRank=-1, description=o6.LocalizedText("Desired Value of the ManualProcessValue Variable.")
        )
    ],
)
o6.call(nodeId="ns=pnrio;i=7025", browseName="ns=pnrio;SetManualProcessValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6294"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6295",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7026", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6295"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6296",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="Value",
            dataType=o6.NodeId("ns=pnrio;i=3020"),
            valueRank=-1,
            description=o6.LocalizedText("Desired content of the Value struct member of the SimulationValue Variable."),
        ),
        ns0.datatypes.Argument(
            name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Desired content of the Qualifier struct member of the SimulationValue Variable.")
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7027", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6296"]))


@o6.objecttype(nodeId="ns=pnrio;i=1002", browseName="ns=pnrio;RioPaAnalogInputChannelType", displayName="RioPaAnalogInputChannelType")
class RioPaAnalogInputChannelType(RioChannelType):
    config: pnrio_vartypes.RioPaAnalogInputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaAnalogInputConfigVariableType(
            nodeId="ns=pnrio;i=6116",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioPaAnalogInputConfigDataType,
            value=pnrio_datypes.RioPaAnalogInputConfigDataType(
                damping=0.0,
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
                highLimit=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
                lowLimit=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
            ),
        )
    )
    manualProcessValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6114", browseName="ns=pnrio;ManualProcessValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    mode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6003", browseName="ns=pnrio;Mode", dataType=pnrio_datypes.RioChannelModeEnumeration)
    )
    processValue: pnrio_vartypes.RioPaAnalogProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaAnalogProcessValueVariableType(nodeId="ns=pnrio;i=6001", browseName="ns=pnrio;ProcessValue", dataType=pnrio_datypes.RioPaAnalogProcessValueDataType)
    )
    setManualProcessValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7025"])
    setMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7024"])
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7026"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7027"])
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6002", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    simulationEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6115", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean)
    )
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6004",
            browseName="ns=pnrio;SimulationValue",
            dataType=pnrio_datypes.RioPaAnalogValueDataType,
            value=pnrio_datypes.RioPaAnalogValueDataType(value=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0), qualifier=0),
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6297",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.NodeId("ns=pnrio;i=3007"), valueRank=-1, description=o6.LocalizedText("Desired content of the Mode Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7028", browseName="ns=pnrio;SetMode", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6297"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6298",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ManualOutValue", dataType=o6.NodeId("ns=pnrio;i=3020"), valueRank=-1, description=o6.LocalizedText("Desired Value of the ManualOutValue Variable.")
        )
    ],
)
o6.call(nodeId="ns=pnrio;i=7029", browseName="ns=pnrio;SetManualOutValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6298"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6299",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7030", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6299"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6300",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="Value", dataType=o6.NodeId("ns=pnrio;i=3020"), valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable.")
        ),
        ns0.datatypes.Argument(name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable.")),
    ],
)
o6.call(nodeId="ns=pnrio;i=7031", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6300"]))


@o6.objecttype(nodeId="ns=pnrio;i=1006", browseName="ns=pnrio;RioPaAnalogOutputChannelType", displayName="RioPaAnalogOutputChannelType")
class RioPaAnalogOutputChannelType(RioChannelType):
    config: pnrio_vartypes.RioPaAnalogOutputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaAnalogOutputConfigVariableType(
            nodeId="ns=pnrio;i=6130",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioPaAnalogOutputConfigDataType,
            value=pnrio_datypes.RioPaAnalogOutputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
                substituteTime=0.0,
            ),
        )
    )
    manualOutValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6128", browseName="ns=pnrio;ManualOutValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    mode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6126", browseName="ns=pnrio;Mode", dataType=pnrio_datypes.RioChannelModeEnumeration)
    )
    processValue: pnrio_vartypes.RioPaAnalogProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaAnalogProcessValueVariableType(nodeId="ns=pnrio;i=6122", browseName="ns=pnrio;ProcessValue", dataType=pnrio_datypes.RioPaAnalogProcessValueDataType)
    )
    processValueReadback: pnrio_vartypes.RioPaAnalogProcessValueVariableType | None = o6.hasComponent(
        pnrio_vartypes.RioPaAnalogProcessValueVariableType(
            nodeId="ns=pnrio;i=6123", browseName="ns=pnrio;ProcessValueReadback", dataType=pnrio_datypes.RioPaAnalogProcessValueDataType
        )
    )
    setManualOutValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7029"])
    setMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7028"])
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7030"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7031"])
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6124", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    signalValueReadback: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6125", browseName="ns=pnrio;SignalValueReadback", dataType=o6.Double)
    )
    simulationEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6129", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean)
    )
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6127",
            browseName="ns=pnrio;SimulationValue",
            dataType=pnrio_datypes.RioPaAnalogValueDataType,
            value=pnrio_datypes.RioPaAnalogValueDataType(value=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0), qualifier=0),
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6301",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.NodeId("ns=pnrio;i=3007"), valueRank=-1, description=o6.LocalizedText("Desired content of the Mode Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7032", browseName="ns=pnrio;SetMode", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6301"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6302",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ManualProcessValue", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired Value of the ManualProcessValue Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7033", browseName="ns=pnrio;SetManualProcessValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6302"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6303",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7034", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6303"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6304",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="Value", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the Value struct member of the SimulationValue Variable.")
        ),
        ns0.datatypes.Argument(
            name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Desired content of the Qualifier struct member of the SimulationValue Variable.")
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7035", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6304"]))


@o6.objecttype(nodeId="ns=pnrio;i=1008", browseName="ns=pnrio;RioPaDigitalInputChannelType", displayName="RioPaDigitalInputChannelType")
class RioPaDigitalInputChannelType(RioChannelType):
    config: pnrio_vartypes.RioPaDigitalInputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaDigitalInputConfigVariableType(
            nodeId="ns=pnrio;i=6146",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioPaDigitalInputConfigDataType,
            value=pnrio_datypes.RioPaDigitalInputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                inversionEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=False,
            ),
        )
    )
    manualProcessValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6144", browseName="ns=pnrio;ManualProcessValue", dataType=o6.Boolean)
    )
    mode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6142", browseName="ns=pnrio;Mode", dataType=pnrio_datypes.RioChannelModeEnumeration)
    )
    processValue: pnrio_vartypes.RioPaDigitalProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6140",
            browseName="ns=pnrio;ProcessValue",
            dataType=pnrio_datypes.RioPaDigitalProcessValueDataType,
            value=pnrio_datypes.RioPaDigitalProcessValueDataType(value=False, qualifier=0, quality=0, nE_107=0, status_full=0),
        )
    )
    setManualProcessValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7033"])
    setMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7032"])
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7034"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7035"])
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6141", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    simulationEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6145", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean)
    )
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6143", browseName="ns=pnrio;SimulationValue", dataType=pnrio_datypes.RioPaDigitalValueDataType)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.NodeId("ns=pnrio;i=3007"), valueRank=-1, description=o6.LocalizedText("Desired content of the Mode Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7036", browseName="ns=pnrio;SetMode", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6305"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6306",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SimulationEnabled", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the SimulationEnabled Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7037", browseName="ns=pnrio;SetSimulation", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6306"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6307",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="Value", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired content of the Value struct member of the SimulationValue Variable.")
        ),
        ns0.datatypes.Argument(
            name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Desired content of the Qualifier struct member of the SimulationValue Variable.")
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7038", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6307"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6062",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Value", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Value used to set the Value member of the array element.")),
        ns0.datatypes.Argument(name="Qualifier", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Value used to set the Qualifier member of the array element.")),
        ns0.datatypes.Argument(
            name="Index", dataType=o6.Int16, valueRank=-1, description=o6.LocalizedText("Index of array element to set. If -1, the parameters are assigned to all array elements.")
        ),
    ],
)
o6.call(nodeId="ns=pnrio;i=7039", browseName="ns=pnrio;SetSimulationValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6062"]))


@o6.objecttype(nodeId="ns=pnrio;i=1015", browseName="ns=pnrio;RioPaDigitalChannelGroupType", displayName="RioPaDigitalChannelGroupType")
class RioPaDigitalChannelGroupType(RioChannelGroupType):
    inputImage: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6180", browseName="ns=pnrio;InputImage", dataType=pnrio_datypes.RioPaDigitalValueDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pnrio;i=4006",
    )
    outputImage: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnrio;i=6181", browseName="ns=pnrio;OutputImage", dataType=pnrio_datypes.RioPaDigitalValueDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pnrio;i=4006",
    )
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7006"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7039"])
    simulationEnabled: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6136", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0])
    )
    simulationValues: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pnrio;i=6061", browseName="ns=pnrio;SimulationValues", dataType=pnrio_datypes.RioPaDigitalValueDataType, valueRank=1, arrayDimensions=[0]
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6071",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ManualOutValue", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Desired Value of the ManualOutValue Variable."))],
)
o6.call(nodeId="ns=pnrio;i=7040", browseName="ns=pnrio;SetManualOutValue", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6071"]))


@o6.objecttype(nodeId="ns=pnrio;i=1010", browseName="ns=pnrio;RioPaDigitalOutputChannelType", displayName="RioPaDigitalOutputChannelType")
class RioPaDigitalOutputChannelType(RioChannelType):
    config: pnrio_vartypes.RioPaDigitalOutputConfigVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaDigitalOutputConfigVariableType(
            nodeId="ns=pnrio;i=6158",
            browseName="ns=pnrio;Config",
            dataType=pnrio_datypes.RioPaDigitalOutputConfigDataType,
            value=pnrio_datypes.RioPaDigitalOutputConfigDataType(
                signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
                wireCheckEnabled=False,
                inversionEnabled=False,
                substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
                substituteValue=False,
                substituteTime=0.0,
            ),
        )
    )
    manualOutValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6156", browseName="ns=pnrio;ManualOutValue", dataType=o6.Boolean)
    )
    mode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6154", browseName="ns=pnrio;Mode", dataType=pnrio_datypes.RioChannelModeEnumeration)
    )
    processValue: pnrio_vartypes.RioPaDigitalProcessValueVariableType = o6.hasComponent(
        pnrio_vartypes.RioPaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6150",
            browseName="ns=pnrio;ProcessValue",
            dataType=pnrio_datypes.RioPaDigitalProcessValueDataType,
            value=pnrio_datypes.RioPaDigitalProcessValueDataType(value=False, qualifier=0, quality=0, nE_107=0, status_full=0),
        )
    )
    processValueReadback: pnrio_vartypes.RioPaDigitalProcessValueVariableType | None = o6.hasComponent(
        pnrio_vartypes.RioPaDigitalProcessValueVariableType(
            nodeId="ns=pnrio;i=6151",
            browseName="ns=pnrio;ProcessValueReadback",
            dataType=pnrio_datypes.RioPaDigitalProcessValueDataType,
            value=pnrio_datypes.RioPaDigitalProcessValueDataType(value=False, qualifier=0, quality=0, nE_107=0, status_full=0),
        )
    )
    setManualOutValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7040"])
    setMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7036"])
    setSimulation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7037"])
    setSimulationValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnrio;i=7038"])
    signalValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6152", browseName="ns=pnrio;SignalValue", dataType=o6.Double))
    signalValueReadback: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6153", browseName="ns=pnrio;SignalValueReadback", dataType=o6.Double)
    )
    simulationEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6157", browseName="ns=pnrio;SimulationEnabled", dataType=o6.Boolean)
    )
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6155", browseName="ns=pnrio;SimulationValue", dataType=pnrio_datypes.RioPaDigitalValueDataType)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnrio_reftypes, pnrio_datypes, pnrio_vartypes
