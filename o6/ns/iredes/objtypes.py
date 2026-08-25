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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=iredes;i=1003", browseName="ns=iredes;ProjectInfoType", displayName="ProjectInfoType")
class ProjectInfoType(ns0.objtypes.BaseObjectType):
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6016", browseName="ns=iredes;Comment", description="Comments concerning the project can be added here.", dataType=o6.String, accessLevel=3
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6014",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("ProjectInfo"),
            accessLevel=3,
        )
    )
    signature: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6015", browseName="ns=iredes;Signature", description="Project signature.", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1006", browseName="ns=iredes;EquipmentInfoType", displayName="EquipmentInfoType")
class EquipmentInfoType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6017",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("EquipmentInfo"),
            accessLevel=3,
        )
    )
    eqpInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6023", browseName="ns=iredes;EqpInfo", description="Other equipment specific information. Free text.", dataType=o6.String, accessLevel=3
        )
    )
    eqpManufact: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6018", browseName="ns=iredes;EqpManufact", description="Name of the manufacturer.", dataType=o6.String)
    )
    eqpModel: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6020",
            browseName="ns=iredes;EqpModel",
            description="Equipment model describing the model in the specified EqpType. To be stated if required for unequivocal machine type identification.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    eqpName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6024", browseName="ns=iredes;EqpName", description="Used for designation of the machine.", dataType=o6.String, accessLevel=3
        )
    )
    eqpSerNo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6021", browseName="ns=iredes;EqpSerNo", description="Serial number of the machine.", dataType=o6.String, accessLevel=3)
    )
    eqpSysVer: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6022", browseName="ns=iredes;EqpSysVer", description="Version Info Automation System / Software.", dataType=o6.String, accessLevel=3
        )
    )
    eqpType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6019", browseName="ns=iredes;EqpType", description="Manufacturer internal type name of the machine.", dataType=o6.String)
    )


@o6.objecttype(nodeId="ns=iredes;i=1009", browseName="ns=iredes;GenHeadType", displayName="GenHeadType")
class GenHeadType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6025",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("GenHead"),
            accessLevel=3,
        )
    )
    downCompat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6028",
            browseName="ns=iredes;DownCompat",
            description="Downward compatibility of the profile version stated in “version” can be guaranteed down to the version number stated in this attribute. Fixed 2.0.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    equipmentInfo: EquipmentInfoType | None
    fileCreateDate: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6026",
            browseName="ns=iredes;FileCreateDate",
            description="Date of file creation. This is the date/time stamp for initialization of the Data Set.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    iRVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6027",
            browseName="ns=iredes;IRVersion",
            description="Version of the IREDES main components of the standard. This version number changes any time IREDES top level schemas are modified. Please note to state downward compatibility in the separate Attribute. Type definition see below. Fixed 2.0.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    projectInfo: ProjectInfoType | None = o6.hasAddIn(
        ProjectInfoType(nodeId="ns=iredes;i=5007", browseName="ns=iredes;ProjectInfo", description="Project specific information. Type definition see below.")
    )


@o6.objecttype(nodeId="ns=iredes;i=1004", browseName="ns=iredes;DisplayToOperatorType", displayName="DisplayToOperatorType")
class DisplayToOperatorType(ns0.objtypes.BaseObjectType):
    ackFlag: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6030",
            browseName="ns=iredes;AckFlag",
            description="Acknowledgement by the operator that he has read the message. (Will be transferred back as soon as the SiteHead is returned to the mine’s computer system with the next protocol exchange. Contains the name of the operator (user name in the Automation system) or simply ACK if automation system does not work with user logins.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6032",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("DisplayToOperator"),
            accessLevel=3,
        )
    )
    dispFlag: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6029",
            browseName="ns=iredes;DispFlag",
            description="States under which circumstances the line (message) has to be displayed to the operator.",
            dataType=iredes_datypes.DispFlag,
            accessLevel=3,
        )
    )
    dispText: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6031", browseName="ns=iredes;DispText", description="Text to be displayed.", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1008", browseName="ns=iredes;IROptionType", displayName="IROptionType")
class IROptionType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6033",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IROption"),
            accessLevel=3,
        )
    )
    optionSchema: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6034",
            browseName="ns=iredes;OptionSchema",
            description="URI for the schema that will extend the IREDES standard. This schema won’t be processed.",
            dataType=o6.String,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1012", browseName="ns=iredes;SiteHeadType", displayName="SiteHeadType")
