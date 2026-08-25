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

"""Generated OPC UA padim namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0
from . import datatypes as padim_datypes
from . import vartypes as padim_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(nodeId="ns=padim;i=1010", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText, value=o6.LocalizedText())
o6.reference(o6.ns["ns=padim;i=1010"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA031#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1011", browseName="ns=di;ManufacturerUri", displayName="URI manufacturer", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1011"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA032#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1012", browseName="ns=di;Model", dataType=o6.LocalizedText, value=o6.LocalizedText())
o6.reference(o6.ns["ns=padim;i=1012"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA039#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1013", browseName="ns=di;SerialNumber", displayName="Serial number", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1013"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA050#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1014", browseName="ns=di;SoftwareRevision", displayName="Software revision", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1014"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA046#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1015", browseName="ns=di;HardwareRevision", displayName="Hardware revision", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1015"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA047#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1016", browseName="ns=di;ProductCode", displayName="Product code", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1016"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA040#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1017", browseName="ns=di;RevisionCounter", displayName="Revision counter", dataType=o6.Int32, value=0)
o6.reference(o6.ns["ns=padim;i=1017"], "i=17597", "ns=irdi;s=0112/2///61987#ABN603#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1019", browseName="ns=di;AssetId", displayName="Asset ID", dataType=o6.String, value="", accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1019"], "i=17597", "ns=irdi;s=0112/2///61987#ABA038#004")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1020", browseName="ns=di;ProductInstanceUri", displayName="URI product inst.", dataType=o6.String, value="")
o6.reference(o6.ns["ns=padim;i=1020"], "i=17597", "ns=irdi;s=0112/2///61360_7#CBA055#001")


@o6.objecttype(nodeId="ns=padim;i=1021", browseName="ns=padim;SignalSetType", displayName="SignalSetType")
class SignalSetType(ns0.objtypes.BaseObjectType):
    langleSignalIdentifierRangle: SignalType | None


ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=padim;i=1028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ResetMode", dataType=o6.NodeId("ns=aml;i=1156"), valueRank=-1)],
    accessLevel=3,
)
o6.call(nodeId="ns=padim;i=1028", browseName="ns=padim;FactoryReset", displayName="Reset", inputArgs=o6.hasProperty(o6.ns["ns=padim;i=1030"]))
o6.reference(o6.ns["ns=padim;i=1028"], "i=17597", "ns=irdi;s=0112/2///61987#ABN609#002")

ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1029",
    browseName="ns=di;DeviceHealth",
    displayName="Device diagnostic status",
    dataType=di.datatypes.DeviceHealthEnumeration,
    value=di.datatypes.DeviceHealthEnumeration.NORMAL,
)
o6.reference(o6.ns["ns=padim;i=1029"], "i=17597", "ns=irdi;s=0112/2///61987#ABN972#002")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1032", browseName="ns=padim;DateOfLastChange", displayName="Date last change", dataType=o6.DateTime, value=o6.DateTime("1601-01-01T00:00:00Z")
)
o6.reference(o6.ns["ns=padim;i=1032"], "i=17597", "ns=irdi;s=0112/2///61987#ABN604#001")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1033", browseName="ns=padim;DisplayLanguage", displayName="Display language", dataType=ns0.datatypes.LocaleId, value="en", accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1033"], "i=17597", "ns=irdi;s=0112/2///61987#ABN597#004")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1035", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1035"], "i=17597", "ns=irdi;s=0112/2///61987#ABB271#009")


@o6.objecttype(nodeId="ns=padim;i=1008", browseName="ns=padim;SignalType", displayName="SignalType")
class SignalType(ns0.objtypes.BaseObjectType):
    signalTag: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1035"])


@o6.objecttype(nodeId="ns=padim;i=1037", browseName="ns=padim;TwoStateDiscreteSignalType", displayName="TwoStateDiscreteSignalType")
class TwoStateDiscreteSignalType(SignalType):
    twoStateDiscreteSignal: padim_vartypes.TwoStateDiscreteSignalVariableType


@o6.objecttype(nodeId="ns=padim;i=1038", browseName="ns=padim;MultiStateDiscreteSignalType", displayName="MultiStateDiscreteSignalType")
class MultiStateDiscreteSignalType(SignalType):
    multiStateDiscreteSignal: padim_vartypes.MultiStateDiscreteSignalVariableType


padim_vartypes.DiscreteSignalVariableType(nodeId="ns=padim;i=1039", browseName="ns=padim;DiscreteSignal", displayName="Value", valueRank=-2, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1039"], "i=17597", "ns=irdi;s=0112/2///61987#ABN634#001")


@o6.objecttype(nodeId="ns=padim;i=1036", browseName="ns=padim;DiscreteSignalType", displayName="DiscreteSignalType")
class DiscreteSignalType(SignalType):
    discreteSignal: padim_vartypes.DiscreteSignalVariableType = o6.hasComponent(o6.ns["ns=padim;i=1039"])


@o6.objecttype(nodeId="ns=padim;i=1047", browseName="ns=padim;IConductivityCalibrationType", displayName="IConductivityCalibrationType", isAbstract=True)
class IConductivityCalibrationType(ns0.objtypes.BaseInterfaceType):
    conductivityCellConstant: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=padim;i=1053", browseName="ns=padim;ITocDeviceConditionSetType", displayName="ITocDeviceConditionSetType", isAbstract=True)
class ITocDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    actualInjectedVolume: ns0.vartypes.AnalogUnitType | None
    carrierGasGaugePressure: ns0.vartypes.AnalogUnitType | None
    carrierGasVolumeFlow: ns0.vartypes.AnalogUnitType | None
    coolerTemperature: ns0.vartypes.AnalogUnitType | None
    reactorTemperature: ns0.vartypes.AnalogUnitType | None
    referenceInjectionVolume: ns0.vartypes.AnalogUnitType | None
    sampleWaterVolumeFlow: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=padim;i=1054", browseName="ns=padim;IFlameIonisationDeviceConditionSetType", displayName="IFlameIonisationDeviceConditionSetType", isAbstract=True)
class IFlameIonisationDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    blockTemperature: ns0.vartypes.AnalogUnitType | None
    catalystTemperature: ns0.vartypes.AnalogUnitType | None
    combustionAirPressure: ns0.vartypes.AnalogUnitType | None
    fuelGasPressure: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=padim;i=1057", browseName="ns=padim;IParamagneticSignalConditionSetType", displayName="IParamagneticSignalConditionSetType", isAbstract=True)
class IParamagneticSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    sampleTemperature: ns0.vartypes.AnalogUnitType | None
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=padim;i=1058", browseName="ns=padim;IThermalConductivitySignalConditionSetType", displayName="IThermalConductivitySignalConditionSetType", isAbstract=True
)
class IThermalConductivitySignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    sampleTemperature: ns0.vartypes.AnalogUnitType | None


ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1068", browseName="ns=padim;DisplayLanguage", displayName="Display language", dataType=ns0.datatypes.LocaleId, value="en", accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1068"], "i=17597", "ns=irdi;s=0112/2///61987#ABN597#004")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1070", browseName="ns=padim;DateOfLastChange", displayName="Date last change", dataType=o6.DateTime, value=o6.DateTime("1601-01-01T00:00:00Z")
)
o6.reference(o6.ns["ns=padim;i=1070"], "i=17597", "ns=irdi;s=0112/2///61987#ABN604#001")


ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1080",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=padim;i=1072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ResetMode", dataType=o6.NodeId("ns=aml;i=1156"), valueRank=-1)],
    accessLevel=3,
)
o6.call(nodeId="ns=padim;i=1072", browseName="ns=padim;FactoryReset", displayName="Reset", inputArgs=o6.hasProperty(o6.ns["ns=padim;i=1080"]))
o6.reference(o6.ns["ns=padim;i=1072"], "i=17597", "ns=irdi;s=0112/2///61987#ABN609#002")


@o6.objecttype(nodeId="ns=padim;i=1050", browseName="ns=padim;IAdministrationType", displayName="IAdministrationType", isAbstract=True)
class IAdministrationType(ns0.objtypes.BaseInterfaceType):
    dateOfLastChange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1070"])
    displayLanguage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1068"])
    factoryReset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=padim;i=1072"])


@o6.objecttype(nodeId="ns=padim;i=1052", browseName="ns=padim;ISignalSetType", displayName="ISignalSetType", isAbstract=True)
class ISignalSetType(ns0.objtypes.BaseInterfaceType):
    signalSet: SignalSetType | None = o6.hasComponent(SignalSetType(nodeId="ns=padim;i=1074", browseName="ns=padim;SignalSet"))


o6.call(nodeId="ns=padim;i=1109", browseName="ns=padim;ZeroPointAdjustment", displayName="Set zero point")
o6.reference(o6.ns["ns=padim;i=1109"], "i=17597", "ns=irdi;s=0112/2///61987#ABN614#002")

ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1119",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=padim;i=1116",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExecutionMode", dataType=o6.NodeId("ns=aml;i=1158"), valueRank=-1)],
    accessLevel=3,
)
o6.call(nodeId="ns=padim;i=1116", browseName="ns=padim;AutoAdjustPositioner", displayName="Autoadjust", inputArgs=o6.hasProperty(o6.ns["ns=padim;i=1119"]))
o6.reference(o6.ns["ns=padim;i=1116"], "i=17597", "ns=irdi;s=0112/2///61987#ABN726#002")


@o6.objecttype(nodeId="ns=padim;i=1023", browseName="ns=padim;ControlSignalType", displayName="ControlSignalType")
class ControlSignalType(SignalType):
    autoAdjustPositioner: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=padim;i=1116"])
    controlSignal: padim_vartypes.ControlVariableType


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1208", browseName="ns=di;DeviceRevision", displayName="Device revision", dataType=ns0.datatypes.SemanticVersionString, value="1.0.0")
o6.reference(o6.ns["ns=padim;i=1208"], "i=17597", "ns=irdi;s=0112/2///61987#ABP643#002")


@o6.objecttype(nodeId="ns=padim;i=1009", browseName="ns=padim;PADIMType", displayName="PADIMType", interfaces=[di.objtypes.IDeviceHealthType, IAdministrationType, ISignalSetType])
class PADIMType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1019"])
    dateOfLastChange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1032"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=padim;i=1209", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, value=o6.QualifiedName("padim:PADIMView"))
    )
    deviceConditionSet: ns0.objtypes.BaseObjectType | None
    deviceHealth: ns0.vartypes.BaseDataVariableType = o6.hasComponent(o6.ns["ns=padim;i=1029"])
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=padim;i=1018", browseName="ns=di;DeviceHealthAlarms"))
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1208"])
    displayLanguage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1033"])
    factoryReset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=padim;i=1028"])
    hardwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1015"])
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1010"])
    manufacturerUri: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1011"])
    model: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1012"])
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1016"])
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1020"])
    revisionCounter: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1017"])
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1013"])
    signalSet: SignalSetType | None = o6.hasComponent(SignalSetType(nodeId="ns=padim;i=1034", browseName="ns=padim;SignalSet"))
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1014"])
    subDevices: di.objtypes.ConfigurableObjectType | None


o6.reference(PADIMType, "i=17597", "ns=irdi;s=<DictionaryEntryName>")


@o6.objecttype(nodeId="ns=padim;i=1082", browseName="ns=padim;ProcessAnalyserType", displayName="Process analyser")
class ProcessAnalyserType(PADIMType):
    pass


o6.reference(ProcessAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP397#002")


@o6.objecttype(nodeId="ns=padim;i=1083", browseName="ns=padim;AmperometricAnalyserType", displayName="Amperometric analyser")
class AmperometricAnalyserType(ProcessAnalyserType):
    pass


o6.reference(AmperometricAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP407#002")


@o6.objecttype(nodeId="ns=padim;i=1084", browseName="ns=padim;ConductivityMeterType", displayName="Conductivity meter")
class ConductivityMeterType(ProcessAnalyserType):
    pass


o6.reference(ConductivityMeterType, "i=17597", "ns=irdi;s=0112/2///61987#ABP405#002")


@o6.objecttype(nodeId="ns=padim;i=1085", browseName="ns=padim;FlameIonisationDetectorType", displayName="Flame ionisation detector")
class FlameIonisationDetectorType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(FlameIonisationDetectorType, "i=17597", "ns=irdi;s=0112/2///61987#ABP410#002")


@o6.objecttype(nodeId="ns=padim;i=1086", browseName="ns=padim;NonDispersiveInfraredGasAnalyserType", displayName="Non-dispersive infrared gas analyser")
class NonDispersiveInfraredGasAnalyserType(ProcessAnalyserType):
    pass


o6.reference(NonDispersiveInfraredGasAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP425#002")


@o6.objecttype(nodeId="ns=padim;i=1087", browseName="ns=padim;OpticalFluorescenseQuenchingSensorType", displayName="Optical fluorescence quenching sensor")
class OpticalFluorescenseQuenchingSensorType(ProcessAnalyserType):
    pass


o6.reference(OpticalFluorescenseQuenchingSensorType, "i=17597", "ns=irdi;s=0112/2///61987#ABP423#002")


@o6.objecttype(nodeId="ns=padim;i=1088", browseName="ns=padim;ParamagneticGasAnalyserType", displayName="Paramagnetic gas analyser")
class ParamagneticGasAnalyserType(ProcessAnalyserType):
    pass


o6.reference(ParamagneticGasAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP436#002")


@o6.objecttype(nodeId="ns=padim;i=1089", browseName="ns=padim;PhMeterType", displayName="pH meter")
class PhMeterType(ProcessAnalyserType):
    pass


o6.reference(PhMeterType, "i=17597", "ns=irdi;s=0112/2///61987#ABP440#002")


@o6.objecttype(nodeId="ns=padim;i=1090", browseName="ns=padim;ThermalConductivityGasAnalyserType", displayName="Thermal conductivity gas analyser")
class ThermalConductivityGasAnalyserType(ProcessAnalyserType):
    pass


o6.reference(ThermalConductivityGasAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP453#002")


@o6.objecttype(nodeId="ns=padim;i=1091", browseName="ns=padim;TocAnalyserType", displayName="TOC analyser")
class TocAnalyserType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(TocAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP444#002")


@o6.objecttype(nodeId="ns=padim;i=1092", browseName="ns=padim;TunableDiodeLaserSpectrometerType", displayName="Tunable diode laser spectrometer")
class TunableDiodeLaserSpectrometerType(ProcessAnalyserType):
    pass


o6.reference(TunableDiodeLaserSpectrometerType, "i=17597", "ns=irdi;s=0112/2///61987#ABP435#002")


@o6.objecttype(nodeId="ns=padim;i=1093", browseName="ns=padim;ZirconiumDioxideAnalyserType", displayName="Zirconium dioxide analyser")
class ZirconiumDioxideAnalyserType(ProcessAnalyserType):
    pass


o6.reference(ZirconiumDioxideAnalyserType, "i=17597", "ns=irdi;s=0112/2///61987#ABP409#002")


@o6.objecttype(nodeId="ns=padim;i=1096", browseName="ns=padim;GasChromatographType", displayName="Gas Chromatograph")
class GasChromatographType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(GasChromatographType, "i=17597", "ns=irdi;s=0112/2///61987#ABP400#002")


@o6.objecttype(nodeId="ns=padim;i=1102", browseName="ns=padim;DiodeArraySpectrometerType", displayName="Diode Array Spectrometer")
class DiodeArraySpectrometerType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(DiodeArraySpectrometerType, "i=17597", "ns=irdi;s=0112/2///61987#ABP433#002")


@o6.objecttype(nodeId="ns=padim;i=1104", browseName="ns=padim;RamanSpectrometerType", displayName="Raman Spectrometer")
class RamanSpectrometerType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(RamanSpectrometerType, "i=17597", "ns=irdi;s=0112/2///61987#ABP434#002")


@o6.objecttype(nodeId="ns=padim;i=1105", browseName="ns=padim;FtnirOrFtirSpectrometerType", displayName="Fourier Transformation NIR or Fourier Transformation IR Spectrometer")
class FtnirOrFtirSpectrometerType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None


o6.reference(FtnirOrFtirSpectrometerType, "i=17597", "ns=irdi;s=0112/2///61987#ABP432#002")


@o6.objecttype(nodeId="ns=padim;i=1223", browseName="ns=padim;TwoStateDiscreteControlSignalType", displayName="TwoStateDiscreteControlSignalType")
class TwoStateDiscreteControlSignalType(SignalType):
    controlSignal: padim_vartypes.TwoStateDiscreteControlVariableType


@o6.objecttype(nodeId="ns=padim;i=1239", browseName="ns=padim;MultiStateDiscreteControlSignalType", displayName="MultiStateDiscreteControlSignalType")
class MultiStateDiscreteControlSignalType(SignalType):
    controlSignal: padim_vartypes.MultiStateDiscreteControlVariableType


@o6.objecttype(nodeId="ns=padim;i=1022", browseName="ns=padim;AnalogSignalType", displayName="AnalogSignalType")
class AnalogSignalType(SignalType):
    analogSignal: padim_vartypes.AnalogSignalVariableType
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=1290", browseName="ns=padim;SignalConditionSet"))
    zeroPointAdjustment: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=padim;i=1109"])


@o6.objecttype(nodeId="ns=padim;i=1065", browseName="ns=padim;AnalyticalSignalType", displayName="AnalyticalSignalType")
class AnalyticalSignalType(AnalogSignalType):
    analogSignal: padim_vartypes.PatMeasurementVariableType


@o6.objecttype(nodeId="ns=padim;i=1066", browseName="ns=padim;AmperometricSignalType", displayName="AmperometricSignalType")
class AmperometricSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1067", browseName="ns=padim;ConductivitySignalType", displayName="ConductivitySignalType")
class ConductivitySignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1069", browseName="ns=padim;FlameIonisationSignalType", displayName="FlameIonisationSignalType")
class FlameIonisationSignalType(AnalyticalSignalType):
    pass


@o6.objecttype(nodeId="ns=padim;i=1071", browseName="ns=padim;NonDispersiveInfraredSignalType", displayName="NonDispersiveInfraredSignalType")
class NonDispersiveInfraredSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1073", browseName="ns=padim;OpticalFluorescenseQuenchingSignalType", displayName="OpticalFluorescenseQuenchingSignalType")
class OpticalFluorescenseQuenchingSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1075", browseName="ns=padim;ParamagneticSignalType", displayName="ParamagneticSignalType")
class ParamagneticSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1076", browseName="ns=padim;PhSignalType", displayName="PhSignalType")
class PhSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1077", browseName="ns=padim;ThermalConductivitySignalType", displayName="ThermalConductivitySignalType")
class ThermalConductivitySignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1078", browseName="ns=padim;TocSignalType", displayName="TocSignalType")
class TocSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1079", browseName="ns=padim;TunableDiodeLaserSignalType", displayName="TunableDiodeLaserSignalType")
class TunableDiodeLaserSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1081", browseName="ns=padim;ZirconiumDioxideSignalType", displayName="ZirconiumDioxideSignalType")
class ZirconiumDioxideSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1107", browseName="ns=padim;AmperometricGasDetectorSignalType", displayName="AmperometricGasDetectorSignalType")
class AmperometricGasDetectorSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1110", browseName="ns=padim;GasChromatographSignalType", displayName="GasChromatographSignalType")
class GasChromatographSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1230", browseName="ns=padim;InfraredSignalType", displayName="InfraredSignalType")
class InfraredSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=padim;i=1232", browseName="ns=padim;CatalyticBeadSignalType", displayName="CatalyticBeadSignalType")
class CatalyticBeadSignalType(AnalyticalSignalType):
    signalConditionSet: ns0.objtypes.BaseObjectType | None


ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1307",
    browseName="ns=padim;CalibrationTimestamp",
    displayName="Timestamp of calibration",
    dataType=o6.DateTime,
    value=o6.DateTime("1601-01-01T00:00:00Z"),
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1307"], "i=17597", "ns=irdi;s=0112/2///61987#ABP544#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1316",
    browseName="ns=di;OperationCycleCounter",
    description="Operation cycle counter is counting the times the Device switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted.",
    displayName="Operation cycle counter",
    dataType=ns0.datatypes.UInteger,
)
o6.reference(o6.ns["ns=padim;i=1316"], "i=17597", "ns=irdi;s=0112/2///61987#ABP545#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1317",
    browseName="ns=di;OperationDuration",
    description="Operation duration is the duration the Device has been powered and performing an activity. This counter is intended for Devices where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for Devices always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
    displayName="Operation duration",
    dataType=ns0.datatypes.Duration,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1317"], "i=17597", "ns=irdi;s=0112/2///61987#ABN639#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1318",
    browseName="ns=di;PowerOnDuration",
    description="Power on duration is the duration the Device has been powered. The main purpose is to determine the time in which degradation of the Device occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the Device has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
    displayName="Power on duration",
    dataType=ns0.datatypes.Duration,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1318"], "i=17597", "ns=irdi;s=0112/2///61987#ABP550#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1323", browseName="ns=padim;SourceResidualLife", displayName="Residual operational life of radiation source", dataType=o6.Float, value=1.0
)
o6.reference(o6.ns["ns=padim;i=1323"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")


@o6.objecttype(
    nodeId="ns=padim;i=1055", browseName="ns=padim;INonDispersiveInfraredSignalConditionSetType", displayName="INonDispersiveInfraredSignalConditionSetType", isAbstract=True
)
class INonDispersiveInfraredSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    absoluteSampleGasPressure: ns0.vartypes.AnalogUnitType | None
    chopperFrequencyDeviation: ns0.vartypes.BaseAnalogType | None
    sampleCellTemperature: ns0.vartypes.AnalogUnitType | None
    sourceResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1323"])


ns0.vartypes.DataItemType(nodeId="ns=padim;i=1347", browseName="ns=padim;TransmissionRatio", displayName="Transmission ratio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1347"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.DataItemType(nodeId="ns=padim;i=1348", browseName="ns=padim;SignalNoiseRatio", displayName="Signal/noise ratio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1348"], "i=17597", "ns=irdi;s=0112/2///61987#ABP581#001")
ns0.vartypes.DataItemType(nodeId="ns=padim;i=1349", browseName="ns=padim;SignalFitQuality", displayName="Signal fit quality", dataType=o6.Float, value=0.0, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1349"], "i=17597", "ns=irdi;s=0112/2///61987#ABP580#001")


@o6.objecttype(nodeId="ns=padim;i=1059", browseName="ns=padim;ITunableDiodeLaserSignalConditionSetType", displayName="ITunableDiodeLaserSignalConditionSetType", isAbstract=True)
class ITunableDiodeLaserSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    absoluteSampleGasPressure: ns0.vartypes.AnalogUnitType | None
    laserTemperature: ns0.vartypes.AnalogUnitType | None
    sampleTemperature: ns0.vartypes.AnalogUnitType | None
    signalFitQuality: ns0.vartypes.DataItemType | None = o6.hasComponent(o6.ns["ns=padim;i=1349"])
    signalNoiseRatio: ns0.vartypes.DataItemType | None = o6.hasComponent(o6.ns["ns=padim;i=1348"])
    transmissionRatio: ns0.vartypes.DataItemType | None = o6.hasComponent(o6.ns["ns=padim;i=1347"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1360", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1360"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1361", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1361"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")


@o6.objecttype(nodeId="ns=padim;i=1061", browseName="ns=padim;IPhSignalConditionSetType", displayName="IPhSignalConditionSetType", isAbstract=True)
class IPhSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    phMeasuringMethod: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    sensingElementImpedance: ns0.vartypes.AnalogUnitType | None
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorCleaningsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1360"])
    sensorNextCalibration: ns0.vartypes.AnalogUnitType | None
    sensorReferenceImpedance: ns0.vartypes.AnalogUnitType | None
    sensorSterilisationsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1361"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1369", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1369"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1370", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1370"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")


@o6.objecttype(nodeId="ns=padim;i=1062", browseName="ns=padim;IConductivitySignalConditionSetType", displayName="IConductivitySignalConditionSetType", isAbstract=True)
class IConductivitySignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    conductivityMeasuringMethod: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorCleaningsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1369"])
    sensorSterilisationsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1370"])
    temperatureCompensationStyle: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1376", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1376"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1377", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1377"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")


@o6.objecttype(nodeId="ns=padim;i=1064", browseName="ns=padim;IAmperometricSignalConditionSetType", displayName="IAmperometricSignalConditionSetType", isAbstract=True)
class IAmperometricSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorCleaningsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1376"])
    sensorNextCalibration: ns0.vartypes.AnalogUnitType | None
    sensorSterilisationsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1377"])


ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1384", browseName="ns=padim;SourceResidualLife", displayName="Residual operational life of radiation source", dataType=o6.Float, value=1.0
)
o6.reference(o6.ns["ns=padim;i=1384"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")


@o6.objecttype(nodeId="ns=padim;i=1056", browseName="ns=padim;ITocSignalConditionSetType", displayName="ITocSignalConditionSetType", isAbstract=True)
class ITocSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    absoluteSampleGasPressure: ns0.vartypes.AnalogUnitType | None
    chopperFrequencyDeviation: ns0.vartypes.BaseAnalogType | None
    detectorZeroSignal: ns0.vartypes.AnalogUnitType | None
    relativeReagentLevel: ns0.vartypes.AnalogUnitType | None
    sampleCellTemperature: ns0.vartypes.AnalogUnitType | None
    sampleGasVolumeFlow: ns0.vartypes.AnalogUnitType | None
    sourceResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1384"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1425", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1425"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")


@o6.objecttype(nodeId="ns=padim;i=1046", browseName="ns=padim;IPhCalibrationType", displayName="IPhCalibrationType", isAbstract=True)
class IPhCalibrationType(ns0.objtypes.BaseInterfaceType):
    sensorAsymmetryPotential: ns0.vartypes.AnalogUnitType | None
    sensorSlope: ns0.vartypes.AnalogUnitType | None
    sensorT90: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1425"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1510", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1510"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")


@o6.objecttype(nodeId="ns=padim;i=1048", browseName="ns=padim;IAmperometricCalibrationType", displayName="IAmperometricCalibrationType", isAbstract=True)
class IAmperometricCalibrationType(ns0.objtypes.BaseInterfaceType):
    absoluteAirPressure: ns0.vartypes.AnalogUnitType | None
    amperometricSensorSlope: ns0.vartypes.AnalogUnitType | None
    amperometricSensorZeroPoint: ns0.vartypes.AnalogUnitType | None
    sensorT90: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1510"])


ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1512", browseName="ns=padim;CalibrationSetpoint", dataType=o6.Float, valueRank=-2)
o6.reference(o6.ns["ns=padim;i=1512"], "i=17597", "ns=irdi;s=<DictionaryEntryName>")
ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1513", browseName="ns=padim;CalibrationActualValue", dataType=o6.Float, valueRank=-2)
o6.reference(o6.ns["ns=padim;i=1513"], "i=17597", "ns=irdi;s=<DictionaryEntryName>")


@o6.objecttype(nodeId="ns=padim;i=1042", browseName="ns=padim;CalibrationPointType", displayName="CalibrationPointType")
class CalibrationPointType(ns0.objtypes.BaseObjectType):
    calibrationActualValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1513"])
    calibrationSetpoint: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1512"])


@o6.objecttype(nodeId="ns=padim;i=1043", browseName="ns=padim;CalibrationPointSetType", displayName="CalibrationPointSetType")
class CalibrationPointSetType(ns0.objtypes.BaseObjectType):
    langleCalibrationPointIdentifierRangle: CalibrationPointType | None = o6.hasComponent(
        CalibrationPointType(nodeId="ns=padim;i=1282", browseName="ns=padim;<CalibrationPointIdentifier>", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(nodeId="ns=padim;i=1045", browseName="ns=padim;ICalibrationType", displayName="ICalibrationType", isAbstract=True)
class ICalibrationType(ns0.objtypes.BaseInterfaceType):
    calibrationPointSet: CalibrationPointSetType | None = o6.hasComponent(CalibrationPointSetType(nodeId="ns=padim;i=1283", browseName="ns=padim;CalibrationPointSet"))
    calibrationTimestamp: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1307"])
    typeOfCalibration: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1519", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1519"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")


@o6.objecttype(
    nodeId="ns=padim;i=1049", browseName="ns=padim;IOpticalFluorescenseQuenchingCalibrationType", displayName="IOpticalFluorescenseQuenchingCalibrationType", isAbstract=True
)
class IOpticalFluorescenseQuenchingCalibrationType(ns0.objtypes.BaseInterfaceType):
    absoluteAirPressure: ns0.vartypes.AnalogUnitType | None
    opticalFluorescenseQuenchingSensorSlope: ns0.vartypes.AnalogUnitType | None
    opticalFluorescenseQuenchingSensorZeroPoint: ns0.vartypes.AnalogUnitType | None
    sensorT90: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1519"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1520", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1520"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1522", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1522"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")


@o6.objecttype(
    nodeId="ns=padim;i=1063",
    browseName="ns=padim;IOpticalFluorescenseQuenchingSignalConditionSetType",
    displayName="IOpticalFluorescenseQuenchingSignalConditionSetType",
    isAbstract=True,
)
class IOpticalFluorescenseQuenchingSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorCleaningsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1520"])
    sensorNextCalibration: ns0.vartypes.AnalogUnitType | None
    sensorSterilisationsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1522"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1529", browseName="ns=padim;ResidualLife", displayName="Residual operational life", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=1529"], "i=17597", "ns=irdi;s=0112/2///61987#ABP595#001")


@o6.objecttype(
    nodeId="ns=padim;i=1051", browseName="ns=padim;GeneralDeviceConditionSetType", displayName="GeneralDeviceConditionSetType", interfaces=[di.objtypes.IOperationCounterType]
)
class GeneralDeviceConditionSetType(ns0.objtypes.BaseObjectType):
    internalTemperature: ns0.vartypes.AnalogUnitType | None
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1316"])
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1317"])
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1318"])
    residualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1529"])


@o6.objecttype(nodeId="ns=padim;i=1044", browseName="ns=padim;IGeneralDeviceConditionSetType", displayName="IGeneralDeviceConditionSetType", isAbstract=True)
class IGeneralDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    deviceComponentConditions: ns0.objtypes.BaseObjectType | None
    generalDeviceConditions: GeneralDeviceConditionSetType | None = o6.hasComponent(
        GeneralDeviceConditionSetType(nodeId="ns=padim;i=1279", browseName="ns=padim;GeneralDeviceConditions")
    )


@o6.objecttype(nodeId="ns=padim;i=1097", browseName="ns=padim;InfraredSensorType", displayName="Infrared Sensor")
class InfraredSensorType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5010", browseName="ns=padim;DeviceConditionSet"))


o6.reference(InfraredSensorType, "i=17597", "ns=irdi;s=0112/2///61987#ABP413#002")


@o6.objecttype(nodeId="ns=padim;i=1098", browseName="ns=padim;AmperometricGasDetectorType", displayName="Amperometric Gas Detector")
class AmperometricGasDetectorType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5020", browseName="ns=padim;DeviceConditionSet"))


o6.reference(AmperometricGasDetectorType, "i=17597", "ns=irdi;s=0112/2///61987#ABP415#002")


@o6.objecttype(nodeId="ns=padim;i=1099", browseName="ns=padim;CatalyticBeadSensorType", displayName="Catalytic Bead Sensor")
class CatalyticBeadSensorType(ProcessAnalyserType):
    deviceConditionSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5030", browseName="ns=padim;DeviceConditionSet"))


o6.reference(CatalyticBeadSensorType, "i=17597", "ns=irdi;s=0112/2///61987#ABP412#002")


ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5074", browseName="ns=padim;<SignalCalibrationIdentifier>", modellingRule="OptionalPlaceholder")
o6.reference(o6.ns["ns=padim;i=5074"], "i=17603", ICalibrationType)


@o6.objecttype(nodeId="ns=padim;i=1114", browseName="ns=padim;FtnirOrFtirSignalType", displayName="FtnirOrFtirSignalType")
class FtnirOrFtirSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=padim;i=5074"])
    signalConditionSet: ns0.objtypes.BaseObjectType | None


ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5076", browseName="ns=padim;<SignalCalibrationIdentifier>", modellingRule="OptionalPlaceholder")
o6.reference(o6.ns["ns=padim;i=5076"], "i=17603", ICalibrationType)


@o6.objecttype(nodeId="ns=padim;i=1150", browseName="ns=padim;DiodeArraySignalType", displayName="DiodeArraySignalType")
class DiodeArraySignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=padim;i=5076"])
    signalConditionSet: ns0.objtypes.BaseObjectType | None


ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=5078", browseName="ns=padim;<SignalCalibrationIdentifier>", modellingRule="OptionalPlaceholder")
o6.reference(o6.ns["ns=padim;i=5078"], "i=17603", ICalibrationType)


@o6.objecttype(nodeId="ns=padim;i=1227", browseName="ns=padim;RamanSignalType", displayName="RamanSignalType")
class RamanSignalType(AnalyticalSignalType):
    langleSignalCalibrationIdentifierRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=padim;i=5078"])
    signalConditionSet: ns0.objtypes.BaseObjectType | None


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6000", browseName="ns=padim;CalibrationRange1ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6000"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ024#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6005", browseName="ns=padim;CalibrationRange2ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6005"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ027#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6010", browseName="ns=padim;CalibrationRange3ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6010"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ030#001")


@o6.objecttype(nodeId="ns=padim;i=1094", browseName="ns=padim;IGasChromatographCalibrationType", displayName="IGasChromatographCalibrationType", isAbstract=True)
class IGasChromatographCalibrationType(ns0.objtypes.BaseInterfaceType):
    calibrationRange1LowerRangeValue: ns0.vartypes.AnalogUnitType | None
    calibrationRange1ResponseFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6000"])
    calibrationRange1UpperRangeValue: ns0.vartypes.AnalogUnitType | None
    calibrationRange2LowerRangeValue: ns0.vartypes.AnalogUnitType | None
    calibrationRange2ResponseFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6005"])
    calibrationRange2UpperRangeValue: ns0.vartypes.AnalogUnitType | None
    calibrationRange3LowerRangeValue: ns0.vartypes.AnalogUnitType | None
    calibrationRange3ResponseFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6010"])
    calibrationRange3UpperRangeValue: ns0.vartypes.AnalogUnitType | None


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6015", browseName="ns=padim;ValveName", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
o6.reference(o6.ns["ns=padim;i=6015"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ046#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6016", browseName="ns=padim;ValveSwitchingCyclesCounter", dataType=o6.UInt32, valueRank=1, arrayDimensions=[1], value=[0])
o6.reference(o6.ns["ns=padim;i=6016"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ007#001")


@o6.objecttype(nodeId="ns=padim;i=1095", browseName="ns=padim;IGasChromatographDeviceConditionSetType", displayName="IGasChromatographDeviceConditionSetType", isAbstract=True)
class IGasChromatographDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    baselineNoise: ns0.vartypes.AnalogUnitType | None
    totalAreaMeasuredPeaks: ns0.vartypes.AnalogUnitType | None
    valveName: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6015"])
    valveSwitchingCyclesCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6016"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6040", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6040"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6041", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6041"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")


@o6.objecttype(nodeId="ns=padim;i=1100", browseName="ns=padim;IFtnirOrFtirDeviceConditionSetType", displayName="IFtnirOrFtirDeviceConditionSetType", isAbstract=True)
class IFtnirOrFtirDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    remainingDataStorageCapacity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6041"])
    watchdog: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6040"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6042", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6042"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6043", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6043"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")


@o6.objecttype(nodeId="ns=padim;i=1101", browseName="ns=padim;IDiodeArrayDeviceConditionSetType", displayName="IDiodeArrayDeviceConditionSetType", isAbstract=True)
class IDiodeArrayDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    remainingDataStorageCapacity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6043"])
    watchdog: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6042"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6052", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6052"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6053", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6053"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")


@o6.objecttype(nodeId="ns=padim;i=1103", browseName="ns=padim;IRamanDeviceConditionSetType", displayName="IRamanDeviceConditionSetType", isAbstract=True)
class IRamanDeviceConditionSetType(ns0.objtypes.BaseInterfaceType):
    remainingDataStorageCapacity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6053"])
    watchdog: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6052"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6074", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6074"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6075", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6075"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6076", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6076"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6077", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6077"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6078", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6078"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6079", browseName="ns=padim;ConsumedSensorCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6079"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ018#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6080", browseName="ns=padim;RangeExceedancePeakValue", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6080"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ019#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6081", browseName="ns=padim;RangeExceedanceDuration", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6081"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ020#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6082", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6082"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")


@o6.objecttype(
    nodeId="ns=padim;i=1106", browseName="ns=padim;IAmperometricGasDetectorSignalConditionSetType", displayName="IAmperometricGasDetectorSignalConditionSetType", isAbstract=True
)
class IAmperometricGasDetectorSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    consumedSensorCapacity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6079"])
    powerOnDurationSensor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6076"])
    rangeExceedanceDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6081"])
    rangeExceedancePeakValue: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6080"])
    relativeGasFlowRate: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6078"])
    sensingElementResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6077"])
    sensingElementResidualSensitivity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6082"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorNextCalibrationDynamic: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6075"])
    sensorNextCalibrationFixed: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6074"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6125", browseName="ns=padim;TailingFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6125"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ033#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6130", browseName="ns=padim;InjectionTime", dataType=o6.DateTime, value=o6.DateTime("1601-01-01T00:00:00Z"))
o6.reference(o6.ns["ns=padim;i=6130"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ006#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6131", browseName="ns=padim;ComponentName", dataType=o6.String)
o6.reference(o6.ns["ns=padim;i=6131"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ045#001")


@o6.objecttype(nodeId="ns=padim;i=1108", browseName="ns=padim;IGasChromatographSignalConditionSetType", displayName="IGasChromatographSignalConditionSetType", isAbstract=True)
class IGasChromatographSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    actualRetentionTime: ns0.vartypes.AnalogUnitType | None
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6131"])
    expectedRetentionTime: ns0.vartypes.AnalogUnitType | None
    injectionTime: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6130"])
    peakArea: ns0.vartypes.AnalogUnitType | None
    peakHeight: ns0.vartypes.AnalogUnitType | None
    peakWidth: ns0.vartypes.AnalogUnitType | None
    tailingFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6125"])


ns0.vartypes.DataItemType(nodeId="ns=padim;i=6168", browseName="ns=padim;TransmissionRatio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6168"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6171", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6171"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6172", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6172"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6173", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6173"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6174", browseName="ns=padim;LaserResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6174"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ044#001")


@o6.objecttype(nodeId="ns=padim;i=1112", browseName="ns=padim;IFtnirOrFtirSignalConditionSetType", displayName="IFtnirOrFtirSignalConditionSetType", isAbstract=True)
class IFtnirOrFtirSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    electronicsReadNoise: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6173"])
    laserResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6174"])
    mahalanobisDistance: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6171"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    spectralResidual: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6172"])
    transmissionRatio: ns0.vartypes.DataItemType | None = o6.hasComponent(o6.ns["ns=padim;i=6168"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6187", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6187"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6190", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6190"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6191", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6191"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6192", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6192"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")


@o6.objecttype(nodeId="ns=padim;i=1146", browseName="ns=padim;IDiodeArraySignalConditionSetType", displayName="IDiodeArraySignalConditionSetType", isAbstract=True)
class IDiodeArraySignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    electronicsReadNoise: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6192"])
    mahalanobisDistance: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6190"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sourceResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6187"])
    spectralResidual: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6191"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6206", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6206"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6209", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6209"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6210", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6210"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6211", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6211"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")


@o6.objecttype(nodeId="ns=padim;i=1154", browseName="ns=padim;IRamanSignalConditionSetType", displayName="IRamanSignalConditionSetType", isAbstract=True)
class IRamanSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    electronicsReadNoise: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6211"])
    mahalanobisDistance: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6209"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sourceResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6206"])
    spectralResidual: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6210"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6228", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6228"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ041#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6229", browseName="ns=padim;TransmissionRatio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6229"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6230", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6230"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6231", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6231"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6232", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6232"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6233", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6233"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6234", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6234"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6235", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6235"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")


@o6.objecttype(nodeId="ns=padim;i=1229", browseName="ns=padim;IInfraredSignalConditionSetType", displayName="IInfraredSignalConditionSetType", isAbstract=True)
class IInfraredSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    powerOnDurationSensor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6232"])
    relativeGasFlowRate: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6234"])
    sensingElementResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6233"])
    sensingElementResidualSensitivity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6235"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorNextCalibrationDynamic: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6231"])
    sensorNextCalibrationFixed: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6230"])
    sourceResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6228"])
    transmissionRatio: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6229"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6250", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6250"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")


@o6.objecttype(nodeId="ns=padim;i=1060", browseName="ns=padim;IZirconiumDioxideSignalConditionSetType", displayName="IZirconiumDioxideSignalConditionSetType", isAbstract=True)
class IZirconiumDioxideSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    cellResistance: ns0.vartypes.AnalogUnitType | None
    relativeHeatOutput: ns0.vartypes.AnalogUnitType | None
    sampleGasVolumeFlow: ns0.vartypes.AnalogUnitType | None
    sensingElementResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6250"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None


ns0.vartypes.PropertyType(nodeId="ns=padim;i=6255", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6255"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6256", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6256"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6257", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6257"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6258", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6258"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6259", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6259"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6262", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6262"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")


@o6.objecttype(nodeId="ns=padim;i=1231", browseName="ns=padim;ICatalyticBeadSignalConditionSetType", displayName="ICatalyticBeadSignalConditionSetType", isAbstract=True)
class ICatalyticBeadSignalConditionSetType(ns0.objtypes.BaseInterfaceType):
    powerOnDurationSensor: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6257"])
    relativeGasFlowRate: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6259"])
    sensingElementResidualLife: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6258"])
    sensingElementResidualSensitivity: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6262"])
    sensingElementTemperature: ns0.vartypes.AnalogUnitType | None
    sensorNextCalibrationDynamic: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6256"])
    sensorNextCalibrationFixed: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=6255"])
    sensorValue: ns0.vartypes.AnalogUnitType | None


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim_datypes, padim_vartypes
