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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=dexpi;i=1000", browseName="SiphonClassification")
class SiphonClassification(ns0.datatypes.Enumeration):
    NO_SIPHON = o6.enumfield(0, name="NoSiphon")
    SIPHON = o6.enumfield(1, name="Siphon")


@o6.enumtype(nodeId="ns=dexpi;i=1002", browseName="PipingNetworkSegmentFlowClassification")
class PipingNetworkSegmentFlowClassification(ns0.datatypes.Enumeration):
    DUAL_FLOW_PIPING_NETWORK_SEGMENT = o6.enumfield(0, name="DualFlowPipingNetworkSegment")
    SINGLE_FLOW_PIPING_NETWORK_SEGMENT = o6.enumfield(1, name="SingleFlowPipingNetworkSegment")


@o6.enumtype(nodeId="ns=dexpi;i=1004", browseName="GuaranteedSupplyFunctionClassification")
class GuaranteedSupplyFunctionClassification(ns0.datatypes.Enumeration):
    GUARANTEED_SUPPLY_FUNCTION = o6.enumfield(0, name="GuaranteedSupplyFunction")
    NON_GUARANTEED_SUPPLY_FUNCTION = o6.enumfield(1, name="NonGuaranteedSupplyFunction")


@o6.enumtype(nodeId="ns=dexpi;i=1006", browseName="FireResistantArtefactClassification")
class FireResistantArtefactClassification(ns0.datatypes.Enumeration):
    FIRE_RESISTANT_ARTEFACT = o6.enumfield(0, name="FireResistantArtefact")
    NON_FIRE_RESISTANT_ARTEFACT = o6.enumfield(1, name="NonFireResistantArtefact")


@o6.enumtype(nodeId="ns=dexpi;i=1008", browseName="OnHoldClassification")
class OnHoldClassification(ns0.datatypes.Enumeration):
    NOT_ON_HOLD = o6.enumfield(0, name="NotOnHold")
    ON_HOLD = o6.enumfield(1, name="OnHold")


@o6.enumtype(nodeId="ns=dexpi;i=1010", browseName="QualityRelevanceClassification")
class QualityRelevanceClassification(ns0.datatypes.Enumeration):
    NON_QUALITY_RELEVANT_FUNCTION = o6.enumfield(0, name="NonQualityRelevantFunction")
    QUALITY_RELEVANT_FUNCTION = o6.enumfield(1, name="QualityRelevantFunction")


@o6.enumtype(nodeId="ns=dexpi;i=1012", browseName="ConfidentialityClassification")
class ConfidentialityClassification(ns0.datatypes.Enumeration):
    CONFIDENTIAL_INFORMATION = o6.enumfield(0, name="ConfidentialInformation")
    NON_CONFIDENTIAL_INFORMATION = o6.enumfield(1, name="NonConfidentialInformation")


@o6.enumtype(nodeId="ns=dexpi;i=1014", browseName="ExplosionProofArtefactClassification")
class ExplosionProofArtefactClassification(ns0.datatypes.Enumeration):
    EXPLOSION_PROOF_ARTEFACT = o6.enumfield(0, name="ExplosionProofArtefact")
    NON_EXPLOSION_PROOF_ARTEFACT = o6.enumfield(1, name="NonExplosionProofArtefact")


@o6.enumtype(nodeId="ns=dexpi;i=1016", browseName="PipingClassBreakClassification")
class PipingClassBreakClassification(ns0.datatypes.Enumeration):
    NO_PIPING_CLASS_BREAK = o6.enumfield(0, name="NoPipingClassBreak")
    PIPING_CLASS_BREAK = o6.enumfield(1, name="PipingClassBreak")