class SiteHeadType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6035",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("SiteHead"),
            accessLevel=3,
        )
    )
    displayToOperator: DisplayToOperatorType = o6.hasAddIn(
        DisplayToOperatorType(nodeId="ns=iredes;i=5009", browseName="ns=iredes;DisplayToOperator", description="Object used to display messages to the operator of a machine.")
    )
    siteOption: IROptionType = o6.hasAddIn(
        IROptionType(nodeId="ns=iredes;i=5010", browseName="ns=iredes;SiteOption", description="Object that holds/references information that will not be processed.")
    )


@o6.objecttype(nodeId="ns=iredes;i=1015", browseName="ns=iredes;GenTrailerType", displayName="GenTrailerType")
class GenTrailerType(ns0.objtypes.BaseObjectType):
    chkSum: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6038", browseName="ns=iredes;ChkSum", description="CRC 32 checksum.", dataType=o6.ByteString, accessLevel=3)
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6036",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("GenTrailer"),
            accessLevel=3,
        )
    )
    fileCloseDate: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6037", browseName="ns=iredes;FileCloseDate", description="Date the file was created.", dataType=o6.DateTime, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1005", browseName="ns=iredes;IREDESType", displayName="IREDESType")
class IREDESType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6039",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IREDES"),
            accessLevel=3,
        )
    )
    genHead: GenHeadType
    iRDownwCompat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6044",
            browseName="ns=iredes;IRDownwCompat",
            description="Earliest version the IREDES Base system version stated in IRVersion is downward compatible to. Since this version, only extensions have been made but no changes affecting compatibility issues (data type changes etc).",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    iRVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6043", browseName="ns=iredes;IRVersion", description="IREDES Base version needed to process this scheme.", dataType=o6.String, accessLevel=3
        )
    )
    siteHead: SiteHeadType | None


@o6.objecttype(nodeId="ns=iredes;i=1007", browseName="ns=iredes;OpPerfLogType", displayName="OpPerfLogType")
class OpPerfLogType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6045",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("OpPerfLog"),
            accessLevel=3,
        )
    )
    mworking: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6046", browseName="ns=iredes;Mworking", description="Machine working.", dataType=ns0.datatypes.Duration, accessLevel=3
        )
    )
    turnedOff: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6051",
            browseName="ns=iredes;TurnedOff",
            description="Machine intentionally put in “OFF” state. This state is only counted if the machine is intentionally deactivated by an operator. Observe that a “switch off” while the machine is in “Wait Repair” mode will be counted as “wait repair” until the machine is switched on again.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    waitOperator: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6048",
            browseName="ns=iredes;WaitOperator",
            description="Time the machine waits for operator assistance during the reporting period. See “IREDES Drill Rig profile description” document.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    waitProcess: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6047",
            browseName="ns=iredes;WaitProcess",
            description="Machine waiting for other partners in the process or for process reasons not caused by the machine itself. This may be an (autonomous) machine waiting for access to a shared tramming zone or waiting for access to a dump shaft, a truck to become available etc. See “IREDES Drill Rig profile description” document.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    waitRepair: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6049",
            browseName="ns=iredes;WaitRepair",
            description="Waiting time for repair until the repair is finished and the machine manually is switched on again. See “IREDES Drill Rig profile description” document.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    waitSamples: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6050",
            browseName="ns=iredes;WaitSamples",
            description="Waiting time for external supplies like electric power, network connection for remote control (if not in local operation mode), water, material etc. See “IREDES Drill Rig profile description” document.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1013", browseName="ns=iredes;IRpPerfGenType", displayName="IRpPerfGenType")
class IRpPerfGenType(ns0.objtypes.BaseObjectType):
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6066", browseName="ns=iredes;Comment", description="Project information concerning this log.", dataType=o6.String, accessLevel=3
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6052",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRpPerfGen"),
            accessLevel=3,
        )
    )
    endLogTine: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6065",
            browseName="ns=iredes;EndLogTine",
            description="End of the reporting period. Date and time when the last entry to this xml-set was made.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    iREDES: IREDESType
    opPerfLog: OpPerfLogType | None
    reportId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6063", browseName="ns=iredes;ReportId", description="Report ID code, to uniquely identify this log report.", dataType=o6.String, accessLevel=3
        )
    )
    startLogTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6064",
            browseName="ns=iredes;StartLogTime",
            description="Start of the reporting period. Date and time when the first entry to this xml-set was made.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1017", browseName="ns=iredes;IRplanGenType", displayName="IRplanGenType")
