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

"""Generated OPC UA iredes namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as iredes_datypes
from . import objtypes as iredes_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5002", browseName="Default XML")
o6.hasEncoding(iredes_datypes.IRLengthDataType, o6.ns["ns=iredes;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5003", browseName="Default JSON")
o6.hasEncoding(iredes_datypes.IRLengthDataType, o6.ns["ns=iredes;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5005", browseName="Default XML")
o6.hasEncoding(iredes_datypes.JobAssignmentTimeDataType, o6.ns["ns=iredes;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=iredes;i=5006", browseName="Default JSON")
o6.hasEncoding(iredes_datypes.JobAssignmentTimeDataType, o6.ns["ns=iredes;i=5006"])
iredes_objtypes.SiteHeadType(
    nodeId="ns=iredes;i=5012",
    browseName="ns=iredes;SiteHead",
    description="Optional site header.",
    modellingRule="Optional",
    references=[
        o6.hasAddIn(
            iredes_objtypes.DisplayToOperatorType(
                nodeId="ns=iredes;i=5013", browseName="ns=iredes;DisplayToOperator", description="Object used to display messages to the operator of a machine."
            )
        ),
        o6.hasAddIn(
            iredes_objtypes.IROptionType(
                nodeId="ns=iredes;i=5014", browseName="ns=iredes;SiteOption", description="Object that holds/references information that will not be processed."
            )
        ),
    ],
)
o6.reference(iredes_objtypes.IREDESType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5012"])
ns0.vartypes.PropertyType(
    nodeId="ns=iredes;i=6007",
    browseName="EnumValues",
    parent="ns=iredes;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("MachStart"),
            description=o6.LocalizedText("To be displayed when the machine is started. Machine start is defined as switching on the main power supply or power generation."),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("FileLoad"),
            description=o6.LocalizedText(
                "To be displayed as soon as the file is loaded (activated) in the machine&#8217;s automation system (applicable especially to plan files originating from the mine!)."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=iredes;i=6008",
    browseName="EnumValues",
    parent="ns=iredes;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Accepted"), description=o6.LocalizedText("Order is accepted.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Delayed"), description=o6.LocalizedText("Order can only be executed with delay.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AcceptedWithCondition"), description=o6.LocalizedText("Order is accepted under a condition.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Denied"), description=o6.LocalizedText("Orders denied.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=iredes;i=6009",
    browseName="EnumValues",
    parent="ns=iredes;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LoadPt"), description=o6.LocalizedText("Load point")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DumpPt"), description=o6.LocalizedText("Dump point")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Parking"), description=o6.LocalizedText("Parking")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Workshop"), description=o6.LocalizedText("Workshop")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Others"), description=o6.LocalizedText("Others")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=iredes;i=6010",
    browseName="EnumValues",
    parent="ns=iredes;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LoadPt"), description=o6.LocalizedText("Load point")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DumpPt"), description=o6.LocalizedText("Dump point")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Parking"), description=o6.LocalizedText("Parking")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Boulder"), description=o6.LocalizedText("Boulder")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Workshop"), description=o6.LocalizedText("Workshop")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Others"), description=o6.LocalizedText("Others")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=iredes;i=6011",
    browseName="EnumValues",
    parent="ns=iredes;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Load"), description=o6.LocalizedText("Load")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Dump"), description=o6.LocalizedText("Dump")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Parking"), description=o6.LocalizedText("Parking")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Workshop"), description=o6.LocalizedText("Workshop")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Other")),
    ],
)
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5011",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6040",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6041",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6042",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(iredes_objtypes.IREDESType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5011"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5016",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6054",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6055",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6056",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5015",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6053",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6057", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5016"]),
    ],
)
o6.reference(iredes_objtypes.IRpPerfGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5015"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5018",
    browseName="ns=iredes;GenHead",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6059",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6060",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6061",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.OpPerfLogType(
    nodeId="ns=iredes;i=5017",
    browseName="ns=iredes;OpPerfLog",
    description="Object Type which accumulates the time of each operation mode during the reporting period.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6058",
                browseName="ns=iredes;DownCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6062", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5018"]),
    ],
)
o6.reference(iredes_objtypes.IRpPerfGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5017"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5020",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6069",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6070",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6071",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5019",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6068",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6072", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5020"]),
    ],
)
o6.reference(iredes_objtypes.IRplanGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5019"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5021",
    browseName="ns=iredes;Reply",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6091", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
o6.reference(iredes_objtypes.IRreplyType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5021"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5023",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6095",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6096",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6097",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5022",
    browseName="ns=iredes;IREDESType",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6094",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6098", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5023"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5022"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5025",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6111", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5024",
    browseName="ns=iredes;Reply1",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6110", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5025"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5024"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5027",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6113", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5026",
    browseName="ns=iredes;Reply2",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6112", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5027"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5026"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5029",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6115", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5028",
    browseName="ns=iredes;Reply3",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6114", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5029"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5028"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5031",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6117", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5030",
    browseName="ns=iredes;Reply4",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6116", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5031"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5030"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5033",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6119", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5032",
    browseName="ns=iredes;Reply5",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6118", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5033"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5032"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5035",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6121", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5034",
    browseName="ns=iredes;Reply6",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6120", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5035"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5034"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5037",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6123", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5036",
    browseName="ns=iredes;Reply7",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6122", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5037"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5036"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5039",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6125", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5038",
    browseName="ns=iredes;Reply8",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6124", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5039"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5038"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5041",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6127", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5040",
    browseName="ns=iredes;Reply9",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6126", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5041"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5040"])
iredes_objtypes.IRWorkOrderReplyGenType(
    nodeId="ns=iredes;i=5043",
    browseName="ns=iredes;Reply",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6129", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
            )
        )
    ],
)
iredes_objtypes.IRreplyType(
    nodeId="ns=iredes;i=5042",
    browseName="ns=iredes;Reply10",
    description="Work order reply.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6128", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=0, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5043"]),
    ],
)
o6.reference(iredes_objtypes.IRWorkOrderGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5042"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5046",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6132",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6133",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6134",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5045",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6131",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6135", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5046"]),
    ],
)
o6.reference(iredes_objtypes.IRLTMMonType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5045"])
iredes_objtypes.GenTrailerType(
    nodeId="ns=iredes;i=5047",
    browseName="ns=iredes;GenTrailer",
    description="Datatype that is used to guarantee the integrity of the data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6136", browseName="ns=iredes;ChkSum", description="CRC 32 checksum.", dataType=o6.ByteString, accessLevel=3)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6137", browseName="ns=iredes;FileCloseDate", description="Date the file was created.", dataType=o6.DateTime, accessLevel=3
            )
        ),
    ],
)
o6.reference(iredes_objtypes.IRLTMMonType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5047"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5050",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6142",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6143",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6144",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5049",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6141",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6145", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5050"]),
    ],
)
iredes_objtypes.IRplanGenType(
    nodeId="ns=iredes;i=5048",
    browseName="ns=iredes;IRplanGen",
    description="Generic datatype for production planning.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6146",
                browseName="ns=iredes;PlanId",
                description="IREDES internal production plan ID used for reference e.g. by Production Quality data sets basing on a particular production plan.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6147",
                browseName="ns=iredes;PlanName",
                description="Plan logical name to identify this specific plan to the human user. Useful to help the operator of a machine to logical identify a specific plan.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5049"]),
    ],
)
o6.reference(iredes_objtypes.IRLTPlanType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5048"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5053",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6149",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6150",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6151",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5052",
    browseName="ns=iredes;IREDESType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6148",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6152", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5053"]),
    ],
)
iredes_objtypes.GenTrailerType(
    nodeId="ns=iredes;i=5051",
    browseName="ns=iredes;GenTrailer",
    description="Datatype that is used to ensure the integrity of the data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6153",
                browseName="ns=iredes;PlanId",
                description="IREDES internal production plan ID used for reference e.g. by Production Quality data sets basing on a particular production plan.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6154",
                browseName="ns=iredes;PlanName",
                description="Plan logical name to identify this specific plan to the human user. Useful to help the operator of a machine to logical identify a specific plan.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5052"]),
    ],
)
o6.reference(iredes_objtypes.IRLTPlanType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5051"])
iredes_objtypes.LTPPTimeRepType(
    nodeId="ns=iredes;i=5054",
    browseName="ns=iredes;LTPPTimeRep",
    description="Time reporting for access to the particular load / Dump point pair. Multiple elements may be required as work can be interrupted and restarted again at a later time during reporting period.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6195", browseName="ns=iredes;LTPPEndTime", description="Mission end time.", dataType=ns0.datatypes.UtcTime, accessLevel=3)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6196", browseName="ns=iredes;LTPPStartTime", description="Mission start time.", dataType=ns0.datatypes.UtcTime, accessLevel=3
            )
        ),
    ],
)
o6.reference(iredes_objtypes.LTPPaccPtsType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5054"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5060",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6212",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6213",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6214",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5059",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6211",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6215", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5060"]),
    ],
)
iredes_objtypes.IRpPerfGenType(
    nodeId="ns=iredes;i=5058",
    browseName="ns=iredes;IRpPerfGen",
    description="Generic type used report production performance.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6210",
                browseName="ns=iredes;EndLogTine",
                description="End of the reporting period. Date and time when the last entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6216", browseName="ns=iredes;ReportId", description="Report ID code, to uniquely identify this log report.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6217",
                browseName="ns=iredes;StartLogTime",
                description="Start of the reporting period. Date and time when the first entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5059"]),
    ],
)
o6.reference(iredes_objtypes.IRLTPPerfType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5058"])
iredes_objtypes.LTPPLoadRepType(
    nodeId="ns=iredes;i=5061",
    browseName="ns=iredes;LTPPLoadRep",
    description="Reports on how much material has been transported between load and dump points during the reporting period.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6218",
                browseName="ns=iredes;LTPPCyclTot",
                description="Total number of working cycles (rounds) completed during the reporting period.",
                dataType=o6.UInt64,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6219",
                browseName="ns=iredes;LTPPloadTot",
                description="Total load carried under all completed working cycles during reporting period. Minimum accuracy required by the standard: 0.01.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(iredes_objtypes.IRLTPPerfType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5061"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5065",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6225",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6226",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6227",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5064",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6224",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6228", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5065"]),
    ],
)
iredes_objtypes.IRpPerfGenType(
    nodeId="ns=iredes;i=5063",
    browseName="ns=iredes;IRpPerfGen",
    description="Generic type used report production performance.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6223",
                browseName="ns=iredes;EndLogTine",
                description="End of the reporting period. Date and time when the last entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6229", browseName="ns=iredes;ReportId", description="Report ID code, to uniquely identify this log report.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6230",
                browseName="ns=iredes;StartLogTime",
                description="Start of the reporting period. Date and time when the first entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5064"]),
    ],
)
iredes_objtypes.LTPPLoadRepType(
    nodeId="ns=iredes;i=5066",
    browseName="ns=iredes;LTPPLoadRep",
    description="Reports on how much material has been transported between load and dump points during the reporting period.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6233",
                browseName="ns=iredes;LTPPCyclTot",
                description="Total number of working cycles (rounds) completed during the reporting period.",
                dataType=o6.UInt64,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6234",
                browseName="ns=iredes;LTPPloadTot",
                description="Total load carried under all completed working cycles during reporting period. Minimum accuracy required by the standard: 0.01.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IRLTPPerfType(
    nodeId="ns=iredes;i=5062",
    browseName="ns=iredes;IRLTPPerf",
    description="IRLHD production performance reporting.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6231", browseName="ns=iredes;LTPPerfDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6232", browseName="ns=iredes;LTPPerfVersion", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5063"]),
        o6.hasAddIn(o6.ns["ns=iredes;i=5066"]),
    ],
)
o6.reference(iredes_objtypes.IRLHDTruckType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5062"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5070",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6237",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6238",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6239",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5069",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6236",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6240", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5070"]),
    ],
)
iredes_objtypes.IRpPerfGenType(
    nodeId="ns=iredes;i=5068",
    browseName="ns=iredes;IRpPerfGenType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6235",
                browseName="ns=iredes;EndLogTine",
                description="End of the reporting period. Date and time when the last entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6241", browseName="ns=iredes;ReportId", description="Report ID code, to uniquely identify this log report.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6242",
                browseName="ns=iredes;StartLogTime",
                description="Start of the reporting period. Date and time when the first entry to this xml-set was made.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5069"]),
    ],
)
iredes_objtypes.LTPPLoadRepType(
    nodeId="ns=iredes;i=5071",
    browseName="ns=iredes;LTPPLoadRepType",
    description="Reports on how much material has been transported between load and dump points during the reporting period.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6245",
                browseName="ns=iredes;LTPPCyclTot",
                description="Total number of working cycles (rounds) completed during the reporting period.",
                dataType=o6.UInt64,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6246",
                browseName="ns=iredes;LTPPloadTot",
                description="Total load carried under all completed working cycles during reporting period. Minimum accuracy required by the standard: 0.01.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IRLTPlanType(
    nodeId="ns=iredes;i=5067",
    browseName="ns=iredes;IRLTPlan",
    description="IRLHD production planning.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6243", browseName="ns=iredes;LTPPerfDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6244", browseName="ns=iredes;LTPPerfVersion", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5068"]),
        o6.hasAddIn(o6.ns["ns=iredes;i=5071"]),
    ],
)
o6.reference(iredes_objtypes.IRLHDTruckType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5067"])
iredes_objtypes.GenTrailerType(
    nodeId="ns=iredes;i=5073",
    browseName="ns=iredes;GenTrailer",
    description="Datatype that is used to guarantee the integrity of the data set.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6247", browseName="ns=iredes;ChkSum", description="CRC 32 checksum.", dataType=o6.ByteString, accessLevel=3)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6248", browseName="ns=iredes;FileCloseDate", description="Date the file was created.", dataType=o6.DateTime, accessLevel=3
            )
        ),
    ],
)
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5075",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6250",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6251",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6252",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5074",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6249",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6253", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5075"]),
    ],
)
iredes_objtypes.IRLTMMonType(
    nodeId="ns=iredes;i=5072",
    browseName="ns=iredes;IRLTMMon",
    description="IRLHD machine monitoring reporting.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6254", browseName="ns=iredes;LTMMonDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6255", browseName="ns=iredes;LTMMonVersion", description="2.0.", dataType=o6.String, accessLevel=3)),
        o6.hasAddIn(o6.ns["ns=iredes;i=5073"]),
        o6.hasAddIn(o6.ns["ns=iredes;i=5074"]),
    ],
)
o6.reference(iredes_objtypes.IRLHDTruckType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5072"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashExternalStandardsSlashIREDES = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=iredes;i=5076",
    browseName="ns=iredes;http://opcfoundation.org/UA/Mining/ExternalStandards/IREDES",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6256", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6257", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-02-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6258", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/ExternalStandards/IREDES")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6259", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6260", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6261", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6262", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
iredes_objtypes.EquipmentInfoType(
    nodeId="ns=iredes;i=5008",
    browseName="ns=iredes;EquipmentInfo",
    description="Equipment specific information concerning the main aggregate the information comes from. ATTENTION: This information shall not be required to interpret a standard conformant data set.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6263", browseName="ns=iredes;EqpManufact", description="Name of the manufacturer.", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6264", browseName="ns=iredes;EqpType", description="Manufacturer internal type name of the machine.", dataType=o6.String)
        ),
    ],
)
o6.reference(iredes_objtypes.GenHeadType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5008"])
iredes_objtypes.GenHeadType(
    nodeId="ns=iredes;i=5078",
    browseName="ns=iredes;GenHead",
    description="IREDES general header.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6266",
                browseName="ns=iredes;DownCompat",
                description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6267",
                browseName="ns=iredes;FileCreateDate",
                description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
                dataType=o6.DateTime,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6268",
                browseName="ns=iredes;IRVersion",
                description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
    ],
)
iredes_objtypes.IREDESType(
    nodeId="ns=iredes;i=5077",
    browseName="ns=iredes;IREDES",
    description="Basic IREDES data type. Part of every complete IREDES data set.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6265",
                browseName="ns=iredes;IRDownwCompat",
                description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6269", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasAddIn(o6.ns["ns=iredes;i=5078"]),
    ],
)
o6.reference(iredes_objtypes.IRStatusGenType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5077"])
iredes_objtypes.LTPPMissionType(
    nodeId="ns=iredes;i=5057",
    browseName="ns=iredes;LTPPMission",
    description="See LTPPMissionType.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6206",
                browseName="ns=iredes;LTPPMisSeq",
                description="Sequence number of the mission. Starting at 1 with the first mission in the reporting period.",
                dataType=o6.UInt64,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6207",
                browseName="ns=iredes;LTPPMptFromN",
                description="Name of the point where the mission originated (tramming started).",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6208",
                browseName="ns=iredes;LTPPMptToN",
                description="Name of the destination point, where the tramming finished and the mission ended.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6270",
                browseName="ns=iredes;LTPPMaction",
                description="Action to be carried out at destination point specified in LTPPMptTo.",
                dataType=iredes_datypes.LTPPMaction,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6271",
                browseName="ns=iredes;LTPPMpayld",
                description="Tonnage of payload carried between start and destination points.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6272",
                browseName="ns=iredes;LTPPMtramDist",
                description="Tramming distance between start and destination point. Unit: km; Resolution: 0.0001 km (10 cm).",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(iredes_objtypes.LTPPLoadRepType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5057"])
iredes_objtypes.LTPPaccPtsType(
    nodeId="ns=iredes;i=5056",
    browseName="ns=iredes;LTPPaccPts",
    description="Report data for each pair of load point / dump point.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6203",
                browseName="ns=iredes;LTPPLdrawPtN",
                description="Name of the draw (load point) accessed in the reported job.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=iredes;i=6204", browseName="ns=iredes;LTPPLdumpPtN", description="Name of the dump point in this combination.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6202",
                browseName="ns=iredes;LTPPLcycl",
                description="Number of cycles travelled between this point pair during reporting period.",
                dataType=o6.UInt16,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6205",
                browseName="ns=iredes;LTPPLmass",
                description="Mass transported between this point pair during reporting period in t. Min accuracy: 0.01 t.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=iredes;i=6273",
                browseName="ns=iredes;LTPPLdist",
                description="Distance travelled between those two points during reporting period. Accumulated distance of al rounds travelled. Both routes are counted! Accuracy: 0.01 km.",
                dataType=o6.Float,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(iredes_objtypes.LTPPLoadRepType, ns0.reftypes.HasAddIn, o6.ns["ns=iredes;i=5056"])


del Any, TYPE_CHECKING, uuid, o6, ns0, iredes_datypes, iredes_objtypes
