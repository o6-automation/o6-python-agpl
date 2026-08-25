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

"""Generated OPC UA plastics_lds namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_lds_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1002", browseName="ns=plastics_lds;AdditiveAlarmType", displayName="AdditiveAlarmType", description="Represent additive-related text messages"
)
class AdditiveAlarmType(plastics_rubber.objtypes.HelpOffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1003", browseName="ns=plastics_lds;ComponentAlarmType", displayName="ComponentAlarmType", description="Represent component-related text messages"
)
class ComponentAlarmType(plastics_rubber.objtypes.HelpOffNormalAlarmType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6072",
    browseName="ns=plastics_lds;ActivateMaterialBalanceSystem",
    description="If the value is true, the material balance system is activated",
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=plastics_lds;i=6081",
    browseName="ns=plastics_lds;RemainingMaterialTime",
    description="Remaining time until first material is empty",
    dataType=ns0.datatypes.Duration,
    value=0.0,
)


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1007",
    browseName="ns=plastics_lds;LDS_InterfaceType",
    displayName="LDS_InterfaceType",
    description="Root ObjectType representing a LSR dosing system with its subcomponents",
)
class LDS_InterfaceType(ns0.objtypes.BaseObjectType):
    deviceEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6206",
            browseName="ns=plastics_lds;DeviceEnabled",
            description="This variable is used to release the drives of the dosing system. If the value is FALSE, the LDS shall not be able to start ist drives.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    displayLanguage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6205",
            browseName="ns=plastics_lds;DisplayLanguage",
            description="With this Property the client can set the desired language on the user interface at the LDS",
            dataType=ns0.datatypes.LocaleId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identification: plastics_rubber.objtypes.IdentificationType
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    operation: OperationType


o6.reference(LDS_InterfaceType, "i=41", "ns=plastics_rubber;i=1052")


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1008",
    browseName="ns=plastics_lds;LDSCycleParametersEventType",
    displayName="LDSCycleParametersEventType",
    description="Information on a dosing cycle",
    isAbstract=True,
)
class LDSCycleParametersEventType(ns0.objtypes.BaseEventType):
    additivesPressure: ns0.vartypes.AnalogItemType | None
    additivesRatioActual: ns0.vartypes.AnalogItemType | None
    additivesRatioTarget: ns0.vartypes.AnalogItemType | None
    cycleNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_lds;i=6450", browseName="ns=plastics_lds;CycleNumber", description="Number of the dosing cycle", dataType=o6.UInt64)
    )
    dosingTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6451", browseName="ns=plastics_lds;DosingTime", description="Duration of the dosing cycle", dataType=ns0.datatypes.Duration
        )
    )
    filterPressurePrimary: ns0.vartypes.AnalogItemType | None
    filterPressureSecondary: ns0.vartypes.AnalogItemType | None
    mixingPointPressureA: ns0.vartypes.AnalogItemType | None
    mixingPointPressureB: ns0.vartypes.AnalogItemType | None
    mixingPointPressureBlender: ns0.vartypes.AnalogItemType | None
    mixingRatioActual: ns0.vartypes.AnalogItemType | None
    mixingRatioTarget: ns0.vartypes.AnalogItemType | None
    residualAmountA: ns0.vartypes.AnalogItemType | None
    residualAmountB: ns0.vartypes.AnalogItemType | None
    volumeA: ns0.vartypes.AnalogItemType | None
    volumeAB: ns0.vartypes.AnalogItemType | None
    volumeAdditives: ns0.vartypes.AnalogItemType | None
    volumeB: ns0.vartypes.AnalogItemType | None
    volumeTotal: ns0.vartypes.AnalogItemType | None


o6.reference(o6.ns["ns=plastics_lds;i=6072"], "i=41", LDSCycleParametersEventType)
o6.reference(o6.ns["ns=plastics_lds;i=6081"], "i=41", LDSCycleParametersEventType)


@o6.objecttype(nodeId="ns=plastics_lds;i=1004", browseName="ns=plastics_lds;AdditiveType", displayName="AdditiveType", description="Information about used additives")
class AdditiveType(ns0.objtypes.BaseObjectType):
    activateAdditive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6008",
            browseName="ns=plastics_lds;ActivateAdditive",
            description="Set value to activate the additive",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    activateClosedLoopControl: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6042",
            browseName="ns=plastics_lds;ActivateClosedLoopControl",
            description="Activate the closed loop control of the additive",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    additiveActivated: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6009", browseName="ns=plastics_lds;AdditiveActivated", description="Is true if the additive is activated.", dataType=o6.Boolean, value=False
        )
    )
    additiveFraction: plastics_rubber.objtypes.ControlledParameterType | None
    additiveStrokeVolume: plastics_rubber.objtypes.ControlledParameterType | None
    closedLoopControlActivated: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6449",
            browseName="ns=plastics_lds;ClosedLoopControlActivated",
            description="Is true if the closed loop control of the additive is activated",
            dataType=o6.Boolean,
        )
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6636", browseName="ns=plastics_lds;IsPresent", description="Informs the client if the additive is physically present.", dataType=o6.Boolean
        )
    )
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6010",
            browseName="ns=plastics_lds;Status",
            description="Actual status of the additive provides a minimal error handling for devices without event support.",
            dataType=plastics_lds_datypes.AdditiveStatusEnumeration,
            value=plastics_lds_datypes.AdditiveStatusEnumeration.GOOD,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6039",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CycleNumber", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7006",
    browseName="ns=plastics_lds;SetCycleNumber",
    description="Method to set the cycle number of the LDS to synchronize it with the cycle number of the injection moulding machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6039"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6059",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7010",
    browseName="ns=plastics_lds;ResetErrorById",
    description="Method to reset one error of the device",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6059"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_lds;i=6448",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_lds;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_lds;i=7020",
    browseName="ns=plastics_lds;SetSetValueDensity",
    description="This optional method is used to modify SetValueDensity if allowed by the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_lds;i=6448"]),
)


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1005", browseName="ns=plastics_lds;ComponentType", displayName="ComponentType", description="Information about the mixing components A and B"
)
class ComponentType(ns0.objtypes.BaseObjectType):
    actualFollowerPlatePressure: ns0.vartypes.AnalogItemType | None
    actualPressure: ns0.vartypes.AnalogItemType | None
    allowsCycles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6049",
            browseName="ns=plastics_lds;AllowsCycles",
            description="Expected number of remaining cycles with the current drum",
            dataType=o6.Double,
            value=0.0,
        )
    )
    drumCapacity: ns0.vartypes.AnalogItemType | None
    remainingMaterialTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_lds;i=6048",
            browseName="ns=plastics_lds;RemainingMaterialTime",
            description="Time until the material of the component is empty",
            dataType=ns0.datatypes.Duration,
            value=0.0,
        )
    )
    residualAmount: ns0.vartypes.AnalogItemType | None
    setFollowerPlatePressure: ns0.vartypes.AnalogItemType | None
    setSetValueDensity: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_lds;i=7020"])
    setValueDensity: ns0.vartypes.AnalogItemType | None
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6050",
            browseName="ns=plastics_lds;Status",
            description="Actual status of the component provides a minimal error handling for devices without event support.",
            dataType=plastics_lds_datypes.ComponentStatusEnumeration,
            value=plastics_lds_datypes.ComponentStatusEnumeration.GOOD,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_lds;i=1006",
    browseName="ns=plastics_lds;OperationType",
    displayName="OperationType",
    description="This ObjectType contains components which are necessary to operate the LDS.",
)
class OperationType(ns0.objtypes.BaseObjectType):
    activateMaterialBalanceSystem: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=plastics_lds;i=6072"])
    activateRemoteControl: ns0.vartypes.MultiStateValueDiscreteType
    activeErrors: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_lds;i=6506",
            browseName="ns=plastics_lds;ActiveErrors",
            description="List of the active errors of the device",
            dataType=plastics_rubber.datatypes.ClassifiedActiveErrorDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    actualDeviationMixingRatio: ns0.vartypes.AnalogItemType | None
    actualShotWeight: ns0.vartypes.AnalogItemType | None
    additive_LangleYRangle: AdditiveType | None
    component_A: ComponentType
    component_B: ComponentType
    deliveryFlowrate: plastics_rubber.objtypes.ControlledParameterType | None
    deliveryPressure: plastics_rubber.objtypes.ControlledParameterType | None
    deliveryPressureMeasuringPoint: ns0.vartypes.MultiStateValueDiscreteType | None
    deliveryType: ns0.vartypes.MultiStateValueDiscreteType
    deviceMappingNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6058",
            browseName="ns=plastics_lds;DeviceMappingNumber",
            description="Unique identifier/address/number for devices of the same DeviceType within a local network",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dosingActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_lds;i=6052", browseName="ns=plastics_lds;DosingActive", dataType=o6.Boolean)
    )
    highestActiveAlarmSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6057",
            browseName="ns=plastics_lds;HighestActiveAlarmSeverity",
            description="Indication of the severity of the highest active alarm",
            dataType=o6.UInt16,
        )
    )
    identifyDevice: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_lds;i=7002",
            browseName="ns=plastics_lds;IdentifyDevice",
            description="The peripheral device on which this method is called shows itself by e.g. activation of a LED.",
        )
    )
    materialBalanceSystemType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6061",
            browseName="ns=plastics_lds;MaterialBalanceSystemType",
            description="Type of the material balance system",
            dataType=plastics_lds_datypes.MaterialBalanceSystemTypeEnumeration,
            value=plastics_lds_datypes.MaterialBalanceSystemTypeEnumeration.NOT_AVAILABLE,
        )
    )
    maxDeviationMixingRatio: ns0.vartypes.AnalogItemType | None
    mixingRatioTarget: ns0.vartypes.AnalogItemType | None
    purgeCyclicActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_lds;i=6201",
            browseName="ns=plastics_lds;PurgeCyclicActive",
            description="Difference between purging (true) and waiting (false)",
            dataType=o6.Boolean,
        )
    )
    purgeCyclicIdleTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_lds;i=6200",
            browseName="ns=plastics_lds;PurgeCyclicIdleTime",
            description="Time until the next purge cycle starts",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    purgeCyclicQuantity: ns0.vartypes.AnalogItemType | None
    purgeMode: ns0.vartypes.MultiStateValueDiscreteType | None
    purgeQuantity: ns0.vartypes.AnalogItemType | None
    purgeStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_lds;i=6361",
            browseName="ns=plastics_lds;PurgeStatus",
            description="Actual status of the purge function",
            dataType=plastics_lds_datypes.PurgeStatusEnumeration,
        )
    )
    purgeTimeout: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_lds;i=6192",
            browseName="ns=plastics_lds;PurgeTimeout",
            description="Maximum time of the active PurgeMode",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    remainingMaterialTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=plastics_lds;i=6081"])
    remoteControlActivated: ns0.vartypes.MultiStateValueDiscreteType
    resetAllErrors: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_lds;i=7003", browseName="ns=plastics_lds;ResetAllErrors", description="Method to reset all errors of the device")
    )
    resetErrorById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_lds;i=7010"])
    setCycleNumber: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_lds;i=7006"])
    setShotWeight: ns0.vartypes.AnalogItemType | None
    setValueCompositeDensity: ns0.vartypes.AnalogItemType | None
    startDosing: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_lds;i=7021",
            browseName="ns=plastics_lds;StartDosing",
            description="If RemoteControlActivated = 2, this Method (without arguments) is used to start the dosing",
        )
    )
    stopDosing: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_lds;i=7028", browseName="ns=plastics_lds;StopDosing"))
    targetDeviationMixingRatio: ns0.vartypes.AnalogItemType | None


o6.reference(OperationType, "i=41", LDSCycleParametersEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_lds_datypes