@o6.enumtype(nodeId="ns=dexpi;i=1018", browseName="NominalPressureStandardClassification")
class NominalPressureStandardClassification(ns0.datatypes.Enumeration):
    CLASS10000_PSI_ARTEFACT = o6.enumfield(0, name="Class10000PsiArtefact")
    CLASS1000_KPA_ARTEFACT = o6.enumfield(1, name="Class1000KpaArtefact")
    CLASS125_LBS_ARTEFACT = o6.enumfield(2, name="Class125LbsArtefact")
    CLASS15000_PSI_ARTEFACT = o6.enumfield(3, name="Class15000PsiArtefact")
    CLASS1500_LBS_ARTEFACT = o6.enumfield(4, name="Class1500LbsArtefact")
    CLASS150_LBS_ARTEFACT = o6.enumfield(5, name="Class150LbsArtefact")
    CLASS16_BAR_ARTEFACT = o6.enumfield(6, name="Class16BarArtefact")
    CLASS20000_PSI_ARTEFACT = o6.enumfield(7, name="Class20000PsiArtefact")
    CLASS2000_PSI_ARTEFACT = o6.enumfield(8, name="Class2000PsiArtefact")
    CLASS2500_LBS_ARTEFACT = o6.enumfield(9, name="Class2500LbsArtefact")
    CLASS250_PSI_ARTEFACT = o6.enumfield(10, name="Class250PsiArtefact")
    CLASS3000_PSI_ARTEFACT = o6.enumfield(11, name="Class3000PsiArtefact")
    CLASS300_LBS_ARTEFACT = o6.enumfield(12, name="Class300LbsArtefact")
    CLASS300_PSI_ARTEFACT = o6.enumfield(13, name="Class300PsiArtefact")
    CLASS315_BAR_ARTEFACT = o6.enumfield(14, name="Class315BarArtefact")
    CLASS345_BAR_ARTEFACT = o6.enumfield(15, name="Class345BarArtefact")
    CLASS350_BAR_ARTEFACT = o6.enumfield(16, name="Class350BarArtefact")
    CLASS4000_PSI_ARTEFACT = o6.enumfield(17, name="Class4000PsiArtefact")
    CLASS400_LBS_ARTEFACT = o6.enumfield(18, name="Class400LbsArtefact")
    CLASS4500_LBS_ARTEFACT = o6.enumfield(19, name="Class4500LbsArtefact")
    CLASS4500_PSI_ARTEFACT = o6.enumfield(20, name="Class4500PsiArtefact")
    CLASS5000_PSI_ARTEFACT = o6.enumfield(21, name="Class5000PsiArtefact")
    CLASS50_BAR_ARTEFACT = o6.enumfield(22, name="Class50BarArtefact")
    CLASS517_BAR_ARTEFACT = o6.enumfield(23, name="Class517BarArtefact")
    CLASS6000_PSI_ARTEFACT = o6.enumfield(24, name="Class6000PsiArtefact")
    CLASS600_LBS_ARTEFACT = o6.enumfield(25, name="Class600LbsArtefact")
    CLASS690_BAR_ARTEFACT = o6.enumfield(26, name="Class690BarArtefact")
    CLASS800_LBS_ARTEFACT = o6.enumfield(27, name="Class800LbsArtefact")
    CLASS800_PSI_ARTEFACT = o6.enumfield(28, name="Class800PsiArtefact")
    CLASS850_KPA_ARTEFACT = o6.enumfield(29, name="Class850KpaArtefact")
    CLASS9000_LBS_ARTEFACT = o6.enumfield(30, name="Class9000LbsArtefact")
    CLASS900_LBS_ARTEFACT = o6.enumfield(31, name="Class900LbsArtefact")
    EN1333_PN100_ARTEFACT = o6.enumfield(32, name="En1333Pn100Artefact")
    EN1333_PN10_ARTEFACT = o6.enumfield(33, name="En1333Pn10Artefact")
    EN1333_PN160_ARTEFACT = o6.enumfield(34, name="En1333Pn160Artefact")
    EN1333_PN16_ARTEFACT = o6.enumfield(35, name="En1333Pn16Artefact")
    EN1333_PN2_5_ARTEFACT = o6.enumfield(36, name="En1333Pn2,5Artefact")
    EN1333_PN250_ARTEFACT = o6.enumfield(37, name="En1333Pn250Artefact")
    EN1333_PN25_ARTEFACT = o6.enumfield(38, name="En1333Pn25Artefact")
    EN1333_PN320_ARTEFACT = o6.enumfield(39, name="En1333Pn320Artefact")
    EN1333_PN400_ARTEFACT = o6.enumfield(40, name="En1333Pn400Artefact")
    EN1333_PN40_ARTEFACT = o6.enumfield(41, name="En1333Pn40Artefact")
    EN1333_PN63_ARTEFACT = o6.enumfield(42, name="En1333Pn63Artefact")
    EN1333_PN6_ARTEFACT = o6.enumfield(43, name="En1333Pn6Artefact")


