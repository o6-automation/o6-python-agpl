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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=aml_libraries;i=22", browseName="ns=aml_libraries;AutomationMLBaseInterface", displayName="AutomationMLBaseInterface")
class AutomationMLBaseInterface(aml.objtypes.CAEXObjectType):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=23", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=24", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=25", browseName="ns=aml_libraries;Order", displayName="Order")
class Order(AutomationMLBaseInterface):
    direction: ns0.vartypes.BaseDataVariableType
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=26", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=27", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", Order)


@o6.objecttype(nodeId="ns=aml_libraries;i=28", browseName="ns=aml_libraries;PortConnector", displayName="PortConnector")
class PortConnector(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=29", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=30", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", PortConnector)


@o6.objecttype(nodeId="ns=aml_libraries;i=31", browseName="ns=aml_libraries;InterlockingConnector", displayName="InterlockingConnector")
class InterlockingConnector(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=32", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=33", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", InterlockingConnector)


@o6.objecttype(nodeId="ns=aml_libraries;i=34", browseName="ns=aml_libraries;PPRConnector", displayName="PPRConnector")
class PPRConnector(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=35", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=36", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", PPRConnector)


@o6.objecttype(nodeId="ns=aml_libraries;i=37", browseName="ns=aml_libraries;ExternalDataConnector", displayName="ExternalDataConnector")
class ExternalDataConnector(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=38", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    refURI: ns0.vartypes.BaseDataVariableType
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=39", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", ExternalDataConnector)


@o6.objecttype(nodeId="ns=aml_libraries;i=40", browseName="ns=aml_libraries;Communication", displayName="Communication")
class Communication(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=41", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=42", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", Communication)


@o6.objecttype(nodeId="ns=aml_libraries;i=43", browseName="ns=aml_libraries;AttachmentInterface", displayName="AttachmentInterface")
class AttachmentInterface(AutomationMLBaseInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=44", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=45", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseInterface, "ns=aml;i=4002", AttachmentInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=52", browseName="ns=aml_libraries;COLLADAInterface", displayName="COLLADAInterface")
class COLLADAInterface(ExternalDataConnector):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=53", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=54", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ExternalDataConnector, "ns=aml;i=4002", COLLADAInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=55", browseName="ns=aml_libraries;PLCopenXMLInterface", displayName="PLCopenXMLInterface")
class PLCopenXMLInterface(ExternalDataConnector):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=56", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=57", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ExternalDataConnector, "ns=aml;i=4002", PLCopenXMLInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=58", browseName="ns=aml_libraries;LogicInterface", displayName="LogicInterface")
class LogicInterface(PLCopenXMLInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=59", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=60", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(PLCopenXMLInterface, "ns=aml;i=4002", LogicInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=61", browseName="ns=aml_libraries;VariableInterface", displayName="VariableInterface")
class VariableInterface(PLCopenXMLInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=62", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=63", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(PLCopenXMLInterface, "ns=aml;i=4002", VariableInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=64", browseName="ns=aml_libraries;InterlockingVariableInterface", displayName="InterlockingVariableInterface")
class InterlockingVariableInterface(VariableInterface):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=65", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    safeConditionEquals: ns0.vartypes.BaseDataVariableType
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=66", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(VariableInterface, "ns=aml;i=4002", InterlockingVariableInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=71", browseName="ns=aml_libraries;SignalInterface", displayName="SignalInterface")
class SignalInterface(Communication):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=72", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=73", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Communication, "ns=aml;i=4002", SignalInterface)


@o6.objecttype(nodeId="ns=aml_libraries;i=74", browseName="ns=aml_libraries;AutomationMLBaseRole", displayName="AutomationMLBaseRole")
class AutomationMLBaseRole(aml.objtypes.CAEXObjectType):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=75", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=76", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=77", browseName="ns=aml_libraries;Group", displayName="Group")
class Group(AutomationMLBaseRole):
    associatedFacet: ns0.vartypes.BaseDataVariableType
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=78", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=79", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Group)


@o6.objecttype(nodeId="ns=aml_libraries;i=80", browseName="ns=aml_libraries;Facet", displayName="Facet")
class Facet(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=81", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=82", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Facet)


@o6.objecttype(nodeId="ns=aml_libraries;i=83", browseName="ns=aml_libraries;Port", displayName="Port")
class Port(AutomationMLBaseRole):
    cardinality: ns0.vartypes.BaseDataVariableType
    category: ns0.vartypes.BaseDataVariableType
    connectionPoint: PortConnector
    direction: ns0.vartypes.BaseDataVariableType
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=84", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=85", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Port)


@o6.objecttype(nodeId="ns=aml_libraries;i=86", browseName="ns=aml_libraries;Resource", displayName="Resource")
class Resource(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=87", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=88", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Resource)


@o6.objecttype(nodeId="ns=aml_libraries;i=89", browseName="ns=aml_libraries;Product", displayName="Product")
class Product(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=90", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=91", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Product)


@o6.objecttype(nodeId="ns=aml_libraries;i=92", browseName="ns=aml_libraries;Process", displayName="Process")
class Process(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=93", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=94", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Process)


@o6.objecttype(nodeId="ns=aml_libraries;i=95", browseName="ns=aml_libraries;Structure", displayName="Structure")
class Structure(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=96", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=97", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Structure)


@o6.objecttype(nodeId="ns=aml_libraries;i=98", browseName="ns=aml_libraries;PropertySet", displayName="PropertySet")
class PropertySet(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=99", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=100", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", PropertySet)


@o6.objecttype(nodeId="ns=aml_libraries;i=101", browseName="ns=aml_libraries;Frame", displayName="Frame")
class Frame(AutomationMLBaseRole):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=102", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=103", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(AutomationMLBaseRole, "ns=aml;i=4002", Frame)


@o6.objecttype(nodeId="ns=aml_libraries;i=107", browseName="ns=aml_libraries;SignalGroup", displayName="SignalGroup")
class SignalGroup(Group):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=108", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=109", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Group, "ns=aml;i=4002", SignalGroup)


@o6.objecttype(nodeId="ns=aml_libraries;i=110", browseName="ns=aml_libraries;ComponentGroup", displayName="ComponentGroup")
class ComponentGroup(Group):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=111", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=112", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Group, "ns=aml;i=4002", ComponentGroup)


@o6.objecttype(nodeId="ns=aml_libraries;i=131", browseName="ns=aml_libraries;ProductStructure", displayName="ProductStructure")
class ProductStructure(Structure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=132", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=133", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Structure, "ns=aml;i=4002", ProductStructure)


@o6.objecttype(nodeId="ns=aml_libraries;i=134", browseName="ns=aml_libraries;ProcessStructure", displayName="ProcessStructure")
class ProcessStructure(Structure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=135", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=136", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Structure, "ns=aml;i=4002", ProcessStructure)


@o6.objecttype(nodeId="ns=aml_libraries;i=137", browseName="ns=aml_libraries;ResourceStructure", displayName="ResourceStructure")
class ResourceStructure(Structure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=138", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=139", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Structure, "ns=aml;i=4002", ResourceStructure)


@o6.objecttype(nodeId="ns=aml_libraries;i=140", browseName="ns=aml_libraries;BatchManufacturingEquipment", displayName="BatchManufacturingEquipment")
class BatchManufacturingEquipment(aml.objtypes.CAEXObjectType):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=141", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=142", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=143", browseName="ns=aml_libraries;ContManufacturingEquipment", displayName="ContManufacturingEquipment")
class ContManufacturingEquipment(aml.objtypes.CAEXObjectType):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=144", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=145", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=146", browseName="ns=aml_libraries;DiscManufacturingEquipment", displayName="DiscManufacturingEquipment")
class DiscManufacturingEquipment(Resource):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=147", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=148", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=149", browseName="ns=aml_libraries;Transport", displayName="Transport")
class Transport(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=150", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=151", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Transport)


@o6.objecttype(nodeId="ns=aml_libraries;i=152", browseName="ns=aml_libraries;Storage", displayName="Storage")
class Storage(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=153", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=154", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Storage)


@o6.objecttype(nodeId="ns=aml_libraries;i=155", browseName="ns=aml_libraries;Fixture", displayName="Fixture")
class Fixture(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=156", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=157", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Fixture)


@o6.objecttype(nodeId="ns=aml_libraries;i=158", browseName="ns=aml_libraries;Gate", displayName="Gate")
class Gate(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=159", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=160", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Gate)


@o6.objecttype(nodeId="ns=aml_libraries;i=161", browseName="ns=aml_libraries;Robot", displayName="Robot")
class Robot(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=162", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=163", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Robot)


@o6.objecttype(nodeId="ns=aml_libraries;i=164", browseName="ns=aml_libraries;Tool", displayName="Tool")
class Tool(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=165", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=166", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Tool)


@o6.objecttype(nodeId="ns=aml_libraries;i=167", browseName="ns=aml_libraries;Carrier", displayName="Carrier")
class Carrier(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=168", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=169", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Carrier)


@o6.objecttype(nodeId="ns=aml_libraries;i=170", browseName="ns=aml_libraries;Machine", displayName="Machine")
class Machine(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=171", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=172", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", Machine)


@o6.objecttype(nodeId="ns=aml_libraries;i=173", browseName="ns=aml_libraries;StaticObject", displayName="StaticObject")
class StaticObject(DiscManufacturingEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=174", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=175", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(DiscManufacturingEquipment, "ns=aml;i=4002", StaticObject)


@o6.objecttype(nodeId="ns=aml_libraries;i=176", browseName="ns=aml_libraries;ControlEquipment", displayName="ControlEquipment")
class ControlEquipment(Resource):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=177", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=178", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=179", browseName="ns=aml_libraries;Communication", displayName="Communication")
class Communication_2(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=180", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=181", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlEquipment, "ns=aml;i=4002", Communication_2)


@o6.objecttype(nodeId="ns=aml_libraries;i=182", browseName="ns=aml_libraries;ControlHardware", displayName="ControlHardware")
class ControlHardware(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=183", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=184", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlEquipment, "ns=aml;i=4002", ControlHardware)


@o6.objecttype(nodeId="ns=aml_libraries;i=185", browseName="ns=aml_libraries;Sensor", displayName="Sensor")
class Sensor(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=186", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=187", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlEquipment, "ns=aml;i=4002", Sensor)


@o6.objecttype(nodeId="ns=aml_libraries;i=188", browseName="ns=aml_libraries;Actuator", displayName="Actuator")
class Actuator(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=189", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=190", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlEquipment, "ns=aml;i=4002", Actuator)


@o6.objecttype(nodeId="ns=aml_libraries;i=191", browseName="ns=aml_libraries;Controller", displayName="Controller")
class Controller(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=192", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=193", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlEquipment, "ns=aml;i=4002", Controller)


@o6.objecttype(nodeId="ns=aml_libraries;i=194", browseName="ns=aml_libraries;PC", displayName="PC")
class PC(ControlHardware):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=195", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=196", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlHardware, "ns=aml;i=4002", PC)


@o6.objecttype(nodeId="ns=aml_libraries;i=197", browseName="ns=aml_libraries;IPC", displayName="IPC")
class IPC(ControlHardware):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=198", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=199", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlHardware, "ns=aml;i=4002", IPC)


@o6.objecttype(nodeId="ns=aml_libraries;i=200", browseName="ns=aml_libraries;EmbeddedDevice", displayName="EmbeddedDevice")
class EmbeddedDevice(ControlHardware):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=201", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=202", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlHardware, "ns=aml;i=4002", EmbeddedDevice)


@o6.objecttype(nodeId="ns=aml_libraries;i=203", browseName="ns=aml_libraries;Handheld", displayName="Handheld")
class Handheld(ControlHardware):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=204", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=205", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(ControlHardware, "ns=aml;i=4002", Handheld)


@o6.objecttype(nodeId="ns=aml_libraries;i=206", browseName="ns=aml_libraries;PLC", displayName="PLC")
class PLC(Controller):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=207", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=208", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Controller, "ns=aml;i=4002", PLC)


@o6.objecttype(nodeId="ns=aml_libraries;i=209", browseName="ns=aml_libraries;NC", displayName="NC")
class NC(Controller):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=210", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=211", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Controller, "ns=aml;i=4002", NC)


@o6.objecttype(nodeId="ns=aml_libraries;i=212", browseName="ns=aml_libraries;RC", displayName="RC")
class RC(Controller):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=213", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=214", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Controller, "ns=aml;i=4002", RC)


