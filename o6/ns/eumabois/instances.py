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

"""Generated OPC UA eumabois namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
import o6.ns.woodworking as woodworking

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.BaseObjectType(nodeId="ns=eumabois;i=5040", browseName="ns=woodworking;Values", description="The Values Object provides the counters of the unit.")
o6.reference(o6.ns["ns=eumabois;i=5040"], "i=17603", "ns=woodworking;i=1006")
ns0.objtypes.FolderType(
    nodeId="ns=eumabois;i=5007",
    browseName="ns=woodworking;ManufacturerSpecific",
    description="The ManufacturerSpecific Object provides manufacturer specific functionality.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6020", browseName="ns=woodworking;LastProgramName", dataType=o6.String, value="P46", accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=eumabois;i=5001",
    browseName="ns=di;Identification",
    description="The Identification Object provides identification information of the machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6001",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
                value="Edgebander",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6002",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("EUMABOIS"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6003",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("Edgebander EB739"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6004",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
                value="https://www.eumabois.com/0-237-24-2749",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6005",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
                value="0-237-24-2749",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6006",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
                value=2021,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6007",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="Hall 3, Machine 039",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6008",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("Machine 039"),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6009",
                browseName="ns=woodworking;LocationPlant",
                description="The LocationPlant provides the location of the plant.",
                dataType=o6.String,
                value="Hannover",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6010",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
                value="01.33",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6011",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
                value=o6.DateTime("2021-01-27T01:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6012",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                value="Hall 3 / Place 247",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6015",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
                value="https://www.eumabois.com/",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6016",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
                value=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6017",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
                value="11182372",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6018",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
                value="2.2.38.1",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6022",
                browseName="ns=woodworking;CustomerCompanyName",
                description="The CustomerCompanyName provides the customer name of the Woodworking manufacturer.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(";Name of furniture manufacturer&gt;"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6023",
                browseName="ns=woodworking;LocationGPS",
                description='The LocationGPS provides the location of the plant in GPS coordinates. The format is decimal degrees with north and east coordinates. For example, Hannover Messe has "52.3235858255059, 9.804918108600956".\nSouthern latitudes have a negative value, western longitudes as well. For example, Quito has the coordinates “-0.21975073282167099, -78.51255572531042”.',
                dataType=o6.String,
                value="52.3235858255059, 9.804918108600956",
            )
        ),
    ],
)
gluingUnit = ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5011",
    browseName="ns=eumabois;GluingUnit",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6065", browseName="ns=eumabois;GlueTemperature", description="Temperature of gluing aggregate in °C", dataType=o6.UInt32, value=173
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6066", browseName="ns=eumabois;TemperaturePreselection", dataType=o6.UInt32, value=180, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=eumabois;i=5005",
    browseName="ns=woodworking;ManufacturerSpecific",
    description="The ManufacturerSpecific Object provides manufacturer specific functionality.",
    references=[
        o6.organizes(gluingUnit),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6019", browseName="ns=woodworking;LastProgramName", dataType=o6.String, value="P08", accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5016",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6101",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6102", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6103",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6104",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6105",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6106",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6107",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6109",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6113",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6114",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6116",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6117", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6118",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6120",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6121",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6122",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6123", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6124",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5016"], "i=17603", "ns=woodworking;i=4")
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashEumaboisSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=eumabois;i=5030",
    browseName="ns=eumabois;http://opcfoundation.org/UA/Eumabois/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6108", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6110", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-01-27T00:14:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6111", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Eumabois/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6112", browseName="NamespaceVersion", dataType=o6.String, value="0.14")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6115", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6119", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6126", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5017",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6125",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking.datatypes.WwUnitModeEnumeration,
                value=woodworking.datatypes.WwUnitModeEnumeration.AUTOMATIC,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6127",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking.datatypes.WwUnitStateEnumeration,
                value=woodworking.datatypes.WwUnitStateEnumeration.WORKING,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5017"], "i=17603", "ns=woodworking;i=5")
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=eumabois;i=5015",
    browseName="ns=di;Identification",
    description="The Identification Object provides identification information of the machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6013",
                browseName="ns=woodworking;LocationPlant",
                description="The LocationPlant provides the location of the plant.",
                dataType=o6.String,
                value="Hannover",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6014",
                browseName="ns=woodworking;CustomerCompanyName",
                description="The CustomerCompanyName provides the customer name of the Woodworking manufacturer.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(";Name of furniture manufacturer&gt;"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6021",
                browseName="ns=woodworking;LocationGPS",
                description='The LocationGPS provides the location of the plant in GPS coordinates. The format is decimal degrees with north and east coordinates. For example, Hannover Messe has "52.3235858255059, 9.804918108600956".\nSouthern latitudes have a negative value, western longitudes as well. For example, Quito has the coordinates “-0.21975073282167099, -78.51255572531042”.',
                dataType=o6.String,
                value="52.3235858255059, 9.804918108600956",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6131",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="Hall 1, Machine 074",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6132",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("Machine 074"),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6134",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
                value="CNC Working\xa0Centre",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6135",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
                value="01.07",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6136",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
                value=o6.DateTime("2021-01-27T01:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6137",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                value="Hall 1 / Place 083",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6140",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("EUMABOIS"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6141",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
                value="https://www.eumabois.com/",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6142",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("CNC C38"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6143",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
                value=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6144",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
                value="36283537",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6145",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
                value="https://www.eumabois.com/0-219-64-9274",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6146",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
                value="0-219-64-9274",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6147",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
                value="2.1.64.3",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=eumabois;i=6148",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
                value=2021,
            )
        ),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5019",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6099", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6100",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6151",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6152",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6153",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6154",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6155",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6156", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6157",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6160",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6162",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6163",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6164",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6165", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6166",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6167",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6168",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6169",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5019"], "i=17603", "ns=woodworking;i=4")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5020",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6170",
                browseName="ns=woodworking;AxisOverride",
                description="The AxisOverride Variable provides the override for the axis in percent.",
                dataType=o6.UInt32,
                value=100,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6172",
                browseName="ns=woodworking;RelativeErrorTime",
                description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
                dataType=o6.UInt64,
                value=960000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6176",
                browseName="ns=woodworking;RelativeProductionTime",
                description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
                dataType=o6.UInt64,
                value=14610000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6177",
                browseName="ns=woodworking;RelativeRunsAborted",
                description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
                dataType=o6.UInt64,
                value=7,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6178",
                browseName="ns=woodworking;RelativeRunsGood",
                description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
                dataType=o6.UInt64,
                value=14603,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6181",
                browseName="ns=woodworking;RelativeRunsTotal",
                description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
                dataType=o6.UInt64,
                value=14610,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6183",
                browseName="ns=woodworking;RelativeStandbyTime",
                description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
                dataType=o6.UInt64,
                value=720000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6184",
                browseName="ns=woodworking;RelativeWorkingTime",
                description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
                dataType=o6.UInt64,
                value=29220000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6187",
                browseName="ns=woodworking;SpindleOverride",
                description="The SpindleOverride Variable provides the override for the spindle in percent.",
                dataType=o6.UInt32,
                value=100,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6188",
                browseName="ns=woodworking;RelativeReadyTime",
                description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
                dataType=o6.UInt64,
                value=5100000,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5020"], "i=17603", "ns=woodworking;i=1006")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5021",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6129",
                browseName="ns=woodworking;AxisOverride",
                description="The AxisOverride Variable provides the override for the axis in percent.",
                dataType=o6.UInt32,
                value=83,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6130",
                browseName="ns=woodworking;RelativeErrorTime",
                description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
                dataType=o6.UInt64,
                value=960000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6150",
                browseName="ns=woodworking;RelativeProductionTime",
                description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
                dataType=o6.UInt64,
                value=14610000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6159",
                browseName="ns=woodworking;RelativeReadyTime",
                description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
                dataType=o6.UInt64,
                value=5100000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6161",
                browseName="ns=woodworking;RelativeRunsAborted",
                description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
                dataType=o6.UInt64,
                value=7,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6171",
                browseName="ns=woodworking;RelativeRunsGood",
                description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
                dataType=o6.UInt64,
                value=14603,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6173",
                browseName="ns=woodworking;RelativeRunsTotal",
                description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
                dataType=o6.UInt64,
                value=14610,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6191",
                browseName="ns=woodworking;RelativeStandbyTime",
                description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
                dataType=o6.UInt64,
                value=720000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6192",
                browseName="ns=woodworking;RelativeWorkingTime",
                description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
                dataType=o6.UInt64,
                value=29220000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6193",
                browseName="ns=woodworking;SpindleOverride",
                description="The SpindleOverride Variable provides the override for the spindle in percent.",
                dataType=o6.UInt32,
                value=83,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5021"], "i=17603", "ns=woodworking;i=1006")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5014",
    browseName="ns=eumabois;Place_2",
    description="Each <SubUnit> Object represents an instance of a state. For example, a CNC machine can have two places where independent jobs are produced. Then there are two <SubUnit> Objects. They may be named “Place 1” and “Place 2”.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5016"]), o6.hasComponent(o6.ns["ns=eumabois;i=5017"]), o6.hasComponent(o6.ns["ns=eumabois;i=5021"])],
)
o6.reference(o6.ns["ns=eumabois;i=5014"], "i=17603", "ns=woodworking;i=6")
httpsColonSlashSlashWwwDotEumaboisDotCom = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=eumabois;i=5028",
    browseName="ns=eumabois;https://www.eumabois.com",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6128", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6158", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-01-27T00:13:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6190", browseName="NamespaceUri", dataType=o6.String, value="https://www.eumabois.com/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6198", browseName="NamespaceVersion", dataType=o6.String, value="0.13")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6199", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6200", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=eumabois;i=6203", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5035",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6207",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking.datatypes.WwUnitStateEnumeration,
                value=woodworking.datatypes.WwUnitStateEnumeration.WORKING,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6214",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking.datatypes.WwUnitModeEnumeration,
                value=woodworking.datatypes.WwUnitModeEnumeration.AUTOMATIC,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5035"], "i=17603", "ns=woodworking;i=5")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5022",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6174", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6179",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6180",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6182",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6185",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6186",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6189",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6194", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6195",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6196",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6197",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6201",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6202",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6204",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6205",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6206",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6208",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6209", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6210",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6211",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6212",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6213",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6215",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6217",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6218",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6219",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5022"], "i=17603", "ns=woodworking;i=4")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5036",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6216",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking.datatypes.WwUnitStateEnumeration,
                value=woodworking.datatypes.WwUnitStateEnumeration.WORKING,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6225",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking.datatypes.WwUnitModeEnumeration,
                value=woodworking.datatypes.WwUnitModeEnumeration.AUTOMATIC,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5036"], "i=17603", "ns=woodworking;i=5")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5038",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6226",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking.datatypes.WwUnitModeEnumeration,
                value=woodworking.datatypes.WwUnitModeEnumeration.MANUAL,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6227",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking.datatypes.WwUnitStateEnumeration,
                value=woodworking.datatypes.WwUnitStateEnumeration.READY,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5038"], "i=17603", "ns=woodworking;i=5")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5037",
    browseName="ns=eumabois;Place_1",
    description="Each <SubUnit> Object represents an instance of a state. For example, a CNC machine can have two places where independent jobs are produced. Then there are two <SubUnit> Objects. They may be named “Place 1” and “Place 2”.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5019"]), o6.hasComponent(o6.ns["ns=eumabois;i=5020"]), o6.hasComponent(o6.ns["ns=eumabois;i=5038"])],
)
o6.reference(o6.ns["ns=eumabois;i=5037"], "i=17603", "ns=woodworking;i=6")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5034",
    browseName="ns=woodworking;SubUnits",
    description="The SubUnits Object is used when a machine has multiple states. For example, a CNC machine can have several places where independent jobs are produced.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5014"]), o6.hasComponent(o6.ns["ns=eumabois;i=5037"])],
)
o6.reference(o6.ns["ns=eumabois;i=5034"], "i=17603", "ns=woodworking;i=7")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5039",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6228", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6229",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6230",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6231",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6232",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6233",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6234",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6235", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6236",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6237",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6238",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6241",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6243",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6244",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6245", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6246",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6247",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6248",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6249",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6250",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=eumabois;i=6253",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5039"], "i=17603", "ns=woodworking;i=4")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5032",
    browseName="ns=woodworking;Machine",
    description="State of the whole machine.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5036"]), o6.hasComponent(o6.ns["ns=eumabois;i=5039"]), o6.hasComponent(o6.ns["ns=eumabois;i=5040"])],
)
o6.reference(o6.ns["ns=eumabois;i=5032"], "i=17603", "ns=woodworking;i=6")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5018",
    browseName="ns=woodworking;State",
    description="The State Object provides information about the states of the machine.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5032"]), o6.hasComponent(o6.ns["ns=eumabois;i=5034"])],
)
o6.reference(o6.ns["ns=eumabois;i=5018"], "i=17603", "ns=woodworking;i=8")
httpsColonSlashSlashWwwDotEumaboisDotComSlash0Minus219Minus64Minus9274 = woodworking.objtypes.WwMachineType(
    nodeId="ns=eumabois;i=5006",
    browseName="ns=eumabois;https://www.eumabois.com/0-219-64-9274",
    references=[
        o6.hasComponent(o6.ns["ns=eumabois;i=5007"]),
        o6.hasComponent(
            woodworking.objtypes.WwEventsDispatcherType(
                nodeId="ns=eumabois;i=5013", browseName="ns=woodworking;Events", description="The Event Object provides events.", eventNotifier=1
            )
        ),
        o6.hasComponent(o6.ns["ns=eumabois;i=5018"]),
        o6.hasAddIn(o6.ns["ns=eumabois;i=5015"]),
    ],
    parent="ns=machinery;i=1001",
    referenceType=ns0.reftypes.Organizes,
    eventNotifier=1,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5023",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6220",
                browseName="ns=woodworking;ActualCycle",
                description="The ActualCycle Variable provides the parts per minutes.",
                dataType=o6.Double,
                value=30.0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6221",
                browseName="ns=woodworking;FeedSpeed",
                description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
                dataType=o6.Double,
                value=40.0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6222",
                browseName="ns=woodworking;RelativeErrorTime",
                description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
                dataType=o6.UInt64,
                value=960000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6223",
                browseName="ns=woodworking;RelativeLength",
                description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
                dataType=o6.UInt64,
                value=365075,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6224",
                browseName="ns=woodworking;RelativeMachineOnTime",
                description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
                dataType=o6.UInt64,
                value=36000000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6240",
                browseName="ns=woodworking;RelativePiecesIn",
                description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
                dataType=o6.UInt64,
                value=14610,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6242",
                browseName="ns=woodworking;RelativePiecesOut",
                description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
                dataType=o6.UInt64,
                value=14603,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6251",
                browseName="ns=woodworking;RelativePowerPresentTime",
                description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
                dataType=o6.UInt64,
                value=36000000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6252",
                browseName="ns=woodworking;RelativeProductionTime",
                description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
                dataType=o6.UInt64,
                value=14610000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6254",
                browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
                description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
                dataType=o6.UInt64,
                value=1920000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6255",
                browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
                description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
                dataType=o6.UInt64,
                value=14610000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6256",
                browseName="ns=woodworking;RelativeReadyTime",
                description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
                dataType=o6.UInt64,
                value=5100000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6257",
                browseName="ns=woodworking;RelativeRunsAborted",
                description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
                dataType=o6.UInt64,
                value=7,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6258",
                browseName="ns=woodworking;RelativeRunsGood",
                description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
                dataType=o6.UInt64,
                value=14603,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6259",
                browseName="ns=woodworking;RelativeRunsTotal",
                description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
                dataType=o6.UInt64,
                value=14610,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6260",
                browseName="ns=woodworking;RelativeWorkingTime",
                description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
                dataType=o6.UInt64,
                value=29220000,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseAnalogType(
                nodeId="ns=eumabois;i=6261",
                browseName="ns=woodworking;RelativeStandbyTime",
                description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
                dataType=o6.UInt64,
                value=720000,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=eumabois;i=5023"], "i=17603", "ns=woodworking;i=1006")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5031",
    browseName="ns=woodworking;Machine",
    description="State of the whole machine.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5022"]), o6.hasComponent(o6.ns["ns=eumabois;i=5023"]), o6.hasComponent(o6.ns["ns=eumabois;i=5035"])],
)
o6.reference(o6.ns["ns=eumabois;i=5031"], "i=17603", "ns=woodworking;i=6")
ns0.objtypes.BaseObjectType(
    nodeId="ns=eumabois;i=5003",
    browseName="ns=woodworking;State",
    description="The State Object provides information about the states of the machine.",
    references=[o6.hasComponent(o6.ns["ns=eumabois;i=5031"])],
)
o6.reference(o6.ns["ns=eumabois;i=5003"], "i=17603", "ns=woodworking;i=8")
httpsColonSlashSlashWwwDotEumaboisDotComSlash0Minus237Minus24Minus2749 = woodworking.objtypes.WwMachineType(
    nodeId="ns=eumabois;i=5002",
    browseName="ns=eumabois;https://www.eumabois.com/0-237-24-2749",
    references=[
        o6.hasComponent(o6.ns["ns=eumabois;i=5003"]),
        o6.hasComponent(
            woodworking.objtypes.WwEventsDispatcherType(
                nodeId="ns=eumabois;i=5004", browseName="ns=woodworking;Events", description="The Event Object provides events.", eventNotifier=1
            )
        ),
        o6.hasComponent(o6.ns["ns=eumabois;i=5005"]),
        o6.hasAddIn(o6.ns["ns=eumabois;i=5001"]),
    ],
    parent="ns=machinery;i=1001",
    referenceType=ns0.reftypes.Organizes,
    eventNotifier=1,
)


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, woodworking
