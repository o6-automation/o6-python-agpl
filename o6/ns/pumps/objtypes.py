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

"""Generated OPC UA pumps namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as pumps_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=pumps;i=1002",
    browseName="ns=pumps;MarkingsType",
    displayName="MarkingsType",
    description="Safety instructions for safe use, e.g. temperature and pressure resistance, electrostatic charge, high voltage, radioactivity, explosive protection.",
)
class MarkingsType(ns0.objtypes.FolderType):
    langleMarkingRangle: ns0.objtypes.FileType | None


@o6.objecttype(nodeId="ns=pumps;i=1006", browseName="ns=pumps;DocumentationType", displayName="DocumentationType")
class DocumentationType(di.objtypes.FunctionalGroupType):
    arrangements: ns0.objtypes.FileType | None
    arrangementsLink: ns0.vartypes.DataItemType | None
    certificates: ns0.objtypes.FileType | None
    certificatesLink: ns0.vartypes.DataItemType | None
    circuitDiagram: ns0.objtypes.FileType | None
    circuitDiagramLink: ns0.vartypes.DataItemType | None
    componentsList: ns0.objtypes.FileType | None
    componentsListLink: ns0.vartypes.DataItemType | None
    detail: ns0.objtypes.FileType | None
    detailLink: ns0.vartypes.DataItemType | None
    duringMaintenanceServicesRendered: ns0.objtypes.FileType | None
    duringMaintenanceServicesRenderedLink: ns0.vartypes.DataItemType | None
    implementationDescription: ns0.objtypes.FileType | None
    implementationDescriptionLink: ns0.vartypes.DataItemType | None
    layout: ns0.objtypes.FileType | None
    layoutLink: ns0.vartypes.DataItemType | None
    location: ns0.objtypes.FileType | None
    locationLink: ns0.vartypes.DataItemType | None
    logicDiagram: ns0.objtypes.FileType | None
    logicDiagramLink: ns0.vartypes.DataItemType | None
    lubricationMap: ns0.objtypes.FileType | None
    lubricationMapLink: ns0.vartypes.DataItemType | None
    maintenanceManual: ns0.objtypes.FileType | None
    maintenanceManualLink: ns0.vartypes.DataItemType | None
    operationManual: ns0.objtypes.FileType | None
    operationManualLink: ns0.vartypes.DataItemType | None
    personnelRecording: ns0.objtypes.FileType | None
    personnelRecordingLink: ns0.vartypes.DataItemType | None
    pipeAndInstrumentDiagram: ns0.objtypes.FileType | None
    pipeAndInstrumentDiagramLink: ns0.vartypes.DataItemType | None
    scopeOfWork: ns0.objtypes.FileType | None
    scopeOfWorkLink: ns0.vartypes.DataItemType | None
    singleLineDiagram: ns0.objtypes.FileType | None
    singleLineDiagramLink: ns0.vartypes.DataItemType | None
    sparePartReference: ns0.objtypes.FileType | None
    sparePartReferenceLink: ns0.vartypes.DataItemType | None
    staff: ns0.objtypes.FileType | None
    staffLink: ns0.vartypes.DataItemType | None
    technicalData: ns0.objtypes.FileType | None
    technicalDataLink: ns0.vartypes.DataItemType | None
    testProgramReport: ns0.objtypes.FileType | None
    testProgramReportLink: ns0.vartypes.DataItemType | None
    unitMaintenanceReport: ns0.objtypes.FileType | None
    unitMaintenanceReportLink: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1007", browseName="ns=pumps;GeneralMaintenanceType", displayName="GeneralMaintenanceType")
class GeneralMaintenanceType(di.objtypes.FunctionalGroupType):
    activeMaintenanceTime: ns0.vartypes.BaseAnalogType | None
    downTime: ns0.vartypes.BaseAnalogType | None
    externalDisabledTime: ns0.vartypes.BaseAnalogType | None
    failureRate: ns0.vartypes.BaseAnalogType | None
    idleTime: ns0.vartypes.BaseAnalogType | None
    maintenanceLevel: ns0.vartypes.DataItemType | None
    maintenanceTime: ns0.vartypes.BaseAnalogType | None
    meanOperatingTimeBetweenFailures: ns0.vartypes.BaseAnalogType | None
    meanRepairTime: ns0.vartypes.BaseAnalogType | None
    meanTimeToRestauration: ns0.vartypes.BaseAnalogType | None
    obsolescence: ns0.vartypes.TwoStateDiscreteType | None
    operatingTime: ns0.vartypes.BaseAnalogType | None
    operatingTimeBetweenFailures: ns0.vartypes.BaseAnalogType | None
    operatingTimeToFailure: ns0.vartypes.BaseAnalogType | None
    repairTime: ns0.vartypes.BaseAnalogType | None
    standbyTime: ns0.vartypes.BaseAnalogType | None
    stateOfTheItem: ns0.vartypes.DataItemType | None
    timeBetweenFailures: ns0.vartypes.BaseAnalogType | None
    timeToRestoration: ns0.vartypes.BaseAnalogType | None
    upTime: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1008", browseName="ns=pumps;ConditionBasedMaintenanceType", displayName="ConditionBasedMaintenanceType")
class ConditionBasedMaintenanceType(di.objtypes.FunctionalGroupType):
    availability: ns0.vartypes.BaseAnalogType | None
    durability: ns0.vartypes.BaseAnalogType | None
    expectedReliability: ns0.vartypes.BaseAnalogType | None
    instantaneousAvailability: ns0.vartypes.BaseAnalogType | None
    intrinsicMaintainability: ns0.vartypes.BaseAnalogType | None
    intrinsicReliability: ns0.vartypes.BaseAnalogType | None
    maintainability: ns0.vartypes.BaseAnalogType | None
    operationalReliability: ns0.vartypes.BaseAnalogType | None
    productionBasedAvailability: ns0.vartypes.BaseAnalogType | None
    reliability: ns0.vartypes.BaseAnalogType | None
    timeBasedAvailability: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1009", browseName="ns=pumps;PreventiveMaintenanceType", displayName="PreventiveMaintenanceType")
class PreventiveMaintenanceType(di.objtypes.FunctionalGroupType):
    activePreventiveMaintenanceTime: ns0.vartypes.BaseAnalogType | None
    installationDate: ns0.vartypes.DataItemType | None
    lastInspectionDate: ns0.vartypes.DataItemType | None
    lastServicingDate: ns0.vartypes.DataItemType | None
    nextInspectionDate: ns0.vartypes.DataItemType | None
    nextServicingDate: ns0.vartypes.DataItemType | None
    preventiveMaintenanceTime: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1010", browseName="ns=pumps;BreakdownMaintenanceType", displayName="BreakdownMaintenanceType")
class BreakdownMaintenanceType(di.objtypes.FunctionalGroupType):
    correctiveMaintenanceTime: ns0.vartypes.BaseAnalogType | None
    criticality: ns0.vartypes.BaseAnalogType | None
    failure: ns0.vartypes.TwoStateDiscreteType | None
    numberOfFailures: ns0.vartypes.BaseAnalogType | None
    severity: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1011", browseName="ns=pumps;MaintenanceGroupType", displayName="MaintenanceGroupType")
class MaintenanceGroupType(di.objtypes.FunctionalGroupType):
    breakdownMaintenance: BreakdownMaintenanceType | None
    conditionBasedMaintenance: ConditionBasedMaintenanceType | None
    generalMaintenance: GeneralMaintenanceType | None
    preventiveMaintenance: PreventiveMaintenanceType | None


@o6.objecttype(
    nodeId="ns=pumps;i=1012",
    browseName="ns=pumps;SupervisionMechanicsType",
    displayName="SupervisionMechanicsType",
    description="Supervision mechanics specifies supervising information related to device mechanics.",
)
class SupervisionMechanicsType(di.objtypes.FunctionalGroupType):
    axialBearingAbrasion: ns0.vartypes.TwoStateDiscreteType | None
    axialBearingFault: ns0.vartypes.TwoStateDiscreteType | None
    axialBearingOverheat: ns0.vartypes.TwoStateDiscreteType | None
    bearingFault: ns0.vartypes.TwoStateDiscreteType | None
    brakeChopper: ns0.vartypes.TwoStateDiscreteType | None
    brakeOverheat: ns0.vartypes.TwoStateDiscreteType | None
    excessVibration: ns0.vartypes.TwoStateDiscreteType | None
    gapWear: ns0.vartypes.TwoStateDiscreteType | None
    mechanicalFault: ns0.vartypes.TwoStateDiscreteType | None
    misalignment: ns0.vartypes.TwoStateDiscreteType | None
    radialBearingAbrasion: ns0.vartypes.TwoStateDiscreteType | None
    radialBearingFault: ns0.vartypes.TwoStateDiscreteType | None
    radialBearingOverheat: ns0.vartypes.TwoStateDiscreteType | None
    rotorBlocked: ns0.vartypes.TwoStateDiscreteType | None
    rotorStationRubbing: ns0.vartypes.TwoStateDiscreteType | None
    unbalance: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionMechanicsType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionMechanicsType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionMechanicsType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionMechanicsType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1013",
    browseName="ns=pumps;SupervisionHardwareType",
    displayName="SupervisionHardwareType",
    description="Supervision hardware specifies supervising information related to device hardware.",
)
class SupervisionHardwareType(di.objtypes.FunctionalGroupType):
    communication: ns0.vartypes.TwoStateDiscreteType | None
    computingCircuit: ns0.vartypes.TwoStateDiscreteType | None
    controlCircuit: ns0.vartypes.TwoStateDiscreteType | None
    dCLinkSupply: ns0.vartypes.TwoStateDiscreteType | None
    eprom: ns0.vartypes.TwoStateDiscreteType | None
    hardwareFault: ns0.vartypes.TwoStateDiscreteType | None
    iONA: ns0.vartypes.TwoStateDiscreteType | None
    measureCircuit: ns0.vartypes.TwoStateDiscreteType | None
    microProcessor: ns0.vartypes.TwoStateDiscreteType | None
    networkNA: ns0.vartypes.TwoStateDiscreteType | None
    powerSupply: ns0.vartypes.TwoStateDiscreteType | None
    ram: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionHardwareType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionHardwareType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionHardwareType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionHardwareType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1014",
    browseName="ns=pumps;SupervisionSoftwareType",
    displayName="SupervisionSoftwareType",
    description="Supervision software specifies supervising information related to device software.",
)
class SupervisionSoftwareType(di.objtypes.FunctionalGroupType):
    application: ns0.vartypes.TwoStateDiscreteType | None
    communication: ns0.vartypes.TwoStateDiscreteType | None
    control: ns0.vartypes.TwoStateDiscreteType | None
    memory: ns0.vartypes.TwoStateDiscreteType | None
    oS: ns0.vartypes.TwoStateDiscreteType | None
    parameter: ns0.vartypes.TwoStateDiscreteType | None
    softwareFault: ns0.vartypes.TwoStateDiscreteType | None
    softwareReset: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionSoftwareType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionSoftwareType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionSoftwareType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionSoftwareType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1015",
    browseName="ns=pumps;SupervisionProcessFluidType",
    displayName="SupervisionProcessFluidType",
    description="Supervision process fluid specifies information for monitoring the fluid of a pump.",
)
class SupervisionProcessFluidType(di.objtypes.FunctionalGroupType):
    blockage: ns0.vartypes.TwoStateDiscreteType | None
    cavitation: ns0.vartypes.TwoStateDiscreteType | None
    condensation: ns0.vartypes.TwoStateDiscreteType | None
    dry: ns0.vartypes.TwoStateDiscreteType | None
    flow: ns0.vartypes.TwoStateDiscreteType | None
    gas: ns0.vartypes.TwoStateDiscreteType | None
    liquid: ns0.vartypes.TwoStateDiscreteType | None
    pressure: ns0.vartypes.TwoStateDiscreteType | None
    processFault: ns0.vartypes.TwoStateDiscreteType | None
    solid: ns0.vartypes.TwoStateDiscreteType | None
    stall: ns0.vartypes.TwoStateDiscreteType | None
    temperature: ns0.vartypes.TwoStateDiscreteType | None
    viscosity: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionProcessFluidType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionProcessFluidType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionProcessFluidType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionProcessFluidType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1016",
    browseName="ns=pumps;SupervisionPumpOperationType",
    displayName="SupervisionPumpOperationType",
    description="Supervision pump operation specifies information for monitoring the pump operation.",
)
class SupervisionPumpOperationType(di.objtypes.FunctionalGroupType):
    accessoryLiquidFlow: ns0.vartypes.TwoStateDiscreteType | None
    accessoryLiquidHigh: ns0.vartypes.TwoStateDiscreteType | None
    accessoryLiquidLow: ns0.vartypes.TwoStateDiscreteType | None
    accessoryLiquidOverheat: ns0.vartypes.TwoStateDiscreteType | None
    accessoryLiquidPressure: ns0.vartypes.TwoStateDiscreteType | None
    ambientTemperature: ns0.vartypes.TwoStateDiscreteType | None
    caseOverheat: ns0.vartypes.TwoStateDiscreteType | None
    controllerOverheat: ns0.vartypes.TwoStateDiscreteType | None
    converterOverheat: ns0.vartypes.TwoStateDiscreteType | None
    coolantFlow: ns0.vartypes.TwoStateDiscreteType | None
    coolantHigh: ns0.vartypes.TwoStateDiscreteType | None
    coolantLow: ns0.vartypes.TwoStateDiscreteType | None
    coolantOverheat: ns0.vartypes.TwoStateDiscreteType | None
    deceleration: ns0.vartypes.TwoStateDiscreteType | None
    dirtyImpeller: ns0.vartypes.TwoStateDiscreteType | None
    driveOverheat: ns0.vartypes.TwoStateDiscreteType | None
    generatorOperation: ns0.vartypes.TwoStateDiscreteType | None
    leakage: ns0.vartypes.TwoStateDiscreteType | None
    lubricant: ns0.vartypes.TwoStateDiscreteType | None
    maximumNumberStarts: ns0.vartypes.TwoStateDiscreteType | None
    maximumOperationTime: ns0.vartypes.TwoStateDiscreteType | None
    maximumStartsAtTime: ns0.vartypes.TwoStateDiscreteType | None
    motorHumidity: ns0.vartypes.TwoStateDiscreteType | None
    motorOverheat: ns0.vartypes.TwoStateDiscreteType | None
    operationFault: ns0.vartypes.TwoStateDiscreteType | None
    overLoad: ns0.vartypes.TwoStateDiscreteType | None
    overSpeed: ns0.vartypes.TwoStateDiscreteType | None
    partialLoad: ns0.vartypes.TwoStateDiscreteType | None
    synchronisation: ns0.vartypes.TwoStateDiscreteType | None
    tMSFailure: ns0.vartypes.TwoStateDiscreteType | None
    temperatureFault: ns0.vartypes.TwoStateDiscreteType | None
    timeOut: ns0.vartypes.TwoStateDiscreteType | None
    torqueLimit: ns0.vartypes.TwoStateDiscreteType | None
    turbineOperation: ns0.vartypes.TwoStateDiscreteType | None
    underSpeed: ns0.vartypes.TwoStateDiscreteType | None
    velocityLimit: ns0.vartypes.TwoStateDiscreteType | None
    wearReserveExhausted: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionPumpOperationType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionPumpOperationType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionPumpOperationType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionPumpOperationType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1017",
    browseName="ns=pumps;SupervisionAuxiliaryDeviceType",
    displayName="SupervisionAuxiliaryDeviceType",
    description="Supervision auxiliary device specifies information for monitoring an additional device.",
)
class SupervisionAuxiliaryDeviceType(di.objtypes.FunctionalGroupType):
    actuatorElement: ns0.vartypes.TwoStateDiscreteType | None
    ambientTemperature: ns0.vartypes.TwoStateDiscreteType | None
    auxiliaryDeviceFault: ns0.vartypes.TwoStateDiscreteType | None
    auxiliaryMediumAbsence: ns0.vartypes.TwoStateDiscreteType | None
    auxiliaryMediumInsufficiency: ns0.vartypes.TwoStateDiscreteType | None
    auxiliaryPowerPole: ns0.vartypes.TwoStateDiscreteType | None
    auxiliaryPowerRange: ns0.vartypes.TwoStateDiscreteType | None
    communicationError: ns0.vartypes.TwoStateDiscreteType | None
    corrosion: ns0.vartypes.TwoStateDiscreteType | None
    deviation: ns0.vartypes.TwoStateDiscreteType | None
    electromagneticInterference: ns0.vartypes.TwoStateDiscreteType | None
    electronicFault: ns0.vartypes.TwoStateDiscreteType | None
    energySupply: ns0.vartypes.TwoStateDiscreteType | None
    evaluationElectronics: ns0.vartypes.TwoStateDiscreteType | None
    exciterError: ns0.vartypes.TwoStateDiscreteType | None
    fouling: ns0.vartypes.TwoStateDiscreteType | None
    humidityElectronics: ns0.vartypes.TwoStateDiscreteType | None
    installation: ns0.vartypes.TwoStateDiscreteType | None
    interruption: ns0.vartypes.TwoStateDiscreteType | None
    lineLength: ns0.vartypes.TwoStateDiscreteType | None
    materialElectronics: ns0.vartypes.TwoStateDiscreteType | None
    measuredMaterialElectronics: ns0.vartypes.TwoStateDiscreteType | None
    mechanicalDamage: ns0.vartypes.TwoStateDiscreteType | None
    operatingConditions: ns0.vartypes.TwoStateDiscreteType | None
    other: ns0.vartypes.TwoStateDiscreteType | None
    overloading: ns0.vartypes.TwoStateDiscreteType | None
    parameterSetting: ns0.vartypes.TwoStateDiscreteType | None
    peripheral: ns0.vartypes.TwoStateDiscreteType | None
    processInfluence: ns0.vartypes.TwoStateDiscreteType | None
    sensorElement: ns0.vartypes.TwoStateDiscreteType | None
    startUp: ns0.vartypes.TwoStateDiscreteType | None
    temperatureShock: ns0.vartypes.TwoStateDiscreteType | None
    vibration: ns0.vartypes.TwoStateDiscreteType | None
    wearReserveOperation: ns0.vartypes.TwoStateDiscreteType | None
    wearReserveWear: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionAuxiliaryDeviceType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionAuxiliaryDeviceType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionAuxiliaryDeviceType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionAuxiliaryDeviceType, "i=41", "ns=di;i=15739")


@o6.objecttype(
    nodeId="ns=pumps;i=1018",
    browseName="ns=pumps;SupervisionElectronicsType",
    displayName="SupervisionElectronicsType",
    description="Supervision Electrics specifies information for monitoring the electronics.",
)
class SupervisionElectronicsType(di.objtypes.FunctionalGroupType):
    armatureCircuit: ns0.vartypes.TwoStateDiscreteType | None
    currentInsideDevice: ns0.vartypes.TwoStateDiscreteType | None
    electricalFault: ns0.vartypes.TwoStateDiscreteType | None
    fieldCircuit: ns0.vartypes.TwoStateDiscreteType | None
    installationFault: ns0.vartypes.TwoStateDiscreteType | None
    insulationResistance: ns0.vartypes.TwoStateDiscreteType | None
    phaseFailure: ns0.vartypes.TwoStateDiscreteType | None
    shortCircuit: ns0.vartypes.TwoStateDiscreteType | None
    shortToEarth: ns0.vartypes.TwoStateDiscreteType | None
    supplyCurrent: ns0.vartypes.TwoStateDiscreteType | None
    supplyCurrentHigh: ns0.vartypes.TwoStateDiscreteType | None
    supplyCurrentLow: ns0.vartypes.TwoStateDiscreteType | None
    supplyFrequency: ns0.vartypes.TwoStateDiscreteType | None
    supplyFrequencyHigh: ns0.vartypes.TwoStateDiscreteType | None
    supplyFrequencyLow: ns0.vartypes.TwoStateDiscreteType | None
    supplyVoltage: ns0.vartypes.TwoStateDiscreteType | None
    supplyVoltageHigh: ns0.vartypes.TwoStateDiscreteType | None
    supplyVoltageLow: ns0.vartypes.TwoStateDiscreteType | None
    voltageInsideDevice: ns0.vartypes.TwoStateDiscreteType | None
    windingTemperature: ns0.vartypes.TwoStateDiscreteType | None


o6.reference(SupervisionElectronicsType, "i=41", "ns=di;i=15292")
o6.reference(SupervisionElectronicsType, "i=41", "ns=di;i=15441")
o6.reference(SupervisionElectronicsType, "i=41", "ns=di;i=15590")
o6.reference(SupervisionElectronicsType, "i=41", "ns=di;i=15739")


@o6.objecttype(nodeId="ns=pumps;i=1019", browseName="ns=pumps;SupervisionType", displayName="SupervisionType")
class SupervisionType(di.objtypes.FunctionalGroupType):
    supervisionAuxiliaryDevice: SupervisionAuxiliaryDeviceType | None
    supervisionElectronics: SupervisionElectronicsType | None
    supervisionHardware: SupervisionHardwareType | None
    supervisionMechanics: SupervisionMechanicsType | None
    supervisionProcessFluid: SupervisionProcessFluidType | None
    supervisionPumpOperation: SupervisionPumpOperationType | None
    supervisionSoftware: SupervisionSoftwareType | None


@o6.objecttype(nodeId="ns=pumps;i=1020", browseName="ns=pumps;DesignType", displayName="DesignType")
class DesignType(di.objtypes.FunctionalGroupType):
    additionalFieldbuses: ns0.vartypes.DataItemType | None
    balancingRateOfFlow: ns0.vartypes.BaseAnalogType | None
    basePressure: ns0.vartypes.BaseAnalogType | None
    clearanceVolume: ns0.vartypes.BaseAnalogType | None
    clockwiseRotation: ns0.vartypes.TwoStateDiscreteType | None
    controllable: ns0.vartypes.TwoStateDiscreteType | None
    cool_DownTimeForAVaporJetPumpOrADiffusionPump: ns0.vartypes.BaseAnalogType | None
    counter_ClockwiseRotation: ns0.vartypes.TwoStateDiscreteType | None
    criticalSpeed: ns0.vartypes.BaseAnalogType | None
    declarationOfConformity: ns0.vartypes.DataItemType | None
    declarationOfConformityAvailable: ns0.vartypes.TwoStateDiscreteType | None
    designAxialLoad: ns0.vartypes.BaseAnalogType | None
    designRadialLoad: ns0.vartypes.BaseAnalogType | None
    directivesOfEUDeclarationOfConformity: ns0.vartypes.DataItemType | None
    dryCriticalSpeed: ns0.vartypes.BaseAnalogType | None
    explosionProtection: ns0.vartypes.DataItemType | None
    geometricDisplacementVolume: ns0.vartypes.BaseAnalogType | None
    geometricalFlow: ns0.vartypes.BaseAnalogType | None
    headAtPeakPoint: ns0.vartypes.BaseAnalogType | None
    installationNpshCurve: ns0.objtypes.FileType | None
    leakageRateOfFlow: ns0.vartypes.BaseAnalogType | None
    maximumAllowableAmbientTemperature: ns0.vartypes.BaseAnalogType | None
    maximumAllowableCasingWorkingPressure: ns0.vartypes.BaseAnalogType | None
    maximumAllowableContinuousSpeed: ns0.vartypes.BaseAnalogType | None
    maximumAllowableHead: ns0.vartypes.BaseAnalogType | None
    maximumAllowableRelativeHumidity: ns0.vartypes.BaseAnalogType | None
    maximumAllowableTemperature: ns0.vartypes.BaseAnalogType | None
    maximumAllowableThroughput: ns0.vartypes.BaseAnalogType | None
    maximumAllowableWorkingPressure: ns0.vartypes.BaseAnalogType | None
    maximumAxialLoad: ns0.vartypes.BaseAnalogType | None
    maximumPumpPowerInput: ns0.vartypes.BaseAnalogType | None
    maximumRadialLoad: ns0.vartypes.BaseAnalogType | None
    maximumStaticSealingPressure: ns0.vartypes.BaseAnalogType | None
    meanTimebetweenFailures: ns0.vartypes.BaseAnalogType | None
    minimumAllowableAmbientTemperature: ns0.vartypes.BaseAnalogType | None
    minimumAllowableContinuousSpeed: ns0.vartypes.BaseAnalogType | None
    minimumAllowableHead: ns0.vartypes.BaseAnalogType | None
    minimumAllowableRelativeHumidity: ns0.vartypes.BaseAnalogType | None
    minimumAllowableTemperature: ns0.vartypes.BaseAnalogType | None
    minimumAllowableThermalFlow: ns0.vartypes.BaseAnalogType | None
    minimumContinuousStableFlow: ns0.vartypes.BaseAnalogType | None
    minimumContinuousThermalFlow: ns0.vartypes.BaseAnalogType | None
    netPositiveSuctionHeadRequired: ns0.vartypes.BaseAnalogType | None
    netPositiveSuctionHeadRequiredForADropOf3Percent: ns0.vartypes.BaseAnalogType | None
    offeredControlModes: ns0.vartypes.DataItemType | None
    offeredFieldbuses: ns0.vartypes.DataItemType | None
    optimumHead: ns0.vartypes.BaseAnalogType | None
    optimumPumpPowerInput: ns0.vartypes.BaseAnalogType | None
    optimumRateOfFlow: ns0.vartypes.BaseAnalogType | None
    pistonVelocity: ns0.vartypes.BaseAnalogType | None
    possibleFluids: ns0.vartypes.DataItemType | None
    pre_ChargePressure: ns0.vartypes.BaseAnalogType | None
    pumpClass: ns0.vartypes.DataItemType | None
    pumpCurve: ns0.objtypes.FileType | None
    pumpEfficiencyCurve: ns0.objtypes.FileType | None
    pumpH_Q_Curve: ns0.objtypes.FileType | None
    pumpNpshCurve: ns0.objtypes.FileType | None
    pumpPowerInputCurve: ns0.objtypes.FileType | None
    shut_OffHead: ns0.vartypes.BaseAnalogType | None
    shut_OffPumpPowerInput: ns0.vartypes.BaseAnalogType | None
    slipFlow: ns0.vartypes.BaseAnalogType | None
    soundEnergy: ns0.vartypes.BaseAnalogType | None
    soundEnergyLevel: ns0.vartypes.BaseAnalogType | None
    soundPower: ns0.vartypes.BaseAnalogType | None
    soundPowerLevel: ns0.vartypes.BaseAnalogType | None
    soundPressure: ns0.vartypes.BaseAnalogType | None
    soundPressureLevel: ns0.vartypes.BaseAnalogType | None
    specificSpeed: ns0.vartypes.BaseAnalogType | None
    stablePumpH_Q_Curve: ns0.objtypes.FileType | None
    standardGasFlowrate: ns0.vartypes.BaseAnalogType | None
    startingPressure: ns0.vartypes.BaseAnalogType | None
    suction_SpecificSpeed: ns0.vartypes.BaseAnalogType | None
    sweptVolume: ns0.vartypes.BaseAnalogType | None
    tripSpeed: ns0.vartypes.BaseAnalogType | None
    typeNumber: ns0.vartypes.DataItemType | None
    volumeFlowRate: ns0.vartypes.BaseAnalogType | None
    volumeFlowRateOfBackingPump: ns0.vartypes.BaseAnalogType | None
    warmUpTimeForAVaporJetPumpOrADiffusionPump: ns0.vartypes.BaseAnalogType | None
    waterVaporTolerableLoad: ns0.vartypes.BaseAnalogType | None
    wetCriticalSpeed: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1021", browseName="ns=pumps;ControlType", displayName="ControlType")
class ControlType(di.objtypes.FunctionalGroupType):
    commandVariable: ns0.vartypes.BaseAnalogType | None
    controlDifferenceVariable: ns0.vartypes.BaseAnalogType | None
    controlledVariable: ns0.vartypes.BaseAnalogType | None
    controllerOutputVariable: ns0.vartypes.BaseAnalogType | None
    deadTime: ns0.vartypes.BaseAnalogType | None
    derivativeActionCoefficient: ns0.vartypes.BaseAnalogType | None
    feedbackVariable: ns0.vartypes.BaseAnalogType | None
    finalControlledVariable: ns0.vartypes.BaseAnalogType | None
    integralActionCoefficient: ns0.vartypes.BaseAnalogType | None
    manipulatedVariable: ns0.vartypes.BaseAnalogType | None
    operatingMode: ns0.vartypes.DataItemType | None
    proportionalActionCoefficient: ns0.vartypes.BaseAnalogType | None
    referenceVariable: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1022", browseName="ns=pumps;SystemRequirementsType", displayName="SystemRequirementsType")
class SystemRequirementsType(di.objtypes.FunctionalGroupType):
    compressionRatio: ns0.vartypes.BaseAnalogType | None
    explosionZone: ns0.vartypes.DataItemType | None
    fieldbus: ns0.vartypes.DataItemType | None
    fluid: ns0.vartypes.DataItemType | None
    gasContent: ns0.vartypes.BaseAnalogType | None
    heightOfTheInletSideOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    heightOfTheOutletSideOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    heightOfThePump: ns0.vartypes.BaseAnalogType | None
    maximumAmbientTemperature: ns0.vartypes.BaseAnalogType | None
    maximumFlow: ns0.vartypes.BaseAnalogType | None
    maximumHead: ns0.vartypes.BaseAnalogType | None
    maximumInletPressure: ns0.vartypes.BaseAnalogType | None
    maximumOutletPressure: ns0.vartypes.BaseAnalogType | None
    maximumRelativeHumidity: ns0.vartypes.BaseAnalogType | None
    maximumTemperature: ns0.vartypes.BaseAnalogType | None
    meanTimeBetweenFailures: ns0.vartypes.BaseAnalogType | None
    minimumAmbientTemperature: ns0.vartypes.BaseAnalogType | None
    minimumFlow: ns0.vartypes.BaseAnalogType | None
    minimumHead: ns0.vartypes.BaseAnalogType | None
    minimumInletPressure: ns0.vartypes.BaseAnalogType | None
    minimumOutletPressure: ns0.vartypes.BaseAnalogType | None
    minimumRelativeHumidity: ns0.vartypes.BaseAnalogType | None
    minimumTemperature: ns0.vartypes.BaseAnalogType | None
    multi_Phase: ns0.vartypes.TwoStateDiscreteType | None
    netPositiveInletPressureAvailable: ns0.vartypes.BaseAnalogType | None
    normalFlow: ns0.vartypes.BaseAnalogType | None
    npshDatumPlane: ns0.vartypes.BaseAnalogType | None
    operatingMode: ns0.vartypes.DataItemType | None
    ratedInletPressureOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    ratedPumpUnitTotalHead: ns0.vartypes.BaseAnalogType | None
    referencePlane: ns0.vartypes.BaseAnalogType | None
    requiredControlMode: ns0.vartypes.DataItemType | None
    requiredTime: ns0.vartypes.BaseAnalogType | None
    solidContent: ns0.vartypes.BaseAnalogType | None
    throughput: ns0.vartypes.BaseAnalogType | None
    ultimatePressureOfAVacuumPump: ns0.vartypes.BaseAnalogType | None
    workingTemperature: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1023", browseName="ns=pumps;ImplementationType", displayName="ImplementationType")
class ImplementationType(di.objtypes.FunctionalGroupType):
    atmosphericPressure: ns0.vartypes.BaseAnalogType | None
    density: ns0.vartypes.BaseAnalogType | None
    dynamicViscosity: ns0.vartypes.BaseAnalogType | None
    heightOfTheInletManometer: ns0.vartypes.BaseAnalogType | None
    heightOfTheNpshDatumPlane: ns0.vartypes.BaseAnalogType | None
    heightOfTheOutletManometer: ns0.vartypes.BaseAnalogType | None
    hydraulicEfficiency: ns0.vartypes.BaseAnalogType | None
    installationTotalHead: ns0.vartypes.BaseAnalogType | None
    kinematicViscosity: ns0.vartypes.BaseAnalogType | None
    maximumAllowableFlow: ns0.vartypes.BaseAnalogType | None
    maximumDynamicSealingPressure: ns0.vartypes.BaseAnalogType | None
    mechanicalEfficiency: ns0.vartypes.BaseAnalogType | None
    minimumAllowableFlow: ns0.vartypes.BaseAnalogType | None
    minimumAllowableStableFlow: ns0.vartypes.BaseAnalogType | None
    netPositiveSuctionHeadAvailable: ns0.vartypes.BaseAnalogType | None
    overallEfficiency: ns0.vartypes.BaseAnalogType | None
    pumpBestEfficiency: ns0.vartypes.BaseAnalogType | None
    pumpEfficiency: ns0.vartypes.BaseAnalogType | None
    pumpMechanicalPowerLosses: ns0.vartypes.BaseAnalogType | None
    pumpRatedPowerInput: ns0.vartypes.BaseAnalogType | None
    pumpTotalHead: ns0.vartypes.BaseAnalogType | None
    ratedDifferentialPressure: ns0.vartypes.BaseAnalogType | None
    ratedFlow: ns0.vartypes.BaseAnalogType | None
    ratedMeanVelocityAtInletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    ratedMeanVelocityAtOutletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    ratedSpeed: ns0.vartypes.BaseAnalogType | None
    totalHeadAtInletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    totalHeadAtOutletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    usefulLife: ns0.vartypes.BaseAnalogType | None
    valveSeatVelocity: ns0.vartypes.BaseAnalogType | None
    valveSpillVelocity: ns0.vartypes.BaseAnalogType | None
    vaporPressureOfThePumpedLiquid: ns0.vartypes.BaseAnalogType | None
    volumetricEfficiency: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1024", browseName="ns=pumps;ConfigurationGroupType", displayName="ConfigurationGroupType")
class ConfigurationGroupType(di.objtypes.FunctionalGroupType):
    design: DesignType | None
    implementation: ImplementationType | None
    systemRequirements: SystemRequirementsType | None


@o6.objecttype(nodeId="ns=pumps;i=1025", browseName="ns=pumps;ActuationType", displayName="ActuationType")
class ActuationType(di.objtypes.FunctionalGroupType):
    faultAction: ns0.vartypes.TwoStateDiscreteType | None
    faultValue: ns0.vartypes.BaseAnalogType | None
    feedbackVariable: ns0.vartypes.AnalogUnitType | None
    manipulatedValue: ns0.vartypes.BaseAnalogType | None
    onOff: ns0.vartypes.TwoStateDiscreteType | None
    referenceVariable: ns0.vartypes.AnalogUnitType | None
    status: ns0.vartypes.TwoStateDiscreteType | None


@o6.objecttype(nodeId="ns=pumps;i=1028", browseName="ns=pumps;PumpActuationType", displayName="PumpActuationType")
class PumpActuationType(ActuationType):
    actualControlMode: ns0.vartypes.DataItemType | None
    actualOperationMode: ns0.vartypes.DataItemType | None
    cleanValveRequest: DiscreteOutputObjectType | None
    controlInversion: ns0.vartypes.TwoStateDiscreteType | None
    enable: ns0.vartypes.TwoStateDiscreteType | None
    externalSignal: ns0.vartypes.TwoStateDiscreteType | None
    flushValveRequest: DiscreteOutputObjectType | None
    gasDilValveRequest: DiscreteOutputObjectType | None
    inletValveRequest: DiscreteOutputObjectType | None
    outletValveRequest: DiscreteOutputObjectType | None
    pumpKick: PumpKickObjectType | None
    pumpStandByRequest: DiscreteOutputObjectType | None
    purgeValveRequest: DiscreteOutputObjectType | None
    reverseRotatingDirection: ns0.vartypes.TwoStateDiscreteType | None
    setControlMode: ns0.vartypes.DataItemType | None
    setOperationMode: ns0.vartypes.DataItemType | None
    ventValveRequest: DiscreteOutputObjectType | None


@o6.objecttype(nodeId="ns=pumps;i=1029", browseName="ns=pumps;DiscreteObjectType", displayName="DiscreteObjectType", isAbstract=True)
class DiscreteObjectType(ns0.objtypes.BaseObjectType):
    onOffCycle: ns0.vartypes.BaseAnalogType | None
    status: ns0.vartypes.TwoStateDiscreteType | None


@o6.objecttype(nodeId="ns=pumps;i=1030", browseName="ns=pumps;DiscreteInputObjectType", displayName="DiscreteInputObjectType")
class DiscreteInputObjectType(DiscreteObjectType):
    discreteInputValue: ns0.vartypes.TwoStateDiscreteType


@o6.objecttype(nodeId="ns=pumps;i=1031", browseName="ns=pumps;DiscreteOutputObjectType", displayName="DiscreteOutputObjectType")
class DiscreteOutputObjectType(DiscreteObjectType):
    discreteOutputValue: ns0.vartypes.TwoStateDiscreteType
    faultAction: ns0.vartypes.TwoStateDiscreteType | None
    faultValue: ns0.vartypes.TwoStateDiscreteType | None


@o6.objecttype(nodeId="ns=pumps;i=1032", browseName="ns=pumps;PumpKickObjectType", displayName="PumpKickObjectType")
class PumpKickObjectType(DiscreteOutputObjectType):
    pumpKickMode: ns0.vartypes.DataItemType | None
    pumpKickTime: ns0.vartypes.DataItemType | None
    pumpKickTimeDifference: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=pumps;i=1033", browseName="ns=pumps;SignalsType", displayName="SignalsType")
class SignalsType(di.objtypes.FunctionalGroupType):
    acceleration: DiscreteInputObjectType | None
    cleanValveOpen: DiscreteInputObjectType | None
    deceleration: DiscreteInputObjectType | None
    flushValveOpen: DiscreteInputObjectType | None
    gasDilValveOpen: DiscreteInputObjectType | None
    inletValveOpen: DiscreteInputObjectType | None
    noRotation: DiscreteInputObjectType | None
    outletValveOpen: DiscreteInputObjectType | None
    processIsActive: DiscreteInputObjectType | None
    pumpActivation: DiscreteInputObjectType | None
    pumpDirection: DiscreteInputObjectType | None
    pumpOperation: DiscreteInputObjectType | None
    pumpPowerMax: DiscreteInputObjectType | None
    pumpSpeedMax: DiscreteInputObjectType | None
    pumpSpeedMin: DiscreteInputObjectType | None
    purgeValveOpen: DiscreteInputObjectType | None
    ratedSpeed: DiscreteInputObjectType | None
    standBy: DiscreteInputObjectType | None
    standBySpeed: DiscreteInputObjectType | None
    targetSpeed: DiscreteInputObjectType | None
    ventValveOpen: DiscreteInputObjectType | None


@o6.objecttype(nodeId="ns=pumps;i=1034", browseName="ns=pumps;PortsGroupType", displayName="PortsGroupType")
class PortsGroupType(di.objtypes.FunctionalGroupType):
    langleDriveRangle: DrivePortType | None
    langleInletConnectionRangle: InletConnectionPortType | None
    langleOutletConnectionRangle: OutletConnectionPortType | None


@o6.objecttype(nodeId="ns=pumps;i=1035", browseName="ns=pumps;PortType", displayName="PortType", isAbstract=True)
class PortType(ns0.objtypes.BaseObjectType):
    category: ns0.vartypes.DataItemType | None
    direction: ns0.vartypes.DataItemType | None
    idCarrier: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1036", browseName="ns=pumps;InletConnectionPortType", displayName="InletConnectionPortType")
class InletConnectionPortType(PortType):
    design: InletConnectionDesignType | None
    implementation: InletConnectionImplementationType | None
    measurements: InletConnectionMeasurementsType | None
    systemRequirements: InletConnectionSystemRequirementsType | None


@o6.objecttype(nodeId="ns=pumps;i=1037", browseName="ns=pumps;OutletConnectionPortType", displayName="OutletConnectionPortType")
class OutletConnectionPortType(PortType):
    design: OutletConnectionDesignType | None
    implementation: OutletConnectionImplementationType | None
    measurements: OutletConnectionMeasurementsType | None
    systemRequirements: OutletConnectionSystemRequirementsType | None


@o6.objecttype(nodeId="ns=pumps;i=1038", browseName="ns=pumps;DrivePortType", displayName="DrivePortType")
class DrivePortType(PortType):
    design: DriveDesignType | None
    measurements: DriveMeasurementsType | None


@o6.objecttype(nodeId="ns=pumps;i=1039", browseName="ns=pumps;MultiPumpType", displayName="MultiPumpType")
class MultiPumpType(di.objtypes.FunctionalGroupType):
    distributionPriority: ns0.vartypes.DataItemType | None
    distributionType: ns0.vartypes.DataItemType | None
    exchangeMode: ns0.vartypes.DataItemType | None
    exchangeTime: ns0.vartypes.DataItemType | None
    exchangeTimeDifference: ns0.vartypes.AnalogUnitType | None
    maximumNumberOfPumpsInOperation: ns0.vartypes.DataItemType | None
    multiPumpOperationMode: ns0.vartypes.DataItemType | None
    numberOfPumps: ns0.vartypes.DataItemType | None
    pumpCollectiveIDs: ns0.vartypes.DataItemType | None
    pumpRole: ns0.vartypes.DataItemType | None
    redundantPumpIDs: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1040", browseName="ns=pumps;ConnectionDesignType", displayName="ConnectionDesignType", isAbstract=True)
class ConnectionDesignType(di.objtypes.FunctionalGroupType):
    nominalPressure: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1041", browseName="ns=pumps;InletConnectionDesignType", displayName="InletConnectionDesignType")
class InletConnectionDesignType(ConnectionDesignType):
    criticalBackingPressure: ns0.vartypes.BaseAnalogType | None
    inletAreaOfThePump: ns0.vartypes.BaseAnalogType | None
    maximumAllowableInletPressure: ns0.vartypes.BaseAnalogType | None
    maximumTolerableWaterVaporInletPressure: ns0.vartypes.BaseAnalogType | None
    maximumWorkingPressure: ns0.vartypes.BaseAnalogType | None
    minimumAllowableInletPressure: ns0.vartypes.BaseAnalogType | None
    netPositiveInletPressureRequired: ns0.vartypes.BaseAnalogType | None
    waterVaporCapacity: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1042", browseName="ns=pumps;OutletConnectionDesignType", displayName="OutletConnectionDesignType")
class OutletConnectionDesignType(ConnectionDesignType):
    maximumAllowableOutletPressure: ns0.vartypes.BaseAnalogType | None
    minimumAllowableOutetPressure: ns0.vartypes.BaseAnalogType | None
    outletAreaOfThePump: ns0.vartypes.BaseAnalogType | None
    reliefValveAccumulationPressure: ns0.vartypes.BaseAnalogType | None
    reliefValveBackPressure: ns0.vartypes.BaseAnalogType | None
    reliefValveReseatPressure: ns0.vartypes.BaseAnalogType | None
    reliefValveSetPressure: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1043", browseName="ns=pumps;DriveDesignType", displayName="DriveDesignType")
class DriveDesignType(di.objtypes.FunctionalGroupType):
    energyEfficiencyClassOfMotor: ns0.vartypes.DataItemType | None
    maxNominalFrequency: ns0.vartypes.BaseAnalogType | None
    minNominalFrequency: ns0.vartypes.BaseAnalogType | None
    motorEfficiency: ns0.vartypes.BaseAnalogType | None
    nominalFrequency: ns0.vartypes.BaseAnalogType | None
    nominalPowerConsumption: ns0.vartypes.BaseAnalogType | None
    nominalVoltage: ns0.vartypes.BaseAnalogType | None
    powerFactor: ns0.vartypes.BaseAnalogType | None
    protectionClass: ns0.vartypes.DataItemType | None
    ratedCurrent: ns0.vartypes.BaseAnalogType | None
    ratedSpeed: ns0.vartypes.BaseAnalogType | None
    torqueAtNominalSpeedOfDrive: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1044", browseName="ns=pumps;OutletConnectionSystemRequirementsType", displayName="OutletConnectionSystemRequirementsType")
class OutletConnectionSystemRequirementsType(di.objtypes.FunctionalGroupType):
    backingPressure: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1045", browseName="ns=pumps;InletConnectionSystemRequirementsType", displayName="InletConnectionSystemRequirementsType")
class InletConnectionSystemRequirementsType(di.objtypes.FunctionalGroupType):
    inletPressure: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1046", browseName="ns=pumps;ConnectionImplementationType", displayName="ConnectionImplementationType", isAbstract=True)
class ConnectionImplementationType(di.objtypes.FunctionalGroupType):
    nominalSize: ns0.vartypes.DataItemType | None


@o6.objecttype(nodeId="ns=pumps;i=1047", browseName="ns=pumps;InletConnectionImplementationType", displayName="InletConnectionImplementationType")
class InletConnectionImplementationType(ConnectionImplementationType):
    heightOfTheInletConnection: ns0.vartypes.BaseAnalogType | None
    meanRatedVelocityAtInlet: ns0.vartypes.BaseAnalogType | None
    ratedInletPressure: ns0.vartypes.BaseAnalogType | None
    totalHeadAtInletAreaOfThePump: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1048", browseName="ns=pumps;OutletConnectionImplementationType", displayName="OutletConnectionImplementationType")
class OutletConnectionImplementationType(ConnectionImplementationType):
    heightOfTheOutletConnection: ns0.vartypes.BaseAnalogType | None
    meanRatedVelocityAtOutlet: ns0.vartypes.BaseAnalogType | None
    ratedOutletPressure: ns0.vartypes.BaseAnalogType | None
    totalHeadAtOutletAreaOfThePump: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1049", browseName="ns=pumps;OutletConnectionMeasurementsType", displayName="OutletConnectionMeasurementsType")
class OutletConnectionMeasurementsType(di.objtypes.FunctionalGroupType):
    meanVelocityAtOutlet: ns0.vartypes.BaseAnalogType | None
    outletTemperatureOfThePump: ns0.vartypes.BaseAnalogType | None


o6.reference(OutletConnectionMeasurementsType, "i=41", "i=2955")


@o6.objecttype(nodeId="ns=pumps;i=1050", browseName="ns=pumps;InletConnectionMeasurementsType", displayName="InletConnectionMeasurementsType")
class InletConnectionMeasurementsType(di.objtypes.FunctionalGroupType):
    inletTemperatureOfThePump: ns0.vartypes.BaseAnalogType | None
    meanVelocityAtInlet: ns0.vartypes.BaseAnalogType | None


o6.reference(InletConnectionMeasurementsType, "i=41", "i=2955")


@o6.objecttype(nodeId="ns=pumps;i=1051", browseName="ns=pumps;DriveMeasurementsType", displayName="DriveMeasurementsType")
class DriveMeasurementsType(di.objtypes.FunctionalGroupType):
    current: ns0.vartypes.BaseAnalogType | None
    dCLinkCurrent: ns0.vartypes.BaseAnalogType | None
    dCLinkVoltage: ns0.vartypes.BaseAnalogType | None
    driverPowerInput: ns0.vartypes.BaseAnalogType | None
    energyConsumption: ns0.vartypes.BaseAnalogType | None
    frequency: ns0.vartypes.BaseAnalogType | None
    motorCurrent: ns0.vartypes.BaseAnalogType | None
    motorEfficiency: ns0.vartypes.BaseAnalogType | None
    motorTemperature: ns0.vartypes.BaseAnalogType | None
    motorVoltage: ns0.vartypes.BaseAnalogType | None
    powerFactor: ns0.vartypes.BaseAnalogType | None
    torque: ns0.vartypes.BaseAnalogType | None
    voltage: ns0.vartypes.BaseAnalogType | None


o6.reference(DriveMeasurementsType, "i=41", "i=2955")


@o6.objecttype(nodeId="ns=pumps;i=1052", browseName="ns=pumps;PumpType", displayName="PumpType")
class PumpType(di.objtypes.TopologyElementType):
    configuration: ConfigurationGroupType | None
    documentation: DocumentationType | None
    events: SupervisionType | None
    identification: PumpIdentificationType
    maintenance: MaintenanceGroupType | None
    operational: OperationalGroupType | None
    ports: PortsGroupType | None


@o6.objecttype(nodeId="ns=pumps;i=1053", browseName="ns=pumps;OperationalGroupType", displayName="OperationalGroupType")
class OperationalGroupType(di.objtypes.FunctionalGroupType):
    bypassActuation: ActuationType | None
    control: ControlType | None
    measurements: MeasurementsType | None
    multiPump: MultiPumpType | None
    pumpActuation: PumpActuationType | None
    signals: SignalsType | None
    throttleValveActuation: ActuationType | None


@o6.objecttype(nodeId="ns=pumps;i=1054", browseName="ns=pumps;MeasurementsType", displayName="MeasurementsType")
class MeasurementsType(di.objtypes.FunctionalGroupType):
    ambientHumidity: ns0.vartypes.BaseAnalogType | None
    ambientTemperature: ns0.vartypes.BaseAnalogType | None
    axialLoadOfPumpRotor: ns0.vartypes.BaseAnalogType | None
    axialRotorPosition: ns0.vartypes.BaseAnalogType | None
    backPressure: ns0.vartypes.BaseAnalogType | None
    bearingTemperature: ns0.vartypes.BaseAnalogType | None
    clearanceFlow: ns0.vartypes.BaseAnalogType | None
    coolantTemperature: ns0.vartypes.BaseAnalogType | None
    density: ns0.vartypes.BaseAnalogType | None
    differentialPressure: ns0.vartypes.BaseAnalogType | None
    dynamicViscosity: ns0.vartypes.BaseAnalogType | None
    electronicTemperature: ns0.vartypes.BaseAnalogType | None
    fluidTemperature: ns0.vartypes.BaseAnalogType | None
    housingTemperature: ns0.vartypes.BaseAnalogType | None
    hydraulicEfficiency: ns0.vartypes.BaseAnalogType | None
    inletPressureOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    installationTotalHead: ns0.vartypes.BaseAnalogType | None
    kinematicViscosity: ns0.vartypes.BaseAnalogType | None
    langleVibrationRangle: VibrationMeasurementType | None
    leakageRateOfFlow: ns0.vartypes.BaseAnalogType | None
    level: ns0.vartypes.BaseAnalogType | None
    lubricatingOilConsumption: ns0.vartypes.BaseAnalogType | None
    lubricatingOilPressure: ns0.vartypes.BaseAnalogType | None
    massFlow: ns0.vartypes.BaseAnalogType | None
    meanVelocityAtThroat: ns0.vartypes.BaseAnalogType | None
    mechanicalEfficiency: ns0.vartypes.BaseAnalogType | None
    netPositiveInletPressure: ns0.vartypes.BaseAnalogType | None
    netPositiveSuctionHead: ns0.vartypes.BaseAnalogType | None
    numberOfStarts: ns0.vartypes.BaseAnalogType | None
    outletPressureOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    overallEfficiency: ns0.vartypes.BaseAnalogType | None
    powerLossDueToInternalLeakage: ns0.vartypes.BaseAnalogType | None
    processPressure: ns0.vartypes.BaseAnalogType | None
    pumpEfficiency: ns0.vartypes.BaseAnalogType | None
    pumpHumidity: ns0.vartypes.BaseAnalogType | None
    pumpPowerInput: ns0.vartypes.BaseAnalogType | None
    pumpPowerOutput: ns0.vartypes.BaseAnalogType | None
    pumpTemperature: ns0.vartypes.BaseAnalogType | None
    pumpTotalHead: ns0.vartypes.BaseAnalogType | None
    radialLoadOfPumpRotor: ns0.vartypes.BaseAnalogType | None
    soundEnergy: ns0.vartypes.BaseAnalogType | None
    soundEnergyLevel: ns0.vartypes.BaseAnalogType | None
    soundPower: ns0.vartypes.BaseAnalogType | None
    soundPowerLevel: ns0.vartypes.BaseAnalogType | None
    soundPressure: ns0.vartypes.BaseAnalogType | None
    soundPressureLevel: ns0.vartypes.BaseAnalogType | None
    speed: ns0.vartypes.BaseAnalogType | None
    throughput: ns0.vartypes.BaseAnalogType | None
    totalHeadAtInletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    totalHeadAtOutletAreaOfTheInstallation: ns0.vartypes.BaseAnalogType | None
    volumetricEfficiency: ns0.vartypes.BaseAnalogType | None


o6.reference(MeasurementsType, "i=41", "i=2955")


@o6.objecttype(nodeId="ns=pumps;i=1055", browseName="ns=pumps;VibrationMeasurementType", displayName="VibrationMeasurementType")
class VibrationMeasurementType(di.objtypes.FunctionalGroupType):
    bearingIndex: ns0.vartypes.BaseAnalogType | None
    bearingIndexPerG: ns0.vartypes.BaseAnalogType | None
    broadbandCavitationAccelerationPerG_RMS: ns0.vartypes.BaseAnalogType | None
    broadbandCavitationAccelerationRMS: ns0.vartypes.BaseAnalogType | None
    gapVoltage: ns0.vartypes.BaseAnalogType | None
    not1XRelativeShaftVibrationP_P: ns0.vartypes.BaseAnalogType | None
    oneXPhase: ns0.vartypes.BaseAnalogType | None
    oneXRelativeShaftVibrationP_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationAcceleration0_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationAccelerationP_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationAccelerationPerG0_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationAccelerationPerGP_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationAccelerationPerG_RMS: ns0.vartypes.BaseAnalogType | None
    overallVibrationAccelerationRMS: ns0.vartypes.BaseAnalogType | None
    overallVibrationDisplacementP_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationDisplacementRMS: ns0.vartypes.BaseAnalogType | None
    overallVibrationVelocity0_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationVelocityP_P: ns0.vartypes.BaseAnalogType | None
    overallVibrationVelocityRMS: ns0.vartypes.BaseAnalogType | None
    referenceStandardForVibrationMeasurement: ns0.vartypes.DataItemType | None
    rotationalPhase1X: ns0.vartypes.BaseAnalogType | None
    rotationalPhase2X: ns0.vartypes.BaseAnalogType | None
    speedOfRotation: ns0.vartypes.BaseAnalogType | None
    thrustPosition: ns0.vartypes.BaseAnalogType | None
    twoXPhase: ns0.vartypes.BaseAnalogType | None
    twoXRelativeShaftVibrationP_P: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheBearingDefectFrequencies: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheBearingDefectFrequenciesPerG: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheBladePassFrequency: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheFirstHarmonicOfTheRotationFrequency2X: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheGearMeshingFrequency: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheGearMeshingFrequencyPerG: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheHarmonicsOfTheRotationFrequencyNx: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheRotationFrequency1X: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheSidebandsOfTheGearMeshingFrequency: ns0.vartypes.BaseAnalogType | None
    vibrationAmplitudeAtTheSidebandsOfTheGearMeshingFrequencyPerG: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(nodeId="ns=pumps;i=1004", browseName="ns=pumps;IPumpVendorNameplateType", displayName="IPumpVendorNameplateType", isAbstract=True)
class IPumpVendorNameplateType(machinery.objtypes.IMachineVendorNameplateType):
    articleNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6063",
            browseName="ns=pumps;ArticleNumber",
            description="Alphanumeric character sequence identifying a manufactured, non-configurable product.",
            dataType=o6.String,
        )
    )
    countryOfOrigin: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6080",
            browseName="ns=pumps;CountryOfOrigin",
            description="Country in which the product is manufactured.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dayOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6064",
            browseName="ns=pumps;DayOfConstruction",
            description="The optional DayOfConstrucition provides the day of the month in which the manufacturing process of the machine has been completed. It shall be a number and never change during the life-cycle of a machine.",
            dataType=o6.Int32,
        )
    )
    fabricationNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6065",
            browseName="ns=pumps;FabricationNumber",
            description="Alphanumeric character sequence assigned to a fabricated product, which allows the date, time and circumstances of fabrication to be traced.",
            dataType=o6.String,
        )
    )
    gTINCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6066",
            browseName="ns=pumps;GTINCode",
            description="Bar code number that identifies the device based on the Global Trade Item Number system.",
            dataType=o6.String,
        )
    )
    nationalStockNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6067",
            browseName="ns=pumps;NationalStockNumber",
            description="13-digit numeric code, identifying all 'standardized material items of supply' as recognized by the United States Department of Defense.",
            dataType=o6.String,
        )
    )
    orderProductCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6068", browseName="ns=pumps;OrderProductCode", description="Unique combination of numbers and letters used to order the device.", dataType=o6.String
        )
    )
    physicalAddress: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=9940",
            browseName="ns=pumps;PhysicalAddress",
            description="Physical address of the manufacturer.",
            dataType=pumps_datypes.PhysicalAddressDataType,
            value=pumps_datypes.PhysicalAddressDataType(street=None, number=None, city=None, postalCode=None, state=None, country=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supplier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pumps;i=6069", browseName="ns=pumps;Supplier", description="Name of the supplier or vendor of a device.", dataType=o6.String)
    )
    typeOfProduct: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6070",
            browseName="ns=pumps;TypeOfProduct",
            description="Characterization of the device based on its usage, operation principle, and its fabricated form.",
            dataType=o6.String,
        )
    )


@o6.objecttype(nodeId="ns=pumps;i=1005", browseName="ns=pumps;PumpIdentificationType", displayName="PumpIdentificationType", interfaces=[IPumpVendorNameplateType])
class PumpIdentificationType(machinery.objtypes.MachineIdentificationType):
    articleNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6071",
            browseName="ns=pumps;ArticleNumber",
            description="Alphanumeric character sequence identifying a manufactured, non-configurable product.",
            dataType=o6.String,
        )
    )
    countryOfOrigin: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pumps;i=6079", browseName="ns=pumps;CountryOfOrigin", description="Country in which the product is manufactured.", dataType=o6.String)
    )
    dayOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6072",
            browseName="ns=pumps;DayOfConstruction",
            description="The optional DayOfConstrucition provides the day of the month in which the manufacturing process of the machine has been completed. It shall be a number and never change during the life-cycle of a machine.",
            dataType=o6.Int32,
        )
    )
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=12928", browseName="ns=di;DeviceClass", description="Domain or for what purpose this item is used.", dataType=o6.String, value="Pump"
        )
    )
    fabricationNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6073",
            browseName="ns=pumps;FabricationNumber",
            description="Alphanumeric character sequence assigned to a fabricated product, which allows the date, time and circumstances of fabrication to be traced.",
            dataType=o6.String,
        )
    )
    gTINCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6074",
            browseName="ns=pumps;GTINCode",
            description="Bar code number that identifies the device based on the Global Trade Item Number system.",
            dataType=o6.String,
        )
    )
    markings: MarkingsType | None
    nationalStockNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6075",
            browseName="ns=pumps;NationalStockNumber",
            description="13-digit numeric code, identifying all 'standardized material items of supply' as recognized by the United States Department of Defense.",
            dataType=o6.String,
        )
    )
    orderProductCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6076", browseName="ns=pumps;OrderProductCode", description="Unique combination of numbers and letters used to order the device.", dataType=o6.String
        )
    )
    physicalAddress: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6081",
            browseName="ns=pumps;PhysicalAddress",
            description="Physical address of the manufacturer.",
            dataType=pumps_datypes.PhysicalAddressDataType,
            value=pumps_datypes.PhysicalAddressDataType(street=None, number=None, city=None, postalCode=None, state=None, country=None),
        )
    )
    supplier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pumps;i=6077", browseName="ns=pumps;Supplier", description="Name of the supplier or vendor of a device.", dataType=o6.String)
    )
    typeOfProduct: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pumps;i=6078",
            browseName="ns=pumps;TypeOfProduct",
            description="Characterisation of the device based on its usage, operation principle, and its fabricated form.",
            dataType=o6.String,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pumps_datypes
