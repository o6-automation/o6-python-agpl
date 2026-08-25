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

"""Generated OPC UA commercial_kitchen namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as commercial_kitchen_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1002", browseName="ns=commercial_kitchen;BatchInformationType", displayName="BatchInformationType")
class BatchInformationType(ns0.objtypes.BaseObjectType):
    batchId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6002", browseName="ns=commercial_kitchen;BatchId", dataType=o6.String, accessLevel=3)
    )
    localTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6004", browseName="ns=commercial_kitchen;LocalTime", dataType=ns0.datatypes.TimeZoneDataType, accessLevel=3)
    )
    orderId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6001", browseName="ns=commercial_kitchen;OrderId", dataType=o6.String, accessLevel=3)
    )
    systemTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6003", browseName="ns=commercial_kitchen;SystemTime", dataType=ns0.datatypes.UtcTime, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1003", browseName="ns=commercial_kitchen;KitchenDeviceHAConfigType", displayName="KitchenDeviceHAConfigType")
class KitchenDeviceHAConfigType(ns0.objtypes.HistoricalDataConfigurationType):
    historyDuration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6005", browseName="ns=commercial_kitchen;HistoryDuration", dataType=ns0.datatypes.Duration, accessLevel=3)
    )
    samplingInterval: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6006", browseName="ns=commercial_kitchen;SamplingInterval", dataType=ns0.datatypes.Duration, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1004", browseName="ns=commercial_kitchen;KitchenDeviceParameterType", displayName="KitchenDeviceParameterType", isAbstract=True)
class KitchenDeviceParameterType(ns0.objtypes.BaseObjectType):
    programId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6007", browseName="ns=commercial_kitchen;ProgramId", dataType=o6.Int32, accessLevel=3)
    )
    programName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6008", browseName="ns=commercial_kitchen;ProgramName", dataType=o6.LocalizedText, accessLevel=3)
    )
    programUId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6009", browseName="ns=commercial_kitchen;ProgramUId", dataType=o6.Guid, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1005", browseName="ns=commercial_kitchen;CommercialKitchenDeviceType", displayName="CommercialKitchenDeviceType", isAbstract=True)
class CommercialKitchenDeviceType(di.objtypes.DeviceType):
    batchInformation: BatchInformationType | None
    deviceClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6015", browseName="ns=di;DeviceClass", description="Indicates in which domain or for what purpose a device is used.", dataType=o6.String
        )
    )
    deviceLocationName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6016", browseName="ns=commercial_kitchen;DeviceLocationName", dataType=o6.String)
    )
    errorConditions: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=commercial_kitchen;i=5002", browseName="ns=commercial_kitchen;ErrorConditions")
    )
    hACCPValues: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=commercial_kitchen;i=5004", browseName="ns=commercial_kitchen;HACCPValues")
    )
    informationConditions: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=commercial_kitchen;i=5003", browseName="ns=commercial_kitchen;InformationConditions")
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1013", browseName="ns=commercial_kitchen;OvenDeviceType", displayName="OvenDeviceType")
class OvenDeviceType(CommercialKitchenDeviceType):
    chamber_LangleNoDotRangle: ChamberType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1024", browseName="ns=commercial_kitchen;CoffeeMachineDeviceType", displayName="CoffeeMachineDeviceType")
class CoffeeMachineDeviceType(CommercialKitchenDeviceType):
    langleRecipeNameRangle: CoffeeMachineRecipeParameterType
    parameters: CoffeeMachineParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1026", browseName="ns=commercial_kitchen;DishWashingMachineDeviceType", displayName="DishWashingMachineDeviceType")
class DishWashingMachineDeviceType(CommercialKitchenDeviceType):
    parameters: DishWashingMachineProgramParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1028", browseName="ns=commercial_kitchen;ServeryCounterDeviceType", displayName="ServeryCounterDeviceType")
class ServeryCounterDeviceType(CommercialKitchenDeviceType):
    tray_LangleNoDotRangle: TrayType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1034", browseName="ns=commercial_kitchen;MicrowaveCombiOvenDeviceType", displayName="MicrowaveCombiOvenDeviceType")
class MicrowaveCombiOvenDeviceType(CommercialKitchenDeviceType):
    microwaveCombiOven: MicrowaveCombiOvenParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1006", browseName="ns=commercial_kitchen;FryerParameterType", displayName="FryerParameterType")
class FryerParameterType(KitchenDeviceParameterType):
    actualTemperature: ns0.vartypes.AnalogItemType
    isLiftUp: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6032", browseName="ns=commercial_kitchen;IsLiftUp", dataType=o6.Boolean)
    )
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6010", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.FryerModeEnumeration
        )
    )
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6031", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
        )
    )
    timeRemaining: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1007", browseName="ns=commercial_kitchen;FryerDeviceType", displayName="FryerDeviceType")
class FryerDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6038", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    fryerCup_LangleNoDotRangle: FryerParameterType
    isWithLift: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6037", browseName="ns=commercial_kitchen;IsWithLift", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1008", browseName="ns=commercial_kitchen;FryingPanParameterType", displayName="FryingPanParameterType")
class FryingPanParameterType(KitchenDeviceParameterType):
    actualCoreTemperature: ns0.vartypes.AnalogItemType
    actualPressurePan: ns0.vartypes.AnalogItemType | None
    actualTemperature: ns0.vartypes.AnalogItemType
    cookingLevel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6055", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)
    )
    isLidLocked: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6072", browseName="ns=commercial_kitchen;IsLidLocked", dataType=o6.Boolean)
    )
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6054", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.FryingPanModeEnumeration
        )
    )
    setCoreTemperature: ns0.vartypes.AnalogItemType
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6069", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
        )
    )
    timeRemaining: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1009", browseName="ns=commercial_kitchen;FryingPanDeviceType", displayName="FryingPanDeviceType")
class FryingPanDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6080", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    fryingPan: FryingPanParameterType
    isWithPressure: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6079", browseName="ns=commercial_kitchen;IsWithPressure", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1010", browseName="ns=commercial_kitchen;CombiSteamerParameterType", displayName="CombiSteamerParameterType")
class CombiSteamerParameterType(KitchenDeviceParameterType):
    actualExternalCoreTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualHumidity: ns0.vartypes.AnalogItemType | None
    actualInternalCoreTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualTemperatureChamber_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    combiSteamerMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6104", browseName="ns=commercial_kitchen;CombiSteamerMode", dataType=commercial_kitchen_datypes.CombiSteamerModeEnumeration
        )
    )
    isDoorOpen: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6130", browseName="ns=commercial_kitchen;IsDoorOpen", dataType=o6.Boolean)
    )
    isEnergySavingActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6131", browseName="ns=commercial_kitchen;IsEnergySavingActive", dataType=o6.Boolean)
    )
    isLoaActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6133", browseName="ns=commercial_kitchen;IsLoaActive", dataType=o6.Boolean)
    )
    isSteamExhaustSystemActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6132", browseName="ns=commercial_kitchen;IsSteamExhaustSystemActive", dataType=o6.Boolean, accessLevel=3)
    )
    setExternalCoreTemperature: ns0.vartypes.AnalogItemType | None
    setHumidity: ns0.vartypes.AnalogItemType | None
    setInternalCoreTemperature: ns0.vartypes.AnalogItemType | None
    setProcessTimeProgram: ns0.vartypes.AnalogItemType
    setProcessTimeStep: ns0.vartypes.AnalogItemType | None
    setTemperature: ns0.vartypes.AnalogItemType
    specialCookingMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6121", browseName="ns=commercial_kitchen;SpecialCookingMode", dataType=commercial_kitchen_datypes.SpecialCookingModeEnumeration
        )
    )
    timeRemainingProgram: ns0.vartypes.AnalogItemType
    timeRemainingStep: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1011", browseName="ns=commercial_kitchen;CombiSteamerDeviceType", displayName="CombiSteamerDeviceType")
class CombiSteamerDeviceType(CommercialKitchenDeviceType):
    combiSteamer: CombiSteamerParameterType
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6146", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    isWithAutomaticCleaning: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6147", browseName="ns=commercial_kitchen;IsWithAutomaticCleaning", dataType=o6.Boolean)
    )
    isWithExternalCoreTempSensor: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6149", browseName="ns=commercial_kitchen;IsWithExternalCoreTempSensor", dataType=o6.Boolean)
    )
    isWithInternalCoreTempSensor: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6148", browseName="ns=commercial_kitchen;IsWithInternalCoreTempSensor", dataType=o6.Boolean)
    )
    isWithSousvideTempSensor: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6150", browseName="ns=commercial_kitchen;IsWithSousvideTempSensor", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1012", browseName="ns=commercial_kitchen;ChamberType", displayName="ChamberType")
class ChamberType(KitchenDeviceParameterType):
    actualBoilerTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualBottomTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualChamberTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualCoreTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualFanSpeed_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualHumidity_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualTopTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    isDoorOpen: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6200", browseName="ns=commercial_kitchen;IsDoorOpen", dataType=o6.Boolean)
    )
    isProgramEnd: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6199", browseName="ns=commercial_kitchen;IsProgramEnd", dataType=o6.Boolean)
    )
    isReadyToStart: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6198", browseName="ns=commercial_kitchen;IsReadyToStart", dataType=o6.Boolean)
    )
    operationMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6169", browseName="ns=commercial_kitchen;OperationMode", dataType=commercial_kitchen_datypes.ChamberModeEnumeration
        )
    )
    setBoilerTemperature: ns0.vartypes.AnalogItemType | None
    setBottomTemperature: ns0.vartypes.AnalogItemType | None
    setChamberTemperature: ns0.vartypes.AnalogItemType | None
    setCoreTemperature: ns0.vartypes.AnalogItemType | None
    setFanSpeed: ns0.vartypes.AnalogItemType | None
    setHumidity: ns0.vartypes.AnalogItemType | None
    setProcessTimeProgram: ns0.vartypes.AnalogItemType | None
    setTopTemperature: ns0.vartypes.AnalogItemType | None
    timeRemaining: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1014", browseName="ns=commercial_kitchen;PressureCookingKettleParameterType", displayName="PressureCookingKettleParameterType")
class PressureCookingKettleParameterType(KitchenDeviceParameterType):
    actualCoreTemperature: ns0.vartypes.AnalogItemType
    actualPressureAbsolute: ns0.vartypes.AnalogItemType
    actualPressureKettle: ns0.vartypes.AnalogItemType
    actualTemperature: ns0.vartypes.AnalogItemType
    cookingLevel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6208", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)
    )
    isLidLocked: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6226", browseName="ns=commercial_kitchen;IsLidLocked", dataType=o6.Boolean)
    )
    isOpenExpressActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6228", browseName="ns=commercial_kitchen;IsOpenExpressActive", dataType=o6.Boolean)
    )
    isSteamActive: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6227", browseName="ns=commercial_kitchen;IsSteamActive", dataType=o6.Boolean)
    )
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6207", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.PressureCookingKettleModeEnumeration
        )
    )
    setCoreTemperature: ns0.vartypes.AnalogItemType
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6225", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
        )
    )
    timeRemaining: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1015", browseName="ns=commercial_kitchen;PressureCookingKettleDeviceType", displayName="PressureCookingKettleDeviceType")
class PressureCookingKettleDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6229", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    pressureCookingKettle: PressureCookingKettleParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1016", browseName="ns=commercial_kitchen;CookingKettleParameterType", displayName="CookingKettleParameterType")
class CookingKettleParameterType(KitchenDeviceParameterType):
    actualCoreTemperature: ns0.vartypes.AnalogItemType
    actualTemperature: ns0.vartypes.AnalogItemType
    cookingLevel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6252", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)
    )
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6103", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.CookingKettleModeEnumeration
        )
    )
    setCoreTemperature: ns0.vartypes.AnalogItemType
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6267", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
        )
    )
    timeRemaining: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1017", browseName="ns=commercial_kitchen;CookingKettleDeviceType", displayName="CookingKettleDeviceType")
class CookingKettleDeviceType(CommercialKitchenDeviceType):
    cookingKettle: CookingKettleParameterType
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6270", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    isWithAgitator: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6268", browseName="ns=commercial_kitchen;IsWithAgitator", dataType=o6.Boolean)
    )
    isWithCooling: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6269", browseName="ns=commercial_kitchen;IsWithCooling", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1018", browseName="ns=commercial_kitchen;MultiFunctionPanParameterType", displayName="MultiFunctionPanParameterType")
class MultiFunctionPanParameterType(KitchenDeviceParameterType):
    actualCoreTemperature: ns0.vartypes.AnalogItemType
    actualPressureAbsolute: ns0.vartypes.AnalogItemType | None
    actualTemperatureBottom: ns0.vartypes.AnalogItemType
    actualTemperatureCup: ns0.vartypes.AnalogItemType
    actualZoneTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    cookingLevel: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6290", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)
    )
    isLidLocked: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6315", browseName="ns=commercial_kitchen;IsLidLocked", dataType=o6.Boolean)
    )
    isLidOpen: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6316", browseName="ns=commercial_kitchen;IsLidOpen", dataType=o6.Boolean)
    )
    isWithCleaning: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6319", browseName="ns=commercial_kitchen;IsWithCleaning", dataType=o6.Boolean)
    )
    isWithLift: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6320", browseName="ns=commercial_kitchen;IsWithLift", dataType=o6.Boolean)
    )
    isWithPressure: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6317", browseName="ns=commercial_kitchen;IsWithPressure", dataType=o6.Boolean)
    )
    isWithTilting: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6318", browseName="ns=commercial_kitchen;IsWithTilting", dataType=o6.Boolean)
    )
    multiFunctionPanMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6288", browseName="ns=commercial_kitchen;MultiFunctionPanMode", dataType=commercial_kitchen_datypes.MultiFunctionPanModeEnumeration
        )
    )
    setCoreTemperature: ns0.vartypes.AnalogItemType
    setProcessTimeProgram: ns0.vartypes.AnalogItemType
    setProcessTimeStep: ns0.vartypes.AnalogItemType | None
    setTemperature: ns0.vartypes.AnalogItemType
    setZoneTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    specialFunctionMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6289", browseName="ns=commercial_kitchen;SpecialFunctionMode", dataType=commercial_kitchen_datypes.SpecialFunctionModeEnumeration
        )
    )
    timeRemainingProgram: ns0.vartypes.AnalogItemType
    timeRemainingStep: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1019", browseName="ns=commercial_kitchen;MultiFunctionPanDeviceType", displayName="MultiFunctionPanDeviceType")
class MultiFunctionPanDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6321", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    multiFunctionPan_LangleNoDotRangle: MultiFunctionPanParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1020", browseName="ns=commercial_kitchen;PastaCookerParameterType", displayName="PastaCookerParameterType")
class PastaCookerParameterType(KitchenDeviceParameterType):
    actualTemperature: ns0.vartypes.AnalogItemType
    cookingLevel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6339", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)
    )
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6338", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.PastaCookerModeEnumeration
        )
    )
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6348", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
        )
    )
    timeRemaining: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1021", browseName="ns=commercial_kitchen;PastaCookerDeviceType", displayName="PastaCookerDeviceType")
class PastaCookerDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6350", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    isWithLift: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6349", browseName="ns=commercial_kitchen;IsWithLift", dataType=o6.Boolean)
    )
    pastaCooker: PastaCookerParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1022", browseName="ns=commercial_kitchen;CoffeeMachineParameterType", displayName="CoffeeMachineParameterType")
class CoffeeMachineParameterType(KitchenDeviceParameterType):
    boilerPressureSteam: ns0.vartypes.AnalogItemType
    boilerPressureWater: ns0.vartypes.AnalogItemType
    boilerTempSteam: ns0.vartypes.AnalogItemType | None
    boilerTempWater: ns0.vartypes.AnalogItemType
    currentState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6368", browseName="ns=commercial_kitchen;CurrentState", dataType=commercial_kitchen_datypes.CoffeeMachineModeEnumeration, accessLevel=3
        )
    )
    grinderRuntime_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    systemClean: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6375", browseName="ns=commercial_kitchen;SystemClean", dataType=o6.DateTime)
    )
    totalBrew_LangleNoDotRangle: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6376", browseName="ns=commercial_kitchen;TotalBrew_<No.>", modellingRule="MandatoryPlaceholder", dataType=o6.UInt64
        )
    )
    totalMix: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6377", browseName="ns=commercial_kitchen;TotalMix", dataType=o6.UInt64)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1023", browseName="ns=commercial_kitchen;CoffeeMachineRecipeParameterType", displayName="CoffeeMachineRecipeParameterType")
class CoffeeMachineRecipeParameterType(KitchenDeviceParameterType):
    beverageSML: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6386", browseName="ns=commercial_kitchen;BeverageSML", dataType=commercial_kitchen_datypes.BeverageSMLEnumeration, accessLevel=3
        )
    )
    beverageSize: ns0.vartypes.AnalogItemType
    coffeeType: ns0.vartypes.MultiStateDiscreteType
    container: ns0.vartypes.MultiStateDiscreteType
    foamAmount: ns0.vartypes.AnalogItemType
    groundsAmount: ns0.vartypes.AnalogItemType
    groundsWater: ns0.vartypes.AnalogItemType
    milkAmount: ns0.vartypes.AnalogItemType
    powderAmount: ns0.vartypes.AnalogItemType
    rcpType: ns0.vartypes.MultiStateDiscreteType


@o6.objecttype(
    nodeId="ns=commercial_kitchen;i=1025", browseName="ns=commercial_kitchen;DishWashingMachineProgramParameterType", displayName="DishWashingMachineProgramParameterType"
)
class DishWashingMachineProgramParameterType(KitchenDeviceParameterType):
    actualFinalRinseTemperatureNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6469", browseName="ns=commercial_kitchen;ActualFinalRinseTemperatureNo", dataType=o6.UInt16)
    )
    actualFinalRinseTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    actualHygieneValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6473", browseName="ns=commercial_kitchen;ActualHygieneValue", dataType=o6.UInt16)
    )
    actualMainTankTemperatureNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6463", browseName="ns=commercial_kitchen;ActualMainTankTemperatureNo", dataType=o6.UInt16)
    )
    actualMainTankTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    actualPreTankTemperatureNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6460", browseName="ns=commercial_kitchen;ActualPreTankTemperatureNo", dataType=o6.UInt16)
    )
    actualPreTankTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    actualPumpedFinalRinseTemperatureNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6466", browseName="ns=commercial_kitchen;ActualPumpedFinalRinseTemperatureNo", dataType=o6.UInt16)
    )
    actualPumpedFinalRinseTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    finalRinseTemperatureSetpointNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6457", browseName="ns=commercial_kitchen;FinalRinseTemperatureSetpointNo", dataType=o6.UInt16)
    )
    finalRinseTemperatureSetpoint_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    hygieneMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6475", browseName="ns=commercial_kitchen;HygieneMode", dataType=commercial_kitchen_datypes.HygieneModeEnumeration
        )
    )
    hygieneSetpoint: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6472", browseName="ns=commercial_kitchen;HygieneSetpoint", dataType=o6.UInt16)
    )
    mainTankTemperatureSetpointNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6451", browseName="ns=commercial_kitchen;MainTankTemperatureSetpointNo", dataType=o6.UInt16)
    )
    mainTankTemperatureSetpoint_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    operationMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6476", browseName="ns=commercial_kitchen;OperationMode", dataType=commercial_kitchen_datypes.OperationModeEnumeration
        )
    )
    preTankTemperatureSetpointNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6448", browseName="ns=commercial_kitchen;PreTankTemperatureSetpointNo", dataType=o6.UInt16)
    )
    preTankTemperatureSetpoint_LangleNoDotRangle: ns0.vartypes.AnalogItemType
    productGroup: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6446", browseName="ns=commercial_kitchen;ProductGroup", dataType=o6.String)
    )
    productType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6447", browseName="ns=commercial_kitchen;ProductType", dataType=o6.UInt32)
    )
    programMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6474", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.ProgramModeEnumeration
        )
    )
    pumpedFinalRinseTemperatureSetpointNo: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6454", browseName="ns=commercial_kitchen;PumpedFinalRinseTemperatureSetpointNo", dataType=o6.UInt16)
    )
    pumpedFinalRinseTemperatureSetpoint_LangleNoDotRangle: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1027", browseName="ns=commercial_kitchen;TrayType", displayName="TrayType")
class TrayType(KitchenDeviceParameterType):
    activeSince: ns0.vartypes.AnalogItemType
    actualTemperature: ns0.vartypes.AnalogItemType
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6504", browseName="ns=commercial_kitchen;Name", dataType=o6.String, accessLevel=3)
    )
    operatingCounter: ns0.vartypes.AnalogItemType
    programMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6499", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.TrayModeEnumeration, accessLevel=3
        )
    )
    setTemperature: ns0.vartypes.AnalogItemType
    type: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6505", browseName="ns=commercial_kitchen;Type", dataType=commercial_kitchen_datypes.TrayTypeEnumeration)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1029", browseName="ns=commercial_kitchen;CookingZoneParameterType", displayName="CookingZoneParameterType")
class CookingZoneParameterType(KitchenDeviceParameterType):
    actualPower: ns0.vartypes.AnalogItemType | None
    actualProcessTime: ns0.vartypes.AnalogItemType | None
    actualTemperature: ns0.vartypes.AnalogItemType | None
    cookingZoneName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6531", browseName="ns=commercial_kitchen;CookingZoneName", dataType=o6.String)
    )
    currentState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6530", browseName="ns=commercial_kitchen;CurrentState", dataType=commercial_kitchen_datypes.CurrentStateEnumeration
        )
    )
    isPanDetected: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6542", browseName="ns=commercial_kitchen;IsPanDetected", dataType=o6.Boolean)
    )
    nominalPower: ns0.vartypes.AnalogItemType
    setPowerValue: ns0.vartypes.AnalogItemType | None
    setTemperature: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1030", browseName="ns=commercial_kitchen;CookingZoneDeviceType", displayName="CookingZoneDeviceType")
class CookingZoneDeviceType(CommercialKitchenDeviceType):
    cookingZone_LangleNoDotRangle: CookingZoneParameterType
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6552", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    isWithPanDetection: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6551", browseName="ns=commercial_kitchen;IsWithPanDetection", dataType=o6.Boolean)
    )
    nominalVoltage: ns0.vartypes.AnalogItemType
    numberOfPhases: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6555", browseName="ns=commercial_kitchen;NumberOfPhases", dataType=o6.Int32)
    )


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1031", browseName="ns=commercial_kitchen;FryingAndGrillingParameterType", displayName="FryingAndGrillingParameterType")
class FryingAndGrillingParameterType(KitchenDeviceParameterType):
    actualGrillTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    actualPlatenTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    currentState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6558", browseName="ns=commercial_kitchen;CurrentState", dataType=commercial_kitchen_datypes.GrillingZoneStateEnumeration
        )
    )
    grillingZoneName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6559", browseName="ns=commercial_kitchen;GrillingZoneName", dataType=o6.String)
    )
    isWithPlaten: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6573", browseName="ns=commercial_kitchen;IsWithPlaten", dataType=o6.Boolean)
    )
    platenPositionState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6572", browseName="ns=commercial_kitchen;PlatenPositionState", dataType=commercial_kitchen_datypes.PlatenPositionStateEnumeration
        )
    )
    remainingProcessTime: ns0.vartypes.AnalogItemType | None
    setGrillTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    setPlatenTemperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    setProcessTime: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1032", browseName="ns=commercial_kitchen;FryingAndGrillingDeviceType", displayName="FryingAndGrillingDeviceType")
class FryingAndGrillingDeviceType(CommercialKitchenDeviceType):
    energySource: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=commercial_kitchen;i=6580", browseName="ns=commercial_kitchen;EnergySource", dataType=commercial_kitchen_datypes.EnergySourceEnumeration
        )
    )
    grillingZone_LangleNoDotRangle: FryingAndGrillingParameterType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1033", browseName="ns=commercial_kitchen;MicrowaveCombiOvenParameterType", displayName="MicrowaveCombiOvenParameterType")
class MicrowaveCombiOvenParameterType(KitchenDeviceParameterType):
    actualTemperatureChamber: ns0.vartypes.AnalogItemType
    cookingStep: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6592", browseName="ns=commercial_kitchen;CookingStep", dataType=o6.Int32)
    )
    fanSpeed: ns0.vartypes.AnalogItemType | None
    isDoorOpen: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6598", browseName="ns=commercial_kitchen;IsDoorOpen", dataType=o6.Boolean, accessLevel=3)
    )
    microwaveEnergy: ns0.vartypes.AnalogItemType | None
    operatingMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=commercial_kitchen;i=6597", browseName="ns=commercial_kitchen;OperatingMode", dataType=commercial_kitchen_datypes.OperatingModeEnumeration
        )
    )
    remainingProcessTime: ns0.vartypes.AnalogItemType
    remainingProcessTimeStep: ns0.vartypes.AnalogItemType | None
    setProcessTime: ns0.vartypes.AnalogItemType
    setTemperature: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1035", browseName="ns=commercial_kitchen;IceMachineParameterType", displayName="IceMachineParameterType")
class IceMachineParameterType(KitchenDeviceParameterType):
    lastFreezeTime: ns0.vartypes.AnalogItemType | None
    lastHarvestTime: ns0.vartypes.AnalogItemType | None
    status: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6621", browseName="ns=commercial_kitchen;Status", dataType=commercial_kitchen_datypes.StatusEnumeration)
    )
    temperature_LangleNoDotRangle: ns0.vartypes.AnalogItemType | None
    waterFillTime: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=commercial_kitchen;i=1036", browseName="ns=commercial_kitchen;IceMachineDeviceType", displayName="IceMachineDeviceType")
class IceMachineDeviceType(CommercialKitchenDeviceType):
    iceMachine: IceMachineParameterType = o6.hasComponent(IceMachineParameterType(nodeId="ns=commercial_kitchen;i=5020", browseName="ns=commercial_kitchen;IceMachine"))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, commercial_kitchen_datypes
