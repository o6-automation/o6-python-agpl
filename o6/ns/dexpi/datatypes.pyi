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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class SiphonClassification(enum.IntFlag):
    NO_SIPHON = 0
    SIPHON = 1

class PipingNetworkSegmentFlowClassification(enum.IntFlag):
    DUAL_FLOW_PIPING_NETWORK_SEGMENT = 0
    SINGLE_FLOW_PIPING_NETWORK_SEGMENT = 1

class GuaranteedSupplyFunctionClassification(enum.IntFlag):
    GUARANTEED_SUPPLY_FUNCTION = 0
    NON_GUARANTEED_SUPPLY_FUNCTION = 1

class FireResistantArtefactClassification(enum.IntFlag):
    FIRE_RESISTANT_ARTEFACT = 0
    NON_FIRE_RESISTANT_ARTEFACT = 1

class OnHoldClassification(enum.IntFlag):
    NOT_ON_HOLD = 0
    ON_HOLD = 1

class QualityRelevanceClassification(enum.IntFlag):
    NON_QUALITY_RELEVANT_FUNCTION = 0
    QUALITY_RELEVANT_FUNCTION = 1

class ConfidentialityClassification(enum.IntFlag):
    CONFIDENTIAL_INFORMATION = 0
    NON_CONFIDENTIAL_INFORMATION = 1

class ExplosionProofArtefactClassification(enum.IntFlag):
    EXPLOSION_PROOF_ARTEFACT = 0
    NON_EXPLOSION_PROOF_ARTEFACT = 1

class PipingClassBreakClassification(enum.IntFlag):
    NO_PIPING_CLASS_BREAK = 0
    PIPING_CLASS_BREAK = 1

class NominalPressureStandardClassification(enum.IntFlag):
    CLASS10000_PSI_ARTEFACT = 0
    CLASS1000_KPA_ARTEFACT = 1
    CLASS125_LBS_ARTEFACT = 2
    CLASS15000_PSI_ARTEFACT = 3
    CLASS1500_LBS_ARTEFACT = 4
    CLASS150_LBS_ARTEFACT = 5
    CLASS16_BAR_ARTEFACT = 6
    CLASS20000_PSI_ARTEFACT = 7
    CLASS2000_PSI_ARTEFACT = 8
    CLASS2500_LBS_ARTEFACT = 9
    CLASS250_PSI_ARTEFACT = 10
    CLASS3000_PSI_ARTEFACT = 11
    CLASS300_LBS_ARTEFACT = 12
    CLASS300_PSI_ARTEFACT = 13
    CLASS315_BAR_ARTEFACT = 14
    CLASS345_BAR_ARTEFACT = 15
    CLASS350_BAR_ARTEFACT = 16
    CLASS4000_PSI_ARTEFACT = 17
    CLASS400_LBS_ARTEFACT = 18
    CLASS4500_LBS_ARTEFACT = 19
    CLASS4500_PSI_ARTEFACT = 20
    CLASS5000_PSI_ARTEFACT = 21
    CLASS50_BAR_ARTEFACT = 22
    CLASS517_BAR_ARTEFACT = 23
    CLASS6000_PSI_ARTEFACT = 24
    CLASS600_LBS_ARTEFACT = 25
    CLASS690_BAR_ARTEFACT = 26
    CLASS800_LBS_ARTEFACT = 27
    CLASS800_PSI_ARTEFACT = 28
    CLASS850_KPA_ARTEFACT = 29
    CLASS9000_LBS_ARTEFACT = 30
    CLASS900_LBS_ARTEFACT = 31
    EN1333_PN100_ARTEFACT = 32
    EN1333_PN10_ARTEFACT = 33
    EN1333_PN160_ARTEFACT = 34
    EN1333_PN16_ARTEFACT = 35
    EN1333_PN2_5_ARTEFACT = 36
    EN1333_PN250_ARTEFACT = 37
    EN1333_PN25_ARTEFACT = 38
    EN1333_PN320_ARTEFACT = 39
    EN1333_PN400_ARTEFACT = 40
    EN1333_PN40_ARTEFACT = 41
    EN1333_PN63_ARTEFACT = 42
    EN1333_PN6_ARTEFACT = 43

class GmpRelevanceClassification(enum.IntFlag):
    GMP_RELEVANT_FUNCTION = 0
    NON_GMP_RELEVANT_FUNCTION = 1

class NumberOfPortsClassification(enum.IntFlag):
    FOUR_PORT_VALVE = 0
    THREE_PORT_VALVE = 1
    TWO_PORT_VALVE = 2

class DetonationProofArtefactClassification(enum.IntFlag):
    DETONATION_PROOF_ARTEFACT = 0
    NON_DETONATION_PROOF_ARTEFACT = 1

class CompositionBreakClassification(enum.IntFlag):
    COMPOSITION_BREAK = 0
    NO_COMPOSITION_BREAK = 1

class NodeFlowClassification(enum.IntFlag):
    MAIN_FLOW_IN_NODE = 0
    MAIN_FLOW_OUT_NODE = 1

class InsulationBreakClassification(enum.IntFlag):
    INSULATION_BREAK = 0
    NO_INSULATION_BREAK = 1