class IRplanGenType(ns0.objtypes.BaseObjectType):
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6075",
            browseName="ns=iredes;Comment",
            description="Comments to the plan for example type of plan, purpose, tools to use.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[8],
            accessLevel=3,
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6067",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRplanGen"),
            accessLevel=3,
        )
    )
    iREDES: IREDESType
    planId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6074",
            browseName="ns=iredes;PlanId",
            description="IREDES internal production plan ID used for reference e.g. by Production Quality data sets basing on a particular production plan.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    planName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6073",
            browseName="ns=iredes;PlanName",
            description="Plan logical name to identify this specific plan to the human user. Useful to help the operator of a machine to logical identify a specific plan.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    project: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6076",
            browseName="ns=iredes;Project",
            description="Project ID code. To identify the target project for this plan.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    workOrder: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6077",
            browseName="ns=iredes;WorkOrder",
            description="Work order ID code. To identify the work order associated with this plan.",
            dataType=o6.String,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1020", browseName="ns=iredes;IRStatusGenType", displayName="IRStatusGenType")
class IRStatusGenType(ns0.objtypes.BaseObjectType):
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6082", browseName="ns=iredes;Comment", description="Project information concerning this log.", dataType=o6.String, accessLevel=3
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6078",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRStatusGen"),
            accessLevel=3,
        )
    )
    endLogTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6081",
            browseName="ns=iredes;EndLogTime",
            description="End of the reporting period. Date and time when the last entry to this xml-set was made.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    iREDES: IREDESType
    operatorId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6083", browseName="ns=iredes;OperatorId", description="Identify the operator of the machine for reference.", dataType=o6.String, accessLevel=3
        )
    )
    reportId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6079", browseName="ns=iredes;ReportId", description="Report ID code, to uniquely identify this log report.", dataType=o6.String, accessLevel=3
        )
    )
    startLogTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6080",
            browseName="ns=iredes;StartLogTime",
            description="Start of the reporting period. Date and time when the first entry to this xml-set was made.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1010", browseName="ns=iredes;IRWorkOrderReplyGenType", displayName="IRWorkOrderReplyGenType")
class IRWorkOrderReplyGenType(ns0.objtypes.BaseObjectType):
    answer: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6085", browseName="ns=iredes;Answer", description="See Answer enumeration.", dataType=iredes_datypes.Answer, accessLevel=3
        )
    )
    condition: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6087",
            browseName="ns=iredes;Condition",
            description='Only for "AcceptedWithCondition" option. Free text field for condition such as "need consumable", etc.',
            dataType=o6.String,
            accessLevel=3,
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.BaseDataVariableType = o6.hasProperty(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6084", browseName="ns=iredes;DefaultInstanceBrowseName", dataType=o6.QualifiedName, accessLevel=3)
    )
    duration: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6086", browseName="ns=iredes;Duration", description="For delayed option only.", dataType=ns0.datatypes.Duration, accessLevel=3
        )
    )
    extra: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6088", browseName="ns=iredes;Extra", dataType=o6.String, valueRank=1, arrayDimensions=[10], accessLevel=3)
    )
    reason: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6089",
            browseName="ns=iredes;Reason",
            description="Place to clarify reasons for delaying or denying the work order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[5],
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1016", browseName="ns=iredes;IRreplyType", displayName="IRreplyType")
class IRreplyType(ns0.objtypes.BaseObjectType):
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6092", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=1, arrayDimensions=[5], accessLevel=3)
    )
    defaultInstanceBrowseName: ns0.vartypes.BaseDataVariableType = o6.hasProperty(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6090", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, accessLevel=3)
    )
    reply: IRWorkOrderReplyGenType


