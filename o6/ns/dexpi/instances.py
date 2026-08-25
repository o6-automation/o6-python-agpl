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

"""Generated OPC UA dexpi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as dexpi_reftypes
from . import datatypes as dexpi_datypes
from . import objtypes as dexpi_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1001",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NoSiphon"), o6.LocalizedText("Siphon")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1003",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("DualFlowPipingNetworkSegment"), o6.LocalizedText("SingleFlowPipingNetworkSegment")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1005",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("GuaranteedSupplyFunction"), o6.LocalizedText("NonGuaranteedSupplyFunction")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1007",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("FireResistantArtefact"), o6.LocalizedText("NonFireResistantArtefact")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1009",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NotOnHold"), o6.LocalizedText("OnHold")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1011",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NonQualityRelevantFunction"), o6.LocalizedText("QualityRelevantFunction")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1013",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("ConfidentialInformation"), o6.LocalizedText("NonConfidentialInformation")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1015",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("ExplosionProofArtefact"), o6.LocalizedText("NonExplosionProofArtefact")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1017",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NoPipingClassBreak"), o6.LocalizedText("PipingClassBreak")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1019",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[44],
    value=[
        o6.LocalizedText("Class10000PsiArtefact"),
        o6.LocalizedText("Class1000KpaArtefact"),
        o6.LocalizedText("Class125LbsArtefact"),
        o6.LocalizedText("Class15000PsiArtefact"),
        o6.LocalizedText("Class1500LbsArtefact"),
        o6.LocalizedText("Class150LbsArtefact"),
        o6.LocalizedText("Class16BarArtefact"),
        o6.LocalizedText("Class20000PsiArtefact"),
        o6.LocalizedText("Class2000PsiArtefact"),
        o6.LocalizedText("Class2500LbsArtefact"),
        o6.LocalizedText("Class250PsiArtefact"),
        o6.LocalizedText("Class3000PsiArtefact"),
        o6.LocalizedText("Class300LbsArtefact"),
        o6.LocalizedText("Class300PsiArtefact"),
        o6.LocalizedText("Class315BarArtefact"),
        o6.LocalizedText("Class345BarArtefact"),
        o6.LocalizedText("Class350BarArtefact"),
        o6.LocalizedText("Class4000PsiArtefact"),
        o6.LocalizedText("Class400LbsArtefact"),
        o6.LocalizedText("Class4500LbsArtefact"),
        o6.LocalizedText("Class4500PsiArtefact"),
        o6.LocalizedText("Class5000PsiArtefact"),
        o6.LocalizedText("Class50BarArtefact"),
        o6.LocalizedText("Class517BarArtefact"),
        o6.LocalizedText("Class6000PsiArtefact"),
        o6.LocalizedText("Class600LbsArtefact"),
        o6.LocalizedText("Class690BarArtefact"),
        o6.LocalizedText("Class800LbsArtefact"),
        o6.LocalizedText("Class800PsiArtefact"),
        o6.LocalizedText("Class850KpaArtefact"),
        o6.LocalizedText("Class9000LbsArtefact"),
        o6.LocalizedText("Class900LbsArtefact"),
        o6.LocalizedText("En1333Pn100Artefact"),
        o6.LocalizedText("En1333Pn10Artefact"),
        o6.LocalizedText("En1333Pn160Artefact"),
        o6.LocalizedText("En1333Pn16Artefact"),
        o6.LocalizedText("En1333Pn2,5Artefact"),
        o6.LocalizedText("En1333Pn250Artefact"),
        o6.LocalizedText("En1333Pn25Artefact"),
        o6.LocalizedText("En1333Pn320Artefact"),
        o6.LocalizedText("En1333Pn400Artefact"),
        o6.LocalizedText("En1333Pn40Artefact"),
        o6.LocalizedText("En1333Pn63Artefact"),
        o6.LocalizedText("En1333Pn6Artefact"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1021",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("GmpRelevantFunction"), o6.LocalizedText("NonGmpRelevantFunction")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1023",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("FourPortValve"), o6.LocalizedText("ThreePortValve"), o6.LocalizedText("TwoPortValve")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1025",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("DetonationProofArtefact"), o6.LocalizedText("NonDetonationProofArtefact")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1027",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("CompositionBreak"), o6.LocalizedText("NoCompositionBreak")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1029",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("MainFlowInNode"), o6.LocalizedText("MainFlowOutNode")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1031",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("InsulationBreak"), o6.LocalizedText("NoInsulationBreak")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1033",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[65],
    value=[
        o6.LocalizedText("Din2448ObjectDn100"),
        o6.LocalizedText("Din2448ObjectDn125"),
        o6.LocalizedText("Din2448ObjectDn15"),
        o6.LocalizedText("Din2448ObjectDn150"),
        o6.LocalizedText("Din2448ObjectDn20"),
        o6.LocalizedText("Din2448ObjectDn200"),
        o6.LocalizedText("Din2448ObjectDn25"),
        o6.LocalizedText("Din2448ObjectDn32"),
        o6.LocalizedText("Din2448ObjectDn40"),
        o6.LocalizedText("Din2448ObjectDn50"),
        o6.LocalizedText("Din2448ObjectDn65"),
        o6.LocalizedText("Din2448ObjectDn80"),
        o6.LocalizedText("Iso6708ObjectDn100"),
        o6.LocalizedText("Iso6708ObjectDn1000"),
        o6.LocalizedText("Iso6708ObjectDn1200"),
        o6.LocalizedText("Iso6708ObjectDn125"),
        o6.LocalizedText("Iso6708ObjectDn1400"),
        o6.LocalizedText("Iso6708ObjectDn15"),
        o6.LocalizedText("Iso6708ObjectDn150"),
        o6.LocalizedText("Iso6708ObjectDn1600"),
        o6.LocalizedText("Iso6708ObjectDn20"),
        o6.LocalizedText("Iso6708ObjectDn200"),
        o6.LocalizedText("Iso6708ObjectDn25"),
        o6.LocalizedText("Iso6708ObjectDn250"),
        o6.LocalizedText("Iso6708ObjectDn300"),
        o6.LocalizedText("Iso6708ObjectDn32"),
        o6.LocalizedText("Iso6708ObjectDn350"),
        o6.LocalizedText("Iso6708ObjectDn40"),
        o6.LocalizedText("Iso6708ObjectDn400"),
        o6.LocalizedText("Iso6708ObjectDn450"),
        o6.LocalizedText("Iso6708ObjectDn50"),
        o6.LocalizedText("Iso6708ObjectDn500"),
        o6.LocalizedText("Iso6708ObjectDn600"),
        o6.LocalizedText("Iso6708ObjectDn65"),
        o6.LocalizedText("Iso6708ObjectDn700"),
        o6.LocalizedText("Iso6708ObjectDn80"),
        o6.LocalizedText("Iso6708ObjectDn800"),
        o6.LocalizedText("Iso6708ObjectDn900"),
        o6.LocalizedText("Nps1/2Artefact"),
        o6.LocalizedText("Nps1/4Artefact"),
        o6.LocalizedText("Nps10Artefact"),
        o6.LocalizedText("Nps12Artefact"),
        o6.LocalizedText("Nps14Artefact"),
        o6.LocalizedText("Nps16Artefact"),
        o6.LocalizedText("Nps18Artefact"),
        o6.LocalizedText("Nps1Artefact"),
        o6.LocalizedText("Nps1_1/2Artefact"),
        o6.LocalizedText("Nps1_1/4Artefact"),
        o6.LocalizedText("Nps20Artefact"),
        o6.LocalizedText("Nps24Artefact"),
        o6.LocalizedText("Nps2Artefact"),
        o6.LocalizedText("Nps2_1/2Artefact"),
        o6.LocalizedText("Nps3/4Artefact"),
        o6.LocalizedText("Nps30Artefact"),
        o6.LocalizedText("Nps36Artefact"),
        o6.LocalizedText("Nps3Artefact"),
        o6.LocalizedText("Nps3_1/2Artefact"),
        o6.LocalizedText("Nps42Artefact"),
        o6.LocalizedText("Nps48Artefact"),
        o6.LocalizedText("Nps4Artefact"),
        o6.LocalizedText("Nps54Artefact"),
        o6.LocalizedText("Nps5Artefact"),
        o6.LocalizedText("Nps60Artefact"),
        o6.LocalizedText("Nps6Artefact"),
        o6.LocalizedText("Nps8Artefact"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1035",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("SlopedPipingNetworkSegment"), o6.LocalizedText("UnslopedPipingNetworkSegment")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1037",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NonPipingClassArtefact"), o6.LocalizedText("PipingClassArtefact")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1039",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("ElectricalHeatTracingSystem"),
        o6.LocalizedText("HeatTracingSystem"),
        o6.LocalizedText("NoHeatTracingSystem"),
        o6.LocalizedText("SteamHeatTracingSystem"),
        o6.LocalizedText("TubularHeatTracingSystem"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1041",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("CapillarySignalConveying"),
        o6.LocalizedText("ConductedRadiationSignalConveying"),
        o6.LocalizedText("ElectricalSignalConveying"),
        o6.LocalizedText("HydraulicSignalConveying"),
        o6.LocalizedText("PneumaticSignalConveying"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1043",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("PrimaryPipingNetworkSegment"), o6.LocalizedText("SecondaryPipingNetworkSegment")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1045",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Cooling"), o6.LocalizedText("Heating"), o6.LocalizedText("Processing"), o6.LocalizedText("Tempering")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1047",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("ContinuousOperation"), o6.LocalizedText("IntermittentOperation")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1049",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NoNominalDiameterBreak"), o6.LocalizedText("NominalDiameterBreak")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1051",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("FailClose"), o6.LocalizedText("FailOpen"), o6.LocalizedText("FailRetainPosition")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1053",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("JacketedPipe"), o6.LocalizedText("UnjacketedPipe")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1055",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CentralLocation"), o6.LocalizedText("ControlPanel"), o6.LocalizedText("Field")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=dexpi;i=1057",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=dexpi;i=1056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("StatusHighHighHighPort"),
        o6.LocalizedText("StatusHighHighPort"),
        o6.LocalizedText("StatusHighPort"),
        o6.LocalizedText("StatusLowLowLowPort"),
        o6.LocalizedText("StatusLowLowPort"),
        o6.LocalizedText("StatusLowPort"),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1228",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the OfflinePrimaryElement.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1229",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1230", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.OfflinePrimaryElementType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1228"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1236",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the OfflinePrimaryElement.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1237",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1238", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.OfflinePrimaryElementType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1236"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1313",
    browseName="ns=dexpi;DesignCapacityMotiveFluid",
    description="The design capacity for the motive fluid of the EjectorPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1314",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1315", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.EjectorPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1313"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1317",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the Kneader.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1318",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1319", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.KneaderType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1317"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1320",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the Kneader.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1321",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1322", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.KneaderType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1320"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1323",
    browseName="ns=dexpi;UpperLimitAllowableDesignPressureDrop",
    description="The maximum allowable design pressure drop of the Kneader.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1324",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1325", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.KneaderType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1323"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1327",
    browseName="ns=dexpi;DesignHeatFlowRate",
    description="The heat flow rate for which the HeatExchanger is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1328",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1329", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.HeatExchangerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1327"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1330",
    browseName="ns=dexpi;DesignHeatTransferArea",
    description="The design heat transfer area of the HeatExchanger.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1331",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Area")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1332", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.HeatExchangerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1330"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1333",
    browseName="ns=dexpi;DesignHeatTransferCoefficient",
    description="The design heat transfer coefficient of the HeatExchanger.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1334",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("HeatTransferCoefficient")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1335", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.HeatExchangerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1333"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1343",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the RotaryPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1344",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1345", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1343"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1346",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the RotaryPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1347",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1348", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1346"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1351",
    browseName="ns=dexpi;DesignPower",
    description="The design power of the ThinFilmEvaporator.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1352",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1353", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ThinFilmEvaporatorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1351"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1354",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the ThinFilmEvaporator.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1355",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1356", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ThinFilmEvaporatorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1354"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1357",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the ThinFilmEvaporator.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1358",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1359", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ThinFilmEvaporatorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1357"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1371",
    browseName="ns=dexpi;Height",
    description="The height of the ColumnPackingsArrangement.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1372",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1373", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ColumnPackingsArrangementType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1371"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1380",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the ReciprocatingCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1381",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1382", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ReciprocatingCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1380"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1383",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the ReciprocatingCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1384",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1385", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ReciprocatingCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1383"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1388",
    browseName="ns=dexpi;DesignCapacityMotiveFluid",
    description="The design capacity for the motive fluid of the SpecialCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1389",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1390", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1388"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1391",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the SpecialCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1392",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1393", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1391"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1394",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the SpecialCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1395",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1396", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1394"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1401",
    browseName="ns=dexpi;Height",
    description="The height of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1402",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1403", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SubTaggedColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1401"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1404",
    browseName="ns=dexpi;InsideDiameter",
    description="The inside diameter of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1405",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1406", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SubTaggedColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1404"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1409",
    browseName="ns=dexpi;DesignVolumeFlowRate",
    description="The volume flow rate for which the Compressor is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1410",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1411", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1409"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1412",
    browseName="ns=dexpi;DifferentialPressure",
    description="The differential pressure of the Compressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1413",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1414", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1412"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1416",
    browseName="ns=dexpi;UpperLimitAllowableDesignPressureDrop",
    description="The maximum allowable design pressure drop of the RotaryMixer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1417",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1418", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryMixerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1416"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1419",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the RotaryMixer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1420",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1421", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryMixerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1419"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1422",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the RotaryMixer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1423",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1424", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryMixerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1422"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1426",
    browseName="ns=dexpi;NominalCapacityVolume",
    description="The nominal volumetric capacity of the Vessel.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1427",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Volume")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1428", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.VesselType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1426"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1432",
    browseName="ns=dexpi;Capacity_VolumeFlowRate",
    description="The handling flow rate for which the GasFilter is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1433",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1434", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.GasFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1432"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1435",
    browseName="ns=dexpi;UpperLimitAllowableDesignPressureDrop",
    description="The maximum allowable design pressure drop of the GasFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1436",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1437", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.GasFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1435"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1438",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the GasFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1439",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1440", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.GasFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1438"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1441",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the GasFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1442",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1443", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.GasFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1441"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1446",
    browseName="ns=dexpi;CylinderLength",
    description="The cylinder length of the PressureVessel.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1447",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1448", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PressureVesselType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1446"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1450",
    browseName="ns=dexpi;CylinderLength",
    description="The cylinder length of the SpecialVessel.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1451",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1452", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialVesselType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1450"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1458",
    browseName="ns=dexpi;Efficiency",
    description="The efficiency of the FilterUnit.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1459",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Percentage")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1460", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1458"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1461",
    browseName="ns=dexpi;FilterArea",
    description="The filter area of the FilterUnit.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1462",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Area")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1463", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1461"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1464",
    browseName="ns=dexpi;LowerLimitAllowableSolidsConcentration",
    description="The minimum allowable concentration for solids.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1465",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Percentage")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1466", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1464"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1467",
    browseName="ns=dexpi;LowerLimitPermeableParticleDiameter",
    description="The minimum of the particle size.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1468",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1469", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1467"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1472",
    browseName="ns=dexpi;UpperLimitAllowableSolidsConcentration",
    description="The maximum allowable concentration for solids.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1473",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Percentage")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1474", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1472"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1475",
    browseName="ns=dexpi;UpperLimitPermeableParticleDiameter",
    description="The maximum of the particle size.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1476",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1477", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1475"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1479",
    browseName="ns=dexpi;DesignPower",
    description="The design power of the AirCoolingSystem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1480",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1481", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AirCoolingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1479"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1482",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the AirCoolingSystem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1483",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1484", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AirCoolingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1482"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1485",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the AirCoolingSystem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1486",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1487", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AirCoolingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1485"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1495",
    browseName="ns=dexpi;Height",
    description="The height of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1496",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1497", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1495"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1498",
    browseName="ns=dexpi;InsideDiameter",
    description="The inside diameter of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1499",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1500", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1498"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1504",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the ReciprocatingPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1505",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1506", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ReciprocatingPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1504"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1507",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the ReciprocatingPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1508",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1509", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ReciprocatingPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1507"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1516",
    browseName="ns=dexpi;Height",
    description="The height of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1517",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1518", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.TaggedColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1516"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1519",
    browseName="ns=dexpi;InsideDiameter",
    description="The inside diameter of the ColumnSection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1520",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1521", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.TaggedColumnSectionType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1519"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1528",
    browseName="ns=dexpi;Height",
    description="The height of the Chamber.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1529",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1530", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1528"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1531",
    browseName="ns=dexpi;InsideDiameter",
    description="The inside diameter of the Chamber.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1532",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1533", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1531"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1534",
    browseName="ns=dexpi;Length",
    description="The length of the Chamber.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1535",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1536", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1534"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1537",
    browseName="ns=dexpi;LowerLimitDesignPressure",
    description="The lowest pressure for which the Chamber is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1538",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1539", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1537"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1540",
    browseName="ns=dexpi;LowerLimitDesignTemperature",
    description="The lowest temperature for which the Chamber is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1541",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1542", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1540"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1544",
    browseName="ns=dexpi;NominalDiameter",
    description="The nominal diameter of the Chamber, given as a length. See also <owner.NominalDiameterTypeRepresentationClass>.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1545",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1546", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1544"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1548",
    browseName="ns=dexpi;UpperLimitDesignPressure",
    description="The highest pressure for which the Chamber is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1549",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1550", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1548"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1551",
    browseName="ns=dexpi;UpperLimitDesignTemperature",
    description="The highest temperature for which the Chamber is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1552",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1553", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1551"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1554",
    browseName="ns=dexpi;Width",
    description="The width of the Chamber.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1555",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1556", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1554"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1558",
    browseName="ns=dexpi;DesignPower",
    description="The design power of the ElectricHeater.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1559",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1560", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ElectricHeaterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1558"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1567",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the CentrifugalCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1568",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1569", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CentrifugalCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1567"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1570",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the CentrifugalCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1571",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1572", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CentrifugalCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1570"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1578",
    browseName="ns=dexpi;PlateHeight",
    description="The height of the plates in the PlateAndShellHeatExchanger.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1579",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1580", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PlateAndShellHeatExchangerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1578"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1581",
    browseName="ns=dexpi;PlateWidth",
    description="The width of the plates in the PlateAndShellHeatExchanger.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1582",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1583", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PlateAndShellHeatExchangerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1581"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1585",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the CentrifugalPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1586",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1587", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CentrifugalPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1585"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1588",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the CentrifugalPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1589",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1590", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CentrifugalPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1588"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1594",
    browseName="ns=dexpi;TubeLength",
    description="The length of the tubes of the TubeBundle.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1595",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1596", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.TubeBundleType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1594"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1609",
    browseName="ns=dexpi;DesignCapacityMotiveFluid",
    description="The design capacity for the motive fluid of the SpecialPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1610",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1611", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1609"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1612",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the SpecialPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1613",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1614", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1612"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1615",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the SpecialPump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1616",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1617", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SpecialPumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1615"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1621",
    browseName="ns=dexpi;DesignCapacityMotiveFluid",
    description="The design capacity for the motive fluid of the AirEjector.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1622",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1623", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AirEjectorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1621"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1626",
    browseName="ns=dexpi;UpperLimitAllowableDesignPressureDrop",
    description="The maximum allowable design pressure drop of the StaticMixer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1627",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1628", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.StaticMixerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1626"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1630",
    browseName="ns=dexpi;Diameter",
    description="The diameter of the Impeller.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1631",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1632", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ImpellerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1630"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1638",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the Agitator.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1639",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1640", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AgitatorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1638"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1641",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the Agitator.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1642",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1643", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AgitatorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1641"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1646",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the AxialCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1647",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1648", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AxialCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1646"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1649",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the AxialCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1650",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1651", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AxialCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1649"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1659",
    browseName="ns=dexpi;VolumePerStroke",
    description="The volume per stroke of the Displacer.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1660",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Volume")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1661", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.DisplacerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1659"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1664",
    browseName="ns=dexpi;CylinderLength",
    description="The cylinder length of the Tank.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1665",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1666", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.TankType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1664"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1668",
    browseName="ns=dexpi;NominalCapacityVolume",
    description="The nominal volumetric capacity of the ProcessColumn.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1669",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Volume")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1670", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ProcessColumnType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1668"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1673",
    browseName="ns=dexpi;Diameter",
    description="The diameter of the AgitatorRotor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1674",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1675", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AgitatorRotorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1673"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1676",
    browseName="ns=dexpi;LengthToMountingFlange",
    description="The length to the mounting flange of the AgitatorRotor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1677",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1678", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.AgitatorRotorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1676"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1695",
    browseName="ns=dexpi;Capacity_VolumeFlowRate",
    description="The handling flow rate for which the LiquidFilter is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1696",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1697", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.LiquidFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1695"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1698",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the LiquidFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1699",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1700", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.LiquidFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1698"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1701",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the LiquidFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1702",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1703", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.LiquidFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1701"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1704",
    browseName="ns=dexpi;UpperLimitAllowableDesignPressureDrop",
    description="The maximum allowable design pressure drop of the LiquidFilter.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1705",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1706", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.LiquidFilterType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1704"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1709",
    browseName="ns=dexpi;DesignRotationalSpeed",
    description="The design rotational speed of the RotaryCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1710",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("RotationalSpeed")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1711", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1709"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1712",
    browseName="ns=dexpi;DesignShaftPower",
    description="The design shaft power of the RotaryCompressor.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1713",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Power")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1714", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.RotaryCompressorType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1712"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1717",
    browseName="ns=dexpi;DesignVolumeFlowRate",
    description="The volume flow rate for which the Pump is designed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1718",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("VolumeFlowRate")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1719", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1717"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1720",
    browseName="ns=dexpi;DesignPressureHead",
    description="The design pressure head of the Pump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1721",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1722", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1720"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1723",
    browseName="ns=dexpi;DifferentialPressure",
    description="The differential pressure of the Pump.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1724",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1725", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PumpType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1723"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1729",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipingNetworkSystem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1730",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1731", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSystemType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1729"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1733",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipingNetworkSystem.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1734",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1735", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSystemType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1733"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1759",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1760",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1761", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.StrainerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1759"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1764",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1765",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1766", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.StrainerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1764"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1777",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the CheckValve.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1778",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1779", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CheckValveType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1777"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1781",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the CheckValve.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1782",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1783", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.CheckValveType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1781"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1795",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the InlinePrimaryElement.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1796",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1797", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.InlinePrimaryElementType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1795"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1800",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the InlinePrimaryElement.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1801",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1802", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.InlinePrimaryElementType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1800"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1814",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1815",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1816", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SteamTrapType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1814"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1819",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1820",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1821", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SteamTrapType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1819"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1834",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1835",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1836", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SilencerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1834"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1839",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1840",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1841", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SilencerType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1839"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1849",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the ShutOffValve.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1850",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1851", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ShutOffValveType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1849"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1853",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the ShutOffValve.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1854",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1855", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.ShutOffValveType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1853"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1879",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1880",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1881", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipeFittingType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1879"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1884",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1885",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1886", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipeFittingType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1884"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1906",
    browseName="ns=dexpi;Inclination",
    description="The inclination (slope) of the PipingNetworkSegment in percent.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1907",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Percentage")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1908", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSegmentType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1906"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1909",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipingNetworkSegment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1910",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1911", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSegmentType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1909"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1914",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipingNetworkSegment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1915",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1916", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSegmentType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1914"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1922",
    browseName="ns=dexpi;OperatingTemperature",
    description="The operating temperature of the PipingNetworkSegment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1923",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1924", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.PipingNetworkSegmentType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1922"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1949",
    browseName="ns=dexpi;SetPressureLow",
    description="The low pressure at which the SafetyValveOrFitting is activated.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1950",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1951", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SafetyValveOrFittingType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1949"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1952",
    browseName="ns=dexpi;SetPressureHigh",
    description="The high pressure at which the SafetyValveOrFitting is activated.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1953",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Pressure")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1954", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.SafetyValveOrFittingType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1952"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1960",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1961",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1962", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.VentilationDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1960"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1965",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1966",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1967", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.VentilationDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1965"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1978",
    browseName="ns=dexpi;LowerLimitHeatTracingTemperature",
    description="The temperature that a heat tracing system must ensure for the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1979",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Temperature")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1980", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.OrificePlateType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1978"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=dexpi;i=1983",
    browseName="ns=dexpi;InsulationThickness",
    description="The insulation thickness of the PipeFitting.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=1984",
                browseName="ns=dexpi;EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText("Length")),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=1985", browseName="ns=dexpi;EURange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(dexpi_objtypes.OrificePlateType, ns0.reftypes.HasComponent, o6.ns["ns=dexpi;i=1983"])
dEXPISupplementaryData = dexpi_objtypes.DEXPISupplementaryDataType(
    nodeId="ns=dexpi;i=2122",
    browseName="ns=dexpi;DEXPISupplementaryData",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=2123", browseName="ns=dexpi;DEXPISpecificationVersion", dataType=o6.String, value="1.2", accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=2124", browseName="ns=dexpi;ProteusSchemaVersion", dataType=o6.String, value="4.0.1", accessLevel=3, userAccessLevel=1)
        ),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashDEXPISlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=dexpi;i=5001",
    browseName="ns=dexpi;http://opcfoundation.org/UA/DEXPI/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-09-10T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DEXPI/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=6005", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=dexpi;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=dexpi;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, dexpi_reftypes, dexpi_datypes, dexpi_objtypes
