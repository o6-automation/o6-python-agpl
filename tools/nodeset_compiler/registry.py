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

"""Registry of NodeSets shipped as generated modules."""

from __future__ import annotations

from collections import namedtuple

Nodeset = namedtuple("Nodeset", ["path", "shortname"])

# Registry of nodesets to emit into `o6/ns/<shortname>.py`.
# Every dependency MUST appear here (`from o6.ns import <shortname>` and `--depends` resolves to <shortname>).
# Order is cosmetic — dependency resolution is by URI via that registry, not list position.
#
# Entries below all import + inject (`server.ns.append`) cleanly, verified by `dev_docs/verify.py --all`.
# Regenerate with: python tools/nodeset_compiler/compile_all.py --keep-going
NODESETS: list[Nodeset] = [
    # ── Base + foundation ────────────────────────────────────────────────
    Nodeset(path="deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml", shortname="ns0"),
    Nodeset(path="deps/UA-Nodeset/DI/Opc.Ua.Di.NodeSet2.xml", shortname="di"),
    Nodeset(path="deps/UA-Nodeset/IA/Opc.Ua.IA.NodeSet2.xml", shortname="ia"),
    # ── Machinery ecosystem ──────────────────────────────────────────────
    Nodeset(path="deps/UA-Nodeset/Machinery/Opc.Ua.Machinery.NodeSet2.xml", shortname="machinery"),
    Nodeset(
        path="deps/UA-Nodeset/Machinery/Result/Opc.Ua.Machinery_Result.NodeSet2.xml",
        shortname="machinery_result",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Machinery/ProcessValues/Opc.Ua.Machinery.ProcessValues.NodeSet2.xml",
        shortname="machinery_processvalues",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Machinery/Energy/Opc.Ua.Machinery.Energy.NodeSet2.xml",
        shortname="machinery_energy",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Machinery/Jobs/Opc.Ua.Machinery.Jobs.Nodeset2.xml",
        shortname="machinery_jobs",
    ),
    Nodeset(
        path="deps/UA-Nodeset/MachineTool/Opc.Ua.MachineTool.NodeSet2.xml",
        shortname="machine_tool",
    ),
    Nodeset(path="deps/UA-Nodeset/GMS/opc.ua.gms.nodeset2.xml", shortname="gms"),
    Nodeset(
        path="deps/UA-Nodeset/CuttingTool/Opc.Ua.CuttingTool.NodeSet2.xml",
        shortname="cutting_tool",
    ),
    Nodeset(
        path="deps/UA-Nodeset/LaserSystems/Opc.Ua.LaserSystems.NodeSet2.xml",
        shortname="laser_systems",
    ),
    Nodeset(
        path="deps/UA-Nodeset/MetalForming/Opc.Ua.MetalForming.NodeSet2.xml",
        shortname="metal_forming",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Shotblasting/Opc.Ua.Shotblasting.NodeSet2.xml",
        shortname="shotblasting",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Woodworking/Opc.Ua.Woodworking.NodeSet2.xml",
        shortname="woodworking",
    ),
    Nodeset(path="deps/UA-Nodeset/IJT/Base/Opc.Ua.Ijt.Base.NodeSet2.xml", shortname="ijt_base"),
    Nodeset(
        path="deps/UA-Nodeset/IJT/Tightening/Opc.Ua.Ijt.Tightening.NodeSet2.xml",
        shortname="ijt_tightening",
    ),
    Nodeset(path="deps/UA-Nodeset/UAFX/opc.ua.fx.data.nodeset2.xml", shortname="fx_data"),
    Nodeset(path="deps/UA-Nodeset/UAFX/opc.ua.fx.ac.nodeset2.xml", shortname="fx_ac"),
    Nodeset(path="deps/UA-Nodeset/UAFX/opc.ua.fx.cm.nodeset2.xml", shortname="fx_cm"),
    Nodeset(
        path="deps/UA-Nodeset/Powertrain/Opc.Ua.Powertrain.NodeSet2.xml", shortname="powertrain"
    ),
    Nodeset(path="deps/UA-Nodeset/LADS/Opc.Ua.LADS.NodeSet2.xml", shortname="lads"),
    Nodeset(
        path="deps/UA-Nodeset/MachineVision/Opc.Ua.MachineVision.NodeSet2.xml",
        shortname="machine_vision",
    ),
    Nodeset(path="deps/UA-Nodeset/Robotics/Opc.Ua.Robotics.NodeSet2.xml", shortname="robotics"),
    Nodeset(path="deps/UA-Nodeset/Pumps/Opc.Ua.Pumps.NodeSet2.xml", shortname="pumps"),
    Nodeset(
        path="deps/UA-Nodeset/Weihenstephan/Opc.Ua.Weihenstephan.NodeSet2.xml",
        shortname="weihenstephan",
    ),
    Nodeset(
        path="deps/UA-Nodeset/CommercialKitchenEquipment/Opc.Ua.CommercialKitchenEquipment.NodeSet2.xml",
        shortname="commercial_kitchen",
    ),
    Nodeset(
        path="deps/UA-Nodeset/CranesHoists/Opc.Ua.CranesHoists.NodeSet2.xml",
        shortname="cranes_hoists",
    ),
    # ── Fieldbus / network ───────────────────────────────────────────────
    Nodeset(path="deps/UA-Nodeset/PNEM/Opc.Ua.PnEm.NodeSet2.xml", shortname="pnem"),
    Nodeset(path="deps/UA-Nodeset/PROFINET/Opc.Ua.Pn.NodeSet2.xml", shortname="profinet"),
    Nodeset(path="deps/UA-Nodeset/POWERLINK/Opc.Ua.POWERLINK.NodeSet2.xml", shortname="powerlink"),
    Nodeset(path="deps/UA-Nodeset/Sercos/Sercos.NodeSet2.xml", shortname="sercos"),
    Nodeset(path="deps/UA-Nodeset/IOLink/Opc.Ua.IOLink.NodeSet2.xml", shortname="io_link"),
    Nodeset(
        path="deps/UA-Nodeset/IOLink/Opc.Ua.IOLinkIODD.NodeSet2.xml",
        shortname="io_link_iodd",
    ),
    Nodeset(
        path="deps/UA-Nodeset/CSPPlusForMachine/Opc.Ua.CSPPlusForMachine.NodeSet2.xml",
        shortname="csp_plus",
    ),
    Nodeset(path="deps/UA-Nodeset/PNENC/Opc.Ua.PnEnc.Nodeset2.xml", shortname="pnenc"),
    Nodeset(path="deps/UA-Nodeset/PNDRV/Opc.Ua.PNDRV.Nodeset2.xml", shortname="pndrv"),
    Nodeset(path="deps/UA-Nodeset/PNRIO/Opc.Ua.PnRio.Nodeset2.xml", shortname="pnrio"),
    Nodeset(path="deps/UA-Nodeset/PNGSDGM/opc.ua.pngsdgm.Nodeset2.xml", shortname="pngsdgm"),
    # ── Process / industry vertical ──────────────────────────────────────
    Nodeset(path="deps/UA-Nodeset/ADI/Opc.Ua.Adi.NodeSet2.xml", shortname="adi"),
    Nodeset(path="deps/UA-Nodeset/PADIM/Opc.Ua.IRDI.NodeSet2.xml", shortname="irdi"),
    Nodeset(path="deps/UA-Nodeset/PADIM/Opc.Ua.PADIM.NodeSet2.xml", shortname="padim"),
    Nodeset(path="deps/UA-Nodeset/PAEFS/Opc.Ua.PAEFS.NodeSet2.xml", shortname="paefs"),
    Nodeset(path="deps/UA-Nodeset/FDI/Opc.Ua.Fdi5.NodeSet2.xml", shortname="fdi"),
    Nodeset(path="deps/UA-Nodeset/FDI/Opc.Ua.Fdi7.NodeSet2.xml", shortname="fdi7"),
    Nodeset(path="deps/UA-Nodeset/PackML/Opc.Ua.PackML.NodeSet2.xml", shortname="pack_ml"),
    Nodeset(path="deps/UA-Nodeset/AutoID/Opc.Ua.AutoID.NodeSet2.xml", shortname="auto_id"),
    Nodeset(path="deps/UA-Nodeset/DEXPI/Opc.Ua.DEXPI.NodeSet2.xml", shortname="dexpi"),
    Nodeset(path="deps/UA-Nodeset/ECM/Opc.Ua.ECM.NodeSet2.xml", shortname="ecm"),
    Nodeset(path="deps/UA-Nodeset/GDS/Opc.Ua.Gds.NodeSet2.xml", shortname="gds"),
    Nodeset(path="deps/UA-Nodeset/GPOS/Opc.Ua.GPOS.NodeSet2.xml", shortname="gpos"),
    Nodeset(path="deps/UA-Nodeset/IREDES/Opc.Ua.IREDES.NodeSet2.xml", shortname="iredes"),
    Nodeset(path="deps/UA-Nodeset/I4AAS/Opc.Ua.I4AAS.NodeSet2.xml", shortname="i4aas"),
    Nodeset(path="deps/UA-Nodeset/ISA-95/Opc.ISA95.NodeSet2.xml", shortname="isa95"),
    Nodeset(
        path="deps/UA-Nodeset/ISA95-JOBCONTROL/opc.ua.isa95-jobcontrol.nodeset2.xml",
        shortname="isa95_jobcontrol_v2",
    ),
    Nodeset(path="deps/UA-Nodeset/TMC/Opc.Ua.TMC.NodeSet2.xml", shortname="tmc"),
    Nodeset(path="deps/UA-Nodeset/MTConnect/Opc.Ua.MTConnect.NodeSet2.xml", shortname="mt_connect"),
    Nodeset(path="deps/UA-Nodeset/MDIS/Opc.MDIS.NodeSet2.xml", shortname="mdis"),
    Nodeset(path="deps/UA-Nodeset/CAS/Opc.Ua.CAS.NodeSet2.xml", shortname="cas"),
    Nodeset(
        path="deps/UA-Nodeset/Mining/General/1.0.0/Opc.Ua.Mining.General.NodeSet2.xml",
        shortname="mining",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/DevelopmentSupport/General/1.0.0/Opc.Ua.Mining.DevelopmentSupport.General.NodeSet2.xml",
        shortname="mining_development_support",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/DevelopmentSupport/Dozer/1.0.0/Opc.Ua.Mining.DevelopmentSupport.Dozer.NodeSet2.xml",
        shortname="mining_dozer",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/DevelopmentSupport/RoofSupportSystem/1.0.0/Opc.Ua.Mining.DevelopmentSupport.RoofSupportSystem.NodeSet2.xml",
        shortname="mining_roof_support",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/Extraction/General/1.0.0/Opc.Ua.Mining.Extraction.General.NodeSet2.xml",
        shortname="mining_extraction",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/Extraction/ShearerLoader/1.0.0/Opc.Ua.Mining.Extraction.ShearerLoader.NodeSet2.xml",
        shortname="mining_shearer_loader",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/Loading/General/1.0.0/Opc.Ua.Mining.Loading.General.NodeSet2.xml",
        shortname="mining_loading",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/Loading/HydraulicExcavator/1.0.0/Opc.Ua.Mining.Loading.HydraulicExcavator.NodeSet2.xml",
        shortname="mining_hydraulic_excavator",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/MineralProcessing/General/1.0.0/Opc.Ua.Mining.MineralProcessing.General.NodeSet2.xml",
        shortname="mining_mineral_processing",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/MineralProcessing/RockCrusher/1.0.0/Opc.Ua.Mining.MineralProcessing.RockCrusher.NodeSet2.xml",
        shortname="mining_rock_crusher",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/MonitoringSupervisionServices/General/1.0.0/Opc.Ua.Mining.MonitoringSupervisionServices.General.NodeSet2.xml",
        shortname="mining_monitoring_supervision",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/PELOServices/General/1.0.0/Opc.Ua.Mining.PELOServices.General.NodeSet2.xml",
        shortname="mining_pelo_services",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/PELOServices/FaceAlignmentSystem/1.0.0/Opc.Ua.Mining.PELOServices.FaceAlignmentSystem.NodeSet2.xml",
        shortname="mining_face_alignment",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/TransportDumping/General/1.0.0/Opc.Ua.Mining.TransportDumping.General.NodeSet2.xml",
        shortname="mining_transport_dumping",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/TransportDumping/ArmouredFaceConveyor/1.0.0/Opc.Ua.Mining.TransportDumping.ArmouredFaceConveyor.NodeSet2.xml",
        shortname="mining_armoured_face_conveyor",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Mining/TransportDumping/RearDumpTruck/1.0.0/Opc.Ua.Mining.TransportDumping.RearDumpTruck.NodeSet2.xml",
        shortname="mining_rear_dump_truck",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/GeneralTypes/1.03/Opc.Ua.PlasticsRubber.GeneralTypes.NodeSet2.xml",
        shortname="plastics_rubber",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/GeneralTypes/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.GeneralTypes.NodeSet2.xml",
        shortname="plastics_extrusion",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/GeneralTypes/1.01/Opc.Ua.PlasticsRubber.Extrusion.GeneralTypes.NodeSet2.xml",
        shortname="plastics_extrusion_v1",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Calender/1.00/Opc.Ua.PlasticsRubber.Extrusion.Calender.NodeSet2.xml",
        shortname="plastics_extrusion_v1_calender",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Calibrator/1.00/Opc.Ua.PlasticsRubber.Extrusion.Calibrator.NodeSet2.xml",
        shortname="plastics_extrusion_v1_calibrator",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Corrugator/1.00/Opc.Ua.PlasticsRubber.Extrusion.Corrugator.NodeSet2.xml",
        shortname="plastics_extrusion_v1_corrugator",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Cutter/1.00/Opc.Ua.PlasticsRubber.Extrusion.Cutter.NodeSet2.xml",
        shortname="plastics_extrusion_v1_cutter",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Die/1.00/Opc.Ua.PlasticsRubber.Extrusion.Die.NodeSet2.xml",
        shortname="plastics_extrusion_v1_die",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Extruder/1.00/Opc.Ua.PlasticsRubber.Extrusion.Extruder.NodeSet2.xml",
        shortname="plastics_extrusion_v1_extruder",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/ExtrusionLine/1.00/Opc.Ua.PlasticsRubber.Extrusion.ExtrusionLine.NodeSet2.xml",
        shortname="plastics_extrusion_v1_line",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Filter/1.00/Opc.Ua.PlasticsRubber.Extrusion.Filter.NodeSet2.xml",
        shortname="plastics_extrusion_v1_filter",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/HaulOff/1.00/Opc.Ua.PlasticsRubber.Extrusion.HaulOff.NodeSet2.xml",
        shortname="plastics_extrusion_v1_haul_off",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/MeltPump/1.00/Opc.Ua.PlasticsRubber.Extrusion.MeltPump.NodeSet2.xml",
        shortname="plastics_extrusion_v1_melt_pump",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion/Pelletizer/1.00/Opc.Ua.PlasticsRubber.Extrusion.Pelletizer.NodeSet2.xml",
        shortname="plastics_extrusion_v1_pelletizer",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Calender/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Calender.NodeSet2.xml",
        shortname="plastics_extrusion_calender",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Calibrator/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Calibrator.NodeSet2.xml",
        shortname="plastics_extrusion_calibrator",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Corrugator/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Corrugator.NodeSet2.xml",
        shortname="plastics_extrusion_corrugator",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Cutter/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Cutter.NodeSet2.xml",
        shortname="plastics_extrusion_cutter",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Die/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Die.NodeSet2.xml",
        shortname="plastics_extrusion_die",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Extruder/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Extruder.NodeSet2.xml",
        shortname="plastics_extrusion_extruder",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/ExtrusionLine/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.ExtrusionLine.NodeSet2.xml",
        shortname="plastics_extrusion_line",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Filter/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Filter.NodeSet2.xml",
        shortname="plastics_extrusion_filter",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/HaulOff/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.HaulOff.NodeSet2.xml",
        shortname="plastics_extrusion_haul_off",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/MeltPump/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.MeltPump.NodeSet2.xml",
        shortname="plastics_extrusion_melt_pump",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/Extrusion_v2/Pelletizer/2.00/Opc.Ua.PlasticsRubber.Extrusion_v2.Pelletizer.NodeSet2.xml",
        shortname="plastics_extrusion_pelletizer",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/HotRunner/1.00/Opc.Ua.PlasticsRubber.HotRunner.NodeSet2.xml",
        shortname="plastics_hot_runner",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/IMM2MES/1.01/Opc.Ua.PlasticsRubber.IMM2MES.NodeSet2.xml",
        shortname="plastics_imm2mes",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/LDS/1.02/Opc.Ua.PlasticsRubber.LDS.NodeSet2.xml",
        shortname="plastics_lds",
    ),
    Nodeset(
        path="deps/UA-Nodeset/PlasticsRubber/TCD/1.01/Opc.Ua.PlasticsRubber.TCD.NodeSet2.xml",
        shortname="plastics_tcd",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Onboarding/Opc.Ua.Onboarding.NodeSet2.xml", shortname="onboarding"
    ),
    Nodeset(path="deps/UA-Nodeset/OpenSCS/Opc.Ua.OPENSCS.NodeSet2.xml", shortname="open_scs"),
    Nodeset(path="deps/UA-Nodeset/RSL/Opc.Ua.RSL.NodeSet2.xml", shortname="rsl"),
    Nodeset(path="deps/UA-Nodeset/Safety/Opc.Ua.Safety.NodeSet2.xml", shortname="safety"),
    Nodeset(path="deps/UA-Nodeset/Scales/Opc.Ua.Scales.NodeSet2.xml", shortname="scales"),
    Nodeset(path="deps/UA-Nodeset/Scheduler/Opc.Ua.Scheduler.NodeSet2.xml", shortname="scheduler"),
    Nodeset(path="deps/UA-Nodeset/WoT/Opc.Ua.WotCon.NodeSet2.xml", shortname="wot"),
    # ── Standards / cross-domain ─────────────────────────────────────────
    Nodeset(path="deps/UA-Nodeset/AMB/Opc.Ua.AMB.NodeSet2.xml", shortname="amb"),
    Nodeset(path="deps/UA-Nodeset/BACnet/Opc.Ua.BACnet.NodeSet2.xml", shortname="bacnet"),
    Nodeset(path="deps/UA-Nodeset/XML/Opc.Ua.Xml.NodeSet2.xml", shortname="xml"),
    Nodeset(
        path="deps/UA-Nodeset/PLCopen/Opc.Ua.PLCopen.NodeSet2_V1.02.xml",
        shortname="plcopen",
    ),
    Nodeset(path="deps/UA-Nodeset/AML/Opc.Ua.AMLBaseTypes.NodeSet2.xml", shortname="aml"),
    Nodeset(path="deps/UA-Nodeset/AML/Opc.Ua.AMLLibraries.NodeSet2.xml", shortname="aml_libraries"),
    Nodeset(
        path="deps/UA-Nodeset/MachineVision/AMCM/Opc.Ua.MachineVision.AMCM.NodeSet2.xml",
        shortname="machine_vision_amcm",
    ),
    Nodeset(
        path="deps/UA-Nodeset/SurfaceTechnology/GeneralTypes/Opc.Ua.STGeneralTypes.NodeSet2.xml",
        shortname="surface_technology",
    ),
    Nodeset(
        path="deps/UA-Nodeset/SurfaceTechnology/Plasma/Opc.Ua.SurfaceTechnology.Plasma.NodeSet2.xml",
        shortname="surface_technology_plasma",
    ),
    Nodeset(
        path="deps/UA-Nodeset/WireHarness/opc.ua.wireharness.nodeset2.xml",
        shortname="wire_harness",
    ),
    Nodeset(
        path="deps/UA-Nodeset/WireHarness/opc.ua.wireharness.vec.nodeset2.xml",
        shortname="wire_harness_vec",
    ),
    Nodeset(path="deps/UA-Nodeset/WMTP/Opc.Ua.WMTP.Nodeset2.xml", shortname="wmtp"),
    Nodeset(path="deps/UA-Nodeset/TTD/opc.ua.ttd.nodeset2.xml", shortname="ttd"),
    Nodeset(
        path="deps/UA-Nodeset/AdditiveManufacturing/Opc.Ua.AdditiveManufacturing.Nodeset2.xml",
        shortname="additive_manufacturing",
    ),
    Nodeset(
        path="deps/UA-Nodeset/Glass/Flat/v2/Opc.Ua.Glass.v2.NodeSet2.xml",
        shortname="glass_flat_v2",
    ),
    Nodeset(path="deps/UA-Nodeset/Glass/Flat/Opc.Ua.Glass.NodeSet2.xml", shortname="glass_flat"),
    Nodeset(path="deps/UA-Nodeset/Woodworking/Opc.Ua.Eumabois.Nodeset2.xml", shortname="eumabois"),
]