@o6.enumtype(nodeId="ns=dexpi;i=1020", browseName="GmpRelevanceClassification")
class GmpRelevanceClassification(ns0.datatypes.Enumeration):
    GMP_RELEVANT_FUNCTION = o6.enumfield(0, name="GmpRelevantFunction")
    NON_GMP_RELEVANT_FUNCTION = o6.enumfield(1, name="NonGmpRelevantFunction")


@o6.enumtype(nodeId="ns=dexpi;i=1022", browseName="NumberOfPortsClassification")
class NumberOfPortsClassification(ns0.datatypes.Enumeration):
    FOUR_PORT_VALVE = o6.enumfield(0, name="FourPortValve")
    THREE_PORT_VALVE = o6.enumfield(1, name="ThreePortValve")
    TWO_PORT_VALVE = o6.enumfield(2, name="TwoPortValve")


@o6.enumtype(nodeId="ns=dexpi;i=1024", browseName="DetonationProofArtefactClassification")
class DetonationProofArtefactClassification(ns0.datatypes.Enumeration):
    DETONATION_PROOF_ARTEFACT = o6.enumfield(0, name="DetonationProofArtefact")
    NON_DETONATION_PROOF_ARTEFACT = o6.enumfield(1, name="NonDetonationProofArtefact")


@o6.enumtype(nodeId="ns=dexpi;i=1026", browseName="CompositionBreakClassification")
class CompositionBreakClassification(ns0.datatypes.Enumeration):
    COMPOSITION_BREAK = o6.enumfield(0, name="CompositionBreak")
    NO_COMPOSITION_BREAK = o6.enumfield(1, name="NoCompositionBreak")


@o6.enumtype(nodeId="ns=dexpi;i=1028", browseName="NodeFlowClassification")
class NodeFlowClassification(ns0.datatypes.Enumeration):
    MAIN_FLOW_IN_NODE = o6.enumfield(0, name="MainFlowInNode")
    MAIN_FLOW_OUT_NODE = o6.enumfield(1, name="MainFlowOutNode")


@o6.enumtype(nodeId="ns=dexpi;i=1030", browseName="InsulationBreakClassification")
class InsulationBreakClassification(ns0.datatypes.Enumeration):
    INSULATION_BREAK = o6.enumfield(0, name="InsulationBreak")
    NO_INSULATION_BREAK = o6.enumfield(1, name="NoInsulationBreak")