@o6.objecttype(nodeId="ns=iredes;i=1021", browseName="ns=iredes;IRWorkOrderGenType", displayName="IRWorkOrderGenType")
class IRWorkOrderGenType(ns0.objtypes.BaseObjectType):
    assignmentTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6099",
            browseName="ns=iredes;AssignmentTime",
            description="Time the execution of the job is expected to take.",
            dataType=iredes_datypes.JobAssignmentTimeDataType,
            accessLevel=3,
        )
    )
    comment: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6109", browseName="ns=iredes;Comment", dataType=o6.String, valueRank=1, arrayDimensions=[5], accessLevel=3)
    )
    defaultInstanceBrowseName: ns0.vartypes.BaseDataVariableType = o6.hasProperty(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6093", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, accessLevel=3)
    )
    iREDESType: IREDESType
    issuer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6103", browseName="ns=iredes;Issuer", description="ID of the person or institute who issued this work order.", dataType=o6.String, accessLevel=3
        )
    )
    machineId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6104",
            browseName="ns=iredes;MachineId",
            description="Machine assigned to the work.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[10],
            accessLevel=3,
        )
    )
    operatorId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6105",
            browseName="ns=iredes;OperatorId",
            description="Operators assigned to the work.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[10],
            accessLevel=3,
        )
    )
    priorityLevel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6101",
            browseName="ns=iredes;PriorityLevel",
            description="Priority of the workorder. Level from 1 to 10 as 10 representing top priority.",
            dataType=o6.UInt32,
            accessLevel=3,
        )
    )
    reply1: IRreplyType | None
    reply10: IRreplyType | None
    reply2: IRreplyType | None
    reply3: IRreplyType | None
    reply4: IRreplyType | None
    reply5: IRreplyType | None
    reply6: IRreplyType | None
    reply7: IRreplyType | None
    reply8: IRreplyType | None
    reply9: IRreplyType | None
    safetyAdvice: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6106",
            browseName="ns=iredes;SafetyAdvice",
            description="Work order shall be carried out. Schema should be defined separately within the IRoptionType.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[10],
            accessLevel=3,
        )
    )
    specialCondition: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6107",
            browseName="ns=iredes;SpecialCondition",
            description="E.g. electricity will be switched off in some region in mine during operation.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[10],
            accessLevel=3,
        )
    )
    specialTask: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6108",
            browseName="ns=iredes;SpecialTask",
            description="Tasks that are not or hard to describe in workorder.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[10],
            accessLevel=3,
        )
    )
    workOrderContent: IROptionType = o6.hasAddIn(IROptionType(nodeId="ns=iredes;i=5044", browseName="ns=iredes;WorkOrderContent"))
    workOrderId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6102",
            browseName="ns=iredes;WorkOrderId",
            description="Identification of this work order. This ID has nothing to do with the, for example, work plan ID.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    workOrderType: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6100", browseName="ns=iredes;WorkOrderType", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1011", browseName="ns=iredes;IRLTMMonType", displayName="IRLTMMonType")
class IRLTMMonType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6130",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRLTMMon"),
            accessLevel=3,
        )
    )
    genTrailer: GenTrailerType
    iREDES: IREDESType
    lTMMonDownwCompat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6139", browseName="ns=iredes;LTMMonDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)
    )
    lTMMonVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6138", browseName="ns=iredes;LTMMonVersion", description="2.0.", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1014", browseName="ns=iredes;IRLTPlanType", displayName="IRLTPlanType")
class IRLTPlanType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6140",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRLTPlan"),
            accessLevel=3,
        )
    )
    genTrailer: GenTrailerType
    iRplanGen: IRplanGenType
    lTPlanDownwCompat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6156", browseName="ns=iredes;LTPlanDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)
    )
    lTPlanVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6155", browseName="ns=iredes;LTPlanVersion", description="2.0.", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1022", browseName="ns=iredes;LTPPwaitProcType", displayName="LTPPwaitProcType")
class LTPPwaitProcType(ns0.objtypes.BaseObjectType):
    blastDelay: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6158", browseName="ns=iredes;BlastDelay", description="Any Delay caused by blasting operations.", dataType=o6.DateTime, accessLevel=3
        )
    )
    cantDump: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6159",
            browseName="ns=iredes;CantDump",
            description="Dump point blocked by another machine, boulders or dump shaft filled / truck missing.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6157",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LTPPwaitProc"),
            accessLevel=3,
        )
    )
    mineUtils: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6162", browseName="ns=iredes;MineUtils", description="Waiting for mine utilities.", dataType=o6.DateTime, accessLevel=3
        )
    )
    noRock: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6161",
            browseName="ns=iredes;NoRock",
            description="Wait for material to handle - No access to material to load.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    roadMaint: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6164", browseName="ns=iredes;RoadMaint", description="Waiting for roadway maintenance.", dataType=o6.DateTime, accessLevel=3
        )
    )
    traffic: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6160",
            browseName="ns=iredes;Traffic",
            description="Traffic caused delays: roadway blocked by another machine / cars / other traffic.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1025", browseName="ns=iredes;LTPPTimeRepType", displayName="LTPPTimeRepType")
