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

"""Generated OPC UA ecm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import datatypes as ecm_datypes
from . import vartypes as ecm_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=ecm;i=1004", browseName="ns=ecm;EnergySavingModesContainerType", displayName="EnergySavingModesContainerType")
class EnergySavingModesContainerType(ns0.objtypes.BaseObjectType):
    langleEnergySavingModesRangle: EnergySavingModeType


@o6.objecttype(nodeId="ns=ecm;i=1007", browseName="ns=ecm;IEnergyProfileE0Type", displayName="IEnergyProfileE0Type", isAbstract=True)
class IEnergyProfileE0Type(ns0.objtypes.BaseInterfaceType):
    acCurrentPe: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1008", browseName="ns=ecm;IEnergyProfileE1Type", displayName="IEnergyProfileE1Type", isAbstract=True)
class IEnergyProfileE1Type(ns0.objtypes.BaseInterfaceType):
    acActivePowerTotal: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1009", browseName="ns=ecm;IEnergyProfileE2Type", displayName="IEnergyProfileE2Type", isAbstract=True)
class IEnergyProfileE2Type(ns0.objtypes.BaseInterfaceType):
    acActiveEnergyTotalExportLp: ecm_vartypes.EnergyMeasurementValueType
    acActiveEnergyTotalImportLp: ecm_vartypes.EnergyMeasurementValueType
    acActivePowerTotal: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1010", browseName="ns=ecm;IEnergyProfileE3Type", displayName="IEnergyProfileE3Type", isAbstract=True)
class IEnergyProfileE3Type(ns0.objtypes.BaseInterfaceType):
    acActiveEnergyTotalExportHp: ecm_vartypes.EnergyMeasurementValueType
    acActiveEnergyTotalImportHp: ecm_vartypes.EnergyMeasurementValueType
    acActivePowerPe: ecm_vartypes.EnergyMeasurementValueType
    acCurrentPe: ecm_vartypes.EnergyMeasurementValueType
    acPowerFactorPe: ecm_vartypes.EnergyMeasurementValueType
    acReactiveEnergyTotalExportHp: ecm_vartypes.EnergyMeasurementValueType
    acReactiveEnergyTotalImportHp: ecm_vartypes.EnergyMeasurementValueType
    acReactivePowerPe: ecm_vartypes.EnergyMeasurementValueType
    acVoltagePe: ecm_vartypes.EnergyMeasurementValueType
    acVoltagePp: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1011", browseName="ns=ecm;IEnergyProfileD0Type", displayName="IEnergyProfileD0Type", isAbstract=True)
class IEnergyProfileD0Type(ns0.objtypes.BaseInterfaceType):
    dcCurrent: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1015", browseName="ns=ecm;IEnergyProfileD1Type", displayName="IEnergyProfileD1Type", isAbstract=True)
class IEnergyProfileD1Type(ns0.objtypes.BaseInterfaceType):
    dcActivePower: ecm_vartypes.EnergyMeasurementValueType
    dcCurrent: ecm_vartypes.EnergyMeasurementValueType
    dcElectricalCharge: ecm_vartypes.EnergyMeasurementValueType
    dcEnergyTotalExportLp: ecm_vartypes.EnergyMeasurementValueType
    dcEnergyTotalImportLp: ecm_vartypes.EnergyMeasurementValueType
    dcRelativeCharge: ecm_vartypes.EnergyMeasurementValueType
    dcVoltage: ecm_vartypes.EnergyMeasurementValueType


@o6.objecttype(nodeId="ns=ecm;i=1002", browseName="ns=ecm;EnergySavingModeStatusType", displayName="EnergySavingModeStatusType")
class EnergySavingModeStatusType(ns0.objtypes.BaseObjectType):
    currentTransitionData: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6023", browseName="ns=ecm;CurrentTransitionData", dataType=ecm_datypes.StandbyModeTransitionDataType)
    )
    stateInformation: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ecm;i=6024",
            browseName="ns=ecm;StateInformation",
            dataType=ecm_datypes.EnergyStateInformationDataType,
            value=ecm_datypes.EnergyStateInformationDataType(iDSource=0, iDDestination=0, regularTimeToOperate=0.0, modePowerConsumption=0.0),
        )
    )


@o6.objecttype(nodeId="ns=ecm;i=1003", browseName="ns=ecm;EnergySavingModeType", displayName="EnergySavingModeType")
class EnergySavingModeType(ns0.objtypes.BaseObjectType):
    dynamicData: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6026", browseName="ns=ecm;DynamicData", dataType=o6.Boolean))
    energyConsumptionToOperate: ns0.vartypes.AnalogUnitType
    energyConsumptionToPause: ns0.vartypes.AnalogUnitType
    iD: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6025", browseName="ns=ecm;ID", dataType=o6.Byte))
    modePowerConsumption: ns0.vartypes.AnalogUnitType
    regularTimeToOperate: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6031", browseName="ns=ecm;RegularTimeToOperate", dataType=ns0.datatypes.Duration)
    )
    timeMaxLengthOfStay: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6030", browseName="ns=ecm;TimeMaxLengthOfStay", dataType=ns0.datatypes.Duration)
    )
    timeMinLengthOfStay: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6029", browseName="ns=ecm;TimeMinLengthOfStay", dataType=ns0.datatypes.Duration)
    )
    timeMinPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6027", browseName="ns=ecm;TimeMinPause", dataType=ns0.datatypes.Duration)
    )
    timeToPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6028", browseName="ns=ecm;TimeToPause", dataType=ns0.datatypes.Duration)
    )


@o6.objecttype(nodeId="ns=ecm;i=1014", browseName="ns=ecm;AccuracyDomainType", displayName="AccuracyDomainType")
class AccuracyDomainType(ns0.objtypes.BaseObjectType):
    enumValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ecm;i=6201", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PauseTime", dataType=ns0.datatypes.Duration, valueRank=-1, description=o6.LocalizedText("Requested pause time."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="ModeID", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("ID of the destination energy saving mode if successful, otherwise unchanged.")
        ),
        ns0.datatypes.Argument(
            name="CurrentTimeToDestination",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time needed to reach the energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(
            name="RegularTimeToOperate",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText(
                "Time needed to reach PE_ready_to_operate again if the destination energy saving mode will be regularly terminated if successful, otherwise unchanged."
            ),
        ),
        ns0.datatypes.Argument(
            name="TimeMinLengthOfStay",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time of minimum stay in the destination energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Return code.")),
    ],
)
o6.call(nodeId="ns=ecm;i=7005", browseName="ns=ecm;StartPause", inputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6050"]), outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6051"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6054",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="CurrentTimeToOperate",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time needed to reach PE_ready_to_operate if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Return code.")),
    ],
)
o6.call(nodeId="ns=ecm;i=7006", browseName="ns=ecm;EndPause", outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6054"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ModeID", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("ID of the requested energy saving mode."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="EffectiveModeID",
            dataType=o6.Byte,
            valueRank=-1,
            description=o6.LocalizedText("ID of the effectively chosen destination energy saving mode if successful, otherwise current mode."),
        ),
        ns0.datatypes.Argument(
            name="CurrentTimeToDestination",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time needed to reach the destination energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(
            name="RegularTimeToOperate",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText(
                "Time needed to reach PE_ready_to_operate again if the destination energy saving mode will be regularly terminated if successful, otherwise unchanged."
            ),
        ),
        ns0.datatypes.Argument(
            name="TimeMinLengthOfStay",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time of minimum stay in the destination energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Return code.")),
    ],
)
o6.call(nodeId="ns=ecm;i=7007", browseName="ns=ecm;SwitchToEnergySavingMode", inputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6052"]), outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6053"]))


@o6.objecttype(nodeId="ns=ecm;i=1005", browseName="ns=ecm;EnergyStandbyManagementType", displayName="EnergyStandbyManagementType")
class EnergyStandbyManagementType(ns0.objtypes.BaseObjectType):
    endPause: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ecm;i=7006"])
    energySavingModeStatus: EnergySavingModeStatusType
    energySavingModes: EnergySavingModesContainerType | None
    lock: di.objtypes.LockingServicesType | None
    pauseTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6040", browseName="ns=ecm;PauseTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    standbyManagementStatus: ns0.vartypes.MultiStateDiscreteType
    startPause: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ecm;i=7005"])
    switchToEnergySavingMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ecm;i=7007"])


@o6.objecttype(nodeId="ns=ecm;i=1006", browseName="ns=ecm;EnergyMeasurementType", displayName="EnergyMeasurementType", interfaces=[ia.objtypes.IStatisticsType])
class EnergyMeasurementType(ns0.objtypes.BaseObjectType):
    applicationTag: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6055", browseName="ns=ecm;ApplicationTag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    langleMeasurementValueRangle: ecm_vartypes.EnergyMeasurementValueType
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=ecm;i=7008", browseName="ns=ia;ResetStatistics"))
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6009", browseName="ns=ia;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=ecm;i=6110",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ecm;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="ModeID", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("ID of the destination energy saving mode (0xFE)  if successful, otherwise unchanged.")
        ),
        ns0.datatypes.Argument(
            name="CurrentTimeToDestination",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time needed to reach the energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(
            name="RegularTimeToOperate",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText(
                "Time needed to reach PE_ready_to_operate again if the destination energy saving mode will be regularly terminated if successful, otherwise unchanged."
            ),
        ),
        ns0.datatypes.Argument(
            name="TimeMinLengthOfStay",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time of minimum stay in the destination energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Return code.")),
    ],
)
o6.call(nodeId="ns=ecm;i=7009", browseName="ns=ecm;SwitchOffWOL", outputArgs=o6.hasProperty(o6.ns["ns=ecm;i=6110"]))


@o6.objecttype(nodeId="ns=ecm;i=1012", browseName="ns=ecm;EnergyDevicePowerOffType", displayName="EnergyDevicePowerOffType")
class EnergyDevicePowerOffType(ns0.objtypes.BaseObjectType):
    modePowerConsumption: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6108", browseName="ns=ecm;ModePowerConsumption", dataType=o6.UInt32)
    )
    regularTimeToOperate: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6106", browseName="ns=ecm;RegularTimeToOperate", dataType=ns0.datatypes.Duration)
    )
    switchOffWOL: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=ecm;i=7009"])
    timeMinPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ecm;i=6107", browseName="ns=ecm;TimeMinPause", dataType=ns0.datatypes.Duration)
    )
    wOLMagicPacket: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6109", browseName="ns=ecm;WOLMagicPacket", dataType=o6.ByteString))


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, ecm_datypes, ecm_vartypes