@o6.enumtype(nodeId="ns=dexpi;i=1032", browseName="NominalDiameterStandardClassification")
class NominalDiameterStandardClassification(ns0.datatypes.Enumeration):
    DIN2448_OBJECT_DN100 = o6.enumfield(0, name="Din2448ObjectDn100")
    DIN2448_OBJECT_DN125 = o6.enumfield(1, name="Din2448ObjectDn125")
    DIN2448_OBJECT_DN15 = o6.enumfield(2, name="Din2448ObjectDn15")
    DIN2448_OBJECT_DN150 = o6.enumfield(3, name="Din2448ObjectDn150")
    DIN2448_OBJECT_DN20 = o6.enumfield(4, name="Din2448ObjectDn20")
    DIN2448_OBJECT_DN200 = o6.enumfield(5, name="Din2448ObjectDn200")
    DIN2448_OBJECT_DN25 = o6.enumfield(6, name="Din2448ObjectDn25")
    DIN2448_OBJECT_DN32 = o6.enumfield(7, name="Din2448ObjectDn32")
    DIN2448_OBJECT_DN40 = o6.enumfield(8, name="Din2448ObjectDn40")
    DIN2448_OBJECT_DN50 = o6.enumfield(9, name="Din2448ObjectDn50")
    DIN2448_OBJECT_DN65 = o6.enumfield(10, name="Din2448ObjectDn65")
    DIN2448_OBJECT_DN80 = o6.enumfield(11, name="Din2448ObjectDn80")
    ISO6708_OBJECT_DN100 = o6.enumfield(12, name="Iso6708ObjectDn100")
    ISO6708_OBJECT_DN1000 = o6.enumfield(13, name="Iso6708ObjectDn1000")
    ISO6708_OBJECT_DN1200 = o6.enumfield(14, name="Iso6708ObjectDn1200")
    ISO6708_OBJECT_DN125 = o6.enumfield(15, name="Iso6708ObjectDn125")
    ISO6708_OBJECT_DN1400 = o6.enumfield(16, name="Iso6708ObjectDn1400")
    ISO6708_OBJECT_DN15 = o6.enumfield(17, name="Iso6708ObjectDn15")
    ISO6708_OBJECT_DN150 = o6.enumfield(18, name="Iso6708ObjectDn150")
    ISO6708_OBJECT_DN1600 = o6.enumfield(19, name="Iso6708ObjectDn1600")
    ISO6708_OBJECT_DN20 = o6.enumfield(20, name="Iso6708ObjectDn20")
    ISO6708_OBJECT_DN200 = o6.enumfield(21, name="Iso6708ObjectDn200")
    ISO6708_OBJECT_DN25 = o6.enumfield(22, name="Iso6708ObjectDn25")
    ISO6708_OBJECT_DN250 = o6.enumfield(23, name="Iso6708ObjectDn250")
    ISO6708_OBJECT_DN300 = o6.enumfield(24, name="Iso6708ObjectDn300")
    ISO6708_OBJECT_DN32 = o6.enumfield(25, name="Iso6708ObjectDn32")
    ISO6708_OBJECT_DN350 = o6.enumfield(26, name="Iso6708ObjectDn350")
    ISO6708_OBJECT_DN40 = o6.enumfield(27, name="Iso6708ObjectDn40")
    ISO6708_OBJECT_DN400 = o6.enumfield(28, name="Iso6708ObjectDn400")
    ISO6708_OBJECT_DN450 = o6.enumfield(29, name="Iso6708ObjectDn450")
    ISO6708_OBJECT_DN50 = o6.enumfield(30, name="Iso6708ObjectDn50")
    ISO6708_OBJECT_DN500 = o6.enumfield(31, name="Iso6708ObjectDn500")
    ISO6708_OBJECT_DN600 = o6.enumfield(32, name="Iso6708ObjectDn600")
    ISO6708_OBJECT_DN65 = o6.enumfield(33, name="Iso6708ObjectDn65")
    ISO6708_OBJECT_DN700 = o6.enumfield(34, name="Iso6708ObjectDn700")
    ISO6708_OBJECT_DN80 = o6.enumfield(35, name="Iso6708ObjectDn80")
    ISO6708_OBJECT_DN800 = o6.enumfield(36, name="Iso6708ObjectDn800")
    ISO6708_OBJECT_DN900 = o6.enumfield(37, name="Iso6708ObjectDn900")
    NPS1_2_ARTEFACT = o6.enumfield(38, name="Nps1/2Artefact")
    NPS1_4_ARTEFACT = o6.enumfield(39, name="Nps1/4Artefact")
    NPS10_ARTEFACT = o6.enumfield(40, name="Nps10Artefact")
    NPS12_ARTEFACT = o6.enumfield(41, name="Nps12Artefact")
    NPS14_ARTEFACT = o6.enumfield(42, name="Nps14Artefact")
    NPS16_ARTEFACT = o6.enumfield(43, name="Nps16Artefact")
    NPS18_ARTEFACT = o6.enumfield(44, name="Nps18Artefact")
    NPS1_ARTEFACT = o6.enumfield(45, name="Nps1Artefact")
    NPS1_1_2_ARTEFACT = o6.enumfield(46, name="Nps1_1/2Artefact")
    NPS1_1_4_ARTEFACT = o6.enumfield(47, name="Nps1_1/4Artefact")
    NPS20_ARTEFACT = o6.enumfield(48, name="Nps20Artefact")
    NPS24_ARTEFACT = o6.enumfield(49, name="Nps24Artefact")
    NPS2_ARTEFACT = o6.enumfield(50, name="Nps2Artefact")
    NPS2_1_2_ARTEFACT = o6.enumfield(51, name="Nps2_1/2Artefact")
    NPS3_4_ARTEFACT = o6.enumfield(52, name="Nps3/4Artefact")
    NPS30_ARTEFACT = o6.enumfield(53, name="Nps30Artefact")
    NPS36_ARTEFACT = o6.enumfield(54, name="Nps36Artefact")
    NPS3_ARTEFACT = o6.enumfield(55, name="Nps3Artefact")
    NPS3_1_2_ARTEFACT = o6.enumfield(56, name="Nps3_1/2Artefact")
    NPS42_ARTEFACT = o6.enumfield(57, name="Nps42Artefact")
    NPS48_ARTEFACT = o6.enumfield(58, name="Nps48Artefact")
    NPS4_ARTEFACT = o6.enumfield(59, name="Nps4Artefact")
    NPS54_ARTEFACT = o6.enumfield(60, name="Nps54Artefact")
    NPS5_ARTEFACT = o6.enumfield(61, name="Nps5Artefact")
    NPS60_ARTEFACT = o6.enumfield(62, name="Nps60Artefact")
    NPS6_ARTEFACT = o6.enumfield(63, name="Nps6Artefact")
    NPS8_ARTEFACT = o6.enumfield(64, name="Nps8Artefact")