class LTPPTimeRepType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6165",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LTPPTimeRep"),
            accessLevel=3,
        )
    )
    lTPPEndTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6167", browseName="ns=iredes;LTPPEndTime", description="Mission end time.", dataType=ns0.datatypes.UtcTime, accessLevel=3)
    )
    lTPPStartTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6166", browseName="ns=iredes;LTPPStartTime", description="Mission start time.", dataType=ns0.datatypes.UtcTime, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1028", browseName="ns=iredes;LTPPMissionType", displayName="LTPPMissionType")
class LTPPMissionType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6168",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LTPPMission"),
            accessLevel=3,
        )
    )
    lTPPMaction: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6180",
            browseName="ns=iredes;LTPPMaction",
            description="Action to be carried out at destination point specified in LTPPMptTo.",
            dataType=iredes_datypes.LTPPMaction,
            accessLevel=3,
        )
    )
    lTPPMarea: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6176",
            browseName="ns=iredes;LTPPMarea",
            description="ID for the mine area the machine is operating in. Usually both departure and destination points should be located in this area.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPMisSeq: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6169",
            browseName="ns=iredes;LTPPMisSeq",
            description="Sequence number of the mission. Starting at 1 with the first mission in the reporting period.",
            dataType=o6.UInt64,
            accessLevel=3,
        )
    )
    lTPPMissEnd: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6178",
            browseName="ns=iredes;LTPPMissEnd",
            description="End time of the mission. Counting ends when the machine is ready to start the next mission, including all waiting before the next mission can be started.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    lTPPMisstart: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6177", browseName="ns=iredes;LTPPMisstart", description="Time tag when the mission started.", dataType=o6.DateTime, accessLevel=3
        )
    )
    lTPPMopID: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=iredes;i=6186", browseName="ns=iredes;LTPPMopID", description="Operator ID.", dataType=o6.String, accessLevel=3)
    )
    lTPPMpayld: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6183",
            browseName="ns=iredes;LTPPMpayld",
            description="Tonnage of payload carried between start and destination points.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPMptFromID: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6172",
            browseName="ns=iredes;LTPPMptFromID",
            description="Electronic (Tag) ID of the point where the mission originated (tramming started). Electronic ID of the point stated in LTPPMptFromN.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPMptFromN: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6170",
            browseName="ns=iredes;LTPPMptFromN",
            description="Name of the point where the mission originated (tramming started).",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPMptFromType: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6171",
            browseName="ns=iredes;LTPPMptFromType",
            description="Type of the point where the mission started.",
            dataType=iredes_datypes.LTPPMptFromType,
            accessLevel=3,
        )
    )
    lTPPMptToID: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6174",
            browseName="ns=iredes;LTPPMptToID",
            description="Electronic (tag) ID of the point where the mission ended (destination point).",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPMptToN: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6173",
            browseName="ns=iredes;LTPPMptToN",
            description="Name of the destination point, where the tramming finished and the mission ended.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPMptToType: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6175",
            browseName="ns=iredes;LTPPMptToType",
            description="Type of the point where the mission ended.",
            dataType=iredes_datypes.LTPPMptToType,
            accessLevel=3,
        )
    )
    lTPPMtimeAct: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6182",
            browseName="ns=iredes;LTPPMtimeAct",
            description="Duration of the action carried out at the destination point in LTPPMaction.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    lTPPMtramDist: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6185",
            browseName="ns=iredes;LTPPMtramDist",
            description="Tramming distance between start and destination point. Unit: km; Resolution: 0.0001 km (10 cm).",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPMtramEnd: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6184",
            browseName="ns=iredes;LTPPMtramEnd",
            description="Tramming end time: Time stamp when the tramming ended at destination point.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )
    lTPPMwaitPoint: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6179", browseName="ns=iredes;LTPPMwaitPoint", description="Waiting time for destination point availability.", dataType=o6.DateTime, accessLevel=3
        )
    )
    lTPPMwaitgen: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6181",
            browseName="ns=iredes;LTPPMwaitgen",
            description="Accumulated waiting time during the mission, excluding the time reported in LTPPMwaitPoint.",
            dataType=o6.DateTime,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1018", browseName="ns=iredes;LTPPaccPtsType", displayName="LTPPaccPtsType")
