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

"""Generated OPC UA aml_libraries namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.aml as aml
import o6.ns.ns0 as ns0
from . import objtypes as aml_libraries_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

automationMLInterfaceClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=1",
    browseName="AutomationMLInterfaceClassLib",
    description="Standard Automation Markup Language Interface Class Library - Part 1 Content extended with Part 3 and Part 4 Content",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=2", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=3", browseName="Version", value=[ns0.datatypes.Argument(name="2.2.2", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5008",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLInterfaceClassLib, "ns=aml;i=4002", aml_libraries_objtypes.AutomationMLBaseInterface)
automationMLBaseRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=4",
    browseName="AutomationMLBaseRoleClassLib",
    description="Automation Markup Language Base Role Class Library - Part 1 Content extended with Part 3 and Part 4 Content",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=5", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=6", browseName="Version", value=[ns0.datatypes.Argument(name="2.2.2", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLBaseRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.AutomationMLBaseRole)
automationMLBMIRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=7",
    browseName="AutomationMLBMIRoleClassLib",
    description="Automation Markup Language Batch Manufacturing Industry Role Class Library",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=8", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=9", browseName="Version", value=[ns0.datatypes.Argument(name="1.1.0", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLBMIRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.BatchManufacturingEquipment)
automationMLCMIRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=10",
    browseName="AutomationMLCMIRoleClassLib",
    description="Automation Markup Language Continuous Manufacturing Industry Role Class Library",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=11", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=12", browseName="Version", value=[ns0.datatypes.Argument(name="1.1.0", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLCMIRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ContManufacturingEquipment)
automationMLDMIRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=13",
    browseName="AutomationMLDMIRoleClassLib",
    description="Automation Markup Language  Discrete Manufacturing Industry Role Class Library",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=14", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=15", browseName="Version", value=[ns0.datatypes.Argument(name="2.4.0", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLDMIRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.DiscManufacturingEquipment)
automationMLCSRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=16",
    browseName="AutomationMLCSRoleClassLib",
    description="Automation Markup Language Control Industry Role Class Library",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=17", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=18", browseName="Version", value=[ns0.datatypes.Argument(name="2.3.0", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLCSRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ControlEquipment)
automationMLExtendedRoleClassLib = ns0.objtypes.FolderType(
    nodeId="ns=aml_libraries;i=19",
    browseName="AutomationMLExtendedRoleClassLib",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=20", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=21", browseName="Version", value=[ns0.datatypes.Argument(name="2.7.0", dataType=o6.String, valueRank=-1)])
        ),
    ],
    parent="ns=aml;i=5009",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.PLCFacet)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.HMIFacet)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Enterprise)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Site)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Area)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ProductionLine)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.WorkCell)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ProcessCell)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Unit)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ProductionUnit)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.StorageZone)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.StorageUnit)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Turntable)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Conveyor)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.LiftingTable)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.AGV)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Transposer)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.CarrierHandlingSystem)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.BodyStore)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Lift)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Rollerbed)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.StationaryTool)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.MovableTool)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ControlCabinet)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.IODevice)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.HMI)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ActuatingDrive)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.MotionController)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Panel)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.MeasuringEquipment)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Clamp)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.ProcessController)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Loader)
o6.reference(automationMLExtendedRoleClassLib, "ns=aml;i=4002", aml_libraries_objtypes.Unloader)
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=46",
    browseName="Direction",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=47", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=48", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.Order, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=46"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=49",
    browseName="refURI",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=50", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=51", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.ExternalDataConnector, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=49"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=67",
    browseName="SafeConditionEquals",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=68", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=69", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=70", browseName="DefaultValue", value=[ns0.datatypes.Argument(name="true", dataType=o6.String, valueRank=-1)])
        ),
    ],
    dataType=o6.Boolean,
)
o6.reference(aml_libraries_objtypes.InterlockingVariableInterface, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=67"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=104",
    browseName="AssociatedFacet",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=105", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=106", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.Group, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=104"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=113",
    browseName="Direction",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=114", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=115", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.Port, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=113"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=119",
    browseName="Category",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=120", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=121", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.Port, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=119"])
aml_libraries_objtypes.PortConnector(
    nodeId="ns=aml_libraries;i=122",
    browseName="ConnectionPoint",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=aml_libraries;i=123", browseName="ID", value=[ns0.datatypes.Argument(name="9942bd9c-c19d-44e4-a197-11b9edf264e7", dataType=o6.String, valueRank=-1)]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=124", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
)
o6.reference(aml_libraries_objtypes.Port, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=122"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=125",
    browseName="MinOccur",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=126", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=127", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.UInt32,
)
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=128",
    browseName="MaxOccur",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=129", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=130", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
    ],
    dataType=o6.UInt32,
)
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=aml_libraries;i=116",
    browseName="Cardinality",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=117", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=118", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasComponent(o6.ns["ns=aml_libraries;i=125"]),
        o6.hasComponent(o6.ns["ns=aml_libraries;i=128"]),
    ],
    dataType=o6.String,
)
o6.reference(aml_libraries_objtypes.Port, ns0.reftypes.HasComponent, o6.ns["ns=aml_libraries;i=116"])
ns0.objtypes.FolderType(nodeId="ns=aml_libraries;i=344", browseName="RoleClassLibs")
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLBaseRoleClassLib)
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLBMIRoleClassLib)
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLCMIRoleClassLib)
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLDMIRoleClassLib)
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLCSRoleClassLib)
o6.reference(o6.ns["ns=aml_libraries;i=344"], "i=47", automationMLExtendedRoleClassLib)
ns0.objtypes.FolderType(nodeId="ns=aml_libraries;i=345", browseName="InterfaceClassLibs")
o6.reference(o6.ns["ns=aml_libraries;i=345"], "i=47", automationMLInterfaceClassLib)
automationMLLibsDotAml = aml.objtypes.CAEXFileType(
    nodeId="ns=aml_libraries;i=338",
    browseName="AutomationMLLibs.aml",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=339", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=aml_libraries;i=340", browseName="FileName", value=[ns0.datatypes.Argument(name="AutomationMLLibs.aml", dataType=o6.String, valueRank=-1)]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=aml_libraries;i=341", browseName="CAEXSchemaVersion", value=[ns0.datatypes.Argument(name="2.15", dataType=o6.String, valueRank=-1)]
            )
        ),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml_libraries;i=342", browseName="InstanceHierarchies")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml_libraries;i=343", browseName="SystemUnitClassLibs")),
        o6.hasComponent(o6.ns["ns=aml_libraries;i=344"]),
        o6.hasComponent(o6.ns["ns=aml_libraries;i=345"]),
    ],
    parent="ns=aml;i=5006",
    referenceType=ns0.reftypes.Organizes,
)


del Any, TYPE_CHECKING, uuid, o6, aml, ns0, aml_libraries_objtypes