class NominalDiameterStandardClassification(enum.IntFlag):
    DIN2448_OBJECT_DN100 = 0
    DIN2448_OBJECT_DN125 = 1
    DIN2448_OBJECT_DN15 = 2
    DIN2448_OBJECT_DN150 = 3
    DIN2448_OBJECT_DN20 = 4
    DIN2448_OBJECT_DN200 = 5
    DIN2448_OBJECT_DN25 = 6
    DIN2448_OBJECT_DN32 = 7
    DIN2448_OBJECT_DN40 = 8
    DIN2448_OBJECT_DN50 = 9
    DIN2448_OBJECT_DN65 = 10
    DIN2448_OBJECT_DN80 = 11
    ISO6708_OBJECT_DN100 = 12
    ISO6708_OBJECT_DN1000 = 13
    ISO6708_OBJECT_DN1200 = 14
    ISO6708_OBJECT_DN125 = 15
    ISO6708_OBJECT_DN1400 = 16
    ISO6708_OBJECT_DN15 = 17
    ISO6708_OBJECT_DN150 = 18
    ISO6708_OBJECT_DN1600 = 19
    ISO6708_OBJECT_DN20 = 20
    ISO6708_OBJECT_DN200 = 21
    ISO6708_OBJECT_DN25 = 22
    ISO6708_OBJECT_DN250 = 23
    ISO6708_OBJECT_DN300 = 24
    ISO6708_OBJECT_DN32 = 25
    ISO6708_OBJECT_DN350 = 26
    ISO6708_OBJECT_DN40 = 27
    ISO6708_OBJECT_DN400 = 28
    ISO6708_OBJECT_DN450 = 29
    ISO6708_OBJECT_DN50 = 30
    ISO6708_OBJECT_DN500 = 31
    ISO6708_OBJECT_DN600 = 32
    ISO6708_OBJECT_DN65 = 33
    ISO6708_OBJECT_DN700 = 34
    ISO6708_OBJECT_DN80 = 35
    ISO6708_OBJECT_DN800 = 36
    ISO6708_OBJECT_DN900 = 37
    NPS1_2_ARTEFACT = 38
    NPS1_4_ARTEFACT = 39
    NPS10_ARTEFACT = 40
    NPS12_ARTEFACT = 41
    NPS14_ARTEFACT = 42
    NPS16_ARTEFACT = 43
    NPS18_ARTEFACT = 44
    NPS1_ARTEFACT = 45
    NPS1_1_2_ARTEFACT = 46
    NPS1_1_4_ARTEFACT = 47
    NPS20_ARTEFACT = 48
    NPS24_ARTEFACT = 49
    NPS2_ARTEFACT = 50
    NPS2_1_2_ARTEFACT = 51
    NPS3_4_ARTEFACT = 52
    NPS30_ARTEFACT = 53
    NPS36_ARTEFACT = 54
    NPS3_ARTEFACT = 55
    NPS3_1_2_ARTEFACT = 56
    NPS42_ARTEFACT = 57
    NPS48_ARTEFACT = 58
    NPS4_ARTEFACT = 59
    NPS54_ARTEFACT = 60
    NPS5_ARTEFACT = 61
    NPS60_ARTEFACT = 62
    NPS6_ARTEFACT = 63
    NPS8_ARTEFACT = 64

class PipingNetworkSegmentSlopeClassification(enum.IntFlag):
    SLOPED_PIPING_NETWORK_SEGMENT = 0
    UNSLOPED_PIPING_NETWORK_SEGMENT = 1

class PipingClassArtefactClassification(enum.IntFlag):
    NON_PIPING_CLASS_ARTEFACT = 0
    PIPING_CLASS_ARTEFACT = 1

class HeatTracingTypeClassification(enum.IntFlag):
    ELECTRICAL_HEAT_TRACING_SYSTEM = 0
    HEAT_TRACING_SYSTEM = 1
    NO_HEAT_TRACING_SYSTEM = 2
    STEAM_HEAT_TRACING_SYSTEM = 3
    TUBULAR_HEAT_TRACING_SYSTEM = 4

class SignalConveyingTypeClassification(enum.IntFlag):
    CAPILLARY_SIGNAL_CONVEYING = 0
    CONDUCTED_RADIATION_SIGNAL_CONVEYING = 1
    ELECTRICAL_SIGNAL_CONVEYING = 2
    HYDRAULIC_SIGNAL_CONVEYING = 3
    PNEUMATIC_SIGNAL_CONVEYING = 4

class PrimarySecondaryPipingNetworkSegmentClassification(enum.IntFlag):
    PRIMARY_PIPING_NETWORK_SEGMENT = 0
    SECONDARY_PIPING_NETWORK_SEGMENT = 1

class ChamberFunctionClassification(enum.IntFlag):
    COOLING = 0
    HEATING = 1
    PROCESSING = 2
    TEMPERING = 3

class OperationClassification(enum.IntFlag):
    CONTINUOUS_OPERATION = 0
    INTERMITTENT_OPERATION = 1

class NominalDiameterBreakClassification(enum.IntFlag):
    NO_NOMINAL_DIAMETER_BREAK = 0
    NOMINAL_DIAMETER_BREAK = 1

class FailActionClassification(enum.IntFlag):
    FAIL_CLOSE = 0
    FAIL_OPEN = 1
    FAIL_RETAIN_POSITION = 2

class JacketedPipeClassification(enum.IntFlag):
    JACKETED_PIPE = 0
    UNJACKETED_PIPE = 1

class LocationClassification(enum.IntFlag):
    CENTRAL_LOCATION = 0
    CONTROL_PANEL = 1
    FIELD = 2

class PortStatusClassification(enum.IntFlag):
    STATUS_HIGH_HIGH_HIGH_PORT = 0
    STATUS_HIGH_HIGH_PORT = 1
    STATUS_HIGH_PORT = 2
    STATUS_LOW_LOW_LOW_PORT = 3
    STATUS_LOW_LOW_PORT = 4
    STATUS_LOW_PORT = 5
