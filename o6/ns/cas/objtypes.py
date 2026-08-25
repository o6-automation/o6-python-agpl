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

"""Generated OPC UA cas namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as cas_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=cas;i=1006", browseName="ns=cas;OperationalType", displayName="OperationalType", description="Data for normal operation of the topology element.")
class OperationalType(di.objtypes.FunctionalGroupType):
    healthState: ns0.vartypes.DataItemType | None
    integratedState: ns0.vartypes.DataItemType | None
    onOff: ns0.vartypes.TwoStateDiscreteType | None
    operatingState: ns0.vartypes.DataItemType | None


@o6.objecttype(
    nodeId="ns=cas;i=1002",
    browseName="ns=cas;AirnetOperationalType",
    displayName="AirnetOperationalType",
    description="Contains parameters and methods related to counting process or maintenance data of the airnet.",
)
class AirnetOperationalType(OperationalType):
    airDeliveryRate: ns0.vartypes.BaseAnalogType | None
    compressorsIntegrated: ns0.vartypes.BaseAnalogType | None
    compressorsIsolated: ns0.vartypes.BaseAnalogType | None
    compressorsNotAvailable: ns0.vartypes.BaseAnalogType | None
    controlPressure: ns0.vartypes.BaseAnalogType | None
    healthState: ns0.vartypes.DataItemType | None
    integratedState: ns0.vartypes.DataItemType | None
    operatingState: ns0.vartypes.DataItemType | None
    specificEnergy: ns0.vartypes.BaseAnalogType | None
    specificEnergyCost: ns0.vartypes.BaseAnalogType | None
    volumeFlowRateAvailable: ns0.vartypes.BaseAnalogType | None
    volumeFlowRateUnavailable: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=cas;i=1007",
    browseName="ns=cas;AirnetType",
    displayName="AirnetType",
    description="In a compressed air system the airnet describes the piping, including valves and vessels, and all components between the inlet of the compressed air station and the distribution point to the customer, including compressors, dryers, filters, etc. A compressed air system may contain several airnets and it’s possible for the master control system to manage all airnets simultaniously. A component, like a compressor, must not be assigned to more than one airnet.",
)
class AirnetType(di.objtypes.TopologyElementType):
    ambient: FluidQuantitiesType | None
    components: AirnetComponentsType | None
    configuration: AirnetConfigurationType | None
    electricalCircuit: ElectricalCircuitType | None
    identification: CASIdentificationType
    operational: AirnetOperationalType | None
    processFluidCircuit: FluidCircuitType | None


@o6.objecttype(
    nodeId="ns=cas;i=1013", browseName="ns=cas;FluidCircuitType", displayName="FluidCircuitType", description="Measurements and calculations of a fluid of the topology element."
)
class FluidCircuitType(ns0.objtypes.BaseObjectType):
    delta: FluidQuantitiesType | None
    fluidType: ns0.vartypes.DataItemType | None
    inlet: FluidQuantitiesType | None
    langleOtherRangle: FluidQuantitiesType | None
    outlet: FluidQuantitiesType | None


@o6.objecttype(
    nodeId="ns=cas;i=1014",
    browseName="ns=cas;ElectricalCircuitType",
    displayName="ElectricalCircuitType",
    description="Measurements and calculations of the electrical ports and delta of the topology element.",
)
class ElectricalCircuitType(ns0.objtypes.BaseObjectType):
    delta: ElectricalQuantitiesType | None
    input: ElectricalQuantitiesType | None
    langleOtherRangle: ElectricalQuantitiesType | None
    output: ElectricalQuantitiesType | None


@o6.objecttype(nodeId="ns=cas;i=1017", browseName="ns=cas;MCSType", displayName="MCSType")
class MCSType(di.objtypes.TopologyElementType):
    analyses: AnalysesType | None
    configuration: MCSConfigurationType | None
    electricalCircuit: ElectricalCircuitType | None
    events: EventsType | None
    identification: machinery.objtypes.MachineryComponentIdentificationType
    operational: OperationalType | None
    statistics: StatisticsType | None


@o6.objecttype(nodeId="ns=cas;i=1020", browseName="ns=cas;EventsType", displayName="EventsType", description="Alarms and conditions of the topology element.")
class EventsType(di.objtypes.FunctionalGroupType):
    emergencyStop: ns0.objtypes.OffNormalAlarmType | None
    langleEventRangle: ns0.objtypes.ConditionType | None
    service: ns0.objtypes.OffNormalAlarmType | None
    shutdown: ns0.objtypes.OffNormalAlarmType | None
    warning: ns0.objtypes.OffNormalAlarmType | None


@o6.objecttype(nodeId="ns=cas;i=1028", browseName="ns=cas;MaintenanceType", displayName="MaintenanceType", description="Maintenance purposes of sensors.")
class MaintenanceType(di.objtypes.FunctionalGroupType):
    realTimeSinceLastService: ns0.vartypes.BaseAnalogType
    realTimeToNextService: ns0.vartypes.BaseAnalogType


@o6.objecttype(nodeId="ns=cas;i=1037", browseName="ns=cas;ConfigurationType", displayName="ConfigurationType", description="Configure the behavior of the topology element.")
class ConfigurationType(di.objtypes.FunctionalGroupType):
    pass


@o6.objecttype(nodeId="ns=cas;i=1016", browseName="ns=cas;AirnetConfigurationType", displayName="AirnetConfigurationType", description="Configure the behavior of an airnet.")
class AirnetConfigurationType(ConfigurationType):
    operatingModes: ns0.vartypes.MultiStateDiscreteType | None
    operatingProfiles: ns0.vartypes.MultiStateDiscreteType


@o6.objecttype(nodeId="ns=cas;i=1043", browseName="ns=cas;ParticleType", displayName="ParticleType")
class ParticleType(ns0.objtypes.BaseObjectType):
    fine: ns0.vartypes.BaseAnalogType
    large: ns0.vartypes.BaseAnalogType
    medium: ns0.vartypes.BaseAnalogType


@o6.objecttype(nodeId="ns=cas;i=1044", browseName="ns=cas;DesignType", displayName="DesignType", description="Static design properties of the topology element.")
class DesignType(di.objtypes.FunctionalGroupType):
    componentClass: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1008", browseName="ns=cas;CompressorDesignType", displayName="CompressorDesignType", description="Static design properties of a compressor.")
class CompressorDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    displacementType: ns0.vartypes.DataItemType | None
    lubricationType: ns0.vartypes.DataItemType | None
    numberOfStages: ns0.vartypes.DataItemType | None
    variableFlow: ns0.vartypes.TwoStateDiscreteType | None


@o6.objecttype(nodeId="ns=cas;i=1009", browseName="ns=cas;FilterDesignType", displayName="FilterDesignType", description="Static design properties of a filter.")
class FilterDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    filterClass: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1023", browseName="ns=cas;ReceiverDesignType", displayName="ReceiverDesignType", description="Static design properties of a receiver.")
class ReceiverDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    volume: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=cas;i=1031", browseName="ns=cas;SensorDesignType", displayName="SensorDesignType", description="Static design properties of a sensor.")
class SensorDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    sensorTechnology: ns0.vartypes.DataItemType | None
    softSensor: ns0.vartypes.TwoStateDiscreteType | None


@o6.objecttype(nodeId="ns=cas;i=1032", browseName="ns=cas;ValveDesignType", displayName="ValveDesignType", description="Static design properties of a valve.")
class ValveDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    numberOfPorts: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1033", browseName="ns=cas;DryerDesignType", displayName="DryerDesignType", description="Static design properties of a dryer.")
class DryerDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None
    lowestAmbientTemperature: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=cas;i=1036", browseName="ns=cas;DrainDesignType", displayName="DrainDesignType", description="Static design properties of a condensate drain.")
class DrainDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1040", browseName="ns=cas;SeparatorDesignType", displayName="SeparatorDesignType", description="Static design properties of a separator.")
class SeparatorDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1041", browseName="ns=cas;ConverterDesignType", displayName="ConverterDesignType", description="Static design properties of a converter.")
class ConverterDesignType(DesignType):
    componentClass: ns0.vartypes.DataItemType | None


@o6.objecttype(
    nodeId="ns=cas;i=1045",
    browseName="ns=cas;CompressorOperationalType",
    displayName="CompressorOperationalType",
    description="Contains parameters and methods useful for normal operation of the compressor, like process data.",
)
class CompressorOperationalType(OperationalType):
    activePressureBand: ns0.vartypes.DataItemType | None
    flowRateRatio: ns0.vartypes.BaseAnalogType | None
    isentropicEfficiency: ns0.vartypes.BaseAnalogType | None
    operatingState: ns0.vartypes.DataItemType | None
    specificEnergyRequirement: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=cas;i=1046",
    browseName="ns=cas;ConverterOperationalType",
    displayName="ConverterOperationalType",
    description="Contains parameters and methods useful for normal operation of the converter, like process data.",
)
class ConverterOperationalType(OperationalType):
    catalyticMaterialTemperature: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=cas;i=1049", browseName="ns=cas;AnalysesType", displayName="AnalysesType", description="Invokable analyses for the topology element.")
class AnalysesType(di.objtypes.FunctionalGroupType):
    energyReportISO50001: AnalysisType | None
    langleAnalysisRangle: AnalysisType | None
    langlePrefabAnalysisRangle: ns0.objtypes.FileType | None


@o6.objecttype(
    nodeId="ns=cas;i=1052",
    browseName="ns=cas;DryerOperationalType",
    displayName="DryerOperationalType",
    description="Contains parameters and methods useful for normal operation of the dryer, like process data.",
)
class DryerOperationalType(OperationalType):
    onOff: ns0.vartypes.TwoStateDiscreteType | None
    operatingState: ns0.vartypes.DataItemType | None
    pressureDewPoint: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=cas;i=1053",
    browseName="ns=cas;ValveOperationalType",
    displayName="ValveOperationalType",
    description="Contains parameters and methods useful for normal operation of the valve, like process data.",
)
class ValveOperationalType(OperationalType):
    continuousPosition: ns0.vartypes.BaseAnalogType | None
    portUsed: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=cas;i=1054", browseName="ns=cas;CalibrationType", displayName="CalibrationType", description="Dates important for the calibration of a sensor.")
class CalibrationType(di.objtypes.FunctionalGroupType):
    lastCalibrationDate: ns0.vartypes.DataItemType
    nextCalibrationDate: ns0.vartypes.DataItemType


@o6.objecttype(
    nodeId="ns=cas;i=1047",
    browseName="ns=cas;ComponentsGroupType",
    displayName="ComponentsGroupType",
    description="All components of a specific type in a compressed air system as browsable objects.",
)
class ComponentsGroupType(machinery.objtypes.MachineComponentsType):
    chargingSystems: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5012", browseName="ns=cas;ChargingSystems", description="Organizes all charging systems connected to the compressed air system."
        )
    )
    compressors: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5011", browseName="ns=cas;Compressors", description="Organizes all compressors connected to the compressed air system."
        )
    )
    condensateDrains: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5014", browseName="ns=cas;CondensateDrains", description="Organizes all condensate drains connected to the compressed air system."
        )
    )
    condensateSeparators: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5016", browseName="ns=cas;CondensateSeparators", description="Organizes all condensate separators connected to the compressed air system."
        )
    )
    converters: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5023", browseName="ns=cas;Converters", description="Organizes all converters connected to the compressed air system."
        )
    )
    coolingSystems: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5024", browseName="ns=cas;CoolingSystems", description="Organizes all cooling systems connected to the compressed air system."
        )
    )
    dryers: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5028", browseName="ns=cas;Dryers", description="Organizes all dryers connected to the compressed air system.")
    )
    filters: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5091", browseName="ns=cas;Filters", description="Organizes all filters connected to the compressed air system.")
    )
    heatRecoverySystems: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5188", browseName="ns=cas;HeatRecoverySystems", description="Organizes all heat recovery systems connected to the compressed air system."
        )
    )
    langleComponentsGroupRangle: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5187",
            browseName="ns=cas;<ComponentsGroup>",
            description="All components of a specific type in a compressed air system as browsable objects.",
            modellingRule="OptionalPlaceholder",
        )
    )
    receivers: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(
            nodeId="ns=cas;i=5190", browseName="ns=cas;Receivers", description="Organizes all receivers connected to the compressed air system."
        )
    )
    sensors: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5191", browseName="ns=cas;Sensors", description="Organizes all sensors connected to the compressed air system.")
    )
    valves: machinery.objtypes.MachineComponentsType | None = o6.hasComponent(
        machinery.objtypes.MachineComponentsType(nodeId="ns=cas;i=5192", browseName="ns=cas;Valves", description="Organizes all valves connected to the compressed air system.")
    )


@o6.objecttype(nodeId="ns=cas;i=1050", browseName="ns=cas;AirnetComponentsType", displayName="AirnetComponentsType", description="All components connected to the airnet.")
class AirnetComponentsType(ns0.objtypes.FolderType):
    chargingSystems: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5194", browseName="ns=cas;ChargingSystems", description="Organizes all charging systems connected to the airnet.")
    )
    compressors: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5195", browseName="ns=cas;Compressors", description="Organizes all compressors connected to the airnet.")
    )
    condensateDrains: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5196", browseName="ns=cas;CondensateDrains", description="Organizes all condensate drains connected to the airnet.")
    )
    condensateSeparators: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5212", browseName="ns=cas;CondensateSeparators", description="Organizes all condensate separators connected to the airnet.")
    )
    converters: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5213", browseName="ns=cas;Converters", description="Organizes all converters connected to the airnet.")
    )
    coolingSystems: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5214", browseName="ns=cas;CoolingSystems", description="Organizes all cooling systems connected to the airnet.")
    )
    dryers: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5215", browseName="ns=cas;Dryers", description="Organizes all dryers connected to the airnet.")
    )
    filters: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5218", browseName="ns=cas;Filters", description="Organizes all filters connected to the airnet.")
    )
    heatRecoverySystems: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5219", browseName="ns=cas;HeatRecoverySystems", description="Organizes all heat recovery systems connected to the airnet.")
    )
    langleComponentsGroupRangle: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=cas;i=5193",
            browseName="ns=cas;<ComponentsGroup>",
            description="All components of a specific type connected to the airnet.",
            modellingRule="OptionalPlaceholder",
        )
    )
    receivers: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5220", browseName="ns=cas;Receivers", description="Organizes all receivers connected to the airnet.")
    )
    sensors: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5221", browseName="ns=cas;Sensors", description="Organizes all sensors connected to the airnet.")
    )
    valves: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=cas;i=5222", browseName="ns=cas;Valves", description="Organizes all valves connected to the airnet.")
    )


@o6.objecttype(
    nodeId="ns=cas;i=1012",
    browseName="ns=cas;FluidQuantitiesType",
    displayName="FluidQuantitiesType",
    description="Contains parameters for fluid conditions at the component.",
    interfaces=[ia.objtypes.IStatisticsType],
)
class FluidQuantitiesType(ns0.objtypes.BaseObjectType):
    absolutePressure: ns0.vartypes.BaseAnalogType | None
    accumulatedVolume: ns0.vartypes.BaseAnalogType | None
    dewPoint: ns0.vartypes.BaseAnalogType | None
    gaugePressure: ns0.vartypes.BaseAnalogType | None
    langleQuantityRangle: ns0.vartypes.BaseAnalogType | None
    massFlowRate: ns0.vartypes.BaseAnalogType | None
    oilConcentration: ns0.vartypes.BaseAnalogType | None
    particlesPerSizeRange: ParticleType | None
    relativeHumidity: ns0.vartypes.BaseAnalogType | None
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=7007", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time.")
    )
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=6541",
            browseName="ns=ia;StartTime",
            description="Indicates the point in time at which the collection of the statistical data has been started.",
            dataType=o6.DateTime,
        )
    )
    temperature: ns0.vartypes.BaseAnalogType | None
    volume: ns0.vartypes.BaseAnalogType | None
    volumeFlowRate: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=cas;i=1051",
    browseName="ns=cas;CASIdentificationType",
    displayName="CASIdentificationType",
    description="Identification properties for compressed air systems and airnets.",
    interfaces=[di.objtypes.ITagNameplateType],
)
class CASIdentificationType(di.objtypes.FunctionalGroupType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=7702", browseName="ns=cas;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=7703", browseName="ns=cas;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=cas;i=1018",
    browseName="ns=cas;StatisticsType",
    displayName="StatisticsType",
    description="Data for statistics applications for the topology element.",
    interfaces=[ia.objtypes.IAggregateStatisticsType],
)
class StatisticsType(di.objtypes.FunctionalGroupType):
    realTime: ns0.vartypes.BaseAnalogType | None
    realTimeToNextService: ns0.vartypes.BaseAnalogType | None
    resetCondition: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=6231",
            browseName="ns=ia;ResetCondition",
            description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
            dataType=o6.String,
        )
    )
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=7793", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time.")
    )
    runningTime: ns0.vartypes.BaseAnalogType | None
    runningTimeToNextService: ns0.vartypes.BaseAnalogType | None
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=6230",
            browseName="ns=ia;StartTime",
            description="Indicates the point in time at which the collection of the statistical data has been started.",
            dataType=o6.DateTime,
        )
    )


@o6.objecttype(
    nodeId="ns=cas;i=1027",
    browseName="ns=cas;CompressorStatisticsType",
    displayName="CompressorStatisticsType",
    description="Contains parameters and methods related to counting process or maintenance data of the compressor.",
)
class CompressorStatisticsType(StatisticsType):
    loadedTime: ns0.vartypes.BaseAnalogType | None
    unloadedTime: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=cas;i=1011",
    browseName="ns=cas;ElectricalQuantitiesType",
    displayName="ElectricalQuantitiesType",
    description="Contains parameters for measurements and calculations of electrical connections at the component.",
    interfaces=[ia.objtypes.IStatisticsType],
)
class ElectricalQuantitiesType(ns0.objtypes.BaseObjectType):
    apparentPower: ns0.vartypes.BaseAnalogType | None
    current: ns0.vartypes.BaseAnalogType | None
    energy: ns0.vartypes.BaseAnalogType | None
    power: ns0.vartypes.BaseAnalogType | None
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=7814", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time.")
    )
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=6113",
            browseName="ns=ia;StartTime",
            description="Indicates the point in time at which the collection of the statistical data has been started.",
            dataType=o6.DateTime,
        )
    )
    voltage: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=cas;i=1004", browseName="ns=cas;AnalysisType", displayName="AnalysisType", description="Invokable analysis for the topology element.")
class AnalysisType(ns0.objtypes.BaseObjectType):
    outputFile: ns0.objtypes.FileType | None
    trigger: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=7919", browseName="ns=cas;Trigger", description="Triggers the analysis on the MCS in a compressed air system.")
    )


@o6.objecttype(
    nodeId="ns=cas;i=1019",
    browseName="ns=cas;MCSConfigurationType",
    displayName="MCSConfigurationType",
    description="Contains parameters and methods for configuring the behaviour of the MCS.",
)
class MCSConfigurationType(ConfigurationType):
    communicationSettings: CommunicationSettingsType | None
    configurationFile: ns0.objtypes.FileType | None
    loadConfigurationFile: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=9785", browseName="ns=cas;LoadConfigurationFile", description="Loads the configuration stored in ConfigurationFile to the MCS.")
    )
    saveConfigurationFile: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=10123", browseName="ns=cas;SaveConfigurationFile", description="Saves the current configuration of the MCS to the stored ConfigurationFile.")
    )


@o6.objecttype(nodeId="ns=cas;i=1038", browseName="ns=cas;AirnetsType", displayName="AirnetsType")
class AirnetsType(machinery.objtypes.MachineComponentsType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=10213",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("cas:Airnets"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleComponentRangle: AirnetType | None


@o6.objecttype(nodeId="ns=cas;i=1035", browseName="ns=cas;CASType", displayName="CASType", description="Compressed air system type")
class CASType(ns0.objtypes.BaseObjectType):
    airnets: AirnetsType | None = o6.hasComponent(
        AirnetsType(nodeId="ns=cas;i=5006", browseName="ns=cas;Airnets", description="All airnets in a compressed air system as browsable objects.")
    )
    components: ComponentsGroupType | None
    identification: CASIdentificationType | None
    mCS: MCSType | None


@o6.objecttype(
    nodeId="ns=cas;i=1048",
    browseName="ns=cas;CommunicationSettingsType",
    displayName="CommunicationSettingsType",
    description="OPC UA communication settings of the MCS in a compressed air system.",
)
class CommunicationSettingsType(ns0.objtypes.BaseObjectType):
    defaultGateway: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=10520", browseName="ns=cas;DefaultGateway", description="IP Address of the default gateway used by the MCS.", dataType=o6.String)
    )
    dhcp: ns0.vartypes.TwoStateDiscreteType | None
    dnsServer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=10521", browseName="ns=cas;DnsServer", description="IP Address of the DNS server used by the MCS.", dataType=o6.String)
    )
    domainName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=6324", browseName="ns=cas;DomainName", description="Domain name the MCS is assigned to.", dataType=o6.String)
    )
    hostname: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=6325", browseName="ns=cas;Hostname", description="Host name of the MCS.", dataType=o6.String)
    )
    ipAddress: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=6326", browseName="ns=cas;IpAddress", description="IP address of the MCS.", dataType=o6.String)
    )
    ipVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=10527", browseName="ns=cas;IpVersion", description="Version of the internet protocol used for the MCS.", dataType=cas_datypes.IpVersionEnum
        )
    )
    macAddress: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=cas;i=6460", browseName="ns=cas;MacAddress", description="MAC address of the NIC of the MCS.", dataType=o6.String)
    )
    subnetMask: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cas;i=10528", browseName="ns=cas;SubnetMask", description="Subnet mask of the MCS.", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=cas;i=1003",
    browseName="ns=cas;DrainOperationalType",
    displayName="DrainOperationalType",
    description="Contains parameters and methods useful for normal operation of the condensate drain, like process data.",
)
class DrainOperationalType(OperationalType):
    drainTest: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=cas;i=10530", browseName="ns=cas;DrainTest", description="Invoke a drain test on a condensate drain.")
    )


@o6.objecttype(nodeId="ns=cas;i=1021", browseName="ns=cas;CASComponentType", displayName="CASComponentType")
class CASComponentType(di.objtypes.TopologyElementType):
    activeAirnet: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cas;i=12533",
            browseName="ns=cas;ActiveAirnet",
            description="Indicates which airnet is currently using this component.",
            dataType=o6.NodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ambient: FluidQuantitiesType | None
    configuration: ConfigurationType | None
    coolantCircuit: FluidCircuitType | None
    design: DesignType | None
    electricalCircuit: ElectricalCircuitType | None
    events: EventsType | None
    identification: machinery.objtypes.MachineryItemIdentificationType
    operational: OperationalType | None
    processFluidCircuit: FluidCircuitType | None
    statistics: StatisticsType | None


@o6.objecttype(nodeId="ns=cas;i=1001", browseName="ns=cas;CoolingSystemType", displayName="CoolingSystemType")
class CoolingSystemType(CASComponentType):
    pass


@o6.objecttype(nodeId="ns=cas;i=1005", browseName="ns=cas;ChargingSystemType", displayName="ChargingSystemType")
class ChargingSystemType(CASComponentType):
    pass


@o6.objecttype(nodeId="ns=cas;i=1015", browseName="ns=cas;SensorType", displayName="SensorType")
class SensorType(CASComponentType):
    calibration: CalibrationType | None
    design: SensorDesignType | None
    maintenance: MaintenanceType | None
    operational: OperationalType | None


@o6.objecttype(nodeId="ns=cas;i=1022", browseName="ns=cas;ReceiverType", displayName="ReceiverType")
class ReceiverType(CASComponentType):
    design: ReceiverDesignType | None


@o6.objecttype(nodeId="ns=cas;i=1024", browseName="ns=cas;ValveType", displayName="ValveType")
class ValveType(CASComponentType):
    design: ValveDesignType | None
    operational: ValveOperationalType | None


@o6.objecttype(nodeId="ns=cas;i=1025", browseName="ns=cas;DrainType", displayName="DrainType")
class DrainType(CASComponentType):
    design: DrainDesignType | None
    operational: DrainOperationalType | None
    processFluidCircuit: FluidCircuitType | None


@o6.objecttype(nodeId="ns=cas;i=1026", browseName="ns=cas;SeparatorType", displayName="SeparatorType")
class SeparatorType(CASComponentType):
    design: SeparatorDesignType | None
    processFluidCircuit: FluidCircuitType | None


@o6.objecttype(nodeId="ns=cas;i=1029", browseName="ns=cas;ConverterType", displayName="ConverterType")
class ConverterType(CASComponentType):
    design: ConverterDesignType | None
    operational: ConverterOperationalType | None


@o6.objecttype(nodeId="ns=cas;i=1030", browseName="ns=cas;DryerType", displayName="DryerType")
class DryerType(CASComponentType):
    design: DryerDesignType | None
    operational: DryerOperationalType | None


@o6.objecttype(nodeId="ns=cas;i=1034", browseName="ns=cas;FilterType", displayName="FilterType")
class FilterType(CASComponentType):
    design: FilterDesignType | None


@o6.objecttype(nodeId="ns=cas;i=1039", browseName="ns=cas;CompressorType", displayName="CompressorType")
class CompressorType(CASComponentType):
    design: CompressorDesignType | None
    identification: machinery.objtypes.MachineIdentificationType
    operational: CompressorOperationalType | None
    statistics: CompressorStatisticsType | None


@o6.objecttype(nodeId="ns=cas;i=1042", browseName="ns=cas;HeatRecoverySystemType", displayName="HeatRecoverySystemType")
class HeatRecoverySystemType(CASComponentType):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, cas_datypes
