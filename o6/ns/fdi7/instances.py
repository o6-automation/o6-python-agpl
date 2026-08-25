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

"""Generated OPC UA fdi7 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as fdi7_datypes
from . import objtypes as fdi7_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=76",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=75",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=75", browseName="ns=fdi7;Initialize", outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=76"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=78",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=77",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=77", browseName="ns=fdi7;Reset", outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=78"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=80",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=79",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ModuleTypeName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="InstanceName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="InstanceLabel", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=81",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=79",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InstanceNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=79", browseName="ns=fdi7;AddComponent", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=80"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=81"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=83",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=82",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ModuleNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=84",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=82",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=82", browseName="ns=fdi7;RemoveComponent", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=83"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=84"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=14",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=75"]), o6.hasComponent(o6.ns["ns=fdi7;i=77"]), o6.hasComponent(o6.ns["ns=fdi7;i=79"]), o6.hasComponent(o6.ns["ns=fdi7;i=82"])],
)
o6.reference(fdi7_objtypes.CommunicationServerType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=14"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=158",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=157",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="TopologyScanResult", dataType=o6.XmlElement, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=157", browseName="ns=fdi7;Scan", outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=158"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=160",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=159",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=159", browseName="ns=fdi7;ResetScan", outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=160"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=165",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=164",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ModuleTypeName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="InstanceName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="InstanceLabel", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=166",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=164",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InstanceNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=164", browseName="ns=fdi7;AddComponent", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=165"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=166"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=168",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=167",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ModuleNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=169",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=167",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=167", browseName="ns=fdi7;RemoveComponent", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=168"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=169"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=96",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=157"]), o6.hasComponent(o6.ns["ns=fdi7;i=159"]), o6.hasComponent(o6.ns["ns=fdi7;i=164"]), o6.hasComponent(o6.ns["ns=fdi7;i=167"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=96"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=301",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=300",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=302",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=300",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=300", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=301"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=302"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=236", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=fdi7;i=300"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=236"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=310",
    browseName="InputArguments",
    parent="ns=fdi7;i=309",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="LinkId", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="OldAddress", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="NewAddress", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="NewPDTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=311",
    browseName="OutputArguments",
    parent="ns=fdi7;i=309",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
setAddressMethodFFH1Type = o6.call(
    nodeId="ns=fdi7;i=309", browseName="ns=fdi7;SetAddressMethodFFH1Type", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=310"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=311"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=313",
    browseName="InputArguments",
    parent="ns=fdi7;i=312",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NewPDTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=314",
    browseName="OutputArguments",
    parent="ns=fdi7;i=312",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
setAddressMethodFFHSEType = o6.call(
    nodeId="ns=fdi7;i=312", browseName="ns=fdi7;SetAddressMethodFFHSEType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=313"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=314"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=316",
    browseName="InputArguments",
    parent="ns=fdi7;i=315",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldAddress", dataType=o6.Byte, valueRank=-1), ns0.datatypes.Argument(name="NewAddress", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=317",
    browseName="OutputArguments",
    parent="ns=fdi7;i=315",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
setAddressMethodPROFIBUSType = o6.call(
    nodeId="ns=fdi7;i=315", browseName="ns=fdi7;SetAddressMethodPROFIBUSType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=316"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=317"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=319",
    browseName="InputArguments",
    parent="ns=fdi7;i=318",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MAC", dataType=o6.Byte, valueRank=1, arrayDimensions=[6]),
        ns0.datatypes.Argument(name="IP", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
        ns0.datatypes.Argument(name="DNSNAME", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SubnetMask", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
        ns0.datatypes.Argument(name="Gateway", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=320",
    browseName="OutputArguments",
    parent="ns=fdi7;i=318",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
setAddressMethodPROFINETType = o6.call(
    nodeId="ns=fdi7;i=318", browseName="ns=fdi7;SetAddressMethodPROFINETType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=319"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=320"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=322",
    browseName="InputArguments",
    parent="ns=fdi7;i=321",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldPollAddress", dataType=o6.Byte, valueRank=-1), ns0.datatypes.Argument(name="NewPollAddress", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=323",
    browseName="OutputArguments",
    parent="ns=fdi7;i=321",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
setAddressMethodHARTType = o6.call(
    nodeId="ns=fdi7;i=321", browseName="ns=fdi7;SetAddressMethodHARTType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=322"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=323"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=399",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="LinkId", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="OldAddress", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="NewAddress", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="NewPDTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=400",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=398", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=399"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=400"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=327", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=398"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationFFH1DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=327"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=441",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=440",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=442",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=440",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=440", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=441"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=442"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=444",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=443",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LinkId", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="SIFConnection", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=445",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=443",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=443", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=444"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=445"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=447",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=446",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=448",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=446",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=446", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=447"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=448"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=404",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=440"]), o6.hasComponent(o6.ns["ns=fdi7;i=443"]), o6.hasComponent(o6.ns["ns=fdi7;i=446"])],
)
fdi7_objtypes.ServerCommunicationFFH1ServiceType(
    nodeId="ns=fdi7;i=401",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=422",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=423",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=424", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=425", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=426",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=427", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=428", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=429", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=404"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationFFH1DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=401"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=527",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=526",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NewPDTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=528",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=526",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=526", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=527"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=528"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=455", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=526"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationFFHSEDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=455"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=569",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=568",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=570",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=568",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=568", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=569"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=570"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=572",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=571",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=573",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=571",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=571", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=572"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=573"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=575",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=574",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=576",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=574",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=574", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=575"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=576"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=532",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=568"]), o6.hasComponent(o6.ns["ns=fdi7;i=571"]), o6.hasComponent(o6.ns["ns=fdi7;i=574"])],
)
fdi7_objtypes.ServerCommunicationFFHSEServiceType(
    nodeId="ns=fdi7;i=529",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=550",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=551",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=552", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=553", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=554",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=555", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=556", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=557", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=532"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationFFHSEDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=529"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=655",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=654",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldAddress", dataType=o6.Byte, valueRank=-1), ns0.datatypes.Argument(name="NewAddress", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=656",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=654",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=654", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=655"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=656"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=583", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=654"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFIBUSDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=583"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=697",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=696",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=698",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=696",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=696", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=697"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=698"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=700",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=699",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="ManufacturerId", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=701",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=699",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=699", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=700"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=701"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=703",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=702",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=704",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=702",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=702", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=703"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=704"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=660",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=696"]), o6.hasComponent(o6.ns["ns=fdi7;i=699"]), o6.hasComponent(o6.ns["ns=fdi7;i=702"])],
)
fdi7_objtypes.ServerCommunicationPROFIBUSServiceType(
    nodeId="ns=fdi7;i=657",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=678",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=679",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=680", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=681", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=682",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=683", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=684", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=685", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=660"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFIBUSDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=657"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=780",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=779",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MAC", dataType=o6.Byte, valueRank=1, arrayDimensions=[6]),
        ns0.datatypes.Argument(name="IP", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
        ns0.datatypes.Argument(name="DNSNAME", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SubnetMask", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
        ns0.datatypes.Argument(name="Gateway", dataType=o6.Byte, valueRank=1, arrayDimensions=[4]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=781",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=779",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=779", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=780"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=781"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=708", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=779"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFINETDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=708"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=822",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=821",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=823",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=821",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=821", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=822"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=823"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=825",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=824",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="DNSNAME", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="VendorID", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=826",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=824",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=824", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=825"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=826"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=828",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=827",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUBSLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="API", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=829",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=827",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=827", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=828"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=829"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=785",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=821"]), o6.hasComponent(o6.ns["ns=fdi7;i=824"]), o6.hasComponent(o6.ns["ns=fdi7;i=827"])],
)
fdi7_objtypes.ServerCommunicationPROFINETServiceType(
    nodeId="ns=fdi7;i=782",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=803",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=804",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=805", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=806", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=807",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=808", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=809", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=810", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=785"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFINETDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=782"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=905",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=904",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldPollAddress", dataType=o6.Byte, valueRank=-1), ns0.datatypes.Argument(name="NewPollAddress", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=906",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=904",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=904", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=905"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=906"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=833", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=904"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationHARType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=833"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=947",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=946",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=948",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=946",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=946", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=947"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=948"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=950",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=949",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LongAddress", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=951",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=949",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=949", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=950"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=951"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=953",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=952",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Command", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Request", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=954",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=952",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Reply", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=952", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=953"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=954"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=910",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=946"]), o6.hasComponent(o6.ns["ns=fdi7;i=949"]), o6.hasComponent(o6.ns["ns=fdi7;i=952"])],
)
fdi7_objtypes.ServerCommunicationHARTServiceType(
    nodeId="ns=fdi7;i=907",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=928",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=929",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=930", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=931", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=932",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=933", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=934", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=935", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=910"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationHARType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=907"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=959",
    browseName="InputArguments",
    parent="ns=fdi7;i=958",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LinkId", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="SIFConnection", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=960",
    browseName="OutputArguments",
    parent="ns=fdi7;i=958",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
connectMethodFFH1Type = o6.call(
    nodeId="ns=fdi7;i=958", browseName="ns=fdi7;ConnectMethodFFH1Type", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=959"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=960"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=962",
    browseName="InputArguments",
    parent="ns=fdi7;i=961",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=963",
    browseName="OutputArguments",
    parent="ns=fdi7;i=961",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
connectMethodFFHSEType = o6.call(
    nodeId="ns=fdi7;i=961", browseName="ns=fdi7;ConnectMethodFFHSEType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=962"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=963"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=965",
    browseName="InputArguments",
    parent="ns=fdi7;i=964",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="ManufacturerId", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=966",
    browseName="OutputArguments",
    parent="ns=fdi7;i=964",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
connectMethodPROFIBUSType = o6.call(
    nodeId="ns=fdi7;i=964", browseName="ns=fdi7;ConnectMethodPROFIBUSType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=965"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=966"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=968",
    browseName="InputArguments",
    parent="ns=fdi7;i=967",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="DNSNAME", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="VendorID", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=969",
    browseName="OutputArguments",
    parent="ns=fdi7;i=967",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
connectMethodPROFINETType = o6.call(
    nodeId="ns=fdi7;i=967", browseName="ns=fdi7;ConnectMethodPROFINETType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=968"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=969"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=971",
    browseName="InputArguments",
    parent="ns=fdi7;i=970",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LongAddress", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=972",
    browseName="OutputArguments",
    parent="ns=fdi7;i=970",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
connectMethodHARTType = o6.call(
    nodeId="ns=fdi7;i=970", browseName="ns=fdi7;ConnectMethodHARTType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=971"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=972"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=974",
    browseName="InputArguments",
    parent="ns=fdi7;i=973",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=975",
    browseName="OutputArguments",
    parent="ns=fdi7;i=973",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodFFH1Type = o6.call(
    nodeId="ns=fdi7;i=973", browseName="ns=fdi7;TransferMethodFFH1Type", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=974"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=975"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=977",
    browseName="InputArguments",
    parent="ns=fdi7;i=976",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=978",
    browseName="OutputArguments",
    parent="ns=fdi7;i=976",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodFFHSEType = o6.call(
    nodeId="ns=fdi7;i=976", browseName="ns=fdi7;TransferMethodFFHSEType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=977"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=978"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=980",
    browseName="InputArguments",
    parent="ns=fdi7;i=979",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=981",
    browseName="OutputArguments",
    parent="ns=fdi7;i=979",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodPROFIBUSType = o6.call(
    nodeId="ns=fdi7;i=979", browseName="ns=fdi7;TransferMethodPROFIBUSType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=980"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=981"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=983",
    browseName="InputArguments",
    parent="ns=fdi7;i=982",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUBSLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="API", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=984",
    browseName="OutputArguments",
    parent="ns=fdi7;i=982",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodPROFINETType = o6.call(
    nodeId="ns=fdi7;i=982", browseName="ns=fdi7;TransferMethodPROFINETType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=983"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=984"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=986",
    browseName="InputArguments",
    parent="ns=fdi7;i=985",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Command", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Request", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=987",
    browseName="OutputArguments",
    parent="ns=fdi7;i=985",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Reply", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
transferMethodHARTType = o6.call(
    nodeId="ns=fdi7;i=985", browseName="ns=fdi7;TransferMethodHARTType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=986"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=987"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=989",
    browseName="InputArguments",
    parent="ns=fdi7;i=988",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=990",
    browseName="OutputArguments",
    parent="ns=fdi7;i=988",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
getPublishedDataMethodFFH1Type = o6.call(
    nodeId="ns=fdi7;i=988", browseName="ns=fdi7;GetPublishedDataMethodFFH1Type", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=989"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=990"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=992",
    browseName="InputArguments",
    parent="ns=fdi7;i=991",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=993",
    browseName="OutputArguments",
    parent="ns=fdi7;i=991",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
getPublishedDataMethodFFHSEType = o6.call(
    nodeId="ns=fdi7;i=991",
    browseName="ns=fdi7;GetPublishedDataMethodFFHSEType",
    inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=992"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=993"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=995",
    browseName="InputArguments",
    parent="ns=fdi7;i=994",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=996",
    browseName="OutputArguments",
    parent="ns=fdi7;i=994",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="Command", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Reply", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
getPublishedDataMethodHARTType = o6.call(
    nodeId="ns=fdi7;i=994", browseName="ns=fdi7;GetPublishedDataMethodHARTType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=995"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=996"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1065",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LinkId", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="SIFConnection", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1066",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1064", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1065"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1066"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1068",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1069",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1067", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1068"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1069"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1071",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1072",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1070", browseName="ns=fdi7;GetPublishedData", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1071"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1072"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1000",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1064"]), o6.hasComponent(o6.ns["ns=fdi7;i=1067"]), o6.hasComponent(o6.ns["ns=fdi7;i=1070"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationFFH1ServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1000"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1141",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1140",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OrdinalNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1142",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1140",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1140", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1141"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1142"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1144",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1143",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1145",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1143",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1143", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1144"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1145"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1147",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1148",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="BlockTag", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="DelayForNextCall", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1146", browseName="ns=fdi7;GetPublishedData", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1147"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1148"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1076",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1140"]), o6.hasComponent(o6.ns["ns=fdi7;i=1143"]), o6.hasComponent(o6.ns["ns=fdi7;i=1146"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationFFHSEServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1076"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1217",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1216",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="ManufacturerId", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1218",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1216",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1216", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1217"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1218"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1220",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1219",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1221",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1219",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1219", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1220"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1221"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1152",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1216"]), o6.hasComponent(o6.ns["ns=fdi7;i=1219"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFIBUSServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1152"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1290",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1289",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="DNSNAME", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="VendorID", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1291",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1289",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1289", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1290"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1291"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1293",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1292",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUBSLOT", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="INDEX", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="API", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="REQUEST", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1294",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1292",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="REPLY", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1292", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1293"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1294"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1225",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1289"]), o6.hasComponent(o6.ns["ns=fdi7;i=1292"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationPROFINETServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1225"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1363",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1362",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="LongAddress", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1364",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1362",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1362", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1363"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1364"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1366",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1365",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Command", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Request", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1367",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1365",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Reply", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1365", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1366"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1367"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1369",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1368",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1370",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1368",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="Command", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Reply", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1368", browseName="ns=fdi7;GetPublishedData", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1369"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1370"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1298",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1362"]), o6.hasComponent(o6.ns["ns=fdi7;i=1365"]), o6.hasComponent(o6.ns["ns=fdi7;i=1368"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationHARTServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1298"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1786",
    browseName="InputArguments",
    parent="ns=fdi7;i=1785",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldAddress", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="NewAddress", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1787",
    browseName="OutputArguments",
    parent="ns=fdi7;i=1785",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
setAddressMethodGENERICType = o6.call(
    nodeId="ns=fdi7;i=1785", browseName="ns=fdi7;SetAddressMethodGENERICType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1786"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1787"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1902",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1901",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1903",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1901",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1901", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1902"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1903"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1905",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1904",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IPAddress", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ConnectType", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1906",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1904",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1904", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1905"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1906"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1908",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1907",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AppID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="ObjectID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="AttrOrMethID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="RequestId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1909",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1907",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=1907", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1908"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1909"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1865",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=1901"]), o6.hasComponent(o6.ns["ns=fdi7;i=1904"]), o6.hasComponent(o6.ns["ns=fdi7;i=1907"])],
)
fdi7_objtypes.ServerCommunicationISA100_WirelessServiceType(
    nodeId="ns=fdi7;i=1862",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=1883",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=1884",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=1885", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1886", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=1887",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1888", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=1889", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1890", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=1865"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationISA100_WirelessDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1862"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1989",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1988",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="OldAddress", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="NewAddress", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=1990",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=1988",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=1988", browseName="ns=fdi7;SetAddress", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1989"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=1990"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1916", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdi7;i=1988"])]
)
o6.reference(fdi7_objtypes.ServerCommunicationGENERICDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1916"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2031",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2032",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=2030", browseName="ns=fdi7;Disconnect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2031"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2032"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2034",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2035",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=2033", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2034"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2035"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Header", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RequestData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RequestDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ResponseDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2038",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResponseData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=2036", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2037"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2038"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=1994",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=2030"]), o6.hasComponent(o6.ns["ns=fdi7;i=2033"]), o6.hasComponent(o6.ns["ns=fdi7;i=2036"])],
)
fdi7_objtypes.ServerCommunicationGENERICServiceType(
    nodeId="ns=fdi7;i=1991",
    browseName="ns=fdi7;ServiceProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=2012",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=2013",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=2014", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=2015", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=2016",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=2017", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=2018", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=2019", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=1994"]),
    ],
)
o6.reference(fdi7_objtypes.ServerCommunicationGENERICDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=1991"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2040",
    browseName="InputArguments",
    parent="ns=fdi7;i=2039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IPAddress", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ConnectType", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2041",
    browseName="OutputArguments",
    parent="ns=fdi7;i=2039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
connectMethodISA100_WirelessType = o6.call(
    nodeId="ns=fdi7;i=2039",
    browseName="ns=fdi7;ConnectMethodISA100_WirelessType",
    inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2040"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2041"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2043",
    browseName="InputArguments",
    parent="ns=fdi7;i=2042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2044",
    browseName="OutputArguments",
    parent="ns=fdi7;i=2042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
connectMethodGENERICType = o6.call(
    nodeId="ns=fdi7;i=2042", browseName="ns=fdi7;ConnectMethodGENERICType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2043"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2044"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2046",
    browseName="InputArguments",
    parent="ns=fdi7;i=2045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AppID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="ObjectID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="AttrOrMethID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="RequestId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2047",
    browseName="OutputArguments",
    parent="ns=fdi7;i=2045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodISA100_WirelessType = o6.call(
    nodeId="ns=fdi7;i=2045",
    browseName="ns=fdi7;TransferMethodISA100_WirelessType",
    inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2046"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2047"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2049",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[19],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("BOOLEAN", "\n                ")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DOUBLE", "\n                ")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("FLOAT", "\n                ")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("INTEGER", "\n                ")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("UNSIGNED_INTEGER", "\n                ")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("DATE", "\n                ")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("DATE_AND_TIME", "\n                ")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("DURATION", "\n                ")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("TIME", "\n                ")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("TIME_VALUE", "\n                ")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("BIT_ENUMERATED", "\n                ")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ENUMERATED", "\n                ")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ASCII", "\n                ")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("BITSTRING", "\n                ")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("EUC", "\n                ")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("OCTET", "\n                ")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("PACKED_ASCII", "\n                ")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("PASSWORD", "\n                ")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("VISIBLE", "\n                ")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2052",
    browseName="InputArguments",
    parent="ns=fdi7;i=2051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Header", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RequestData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RequestDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ResponseDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2053",
    browseName="OutputArguments",
    parent="ns=fdi7;i=2051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResponseData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
transferMethodGENERICType = o6.call(
    nodeId="ns=fdi7;i=2051", browseName="ns=fdi7;TransferMethodGENERICType", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2052"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2053"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2055",
    browseName="InputArguments",
    parent="ns=fdi7;i=2054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2056",
    browseName="OutputArguments",
    parent="ns=fdi7;i=2054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="AppID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="ObjectID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
getPublishedDataMethodISA100_WirelessType = o6.call(
    nodeId="ns=fdi7;i=2054",
    browseName="ns=fdi7;GetPublishedDataMethodISA100_WirelessType",
    inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2055"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2056"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2125",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IPAddress", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ConnectType", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2126",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=2124", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2125"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2126"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2128",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2127",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="OPERATION", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AppID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="ObjectID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="AttrOrMethID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SUB_INDEX", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="WriteData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="RequestId", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2129",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2127",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ReadData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=2127", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2128"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2129"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2131",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2132",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="AppID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="ObjectID", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="AlarmEventData", dataType=o6.Byte, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="AlarmEventType", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="TimeStamp", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=2130", browseName="ns=fdi7;GetPublishedData", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2131"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2132"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=2060",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=2124"]), o6.hasComponent(o6.ns["ns=fdi7;i=2127"]), o6.hasComponent(o6.ns["ns=fdi7;i=2130"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationISA100_WirelessServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=2060"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2201",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Address", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2202",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1)],
)
o6.call(nodeId="ns=fdi7;i=2200", browseName="ns=fdi7;Connect", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2201"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2202"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2204",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommunicationRelationId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Header", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RequestData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RequestDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ResponseDataTypes", dataType=o6.NodeId("ns=fdi7;i=2050"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi7;i=2205",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi7;i=2203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResponseData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="RESPONSE_CODES", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceError", dataType=ns0.datatypes.Integer, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fdi7;i=2203", browseName="ns=fdi7;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2204"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi7;i=2205"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=fdi7;i=2136",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=fdi7;i=2200"]), o6.hasComponent(o6.ns["ns=fdi7;i=2203"])],
)
o6.reference(fdi7_objtypes.ServerCommunicationGENERICServiceType, ns0.reftypes.HasComponent, o6.ns["ns=fdi7;i=2136"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi7;i=2206", browseName="Default XML")
o6.hasEncoding(fdi7_datypes.EddDataTypeInfo, o6.ns["ns=fdi7;i=2206"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi7;i=2210", browseName="ns=fdi7;EddDataTypeInfo", dataType=o6.String, value="//xs:element[@name='EddDataTypeInfo']")
o6.reference(o6.ns["ns=fdi7;i=2206"], "i=39", o6.ns["ns=fdi7;i=2210"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi7;i=2213", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi7;i=2217", browseName="ns=fdi7;EddDataTypeInfo", dataType=o6.String, value="EddDataTypeInfo")
o6.reference(o6.ns["ns=fdi7;i=2213"], "i=39", o6.ns["ns=fdi7;i=2217"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi7;i=8001", browseName="Default JSON")
o6.hasEncoding(fdi7_datypes.EddDataTypeInfo, o6.ns["ns=fdi7;i=8001"])
opcDotUaDotFdi7_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdi7;i=2214",
    browseName="ns=fdi7;Opc.Ua.Fdi7",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=2216", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI7/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=8002", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=2217"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/"\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://fdi-cooperation.com/OPCUA/FDI7/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://fdi-cooperation.com/OPCUA/FDI7/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/DI/" Location="Opc.Ua.Di.BinarySchema.bsd"/>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:EnumeratedType Name="EddDataTypeEnum" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="BOOLEAN" Value="1" />\r\n    <opc:EnumeratedValue Name="DOUBLE" Value="2" />\r\n    <opc:EnumeratedValue Name="FLOAT" Value="3" />\r\n    <opc:EnumeratedValue Name="INTEGER" Value="4" />\r\n    <opc:EnumeratedValue Name="UNSIGNED_INTEGER" Value="5" />\r\n    <opc:EnumeratedValue Name="DATE" Value="6" />\r\n    <opc:EnumeratedValue Name="DATE_AND_TIME" Value="7" />\r\n    <opc:EnumeratedValue Name="DURATION" Value="8" />\r\n    <opc:EnumeratedValue Name="TIME" Value="9" />\r\n    <opc:EnumeratedValue Name="TIME_VALUE" Value="10" />\r\n    <opc:EnumeratedValue Name="BIT_ENUMERATED" Value="11" />\r\n    <opc:EnumeratedValue Name="ENUMERATED" Value="12" />\r\n    <opc:EnumeratedValue Name="ASCII" Value="13" />\r\n    <opc:EnumeratedValue Name="BITSTRING" Value="14" />\r\n    <opc:EnumeratedValue Name="EUC" Value="15" />\r\n    <opc:EnumeratedValue Name="OCTET" Value="16" />\r\n    <opc:EnumeratedValue Name="PACKED_ASCII" Value="17" />\r\n    <opc:EnumeratedValue Name="PASSWORD" Value="18" />\r\n    <opc:EnumeratedValue Name="VISIBLE" Value="19" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="EddDataTypeInfo" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="EddDataType" TypeName="tns:EddDataTypeEnum" />\r\n    <opc:Field Name="Size" TypeName="opc:UInt32" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
opcDotUaDotFdi7 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdi7;i=2207",
    browseName="ns=fdi7;Opc.Ua.Fdi7",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=2209", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI7/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=8004", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=fdi7;i=2210"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/Types.xsd"\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://fdi-cooperation.com/OPCUA/FDI7/Types.xsd"\r\n  targetNamespace="http://fdi-cooperation.com/OPCUA/FDI7/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:import namespace="http://opcfoundation.org/UA/DI/Types.xsd" />\r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:simpleType  name="EddDataTypeEnum">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="BOOLEAN_1" />\r\n      <xs:enumeration value="DOUBLE_2" />\r\n      <xs:enumeration value="FLOAT_3" />\r\n      <xs:enumeration value="INTEGER_4" />\r\n      <xs:enumeration value="UNSIGNED_INTEGER_5" />\r\n      <xs:enumeration value="DATE_6" />\r\n      <xs:enumeration value="DATE_AND_TIME_7" />\r\n      <xs:enumeration value="DURATION_8" />\r\n      <xs:enumeration value="TIME_9" />\r\n      <xs:enumeration value="TIME_VALUE_10" />\r\n      <xs:enumeration value="BIT_ENUMERATED_11" />\r\n      <xs:enumeration value="ENUMERATED_12" />\r\n      <xs:enumeration value="ASCII_13" />\r\n      <xs:enumeration value="BITSTRING_14" />\r\n      <xs:enumeration value="EUC_15" />\r\n      <xs:enumeration value="OCTET_16" />\r\n      <xs:enumeration value="PACKED_ASCII_17" />\r\n      <xs:enumeration value="PASSWORD_18" />\r\n      <xs:enumeration value="VISIBLE_19" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="EddDataTypeEnum" type="tns:EddDataTypeEnum" />\r\n\r\n  <xs:complexType name="ListOfEddDataTypeEnum">\r\n    <xs:sequence>\r\n      <xs:element name="EddDataTypeEnum" type="tns:EddDataTypeEnum" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfEddDataTypeEnum" type="tns:ListOfEddDataTypeEnum" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="EddDataTypeInfo">\r\n    <xs:sequence>\r\n      <xs:element name="EddDataType" type="tns:EddDataTypeEnum" minOccurs="0" />\r\n      <xs:element name="Size" type="xs:unsignedInt" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="EddDataTypeInfo" type="tns:EddDataTypeInfo" />\r\n\r\n  <xs:complexType name="ListOfEddDataTypeInfo">\r\n    <xs:sequence>\r\n      <xs:element name="EddDataTypeInfo" type="tns:EddDataTypeInfo" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfEddDataTypeInfo" type="tns:ListOfEddDataTypeInfo" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
httpColonSlashSlashFdiMinusCooperationDotComSlashOPCUASlashFDI7Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fdi7;i=15009",
    browseName="ns=fdi7;http://fdi-cooperation.com/OPCUA/FDI7/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15010", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI7/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15011", browseName="NamespaceVersion", dataType=o6.String, value="1.3")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15012", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2017-07-14T00:00:00Z"))),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15013", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=15014", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=15015", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15016", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15039", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi7;i=15040", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15041", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdi7_datypes, fdi7_objtypes
