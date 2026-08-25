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

"""Generated OPC UA pngsdgm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pngsdgm_reftypes
from . import datatypes as pngsdgm_datypes
from . import vartypes as pngsdgm_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=pngsdgm;i=1002", browseName="ns=pngsdgm;GsdGenAlarmEventType", displayName="GsdGenAlarmEventType")
class GsdGenAlarmEventType(ns0.objtypes.BaseEventType):
    aPI: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6022", browseName="ns=pngsdgm;API", dataType=o6.UInt32))
    accumulative: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6026", browseName="ns=pngsdgm;Accumulative", dataType=pngsdgm_datypes.GsdGenChannelAccumulativeEnumeration)
    )
    channelErrorType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6031", browseName="ns=pngsdgm;ChannelErrorType", dataType=o6.UInt16)
    )
    channelNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6025", browseName="ns=pngsdgm;ChannelNumber", dataType=o6.UInt16)
    )
    direction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6029", browseName="ns=pngsdgm;Direction", dataType=pngsdgm_datypes.GsdGenChannelDirectionEnumeration)
    )
    extChannelAddValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6033", browseName="ns=pngsdgm;ExtChannelAddValue", dataType=o6.UInt32)
    )
    extChannelErrorType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6032", browseName="ns=pngsdgm;ExtChannelErrorType", dataType=o6.UInt16)
    )
    helpText: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6036", browseName="ns=pngsdgm;HelpText", dataType=o6.LocalizedText))
    maintenance: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6027", browseName="ns=pngsdgm;Maintenance", dataType=pngsdgm_datypes.GsdGenChannelMaintenanceEnumeration)
    )
    manufacturerData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6035", browseName="ns=pngsdgm;ManufacturerData", dataType=o6.ByteString)
    )
    qualifiedChannelQualifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6034", browseName="ns=pngsdgm;QualifiedChannelQualifier", dataType=o6.UInt32)
    )
    slot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6023", browseName="ns=pngsdgm;Slot", dataType=o6.UInt16))
    specifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6028", browseName="ns=pngsdgm;Specifier", dataType=pngsdgm_datypes.GsdGenChannelSpecifierEnumeration)
    )
    subslot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6024", browseName="ns=pngsdgm;Subslot", dataType=o6.UInt16))
    userStructureIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6030", browseName="ns=pngsdgm;UserStructureIdentifier", dataType=o6.UInt16)
    )


@o6.objecttype(nodeId="ns=pngsdgm;i=1003", browseName="ns=pngsdgm;GsdGenIoChannelQualityType", displayName="GsdGenIoChannelQualityType")
class GsdGenIoChannelQualityType(ns0.objtypes.BaseObjectType):
    bitOffset: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6037", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16))
    format: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6038", browseName="ns=pngsdgm;Format", dataType=pngsdgm_datypes.GsdGenIoQualityFormatEnumeration)
    )


@o6.objecttype(nodeId="ns=pngsdgm;i=1004", browseName="ns=pngsdgm;GsdGenIoChannelDataType", displayName="GsdGenIoChannelDataType")
class GsdGenIoChannelDataType(ns0.objtypes.BaseObjectType):
    bitLength: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6040", browseName="ns=pngsdgm;BitLength", dataType=o6.UInt16))
    bitOffset: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6039", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=pngsdgm;i=1005", browseName="ns=pngsdgm;GsdGenIoChannelType", displayName="GsdGenIoChannelType")
class GsdGenIoChannelType(ns0.objtypes.BaseObjectType):
    data: GsdGenIoChannelDataType
    number: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6041", browseName="ns=pngsdgm;Number", dataType=o6.UInt16))
    quality: GsdGenIoChannelQualityType | None


@o6.objecttype(nodeId="ns=pngsdgm;i=1006", browseName="ns=pngsdgm;GsdGenIoDataType", displayName="GsdGenIoDataType")
class GsdGenIoDataType(ns0.objtypes.BaseObjectType):
    consistency: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6046", browseName="ns=pngsdgm;Consistency", dataType=pngsdgm_datypes.GsdGenIoConsistencyEnumeration)
    )
    langleDataItemxRangle: pngsdgm_vartypes.GsdGenIoDataItemVariableType | None
    langleInputChannelxRangle: GsdGenIoChannelType | None
    langleOutputChannelxRangle: GsdGenIoChannelType | None


ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6074",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationTag", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=pngsdgm;i=7001", browseName="ns=pngsdgm;SetApplicationTag", inputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6074"]))


@o6.objecttype(nodeId="ns=pngsdgm;i=1007", browseName="ns=pngsdgm;GsdGenSubmoduleApplicationType", displayName="GsdGenSubmoduleApplicationType")
class GsdGenSubmoduleApplicationType(ns0.objtypes.BaseObjectType):
    aRIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6106", browseName="ns=pngsdgm;ARIdentifier", dataType=o6.Guid))
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6006", browseName="ns=pngsdgm;ApplicationTag", dataType=o6.String)
    )
    communicationStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6104", browseName="ns=pngsdgm;CommunicationStatus", dataType=pngsdgm_datypes.GsdGenIoCommunicationStatusEnumeration)
    )
    configuration: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=pngsdgm;i=5015", browseName="ns=pngsdgm;Configuration"))
    configurationStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6105", browseName="ns=pngsdgm;ConfigurationStatus", dataType=pngsdgm_datypes.GsdGenIoConfigurationStatusEnumeration)
    )
    controllerName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6107", browseName="ns=pngsdgm;ControllerName", dataType=o6.String)
    )
    input: GsdGenIoDataType | None
    langleArrayFolderRangle: di.objtypes.FunctionalGroupType | None
    langleEnumerationVariableRangle: ns0.vartypes.BaseDataVariableType | None
    langleFolderNameRangle: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=pngsdgm;i=5016", browseName="ns=pngsdgm;<FolderName>", modellingRule="OptionalPlaceholder")
    )
    langleOptionSetVariableRangle: ns0.vartypes.OptionSetType | None
    langleUnitRangeVariableRangle: ns0.vartypes.AnalogUnitRangeType | None
    langleUnitVariableRangle: ns0.vartypes.AnalogUnitType | None
    langleValuePropertyRangle: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6058", browseName="ns=pngsdgm;<ValueProperty>", modellingRule="OptionalPlaceholder", valueRank=-3)
    )
    langleValueVariableRangle: ns0.vartypes.BaseDataVariableType | None
    lock: di.objtypes.LockingServicesType | None
    output: GsdGenIoDataType | None
    setApplicationTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pngsdgm;i=7001"])


o6.reference(GsdGenSubmoduleApplicationType, "i=41", GsdGenAlarmEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pngsdgm_reftypes, pngsdgm_datypes, pngsdgm_vartypes