class LTPPaccPtsType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6187",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LTPPaccPts"),
            accessLevel=3,
        )
    )
    lTPPLcycl: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6193",
            browseName="ns=iredes;LTPPLcycl",
            description="Number of cycles travelled between this point pair during reporting period.",
            dataType=o6.UInt16,
            accessLevel=3,
        )
    )
    lTPPLdist: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6194",
            browseName="ns=iredes;LTPPLdist",
            description="Distance travelled between those two points during reporting period. Accumulated distance of al rounds travelled. Both routes are counted! Accuracy: 0.01 km.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPLdrawPtID: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6189",
            browseName="ns=iredes;LTPPLdrawPtID",
            description="Electronic (tag) ID of the draw (load point) in this combination (Name in 1.1.1.1).",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPLdrawPtN: ns0.vartypes.BaseDataVariableType = o6.hasProperty(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6188",
            browseName="ns=iredes;LTPPLdrawPtN",
            description="Name of the draw (load point) accessed in the reported job.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPLdumpPtID: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6191",
            browseName="ns=iredes;LTPPLdumpPtID",
            description="Electronic (tag) ID of the draw (load point) in this combination (Name in 1.1.1.1).",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPLdumpPtN: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6190", browseName="ns=iredes;LTPPLdumpPtN", description="Name of the dump point in this combination.", dataType=o6.String, accessLevel=3
        )
    )
    lTPPLmass: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6192",
            browseName="ns=iredes;LTPPLmass",
            description="Mass transported between this point pair during reporting period in t. Min accuracy: 0.01 t.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPLopObserv: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6000",
            browseName="ns=iredes;LTPPLopObserv",
            description="Operator observations regarding the travel way, load or dump points during reporting period (e.g. loose rock, bad roadway,...). Preliminarily a string, later we can add preselect-lists for easier operator input!",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    lTPPTimeRep: LTPPTimeRepType | None


@o6.objecttype(nodeId="ns=iredes;i=1019", browseName="ns=iredes;LTPPLoadRepType", displayName="LTPPLoadRepType")
class LTPPLoadRepType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6197",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LTPPLoadRep"),
            accessLevel=3,
        )
    )
    lTPPCyclTot: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6198",
            browseName="ns=iredes;LTPPCyclTot",
            description="Total number of working cycles (rounds) completed during the reporting period.",
            dataType=o6.UInt64,
            accessLevel=3,
        )
    )
    lTPPMission: LTPPMissionType | None
    lTPPaccPts: LTPPaccPtsType | None
    lTPPdistTot: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6199",
            browseName="ns=iredes;LTPPdistTot",
            description="Overall distance travelled in during the reporting period. This includes also non-performance related tramming e.g. to workshop. Minimum accuracy required by the standard: 0.1 km.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPloadTot: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6201",
            browseName="ns=iredes;LTPPloadTot",
            description="Total load carried under all completed working cycles during reporting period. Minimum accuracy required by the standard: 0.01.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )
    lTPPwaitProc: LTPPwaitProcType | None = o6.hasAddIn(
        LTPPwaitProcType(
            nodeId="ns=iredes;i=5055",
            browseName="ns=iredes;LTPPwaitProc",
            description="Process caused waiting time - LHD specific! Specifies details of the WaitProc timing in the Application Profile!",
        )
    )
    lTPPwrkDist: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=iredes;i=6200",
            browseName="ns=iredes;LTPPwrkDist",
            description="Total distance travelled in a working mode (as reported by MWorking) during the reporting period.",
            dataType=o6.Float,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=iredes;i=1026", browseName="ns=iredes;IRLTPPerfType", displayName="IRLTPPerfType")
class IRLTPPerfType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6209",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRLTPPerf"),
            accessLevel=3,
        )
    )
    iRpPerfGen: IRpPerfGenType
    lTPPLoadRep: LTPPLoadRepType
    lTPPerfDownwCompat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6221", browseName="ns=iredes;LTPPerfDownwCompat", description="2.0.", dataType=o6.String, accessLevel=3)
    )
    lTPPerfVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=iredes;i=6220", browseName="ns=iredes;LTPPerfVersion", description="2.0.", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=iredes;i=1030", browseName="ns=iredes;IRLHDTruckType", displayName="IRLHDTruckType")
class IRLHDTruckType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=iredes;i=6222",
            browseName="ns=iredes;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("IRLHDTruck"),
            accessLevel=3,
        )
    )
    iRLTMMon: IRLTMMonType
    iRLTPPerf: IRLTPPerfType
    iRLTPlan: IRLTPlanType


del Any, TYPE_CHECKING, uuid, o6, ns0, iredes_datypes
