# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 8c1479b224f9061d6444d533aeaf15947e3e241a0cd97835191bf807410f53f3
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/DEXPI/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.7"}]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=1;i=1000",
        "SiphonClassification",
        {
            "fields": [
                {"name": "NoSiphon", "value": 0, "display_name": "NoSiphon"},
                {"name": "Siphon", "value": 1, "display_name": "Siphon"},
            ]
        },
    ),
    (
        "ns=1;i=1002",
        "PipingNetworkSegmentFlowClassification",
        {
            "fields": [
                {
                    "name": "DualFlowPipingNetworkSegment",
                    "value": 0,
                    "display_name": "DualFlowPipingNetworkSegment",
                },
                {
                    "name": "SingleFlowPipingNetworkSegment",
                    "value": 1,
                    "display_name": "SingleFlowPipingNetworkSegment",
                },
            ]
        },
    ),
    (
        "ns=1;i=1004",
        "GuaranteedSupplyFunctionClassification",
        {
            "fields": [
                {
                    "name": "GuaranteedSupplyFunction",
                    "value": 0,
                    "display_name": "GuaranteedSupplyFunction",
                },
                {
                    "name": "NonGuaranteedSupplyFunction",
                    "value": 1,
                    "display_name": "NonGuaranteedSupplyFunction",
                },
            ]
        },
    ),
    (
        "ns=1;i=1006",
        "FireResistantArtefactClassification",
        {
            "fields": [
                {
                    "name": "FireResistantArtefact",
                    "value": 0,
                    "display_name": "FireResistantArtefact",
                },
                {
                    "name": "NonFireResistantArtefact",
                    "value": 1,
                    "display_name": "NonFireResistantArtefact",
                },
            ]
        },
    ),
    (
        "ns=1;i=1008",
        "OnHoldClassification",
        {
            "fields": [
                {"name": "NotOnHold", "value": 0, "display_name": "NotOnHold"},
                {"name": "OnHold", "value": 1, "display_name": "OnHold"},
            ]
        },
    ),
    (
        "ns=1;i=1010",
        "QualityRelevanceClassification",
        {
            "fields": [
                {
                    "name": "NonQualityRelevantFunction",
                    "value": 0,
                    "display_name": "NonQualityRelevantFunction",
                },
                {
                    "name": "QualityRelevantFunction",
                    "value": 1,
                    "display_name": "QualityRelevantFunction",
                },
            ]
        },
    ),
    (
        "ns=1;i=1012",
        "ConfidentialityClassification",
        {
            "fields": [
                {
                    "name": "ConfidentialInformation",
                    "value": 0,
                    "display_name": "ConfidentialInformation",
                },
                {
                    "name": "NonConfidentialInformation",
                    "value": 1,
                    "display_name": "NonConfidentialInformation",
                },
            ]
        },
    ),
    (
        "ns=1;i=1014",
        "ExplosionProofArtefactClassification",
        {
            "fields": [
                {
                    "name": "ExplosionProofArtefact",
                    "value": 0,
                    "display_name": "ExplosionProofArtefact",
                },
                {
                    "name": "NonExplosionProofArtefact",
                    "value": 1,
                    "display_name": "NonExplosionProofArtefact",
                },
            ]
        },
    ),
    (
        "ns=1;i=1016",
        "PipingClassBreakClassification",
        {
            "fields": [
                {
                    "name": "NoPipingClassBreak",
                    "value": 0,
                    "display_name": "NoPipingClassBreak",
                },
                {
                    "name": "PipingClassBreak",
                    "value": 1,
                    "display_name": "PipingClassBreak",
                },
            ]
        },
    ),
    (
        "ns=1;i=1018",
        "NominalPressureStandardClassification",
        {
            "fields": [
                {
                    "name": "Class10000PsiArtefact",
                    "value": 0,
                    "display_name": "Class10000PsiArtefact",
                },
                {
                    "name": "Class1000KpaArtefact",
                    "value": 1,
                    "display_name": "Class1000KpaArtefact",
                },
                {
                    "name": "Class125LbsArtefact",
                    "value": 2,
                    "display_name": "Class125LbsArtefact",
                },
                {
                    "name": "Class15000PsiArtefact",
                    "value": 3,
                    "display_name": "Class15000PsiArtefact",
                },
                {
                    "name": "Class1500LbsArtefact",
                    "value": 4,
                    "display_name": "Class1500LbsArtefact",
                },
                {
                    "name": "Class150LbsArtefact",
                    "value": 5,
                    "display_name": "Class150LbsArtefact",
                },
                {
                    "name": "Class16BarArtefact",
                    "value": 6,
                    "display_name": "Class16BarArtefact",
                },
                {
                    "name": "Class20000PsiArtefact",
                    "value": 7,
                    "display_name": "Class20000PsiArtefact",
                },
                {
                    "name": "Class2000PsiArtefact",
                    "value": 8,
                    "display_name": "Class2000PsiArtefact",
                },
                {
                    "name": "Class2500LbsArtefact",
                    "value": 9,
                    "display_name": "Class2500LbsArtefact",
                },
                {
                    "name": "Class250PsiArtefact",
                    "value": 10,
                    "display_name": "Class250PsiArtefact",
                },
                {
                    "name": "Class3000PsiArtefact",
                    "value": 11,
                    "display_name": "Class3000PsiArtefact",
                },
                {
                    "name": "Class300LbsArtefact",
                    "value": 12,
                    "display_name": "Class300LbsArtefact",
                },
                {
                    "name": "Class300PsiArtefact",
                    "value": 13,
                    "display_name": "Class300PsiArtefact",
                },
                {
                    "name": "Class315BarArtefact",
                    "value": 14,
                    "display_name": "Class315BarArtefact",
                },
                {
                    "name": "Class345BarArtefact",
                    "value": 15,
                    "display_name": "Class345BarArtefact",
                },
                {
                    "name": "Class350BarArtefact",
                    "value": 16,
                    "display_name": "Class350BarArtefact",
                },
                {
                    "name": "Class4000PsiArtefact",
                    "value": 17,
                    "display_name": "Class4000PsiArtefact",
                },
                {
                    "name": "Class400LbsArtefact",
                    "value": 18,
                    "display_name": "Class400LbsArtefact",
                },
                {
                    "name": "Class4500LbsArtefact",
                    "value": 19,
                    "display_name": "Class4500LbsArtefact",
                },
                {
                    "name": "Class4500PsiArtefact",
                    "value": 20,
                    "display_name": "Class4500PsiArtefact",
                },
                {
                    "name": "Class5000PsiArtefact",
                    "value": 21,
                    "display_name": "Class5000PsiArtefact",
                },
                {
                    "name": "Class50BarArtefact",
                    "value": 22,
                    "display_name": "Class50BarArtefact",
                },
                {
                    "name": "Class517BarArtefact",
                    "value": 23,
                    "display_name": "Class517BarArtefact",
                },
                {
                    "name": "Class6000PsiArtefact",
                    "value": 24,
                    "display_name": "Class6000PsiArtefact",
                },
                {
                    "name": "Class600LbsArtefact",
                    "value": 25,
                    "display_name": "Class600LbsArtefact",
                },
                {
                    "name": "Class690BarArtefact",
                    "value": 26,
                    "display_name": "Class690BarArtefact",
                },
                {
                    "name": "Class800LbsArtefact",
                    "value": 27,
                    "display_name": "Class800LbsArtefact",
                },
                {
                    "name": "Class800PsiArtefact",
                    "value": 28,
                    "display_name": "Class800PsiArtefact",
                },
                {
                    "name": "Class850KpaArtefact",
                    "value": 29,
                    "display_name": "Class850KpaArtefact",
                },
                {
                    "name": "Class9000LbsArtefact",
                    "value": 30,
                    "display_name": "Class9000LbsArtefact",
                },
                {
                    "name": "Class900LbsArtefact",
                    "value": 31,
                    "display_name": "Class900LbsArtefact",
                },
                {
                    "name": "En1333Pn100Artefact",
                    "value": 32,
                    "display_name": "En1333Pn100Artefact",
                },
                {
                    "name": "En1333Pn10Artefact",
                    "value": 33,
                    "display_name": "En1333Pn10Artefact",
                },
                {
                    "name": "En1333Pn160Artefact",
                    "value": 34,
                    "display_name": "En1333Pn160Artefact",
                },
                {
                    "name": "En1333Pn16Artefact",
                    "value": 35,
                    "display_name": "En1333Pn16Artefact",
                },
                {
                    "name": "En1333Pn2,5Artefact",
                    "value": 36,
                    "display_name": "En1333Pn2,5Artefact",
                },
                {
                    "name": "En1333Pn250Artefact",
                    "value": 37,
                    "display_name": "En1333Pn250Artefact",
                },
                {
                    "name": "En1333Pn25Artefact",
                    "value": 38,
                    "display_name": "En1333Pn25Artefact",
                },
                {
                    "name": "En1333Pn320Artefact",
                    "value": 39,
                    "display_name": "En1333Pn320Artefact",
                },
                {
                    "name": "En1333Pn400Artefact",
                    "value": 40,
                    "display_name": "En1333Pn400Artefact",
                },
                {
                    "name": "En1333Pn40Artefact",
                    "value": 41,
                    "display_name": "En1333Pn40Artefact",
                },
                {
                    "name": "En1333Pn63Artefact",
                    "value": 42,
                    "display_name": "En1333Pn63Artefact",
                },
                {
                    "name": "En1333Pn6Artefact",
                    "value": 43,
                    "display_name": "En1333Pn6Artefact",
                },
            ]
        },
    ),
    (
        "ns=1;i=1020",
        "GmpRelevanceClassification",
        {
            "fields": [
                {
                    "name": "GmpRelevantFunction",
                    "value": 0,
                    "display_name": "GmpRelevantFunction",
                },
                {
                    "name": "NonGmpRelevantFunction",
                    "value": 1,
                    "display_name": "NonGmpRelevantFunction",
                },
            ]
        },
    ),
    (
        "ns=1;i=1022",
        "NumberOfPortsClassification",
        {
            "fields": [
                {"name": "FourPortValve", "value": 0, "display_name": "FourPortValve"},
                {
                    "name": "ThreePortValve",
                    "value": 1,
                    "display_name": "ThreePortValve",
                },
                {"name": "TwoPortValve", "value": 2, "display_name": "TwoPortValve"},
            ]
        },
    ),
    (
        "ns=1;i=1024",
        "DetonationProofArtefactClassification",
        {
            "fields": [
                {
                    "name": "DetonationProofArtefact",
                    "value": 0,
                    "display_name": "DetonationProofArtefact",
                },
                {
                    "name": "NonDetonationProofArtefact",
                    "value": 1,
                    "display_name": "NonDetonationProofArtefact",
                },
            ]
        },
    ),
    (
        "ns=1;i=1026",
        "CompositionBreakClassification",
        {
            "fields": [
                {
                    "name": "CompositionBreak",
                    "value": 0,
                    "display_name": "CompositionBreak",
                },
                {
                    "name": "NoCompositionBreak",
                    "value": 1,
                    "display_name": "NoCompositionBreak",
                },
            ]
        },
    ),
    (
        "ns=1;i=1028",
        "NodeFlowClassification",
        {
            "fields": [
                {
                    "name": "MainFlowInNode",
                    "value": 0,
                    "display_name": "MainFlowInNode",
                },
                {
                    "name": "MainFlowOutNode",
                    "value": 1,
                    "display_name": "MainFlowOutNode",
                },
            ]
        },
    ),
    (
        "ns=1;i=1030",
        "InsulationBreakClassification",
        {
            "fields": [
                {
                    "name": "InsulationBreak",
                    "value": 0,
                    "display_name": "InsulationBreak",
                },
                {
                    "name": "NoInsulationBreak",
                    "value": 1,
                    "display_name": "NoInsulationBreak",
                },
            ]
        },
    ),
    (
        "ns=1;i=1032",
        "NominalDiameterStandardClassification",
        {
            "fields": [
                {
                    "name": "Din2448ObjectDn100",
                    "value": 0,
                    "display_name": "Din2448ObjectDn100",
                },
                {
                    "name": "Din2448ObjectDn125",
                    "value": 1,
                    "display_name": "Din2448ObjectDn125",
                },
                {
                    "name": "Din2448ObjectDn15",
                    "value": 2,
                    "display_name": "Din2448ObjectDn15",
                },
                {
                    "name": "Din2448ObjectDn150",
                    "value": 3,
                    "display_name": "Din2448ObjectDn150",
                },
                {
                    "name": "Din2448ObjectDn20",
                    "value": 4,
                    "display_name": "Din2448ObjectDn20",
                },
                {
                    "name": "Din2448ObjectDn200",
                    "value": 5,
                    "display_name": "Din2448ObjectDn200",
                },
                {
                    "name": "Din2448ObjectDn25",
                    "value": 6,
                    "display_name": "Din2448ObjectDn25",
                },
                {
                    "name": "Din2448ObjectDn32",
                    "value": 7,
                    "display_name": "Din2448ObjectDn32",
                },
                {
                    "name": "Din2448ObjectDn40",
                    "value": 8,
                    "display_name": "Din2448ObjectDn40",
                },
                {
                    "name": "Din2448ObjectDn50",
                    "value": 9,
                    "display_name": "Din2448ObjectDn50",
                },
                {
                    "name": "Din2448ObjectDn65",
                    "value": 10,
                    "display_name": "Din2448ObjectDn65",
                },
                {
                    "name": "Din2448ObjectDn80",
                    "value": 11,
                    "display_name": "Din2448ObjectDn80",
                },
                {
                    "name": "Iso6708ObjectDn100",
                    "value": 12,
                    "display_name": "Iso6708ObjectDn100",
                },
                {
                    "name": "Iso6708ObjectDn1000",
                    "value": 13,
                    "display_name": "Iso6708ObjectDn1000",
                },
                {
                    "name": "Iso6708ObjectDn1200",
                    "value": 14,
                    "display_name": "Iso6708ObjectDn1200",
                },
                {
                    "name": "Iso6708ObjectDn125",
                    "value": 15,
                    "display_name": "Iso6708ObjectDn125",
                },
                {
                    "name": "Iso6708ObjectDn1400",
                    "value": 16,
                    "display_name": "Iso6708ObjectDn1400",
                },
                {
                    "name": "Iso6708ObjectDn15",
                    "value": 17,
                    "display_name": "Iso6708ObjectDn15",
                },
                {
                    "name": "Iso6708ObjectDn150",
                    "value": 18,
                    "display_name": "Iso6708ObjectDn150",
                },
                {
                    "name": "Iso6708ObjectDn1600",
                    "value": 19,
                    "display_name": "Iso6708ObjectDn1600",
                },
                {
                    "name": "Iso6708ObjectDn20",
                    "value": 20,
                    "display_name": "Iso6708ObjectDn20",
                },
                {
                    "name": "Iso6708ObjectDn200",
                    "value": 21,
                    "display_name": "Iso6708ObjectDn200",
                },
                {
                    "name": "Iso6708ObjectDn25",
                    "value": 22,
                    "display_name": "Iso6708ObjectDn25",
                },
                {
                    "name": "Iso6708ObjectDn250",
                    "value": 23,
                    "display_name": "Iso6708ObjectDn250",
                },
                {
                    "name": "Iso6708ObjectDn300",
                    "value": 24,
                    "display_name": "Iso6708ObjectDn300",
                },
                {
                    "name": "Iso6708ObjectDn32",
                    "value": 25,
                    "display_name": "Iso6708ObjectDn32",
                },
                {
                    "name": "Iso6708ObjectDn350",
                    "value": 26,
                    "display_name": "Iso6708ObjectDn350",
                },
                {
                    "name": "Iso6708ObjectDn40",
                    "value": 27,
                    "display_name": "Iso6708ObjectDn40",
                },
                {
                    "name": "Iso6708ObjectDn400",
                    "value": 28,
                    "display_name": "Iso6708ObjectDn400",
                },
                {
                    "name": "Iso6708ObjectDn450",
                    "value": 29,
                    "display_name": "Iso6708ObjectDn450",
                },
                {
                    "name": "Iso6708ObjectDn50",
                    "value": 30,
                    "display_name": "Iso6708ObjectDn50",
                },
                {
                    "name": "Iso6708ObjectDn500",
                    "value": 31,
                    "display_name": "Iso6708ObjectDn500",
                },
                {
                    "name": "Iso6708ObjectDn600",
                    "value": 32,
                    "display_name": "Iso6708ObjectDn600",
                },
                {
                    "name": "Iso6708ObjectDn65",
                    "value": 33,
                    "display_name": "Iso6708ObjectDn65",
                },
                {
                    "name": "Iso6708ObjectDn700",
                    "value": 34,
                    "display_name": "Iso6708ObjectDn700",
                },
                {
                    "name": "Iso6708ObjectDn80",
                    "value": 35,
                    "display_name": "Iso6708ObjectDn80",
                },
                {
                    "name": "Iso6708ObjectDn800",
                    "value": 36,
                    "display_name": "Iso6708ObjectDn800",
                },
                {
                    "name": "Iso6708ObjectDn900",
                    "value": 37,
                    "display_name": "Iso6708ObjectDn900",
                },
                {
                    "name": "Nps1/2Artefact",
                    "value": 38,
                    "display_name": "Nps1/2Artefact",
                },
                {
                    "name": "Nps1/4Artefact",
                    "value": 39,
                    "display_name": "Nps1/4Artefact",
                },
                {"name": "Nps10Artefact", "value": 40, "display_name": "Nps10Artefact"},
                {"name": "Nps12Artefact", "value": 41, "display_name": "Nps12Artefact"},
                {"name": "Nps14Artefact", "value": 42, "display_name": "Nps14Artefact"},
                {"name": "Nps16Artefact", "value": 43, "display_name": "Nps16Artefact"},
                {"name": "Nps18Artefact", "value": 44, "display_name": "Nps18Artefact"},
                {"name": "Nps1Artefact", "value": 45, "display_name": "Nps1Artefact"},
                {
                    "name": "Nps1_1/2Artefact",
                    "value": 46,
                    "display_name": "Nps1_1/2Artefact",
                },
                {
                    "name": "Nps1_1/4Artefact",
                    "value": 47,
                    "display_name": "Nps1_1/4Artefact",
                },
                {"name": "Nps20Artefact", "value": 48, "display_name": "Nps20Artefact"},
                {"name": "Nps24Artefact", "value": 49, "display_name": "Nps24Artefact"},
                {"name": "Nps2Artefact", "value": 50, "display_name": "Nps2Artefact"},
                {
                    "name": "Nps2_1/2Artefact",
                    "value": 51,
                    "display_name": "Nps2_1/2Artefact",
                },
                {
                    "name": "Nps3/4Artefact",
                    "value": 52,
                    "display_name": "Nps3/4Artefact",
                },
                {"name": "Nps30Artefact", "value": 53, "display_name": "Nps30Artefact"},
                {"name": "Nps36Artefact", "value": 54, "display_name": "Nps36Artefact"},
                {"name": "Nps3Artefact", "value": 55, "display_name": "Nps3Artefact"},
                {
                    "name": "Nps3_1/2Artefact",
                    "value": 56,
                    "display_name": "Nps3_1/2Artefact",
                },
                {"name": "Nps42Artefact", "value": 57, "display_name": "Nps42Artefact"},
                {"name": "Nps48Artefact", "value": 58, "display_name": "Nps48Artefact"},
                {"name": "Nps4Artefact", "value": 59, "display_name": "Nps4Artefact"},
                {"name": "Nps54Artefact", "value": 60, "display_name": "Nps54Artefact"},
                {"name": "Nps5Artefact", "value": 61, "display_name": "Nps5Artefact"},
                {"name": "Nps60Artefact", "value": 62, "display_name": "Nps60Artefact"},
                {"name": "Nps6Artefact", "value": 63, "display_name": "Nps6Artefact"},
                {"name": "Nps8Artefact", "value": 64, "display_name": "Nps8Artefact"},
            ]
        },
    ),
    (
        "ns=1;i=1034",
        "PipingNetworkSegmentSlopeClassification",
        {
            "fields": [
                {
                    "name": "SlopedPipingNetworkSegment",
                    "value": 0,
                    "display_name": "SlopedPipingNetworkSegment",
                },
                {
                    "name": "UnslopedPipingNetworkSegment",
                    "value": 1,
                    "display_name": "UnslopedPipingNetworkSegment",
                },
            ]
        },
    ),
    (
        "ns=1;i=1036",
        "PipingClassArtefactClassification",
        {
            "fields": [
                {
                    "name": "NonPipingClassArtefact",
                    "value": 0,
                    "display_name": "NonPipingClassArtefact",
                },
                {
                    "name": "PipingClassArtefact",
                    "value": 1,
                    "display_name": "PipingClassArtefact",
                },
            ]
        },
    ),
    (
        "ns=1;i=1038",
        "HeatTracingTypeClassification",
        {
            "fields": [
                {
                    "name": "ElectricalHeatTracingSystem",
                    "value": 0,
                    "display_name": "ElectricalHeatTracingSystem",
                },
                {
                    "name": "HeatTracingSystem",
                    "value": 1,
                    "display_name": "HeatTracingSystem",
                },
                {
                    "name": "NoHeatTracingSystem",
                    "value": 2,
                    "display_name": "NoHeatTracingSystem",
                },
                {
                    "name": "SteamHeatTracingSystem",
                    "value": 3,
                    "display_name": "SteamHeatTracingSystem",
                },
                {
                    "name": "TubularHeatTracingSystem",
                    "value": 4,
                    "display_name": "TubularHeatTracingSystem",
                },
            ]
        },
    ),
    (
        "ns=1;i=1040",
        "SignalConveyingTypeClassification",
        {
            "fields": [
                {
                    "name": "CapillarySignalConveying",
                    "value": 0,
                    "display_name": "CapillarySignalConveying",
                },
                {
                    "name": "ConductedRadiationSignalConveying",
                    "value": 1,
                    "display_name": "ConductedRadiationSignalConveying",
                },
                {
                    "name": "ElectricalSignalConveying",
                    "value": 2,
                    "display_name": "ElectricalSignalConveying",
                },
                {
                    "name": "HydraulicSignalConveying",
                    "value": 3,
                    "display_name": "HydraulicSignalConveying",
                },
                {
                    "name": "PneumaticSignalConveying",
                    "value": 4,
                    "display_name": "PneumaticSignalConveying",
                },
            ]
        },
    ),
    (
        "ns=1;i=1042",
        "PrimarySecondaryPipingNetworkSegmentClassification",
        {
            "fields": [
                {
                    "name": "PrimaryPipingNetworkSegment",
                    "value": 0,
                    "display_name": "PrimaryPipingNetworkSegment",
                },
                {
                    "name": "SecondaryPipingNetworkSegment",
                    "value": 1,
                    "display_name": "SecondaryPipingNetworkSegment",
                },
            ]
        },
    ),
    (
        "ns=1;i=1044",
        "ChamberFunctionClassification",
        {
            "fields": [
                {"name": "Cooling", "value": 0, "display_name": "Cooling"},
                {"name": "Heating", "value": 1, "display_name": "Heating"},
                {"name": "Processing", "value": 2, "display_name": "Processing"},
                {"name": "Tempering", "value": 3, "display_name": "Tempering"},
            ]
        },
    ),
    (
        "ns=1;i=1046",
        "OperationClassification",
        {
            "fields": [
                {
                    "name": "ContinuousOperation",
                    "value": 0,
                    "display_name": "ContinuousOperation",
                },
                {
                    "name": "IntermittentOperation",
                    "value": 1,
                    "display_name": "IntermittentOperation",
                },
            ]
        },
    ),
    (
        "ns=1;i=1048",
        "NominalDiameterBreakClassification",
        {
            "fields": [
                {
                    "name": "NoNominalDiameterBreak",
                    "value": 0,
                    "display_name": "NoNominalDiameterBreak",
                },
                {
                    "name": "NominalDiameterBreak",
                    "value": 1,
                    "display_name": "NominalDiameterBreak",
                },
            ]
        },
    ),
    (
        "ns=1;i=1050",
        "FailActionClassification",
        {
            "fields": [
                {"name": "FailClose", "value": 0, "display_name": "FailClose"},
                {"name": "FailOpen", "value": 1, "display_name": "FailOpen"},
                {
                    "name": "FailRetainPosition",
                    "value": 2,
                    "display_name": "FailRetainPosition",
                },
            ]
        },
    ),
    (
        "ns=1;i=1052",
        "JacketedPipeClassification",
        {
            "fields": [
                {"name": "JacketedPipe", "value": 0, "display_name": "JacketedPipe"},
                {
                    "name": "UnjacketedPipe",
                    "value": 1,
                    "display_name": "UnjacketedPipe",
                },
            ]
        },
    ),
    (
        "ns=1;i=1054",
        "LocationClassification",
        {
            "fields": [
                {
                    "name": "CentralLocation",
                    "value": 0,
                    "display_name": "CentralLocation",
                },
                {"name": "ControlPanel", "value": 1, "display_name": "ControlPanel"},
                {"name": "Field", "value": 2, "display_name": "Field"},
            ]
        },
    ),
    (
        "ns=1;i=1056",
        "PortStatusClassification",
        {
            "fields": [
                {
                    "name": "StatusHighHighHighPort",
                    "value": 0,
                    "display_name": "StatusHighHighHighPort",
                },
                {
                    "name": "StatusHighHighPort",
                    "value": 1,
                    "display_name": "StatusHighHighPort",
                },
                {
                    "name": "StatusHighPort",
                    "value": 2,
                    "display_name": "StatusHighPort",
                },
                {
                    "name": "StatusLowLowLowPort",
                    "value": 3,
                    "display_name": "StatusLowLowLowPort",
                },
                {
                    "name": "StatusLowLowPort",
                    "value": 4,
                    "display_name": "StatusLowLowPort",
                },
                {"name": "StatusLowPort", "value": 5, "display_name": "StatusLowPort"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [],
    [
        "ns=1;i=1000",
        "ns=1;i=1002",
        "ns=1;i=1004",
        "ns=1;i=1006",
        "ns=1;i=1008",
        "ns=1;i=1010",
        "ns=1;i=1012",
        "ns=1;i=1014",
        "ns=1;i=1016",
        "ns=1;i=1018",
        "ns=1;i=1020",
        "ns=1;i=1022",
        "ns=1;i=1024",
        "ns=1;i=1026",
        "ns=1;i=1028",
        "ns=1;i=1030",
        "ns=1;i=1032",
        "ns=1;i=1034",
        "ns=1;i=1036",
        "ns=1;i=1038",
        "ns=1;i=1040",
        "ns=1;i=1042",
        "ns=1;i=1044",
        "ns=1;i=1046",
        "ns=1;i=1048",
        "ns=1;i=1050",
        "ns=1;i=1052",
        "ns=1;i=1054",
        "ns=1;i=1056",
    ],
)
_NODES: dict = {
    "datatypes": {
        "ChamberFunctionClassification": (
            "D",
            "ns=1;i=1044",
            {"EnumStrings": ("V", "ns=1;i=1045", {})},
        ),
        "CompositionBreakClassification": (
            "D",
            "ns=1;i=1026",
            {"EnumStrings": ("V", "ns=1;i=1027", {})},
        ),
        "ConfidentialityClassification": (
            "D",
            "ns=1;i=1012",
            {"EnumStrings": ("V", "ns=1;i=1013", {})},
        ),
        "DetonationProofArtefactClassification": (
            "D",
            "ns=1;i=1024",
            {"EnumStrings": ("V", "ns=1;i=1025", {})},
        ),
        "ExplosionProofArtefactClassification": (
            "D",
            "ns=1;i=1014",
            {"EnumStrings": ("V", "ns=1;i=1015", {})},
        ),
        "FailActionClassification": (
            "D",
            "ns=1;i=1050",
            {"EnumStrings": ("V", "ns=1;i=1051", {})},
        ),
        "FireResistantArtefactClassification": (
            "D",
            "ns=1;i=1006",
            {"EnumStrings": ("V", "ns=1;i=1007", {})},
        ),
        "GmpRelevanceClassification": (
            "D",
            "ns=1;i=1020",
            {"EnumStrings": ("V", "ns=1;i=1021", {})},
        ),
        "GuaranteedSupplyFunctionClassification": (
            "D",
            "ns=1;i=1004",
            {"EnumStrings": ("V", "ns=1;i=1005", {})},
        ),
        "HeatTracingTypeClassification": (
            "D",
            "ns=1;i=1038",
            {"EnumStrings": ("V", "ns=1;i=1039", {})},
        ),
        "InsulationBreakClassification": (
            "D",
            "ns=1;i=1030",
            {"EnumStrings": ("V", "ns=1;i=1031", {})},
        ),
        "JacketedPipeClassification": (
            "D",
            "ns=1;i=1052",
            {"EnumStrings": ("V", "ns=1;i=1053", {})},
        ),
        "LocationClassification": (
            "D",
            "ns=1;i=1054",
            {"EnumStrings": ("V", "ns=1;i=1055", {})},
        ),
        "NodeFlowClassification": (
            "D",
            "ns=1;i=1028",
            {"EnumStrings": ("V", "ns=1;i=1029", {})},
        ),
        "NominalDiameterBreakClassification": (
            "D",
            "ns=1;i=1048",
            {"EnumStrings": ("V", "ns=1;i=1049", {})},
        ),
        "NominalDiameterStandardClassification": (
            "D",
            "ns=1;i=1032",
            {"EnumStrings": ("V", "ns=1;i=1033", {})},
        ),
        "NominalPressureStandardClassification": (
            "D",
            "ns=1;i=1018",
            {"EnumStrings": ("V", "ns=1;i=1019", {})},
        ),
        "NumberOfPortsClassification": (
            "D",
            "ns=1;i=1022",
            {"EnumStrings": ("V", "ns=1;i=1023", {})},
        ),
        "OnHoldClassification": (
            "D",
            "ns=1;i=1008",
            {"EnumStrings": ("V", "ns=1;i=1009", {})},
        ),
        "OperationClassification": (
            "D",
            "ns=1;i=1046",
            {"EnumStrings": ("V", "ns=1;i=1047", {})},
        ),
        "PipingClassArtefactClassification": (
            "D",
            "ns=1;i=1036",
            {"EnumStrings": ("V", "ns=1;i=1037", {})},
        ),
        "PipingClassBreakClassification": (
            "D",
            "ns=1;i=1016",
            {"EnumStrings": ("V", "ns=1;i=1017", {})},
        ),
        "PipingNetworkSegmentFlowClassification": (
            "D",
            "ns=1;i=1002",
            {"EnumStrings": ("V", "ns=1;i=1003", {})},
        ),
        "PipingNetworkSegmentSlopeClassification": (
            "D",
            "ns=1;i=1034",
            {"EnumStrings": ("V", "ns=1;i=1035", {})},
        ),
        "PortStatusClassification": (
            "D",
            "ns=1;i=1056",
            {"EnumStrings": ("V", "ns=1;i=1057", {})},
        ),
        "PrimarySecondaryPipingNetworkSegmentClassification": (
            "D",
            "ns=1;i=1042",
            {"EnumStrings": ("V", "ns=1;i=1043", {})},
        ),
        "QualityRelevanceClassification": (
            "D",
            "ns=1;i=1010",
            {"EnumStrings": ("V", "ns=1;i=1011", {})},
        ),
        "SignalConveyingTypeClassification": (
            "D",
            "ns=1;i=1040",
            {"EnumStrings": ("V", "ns=1;i=1041", {})},
        ),
        "SiphonClassification": (
            "D",
            "ns=1;i=1000",
            {"EnumStrings": ("V", "ns=1;i=1001", {})},
        ),
    },
    "objects": {
        "DEXPISupplementaryData": (
            "O",
            "ns=1;i=2122",
            {
                "DEXPISpecificationVersion": ("V", "ns=1;i=2123", {}),
                "ProteusSchemaVersion": ("V", "ns=1;i=2124", {}),
            },
        ),
        "http://opcfoundation.org/UA/DEXPI/": (
            "O",
            "ns=1;i=5001",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6001", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6002", {}),
                "NamespaceUri": ("V", "ns=1;i=6003", {}),
                "NamespaceVersion": ("V", "ns=1;i=6004", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6005", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6006", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6007", {}),
            },
        ),
    },
    "objtypes": {
        "BaseDEXPIObjectType": (
            "OT",
            "ns=1;i=1060",
            {
                "ActuatingFunctionType": (
                    "OT",
                    "ns=1;i=1239",
                    {
                        "ActuatingFunctionNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1240",
                            {},
                        )
                    },
                ),
                "ActuatingSystemType": (
                    "OT",
                    "ns=1;i=1200",
                    {
                        "<ControlledActuator>": ("O", "ns=1;i=2082", {}),
                        "<Positioner>": ("O", "ns=1;i=2084", {}),
                        "<ShutOffValveReference>": ("O", "ns=1;i=2083", {}),
                        "ActuatingSystemNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1201",
                            {},
                        ),
                        "TypicalInformationAssignmentClass": ("V", "ns=1;i=1202", {}),
                    },
                ),
                "AgitatorRotorType": (
                    "OT",
                    "ns=1;i=1672",
                    {
                        "Diameter": (
                            "V",
                            "ns=1;i=1673",
                            {
                                "EURange": ("V", "ns=1;i=1675", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1674", {}),
                            },
                        ),
                        "LengthToMountingFlange": (
                            "V",
                            "ns=1;i=1676",
                            {
                                "EURange": ("V", "ns=1;i=1678", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1677", {}),
                            },
                        ),
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1679",
                            {},
                        ),
                        "RotorTypeAssignmentClass": ("V", "ns=1;i=1680", {}),
                    },
                ),
                "AngleType": (
                    "OT",
                    "ns=1;i=2061",
                    {
                        "Unit": ("V", "ns=1;i=2062", {}),
                        "Value": ("V", "ns=1;i=2064", {}),
                    },
                ),
                "AreaIsa95LocatedStructureType": ("OT", "ns=1;i=1270", {}),
                "AreaIsa95Type": (
                    "OT",
                    "ns=1;i=1290",
                    {
                        "AreaIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1291",
                            {},
                        ),
                        "AreaNameAssignmentClass": ("V", "ns=1;i=1292", {}),
                    },
                ),
                "AreaType": (
                    "OT",
                    "ns=1;i=2029",
                    {
                        "Unit": ("V", "ns=1;i=2030", {}),
                        "Value": ("V", "ns=1;i=2032", {}),
                    },
                ),
                "ChamberOwnerType": (
                    "OT",
                    "ns=1;i=1377",
                    {"<Chamber>": ("O", "ns=1;i=2088", {})},
                ),
                "ChamberType": (
                    "OT",
                    "ns=1;i=1523",
                    {
                        "ChamberDescriptionAssignmentClass": ("V", "ns=1;i=1525", {}),
                        "ChamberFunctionAssignmentClass": ("V", "ns=1;i=1526", {}),
                        "ChamberFunctionSpecialization": ("V", "ns=1;i=1527", {}),
                        "Height": (
                            "V",
                            "ns=1;i=1528",
                            {
                                "EURange": ("V", "ns=1;i=1530", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1529", {}),
                            },
                        ),
                        "InsideDiameter": (
                            "V",
                            "ns=1;i=1531",
                            {
                                "EURange": ("V", "ns=1;i=1533", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1532", {}),
                            },
                        ),
                        "Length": (
                            "V",
                            "ns=1;i=1534",
                            {
                                "EURange": ("V", "ns=1;i=1536", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1535", {}),
                            },
                        ),
                        "LowerLimitDesignPressure": (
                            "V",
                            "ns=1;i=1537",
                            {
                                "EURange": ("V", "ns=1;i=1539", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1538", {}),
                            },
                        ),
                        "LowerLimitDesignTemperature": (
                            "V",
                            "ns=1;i=1540",
                            {
                                "EURange": ("V", "ns=1;i=1542", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1541", {}),
                            },
                        ),
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1543",
                            {},
                        ),
                        "NominalDiameter": (
                            "V",
                            "ns=1;i=1544",
                            {
                                "EURange": ("V", "ns=1;i=1546", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1545", {}),
                            },
                        ),
                        "NominalDiameterTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1547",
                            {},
                        ),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1524", {}),
                        "UpperLimitDesignPressure": (
                            "V",
                            "ns=1;i=1548",
                            {
                                "EURange": ("V", "ns=1;i=1550", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1549", {}),
                            },
                        ),
                        "UpperLimitDesignTemperature": (
                            "V",
                            "ns=1;i=1551",
                            {
                                "EURange": ("V", "ns=1;i=1553", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1552", {}),
                            },
                        ),
                        "Width": (
                            "V",
                            "ns=1;i=1554",
                            {
                                "EURange": ("V", "ns=1;i=1556", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1555", {}),
                            },
                        ),
                    },
                ),
                "ColumnInternalsArrangementType": ("OT", "ns=1;i=1489", {}),
                "ColumnPackingsArrangementType": (
                    "OT",
                    "ns=1;i=1370",
                    {
                        "Height": (
                            "V",
                            "ns=1;i=1371",
                            {
                                "EURange": ("V", "ns=1;i=1373", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1372", {}),
                            },
                        ),
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1374",
                            {},
                        ),
                        "NumberOfPackings": ("V", "ns=1;i=1375", {}),
                        "PackingTypeAssignmentClass": ("V", "ns=1;i=1376", {}),
                    },
                ),
                "ColumnSectionType": (
                    "OT",
                    "ns=1;i=1494",
                    {
                        "<Internal>": ("O", "ns=1;i=2095", {}),
                        "Height": (
                            "V",
                            "ns=1;i=1495",
                            {
                                "EURange": ("V", "ns=1;i=1497", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1496", {}),
                            },
                        ),
                        "InsideDiameter": (
                            "V",
                            "ns=1;i=1498",
                            {
                                "EURange": ("V", "ns=1;i=1500", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1499", {}),
                            },
                        ),
                    },
                ),
                "ColumnTraysArrangementType": (
                    "OT",
                    "ns=1;i=1603",
                    {
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1604",
                            {},
                        ),
                        "NumberOfTrays": ("V", "ns=1;i=1605", {}),
                        "TrayTypeAssignmentClass": ("V", "ns=1;i=1606", {}),
                    },
                ),
                "CompressorEquipmentType": ("OT", "ns=1;i=1636", {}),
                "ControlledActuatorType": (
                    "OT",
                    "ns=1;i=1258",
                    {
                        "DeviceTypeNameAssignmentClass": ("V", "ns=1;i=1260", {}),
                        "FailActionRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1261",
                            {},
                        ),
                        "FailActionSpecialization": ("V", "ns=1;i=1262", {}),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1259", {}),
                    },
                ),
                "DEXPISupplementaryDataType": (
                    "OT",
                    "ns=1;i=1061",
                    {
                        "DEXPISpecificationVersion": ("V", "ns=1;i=1066", {}),
                        "DEXPIXMIExternalLink": ("V", "ns=1;i=1063", {}),
                        "DEXPIXMIFile": ("O", "ns=1;i=1064", {}),
                        "ProteusSchemaVersion": ("V", "ns=1;i=1067", {}),
                        "ProteusXMLExternalLink": ("V", "ns=1;i=1062", {}),
                        "ProteusXMLFile": ("O", "ns=1;i=1065", {}),
                    },
                ),
                "DirectPipingConnectionType": ("OT", "ns=1;i=1860", {}),
                "DisplacerType": (
                    "OT",
                    "ns=1;i=1656",
                    {
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1657",
                            {},
                        ),
                        "StageIdentifierAssignmentClass": ("V", "ns=1;i=1658", {}),
                        "VolumePerStroke": (
                            "V",
                            "ns=1;i=1659",
                            {
                                "EURange": ("V", "ns=1;i=1661", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1660", {}),
                            },
                        ),
                    },
                ),
                "EquipmentType": (
                    "OT",
                    "ns=1;i=1682",
                    {
                        "<Chamber>": ("O", "ns=1;i=2108", {}),
                        "<Nozzle>": ("O", "ns=1;i=2109", {}),
                        "AgitatorType": (
                            "OT",
                            "ns=1;i=1637",
                            {
                                "<Rotor>": ("O", "ns=1;i=2104", {}),
                                "DesignRotationalSpeed": (
                                    "V",
                                    "ns=1;i=1638",
                                    {
                                        "EURange": ("V", "ns=1;i=1640", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1639", {}),
                                    },
                                ),
                                "DesignShaftPower": (
                                    "V",
                                    "ns=1;i=1641",
                                    {
                                        "EURange": ("V", "ns=1;i=1643", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1642", {}),
                                    },
                                ),
                            },
                        ),
                        "CompressorType": (
                            "OT",
                            "ns=1;i=1408",
                            {
                                "AirEjectorType": (
                                    "OT",
                                    "ns=1;i=1620",
                                    {
                                        "<Impeller>": ("O", "ns=1;i=2103", {}),
                                        "DesignCapacityMotiveFluid": (
                                            "V",
                                            "ns=1;i=1621",
                                            {
                                                "EURange": ("V", "ns=1;i=1623", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1622",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "AxialCompressorType": (
                                    "OT",
                                    "ns=1;i=1645",
                                    {
                                        "<Impeller>": ("O", "ns=1;i=2105", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1646",
                                            {
                                                "EURange": ("V", "ns=1;i=1648", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1647",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1649",
                                            {
                                                "EURange": ("V", "ns=1;i=1651", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1650",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "CentrifugalCompressorType": (
                                    "OT",
                                    "ns=1;i=1566",
                                    {
                                        "<Impeller>": ("O", "ns=1;i=2099", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1567",
                                            {
                                                "EURange": ("V", "ns=1;i=1569", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1568",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1570",
                                            {
                                                "EURange": ("V", "ns=1;i=1572", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1571",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DesignVolumeFlowRate": (
                                    "V",
                                    "ns=1;i=1409",
                                    {
                                        "EURange": ("V", "ns=1;i=1411", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1410", {}),
                                    },
                                ),
                                "DifferentialPressure": (
                                    "V",
                                    "ns=1;i=1412",
                                    {
                                        "EURange": ("V", "ns=1;i=1414", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1413", {}),
                                    },
                                ),
                                "ReciprocatingCompressorType": (
                                    "OT",
                                    "ns=1;i=1379",
                                    {
                                        "<Displacer>": ("O", "ns=1;i=2089", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1380",
                                            {
                                                "EURange": ("V", "ns=1;i=1382", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1381",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1383",
                                            {
                                                "EURange": ("V", "ns=1;i=1385", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1384",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RotaryCompressorType": (
                                    "OT",
                                    "ns=1;i=1708",
                                    {
                                        "<Displacer>": ("O", "ns=1;i=2111", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1709",
                                            {
                                                "EURange": ("V", "ns=1;i=1711", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1710",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1712",
                                            {
                                                "EURange": ("V", "ns=1;i=1714", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1713",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "SpecialCompressorType": (
                                    "OT",
                                    "ns=1;i=1387",
                                    {
                                        "<CompressorEquipmentItem>": (
                                            "O",
                                            "ns=1;i=2090",
                                            {},
                                        ),
                                        "DesignCapacityMotiveFluid": (
                                            "V",
                                            "ns=1;i=1388",
                                            {
                                                "EURange": ("V", "ns=1;i=1390", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1389",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1391",
                                            {
                                                "EURange": ("V", "ns=1;i=1393", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1392",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1394",
                                            {
                                                "EURange": ("V", "ns=1;i=1396", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1395",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TypeNameAssignmentClass": (
                                            "V",
                                            "ns=1;i=1397",
                                            {},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "EquipmentDescriptionAssignmentClass": ("V", "ns=1;i=1683", {}),
                        "FilterType": (
                            "OT",
                            "ns=1;i=1619",
                            {
                                "GasFilterType": (
                                    "OT",
                                    "ns=1;i=1431",
                                    {
                                        "<FilterUnit>": ("O", "ns=1;i=2092", {}),
                                        "Capacity_VolumeFlowRate": (
                                            "V",
                                            "ns=1;i=1432",
                                            {
                                                "EURange": ("V", "ns=1;i=1434", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1433",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1438",
                                            {
                                                "EURange": ("V", "ns=1;i=1440", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1439",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1441",
                                            {
                                                "EURange": ("V", "ns=1;i=1443", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1442",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "UpperLimitAllowableDesignPressureDrop": (
                                            "V",
                                            "ns=1;i=1435",
                                            {
                                                "EURange": ("V", "ns=1;i=1437", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1436",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "LiquidFilterType": (
                                    "OT",
                                    "ns=1;i=1694",
                                    {
                                        "<FilterUnit>": ("O", "ns=1;i=2110", {}),
                                        "Capacity_VolumeFlowRate": (
                                            "V",
                                            "ns=1;i=1695",
                                            {
                                                "EURange": ("V", "ns=1;i=1697", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1696",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1698",
                                            {
                                                "EURange": ("V", "ns=1;i=1700", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1699",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1701",
                                            {
                                                "EURange": ("V", "ns=1;i=1703", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1702",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "UpperLimitAllowableDesignPressureDrop": (
                                            "V",
                                            "ns=1;i=1704",
                                            {
                                                "EURange": ("V", "ns=1;i=1706", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1705",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "HeatExchangerType": (
                            "OT",
                            "ns=1;i=1326",
                            {
                                "AirCoolingSystemType": (
                                    "OT",
                                    "ns=1;i=1478",
                                    {
                                        "<Rotor>": ("O", "ns=1;i=2094", {}),
                                        "DesignPower": (
                                            "V",
                                            "ns=1;i=1479",
                                            {
                                                "EURange": ("V", "ns=1;i=1481", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1480",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1482",
                                            {
                                                "EURange": ("V", "ns=1;i=1484", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1483",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1485",
                                            {
                                                "EURange": ("V", "ns=1;i=1487", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1486",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DesignHeatFlowRate": (
                                    "V",
                                    "ns=1;i=1327",
                                    {
                                        "EURange": ("V", "ns=1;i=1329", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1328", {}),
                                    },
                                ),
                                "DesignHeatTransferArea": (
                                    "V",
                                    "ns=1;i=1330",
                                    {
                                        "EURange": ("V", "ns=1;i=1332", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1331", {}),
                                    },
                                ),
                                "DesignHeatTransferCoefficient": (
                                    "V",
                                    "ns=1;i=1333",
                                    {
                                        "EURange": ("V", "ns=1;i=1335", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1334", {}),
                                    },
                                ),
                                "ElectricHeaterType": (
                                    "OT",
                                    "ns=1;i=1557",
                                    {
                                        "<TubeBundle>": ("O", "ns=1;i=2098", {}),
                                        "DesignPower": (
                                            "V",
                                            "ns=1;i=1558",
                                            {
                                                "EURange": ("V", "ns=1;i=1560", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1559",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "PlateAndShellHeatExchangerType": (
                                    "OT",
                                    "ns=1;i=1576",
                                    {
                                        "NumberOfPlates": ("V", "ns=1;i=1577", {}),
                                        "PlateHeight": (
                                            "V",
                                            "ns=1;i=1578",
                                            {
                                                "EURange": ("V", "ns=1;i=1580", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1579",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "PlateWidth": (
                                            "V",
                                            "ns=1;i=1581",
                                            {
                                                "EURange": ("V", "ns=1;i=1583", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1582",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "ShellAndTubeHeatExchangerType": (
                                    "OT",
                                    "ns=1;i=1653",
                                    {
                                        "<TubeBundle>": ("O", "ns=1;i=2106", {}),
                                        "TemaStandardTypeAssignmentClass": (
                                            "V",
                                            "ns=1;i=1654",
                                            {},
                                        ),
                                    },
                                ),
                                "SpiralHeatExchangerType": ("OT", "ns=1;i=1369", {}),
                                "ThinFilmEvaporatorType": (
                                    "OT",
                                    "ns=1;i=1350",
                                    {
                                        "<Rotor>": ("O", "ns=1;i=2086", {}),
                                        "DesignPower": (
                                            "V",
                                            "ns=1;i=1351",
                                            {
                                                "EURange": ("V", "ns=1;i=1353", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1352",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1354",
                                            {
                                                "EURange": ("V", "ns=1;i=1356", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1355",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1357",
                                            {
                                                "EURange": ("V", "ns=1;i=1359", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1358",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "MixerType": (
                            "OT",
                            "ns=1;i=1454",
                            {
                                "<MixingElementAssembly>": ("O", "ns=1;i=2093", {}),
                                "KneaderType": (
                                    "OT",
                                    "ns=1;i=1316",
                                    {
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1317",
                                            {
                                                "EURange": ("V", "ns=1;i=1319", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1318",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1320",
                                            {
                                                "EURange": ("V", "ns=1;i=1322", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1321",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "UpperLimitAllowableDesignPressureDrop": (
                                            "V",
                                            "ns=1;i=1323",
                                            {
                                                "EURange": ("V", "ns=1;i=1325", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1324",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RotaryMixerType": (
                                    "OT",
                                    "ns=1;i=1415",
                                    {
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1419",
                                            {
                                                "EURange": ("V", "ns=1;i=1421", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1420",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1422",
                                            {
                                                "EURange": ("V", "ns=1;i=1424", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1423",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "UpperLimitAllowableDesignPressureDrop": (
                                            "V",
                                            "ns=1;i=1416",
                                            {
                                                "EURange": ("V", "ns=1;i=1418", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1417",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "StaticMixerType": (
                                    "OT",
                                    "ns=1;i=1625",
                                    {
                                        "UpperLimitAllowableDesignPressureDrop": (
                                            "V",
                                            "ns=1;i=1626",
                                            {
                                                "EURange": ("V", "ns=1;i=1628", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1627",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                            },
                        ),
                        "ProcessColumnType": (
                            "OT",
                            "ns=1;i=1667",
                            {
                                "<ColumnSection>": ("O", "ns=1;i=2107", {}),
                                "NominalCapacityVolume": (
                                    "V",
                                    "ns=1;i=1668",
                                    {
                                        "EURange": ("V", "ns=1;i=1670", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1669", {}),
                                    },
                                ),
                            },
                        ),
                        "PumpType": (
                            "OT",
                            "ns=1;i=1716",
                            {
                                "CentrifugalPumpType": (
                                    "OT",
                                    "ns=1;i=1584",
                                    {
                                        "<Impeller>": ("O", "ns=1;i=2101", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1585",
                                            {
                                                "EURange": ("V", "ns=1;i=1587", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1586",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1588",
                                            {
                                                "EURange": ("V", "ns=1;i=1590", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1589",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DesignPressureHead": (
                                    "V",
                                    "ns=1;i=1720",
                                    {
                                        "EURange": ("V", "ns=1;i=1722", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1721", {}),
                                    },
                                ),
                                "DesignVolumeFlowRate": (
                                    "V",
                                    "ns=1;i=1717",
                                    {
                                        "EURange": ("V", "ns=1;i=1719", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1718", {}),
                                    },
                                ),
                                "DifferentialPressure": (
                                    "V",
                                    "ns=1;i=1723",
                                    {
                                        "EURange": ("V", "ns=1;i=1725", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1724", {}),
                                    },
                                ),
                                "EjectorPumpType": (
                                    "OT",
                                    "ns=1;i=1312",
                                    {
                                        "DesignCapacityMotiveFluid": (
                                            "V",
                                            "ns=1;i=1313",
                                            {
                                                "EURange": ("V", "ns=1;i=1315", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1314",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                                "ReciprocatingPumpType": (
                                    "OT",
                                    "ns=1;i=1503",
                                    {
                                        "<Displacer>": ("O", "ns=1;i=2096", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1504",
                                            {
                                                "EURange": ("V", "ns=1;i=1506", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1505",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1507",
                                            {
                                                "EURange": ("V", "ns=1;i=1509", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1508",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RotaryPumpType": (
                                    "OT",
                                    "ns=1;i=1342",
                                    {
                                        "<Displacer>": ("O", "ns=1;i=2085", {}),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1343",
                                            {
                                                "EURange": ("V", "ns=1;i=1345", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1344",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1346",
                                            {
                                                "EURange": ("V", "ns=1;i=1348", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1347",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "SpecialPumpType": (
                                    "OT",
                                    "ns=1;i=1607",
                                    {
                                        "<PumpEquipmentItem>": ("O", "ns=1;i=2102", {}),
                                        "DesignCapacityMotiveFluid": (
                                            "V",
                                            "ns=1;i=1609",
                                            {
                                                "EURange": ("V", "ns=1;i=1611", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1610",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignRotationalSpeed": (
                                            "V",
                                            "ns=1;i=1612",
                                            {
                                                "EURange": ("V", "ns=1;i=1614", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1613",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DesignShaftPower": (
                                            "V",
                                            "ns=1;i=1615",
                                            {
                                                "EURange": ("V", "ns=1;i=1617", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1616",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TypeNameAssignmentClass": (
                                            "V",
                                            "ns=1;i=1608",
                                            {},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "TagNameAssignmentClass": ("V", "ns=1;i=1686", {}),
                        "TagNamePrefixAssignmentClass": ("V", "ns=1;i=1687", {}),
                        "TagNameSequenceNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1688",
                            {},
                        ),
                        "TagNameSuffixAssignmentClass": ("V", "ns=1;i=1689", {}),
                        "TaggedColumnSectionType": (
                            "OT",
                            "ns=1;i=1511",
                            {
                                "<Internal>": ("O", "ns=1;i=2097", {}),
                                "Height": (
                                    "V",
                                    "ns=1;i=1516",
                                    {
                                        "EURange": ("V", "ns=1;i=1518", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1517", {}),
                                    },
                                ),
                                "InsideDiameter": (
                                    "V",
                                    "ns=1;i=1519",
                                    {
                                        "EURange": ("V", "ns=1;i=1521", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1520", {}),
                                    },
                                ),
                                "TagNameAssignmentClass": ("V", "ns=1;i=1512", {}),
                                "TagNamePrefixAssignmentClass": (
                                    "V",
                                    "ns=1;i=1513",
                                    {},
                                ),
                                "TagNameSequenceNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1514",
                                    {},
                                ),
                                "TagNameSuffixAssignmentClass": (
                                    "V",
                                    "ns=1;i=1515",
                                    {},
                                ),
                            },
                        ),
                        "VesselType": (
                            "OT",
                            "ns=1;i=1425",
                            {
                                "NominalCapacityVolume": (
                                    "V",
                                    "ns=1;i=1426",
                                    {
                                        "EURange": ("V", "ns=1;i=1428", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1427", {}),
                                    },
                                ),
                                "PressureVesselType": (
                                    "OT",
                                    "ns=1;i=1445",
                                    {
                                        "CylinderLength": (
                                            "V",
                                            "ns=1;i=1446",
                                            {
                                                "EURange": ("V", "ns=1;i=1448", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1447",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                                "SiloType": ("OT", "ns=1;i=1490", {}),
                                "SpecialVesselType": (
                                    "OT",
                                    "ns=1;i=1449",
                                    {
                                        "CylinderLength": (
                                            "V",
                                            "ns=1;i=1450",
                                            {
                                                "EURange": ("V", "ns=1;i=1452", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1451",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TypeNameAssignmentClass": (
                                            "V",
                                            "ns=1;i=1453",
                                            {},
                                        ),
                                    },
                                ),
                                "TankType": (
                                    "OT",
                                    "ns=1;i=1663",
                                    {
                                        "CylinderLength": (
                                            "V",
                                            "ns=1;i=1664",
                                            {
                                                "EURange": ("V", "ns=1;i=1666", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1665",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "FilterUnitType": (
                    "OT",
                    "ns=1;i=1456",
                    {
                        "Efficiency": (
                            "V",
                            "ns=1;i=1458",
                            {
                                "EURange": ("V", "ns=1;i=1460", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1459", {}),
                            },
                        ),
                        "FilterArea": (
                            "V",
                            "ns=1;i=1461",
                            {
                                "EURange": ("V", "ns=1;i=1463", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1462", {}),
                            },
                        ),
                        "LowerLimitAllowableSolidsConcentration": (
                            "V",
                            "ns=1;i=1464",
                            {
                                "EURange": ("V", "ns=1;i=1466", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1465", {}),
                            },
                        ),
                        "LowerLimitPermeableParticleDiameter": (
                            "V",
                            "ns=1;i=1467",
                            {
                                "EURange": ("V", "ns=1;i=1469", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1468", {}),
                            },
                        ),
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1470",
                            {},
                        ),
                        "NumberOfFilterElements": ("V", "ns=1;i=1471", {}),
                        "UpperLimitAllowableSolidsConcentration": (
                            "V",
                            "ns=1;i=1472",
                            {
                                "EURange": ("V", "ns=1;i=1474", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1473", {}),
                            },
                        ),
                        "UpperLimitPermeableParticleDiameter": (
                            "V",
                            "ns=1;i=1475",
                            {
                                "EURange": ("V", "ns=1;i=1477", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1476", {}),
                            },
                        ),
                    },
                ),
                "FlowInPipeConnectorSymbolType": (
                    "OT",
                    "ns=1;i=1827",
                    {"<Node>": ("O", "ns=1;i=2115", {})},
                ),
                "FlowOutPipeConnectorSymbolType": (
                    "OT",
                    "ns=1;i=1829",
                    {"<Node>": ("O", "ns=1;i=2116", {})},
                ),
                "HeatExchangerRotorType": (
                    "OT",
                    "ns=1;i=1491",
                    {
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1492",
                            {},
                        )
                    },
                ),
                "HeatTransferCoefficientType": (
                    "OT",
                    "ns=1;i=2018",
                    {
                        "Unit": ("V", "ns=1;i=2019", {}),
                        "Value": ("V", "ns=1;i=2021", {}),
                    },
                ),
                "ImpellerType": (
                    "OT",
                    "ns=1;i=1629",
                    {
                        "Diameter": (
                            "V",
                            "ns=1;i=1630",
                            {
                                "EURange": ("V", "ns=1;i=1632", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1631", {}),
                            },
                        ),
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1633",
                            {},
                        ),
                        "StageIdentifierAssignmentClass": ("V", "ns=1;i=1634", {}),
                    },
                ),
                "IndustrialComplexIso10209-2012ParentStructureType": (
                    "OT",
                    "ns=1;i=1284",
                    {},
                ),
                "IndustrialComplexIso10209-2012Type": (
                    "OT",
                    "ns=1;i=1272",
                    {
                        "IndustrialComplexIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1273",
                            {},
                        ),
                        "IndustrialComplexNameAssignmentClass": (
                            "V",
                            "ns=1;i=1274",
                            {},
                        ),
                    },
                ),
                "InstrumentationLoopFunctionType": (
                    "OT",
                    "ns=1;i=1188",
                    {
                        "InstrumentationLoopFunctionNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1190",
                            {},
                        )
                    },
                ),
                "Isa95EnterpriseType": (
                    "OT",
                    "ns=1;i=1305",
                    {
                        "EnterpriseIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1306",
                            {},
                        ),
                        "EnterpriseNameAssignmentClass": ("V", "ns=1;i=1307", {}),
                    },
                ),
                "LengthType": (
                    "OT",
                    "ns=1;i=2041",
                    {
                        "Unit": ("V", "ns=1;i=2042", {}),
                        "Value": ("V", "ns=1;i=2044", {}),
                    },
                ),
                "MassType": (
                    "OT",
                    "ns=1;i=2053",
                    {
                        "Unit": ("V", "ns=1;i=2054", {}),
                        "Value": ("V", "ns=1;i=2056", {}),
                    },
                ),
                "MeasuringLineFunctionType": (
                    "OT",
                    "ns=1;i=1181",
                    {
                        "PortStatusSpecialization": ("V", "ns=1;i=1182", {}),
                        "SignalConveyingTypeSpecialization": ("V", "ns=1;i=1183", {}),
                        "SignalPointNumberAssignmentClass": ("V", "ns=1;i=1184", {}),
                        "SignalProcessControlFunctionsAssignmentClass": (
                            "V",
                            "ns=1;i=1185",
                            {},
                        ),
                    },
                ),
                "MetaDataType": (
                    "OT",
                    "ns=1;i=1079",
                    {
                        "ApprovalDateRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1080",
                            {},
                        ),
                        "ApprovalDescriptionAssignmentClass": ("V", "ns=1;i=1081", {}),
                        "ApproverNameAssignmentClass": ("V", "ns=1;i=1082", {}),
                        "ArchiveNumberAssignmentClass": ("V", "ns=1;i=1083", {}),
                        "AreaIsa95NameAssignmentClass": ("V", "ns=1;i=1084", {}),
                        "BlockNameAssignmentClass": ("V", "ns=1;i=1085", {}),
                        "BlockNumberAssignmentClass": ("V", "ns=1;i=1086", {}),
                        "CheckerNameAssignmentClass": ("V", "ns=1;i=1087", {}),
                        "CompanyNameAssignmentClass": ("V", "ns=1;i=1088", {}),
                        "CompanyNumberAssignmentClass": ("V", "ns=1;i=1089", {}),
                        "ConfidentialitySpecialization": ("V", "ns=1;i=1090", {}),
                        "CreationDateRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1091",
                            {},
                        ),
                        "CreatorNameAssignmentClass": ("V", "ns=1;i=1092", {}),
                        "DesignerNameAssignmentClass": ("V", "ns=1;i=1093", {}),
                        "DrafterNameAssignmentClass": ("V", "ns=1;i=1094", {}),
                        "DrawingNameAssignmentClass": ("V", "ns=1;i=1096", {}),
                        "DrawingNumberAssignmentClass": ("V", "ns=1;i=1095", {}),
                        "DrawingSubTitleAssignmentClass": ("V", "ns=1;i=1097", {}),
                        "FileNameAssignmentClass": ("V", "ns=1;i=1098", {}),
                        "LocationNameAssignmentClass": ("V", "ns=1;i=1099", {}),
                        "ModificationDataRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1100",
                            {},
                        ),
                        "ProcessCellIsa95NameAssignmentClass": ("V", "ns=1;i=1101", {}),
                        "ProcessCellIsa95NumberAssignmentClass": (
                            "V",
                            "ns=1;i=1102",
                            {},
                        ),
                        "ProjectNameAssignmentClass": ("V", "ns=1;i=1103", {}),
                        "ProjectNumberAssignmentClass": ("V", "ns=1;i=1104", {}),
                        "ProjectRangeNumberAssignmentClass": ("V", "ns=1;i=1105", {}),
                        "ReplacedDrawingAssignmentClass": ("V", "ns=1;i=1106", {}),
                        "ResponsibleDepartmentNameAssignmentClass": (
                            "V",
                            "ns=1;i=1107",
                            {},
                        ),
                        "RevisionNumberAssignmentClass": ("V", "ns=1;i=1108", {}),
                        "SheetFormatAssignmentClass": ("V", "ns=1;i=1109", {}),
                        "SheetNumberAssignmentClass": ("V", "ns=1;i=1110", {}),
                        "SiteIsa95NameAssignmentClass": ("V", "ns=1;i=1111", {}),
                        "SubProjectNameAssignmentClass": ("V", "ns=1;i=1112", {}),
                        "SubProjectNumberAssignmentClass": ("V", "ns=1;i=1113", {}),
                        "TotalNumberOfSheets": ("V", "ns=1;i=1114", {}),
                        "UnitIsa95NameAssignmentClass": ("V", "ns=1;i=1115", {}),
                        "UnitIsa95NumberAssignmentClass": ("V", "ns=1;i=1116", {}),
                    },
                ),
                "MixingElementAssemblyType": (
                    "OT",
                    "ns=1;i=1562",
                    {
                        "MaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1564",
                            {},
                        ),
                        "MixingElementAssembly": ("V", "ns=1;i=1565", {}),
                    },
                ),
                "NozzleOwnerType": (
                    "OT",
                    "ns=1;i=1574",
                    {"<Nozzle>": ("O", "ns=1;i=2100", {})},
                ),
                "NozzleType": (
                    "OT",
                    "ns=1;i=1361",
                    {
                        "<Node>": ("O", "ns=1;i=2087", {}),
                        "NominalPressureNumericalValueRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1363",
                            {},
                        ),
                        "NominalPressureRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1364",
                            {},
                        ),
                        "NominalPressureStandardSpecialization": (
                            "V",
                            "ns=1;i=1365",
                            {},
                        ),
                        "NominalPressureTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1366",
                            {},
                        ),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1362", {}),
                    },
                ),
                "OrificePlateType": (
                    "OT",
                    "ns=1;i=1976",
                    {
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1981", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1982", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1983",
                            {
                                "EURange": ("V", "ns=1;i=1985", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1984", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1986", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1978",
                            {
                                "EURange": ("V", "ns=1;i=1980", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1979", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1987", {}),
                        "PipingComponentNameAssignmentClass": ("V", "ns=1;i=1988", {}),
                        "PipingComponentNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1977",
                            {},
                        ),
                    },
                ),
                "PercentageType": (
                    "OT",
                    "ns=1;i=2045",
                    {
                        "Unit": ("V", "ns=1;i=2046", {}),
                        "Value": ("V", "ns=1;i=2048", {}),
                    },
                ),
                "PhysicalQuantityType": (
                    "OT",
                    "ns=1;i=2026",
                    {"Value": ("V", "ns=1;i=2028", {})},
                ),
                "PipeConnectorSymbolType": (
                    "OT",
                    "ns=1;i=1786",
                    {"<Node>": ("O", "ns=1;i=2114", {})},
                ),
                "PipeType": ("OT", "ns=1;i=1890", {}),
                "PipingComponentType": (
                    "OT",
                    "ns=1;i=1995",
                    {
                        "<Node>": ("O", "ns=1;i=2120", {}),
                        "BasfLineClassAssignmentClass": ("V", "ns=1;i=1996", {}),
                        "CheckValveType": (
                            "OT",
                            "ns=1;i=1773",
                            {
                                "GlobeCheckValveType": ("OT", "ns=1;i=1874", {}),
                                "HeatTracingTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1775",
                                    {},
                                ),
                                "HeatTracingTypeSpecialization": (
                                    "V",
                                    "ns=1;i=1776",
                                    {},
                                ),
                                "InsulationThickness": (
                                    "V",
                                    "ns=1;i=1777",
                                    {
                                        "EURange": ("V", "ns=1;i=1779", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1778", {}),
                                    },
                                ),
                                "InsulationTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1780",
                                    {},
                                ),
                                "LowerLimitHeatTracingTemperature": (
                                    "V",
                                    "ns=1;i=1781",
                                    {
                                        "EURange": ("V", "ns=1;i=1783", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1782", {}),
                                    },
                                ),
                                "PipingClassCodeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1784",
                                    {},
                                ),
                                "PipingComponentNameAssignmentClass": (
                                    "V",
                                    "ns=1;i=1785",
                                    {},
                                ),
                                "PipingComponentNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1774",
                                    {},
                                ),
                                "SwingCheckValveType": ("OT", "ns=1;i=1937", {}),
                            },
                        ),
                        "FluidCodeAssignmentClass": ("V", "ns=1;i=1997", {}),
                        "InlinePrimaryElementType": (
                            "OT",
                            "ns=1;i=1793",
                            {
                                "ElectromagneticFlowMeterType": (
                                    "OT",
                                    "ns=1;i=1811",
                                    {},
                                ),
                                "FlowDetectorType": ("OT", "ns=1;i=1865", {}),
                                "FlowNozzleType": ("OT", "ns=1;i=1956", {}),
                                "HeatTracingTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1798",
                                    {},
                                ),
                                "HeatTracingTypeSpecialization": (
                                    "V",
                                    "ns=1;i=1799",
                                    {},
                                ),
                                "InsulationThickness": (
                                    "V",
                                    "ns=1;i=1800",
                                    {
                                        "EURange": ("V", "ns=1;i=1802", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1801", {}),
                                    },
                                ),
                                "InsulationTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1803",
                                    {},
                                ),
                                "LowerLimitHeatTracingTemperature": (
                                    "V",
                                    "ns=1;i=1795",
                                    {
                                        "EURange": ("V", "ns=1;i=1797", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1796", {}),
                                    },
                                ),
                                "PipingComponentNameAssignmentClass": (
                                    "V",
                                    "ns=1;i=1804",
                                    {},
                                ),
                                "PipingComponentNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1794",
                                    {},
                                ),
                                "PositiveDisplacementFlowMeterType": (
                                    "OT",
                                    "ns=1;i=1809",
                                    {},
                                ),
                                "TurbineFlowMeterType": ("OT", "ns=1;i=1755", {}),
                                "VariableAreaFlowMeterType": ("OT", "ns=1;i=1810", {}),
                                "VenturiTubeType": ("OT", "ns=1;i=1955", {}),
                                "VolumetricFlowDetectorType": ("OT", "ns=1;i=1895", {}),
                            },
                        ),
                        "NominalDiametersRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1998",
                            {},
                        ),
                        "OnHoldSpecialization": ("V", "ns=1;i=1999", {}),
                        "PipeFittingType": (
                            "OT",
                            "ns=1;i=1877",
                            {
                                "BlindFlangeType": ("OT", "ns=1;i=1871", {}),
                                "ClampedFlangeCouplingType": ("OT", "ns=1;i=1897", {}),
                                "CompensatorType": ("OT", "ns=1;i=1792", {}),
                                "ConicalStrainerType": ("OT", "ns=1;i=1866", {}),
                                "FlangeType": ("OT", "ns=1;i=1788", {}),
                                "FlangedConnectionType": ("OT", "ns=1;i=1805", {}),
                                "FunnelType": ("OT", "ns=1;i=1770", {}),
                                "HeatTracingTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1882",
                                    {},
                                ),
                                "HeatTracingTypeSpecialization": (
                                    "V",
                                    "ns=1;i=1883",
                                    {},
                                ),
                                "HoseType": ("OT", "ns=1;i=1806", {}),
                                "IlluminatedSightGlassType": ("OT", "ns=1;i=1825", {}),
                                "InLineMixerType": ("OT", "ns=1;i=1772", {}),
                                "InsulationThickness": (
                                    "V",
                                    "ns=1;i=1884",
                                    {
                                        "EURange": ("V", "ns=1;i=1886", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1885", {}),
                                    },
                                ),
                                "InsulationTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1887",
                                    {},
                                ),
                                "LineBlindType": ("OT", "ns=1;i=2005", {}),
                                "LowerLimitHeatTracingTemperature": (
                                    "V",
                                    "ns=1;i=1879",
                                    {
                                        "EURange": ("V", "ns=1;i=1881", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1880", {}),
                                    },
                                ),
                                "PenetrationType": ("OT", "ns=1;i=1936", {}),
                                "PipeCouplingType": ("OT", "ns=1;i=1971", {}),
                                "PipeFlangeSpacerType": ("OT", "ns=1;i=1870", {}),
                                "PipeFlangeSpadeType": ("OT", "ns=1;i=1896", {}),
                                "PipeReducerType": ("OT", "ns=1;i=2004", {}),
                                "PipeTeeType": ("OT", "ns=1;i=1875", {}),
                                "PipingClassCodeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1888",
                                    {},
                                ),
                                "PipingComponentNameAssignmentClass": (
                                    "V",
                                    "ns=1;i=1889",
                                    {},
                                ),
                                "PipingComponentNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1878",
                                    {},
                                ),
                                "SightGlassType": ("OT", "ns=1;i=1867", {}),
                            },
                        ),
                        "PipingClassArtefactSpecialization": ("V", "ns=1;i=2000", {}),
                        "PressureTestCircuitNumberAssignmentClass": (
                            "V",
                            "ns=1;i=2001",
                            {},
                        ),
                        "SafetyValveOrFittingType": (
                            "OT",
                            "ns=1;i=1944",
                            {
                                "BreatherValveType": ("OT", "ns=1;i=1868", {}),
                                "FlameArrestorType": (
                                    "OT",
                                    "ns=1;i=1972",
                                    {
                                        "DetonationProofArtefactSpecialization": (
                                            "V",
                                            "ns=1;i=1973",
                                            {},
                                        ),
                                        "ExplosionProofArtefactSpecialization": (
                                            "V",
                                            "ns=1;i=1974",
                                            {},
                                        ),
                                        "FireResistantArtefactSpecialization": (
                                            "V",
                                            "ns=1;i=1975",
                                            {},
                                        ),
                                    },
                                ),
                                "FlowInPipingClassCodeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1947",
                                    {},
                                ),
                                "FlowOutPipingClassCodeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1948",
                                    {},
                                ),
                                "LocationRegistrationNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1946",
                                    {},
                                ),
                                "PositionNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1945",
                                    {},
                                ),
                                "RuptureDiscType": ("OT", "ns=1;i=1872", {}),
                                "SetPressureHigh": (
                                    "V",
                                    "ns=1;i=1952",
                                    {
                                        "EURange": ("V", "ns=1;i=1954", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1953", {}),
                                    },
                                ),
                                "SetPressureLow": (
                                    "V",
                                    "ns=1;i=1949",
                                    {
                                        "EURange": ("V", "ns=1;i=1951", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1950", {}),
                                    },
                                ),
                                "SpringLoadedAngleGlobeSafetyValveType": (
                                    "OT",
                                    "ns=1;i=1876",
                                    {},
                                ),
                                "SpringLoadedGlobeSafetyValveType": (
                                    "OT",
                                    "ns=1;i=1831",
                                    {},
                                ),
                            },
                        ),
                        "ShutOffValveType": (
                            "OT",
                            "ns=1;i=1845",
                            {
                                "AngleBallValveType": ("OT", "ns=1;i=1789", {}),
                                "AngleGlobeValveType": ("OT", "ns=1;i=1808", {}),
                                "AnglePlugValveType": ("OT", "ns=1;i=1957", {}),
                                "AngleValveType": ("OT", "ns=1;i=1756", {}),
                                "BallValveType": ("OT", "ns=1;i=1790", {}),
                                "ButterflyValveType": ("OT", "ns=1;i=1994", {}),
                                "GateValveType": ("OT", "ns=1;i=2003", {}),
                                "GlobeValveType": ("OT", "ns=1;i=1869", {}),
                                "HeatTracingTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1847",
                                    {},
                                ),
                                "HeatTracingTypeSpecialization": (
                                    "V",
                                    "ns=1;i=1848",
                                    {},
                                ),
                                "InsulationThickness": (
                                    "V",
                                    "ns=1;i=1849",
                                    {
                                        "EURange": ("V", "ns=1;i=1851", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1850", {}),
                                    },
                                ),
                                "InsulationTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1852",
                                    {},
                                ),
                                "LowerLimitHeatTracingTemperature": (
                                    "V",
                                    "ns=1;i=1853",
                                    {
                                        "EURange": ("V", "ns=1;i=1855", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1854", {}),
                                    },
                                ),
                                "NeedleValveType": ("OT", "ns=1;i=1771", {}),
                                "NumberOfPortsSpecialization": ("V", "ns=1;i=1858", {}),
                                "OperationSpecialization": ("V", "ns=1;i=1859", {}),
                                "PipingClassCodeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1856",
                                    {},
                                ),
                                "PipingComponentNameAssignmentClass": (
                                    "V",
                                    "ns=1;i=1857",
                                    {},
                                ),
                                "PipingComponentNumberAssignmentClass": (
                                    "V",
                                    "ns=1;i=1846",
                                    {},
                                ),
                                "PlugValveType": ("OT", "ns=1;i=1791", {}),
                                "StraightwayValveType": ("OT", "ns=1;i=1873", {}),
                            },
                        ),
                    },
                ),
                "PipingConnectionType": ("OT", "ns=1;i=1989", {}),
                "PipingNetworkSegmentItemType": ("OT", "ns=1;i=1754", {}),
                "PipingNetworkSegmentType": (
                    "OT",
                    "ns=1;i=1898",
                    {
                        "<Connection>": ("O", "ns=1;i=2118", {}),
                        "<Item>": ("O", "ns=1;i=2117", {}),
                        "BasfLineClassAssignmentClass": ("V", "ns=1;i=1900", {}),
                        "ColorCodeAssignmentClass": ("V", "ns=1;i=1901", {}),
                        "FlowDirectionSpecialization": ("V", "ns=1;i=1902", {}),
                        "FluidCodeAssignmentClass": ("V", "ns=1;i=1903", {}),
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1904", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1905", {}),
                        "Inclination": (
                            "V",
                            "ns=1;i=1906",
                            {
                                "EURange": ("V", "ns=1;i=1908", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1907", {}),
                            },
                        ),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1909",
                            {
                                "EURange": ("V", "ns=1;i=1911", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1910", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1912", {}),
                        "JacketedPipeSpecialization": ("V", "ns=1;i=1913", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1914",
                            {
                                "EURange": ("V", "ns=1;i=1916", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1915", {}),
                            },
                        ),
                        "NominalDiameterNumericalValueRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1917",
                            {},
                        ),
                        "NominalDiameterRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1918",
                            {},
                        ),
                        "NominalDiameterStandardSpecialization": (
                            "V",
                            "ns=1;i=1919",
                            {},
                        ),
                        "NominalDiameterTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1920",
                            {},
                        ),
                        "OnHoldSpecialization": ("V", "ns=1;i=1921", {}),
                        "OperatingTemperature": (
                            "V",
                            "ns=1;i=1922",
                            {
                                "EURange": ("V", "ns=1;i=1924", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1923", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1925", {}),
                        "PressureTestCircuitNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1926",
                            {},
                        ),
                        "PrimarySecondaryPipingNetworkSegmentSpecialization": (
                            "V",
                            "ns=1;i=1927",
                            {},
                        ),
                        "SegmentNumberAssignmentClass": ("V", "ns=1;i=1899", {}),
                        "SiphonSpecialization": ("V", "ns=1;i=1928", {}),
                        "SlopeSpecialization": ("V", "ns=1;i=1929", {}),
                    },
                ),
                "PipingNetworkSystemType": (
                    "OT",
                    "ns=1;i=1726",
                    {
                        "<PropertyBreak>": ("O", "ns=1;i=2113", {}),
                        "<Segment>": ("O", "ns=1;i=2112", {}),
                        "FluidCodeAssignmentClass": ("V", "ns=1;i=1728", {}),
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1736", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1737", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1729",
                            {
                                "EURange": ("V", "ns=1;i=1731", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1730", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1732", {}),
                        "JacketLineNumberAssignmentClass": ("V", "ns=1;i=1739", {}),
                        "JacketedLineNumberAssignmentClass": ("V", "ns=1;i=1738", {}),
                        "JacketedPipeSpecialization": ("V", "ns=1;i=1740", {}),
                        "LineNumberAssignmentClassOfPipingNetworkSystem": (
                            "V",
                            "ns=1;i=1727",
                            {},
                        ),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1733",
                            {
                                "EURange": ("V", "ns=1;i=1735", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1734", {}),
                            },
                        ),
                        "NominalDiameterNumericalValueRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1742",
                            {},
                        ),
                        "NominalDiameterRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1743",
                            {},
                        ),
                        "NominalDiameterStandardSpecialization": (
                            "V",
                            "ns=1;i=1741",
                            {},
                        ),
                        "NominalDiameterTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1744",
                            {},
                        ),
                        "OnHoldSpecialization": ("V", "ns=1;i=1745", {}),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1746", {}),
                        "PipingNetworkSystemGroupNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1747",
                            {},
                        ),
                    },
                ),
                "PipingNodeOwnerType": (
                    "OT",
                    "ns=1;i=2006",
                    {"<Node>": ("O", "ns=1;i=2121", {})},
                ),
                "PipingNodeType": (
                    "OT",
                    "ns=1;i=2008",
                    {
                        "NodeFlowSpecialization": ("V", "ns=1;i=2009", {}),
                        "NominalDiameterNumericalValueRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=2010",
                            {},
                        ),
                        "NominalDiameterRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=2011",
                            {},
                        ),
                        "NominalDiameterStandardSpecialization": (
                            "V",
                            "ns=1;i=2012",
                            {},
                        ),
                        "NominalDiameterTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=2013",
                            {},
                        ),
                    },
                ),
                "PipingSourceItemType": ("OT", "ns=1;i=1807", {}),
                "PipingTargetItemType": ("OT", "ns=1;i=1826", {}),
                "PlantModelType": (
                    "OT",
                    "ns=1;i=1068",
                    {
                        "<MetaData>": ("O", "ns=1;i=2065", {}),
                        "<Plant>": ("O", "ns=1;i=2067", {}),
                        "<StructureItem>": ("O", "ns=1;i=2066", {}),
                    },
                ),
                "PlantSectionIso10209-2012ParentStructureType": (
                    "OT",
                    "ns=1;i=1296",
                    {},
                ),
                "PlantSectionIso10209-2012Type": (
                    "OT",
                    "ns=1;i=1265",
                    {
                        "PlantSectionIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1266",
                            {},
                        ),
                        "PlantSectionNameAssignmentClass": ("V", "ns=1;i=1267", {}),
                    },
                ),
                "PlantStructureItemType": ("OT", "ns=1;i=1308", {}),
                "PlantSystemLocatedStructureType": ("OT", "ns=1;i=1293", {}),
                "PlantSystemType": (
                    "OT",
                    "ns=1;i=1297",
                    {
                        "PlantSystemIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1298",
                            {},
                        ),
                        "PlantSystemNameAssignmentClass": ("V", "ns=1;i=1299", {}),
                    },
                ),
                "PlantTrainLocatedStructureType": ("OT", "ns=1;i=1277", {}),
                "PlantTrainType": (
                    "OT",
                    "ns=1;i=1309",
                    {
                        "PlantTrainIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1310",
                            {},
                        ),
                        "PlantTrainNameAssignmentClass": ("V", "ns=1;i=1311", {}),
                    },
                ),
                "PlantType": (
                    "OT",
                    "ns=1;i=1072",
                    {
                        "<ActuatingSystem>": ("O", "ns=1;i=2068", {}),
                        "<InstrumentationLoopFunction>": ("O", "ns=1;i=2069", {}),
                        "<PipingNetworkSystem>": ("O", "ns=1;i=2070", {}),
                        "<ProcessInstrumentationFunction>": ("O", "ns=1;i=2071", {}),
                        "<ProcessSignalGeneratingSystem>": ("O", "ns=1;i=2072", {}),
                        "<TaggedPlantItem>": ("O", "ns=1;i=2073", {}),
                    },
                ),
                "PositionerType": (
                    "OT",
                    "ns=1;i=1127",
                    {
                        "DeviceTypeNameAssignmentClass": ("V", "ns=1;i=1129", {}),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1128", {}),
                    },
                ),
                "PowerType": (
                    "OT",
                    "ns=1;i=2037",
                    {
                        "Unit": ("V", "ns=1;i=2038", {}),
                        "Value": ("V", "ns=1;i=2040", {}),
                    },
                ),
                "PressureType": (
                    "OT",
                    "ns=1;i=2057",
                    {
                        "Unit": ("V", "ns=1;i=2058", {}),
                        "Value": ("V", "ns=1;i=2060", {}),
                    },
                ),
                "PrimaryElementType": (
                    "OT",
                    "ns=1;i=1195",
                    {
                        "InlinePrimaryElementReferenceType": ("OT", "ns=1;i=1263", {}),
                        "OfflinePrimaryElementType": (
                            "OT",
                            "ns=1;i=1220",
                            {
                                "ConnectionNominalDiameterNumericalValueRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1221",
                                    {},
                                ),
                                "ConnectionNominalDiameterRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1222",
                                    {},
                                ),
                                "ConnectionNominalDiameterStandardSpecialization": (
                                    "V",
                                    "ns=1;i=1223",
                                    {},
                                ),
                                "ConnectionNominalDiameterTypeRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1224",
                                    {},
                                ),
                                "FluidCodeAssignmentClass": ("V", "ns=1;i=1225", {}),
                                "HeatTracingTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1226",
                                    {},
                                ),
                                "HeatTracingTypeSpecialization": (
                                    "V",
                                    "ns=1;i=1227",
                                    {},
                                ),
                                "InsulationThickness": (
                                    "V",
                                    "ns=1;i=1228",
                                    {
                                        "EURange": ("V", "ns=1;i=1230", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1229", {}),
                                    },
                                ),
                                "InsulationTypeAssignmentClass": (
                                    "V",
                                    "ns=1;i=1231",
                                    {},
                                ),
                                "LocationNominalDiameterNumericalValueRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1232",
                                    {},
                                ),
                                "LocationNominalDiameterRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1233",
                                    {},
                                ),
                                "LocationNominalDiameterStandardSpecialization": (
                                    "V",
                                    "ns=1;i=1234",
                                    {},
                                ),
                                "LocationNominalDiameterTypeRepresentationAssignmentClass": (
                                    "V",
                                    "ns=1;i=1235",
                                    {},
                                ),
                                "LowerLimitHeatTracingTemperature": (
                                    "V",
                                    "ns=1;i=1236",
                                    {
                                        "EURange": ("V", "ns=1;i=1238", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1237", {}),
                                    },
                                ),
                            },
                        ),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1196", {}),
                    },
                ),
                "ProcessControlFunctionType": (
                    "OT",
                    "ns=1;i=1152",
                    {
                        "<ActuatingFunction>": ("O", "ns=1;i=2079", {}),
                        "<ProcessSignalGeneratingFunction>": ("O", "ns=1;i=2080", {}),
                        "<SignalConveyingFunction>": ("O", "ns=1;i=2081", {}),
                        "DeviceInformationAssignmentClass": ("V", "ns=1;i=1154", {}),
                        "GmpRelevanceSpecialization": ("V", "ns=1;i=1155", {}),
                        "GuaranteedSupplyFunctionSpecialization": (
                            "V",
                            "ns=1;i=1156",
                            {},
                        ),
                        "LocationSpecialization": ("V", "ns=1;i=1157", {}),
                        "PanelIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1158",
                            {},
                        ),
                        "ProcessInstrumentationFunctionCategoryAssignmentClass": (
                            "V",
                            "ns=1;i=1160",
                            {},
                        ),
                        "ProcessInstrumentationFunctionModifierAssignmentClass": (
                            "V",
                            "ns=1;i=1161",
                            {},
                        ),
                        "ProcessInstrumentationFunctionNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1153",
                            {},
                        ),
                        "ProcessInstrumentationFunctionsAssignmentClass": (
                            "V",
                            "ns=1;i=1159",
                            {},
                        ),
                        "QualityRelevanceSpecialization": ("V", "ns=1;i=1162", {}),
                        "SafetyRelevanceClassAssignmentClass": ("V", "ns=1;i=1163", {}),
                        "TypicalInformationAssignmentClass": ("V", "ns=1;i=1164", {}),
                        "VendorCompanyNameAssignmentClass": ("V", "ns=1;i=1165", {}),
                        "VotingSystemRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1166",
                            {},
                        ),
                    },
                ),
                "ProcessInstrumentationFunctionType": (
                    "OT",
                    "ns=1;i=1130",
                    {
                        "<ActuatingFunction>": ("O", "ns=1;i=2076", {}),
                        "<ProcessSignalGeneratingFunction>": ("O", "ns=1;i=2077", {}),
                        "<SignalConveyingFunction>": ("O", "ns=1;i=2078", {}),
                        "DeviceInformationAssignmentClass": ("V", "ns=1;i=1132", {}),
                        "GmpRelevanceSpecialization": ("V", "ns=1;i=1133", {}),
                        "GuaranteedSupplyFunctionSpecialization": (
                            "V",
                            "ns=1;i=1134",
                            {},
                        ),
                        "LocationSpecialization": ("V", "ns=1;i=1135", {}),
                        "PanelIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1136",
                            {},
                        ),
                        "ProcessInstrumentationFunctionCategoryAssignmentClass": (
                            "V",
                            "ns=1;i=1138",
                            {},
                        ),
                        "ProcessInstrumentationFunctionModifierAssignmentClass": (
                            "V",
                            "ns=1;i=1139",
                            {},
                        ),
                        "ProcessInstrumentationFunctionNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1131",
                            {},
                        ),
                        "ProcessInstrumentationFunctionsAssignmentClass": (
                            "V",
                            "ns=1;i=1137",
                            {},
                        ),
                        "QualityRelevanceSpecialization": ("V", "ns=1;i=1140", {}),
                        "SafetyRelevanceClassAssignmentClass": ("V", "ns=1;i=1141", {}),
                        "TypicalInformationAssignmentClass": ("V", "ns=1;i=1142", {}),
                        "VendorCompanyNameAssignmentClass": ("V", "ns=1;i=1143", {}),
                        "VotingSystemRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1144",
                            {},
                        ),
                    },
                ),
                "ProcessPlantParentStructureType": ("OT", "ns=1;i=1279", {}),
                "ProcessPlantType": (
                    "OT",
                    "ns=1;i=1300",
                    {
                        "ProcessPlantIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1301",
                            {},
                        ),
                        "ProcessPlantNameAssignmentClass": ("V", "ns=1;i=1302", {}),
                    },
                ),
                "ProcessSignalGeneratingFunctionType": (
                    "OT",
                    "ns=1;i=1210",
                    {
                        "ProcessSignalGeneratingFunctionNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1211",
                            {},
                        ),
                        "SensorTypeAssignmentClass": ("V", "ns=1;i=1212", {}),
                    },
                ),
                "ProcessSignalGeneratingSystemType": (
                    "OT",
                    "ns=1;i=1118",
                    {
                        "<PrimaryElement>": ("O", "ns=1;i=2074", {}),
                        "<Transmitter>": ("O", "ns=1;i=2075", {}),
                        "ProcessSignalGeneratingSystemNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1119",
                            {},
                        ),
                        "TypicalInformationAssignmentClass": ("V", "ns=1;i=1120", {}),
                    },
                ),
                "PropertyBreakType": (
                    "OT",
                    "ns=1;i=1938",
                    {
                        "<Node>": ("O", "ns=1;i=2119", {}),
                        "CompositionBreakSpecialization": ("V", "ns=1;i=1939", {}),
                        "InsulationBreakSpecialization": ("V", "ns=1;i=1940", {}),
                        "NominalDiameterBreakSpecialization": ("V", "ns=1;i=1941", {}),
                        "PipingClassBreakSpecialization": ("V", "ns=1;i=1942", {}),
                    },
                ),
                "PumpEquipmentType": ("OT", "ns=1;i=1502", {}),
                "RotationalSpeedType": (
                    "OT",
                    "ns=1;i=2014",
                    {
                        "Unit": ("V", "ns=1;i=2015", {}),
                        "Value": ("V", "ns=1;i=2017", {}),
                    },
                ),
                "SensingLocationType": ("OT", "ns=1;i=1117", {}),
                "ShutOffValveReferenceType": (
                    "OT",
                    "ns=1;i=1197",
                    {"SubTagNameAssignmentClass": ("V", "ns=1;i=1198", {})},
                ),
                "SignalConveyingFunctionSourceType": ("OT", "ns=1;i=1250", {}),
                "SignalConveyingFunctionTargetType": ("OT", "ns=1;i=1219", {}),
                "SignalConveyingFunctionType": (
                    "OT",
                    "ns=1;i=1251",
                    {
                        "PortStatusSpecialization": ("V", "ns=1;i=1252", {}),
                        "SignalConveyingTypeSpecialization": ("V", "ns=1;i=1253", {}),
                        "SignalPointNumberAssignmentClass": ("V", "ns=1;i=1254", {}),
                        "SignalProcessControlFunctionsAssignmentClass": (
                            "V",
                            "ns=1;i=1255",
                            {},
                        ),
                    },
                ),
                "SignalLineFunctionType": (
                    "OT",
                    "ns=1;i=1174",
                    {
                        "PortStatusSpecialization": ("V", "ns=1;i=1175", {}),
                        "SignalConveyingTypeSpecialization": ("V", "ns=1;i=1176", {}),
                        "SignalPointNumberAssignmentClass": ("V", "ns=1;i=1177", {}),
                        "SignalProcessControlFunctionsAssignmentClass": (
                            "V",
                            "ns=1;i=1178",
                            {},
                        ),
                    },
                ),
                "SilencerType": (
                    "OT",
                    "ns=1;i=1832",
                    {
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1837", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1838", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1839",
                            {
                                "EURange": ("V", "ns=1;i=1841", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1840", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1842", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1834",
                            {
                                "EURange": ("V", "ns=1;i=1836", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1835", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1843", {}),
                        "PipingComponentNameAssignmentClass": ("V", "ns=1;i=1844", {}),
                        "PipingComponentNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1833",
                            {},
                        ),
                    },
                ),
                "SiteIsa95Type": (
                    "OT",
                    "ns=1;i=1280",
                    {
                        "SiteIdentificationCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1281",
                            {},
                        ),
                        "SiteNameAssignmentClass": ("V", "ns=1;i=1282", {}),
                    },
                ),
                "SteamTrapType": (
                    "OT",
                    "ns=1;i=1812",
                    {
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1817", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1818", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1819",
                            {
                                "EURange": ("V", "ns=1;i=1821", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1820", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1822", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1814",
                            {
                                "EURange": ("V", "ns=1;i=1816", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1815", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1823", {}),
                        "PipingComponentNameAssignmentClass": ("V", "ns=1;i=1824", {}),
                        "PipingComponentNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1813",
                            {},
                        ),
                    },
                ),
                "StrainerType": (
                    "OT",
                    "ns=1;i=1757",
                    {
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1762", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1763", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1764",
                            {
                                "EURange": ("V", "ns=1;i=1766", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1765", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1767", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1759",
                            {
                                "EURange": ("V", "ns=1;i=1761", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1760", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1768", {}),
                        "PipingComponentNameAssignmentClass": ("V", "ns=1;i=1769", {}),
                        "PipingComponentNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1758",
                            {},
                        ),
                    },
                ),
                "SubTaggedColumnSectionType": (
                    "OT",
                    "ns=1;i=1399",
                    {
                        "<Internal>": ("O", "ns=1;i=2091", {}),
                        "Height": (
                            "V",
                            "ns=1;i=1401",
                            {
                                "EURange": ("V", "ns=1;i=1403", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1402", {}),
                            },
                        ),
                        "InsideDiameter": (
                            "V",
                            "ns=1;i=1404",
                            {
                                "EURange": ("V", "ns=1;i=1406", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1405", {}),
                            },
                        ),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1400", {}),
                    },
                ),
                "TaggedPlantItemType": (
                    "OT",
                    "ns=1;i=1337",
                    {
                        "TagNameAssignmentClass": ("V", "ns=1;i=1338", {}),
                        "TagNamePrefixAssignmentClass": ("V", "ns=1;i=1339", {}),
                        "TagNameSequenceNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1340",
                            {},
                        ),
                        "TagNameSuffixAssignmentClass": ("V", "ns=1;i=1341", {}),
                    },
                ),
                "TechnicalItemParentStructureType": ("OT", "ns=1;i=1295", {}),
                "TechnicalItemType": ("OT", "ns=1;i=1285", {}),
                "TemperatureType": (
                    "OT",
                    "ns=1;i=2022",
                    {
                        "Unit": ("V", "ns=1;i=2023", {}),
                        "Value": ("V", "ns=1;i=2025", {}),
                    },
                ),
                "TransmitterType": (
                    "OT",
                    "ns=1;i=1247",
                    {
                        "DeviceTypeNameAssignmentClass": ("V", "ns=1;i=1249", {}),
                        "SubTagNameAssignmentClass": ("V", "ns=1;i=1248", {}),
                    },
                ),
                "TubeBundleType": (
                    "OT",
                    "ns=1;i=1592",
                    {
                        "NumberOfTubes": ("V", "ns=1;i=1593", {}),
                        "TubeLength": (
                            "V",
                            "ns=1;i=1594",
                            {
                                "EURange": ("V", "ns=1;i=1596", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1595", {}),
                            },
                        ),
                        "TubeMaterialOfConstructionCodeAssignmentClass": (
                            "V",
                            "ns=1;i=1597",
                            {},
                        ),
                        "TubeNominalDiameterNumericalValueRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1598",
                            {},
                        ),
                        "TubeNominalDiameterRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1599",
                            {},
                        ),
                        "TubeNominalDiameterStandardSpecialization": (
                            "V",
                            "ns=1;i=1600",
                            {},
                        ),
                        "TubeNominalDiameterTypeRepresentationAssignmentClass": (
                            "V",
                            "ns=1;i=1601",
                            {},
                        ),
                    },
                ),
                "VentilationDeviceType": (
                    "OT",
                    "ns=1;i=1958",
                    {
                        "HeatTracingTypeAssignmentClass": ("V", "ns=1;i=1963", {}),
                        "HeatTracingTypeSpecialization": ("V", "ns=1;i=1964", {}),
                        "InsulationThickness": (
                            "V",
                            "ns=1;i=1965",
                            {
                                "EURange": ("V", "ns=1;i=1967", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1966", {}),
                            },
                        ),
                        "InsulationTypeAssignmentClass": ("V", "ns=1;i=1968", {}),
                        "LowerLimitHeatTracingTemperature": (
                            "V",
                            "ns=1;i=1960",
                            {
                                "EURange": ("V", "ns=1;i=1962", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1961", {}),
                            },
                        ),
                        "PipingClassCodeAssignmentClass": ("V", "ns=1;i=1969", {}),
                        "PipingComponentNameAssignmentClass": ("V", "ns=1;i=1970", {}),
                        "PipingComponentNumberAssignmentClass": (
                            "V",
                            "ns=1;i=1959",
                            {},
                        ),
                    },
                ),
                "VolumeFlowRateType": (
                    "OT",
                    "ns=1;i=2033",
                    {
                        "Unit": ("V", "ns=1;i=2034", {}),
                        "Value": ("V", "ns=1;i=2036", {}),
                    },
                ),
                "VolumeType": (
                    "OT",
                    "ns=1;i=2049",
                    {
                        "Unit": ("V", "ns=1;i=2050", {}),
                        "Value": ("V", "ns=1;i=2052", {}),
                    },
                ),
            },
        )
    },
    "reftypes": {
        "HasAssociation": ("RT", "ns=1;i=1058", {}),
        "HasDEXPIRelationship": ("RT", "ns=1;i=1059", {}),
    },
}
