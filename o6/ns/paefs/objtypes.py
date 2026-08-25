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

"""Generated OPC UA paefs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import reftypes as paefs_reftypes
from . import datatypes as paefs_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=paefs;i=1011",
    browseName="ns=paefs;ConsumptionType",
    displayName="ConsumptionType",
    description="The ConsumtionType contains information related to the consumption of a device.",
)
class ConsumptionType(ns0.objtypes.BaseObjectType):
    currentConsumption: SensorMonitoringType | None
    lifetimeConsumption: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=paefs;i=1019", browseName="ns=paefs;IonizerType", displayName="IonizerType", description="Unit for ionizing particles in a process air stream.")
class IonizerType(ns0.objtypes.BaseObjectType):
    ionizerOutput: SensorMonitoringType


@o6.objecttype(nodeId="ns=paefs;i=1020", browseName="ns=paefs;CollectorType", displayName="CollectorType", description="Unit for separating particles from a process air stream.")
class CollectorType(ns0.objtypes.BaseObjectType):
    collectorOutput: SensorMonitoringType


@o6.objecttype(
    nodeId="ns=paefs;i=1025",
    browseName="ns=paefs;MalfunctionAlarmType",
    displayName="MalfunctionAlarmType",
    description="Sent when the component has an error that may prevent it from operating",
)
class MalfunctionAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1026",
    browseName="ns=paefs;EndOfFilterRollAlarmType",
    displayName="EndOfFilterRollAlarmType",
    description="Triggered when the automatic roll filter reaches the end of the filter roll",
)
class EndOfFilterRollAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1029",
    browseName="ns=paefs;WashingAgentInflowMalfunctionAlarmType",
    displayName="WashingAgentInflowMalfunctionAlarmType",
    description="The WashingAgentInflowMalfunctionAlarmType event is triggered when an error occurs on the washing agent inflow",
)
class WashingAgentInflowMalfunctionAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1030",
    browseName="ns=paefs;WashingAgentDrainMalfunctionAlarmType",
    displayName="WashingAgentDrainMalfunctionAlarmType",
    description="The WashingAgentDrainMalfunctionAlarmType is triggered when an error occurs on the washing agent drain",
)
class WashingAgentDrainMalfunctionAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1032",
    browseName="ns=paefs;CompressedAirSupplyInterruptedAlarmType",
    displayName="CompressedAirSupplyInterruptedAlarmType",
    description="Triggered when the compressed air supply is interrupted",
)
class CompressedAirSupplyInterruptedAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1041",
    browseName="ns=paefs;SafetySystemTriggeredAlarmType",
    displayName="SafetySystemTriggeredAlarmType",
    description="Is sent when the safety system is triggered",
)
class SafetySystemTriggeredAlarmType(ns0.objtypes.OffNormalAlarmType):
    pass


ns0.objtypes.FolderType(nodeId="ns=paefs;i=5105", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5107", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5108", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5109", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5110", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5111", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5112", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5113", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5114", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=paefs;i=5115", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(
    nodeId="ns=paefs;i=1010",
    browseName="ns=paefs;SensorMonitoringType",
    displayName="SensorMonitoringType",
    description="Represents a process value whose value is determined by a measuring device",
)
class SensorMonitoringType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5105"])
    signal: machinery_processvalues.objtypes.ProcessValueType
    signalForm: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6007",
            browseName="ns=paefs;SignalForm",
            description="Specifies whether the sensor is an analog or a digital sensor.",
            dataType=paefs_datypes.AnalogDigitalEnum,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1039",
    browseName="ns=paefs;MaintenanceSwitchConditionType",
    displayName="MaintenanceSwitchConditionType",
    description="Is sent when the physical maintenance switch is toggled",
)
class MaintenanceSwitchConditionType(ns0.objtypes.ConditionType):
    switchOn: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6046",
            browseName="ns=paefs;SwitchOn",
            description="Reflects the value of the MaintenanceRequested property of the object from which the event originates at the time the event was sent",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1023",
    browseName="ns=paefs;MaintenanceRequestedConditionType",
    displayName="MaintenanceRequestedConditionType",
    description="Is sent when the manufacturer wants to inform the operator that the system requires maintenance",
)
class MaintenanceRequestedConditionType(ns0.objtypes.AcknowledgeableConditionType):
    requested: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6047",
            browseName="ns=paefs;Requested",
            description="Reflects the value of the MaintenanceRequested property of the object from which the event originates at the time the event was sent",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1037",
    browseName="ns=paefs;CleaningRecommendedConditionType",
    displayName="CleaningRecommendedConditionType",
    description="Triggered by the cleaning unit when cleaning of the separator is necessary",
)
class CleaningRecommendedConditionType(ns0.objtypes.AcknowledgeableConditionType):
    recommended: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6048",
            browseName="ns=paefs;Recommended",
            description="Reflects the value of the property CleaningRequested of the CleaningUnitType",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1031",
    browseName="ns=paefs;HighVoltageUnitSupplyActiveEventType",
    displayName="HighVoltageUnitSupplyActiveEventType",
    description="Triggered when the high voltage unit supply is activated or deactivated",
    isAbstract=True,
)
class HighVoltageUnitSupplyActiveEventType(ns0.objtypes.BaseEventType):
    active: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6049",
            browseName="ns=paefs;Active",
            description="Reflects the value of the SupplyActive property of the HighVoltageUnitType at the time the event was triggered",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1024",
    browseName="ns=paefs;ContainerOpenConditionType",
    displayName="ContainerOpenConditionType",
    description="Triggered when the filter aid reservoir is opened or closed",
)
class ContainerOpenConditionType(ns0.objtypes.ConditionType):
    open: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6050",
            browseName="ns=paefs;Open",
            description="Reflects the value of the ContainerOpen property of the FilterAidDeviceType at the time the condition was triggered",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1003",
    browseName="ns=paefs;SeparatorType",
    displayName="SeparatorType",
    description="This is the abstract base type for separators. It contains optional sensor values that are\ncommon to all separators. Users may use one of the subtypes provided within this\nspecification or create their own type.",
    isAbstract=True,
)
class SeparatorType(ns0.objtypes.BaseObjectType):
    filterMediumOperatingHours: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6081",
            browseName="ns=paefs;FilterMediumOperatingHours",
            description="The number of hours that the unit has been in operation since the last filter change.",
            dataType=o6.UInt32,
        )
    )
    filterMediumState: SensorMonitoringType | None
    humidity: SensorMonitoringType | None
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5113"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    temperature: SensorMonitoringType | None


@o6.objecttype(nodeId="ns=paefs;i=1013", browseName="ns=paefs;CartridgeFilterType", displayName="CartridgeFilterType", description="A basic mechanical separator.")
class CartridgeFilterType(SeparatorType):
    pass


@o6.objecttype(
    nodeId="ns=paefs;i=1014",
    browseName="ns=paefs;WetSeparatorType",
    displayName="WetSeparatorType",
    description="Separator that filters solid, liquid, or gaseous components using a liquid medium.",
)
class WetSeparatorType(SeparatorType):
    washingAgentDrainMalfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6062",
            browseName="ns=paefs;WashingAgentDrainMalfunction",
            description="Indicates whether there is an error with the washing agent drain. True in case of error. Examples: clogging, burst pipe, defective valve.",
            dataType=o6.Boolean,
        )
    )
    washingAgentDrainOpen: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6061", browseName="ns=paefs;WashingAgentDrainOpen", description="Indicates that the washing agent drain valve is open.", dataType=o6.Boolean
        )
    )
    washingAgentInflowMalfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6060",
            browseName="ns=paefs;WashingAgentInflowMalfunction",
            description="Indicates whether there is an error with the washing agent inflow. True in case of error. Examples: clogging, burst pipe, defective valve.",
            dataType=o6.Boolean,
        )
    )
    washingAgentInflowOpen: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6059", browseName="ns=paefs;WashingAgentInflowOpen", description="Indicates that the washing agent inflow valve is open.", dataType=o6.Boolean
        )
    )


o6.reference(WetSeparatorType, "i=41", WashingAgentInflowMalfunctionAlarmType)
o6.reference(WetSeparatorType, "i=41", WashingAgentDrainMalfunctionAlarmType)


@o6.objecttype(
    nodeId="ns=paefs;i=1015",
    browseName="ns=paefs;HighVoltageUnitType",
    displayName="HighVoltageUnitType",
    description="Unit to produce high voltage to supply to ionizers and collectors.",
    interfaces=[di.objtypes.IOperationCounterType],
)
class HighVoltageUnitType(ns0.objtypes.BaseObjectType):
    currentOutput: ns0.vartypes.AnalogUnitRangeType | None
    langleCollectorRangle: CollectorType | None
    langleIonizerRangle: IonizerType | None
    maintenanceRequested: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6093",
            browseName="ns=paefs;MaintenanceRequested",
            description="Indicates that maintenance is requested for the high voltage generator.",
            dataType=o6.Boolean,
        )
    )
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6091",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the high voltage generator is malfunctioning (e.g., excess/insufficient voltage, overheating, etc). True in case of error.",
            dataType=o6.Boolean,
        )
    )
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6098", browseName="ns=paefs;OperationCycleCounter", dataType=ns0.datatypes.UInteger)
    )
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6092", browseName="ns=paefs;OperationDuration", dataType=ns0.datatypes.Duration)
    )
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6039", browseName="ns=paefs;PowerOnDuration", dataType=ns0.datatypes.Duration)
    )
    supplyActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6087", browseName="ns=paefs;SupplyActive", description="Indicates that the high-voltage generator is emitting high voltage.", dataType=o6.Boolean
        )
    )


o6.reference(HighVoltageUnitType, "i=41", MaintenanceRequestedConditionType)
o6.reference(HighVoltageUnitType, "i=41", MalfunctionAlarmType)
o6.reference(HighVoltageUnitType, "i=41", HighVoltageUnitSupplyActiveEventType)


@o6.objecttype(
    nodeId="ns=paefs;i=1018",
    browseName="ns=paefs;ElectrostaticPrecipitatorType",
    displayName="ElectrostaticPrecipitatorType",
    description="Separator that uses electrostatics to filter solid or liquid components from the process air.",
)
class ElectrostaticPrecipitatorType(SeparatorType):
    langleHighVoltageUnitRangle: HighVoltageUnitType = o6.hasComponent(
        HighVoltageUnitType(
            nodeId="ns=paefs;i=5010", browseName="ns=paefs;<HighVoltageUnit>", description="The precipitator’s high voltage units.", modellingRule="MandatoryPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=paefs;i=1034",
    browseName="ns=paefs;SensorSetpointReadType",
    displayName="SensorSetpointReadType",
    description="This type represents a process value and provides a setpoint for this value. This type provides only read-access to the sepoint.",
)
class SensorSetpointReadType(SensorMonitoringType):
    isActiveSetpoint: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6176", browseName="ns=paefs;IsActiveSetpoint", description="Indicates that the setpoint is currently active.", dataType=o6.Boolean
        )
    )
    signal: machinery_processvalues.objtypes.ProcessValueType


@o6.objecttype(
    nodeId="ns=paefs;i=1035",
    browseName="ns=paefs;SensorSetpointWriteType",
    displayName="SensorSetpointWriteType",
    description="This type represents a process value and provides a readable and writable setpoint for this value",
)
class SensorSetpointWriteType(SensorSetpointReadType):
    signal: machinery_processvalues.objtypes.ProcessValueType


@o6.objecttype(
    nodeId="ns=paefs;i=1017",
    browseName="ns=paefs;TemperatureRegulatorType",
    displayName="TemperatureRegulatorType",
    description="Device for regulating the temperature of the process gas.",
)
class TemperatureRegulatorType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5110"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6233",
            browseName="ns=paefs;Malfunction",
            description="Indicates whether there is an error with the temperature regulator. True in case of error.",
            dataType=o6.Boolean,
        )
    )
    powerConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(
            nodeId="ns=paefs;i=5054", browseName="ns=paefs;PowerConsumption", description="Contains information regarding the energy consumption of the temperature regulator."
        )
    )
    temperature: SensorSetpointWriteType | None


o6.reference(TemperatureRegulatorType, "i=41", MalfunctionAlarmType)


@o6.objecttype(
    nodeId="ns=paefs;i=1021",
    browseName="ns=paefs;AutomaticRollFilterType",
    displayName="AutomaticRollFilterType",
    description="A separator that is regenerated by rolling up the filter medium.",
)
class AutomaticRollFilterType(SeparatorType):
    endOfFilterRoll: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6389", browseName="ns=paefs;EndOfFilterRoll", description="EndOfFilterRoll is true if the end of the filter roll is reached.", dataType=o6.Boolean
        )
    )


o6.reference(AutomaticRollFilterType, "i=41", EndOfFilterRollAlarmType)


@o6.objecttype(nodeId="ns=paefs;i=1009", browseName="ns=paefs;FanType", displayName="FanType", description="A device for generating negative air pressure.")
class FanType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5109"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    maintenanceSwitchOn: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6208",
            browseName="ns=paefs;MaintenanceSwitchOn",
            description="Status of a physical maintenance switch on the fan. True when the switch is on.",
            dataType=o6.Boolean,
        )
    )
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6395", browseName="ns=paefs;Malfunction", description="Indicates whether there is an error with the fan. True in case of error.", dataType=o6.Boolean
        )
    )
    powerConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5065", browseName="ns=paefs;PowerConsumption", description="Contains information regarding the energy consumption of the fan.")
    )
    rotationalSpeed: SensorSetpointWriteType | None


o6.reference(FanType, "i=41", MalfunctionAlarmType)
o6.reference(FanType, "i=41", MaintenanceSwitchConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1016",
    browseName="ns=paefs;CleaningUnitValveType",
    displayName="CleaningUnitValveType",
    description="Part of the pressure tank of the cleaning unit for triggering a pressure surge into the\nseparator.",
)
class CleaningUnitValveType(ns0.objtypes.BaseObjectType):
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6359",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the cleaning unit valve is malfunctioning. True in case of error. Malfunctions can be, for example, that the valve does not open or close.",
            dataType=o6.Boolean,
        )
    )
    open: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6418", browseName="ns=paefs;Open", description="Indicates that the valve is open.", dataType=o6.Boolean)
    )


o6.reference(CleaningUnitValveType, "i=41", MalfunctionAlarmType)


@o6.objecttype(
    nodeId="ns=paefs;i=1006",
    browseName="ns=paefs;DischargeSystemType",
    displayName="DischargeSystemType",
    description="Device used to remove collected filter material from the filter unit. The container can be\ndischarged when a certain filling level is reached.",
)
class DischargeSystemType(ns0.objtypes.BaseObjectType):
    airConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5079", browseName="ns=paefs;AirConsumption", description="Contains information regarding the consumption of compressed air.")
    )
    dischargeContainerInstalled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6140", browseName="ns=paefs;DischargeContainerInstalled", description="Indicates that the discharge container is in place.", dataType=o6.Boolean
        )
    )
    dischargeSystemEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6230",
            browseName="ns=paefs;DischargeSystemEnabled",
            description="If enabled, discharge can be performed. If disabled, discharge cannot take place; for example, because a rotary valve is stopped or a discharge flap is closed.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fillingLevel: SensorMonitoringType | None
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5115"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType
    maintenanceSwitchOn: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6139",
            browseName="ns=paefs;MaintenanceSwitchOn",
            description="Status of a physical maintenance switch on the discharge system. True when the switch is on.",
            dataType=o6.Boolean,
        )
    )
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6420",
            browseName="ns=paefs;Malfunction",
            description="Indicates whether there is an error with the discharge system. True in case of error. Examples: discharge motor defective, discharge container full, discharge system blocked.",
            dataType=o6.Boolean,
        )
    )


o6.reference(DischargeSystemType, "i=41", MalfunctionAlarmType)
o6.reference(DischargeSystemType, "i=41", MaintenanceSwitchConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1008",
    browseName="ns=paefs;SafetySystemType",
    displayName="SafetySystemType",
    description="The safety system is a generic component that represents a protective device. Each\ncomponent in the PAEFS can reference an instance of the safety system via a Uses\nreference.",
)
class SafetySystemType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5111"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6430",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the safety system is malfunctioning. True in case of error.",
            dataType=o6.Boolean,
        )
    )
    triggered: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6219",
            browseName="ns=paefs;Triggered",
            description="Indicates that the safety system has been triggered. If true the safety system has been triggered.",
            dataType=o6.Boolean,
        )
    )


o6.reference(SafetySystemType, "i=41", MalfunctionAlarmType)
o6.reference(SafetySystemType, "i=41", SafetySystemTriggeredAlarmType)


@o6.objecttype(nodeId="ns=paefs;i=1022", browseName="ns=paefs;FilterMachineIdentificationType", displayName="FilterMachineIdentificationType")
class FilterMachineIdentificationType(machinery.objtypes.MachineIdentificationType):
    exIdentification: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6440", browseName="ns=paefs;ExIdentification", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    nominalAirflow: ns0.vartypes.AnalogUnitRangeType
    ratedPower: ns0.vartypes.AnalogUnitRangeType | None


ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6277",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=paefs;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Value", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=paefs;i=7003",
    browseName="ns=paefs;SetAndActivateAirflowSetpoint",
    description="The Method SetAirflowSetpoint sets a setpoint for the airflow. The value’s unit is the same as the one specified in object Airflow. Since setpoints are mutually exclusive, the method also sets the boolean IsActiveSetpoint of the setpoints for pressure and rotational speed to false.",
    inputArgs=o6.hasProperty(o6.ns["ns=paefs;i=6277"]),
)


@o6.objecttype(
    nodeId="ns=paefs;i=1005",
    browseName="ns=paefs;CleaningUnitType",
    displayName="CleaningUnitType",
    description="The CleaningUnitType represents a device for the reduction of filtered materials in separators",
)
class CleaningUnitType(ns0.objtypes.BaseObjectType):
    airConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5078", browseName="ns=paefs;AirConsumption", description="Describes the current consumption of compressed air.")
    )
    automaticCleaningEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6082",
            browseName="ns=paefs;AutomaticCleaningEnabled",
            description="If enabled, the cleaning unit may automatically perform the cleaning according to predefined rules when cleaning is necessary. Otherwise, automatic cleaning is blocked.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    cleaningActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6161", browseName="ns=paefs;CleaningActive", description="Describes that the unit is currently in a cleaning cycle.", dataType=o6.Boolean
        )
    )
    cleaningInterval: SensorSetpointWriteType | None
    cleaningRecommended: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6187", browseName="ns=paefs;CleaningRecommended", description="Indicates that cleaning of the separator is recommended.", dataType=o6.Boolean
        )
    )
    filterCleaningEffect: SensorSetpointWriteType | None
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    langleValveRangle: CleaningUnitValveType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5114"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6406",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the cleaning unit is malfunctioning. True in case of error. Malfunctions can be, for example, that the filter cleaning effect is not sufficient.",
            dataType=o6.Boolean,
        )
    )
    requestCleaning: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7007",
            browseName="ns=paefs;RequestCleaning",
            description="The Method RequestCleaning requests cleaning of the unit. The cleaning unit will perform the cleaning as soon as possible.",
        )
    )
    reservoirPressure: SensorSetpointWriteType | None
    totalCleaningCycles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6186",
            browseName="ns=paefs;TotalCleaningCycles",
            description="Count of the number of cleaning cycles carried out by the cleaning system.",
            dataType=o6.UInt32,
        )
    )


o6.reference(CleaningUnitType, "i=41", MalfunctionAlarmType)
o6.reference(CleaningUnitType, "i=41", CleaningRecommendedConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1007",
    browseName="ns=paefs;AirConnectionType",
    displayName="AirConnectionType",
    description="The air connection is an abstract component representing the state of a connection from the\nducting system to a filter unit. The connection can be open or closed. The open state\nrepresents a state of the ducting system where air can pass through to the filter unit.",
)
class AirConnectionType(ns0.objtypes.BaseObjectType):
    airflow: SensorMonitoringType | None
    close: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7009",
            browseName="ns=paefs;Close",
            description="The Method Close closes or switches some of the valves in the ducting system so that no air may pass through the ducting system to the device",
        )
    )
    connectionOpen: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6426",
            browseName="ns=paefs;ConnectionOpen",
            description="Indicates the connections status (open, closed, or a state in between)",
            dataType=paefs_datypes.AirConnectionOpenEnum,
        )
    )
    gasQuality: SensorMonitoringType | None
    humidity: SensorMonitoringType | None
    malfunction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6428",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the AirConnection is malfunctioning, i.e., an error occurs in a component that provides functionality for this abstract component; e.g., an error in the ducting system or a valve. True in case of error.",
            dataType=o6.Boolean,
        )
    )
    open: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7008",
            browseName="ns=paefs;Open",
            description="The Method Open opens or switches all valves of the ducting system so that the air can pass through to the filter device",
        )
    )
    pressure: SensorMonitoringType | None
    temperature: SensorMonitoringType | None


o6.reference(AirConnectionType, "i=41", MalfunctionAlarmType)


@o6.objecttype(
    nodeId="ns=paefs;i=1002",
    browseName="ns=paefs;FilterSystemType",
    displayName="FilterSystemType",
    description="Serves the purpose of extracting and filtering process gas; e.g., air. It consists of several\nfilter units and other devices and components.",
    interfaces=[di.objtypes.IOperationCounterType],
)
class FilterSystemType(ns0.objtypes.BaseObjectType):
    airConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(
            nodeId="ns=paefs;i=5002", browseName="ns=paefs;AirConsumption", description="Contains information regarding the consumption of compressed air of the filter system."
        )
    )
    airIntakeConnection: AirConnectionType = o6.hasComponent(
        AirConnectionType(
            nodeId="ns=paefs;i=5005",
            browseName="ns=paefs;AirIntakeConnection",
            description="The connection to the ducting system from which the process gas enters the filter system.",
        )
    )
    airOutletConnection: AirConnectionType = o6.hasComponent(
        AirConnectionType(
            nodeId="ns=paefs;i=5008",
            browseName="ns=paefs;AirOutletConnection",
            description="The connection to the ducting system to which the cleaned process gas leaves the filter system.",
        )
    )
    controlMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6021",
            browseName="ns=paefs;ControlMode",
            description="Operating mode that describes whether the system can be controlled externally. Possible values are manual, auto and other.",
            dataType=paefs_datypes.ControlModeEnum,
        )
    )
    identification: machinery.objtypes.MachineIdentificationType | None
    langleFanRangle: FanType | None
    langleFilterAidDeviceRangle: FilterAidDeviceType | None
    langleFilterUnitRangle: FilterUnitType
    langleSafetySystemRangle: SafetySystemType | None
    langleTemperatureRegulatorRangle: TemperatureRegulatorType | None = o6.hasComponent(
        TemperatureRegulatorType(
            nodeId="ns=paefs;i=5106",
            browseName="ns=paefs;<TemperatureRegulator>",
            description="All temperature regulators used on the server.",
            modellingRule="OptionalPlaceholder",
        )
    )
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5107"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType
    maintenanceRequested: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6238",
            browseName="ns=paefs;MaintenanceRequested",
            description="The maintenance request allows the manufacturer to inform the operator that the system requires maintenance. True = maintenance requested by system. False = no maintenance requested.",
            dataType=o6.Boolean,
        )
    )
    malfunction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6058",
            browseName="ns=paefs;Malfunction",
            description="Malfunction describes that the filter system has a collective fault message. True in case of error.",
            dataType=o6.Boolean,
        )
    )
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6181", browseName="ns=paefs;OperationCycleCounter", dataType=ns0.datatypes.UInteger)
    )
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6180", browseName="ns=paefs;OperationDuration", dataType=ns0.datatypes.Duration)
    )
    operationOff: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7005",
            browseName="ns=paefs;OperationOff",
            description="The Method OperationOff turns the filter system machine off. As with the OperationOn method, this method should be present under the FilterSystemType if and only if the filter units are considered components of the system rather than individual machines.",
        )
    )
    operationOn: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7004",
            browseName="ns=paefs;OperationOn",
            description="The Method OperationOn turns the filter system machine on. It should only be available on the filter system if the filter units are considered components of the filter system and do not have their own OperationOn and OperationOff methods.",
        )
    )
    powerConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5017", browseName="ns=paefs;PowerConsumption", description="Contains information regarding the energy consumption of the filter system.")
    )
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6054", browseName="ns=paefs;PowerOnDuration", dataType=ns0.datatypes.Duration)
    )
    pressureLoss: SensorMonitoringType | None


o6.reference(FilterSystemType, "i=41", MaintenanceRequestedConditionType)
o6.reference(FilterSystemType, "i=41", MalfunctionAlarmType)


@o6.objecttype(nodeId="ns=paefs;i=1004", browseName="ns=paefs;FilterAidDeviceType", displayName="FilterAidDeviceType", description="Device for the application of a filter aid.")
class FilterAidDeviceType(ns0.objtypes.BaseObjectType):
    airConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5037", browseName="ns=paefs;AirConsumption", description="Describes the compressed air consumption.")
    )
    automaticDosingEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6204",
            browseName="ns=paefs;AutomaticDosingEnabled",
            description="If enabled, the filter aid device is allowed to perform dosing automatically.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    compressedAirSupplyInterrupted: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6146", browseName="ns=paefs;CompressedAirSupplyInterrupted", description="Indicates that the air supply is interrupted.", dataType=o6.Boolean
        )
    )
    containerOpen: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6142", browseName="ns=paefs;ContainerOpen", description="Indicates that the filter aid reservoir is not closed.", dataType=o6.Boolean
        )
    )
    dosageAmount: SensorSetpointWriteType | None
    dosingRequested: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6144", browseName="ns=paefs;DosingRequested", description="Indicates that the filter system requests dosing.", dataType=o6.Boolean
        )
    )
    fillingLevel: SensorMonitoringType | None
    filterAidDeviceStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6143",
            browseName="ns=paefs;FilterAidDeviceStatus",
            description="Describes the action performed by the dosage unit (see FilterAidDeviceStatusEnum).",
            dataType=paefs_datypes.FilterAidDeviceStatusEnum,
        )
    )
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5112"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    malfunction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6145",
            browseName="ns=paefs;Malfunction",
            description="Indicates that the filter aid device is malfunctioning. True in case of error. Malfunctions can be, for example, that there is no more filter aid or that there is a malfunction in the subsystems of the filter aid device.",
            dataType=o6.Boolean,
        )
    )
    powerConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5035", browseName="ns=paefs;PowerConsumption", description="Describes the current power consumption of the filter aid device.")
    )
    resetFillingLevel: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=paefs;i=7006", browseName="ns=paefs;ResetFillingLevel", description="The Method ResetFillingLevel resets the filling level of the filter aid reservoir.")
    )
    triggerDosing: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=paefs;i=7042", browseName="ns=paefs;TriggerDosing", description="The Method TriggerDosing triggers a single additional dosage.")
    )


o6.reference(FilterAidDeviceType, "i=41", ContainerOpenConditionType)
o6.reference(FilterAidDeviceType, "i=41", MalfunctionAlarmType)
o6.reference(FilterAidDeviceType, "i=41", CompressedAirSupplyInterruptedAlarmType)


ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6278",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=paefs;i=7071",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Value", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=paefs;i=7071",
    browseName="ns=paefs;SetAndActivatePressureSetpoint",
    description="The Method SetPressureSetpoint sets a setpoint for the pressure. The value’s unit is the same as the one specified in object Pressure. Since setpoints are mutually exclusive, the method also sets the boolean IsActiveSetpoint of the setpoints for airflow and rotational speed to false.",
    inputArgs=o6.hasProperty(o6.ns["ns=paefs;i=6278"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6279",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=paefs;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Value", dataType=o6.Double, valueRank=-1)],
)
o6.call(
    nodeId="ns=paefs;i=7072",
    browseName="ns=paefs;SetAndActivateRotationalSpeedSetpoint",
    description="The Method SetRotationalSpeedSetpoint sets a setpoint for the rotational speed. The value’s unit is the same as the one specified in object RotationalSpeed. Since setpoints are mutually exclusive, the method also sets the boolean IsActiveSetpoint of the setpoints for airflow and pressure to false.",
    inputArgs=o6.hasProperty(o6.ns["ns=paefs;i=6279"]),
)


@o6.objecttype(
    nodeId="ns=paefs;i=1012",
    browseName="ns=paefs;FilterUnitType",
    displayName="FilterUnitType",
    description="Subcomponent of a filter system consisting of other devices and components.",
    interfaces=[di.objtypes.IOperationCounterType],
)
class FilterUnitType(ns0.objtypes.BaseObjectType):
    airConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(
            nodeId="ns=paefs;i=5030", browseName="ns=paefs;AirConsumption", description="Contains information regarding the consumption of compressed air of the filter unit."
        )
    )
    airIntakeConnection: AirConnectionType = o6.hasComponent(
        AirConnectionType(
            nodeId="ns=paefs;i=5023",
            browseName="ns=paefs;AirIntakeConnection",
            description="The connection to the ducting system from which the polluted process gas enters the filter unit.",
        )
    )
    airOutletConnection: AirConnectionType = o6.hasComponent(
        AirConnectionType(
            nodeId="ns=paefs;i=5024",
            browseName="ns=paefs;AirOutletConnection",
            description="The connection to the ducting system through which the cleaned process gas leaves the filter unit.",
        )
    )
    airflow: SensorSetpointReadType | None
    identification: machinery.objtypes.MachineryItemIdentificationType | None
    langleCleaningUnitRangle: CleaningUnitType | None
    langleDischargeSystemRangle: DischargeSystemType | None
    langleSeparatorRangle: SeparatorType | None = o6.hasComponent(
        SeparatorType(
            nodeId="ns=paefs;i=5036",
            browseName="ns=paefs;<Separator>",
            description="The separators that are part of the filter unit.",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=paefs;i=5108"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType
    maintenanceRequested: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6141",
            browseName="ns=paefs;MaintenanceRequested",
            description="The maintenance request allows the manufacturer to inform the operator that the system requires maintenance. True = maintenance requested by system. False = no maintenance requested.",
            dataType=o6.Boolean,
        )
    )
    malfunction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=6036",
            browseName="ns=paefs;Malfunction",
            description="One or more subsystems of the filter unit have a malfunction. True in case of error.",
            dataType=o6.Boolean,
        )
    )
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6251", browseName="ns=paefs;OperationCycleCounter", dataType=ns0.datatypes.UInteger)
    )
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6250", browseName="ns=paefs;OperationDuration", dataType=ns0.datatypes.Duration)
    )
    operationOff: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7002",
            browseName="ns=paefs;OperationOff",
            description="The Method OperationOff turns the machine off. As with the OperationOn Method, this method should be present under the filter unit if and only if the filter unit is considered a machine.",
        )
    )
    operationOn: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=paefs;i=7001",
            browseName="ns=paefs;OperationOn",
            description="The Method OperationOn turns the machine on. It should only be available on the filter unit if the filter unit is considered a machine, rather than a component of a larger machine. If the filter unit is only a component of a larger machine, the OperationOn Method should be present on the filter system.",
        )
    )
    powerConsumption: ConsumptionType | None = o6.hasComponent(
        ConsumptionType(nodeId="ns=paefs;i=5029", browseName="ns=paefs;PowerConsumption", description="Contains information regarding the energy consumption of the filter unit.")
    )
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6182", browseName="ns=paefs;PowerOnDuration", dataType=ns0.datatypes.Duration)
    )
    pressure: SensorSetpointReadType | None
    pressureLoss: SensorMonitoringType | None
    rotationalSpeed: SensorSetpointReadType | None
    setAndActivateAirflowSetpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=paefs;i=7003"])
    setAndActivatePressureSetpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=paefs;i=7071"])
    setAndActivateRotationalSpeedSetpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=paefs;i=7072"])


o6.reference(FilterUnitType, "i=41", MaintenanceRequestedConditionType)
o6.reference(FilterUnitType, "i=41", MalfunctionAlarmType)


@o6.objecttype(
    nodeId="ns=paefs;i=1027",
    browseName="ns=paefs;WashingAgentInflowOpenConditionType",
    displayName="WashingAgentInflowOpenConditionType",
    description="Triggered when the washing agent inflow valve is opened or closed",
)
class WashingAgentInflowOpenConditionType(ns0.objtypes.ConditionType):
    open: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8419",
            browseName="ns=paefs;Open",
            description="Reflects the value of the WashingAgentInflowOpen property of the WetSeparatorType at the time the event was sent",
            dataType=o6.Boolean,
        )
    )


o6.reference(WetSeparatorType, "i=41", WashingAgentInflowOpenConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1028",
    browseName="ns=paefs;WashingAgentDrainOpenConditionType",
    displayName="WashingAgentDrainOpenConditionType",
    description="The WashingAgentDrainOpenConditionType is triggered when the washing agent drain valve is opened or closed",
)
class WashingAgentDrainOpenConditionType(ns0.objtypes.ConditionType):
    open: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8420",
            browseName="ns=paefs;Open",
            description="Reflects the value of the WashingAgentDrainOpen property of the WetSeparatorType at the time the event was sent",
            dataType=o6.Boolean,
        )
    )


o6.reference(WetSeparatorType, "i=41", WashingAgentDrainOpenConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1033",
    browseName="ns=paefs;FilterAidDeviceStatusChangedConditionType",
    displayName="FilterAidDeviceStatusChangedConditionType",
    description="Triggered when the FilterAidDeviceStatus of the FilterAidDeviceType changes",
)
class FilterAidDeviceStatusChangedConditionType(ns0.objtypes.ConditionType):
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8421",
            browseName="ns=paefs;Status",
            description="Reflects the value of the FilterAidDeviceStatus property at the time the condition was triggered",
            dataType=paefs_datypes.FilterAidDeviceStatusEnum,
        )
    )


o6.reference(FilterAidDeviceType, "i=41", FilterAidDeviceStatusChangedConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1036",
    browseName="ns=paefs;CleaningUnitActiveConditionType",
    displayName="CleaningUnitActiveConditionType",
    description="Triggered when a cleaning cycle is started or stopped",
)
class CleaningUnitActiveConditionType(ns0.objtypes.ConditionType):
    active: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8424",
            browseName="ns=paefs;Active",
            description="Reflects the value of the CleaningActive property of the CleaningUnitType at the time the condition was triggered",
            dataType=o6.Boolean,
        )
    )


o6.reference(CleaningUnitType, "i=41", CleaningUnitActiveConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1038",
    browseName="ns=paefs;DischargeContainerInstalledConditionType",
    displayName="DischargeContainerInstalledConditionType",
    description="The DischargeSystemType sends this event when the container is installed or removed",
)
class DischargeContainerInstalledConditionType(ns0.objtypes.ConditionType):
    installed: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8425",
            browseName="ns=paefs;Installed",
            description="Reflects the value of the DischargeContainerInstalled property of the DischargeSystemType at the time the event was sent",
            dataType=o6.Boolean,
        )
    )


o6.reference(DischargeSystemType, "i=41", DischargeContainerInstalledConditionType)


@o6.objecttype(
    nodeId="ns=paefs;i=1040",
    browseName="ns=paefs;AirConnectionStatusChangedConditionType",
    displayName="AirConnectionStatusChangedConditionType",
    description="Triggered when the ConnectionOpen variable of the AirConnectionType changes",
)
class AirConnectionStatusChangedConditionType(ns0.objtypes.ConditionType):
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=paefs;i=8427",
            browseName="ns=paefs;Status",
            description="Reflects the value of the ConnectionOpen property at the time the event is triggered",
            dataType=paefs_datypes.AirConnectionOpenEnum,
        )
    )


o6.reference(AirConnectionType, "i=41", AirConnectionStatusChangedConditionType)


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, paefs_reftypes, paefs_datypes
