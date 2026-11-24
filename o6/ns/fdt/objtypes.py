# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA fdt namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as fdt_reftypes
from . import datatypes as fdt_datypes
from . import vartypes as fdt_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=fdt;i=1008", browseName="ns=fdt;FdtStartMethodEventType", displayName="FdtStartMethodEventType")
class FdtStartMethodEventType(ns0.objtypes.AuditUpdateMethodEventType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1012", browseName="ns=fdt;FdtAuditEventType", displayName="FdtAuditEventType")
class FdtAuditEventType(ns0.objtypes.AuditEventType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1016", browseName="ns=fdt;IFdtSupportInfoType", displayName="IFdtSupportInfoType", isAbstract=True)
class IFdtSupportInfoType(di.objtypes.ISupportInfoType):
    documentation: ns0.objtypes.FolderType | None
    protocolSupport: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=fdt;i=1031", browseName="ns=fdt;HartFskConnectionPoint", displayName="HartFskConnectionPoint")
class HartFskConnectionPoint(di.objtypes.ConnectionPointType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1032", browseName="ns=fdt;ProfibusDpv1ConnectionPoint", displayName="ProfibusDpv1ConnectionPoint")
class ProfibusDpv1ConnectionPoint(di.objtypes.ConnectionPointType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1045", browseName="ns=fdt;ModbusSLConnectionPoint", displayName="ModbusSLConnectionPoint")
class ModbusSLConnectionPoint(di.objtypes.ConnectionPointType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1046", browseName="ns=fdt;ModbusTCPConnectionPoint", displayName="ModbusTCPConnectionPoint")
class ModbusTCPConnectionPoint(di.objtypes.ConnectionPointType):
    pass


@o6.objecttype(nodeId="ns=fdt;i=1013", browseName="ns=fdt;FdtTransferServiceType", displayName="FdtTransferServiceType")
class FdtTransferServiceType(di.objtypes.TransferServicesType):
    supportedTransfer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6005", browseName="ns=fdt;SupportedTransfer", modellingRule="Mandatory", dataType=fdt_datypes.SupportedTransfer, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(
    nodeId="ns=fdt;i=1001",
    browseName="ns=fdt;FdtProtocolType",
    displayName="FdtProtocolType",
    description="This type is used to specify which protocols an FdtDeviceType requires or supports.",
    isAbstract=True,
)
class FdtProtocolType(di.objtypes.ProtocolType):
    busCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6012", browseName="ns=fdt;BusCategory", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fdt;i=1004", browseName="ns=fdt;FdtDocumentType", displayName="FdtDocumentType", isAbstract=True)
class FdtDocumentType(ns0.objtypes.BaseObjectType):
    classification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6018", browseName="ns=fdt;Classification", modellingRule="Mandatory", dataType=fdt_datypes.DocumentClassification, accessLevel=3, userAccessLevel=1
        )
    )
    help: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6019", browseName="ns=fdt;Help", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    language: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6022", browseName="ns=fdt;Language", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    mediaType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6023", browseName="ns=fdt;MediaType", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    semanticInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6025", browseName="ns=fdt;SemanticInfo", modellingRule="Optional", dataType=fdt_datypes.SemanticInfoType, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=fdt;i=1005", browseName="ns=fdt;FdtDocumentFile", displayName="FdtDocumentFile")
class FdtDocumentFile(FdtDocumentType):
    file: ns0.objtypes.FileType


@o6.objecttype(nodeId="ns=fdt;i=1006", browseName="ns=fdt;FdtDocumentUrl", displayName="FdtDocumentUrl")
class FdtDocumentUrl(FdtDocumentType):
    uRL: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6051", browseName="ns=fdt;URL", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fdt;i=1014", browseName="ns=fdt;FdtFunctionalGroupType", displayName="FdtFunctionalGroupType")
class FdtFunctionalGroupType(di.objtypes.FunctionalGroupType):
    applicationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6052", browseName="ns=fdt;ApplicationId", modellingRule="Optional", dataType=fdt_datypes.ApplicationIdEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    semanticInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6028", browseName="ns=fdt;SemanticInfo", modellingRule="Optional", dataType=fdt_datypes.SemanticInfoType, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=fdt;i=1007", browseName="ns=fdt;FdtAuditWriteUpdateEventType", displayName="FdtAuditWriteUpdateEventType")
class FdtAuditWriteUpdateEventType(ns0.objtypes.AuditWriteUpdateEventType):
    newUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6062", browseName="ns=fdt;NewUnit", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    oldUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6061", browseName="ns=fdt;OldUnit", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fdt;i=1017", browseName="ns=fdt;IFdtDeviceHealthType", displayName="IFdtDeviceHealthType", isAbstract=True)
class IFdtDeviceHealthType(di.objtypes.IDeviceHealthType):
    deviceHealth: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fdt;i=6066", browseName="ns=di;DeviceHealth", modellingRule="Mandatory", dataType=di.datatypes.DeviceHealthEnumeration)
    )


