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

"""Generated OPC UA pnem namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnem_reftypes
from . import datatypes as pnem_datypes
from . import vartypes as pnem_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=pnem;i=1004", browseName="ns=pnem;EnergySavingModesContainerType", displayName="EnergySavingModesContainerType")
class EnergySavingModesContainerType(ns0.objtypes.BaseObjectType):
    langleEnergySavingModesRangle: EnergySavingModeType


@o6.objecttype(nodeId="ns=pnem;i=1007", browseName="ns=pnem;IEnergyProfileE0Type", displayName="IEnergyProfileE0Type", isAbstract=True)
class IEnergyProfileE0Type(ns0.objtypes.BaseInterfaceType):
    acCurrent: pnem_vartypes.MeasurementValueType


@o6.objecttype(nodeId="ns=pnem;i=1008", browseName="ns=pnem;IEnergyProfileE1Type", displayName="IEnergyProfileE1Type", isAbstract=True)
class IEnergyProfileE1Type(ns0.objtypes.BaseInterfaceType):
    acActivePowerTotal: pnem_vartypes.MeasurementValueType


@o6.objecttype(nodeId="ns=pnem;i=1009", browseName="ns=pnem;IEnergyProfileE2Type", displayName="IEnergyProfileE2Type", isAbstract=True)
class IEnergyProfileE2Type(ns0.objtypes.BaseInterfaceType):
    acActiveEnergyTotalExportLp: pnem_vartypes.MeasurementValueType
    acActiveEnergyTotalImportLp: pnem_vartypes.MeasurementValueType
    acActivePowerTotal: pnem_vartypes.MeasurementValueType


@o6.objecttype(nodeId="ns=pnem;i=1010", browseName="ns=pnem;IEnergyProfileE3Type", displayName="IEnergyProfileE3Type", isAbstract=True)
class IEnergyProfileE3Type(ns0.objtypes.BaseInterfaceType):
    acActiveEnergyTotalExportHp: pnem_vartypes.MeasurementValueType
    acActiveEnergyTotalImportHp: pnem_vartypes.MeasurementValueType
    acActivePower: pnem_vartypes.MeasurementValueType
    acCurrent: pnem_vartypes.MeasurementValueType
    acPowerFactor: pnem_vartypes.MeasurementValueType
    acReactiveEnergyTotalExportHp: pnem_vartypes.MeasurementValueType
    acReactiveEnergyTotalImportHp: pnem_vartypes.MeasurementValueType
    acReactivePower: pnem_vartypes.MeasurementValueType
    acVoltagePe: pnem_vartypes.MeasurementValueType
    acVoltagePp: pnem_vartypes.MeasurementValueType


@o6.objecttype(nodeId="ns=pnem;i=1011", browseName="ns=pnem;IEnergyProfileD0Type", displayName="IEnergyProfileD0Type", isAbstract=True)
class IEnergyProfileD0Type(ns0.objtypes.BaseInterfaceType):
    dcCurrent: pnem_vartypes.MeasurementValueType


@o6.objecttype(nodeId="ns=pnem;i=1002", browseName="ns=pnem;EnergySavingModeStatusType", displayName="EnergySavingModeStatusType")
class EnergySavingModeStatusType(ns0.objtypes.BaseObjectType):
    currentTransitionData: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6023", browseName="ns=pnem;CurrentTransitionData", dataType=pnem_datypes.StandbyModeTransitionDataType)
    )
    stateInformation: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnem;i=6024",
            browseName="ns=pnem;StateInformation",
            dataType=pnem_datypes.EnergyStateInformationDataType,
            value=pnem_datypes.EnergyStateInformationDataType(iDSource=0, iDDestination=0, regularTimeToOperate=0.0, modePowerConsumption=0.0),
        )
    )


@o6.objecttype(nodeId="ns=pnem;i=1003", browseName="ns=pnem;EnergySavingModeType", displayName="EnergySavingModeType")
class EnergySavingModeType(ns0.objtypes.BaseObjectType):
    dynamicData: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6026", browseName="ns=pnem;DynamicData", dataType=o6.Boolean))
    energyConsumptionToOperate: ns0.vartypes.AnalogUnitType
    energyConsumptionToPause: ns0.vartypes.AnalogUnitType
    iD: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6025", browseName="ns=pnem;ID", dataType=o6.Byte))
    modePowerConsumption: ns0.vartypes.AnalogUnitType
    regularTimeToOperate: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6031", browseName="ns=pnem;RegularTimeToOperate", dataType=ns0.datatypes.Duration)
    )
    timeMaxLengthOfStay: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6030", browseName="ns=pnem;TimeMaxLengthOfStay", dataType=ns0.datatypes.Duration)
    )
    timeMinLengthOfStay: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6029", browseName="ns=pnem;TimeMinLengthOfStay", dataType=ns0.datatypes.Duration)
    )
    timeMinPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6027", browseName="ns=pnem;TimeMinPause", dataType=ns0.datatypes.Duration)
    )
    timeToPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6028", browseName="ns=pnem;TimeToPause", dataType=ns0.datatypes.Duration)
    )


@o6.objecttype(nodeId="ns=pnem;i=1013", browseName="ns=pnem;PeServiceAccessPointType", displayName="PeServiceAccessPointType")
class PeServiceAccessPointType(ns0.objtypes.BaseObjectType):
    peClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6112", browseName="ns=pnem;PeClass", dataType=pnem_datypes.PeClassEnumeration, accessLevel=3, userAccessLevel=1)
    )
    peSubclass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6113", browseName="ns=pnem;PeSubclass", dataType=pnem_datypes.PeSubclassEnumeration, accessLevel=3, userAccessLevel=1)
    )
    peVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6114", browseName="ns=pnem;PeVersion", dataType=pnem_datypes.PeVersionDataType, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PauseTime", dataType=ns0.datatypes.Duration, valueRank=-1, description=o6.LocalizedText("Requested pause time."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7005",
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
            name="TimeMinLengthToStay",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("Time of minimum stay in the destination energy saving mode if successful, otherwise unchanged."),
        ),
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("PROFIenergy return code. See Table 11.\n")),
    ],
)
o6.call(nodeId="ns=pnem;i=7005", browseName="ns=pnem;StartPause", inputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6050"]), outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6051"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6054",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7006",
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
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("PROFIenergy  return code. See table Table 11.\n")),
    ],
)
o6.call(nodeId="ns=pnem;i=7006", browseName="ns=pnem;EndPause", outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6054"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ModeID", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("ID of the requested energy saving mode."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7007",
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
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("Return code. See table Table 11.\n")),
    ],
)
o6.call(
    nodeId="ns=pnem;i=7007", browseName="ns=pnem;SwitchToEnergySavingMode", inputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6052"]), outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6053"])
)


@o6.objecttype(nodeId="ns=pnem;i=1005", browseName="ns=pnem;EnergyStandbyManagementType", displayName="EnergyStandbyManagementType")
class EnergyStandbyManagementType(ns0.objtypes.BaseObjectType):
    endPause: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnem;i=7006"])
    energySavingModeStatus: EnergySavingModeStatusType
    energySavingModes: EnergySavingModesContainerType | None = o6.hasComponent(EnergySavingModesContainerType(nodeId="ns=pnem;i=5018", browseName="ns=pnem;EnergySavingModes"))
    lock: di.objtypes.LockingServicesType | None
    pauseTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6040", browseName="ns=pnem;PauseTime", dataType=ns0.datatypes.Duration)
    )
    standbyManagementStatus: ns0.vartypes.MultiStateDiscreteType
    startPause: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnem;i=7005"])
    switchToEnergySavingMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnem;i=7007"])


@o6.objecttype(nodeId="ns=pnem;i=1006", browseName="ns=pnem;EnergyMeasurementType", displayName="EnergyMeasurementType")
class EnergyMeasurementType(ns0.objtypes.BaseObjectType):
    langleMeasurementValueRangle: pnem_vartypes.MeasurementValueType
    peObjectNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6055", browseName="ns=pnem;PeObjectNumber", dataType=o6.UInt16))
    resetEnergyCounter: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=pnem;i=7008", browseName="ns=pnem;ResetEnergyCounter"))


ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6110",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7009",
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
        ns0.datatypes.Argument(name="ReturnCode", dataType=o6.Byte, valueRank=-1, description=o6.LocalizedText("PROFIenergy  return code. See Table 11.\n")),
    ],
)
o6.call(nodeId="ns=pnem;i=7009", browseName="ns=pnem;SwitchOffWOL", outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6110"]))


@o6.objecttype(nodeId="ns=pnem;i=1012", browseName="ns=pnem;EnergyDevicePowerOffType", displayName="EnergyDevicePowerOffType")
class EnergyDevicePowerOffType(ns0.objtypes.BaseObjectType):
    modePowerConsumption: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6108", browseName="ns=pnem;ModePowerConsumption", dataType=o6.UInt32)
    )
    regularTimeToOperate: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6106", browseName="ns=pnem;RegularTimeToOperate", dataType=ns0.datatypes.Duration)
    )
    switchOffWOL: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=pnem;i=7009"])
    timeMinPause: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6107", browseName="ns=pnem;TimeMinPause", dataType=ns0.datatypes.Duration)
    )
    wOLMagicPacket: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6109", browseName="ns=pnem;WOLMagicPacket", dataType=o6.ByteString))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnem_reftypes, pnem_datypes, pnem_vartypes