@o6.objecttype(nodeId="ns=aml_libraries;i=215", browseName="ns=aml_libraries;PAC", displayName="PAC")
class PAC(Controller):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=216", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=217", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Controller, "ns=aml;i=4002", PAC)


@o6.objecttype(nodeId="ns=aml_libraries;i=218", browseName="ns=aml_libraries;PLCFacet", displayName="PLCFacet")
class PLCFacet(Facet):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=219", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=220", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=221", browseName="ns=aml_libraries;HMIFacet", displayName="HMIFacet")
class HMIFacet(Facet):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=222", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=223", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=224", browseName="ns=aml_libraries;Enterprise", displayName="Enterprise")
class Enterprise(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=225", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=226", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=227", browseName="ns=aml_libraries;Site", displayName="Site")
class Site(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=228", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=229", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=230", browseName="ns=aml_libraries;Area", displayName="Area")
class Area(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=231", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=232", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=233", browseName="ns=aml_libraries;ProductionLine", displayName="ProductionLine")
class ProductionLine(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=234", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=235", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=236", browseName="ns=aml_libraries;WorkCell", displayName="WorkCell")
class WorkCell(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=237", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=238", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=239", browseName="ns=aml_libraries;ProcessCell", displayName="ProcessCell")
class ProcessCell(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=240", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=241", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=242", browseName="ns=aml_libraries;Unit", displayName="Unit")
class Unit(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=243", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=244", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=245", browseName="ns=aml_libraries;ProductionUnit", displayName="ProductionUnit")
class ProductionUnit(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=246", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=247", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=248", browseName="ns=aml_libraries;StorageZone", displayName="StorageZone")
class StorageZone(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=249", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=250", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=251", browseName="ns=aml_libraries;StorageUnit", displayName="StorageUnit")
class StorageUnit(ResourceStructure):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=252", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=253", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=254", browseName="ns=aml_libraries;Turntable", displayName="Turntable")
class Turntable(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=255", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=256", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=257", browseName="ns=aml_libraries;Conveyor", displayName="Conveyor")
class Conveyor(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=258", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=259", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=260", browseName="ns=aml_libraries;LiftingTable", displayName="LiftingTable")
class LiftingTable(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=261", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=262", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=263", browseName="ns=aml_libraries;AGV", displayName="AGV")
class AGV(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=264", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=265", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=266", browseName="ns=aml_libraries;Transposer", displayName="Transposer")
class Transposer(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=267", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=268", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=269", browseName="ns=aml_libraries;CarrierHandlingSystem", displayName="CarrierHandlingSystem")
class CarrierHandlingSystem(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=270", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=271", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=272", browseName="ns=aml_libraries;BodyStore", displayName="BodyStore")
class BodyStore(Storage):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=273", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=274", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=275", browseName="ns=aml_libraries;Lift", displayName="Lift")
class Lift(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=276", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=277", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=278", browseName="ns=aml_libraries;Rollerbed", displayName="Rollerbed")
class Rollerbed(Transport):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=279", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=280", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=281", browseName="ns=aml_libraries;StationaryTool", displayName="StationaryTool")
class StationaryTool(Tool):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=282", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=283", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=284", browseName="ns=aml_libraries;MovableTool", displayName="MovableTool")
class MovableTool(Tool):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=285", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=286", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=287", browseName="ns=aml_libraries;ControlCabinet", displayName="ControlCabinet")
class ControlCabinet(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=288", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=289", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=290", browseName="ns=aml_libraries;IODevice", displayName="IODevice")
class IODevice(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=291", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=292", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=293", browseName="ns=aml_libraries;HMI", displayName="HMI")
class HMI(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=294", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=295", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=296", browseName="ns=aml_libraries;ActuatingDrive", displayName="ActuatingDrive")
class ActuatingDrive(Actuator):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=297", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=298", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=299", browseName="ns=aml_libraries;MotionController", displayName="MotionController")
class MotionController(ControlEquipment):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=300", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=301", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=302", browseName="ns=aml_libraries;Panel", displayName="Panel")
class Panel(ControlHardware):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=303", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=304", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=305", browseName="ns=aml_libraries;MeasuringEquipment", displayName="MeasuringEquipment")
class MeasuringEquipment(Resource):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=306", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=307", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=308", browseName="ns=aml_libraries;Clamp", displayName="Clamp")
class Clamp(Fixture):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=309", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=310", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=311", browseName="ns=aml_libraries;ProcessController", displayName="ProcessController")
class ProcessController(Controller):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=312", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=313", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=314", browseName="ns=aml_libraries;Loader", displayName="Loader")
class Loader(Storage):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=315", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=316", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=317", browseName="ns=aml_libraries;Unloader", displayName="Unloader")
class Unloader(Storage):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=318", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=319", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


@o6.objecttype(nodeId="ns=aml_libraries;i=320", browseName="ns=aml_libraries;BeltConveyor", displayName="BeltConveyor")
class BeltConveyor(Conveyor):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=321", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=322", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Conveyor, "ns=aml;i=4002", BeltConveyor)


@o6.objecttype(nodeId="ns=aml_libraries;i=323", browseName="ns=aml_libraries;RollConveyor", displayName="RollConveyor")
class RollConveyor(Conveyor):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=324", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=325", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Conveyor, "ns=aml;i=4002", RollConveyor)


@o6.objecttype(nodeId="ns=aml_libraries;i=326", browseName="ns=aml_libraries;ChainConveyor", displayName="ChainConveyor")
class ChainConveyor(Conveyor):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=327", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=328", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Conveyor, "ns=aml;i=4002", ChainConveyor)


@o6.objecttype(nodeId="ns=aml_libraries;i=329", browseName="ns=aml_libraries;PalletConveyor", displayName="PalletConveyor")
class PalletConveyor(Conveyor):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=330", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=331", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Conveyor, "ns=aml;i=4002", PalletConveyor)


@o6.objecttype(nodeId="ns=aml_libraries;i=332", browseName="ns=aml_libraries;OverheadConveyor", displayName="OverheadConveyor")
class OverheadConveyor(Conveyor):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=333", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=334", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(Conveyor, "ns=aml;i=4002", OverheadConveyor)


@o6.objecttype(nodeId="ns=aml_libraries;i=335", browseName="ns=aml_libraries;WarningEquipment", displayName="WarningEquipment")
class WarningEquipment(HMI):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=336", browseName="ID", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=aml_libraries;i=337", browseName="Version", value=[ns0.datatypes.Argument(name="", dataType=o6.String, valueRank=-1)])
    )


o6.reference(HMI, "ns=aml;i=4002", WarningEquipment)


del Any, TYPE_CHECKING, uuid, o6, aml, ns0