@o6.enumtype(nodeId="ns=dexpi;i=1034", browseName="PipingNetworkSegmentSlopeClassification")
class PipingNetworkSegmentSlopeClassification(ns0.datatypes.Enumeration):
    SLOPED_PIPING_NETWORK_SEGMENT = o6.enumfield(0, name="SlopedPipingNetworkSegment")
    UNSLOPED_PIPING_NETWORK_SEGMENT = o6.enumfield(1, name="UnslopedPipingNetworkSegment")


@o6.enumtype(nodeId="ns=dexpi;i=1036", browseName="PipingClassArtefactClassification")
class PipingClassArtefactClassification(ns0.datatypes.Enumeration):
    NON_PIPING_CLASS_ARTEFACT = o6.enumfield(0, name="NonPipingClassArtefact")
    PIPING_CLASS_ARTEFACT = o6.enumfield(1, name="PipingClassArtefact")


@o6.enumtype(nodeId="ns=dexpi;i=1038", browseName="HeatTracingTypeClassification")
class HeatTracingTypeClassification(ns0.datatypes.Enumeration):
    ELECTRICAL_HEAT_TRACING_SYSTEM = o6.enumfield(0, name="ElectricalHeatTracingSystem")
    HEAT_TRACING_SYSTEM = o6.enumfield(1, name="HeatTracingSystem")
    NO_HEAT_TRACING_SYSTEM = o6.enumfield(2, name="NoHeatTracingSystem")
    STEAM_HEAT_TRACING_SYSTEM = o6.enumfield(3, name="SteamHeatTracingSystem")
    TUBULAR_HEAT_TRACING_SYSTEM = o6.enumfield(4, name="TubularHeatTracingSystem")


@o6.enumtype(nodeId="ns=dexpi;i=1040", browseName="SignalConveyingTypeClassification")
class SignalConveyingTypeClassification(ns0.datatypes.Enumeration):
    CAPILLARY_SIGNAL_CONVEYING = o6.enumfield(0, name="CapillarySignalConveying")
    CONDUCTED_RADIATION_SIGNAL_CONVEYING = o6.enumfield(1, name="ConductedRadiationSignalConveying")
    ELECTRICAL_SIGNAL_CONVEYING = o6.enumfield(2, name="ElectricalSignalConveying")
    HYDRAULIC_SIGNAL_CONVEYING = o6.enumfield(3, name="HydraulicSignalConveying")
    PNEUMATIC_SIGNAL_CONVEYING = o6.enumfield(4, name="PneumaticSignalConveying")


