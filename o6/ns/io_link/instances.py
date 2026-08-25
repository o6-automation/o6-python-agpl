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

"""Generated OPC UA io_link namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as io_link_reftypes
from . import datatypes as io_link_datypes
from . import vartypes as io_link_vartypes
from . import objtypes as io_link_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

iOLinkMasterSet = ns0.objtypes.FolderType(nodeId="ns=io_link;i=5005", browseName="ns=io_link;IOLinkMasterSet", parent="i=85", referenceType=ns0.reftypes.Organizes)
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5039", browseName="ns=io_link;ConfiguredDevice")
di.objtypes.FunctionalGroupType(
    nodeId="ns=io_link;i=5031", browseName="ns=io_link;Configuration", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=io_link;i=5039"])]
)
o6.reference(io_link_objtypes.IOLinkPortType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5031"])
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6000",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=io_link;i=3000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ASCII_0")), ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("UTF8_1"))],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashIOLinkSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=io_link;i=5021",
    browseName="ns=io_link;http://opcfoundation.org/UA/IOLink/",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6001", browseName="IsNamespaceSubset", description="If TRUE then the server only supports a subset of the namespace.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6011",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2022-03-24T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6012", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://opcfoundation.org/UA/IOLink/"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6013",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.00.1",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6014",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6015",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[1],
                value=["0:9999"],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6016",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6024", browseName="ns=io_link;ErrorCount", dataType=o6.UInt16)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6024"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6025", browseName="ns=io_link;DetailedDeviceStatus", dataType=o6.Byte, valueRank=2, arrayDimensions=[0, 3])
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6025"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6028", browseName="ns=io_link;OffsetTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6028"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=io_link;i=6021",
    browseName="ns=io_link;ApplicationSpecificTag",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6030", browseName="ns=io_link;StoredInDevice", dataType=o6.Boolean))],
    dataType=o6.String,
    value="***",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6021"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=io_link;i=6022",
    browseName="ns=io_link;FunctionTag",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6031", browseName="ns=io_link;StoredInDevice", dataType=o6.Boolean))],
    dataType=o6.String,
    value="***",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6022"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=io_link;i=6023",
    browseName="ns=io_link;LocationTag",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6032", browseName="ns=io_link;StoredInDevice", dataType=o6.Boolean))],
    dataType=o6.String,
    value="***",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6023"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=io_link;i=5001",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.ns["ns=io_link;i=6021"]), o6.organizes(o6.ns["ns=io_link;i=6022"]), o6.organizes(o6.ns["ns=io_link;i=6023"])],
)
o6.reference(io_link_objtypes.IOLinkDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5001"])
o6.reference(o6.ns["ns=io_link;i=5001"], "i=35", o6.ns["ns=io_link;i=6004"])
o6.reference(o6.ns["ns=io_link;i=5001"], "i=35", o6.ns["ns=io_link;i=6005"])
o6.reference(o6.ns["ns=io_link;i=5001"], "i=35", o6.ns["ns=io_link;i=6029"])
ns0.objtypes.FolderType(
    nodeId="ns=io_link;i=5014",
    browseName="ns=di;DeviceTypeImage",
    description="Organizes pictures of the device.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=io_link;i=6059",
                browseName="ns=di;<ImageIdentifier>",
                description="An image of the device.",
                modellingRule="MandatoryPlaceholder",
                dataType=ns0.datatypes.Image,
                value=b"",
            )
        )
    ],
)
o6.reference(io_link_objtypes.IOLinkIODDDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5014"])
ns0.vartypes.OptionSetType(
    nodeId="ns=io_link;i=6060",
    browseName="ns=io_link;SupportedAccessLocks",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6061", browseName="OptionSetValues", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.Byte,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5007",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=io_link;i=6060"])],
)
o6.reference(io_link_objtypes.IOLinkIODDDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5007"])
ns0.objtypes.FolderType(
    nodeId="ns=io_link;i=5011",
    browseName="ns=io_link;IODDInformation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6062", browseName="ns=io_link;Version", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6063", browseName="ns=io_link;ReleaseDate", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6064", browseName="ns=io_link;Copyright", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6065", browseName="ns=io_link;IOLinkRevision", dataType=o6.String, value="")),
    ],
)
o6.reference(io_link_objtypes.IOLinkIODDDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5011"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6074", browseName="ns=io_link;DeviceIcon", dataType=ns0.datatypes.Image, value=b"")
o6.reference(o6.ns["ns=io_link;i=5014"], "i=47", o6.ns["ns=io_link;i=6074"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6075", browseName="ns=io_link;DeviceSymbol", dataType=ns0.datatypes.Image, value=b"")
o6.reference(o6.ns["ns=io_link;i=5014"], "i=47", o6.ns["ns=io_link;i=6075"])
io_link_objtypes.DeviceVariantType(
    nodeId="ns=io_link;i=5013",
    browseName="ns=io_link;DeviceVariant",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6071", browseName="ns=io_link;Description", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6072", browseName="ns=io_link;Name", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6073", browseName="ns=io_link;ProductId", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=io_link;i=6074"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6075"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkIODDDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5013"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6100", browseName="ns=io_link;MaxNumberOfPorts", dataType=o6.Byte)
o6.reference(o6.ns["ns=io_link;i=5018"], "i=35", o6.ns["ns=io_link;i=6100"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=io_link;i=6101",
    browseName="ns=io_link;MaxPowerSupply",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6048",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        )
    ],
    dataType=o6.Double,
)
o6.reference(o6.ns["ns=io_link;i=5018"], "i=35", o6.ns["ns=io_link;i=6101"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6102", browseName="ns=io_link;ApplicationSpecificTag", dataType=o6.String, value="***", accessLevel=3, userAccessLevel=1)
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6103", browseName="ns=io_link;FunctionTag", dataType=o6.String, value="***", accessLevel=3, userAccessLevel=1)
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6104", browseName="ns=io_link;LocationTag", dataType=o6.String, value="***", accessLevel=3, userAccessLevel=1)
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6106", browseName="ns=io_link;DateOfLastStatisticsReset", dataType=o6.DateTime)
o6.reference(o6.ns["ns=io_link;i=5020"], "i=35", o6.ns["ns=io_link;i=6106"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6107", browseName="ns=io_link;NumberOfIOLinkMasterStarts", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5020"], "i=35", o6.ns["ns=io_link;i=6107"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5017",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=io_link;i=6100"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6101"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6106"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6107"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkMasterType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5017"])
o6.reference(o6.ns["ns=io_link;i=5017"], "i=47", o6.ns["ns=io_link;i=6102"])
o6.reference(o6.ns["ns=io_link;i=5017"], "i=47", o6.ns["ns=io_link;i=6103"])
o6.reference(o6.ns["ns=io_link;i=5017"], "i=47", o6.ns["ns=io_link;i=6104"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6105",
    browseName="ns=io_link;MasterType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6108",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("Unspecific", "en"), o6.LocalizedText("Master acc. V1.0", "en"), o6.LocalizedText("Master acc. V1.1", "en")],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5017"], "i=47", o6.ns["ns=io_link;i=6105"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=io_link;i=5015",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[
        o6.organizes(o6.ns["ns=io_link;i=6102"]),
        o6.organizes(o6.ns["ns=io_link;i=6103"]),
        o6.organizes(o6.ns["ns=io_link;i=6104"]),
        o6.organizes(o6.ns["ns=io_link;i=6105"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkMasterType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5015"])
o6.reference(o6.ns["ns=io_link;i=5015"], "i=35", o6.ns["ns=io_link;i=6078"])
o6.reference(o6.ns["ns=io_link;i=5015"], "i=35", o6.ns["ns=io_link;i=6082"])
io_link_vartypes.ProcessDataVariableType(
    nodeId="ns=io_link;i=6027",
    browseName="ns=io_link;ProcessDataInput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6133", browseName="ns=io_link;ProcessDataLength", dataType=o6.Byte))],
    dataType=o6.Byte,
    valueRank=1,
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6027"])
io_link_vartypes.ProcessDataVariableType(
    nodeId="ns=io_link;i=6026",
    browseName="ns=io_link;ProcessDataOutput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6134", browseName="ns=io_link;ProcessDataLength", dataType=o6.Byte))],
    dataType=o6.Byte,
    valueRank=1,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=6026"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5003",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=io_link;i=6024"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6025"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6026"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6027"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6028"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5003"])
o6.reference(o6.ns["ns=io_link;i=5003"], "i=47", o6.ns["ns=io_link;i=6021"])
o6.reference(o6.ns["ns=io_link;i=5003"], "i=47", o6.ns["ns=io_link;i=6022"])
o6.reference(o6.ns["ns=io_link;i=5003"], "i=47", o6.ns["ns=io_link;i=6023"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6150",
    browseName="ns=io_link;PortClass",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6151",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("CLASS A", "en"), o6.LocalizedText("", "en"), o6.LocalizedText("CLASS B", "en")],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5028"], "i=35", o6.ns["ns=io_link;i=6150"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6153", browseName="ns=io_link;Pin2Support", dataType=o6.Boolean)
o6.reference(o6.ns["ns=io_link;i=5028"], "i=35", o6.ns["ns=io_link;i=6153"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6154", browseName="ns=io_link;CycleTime", dataType=ns0.datatypes.Duration)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=6154"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6155",
    browseName="ns=io_link;ValidationAndBackup",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6156",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    o6.LocalizedText("No Device check", "en"),
                    o6.LocalizedText("Type compatible Device V1.0", "en"),
                    o6.LocalizedText("Type compatible Device V1.1", "en"),
                    o6.LocalizedText("Type compatible Device V1.1, Backup + Restore", "en"),
                    o6.LocalizedText("Type compatible Device V1.1, Restore", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=6155"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6157",
    browseName="ns=io_link;PortMode",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6158",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[
                    o6.LocalizedText("DEACTIVATED", "en"),
                    o6.LocalizedText("IOL_MANUAL", "en"),
                    o6.LocalizedText("IOL_AUTOSTART", "en"),
                    o6.LocalizedText("DI_C/Q (Pin4)", "en"),
                    o6.LocalizedText("DO_C/Q (Pin4)", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=6157"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6159",
    browseName="ns=io_link;Pin2Configuration",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6160",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    o6.LocalizedText("Not supported", "en"),
                    o6.LocalizedText("Digital Input", "en"),
                    o6.LocalizedText("Digital Output", "en"),
                    o6.LocalizedText("Analog Input", "en"),
                    o6.LocalizedText("Analog Output", "en"),
                    o6.LocalizedText("Power 2 (Port Class B)", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=6159"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6161", browseName="ns=io_link;UseIODD", dataType=o6.Boolean)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=6161"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6162", browseName="ns=io_link;DeviceID", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5039"], "i=35", o6.ns["ns=io_link;i=6162"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6163", browseName="ns=io_link;VendorID", dataType=o6.UInt16)
o6.reference(o6.ns["ns=io_link;i=5039"], "i=35", o6.ns["ns=io_link;i=6163"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6164",
    browseName="ns=io_link;Baudrate",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6165",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("NOT_DETECTED", "en"), o6.LocalizedText("COM1", "en"), o6.LocalizedText("COM2", "en"), o6.LocalizedText("COM3", "en")],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5029"], "i=35", o6.ns["ns=io_link;i=6164"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6166", browseName="ns=io_link;ActualCycleTime", dataType=ns0.datatypes.Duration)
o6.reference(o6.ns["ns=io_link;i=5029"], "i=35", o6.ns["ns=io_link;i=6166"])
ns0.vartypes.OptionSetType(
    nodeId="ns=io_link;i=6167",
    browseName="ns=io_link;Quality",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6168",
                browseName="OptionSetValues",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[2],
                value=[o6.LocalizedText("PDIn invalid", "en"), o6.LocalizedText("PDOut invalid", "en")],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5029"], "i=35", o6.ns["ns=io_link;i=6167"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=io_link;i=6169",
    browseName="ns=io_link;Status",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6170",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[255],
                value=[
                    o6.LocalizedText("NO_DEVICE", "en"),
                    o6.LocalizedText("DEACTIVATED", "en"),
                    o6.LocalizedText("INCORRECT_DEVICE", "en"),
                    o6.LocalizedText("PREOPERATE", "en"),
                    o6.LocalizedText("OPERATE", "en"),
                    o6.LocalizedText("DI_C/Q (Pin4)", "en"),
                    o6.LocalizedText("DO_C/Q (Pin4)", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("", "en"),
                    o6.LocalizedText("PORT_FAULT", "en"),
                    o6.LocalizedText("NOT_AVAILABLE", "en"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(o6.ns["ns=io_link;i=5029"], "i=35", o6.ns["ns=io_link;i=6169"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6171", browseName="ns=io_link;Pin2ProcessData", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=io_link;i=5032"], "i=35", o6.ns["ns=io_link;i=6171"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6172", browseName="ns=io_link;Pin4ProcessData", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=io_link;i=5032"], "i=35", o6.ns["ns=io_link;i=6172"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6173", browseName="ns=io_link;DateOfLastStatisticsReset", dataType=o6.DateTime)
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=6173"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6174", browseName="ns=io_link;NumberOfAborts", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=6174"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6175", browseName="ns=io_link;NumberOfCycles", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=6175"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6176", browseName="ns=io_link;NumberOfDeviceHasBeenExchanged", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=6176"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6177", browseName="ns=io_link;NumberOfRetries", dataType=o6.UInt32)
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=6177"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=io_link;i=6152",
    browseName="ns=io_link;MaxPowerSupply",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=io_link;i=6178",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4279632,
                    displayName=o6.LocalizedText("A", "en"),
                    description=o6.LocalizedText("ampere", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
)
o6.reference(o6.ns["ns=io_link;i=5028"], "i=35", o6.ns["ns=io_link;i=6152"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5027",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=io_link;i=6150"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6152"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6153"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6154"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6155"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6157"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6159"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6161"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6162"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6163"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6164"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6166"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6167"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6169"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6171"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6172"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6173"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6174"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6175"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6176"]),
        o6.hasComponent(o6.ns["ns=io_link;i=6177"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkPortType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5027"])


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6033",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Index", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="SubIndex", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6034",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Result", dataType=o6.Byte, valueRank=1),
        ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(nodeId="ns=io_link;i=7005", browseName="ns=io_link;ReadISDU", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6033"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6034"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7005"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6035",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Index", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="SubIndex", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="Data", dataType=o6.Byte, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6036",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7006", browseName="ns=io_link;WriteISDU", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6035"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6036"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7006"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Cmd", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6038",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=io_link;i=7007", browseName="ns=io_link;SystemCommand", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6037"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6038"])
)
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7007"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6039",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7008", browseName="ns=io_link;ParamUploadFromDeviceStart", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6039"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7008"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6040",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7009", browseName="ns=io_link;ParamUploadFromDeviceStop", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6040"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7009"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7010", browseName="ns=io_link;ParamDownloadToDeviceStart", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6041"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7010"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7011", browseName="ns=io_link;ParamDownloadToDeviceStop", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6042"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7011"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6043",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7012", browseName="ns=io_link;ParamDownloadToDeviceStore", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6043"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7012"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7013", browseName="ns=io_link;ParamBreak", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6044"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7013"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6045",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7014", browseName="ns=io_link;DeviceReset", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6045"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7014"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6046",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7015", browseName="ns=io_link;ApplicationReset", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6046"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7015"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6047",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorType", dataType=o6.UInt16, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7016", browseName="ns=io_link;RestoreFactorySettings", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6047"]))
o6.reference(o6.ns["ns=io_link;i=5004"], "i=35", o6.ns["ns=io_link;i=7016"])

ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5002",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=io_link;i=7005"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7006"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7007"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7008"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7009"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7010"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7011"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7012"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7013"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7014"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7015"]),
        o6.hasComponent(o6.ns["ns=io_link;i=7016"]),
    ],
)
o6.reference(io_link_objtypes.IOLinkDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5002"])


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6109",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Delay", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6110",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7024", browseName="ns=io_link;Restart", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6109"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6110"]))
o6.reference(o6.ns["ns=io_link;i=5019"], "i=35", o6.ns["ns=io_link;i=7024"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6111",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7025", browseName="ns=io_link;ResetStatisticsOnAllPorts", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6111"]))
o6.reference(o6.ns["ns=io_link;i=5020"], "i=35", o6.ns["ns=io_link;i=7025"])

ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5016",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=io_link;i=7024"]), o6.hasComponent(o6.ns["ns=io_link;i=7025"])],
)
o6.reference(io_link_objtypes.IOLinkMasterType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5016"])


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6179",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=7040", browseName="ns=io_link;ResetStatistics", outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6179"]))
o6.reference(o6.ns["ns=io_link;i=5030"], "i=35", o6.ns["ns=io_link;i=7040"])

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="CycleTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="ValidationAndBackup", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="PortMode", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="Pin2Configuration", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="UseIODD", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceID", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="VendorID", dataType=o6.UInt16, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6181",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=io_link;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=io_link;i=7041",
    browseName="ns=io_link;UpdateConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6180"]),
    outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=6181"]),
)
o6.reference(o6.ns["ns=io_link;i=5031"], "i=35", o6.ns["ns=io_link;i=7041"])

ns0.objtypes.BaseObjectType(
    nodeId="ns=io_link;i=5026",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=io_link;i=7040"]), o6.hasComponent(o6.ns["ns=io_link;i=7041"])],
)
o6.reference(io_link_objtypes.IOLinkPortType, ns0.reftypes.HasComponent, o6.ns["ns=io_link;i=5026"])


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10003",
    browseName="InputArguments",
    parent="ns=io_link;i=10002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="IODD", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="Force", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10004",
    browseName="OutputArguments",
    parent="ns=io_link;i=10002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=io_link;i=10002", browseName="ns=io_link;RemoveIODD", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10003"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10004"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10008",
    browseName="InputArguments",
    parent="ns=io_link;i=10007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10009",
    browseName="OutputArguments",
    parent="ns=io_link;i=10007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=10007", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10008"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10009"]))

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10011",
    browseName="InputArguments",
    parent="ns=io_link;i=10010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10012",
    browseName="OutputArguments",
    parent="ns=io_link;i=10010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=io_link;i=10010", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10011"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10012"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10014",
    browseName="InputArguments",
    parent="ns=io_link;i=10013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10015",
    browseName="OutputArguments",
    parent="ns=io_link;i=10013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=io_link;i=10013", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10014"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10015"])
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=io_link;i=10005",
    browseName="ns=io_link;TemporaryFileTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=10006", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=io_link;i=10007"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10010"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10013"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10019",
    browseName="InputArguments",
    parent="ns=io_link;i=10018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10020",
    browseName="OutputArguments",
    parent="ns=io_link;i=10018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=io_link;i=10018", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10019"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10020"]))

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10022",
    browseName="InputArguments",
    parent="ns=io_link;i=10021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10023",
    browseName="OutputArguments",
    parent="ns=io_link;i=10021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=io_link;i=10021", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10022"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10023"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10025",
    browseName="InputArguments",
    parent="ns=io_link;i=10024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=10026",
    browseName="OutputArguments",
    parent="ns=io_link;i=10024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=io_link;i=10024", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10025"]), outputArgs=o6.hasProperty(o6.ns["ns=io_link;i=10026"])
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=io_link;i=10016",
    browseName="ns=io_link;TransferIODD",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=10017", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=io_link;i=10018"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10021"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10024"]),
    ],
)
iODDManagement = ns0.objtypes.FolderType(
    nodeId="ns=io_link;i=10000",
    browseName="ns=io_link;IODDManagement",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=io_link;i=10001", browseName="ns=io_link;IODDs")),
        o6.hasComponent(o6.ns["ns=io_link;i=10002"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10005"]),
        o6.hasComponent(o6.ns["ns=io_link;i=10016"]),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, io_link_reftypes, io_link_datypes, io_link_vartypes, io_link_objtypes
