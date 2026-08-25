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

"""Generated OPC UA plcopen namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as plcopen_reftypes
from . import datatypes as plcopen_datypes
from . import objtypes as plcopen_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

langleTaskNameRangle = plcopen_objtypes.CtrlTaskType(nodeId="ns=plcopen;i=1008", browseName="ns=plcopen;<TaskName>", modellingRule="OptionalPlaceholder")
o6.reference(plcopen_objtypes.CtrlProgramOrganizationUnitType, "ns=plcopen;i=4006", "ns=plcopen;i=1008")
plcopen_objtypes.CtrlFunctionBlockType(nodeId="ns=plcopen;i=1016", browseName="ns=plcopen;<BlockName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
o6.reference(plcopen_objtypes.CtrlProgramOrganizationUnitType, plcopen_reftypes.HasLocalVar, o6.ns["ns=plcopen;i=1016"])
plcopen_objtypes.SFCType(
    nodeId="ns=plcopen;i=1018",
    browseName="ns=plcopen;<SFCName>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=1019", browseName="ns=plcopen;Priority", dataType=o6.UInt32))],
)
o6.reference(plcopen_objtypes.CtrlProgramOrganizationUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=1018"])
plcopen_objtypes.CtrlFunctionBlockType(nodeId="ns=plcopen;i=1020", browseName="ns=plcopen;<FunctionBlockInputName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
o6.reference(plcopen_objtypes.CtrlFunctionBlockType, plcopen_reftypes.HasInputVar, o6.ns["ns=plcopen;i=1020"])
plcopen_objtypes.CtrlFunctionBlockType(nodeId="ns=plcopen;i=1021", browseName="ns=plcopen;<FunctionBlockOutputName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
o6.reference(plcopen_objtypes.CtrlFunctionBlockType, plcopen_reftypes.HasOutputVar, o6.ns["ns=plcopen;i=1021"])
plcopen_objtypes.CtrlFunctionBlockType(nodeId="ns=plcopen;i=1022", browseName="ns=plcopen;<FunctionBlockInOutName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
o6.reference(plcopen_objtypes.CtrlFunctionBlockType, plcopen_reftypes.HasInOutVar, o6.ns["ns=plcopen;i=1022"])
subrangeMin = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3400", browseName="ns=plcopen;SubrangeMin", dataType=ns0.datatypes.Number)
subrangeMax = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3401", browseName="ns=plcopen;SubrangeMax", dataType=ns0.datatypes.Number)
dimensions = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3402", browseName="ns=plcopen;Dimensions", dataType=o6.UInt32)
indexMin = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3403", browseName="ns=plcopen;IndexMin", dataType=o6.Int32, valueRank=1)
indexMax = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3404", browseName="ns=plcopen;IndexMax", dataType=o6.Int32, valueRank=1)
rETAIN = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3405", browseName="ns=plcopen;RETAIN", dataType=o6.Boolean)
nON_RETAIN = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3406", browseName="ns=plcopen;NON_RETAIN", dataType=o6.Boolean)
cONSTANT = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3407", browseName="ns=plcopen;CONSTANT", dataType=o6.Boolean)
aT = ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=3408", browseName="ns=plcopen;AT", dataType=o6.String)
ns0.objtypes.BaseObjectType(
    nodeId="ns=plcopen;i=5001",
    browseName="ns=di;ParameterSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plcopen;i=1037",
                browseName="ns=di;<ParameterIdentifier>",
                description="A parameter which belongs to the topology element.",
                modellingRule="MandatoryPlaceholder",
            )
        )
    ],
)
o6.reference(plcopen_objtypes.CtrlConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5001"])
di.objtypes.ConfigurableObjectType(
    nodeId="ns=plcopen;i=5004",
    browseName="ns=plcopen;Resources",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            plcopen_objtypes.CtrlResourceType(
                nodeId="ns=plcopen;i=5005",
                browseName="ns=di;<ResourceName>",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent",
                modellingRule="OptionalPlaceholder",
            )
        )
    ],
)
o6.reference(plcopen_objtypes.CtrlConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5004"])
di.objtypes.ConfigurableObjectType(
    nodeId="ns=plcopen;i=5014",
    browseName="ns=plcopen;Tasks",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            plcopen_objtypes.CtrlTaskType(
                nodeId="ns=plcopen;i=5015",
                browseName="ns=di;<TaskName>",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent",
                modellingRule="OptionalPlaceholder",
            )
        )
    ],
)
o6.reference(plcopen_objtypes.CtrlResourceType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5014"])
di.objtypes.ConfigurableObjectType(
    nodeId="ns=plcopen;i=5016",
    browseName="ns=plcopen;Programs",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            plcopen_objtypes.CtrlProgramType(
                nodeId="ns=plcopen;i=5017",
                browseName="ns=di;<ProgramName>",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent",
                modellingRule="OptionalPlaceholder",
                _allow_abstract=True,
            )
        )
    ],
)
o6.reference(plcopen_objtypes.CtrlResourceType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5016"])


ns0.vartypes.PropertyType(
    nodeId="ns=plcopen;i=1031",
    browseName="InputArguments",
    description="the definition of the input argument of method 1:MethodSet.2:Start",
    modellingRule="Mandatory",
    parent="ns=plcopen;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plcopen;i=1032",
    browseName="OutputArguments",
    description="the definition of the output arguments of method 1:MethodSet.2:Start",
    modellingRule="Mandatory",
    parent="ns=plcopen;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[0],
)
o6.call(nodeId="ns=plcopen;i=7001", browseName="ns=plcopen;Start", inputArgs=o6.hasProperty(o6.ns["ns=plcopen;i=1031"]), outputArgs=o6.hasProperty(o6.ns["ns=plcopen;i=1032"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plcopen;i=1034",
    browseName="InputArguments",
    description="the definition of the input argument of method 1:MethodSet.2:Stop",
    modellingRule="Mandatory",
    parent="ns=plcopen;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plcopen;i=1035",
    browseName="OutputArguments",
    description="the definition of the output arguments of method 1:MethodSet.2:Stop",
    modellingRule="Mandatory",
    parent="ns=plcopen;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[0],
)
o6.call(nodeId="ns=plcopen;i=7002", browseName="ns=plcopen;Stop", inputArgs=o6.hasProperty(o6.ns["ns=plcopen;i=1034"]), outputArgs=o6.hasProperty(o6.ns["ns=plcopen;i=1035"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=plcopen;i=5002",
    browseName="ns=di;MethodSet",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=plcopen;i=7001"]), o6.hasComponent(o6.ns["ns=plcopen;i=7002"])],
)
o6.reference(plcopen_objtypes.CtrlConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5002"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=plcopen;i=5012",
    browseName="ns=plcopen;MethodSet",
    description="Flat list of Methods",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=plcopen;i=7003", browseName="ns=plcopen;Start")),
        o6.hasComponent(o6.call(nodeId="ns=plcopen;i=7004", browseName="ns=plcopen;Stop")),
    ],
)
o6.reference(plcopen_objtypes.CtrlResourceType, ns0.reftypes.HasComponent, o6.ns["ns=plcopen;i=5012"])
httpColonSlashSlashPLCopenDotOrgSlashOpcUaSlashIEC61131Minus3Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plcopen;i=15001",
    browseName="ns=plcopen;http://PLCopen.org/OpcUa/IEC61131-3/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15002", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://PLCopen.org/OpcUa/IEC61131-3/"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15003",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.02",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15004",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2020-11-25T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15005",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15006",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15007",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                value="1:65535",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plcopen;i=15008",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=15031", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=15032", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=15033", browseName="DefaultAccessRestrictions", dataType=o6.UInt16)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plcopen_reftypes, plcopen_datypes, plcopen_objtypes