@o6.enumtype(nodeId="ns=dexpi;i=1042", browseName="PrimarySecondaryPipingNetworkSegmentClassification")
class PrimarySecondaryPipingNetworkSegmentClassification(ns0.datatypes.Enumeration):
    PRIMARY_PIPING_NETWORK_SEGMENT = o6.enumfield(0, name="PrimaryPipingNetworkSegment")
    SECONDARY_PIPING_NETWORK_SEGMENT = o6.enumfield(1, name="SecondaryPipingNetworkSegment")


@o6.enumtype(nodeId="ns=dexpi;i=1044", browseName="ChamberFunctionClassification")
class ChamberFunctionClassification(ns0.datatypes.Enumeration):
    COOLING = o6.enumfield(0, name="Cooling")
    HEATING = o6.enumfield(1, name="Heating")
    PROCESSING = o6.enumfield(2, name="Processing")
    TEMPERING = o6.enumfield(3, name="Tempering")


@o6.enumtype(nodeId="ns=dexpi;i=1046", browseName="OperationClassification")
class OperationClassification(ns0.datatypes.Enumeration):
    CONTINUOUS_OPERATION = o6.enumfield(0, name="ContinuousOperation")
    INTERMITTENT_OPERATION = o6.enumfield(1, name="IntermittentOperation")


@o6.enumtype(nodeId="ns=dexpi;i=1048", browseName="NominalDiameterBreakClassification")
class NominalDiameterBreakClassification(ns0.datatypes.Enumeration):
    NO_NOMINAL_DIAMETER_BREAK = o6.enumfield(0, name="NoNominalDiameterBreak")
    NOMINAL_DIAMETER_BREAK = o6.enumfield(1, name="NominalDiameterBreak")


@o6.enumtype(nodeId="ns=dexpi;i=1050", browseName="FailActionClassification")
class FailActionClassification(ns0.datatypes.Enumeration):
    FAIL_CLOSE = o6.enumfield(0, name="FailClose")
    FAIL_OPEN = o6.enumfield(1, name="FailOpen")
    FAIL_RETAIN_POSITION = o6.enumfield(2, name="FailRetainPosition")


@o6.enumtype(nodeId="ns=dexpi;i=1052", browseName="JacketedPipeClassification")
class JacketedPipeClassification(ns0.datatypes.Enumeration):
    JACKETED_PIPE = o6.enumfield(0, name="JacketedPipe")
    UNJACKETED_PIPE = o6.enumfield(1, name="UnjacketedPipe")


@o6.enumtype(nodeId="ns=dexpi;i=1054", browseName="LocationClassification")
class LocationClassification(ns0.datatypes.Enumeration):
    CENTRAL_LOCATION = o6.enumfield(0, name="CentralLocation")
    CONTROL_PANEL = o6.enumfield(1, name="ControlPanel")
    FIELD = o6.enumfield(2, name="Field")


@o6.enumtype(nodeId="ns=dexpi;i=1056", browseName="PortStatusClassification")
class PortStatusClassification(ns0.datatypes.Enumeration):
    STATUS_HIGH_HIGH_HIGH_PORT = o6.enumfield(0, name="StatusHighHighHighPort")
    STATUS_HIGH_HIGH_PORT = o6.enumfield(1, name="StatusHighHighPort")
    STATUS_HIGH_PORT = o6.enumfield(2, name="StatusHighPort")
    STATUS_LOW_LOW_LOW_PORT = o6.enumfield(3, name="StatusLowLowLowPort")
    STATUS_LOW_LOW_PORT = o6.enumfield(4, name="StatusLowLowPort")
    STATUS_LOW_PORT = o6.enumfield(5, name="StatusLowPort")


del Any, TYPE_CHECKING, uuid, o6, ns0, dexpi_reftypes