@o6.objecttype(
    nodeId="ns=fdt;i=1015",
    browseName="ns=fdt;FdtIoSignalInfoType",
    displayName="FdtIoSignalInfoType",
    description="This type is used to provide information about the IO signals available at the device.",
)
class FdtIoSignalInfoType(ns0.objtypes.BaseObjectType):
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6056", browseName="ns=fdt;Description", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    frameApplicationTag: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6057", browseName="ns=fdt;FrameApplicationTag", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    hasAlarmInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6011", browseName="ns=fdt;HasAlarmInfo", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    hasDeviceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6014", browseName="ns=fdt;HasDeviceData", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    hasRange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6016", browseName="ns=fdt;HasRange", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    hasSubstituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6024", browseName="ns=fdt;HasSubstituteValue", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    hasUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6045", browseName="ns=fdt;HasUnit", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1)
    )
    iECDatatype: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6059", browseName="ns=fdt;IECDatatype", modellingRule="Mandatory", dataType=fdt_datypes.IECDatatype, accessLevel=3, userAccessLevel=1
        )
    )
    isLocked: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6060", browseName="ns=fdt;IsLocked", modellingRule="Mandatory", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    isSafety: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6063", browseName="ns=fdt;IsSafety", modellingRule="Mandatory", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    routedIoSignalId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6064", browseName="ns=fdt;RoutedIoSignalId", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    semanticInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6026", browseName="ns=fdt;SemanticInfo", modellingRule="Optional", dataType=fdt_datypes.SemanticInfoType, accessLevel=3, userAccessLevel=1
        )
    )
    signalType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6069", browseName="ns=fdt;SignalType", modellingRule="Mandatory", dataType=fdt_datypes.SignalTypeEnumeration, accessLevel=3, userAccessLevel=1
        )
    )


o6.reference(fdt_vartypes.FdtParameter, "ns=fdt;i=4002", FdtIoSignalInfoType)


@o6.objecttype(nodeId="ns=fdt;i=1010", browseName="ns=fdt;FdtEndMethodEventType", displayName="FdtEndMethodEventType")
class FdtEndMethodEventType(ns0.objtypes.AuditUpdateMethodEventType):
    result: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6081", browseName="ns=fdt;Result", modellingRule="Mandatory", dataType=fdt_datypes.FunctionExecutionResultState, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=fdt;i=1019", browseName="ns=fdt;FdtDeviceType", displayName="FdtDeviceType", isAbstract=True, interfaces=[IFdtSupportInfoType, IFdtDeviceHealthType])
class FdtDeviceType(di.objtypes.DeviceType):
    deviceHealth: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fdt;i=6065", browseName="ns=fdt;DeviceHealth", modellingRule="Mandatory", dataType=di.datatypes.DeviceHealthEnumeration)
    )
    deviceTag: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6132", browseName="ns=fdt;DeviceTag", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    deviceTypeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6131", browseName="ns=fdt;DeviceTypeId", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    documentation: ns0.objtypes.FolderType | None
    identification: di.objtypes.FunctionalGroupType = o6.hasComponent(
        di.objtypes.FunctionalGroupType(
            nodeId="ns=fdt;i=5462",
            browseName="ns=di;Identification",
            description="Used to organize parameters for identification of this TopologyElement",
            modellingRule="Mandatory",
        )
    )
    manufacturerId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6232", browseName="ns=fdt;ManufacturerId", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    methodSet: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=fdt;i=5466", browseName="ns=di;MethodSet", description="Flat list of Methods", modellingRule="Mandatory")
    )
    parameterSet: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=fdt;i=5467", browseName="ns=di;ParameterSet", description="Flat list of Parameters", modellingRule="Mandatory")
    )
    protocolSupport: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=fdt;i=1003", browseName="ns=fdt;FdtDataType", displayName="FdtDataType", description="Generic FDT data type base class")
class FdtDataType(di.objtypes.ConfigurableObjectType):
    clone: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=fdt;i=7008",
            browseName="ns=fdt;Clone",
            description="Creates a new object that is a deep-copy of the current instance. All objects are duplicated - the top-level objects are duplicated as well as all the lower levels. The cloned object can be modified without affecting the original object.",
            modellingRule="Mandatory",
        )
    )
    verify: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=fdt;i=7009",
            browseName="ns=fdt;Verify",
            description="Verifies that all properties are valid (e.g. mandatory properties have a value).",
            modellingRule="Mandatory",
        )
    )


@o6.objecttype(
    nodeId="ns=fdt;i=1009",
    browseName="ns=fdt;RegularExpression",
    displayName="RegularExpression",
    description="Regular expression that defines which physical device types are supported by a DTM Device Type.",
)
class RegularExpression(FdtDataType):
    text: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fdt;i=6027",
            browseName="ns=fdt;Text",
            description="Regular expression text.",
            modellingRule="Mandatory",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=fdt;i=1011", browseName="ns=fdt;FdtList", displayName="FdtList", description="Generic list of FdtDatatype<T>s, which can be cloned.")
class FdtList(FdtDataType):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdt_reftypes, fdt_datypes, fdt_vartypes
