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

"""Generated OPC UA pnrio namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnrio_reftypes
from . import datatypes as pnrio_datypes
from . import vartypes as pnrio_vartypes
from . import objtypes as pnrio_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5002", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaDigitalInputConfigDataType, o6.ns["ns=pnrio;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5003", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaDigitalInputConfigDataType, o6.ns["ns=pnrio;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5005", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaDigitalInputConfigDataType, o6.ns["ns=pnrio;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5006", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaDigitalInputConfigDataType, o6.ns["ns=pnrio;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5008", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaDigitalOutputConfigDataType, o6.ns["ns=pnrio;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5009", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaDigitalOutputConfigDataType, o6.ns["ns=pnrio;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5011", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaDigitalOutputConfigDataType, o6.ns["ns=pnrio;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5012", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaDigitalOutputConfigDataType, o6.ns["ns=pnrio;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5014", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaAnalogInputConfigDataType, o6.ns["ns=pnrio;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5015", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaAnalogInputConfigDataType, o6.ns["ns=pnrio;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5016", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5017", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaAnalogInputConfigDataType, o6.ns["ns=pnrio;i=5017"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5018", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaAnalogInputConfigDataType, o6.ns["ns=pnrio;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5019", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5020", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaAnalogOutputConfigDataType, o6.ns["ns=pnrio;i=5020"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5021", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaAnalogOutputConfigDataType, o6.ns["ns=pnrio;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5022", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5023", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaAnalogOutputConfigDataType, o6.ns["ns=pnrio;i=5023"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5024", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaAnalogOutputConfigDataType, o6.ns["ns=pnrio;i=5024"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5027", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioAnalogDataType, o6.ns["ns=pnrio;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5028", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5029", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaDigitalProcessValueDataType, o6.ns["ns=pnrio;i=5029"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5030", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaDigitalProcessValueDataType, o6.ns["ns=pnrio;i=5030"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5031", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5032", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaDigitalProcessValueDataType, o6.ns["ns=pnrio;i=5032"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5033", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaDigitalProcessValueDataType, o6.ns["ns=pnrio;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5034", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioAnalogDataType, o6.ns["ns=pnrio;i=5034"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5035", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5036", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioBitFieldDataType, o6.ns["ns=pnrio;i=5036"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5038", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaAnalogProcessValueDataType, o6.ns["ns=pnrio;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5039", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaAnalogProcessValueDataType, o6.ns["ns=pnrio;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5040", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5041", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaAnalogProcessValueDataType, o6.ns["ns=pnrio;i=5041"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5042", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaAnalogProcessValueDataType, o6.ns["ns=pnrio;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5047", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioBitFieldDataType, o6.ns["ns=pnrio;i=5047"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5055", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5056", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaDigitalValueDataType, o6.ns["ns=pnrio;i=5056"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5057", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaDigitalValueDataType, o6.ns["ns=pnrio;i=5057"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5058", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5059", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaDigitalValueDataType, o6.ns["ns=pnrio;i=5059"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5060", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaDigitalValueDataType, o6.ns["ns=pnrio;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5061", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5062", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioPaAnalogValueDataType, o6.ns["ns=pnrio;i=5062"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5063", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioPaAnalogValueDataType, o6.ns["ns=pnrio;i=5063"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5064", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5065", browseName="Default XML")
o6.hasEncoding(pnrio_datypes.RioFaAnalogValueDataType, o6.ns["ns=pnrio;i=5065"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnrio;i=5066", browseName="Default JSON")
o6.hasEncoding(pnrio_datypes.RioFaAnalogValueDataType, o6.ns["ns=pnrio;i=5066"])
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6005",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("GOOD"),
            description=o6.LocalizedText(
                "For ConsumerStatus: The submodule&#8217;s IO data object could be successfully processed by the application process.\nFor ProviderStatus: The content of the submodule&#8217;s IO data object is valid.\n",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("BAD_BY_SUBSLOT"),
            description=o6.LocalizedText(
                "For ConsumerStatus: not used.\nFor ProviderStatus: The content of the submodule&#8217;s IO data object is invalid. The condition was detected by the submodule.\n",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("BAD_BY_SLOT"),
            description=o6.LocalizedText(
                "For ConsumerStatus: not used.\nFor ProviderStatus: . The content of the submodule&#8217;s IO data object is invalid. The condition was detected by the module.\n",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("BAD_BY_DEVICE"),
            description=o6.LocalizedText(
                "For ConsumerStatus: The IO device has locally detected problems to convey data.\nFor ProviderStatus: The content of the submodule&#8217;s IO data object is invalid. The condition was detected by the device.\n",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("BAD_BY_CONTROLLER"),
            description=o6.LocalizedText(
                "For ConsumerStatus: The submodule&#8217;s IO data object could not be successfully processed by the application of the Controller (e.g. because of the operation state &#8220;stop&#8221;).\nFor ProviderStatus: The content of the submodule&#8217;s IO data object is invalid. The condition was only locally detected by the Controller.\n",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6012",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CURRENT-4-20_mA"), description=o6.LocalizedText("Current, 4 to 20 mA")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CURRENT-0-20_mA"), description=o6.LocalizedText("Current, 0 to 20 mA")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("VOLTAGE-0-10_V"), description=o6.LocalizedText("Voltage, 0 to 10 V")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("VOLTAGE-10-10_V"), description=o6.LocalizedText("Voltage, -10 to 10 V")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("HART"), description=o6.LocalizedText("HART Communication (this includes 4 to 20 mA)")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("DIGITAL-0/24V"), description=o6.LocalizedText("Digital, 0/24 V (discrete input or output only)")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("NAMUR"), description=o6.LocalizedText("See NAMUR NE 107.")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("MANUFACTURER_SPECIFIC"), description=o6.LocalizedText("None of the above.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6013",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("USE_SUBSTITUTE_VALUE"),
            description=o6.LocalizedText("The value of the SubstituteValue configuration property is used as substitute value if an error condition is detected."),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("USE_LAST_VALID_VALUE"),
            description=o6.LocalizedText("The last valid value is used as substitute value if an error condition is detected."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("USE_ACTUAL_VALUE"),
            description=o6.LocalizedText("No substitute value is used, the process value can have the wrong calculated value and status even if the error condition is detected."),
        ),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("Unspecified"), description=o6.LocalizedText("No information about the status is given.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6014",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("AUTO"),
            description=o6.LocalizedText("Do not use the value of the ManualProcessValue variable as Process Value of the RIO Channel."),
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("MANUAL"), description=o6.LocalizedText("Use the value of the ManualProcessValue variable as Process Value of the RIO Channel.")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("OUT_OF_SERVICE"), description=o6.LocalizedText("The RIO Channel is out of service.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6015",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("GOOD"),
            description=o6.LocalizedText("Input: The Process Value can be used by the Controller. Output: The Signal was generated from the Process Value.", ""),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("UNCERTAIN"),
            description=o6.LocalizedText("An error condition could compromise the Process Value (Input) or the Signal (Output)."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("BAD"),
            description=o6.LocalizedText("Input: The Process Value cannot be used by the Controller. Output: The Signal may not be generated from the Process Value.", ""),
        ),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("UNSPECIFIED"), description=o6.LocalizedText("No information about the status is given.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6016",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NORMAL"), description=o6.LocalizedText("Good signal.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("FAILURE"), description=o6.LocalizedText("Invalid signal due to malfunction of a sensor or actuator.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("FUNCTION_CHECK"), description=o6.LocalizedText("Temporarily invalid signal.")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("MAINTENANCE_REQUEST"), description=o6.LocalizedText("Valid signal, but function could drop or cease soon.")
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("OUT_OF_SPECIFICATION"), description=o6.LocalizedText("Device is running beyond permissible range of some other parameter.")
        ),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("UNSPECIFIED"), description=o6.LocalizedText("No information about the status is given.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6017",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[32],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("BAD_NOT_SPECIFIC"), description=o6.LocalizedText("Proxy determines that a device does not communicate.")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("BAD_NOT_CONNECTED"), description=o6.LocalizedText("Some communication error: the device is currently unavailable.", "")
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("BAD_NOT_CONNECTED_SIMULATION_ACTIVE"), description=o6.LocalizedText("Same as BAD_NOT_CONNECTED but with simulate flag set.")
        ),
        ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("BAD_PASSIVATED"), description=o6.LocalizedText("The channel is passivated.")),
        ns0.datatypes.EnumValueType(
            value=33, displayName=o6.LocalizedText("BAD_PASSIVATED_SIMULATION_ACTIVE"), description=o6.LocalizedText("Same as BAD_PASSIVATED but with simulate flag set.")
        ),
        ns0.datatypes.EnumValueType(
            value=36, displayName=o6.LocalizedText("BAD_MAINTENANCE_ALARM"), description=o6.LocalizedText("No measurement available because of a failure.")
        ),
        ns0.datatypes.EnumValueType(
            value=37,
            displayName=o6.LocalizedText("BAD_MAINTENANCE_ALARM_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as BAD_MAINTENANCE_ALARM but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(
            value=40, displayName=o6.LocalizedText("BAD_PROCESS"), description=o6.LocalizedText("No measurement available because of invalid process conditions.")
        ),
        ns0.datatypes.EnumValueType(
            value=41, displayName=o6.LocalizedText("BAD_PROCESS_SIMULATION_ACTIVE"), description=o6.LocalizedText("Same as BAD_PROCESS but with simulate flag set.")
        ),
        ns0.datatypes.EnumValueType(value=60, displayName=o6.LocalizedText("BAD_FUNCTION_CHECK"), description=o6.LocalizedText("Local override, value not usable.")),
        ns0.datatypes.EnumValueType(
            value=61, displayName=o6.LocalizedText("BAD_FUNCTION_CHECK_SIMULATION_ACTIVE"), description=o6.LocalizedText("Same as BAD_FUNCTION_CHECK but with simulate flag set.")
        ),
        ns0.datatypes.EnumValueType(
            value=72,
            displayName=o6.LocalizedText("UNCERTAIN_SUBSTITUTE_SET"),
            description=o6.LocalizedText("The configured substitute value (see SubstituteValue) is used as Process Value."),
        ),
        ns0.datatypes.EnumValueType(
            value=73,
            displayName=o6.LocalizedText("UNCERTAIN_SUBSTITUTE_SET_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as UNCERTAIN_SUBSTITUTE_SET but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(
            value=76, displayName=o6.LocalizedText("UNCERTAIN_INITIAL_VALUE"), description=o6.LocalizedText("Default value since no measured value is available.")
        ),
        ns0.datatypes.EnumValueType(
            value=77,
            displayName=o6.LocalizedText("UNCERTAIN_INITIAL_VALUE_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as UNCERTAIN_INITIAL_VALUE but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(value=104, displayName=o6.LocalizedText("UNCERTAIN_MAINTENANCE_DEMANDED"), description=o6.LocalizedText("Value is potentially invalid.")),
        ns0.datatypes.EnumValueType(
            value=105,
            displayName=o6.LocalizedText("UNCERTAIN_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as UNCERTAIN_MAINTENANCE_DEMANDED but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(
            value=120,
            displayName=o6.LocalizedText("UNCERTAIN_NO_MAINTENANCE"),
            description=o6.LocalizedText("The process conditions are out of the specified operating range of the device."),
        ),
        ns0.datatypes.EnumValueType(
            value=121,
            displayName=o6.LocalizedText("UNCERTAIN_NO_MAINTENANCE_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as UNCERTAIN_NO_MAINTENANCE but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(value=128, displayName=o6.LocalizedText("GOOD"), description=o6.LocalizedText("No error or special condition is associated with this value.")),
        ns0.datatypes.EnumValueType(value=129, displayName=o6.LocalizedText("GOOD_SIMULATION_ACTIVE"), description=o6.LocalizedText("Same as GOOD but with simulate flag set.")),
        ns0.datatypes.EnumValueType(value=130, displayName=o6.LocalizedText("UPDATE"), description=o6.LocalizedText("IM_Revision_Counter changed.")),
        ns0.datatypes.EnumValueType(
            value=160,
            displayName=o6.LocalizedText("GOOD_INITIATE_FAULT_STATE"),
            description=o6.LocalizedText("The value is from a block that wants its following output block (e.g. Actuator FB) to go to Fail Safe."),
        ),
        ns0.datatypes.EnumValueType(
            value=164,
            displayName=o6.LocalizedText("GOOD_MAINTENANCE_REQUIRED"),
            description=o6.LocalizedText("Value is usable. Maintenance is recommended within a medium-term period."),
        ),
        ns0.datatypes.EnumValueType(
            value=165,
            displayName=o6.LocalizedText("GOOD_MAINTENANCE_REQUIRED_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as GOOD_MAINTENANCE_REQUIRED but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(
            value=168,
            displayName=o6.LocalizedText("GOOD_MAINTENANCE_DEMANDED"),
            description=o6.LocalizedText("Value is usable. Maintenance is strongly recommended within a short-term period."),
        ),
        ns0.datatypes.EnumValueType(
            value=169,
            displayName=o6.LocalizedText("GOOD_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as GOOD_MAINTENANCE_DEMANDED but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(
            value=156, displayName=o6.LocalizedText("GOOD_LOCAL_OVERRIDE"), description=o6.LocalizedText("The value is from a block that has been locked out.")
        ),
        ns0.datatypes.EnumValueType(
            value=157,
            displayName=o6.LocalizedText("GOOD_LOCAL_OVERRIDE_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as GOOD_LOCAL_OVERRIDE_SIMULATED but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(value=188, displayName=o6.LocalizedText("GOOD_FUNCTION_CHECK"), description=o6.LocalizedText("Function check is being executed.")),
        ns0.datatypes.EnumValueType(
            value=189,
            displayName=o6.LocalizedText("GOOD_FUNCTION_CHECK_SIMULATION_ACTIVE"),
            description=o6.LocalizedText("Same as GOOD_FUNCTION_CHECK but with simulate flag set."),
        ),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("UNSPECIFIED"), description=o6.LocalizedText("No information about the status is given.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6018",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("HI_LIM_EXCEEDED"), description=o6.LocalizedText("Upper limit value exceeded. Only supported by RIOforPA channels. ")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("LO_LIM_EXCEEDED"), description=o6.LocalizedText("Lower limit value underrun. Only supported by RIOforPA channels.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("SIMULATION_ACTIVE"), description=o6.LocalizedText("Simulation is active. Only supported by RIOforPA channels.")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("MODE_CHANGED"), description=o6.LocalizedText("Mode of block has changed. Only supported by RIOforPA channels.")
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("SUBSTITUTE_VALUE_USED"), description=o6.LocalizedText("Substitute value used. Only supported by RIOforPA channels.")
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("Q_BAD_SUBSTITUTE_VALUE_USED"),
            description=o6.LocalizedText("Process Image Qualifier = 0. Substitute value used by (Sub)Module. Only supported by RIOforFA channels."),
        ),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("OUT_OF_SERVICE"), description=o6.LocalizedText("The channel has ceased operation.")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6019", browseName="ns=pnrio;RioPaDigitalInputConfigDataType", dataType=o6.String, value="RioPaDigitalInputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5001"], "i=39", o6.ns["ns=pnrio;i=6019"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6020", browseName="ns=pnrio;RioPaDigitalInputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioPaDigitalInputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5002"], "i=39", o6.ns["ns=pnrio;i=6020"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6021", browseName="ns=pnrio;RioFaDigitalInputConfigDataType", dataType=o6.String, value="RioFaDigitalInputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5004"], "i=39", o6.ns["ns=pnrio;i=6021"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6022", browseName="ns=pnrio;RioFaDigitalInputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioFaDigitalInputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5005"], "i=39", o6.ns["ns=pnrio;i=6022"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6023", browseName="ns=pnrio;RioPaDigitalOutputConfigDataType", dataType=o6.String, value="RioPaDigitalOutputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5007"], "i=39", o6.ns["ns=pnrio;i=6023"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6024", browseName="ns=pnrio;RioPaDigitalOutputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioPaDigitalOutputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5008"], "i=39", o6.ns["ns=pnrio;i=6024"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6025", browseName="ns=pnrio;RioFaDigitalOutputConfigDataType", dataType=o6.String, value="RioFaDigitalOutputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5010"], "i=39", o6.ns["ns=pnrio;i=6025"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6026", browseName="ns=pnrio;RioFaDigitalOutputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioFaDigitalOutputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5011"], "i=39", o6.ns["ns=pnrio;i=6026"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6027", browseName="ns=pnrio;RioPaAnalogInputConfigDataType", dataType=o6.String, value="RioPaAnalogInputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5013"], "i=39", o6.ns["ns=pnrio;i=6027"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6028", browseName="ns=pnrio;RioPaAnalogInputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioPaAnalogInputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5014"], "i=39", o6.ns["ns=pnrio;i=6028"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6029", browseName="ns=pnrio;RioFaAnalogInputConfigDataType", dataType=o6.String, value="RioFaAnalogInputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5016"], "i=39", o6.ns["ns=pnrio;i=6029"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6030", browseName="ns=pnrio;RioFaAnalogInputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioFaAnalogInputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5017"], "i=39", o6.ns["ns=pnrio;i=6030"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6031", browseName="ns=pnrio;RioPaAnalogOutputConfigDataType", dataType=o6.String, value="RioPaAnalogOutputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5019"], "i=39", o6.ns["ns=pnrio;i=6031"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6032", browseName="ns=pnrio;RioPaAnalogOutputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioPaAnalogOutputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5020"], "i=39", o6.ns["ns=pnrio;i=6032"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6033", browseName="ns=pnrio;RioFaAnalogOutputConfigDataType", dataType=o6.String, value="RioFaAnalogOutputConfigDataType")
o6.reference(o6.ns["ns=pnrio;i=5022"], "i=39", o6.ns["ns=pnrio;i=6033"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6034", browseName="ns=pnrio;RioFaAnalogOutputConfigDataType", dataType=o6.String, value="//xs:element[@name='RioFaAnalogOutputConfigDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5023"], "i=39", o6.ns["ns=pnrio;i=6034"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6037", browseName="ns=pnrio;RioPaDigitalProcessValueDataType", dataType=o6.String, value="RioPaDigitalProcessValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5028"], "i=39", o6.ns["ns=pnrio;i=6037"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6038", browseName="ns=pnrio;RioPaDigitalProcessValueDataType", dataType=o6.String, value="//xs:element[@name='RioPaDigitalProcessValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5029"], "i=39", o6.ns["ns=pnrio;i=6038"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6039", browseName="ns=pnrio;RioFaDigitalProcessValueDataType", dataType=o6.String, value="RioFaDigitalProcessValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5031"], "i=39", o6.ns["ns=pnrio;i=6039"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6040", browseName="ns=pnrio;RioFaDigitalProcessValueDataType", dataType=o6.String, value="//xs:element[@name='RioFaDigitalProcessValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5032"], "i=39", o6.ns["ns=pnrio;i=6040"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6043", browseName="ns=pnrio;RioPaAnalogProcessValueDataType", dataType=o6.String, value="RioPaAnalogProcessValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5037"], "i=39", o6.ns["ns=pnrio;i=6043"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6044", browseName="ns=pnrio;RioPaAnalogProcessValueDataType", dataType=o6.String, value="//xs:element[@name='RioPaAnalogProcessValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5038"], "i=39", o6.ns["ns=pnrio;i=6044"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6045", browseName="ns=pnrio;RioFaAnalogProcessValueDataType", dataType=o6.String, value="RioFaAnalogProcessValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5040"], "i=39", o6.ns["ns=pnrio;i=6045"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6046", browseName="ns=pnrio;RioFaAnalogProcessValueDataType", dataType=o6.String, value="//xs:element[@name='RioFaAnalogProcessValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5041"], "i=39", o6.ns["ns=pnrio;i=6046"])
pnrio_vartypes.RioFaAnalogProcessValueVariableType(
    nodeId="ns=pnrio;i=6117",
    browseName="ns=pnrio;ProcessValue",
    modellingRule="Mandatory",
    references=[o6.hasComponent(pnrio_vartypes.RioFaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6118", browseName="ns=pnrio;QualifierValue", dataType=o6.Boolean))],
    dataType=pnrio_datypes.RioFaAnalogProcessValueDataType,
)
o6.reference(pnrio_objtypes.RioFaAnalogInputChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=6117"])
pnrio_vartypes.RioFaAnalogProcessValueVariableType(
    nodeId="ns=pnrio;i=6131",
    browseName="ns=pnrio;ProcessValue",
    modellingRule="Mandatory",
    references=[o6.hasComponent(pnrio_vartypes.RioFaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6132", browseName="ns=pnrio;QualifierValue", dataType=o6.Boolean))],
    dataType=pnrio_datypes.RioFaAnalogProcessValueDataType,
)
o6.reference(pnrio_objtypes.RioFaAnalogOutputChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=6131"])
pnrio_vartypes.RioFaAnalogProcessValueVariableType(
    nodeId="ns=pnrio;i=6134",
    browseName="ns=pnrio;ProcessValueReadback",
    modellingRule="Optional",
    references=[o6.hasComponent(pnrio_vartypes.RioFaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6135", browseName="ns=pnrio;QualifierValue", dataType=o6.Boolean))],
    dataType=pnrio_datypes.RioFaAnalogProcessValueDataType,
)
o6.reference(pnrio_objtypes.RioFaAnalogOutputChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=6134"])
pnrio_objtypes.PnIoSignalType(
    nodeId="ns=pnrio;i=5053",
    browseName="ns=pnrio;<Nr_SignalName>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6166", browseName="ns=pnrio;Offset", dataType=o6.UInt16))],
)
o6.reference(pnrio_objtypes.PnIoTelegramType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=5053"])
pnrio_objtypes.PnIoTelegramType(
    nodeId="ns=pnrio;i=5043",
    browseName="ns=pnrio;Input",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6167", browseName="ns=pnrio;Length", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6168", browseName="ns=pnrio;ProviderStatus", dataType=pnrio_datypes.PnIoTelegramStatusEnumeration)),
    ],
)
o6.reference(pnrio_objtypes.PnTelegramType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=5043"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6172", browseName="ns=pnrio;RioAnalogDataType", dataType=o6.String, value="RioAnalogDataType")
o6.reference(o6.ns["ns=pnrio;i=5026"], "i=39", o6.ns["ns=pnrio;i=6172"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6179", browseName="ns=pnrio;RioAnalogDataType", dataType=o6.String, value="//xs:element[@name='RioAnalogDataType']")
o6.reference(o6.ns["ns=pnrio;i=5027"], "i=39", o6.ns["ns=pnrio;i=6179"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6182", browseName="ns=pnrio;RioBitFieldDataType", dataType=o6.String, value="RioBitFieldDataType")
o6.reference(o6.ns["ns=pnrio;i=5035"], "i=39", o6.ns["ns=pnrio;i=6182"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPNRIOSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pnrio;i=5046",
    browseName="ns=pnrio;http://opcfoundation.org/UA/PNRIO/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6208", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6209", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-07-11T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6210", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNRIO/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6211", browseName="NamespaceVersion", dataType=o6.String, value="1.00.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnrio;i=6212", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnrio;i=6213", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6214", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6216", browseName="ns=pnrio;RioBitFieldDataType", dataType=o6.String, value="//xs:element[@name='RioBitFieldDataType']")
o6.reference(o6.ns["ns=pnrio;i=5036"], "i=39", o6.ns["ns=pnrio;i=6216"])
pnrio_objtypes.PnIoTelegramType(
    nodeId="ns=pnrio;i=5044",
    browseName="ns=pnrio;Output",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6215", browseName="ns=pnrio;Length", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6217", browseName="ns=pnrio;ProviderStatus", dataType=pnrio_datypes.PnIoTelegramStatusEnumeration)),
    ],
)
o6.reference(pnrio_objtypes.PnTelegramType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=5044"])
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6231",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=3026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ALL_DISAPPEARS"), description=o6.LocalizedText("No diagnosis condition of any severity is persisting.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("APPEARS"), description=o6.LocalizedText("The diagnosis condition indicated arises and/or persists. ")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("DISAPPEARS"),
            description=o6.LocalizedText(
                "The diagnosis condition indicated does not longer persist. No diagnosis condition of the same severity is persisting for the affected channel."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("DISAPPEARS_OTHER_REMAIN"),
            description=o6.LocalizedText("The diagnosis condition indicated does not longer persist. Other diagnosis conditions of the same severity are persisting."),
        ),
    ],
)
pnrio_objtypes.RioChannelType(
    nodeId="ns=pnrio;i=5051",
    browseName="ns=pnrio;<RioInputChannel>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6011", browseName="ns=pnrio;ApplicationTag", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6268", browseName="ns=pnrio;RioChannelNumber", dataType=o6.UInt16)),
    ],
    _allow_abstract=True,
)
o6.reference(pnrio_objtypes.RioChannelGroupType, pnrio_reftypes.HasRioInputChannel, o6.ns["ns=pnrio;i=5051"])
pnrio_objtypes.RioChannelType(
    nodeId="ns=pnrio;i=5052",
    browseName="ns=pnrio;<RioOutputChannel>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6272", browseName="ns=pnrio;ApplicationTag", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6273", browseName="ns=pnrio;RioChannelNumber", dataType=o6.UInt16)),
    ],
    _allow_abstract=True,
)
o6.reference(pnrio_objtypes.RioChannelGroupType, pnrio_reftypes.HasRioOutputChannel, o6.ns["ns=pnrio;i=5052"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6308", browseName="ns=pnrio;RioPaDigitalValueDataType", dataType=o6.String, value="RioPaDigitalValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5055"], "i=39", o6.ns["ns=pnrio;i=6308"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6309", browseName="ns=pnrio;RioPaDigitalValueDataType", dataType=o6.String, value="//xs:element[@name='RioPaDigitalValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5056"], "i=39", o6.ns["ns=pnrio;i=6309"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6310", browseName="ns=pnrio;RioFaDigitalValueDataType", dataType=o6.String, value="RioFaDigitalValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5058"], "i=39", o6.ns["ns=pnrio;i=6310"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6311", browseName="ns=pnrio;RioFaDigitalValueDataType", dataType=o6.String, value="//xs:element[@name='RioFaDigitalValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5059"], "i=39", o6.ns["ns=pnrio;i=6311"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6312", browseName="ns=pnrio;RioPaAnalogValueDataType", dataType=o6.String, value="RioPaAnalogValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5061"], "i=39", o6.ns["ns=pnrio;i=6312"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6313", browseName="ns=pnrio;RioPaAnalogValueDataType", dataType=o6.String, value="//xs:element[@name='RioPaAnalogValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5062"], "i=39", o6.ns["ns=pnrio;i=6313"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnrio;i=6314", browseName="ns=pnrio;RioFaAnalogValueDataType", dataType=o6.String, value="RioFaAnalogValueDataType")
o6.reference(o6.ns["ns=pnrio;i=5064"], "i=39", o6.ns["ns=pnrio;i=6314"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnrio;i=6006",
    browseName="ns=pnrio;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNRIO/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6007", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNRIO/")),
        o6.hasComponent(o6.ns["ns=pnrio;i=6019"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6021"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6023"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6025"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6027"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6029"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6031"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6033"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6037"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6039"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6043"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6045"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6172"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6182"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6308"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6310"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6312"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6314"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PNRIO/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PNRIO/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioBitFieldDataType">\n  <opc:Field TypeName="opc:UInt32" Name="BitData"/>\n  <opc:Field TypeName="opc:UInt32" Name="BitUsed"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaAnalogInputConfigDataType">\n  <opc:Field TypeName="opc:Float" Name="Damping"/>\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="SupplyVoltageCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="SubstituteValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaAnalogOutputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="SupplyVoltageCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="LoadVoltageCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="SubstituteValue"/>\n  <opc:Field TypeName="opc:Float" Name="SubstituteTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaAnalogValueDataType">\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="Value"/>\n  <opc:Field TypeName="opc:Boolean" Name="Qualifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:RioFaAnalogValueDataType" Name="RioFaAnalogProcessValueDataType">\n  <opc:Field SourceType="tns:RioFaAnalogValueDataType" TypeName="tns:RioAnalogDataType" Name="Value"/>\n  <opc:Field SourceType="tns:RioFaAnalogValueDataType" TypeName="opc:Boolean" Name="Qualifier"/>\n  <opc:Field TypeName="opc:Byte" Name="Quality"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaDigitalInputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="SupplyVoltageCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="opc:Boolean" Name="SubstituteValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaDigitalOutputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="SupplyVoltageCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="LoadVoltageCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="opc:Boolean" Name="SubstituteValue"/>\n  <opc:Field TypeName="opc:Float" Name="SubstituteTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioFaDigitalValueDataType">\n  <opc:Field TypeName="opc:Boolean" Name="Value"/>\n  <opc:Field TypeName="opc:Boolean" Name="Qualifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:RioFaDigitalValueDataType" Name="RioFaDigitalProcessValueDataType">\n  <opc:Field SourceType="tns:RioFaDigitalValueDataType" TypeName="opc:Boolean" Name="Value"/>\n  <opc:Field SourceType="tns:RioFaDigitalValueDataType" TypeName="opc:Boolean" Name="Qualifier"/>\n  <opc:Field TypeName="opc:Byte" Name="Quality"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaAnalogInputConfigDataType">\n  <opc:Field TypeName="opc:Float" Name="Damping"/>\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="SubstituteValue"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="HighLimit"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="LowLimit"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaAnalogOutputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="SubstituteValue"/>\n  <opc:Field TypeName="opc:Float" Name="SubstituteTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaAnalogValueDataType">\n  <opc:Field TypeName="tns:RioAnalogDataType" Name="Value"/>\n  <opc:Field TypeName="opc:Byte" Name="Qualifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:RioPaAnalogValueDataType" Name="RioPaAnalogProcessValueDataType">\n  <opc:Field SourceType="tns:RioPaAnalogValueDataType" TypeName="tns:RioAnalogDataType" Name="Value"/>\n  <opc:Field SourceType="tns:RioPaAnalogValueDataType" TypeName="opc:Byte" Name="Qualifier"/>\n  <opc:Field TypeName="opc:Byte" Name="Quality"/>\n  <opc:Field TypeName="opc:Byte" Name="NE_107"/>\n  <opc:Field TypeName="opc:Byte" Name="Status_full"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaDigitalInputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="InversionEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="opc:Boolean" Name="SubstituteValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaDigitalOutputConfigDataType">\n  <opc:Field TypeName="tns:RioSignalTypeEnumeration" Name="SignalType"/>\n  <opc:Field TypeName="opc:Boolean" Name="WireCheckEnabled"/>\n  <opc:Field TypeName="opc:Boolean" Name="InversionEnabled"/>\n  <opc:Field TypeName="tns:RioSubstitutePolicyEnumeration" Name="SubstitutePolicy"/>\n  <opc:Field TypeName="opc:Boolean" Name="SubstituteValue"/>\n  <opc:Field TypeName="opc:Float" Name="SubstituteTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RioPaDigitalValueDataType">\n  <opc:Field TypeName="opc:Boolean" Name="Value"/>\n  <opc:Field TypeName="opc:Byte" Name="Qualifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:RioPaDigitalValueDataType" Name="RioPaDigitalProcessValueDataType">\n  <opc:Field SourceType="tns:RioPaDigitalValueDataType" TypeName="opc:Boolean" Name="Value"/>\n  <opc:Field SourceType="tns:RioPaDigitalValueDataType" TypeName="opc:Byte" Name="Qualifier"/>\n  <opc:Field TypeName="opc:Byte" Name="Quality"/>\n  <opc:Field TypeName="opc:Byte" Name="NE_107"/>\n  <opc:Field TypeName="opc:Byte" Name="Status_full"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="RioAnalogDataType">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Float" SwitchValue="1" Name="Float_32"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int16" SwitchValue="2" Name="Int_16"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="3" Name="Int_32"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt16" SwitchValue="4" Name="UInt_16"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="5" Name="UInt_32"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="PnIoTelegramStatusEnumeration">\n  <opc:EnumeratedValue Name="GOOD" Value="0"/>\n  <opc:EnumeratedValue Name="BAD_BY_SUBSLOT" Value="1"/>\n  <opc:EnumeratedValue Name="BAD_BY_SLOT" Value="2"/>\n  <opc:EnumeratedValue Name="BAD_BY_DEVICE" Value="3"/>\n  <opc:EnumeratedValue Name="BAD_BY_CONTROLLER" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioChannelDiagnosisReasonEnumeration">\n  <opc:EnumeratedValue Name="ALL_DISAPPEARS" Value="0"/>\n  <opc:EnumeratedValue Name="APPEARS" Value="1"/>\n  <opc:EnumeratedValue Name="DISAPPEARS" Value="2"/>\n  <opc:EnumeratedValue Name="DISAPPEARS_OTHER_REMAIN" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioChannelDiagnosisStatusEnumeration">\n  <opc:EnumeratedValue Name="HI_LIM_EXCEEDED" Value="0"/>\n  <opc:EnumeratedValue Name="LO_LIM_EXCEEDED" Value="1"/>\n  <opc:EnumeratedValue Name="SIMULATION_ACTIVE" Value="2"/>\n  <opc:EnumeratedValue Name="MODE_CHANGED" Value="3"/>\n  <opc:EnumeratedValue Name="SUBSTITUTE_VALUE_USED" Value="4"/>\n  <opc:EnumeratedValue Name="Q_BAD_SUBSTITUTE_VALUE_USED" Value="5"/>\n  <opc:EnumeratedValue Name="OUT_OF_SERVICE" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioChannelModeEnumeration">\n  <opc:EnumeratedValue Name="AUTO" Value="0"/>\n  <opc:EnumeratedValue Name="MANUAL" Value="1"/>\n  <opc:EnumeratedValue Name="OUT_OF_SERVICE" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioQualifierEnumeration">\n  <opc:EnumeratedValue Name="BAD_NOT_SPECIFIC" Value="0"/>\n  <opc:EnumeratedValue Name="BAD_NOT_CONNECTED" Value="8"/>\n  <opc:EnumeratedValue Name="BAD_NOT_CONNECTED_SIMULATION_ACTIVE" Value="9"/>\n  <opc:EnumeratedValue Name="BAD_PASSIVATED" Value="32"/>\n  <opc:EnumeratedValue Name="BAD_PASSIVATED_SIMULATION_ACTIVE" Value="33"/>\n  <opc:EnumeratedValue Name="BAD_MAINTENANCE_ALARM" Value="36"/>\n  <opc:EnumeratedValue Name="BAD_MAINTENANCE_ALARM_SIMULATION_ACTIVE" Value="37"/>\n  <opc:EnumeratedValue Name="BAD_PROCESS" Value="40"/>\n  <opc:EnumeratedValue Name="BAD_PROCESS_SIMULATION_ACTIVE" Value="41"/>\n  <opc:EnumeratedValue Name="BAD_FUNCTION_CHECK" Value="60"/>\n  <opc:EnumeratedValue Name="BAD_FUNCTION_CHECK_SIMULATION_ACTIVE" Value="61"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_SUBSTITUTE_SET" Value="72"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_SUBSTITUTE_SET_SIMULATION_ACTIVE" Value="73"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_INITIAL_VALUE" Value="76"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_INITIAL_VALUE_SIMULATION_ACTIVE" Value="77"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_MAINTENANCE_DEMANDED" Value="104"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE" Value="105"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_NO_MAINTENANCE" Value="120"/>\n  <opc:EnumeratedValue Name="UNCERTAIN_NO_MAINTENANCE_SIMULATION_ACTIVE" Value="121"/>\n  <opc:EnumeratedValue Name="GOOD" Value="128"/>\n  <opc:EnumeratedValue Name="GOOD_SIMULATION_ACTIVE" Value="129"/>\n  <opc:EnumeratedValue Name="UPDATE" Value="130"/>\n  <opc:EnumeratedValue Name="GOOD_INITIATE_FAULT_STATE" Value="160"/>\n  <opc:EnumeratedValue Name="GOOD_MAINTENANCE_REQUIRED" Value="164"/>\n  <opc:EnumeratedValue Name="GOOD_MAINTENANCE_REQUIRED_SIMULATION_ACTIVE" Value="165"/>\n  <opc:EnumeratedValue Name="GOOD_MAINTENANCE_DEMANDED" Value="168"/>\n  <opc:EnumeratedValue Name="GOOD_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE" Value="169"/>\n  <opc:EnumeratedValue Name="GOOD_LOCAL_OVERRIDE" Value="156"/>\n  <opc:EnumeratedValue Name="GOOD_LOCAL_OVERRIDE_SIMULATION_ACTIVE" Value="157"/>\n  <opc:EnumeratedValue Name="GOOD_FUNCTION_CHECK" Value="188"/>\n  <opc:EnumeratedValue Name="GOOD_FUNCTION_CHECK_SIMULATION_ACTIVE" Value="189"/>\n  <opc:EnumeratedValue Name="UNSPECIFIED" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioQualityEnumeration">\n  <opc:EnumeratedValue Name="GOOD" Value="0"/>\n  <opc:EnumeratedValue Name="UNCERTAIN" Value="1"/>\n  <opc:EnumeratedValue Name="BAD" Value="2"/>\n  <opc:EnumeratedValue Name="UNSPECIFIED" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioSignalTypeEnumeration">\n  <opc:EnumeratedValue Name="CURRENT-4-20_mA" Value="0"/>\n  <opc:EnumeratedValue Name="CURRENT-0-20_mA" Value="1"/>\n  <opc:EnumeratedValue Name="VOLTAGE-0-10_V" Value="2"/>\n  <opc:EnumeratedValue Name="VOLTAGE-10-10_V" Value="3"/>\n  <opc:EnumeratedValue Name="HART" Value="4"/>\n  <opc:EnumeratedValue Name="DIGITAL-0/24V" Value="5"/>\n  <opc:EnumeratedValue Name="NAMUR" Value="6"/>\n  <opc:EnumeratedValue Name="MANUFACTURER_SPECIFIC" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioSpecifierEnumeration">\n  <opc:EnumeratedValue Name="NORMAL" Value="0"/>\n  <opc:EnumeratedValue Name="FAILURE" Value="1"/>\n  <opc:EnumeratedValue Name="FUNCTION_CHECK" Value="2"/>\n  <opc:EnumeratedValue Name="MAINTENANCE_REQUEST" Value="3"/>\n  <opc:EnumeratedValue Name="OUT_OF_SPECIFICATION" Value="4"/>\n  <opc:EnumeratedValue Name="UNSPECIFIED" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RioSubstitutePolicyEnumeration">\n  <opc:EnumeratedValue Name="USE_SUBSTITUTE_VALUE" Value="0"/>\n  <opc:EnumeratedValue Name="USE_LAST_VALID_VALUE" Value="1"/>\n  <opc:EnumeratedValue Name="USE_ACTUAL_VALUE" Value="2"/>\n  <opc:EnumeratedValue Name="Unspecified" Value="255"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnrio;i=6315", browseName="ns=pnrio;RioFaAnalogValueDataType", dataType=o6.String, value="//xs:element[@name='RioFaAnalogValueDataType']"
)
o6.reference(o6.ns["ns=pnrio;i=5065"], "i=39", o6.ns["ns=pnrio;i=6315"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnrio;i=6008",
    browseName="ns=pnrio;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNRIO/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6009", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNRIO/Types.xsd")),
        o6.hasComponent(o6.ns["ns=pnrio;i=6020"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6022"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6024"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6026"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6028"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6030"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6032"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6034"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6038"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6040"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6044"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6046"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6179"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6216"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6309"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6311"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6313"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=6315"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PNRIO/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PNRIO/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="PnIoTelegramStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="GOOD_0"/>\n   <xs:enumeration value="BAD_BY_SUBSLOT_1"/>\n   <xs:enumeration value="BAD_BY_SLOT_2"/>\n   <xs:enumeration value="BAD_BY_DEVICE_3"/>\n   <xs:enumeration value="BAD_BY_CONTROLLER_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnIoTelegramStatusEnumeration" name="PnIoTelegramStatusEnumeration"/>\n <xs:complexType name="ListOfPnIoTelegramStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnIoTelegramStatusEnumeration" name="PnIoTelegramStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnIoTelegramStatusEnumeration" name="ListOfPnIoTelegramStatusEnumeration" nillable="true"/>\n <xs:simpleType name="RioChannelDiagnosisReasonEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ALL_DISAPPEARS_0"/>\n   <xs:enumeration value="APPEARS_1"/>\n   <xs:enumeration value="DISAPPEARS_2"/>\n   <xs:enumeration value="DISAPPEARS_OTHER_REMAIN_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioChannelDiagnosisReasonEnumeration" name="RioChannelDiagnosisReasonEnumeration"/>\n <xs:complexType name="ListOfRioChannelDiagnosisReasonEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioChannelDiagnosisReasonEnumeration" name="RioChannelDiagnosisReasonEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioChannelDiagnosisReasonEnumeration" name="ListOfRioChannelDiagnosisReasonEnumeration" nillable="true"/>\n <xs:simpleType name="RioChannelDiagnosisStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="HI_LIM_EXCEEDED_0"/>\n   <xs:enumeration value="LO_LIM_EXCEEDED_1"/>\n   <xs:enumeration value="SIMULATION_ACTIVE_2"/>\n   <xs:enumeration value="MODE_CHANGED_3"/>\n   <xs:enumeration value="SUBSTITUTE_VALUE_USED_4"/>\n   <xs:enumeration value="Q_BAD_SUBSTITUTE_VALUE_USED_5"/>\n   <xs:enumeration value="OUT_OF_SERVICE_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioChannelDiagnosisStatusEnumeration" name="RioChannelDiagnosisStatusEnumeration"/>\n <xs:complexType name="ListOfRioChannelDiagnosisStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioChannelDiagnosisStatusEnumeration" name="RioChannelDiagnosisStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioChannelDiagnosisStatusEnumeration" name="ListOfRioChannelDiagnosisStatusEnumeration" nillable="true"/>\n <xs:simpleType name="RioChannelModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AUTO_0"/>\n   <xs:enumeration value="MANUAL_1"/>\n   <xs:enumeration value="OUT_OF_SERVICE_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioChannelModeEnumeration" name="RioChannelModeEnumeration"/>\n <xs:complexType name="ListOfRioChannelModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioChannelModeEnumeration" name="RioChannelModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioChannelModeEnumeration" name="ListOfRioChannelModeEnumeration" nillable="true"/>\n <xs:simpleType name="RioQualifierEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="BAD_NOT_SPECIFIC_0"/>\n   <xs:enumeration value="BAD_NOT_CONNECTED_8"/>\n   <xs:enumeration value="BAD_NOT_CONNECTED_SIMULATION_ACTIVE_9"/>\n   <xs:enumeration value="BAD_PASSIVATED_32"/>\n   <xs:enumeration value="BAD_PASSIVATED_SIMULATION_ACTIVE_33"/>\n   <xs:enumeration value="BAD_MAINTENANCE_ALARM_36"/>\n   <xs:enumeration value="BAD_MAINTENANCE_ALARM_SIMULATION_ACTIVE_37"/>\n   <xs:enumeration value="BAD_PROCESS_40"/>\n   <xs:enumeration value="BAD_PROCESS_SIMULATION_ACTIVE_41"/>\n   <xs:enumeration value="BAD_FUNCTION_CHECK_60"/>\n   <xs:enumeration value="BAD_FUNCTION_CHECK_SIMULATION_ACTIVE_61"/>\n   <xs:enumeration value="UNCERTAIN_SUBSTITUTE_SET_72"/>\n   <xs:enumeration value="UNCERTAIN_SUBSTITUTE_SET_SIMULATION_ACTIVE_73"/>\n   <xs:enumeration value="UNCERTAIN_INITIAL_VALUE_76"/>\n   <xs:enumeration value="UNCERTAIN_INITIAL_VALUE_SIMULATION_ACTIVE_77"/>\n   <xs:enumeration value="UNCERTAIN_MAINTENANCE_DEMANDED_104"/>\n   <xs:enumeration value="UNCERTAIN_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE_105"/>\n   <xs:enumeration value="UNCERTAIN_NO_MAINTENANCE_120"/>\n   <xs:enumeration value="UNCERTAIN_NO_MAINTENANCE_SIMULATION_ACTIVE_121"/>\n   <xs:enumeration value="GOOD_128"/>\n   <xs:enumeration value="GOOD_SIMULATION_ACTIVE_129"/>\n   <xs:enumeration value="UPDATE_130"/>\n   <xs:enumeration value="GOOD_INITIATE_FAULT_STATE_160"/>\n   <xs:enumeration value="GOOD_MAINTENANCE_REQUIRED_164"/>\n   <xs:enumeration value="GOOD_MAINTENANCE_REQUIRED_SIMULATION_ACTIVE_165"/>\n   <xs:enumeration value="GOOD_MAINTENANCE_DEMANDED_168"/>\n   <xs:enumeration value="GOOD_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE_169"/>\n   <xs:enumeration value="GOOD_LOCAL_OVERRIDE_156"/>\n   <xs:enumeration value="GOOD_LOCAL_OVERRIDE_SIMULATION_ACTIVE_157"/>\n   <xs:enumeration value="GOOD_FUNCTION_CHECK_188"/>\n   <xs:enumeration value="GOOD_FUNCTION_CHECK_SIMULATION_ACTIVE_189"/>\n   <xs:enumeration value="UNSPECIFIED_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioQualifierEnumeration" name="RioQualifierEnumeration"/>\n <xs:complexType name="ListOfRioQualifierEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioQualifierEnumeration" name="RioQualifierEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioQualifierEnumeration" name="ListOfRioQualifierEnumeration" nillable="true"/>\n <xs:simpleType name="RioQualityEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="GOOD_0"/>\n   <xs:enumeration value="UNCERTAIN_1"/>\n   <xs:enumeration value="BAD_2"/>\n   <xs:enumeration value="UNSPECIFIED_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioQualityEnumeration" name="RioQualityEnumeration"/>\n <xs:complexType name="ListOfRioQualityEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioQualityEnumeration" name="RioQualityEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioQualityEnumeration" name="ListOfRioQualityEnumeration" nillable="true"/>\n <xs:simpleType name="RioSignalTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CURRENT-4-20_mA_0"/>\n   <xs:enumeration value="CURRENT-0-20_mA_1"/>\n   <xs:enumeration value="VOLTAGE-0-10_V_2"/>\n   <xs:enumeration value="VOLTAGE-10-10_V_3"/>\n   <xs:enumeration value="HART_4"/>\n   <xs:enumeration value="DIGITAL-0/24V_5"/>\n   <xs:enumeration value="NAMUR_6"/>\n   <xs:enumeration value="MANUFACTURER_SPECIFIC_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioSignalTypeEnumeration" name="RioSignalTypeEnumeration"/>\n <xs:complexType name="ListOfRioSignalTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioSignalTypeEnumeration" name="RioSignalTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioSignalTypeEnumeration" name="ListOfRioSignalTypeEnumeration" nillable="true"/>\n <xs:simpleType name="RioSpecifierEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NORMAL_0"/>\n   <xs:enumeration value="FAILURE_1"/>\n   <xs:enumeration value="FUNCTION_CHECK_2"/>\n   <xs:enumeration value="MAINTENANCE_REQUEST_3"/>\n   <xs:enumeration value="OUT_OF_SPECIFICATION_4"/>\n   <xs:enumeration value="UNSPECIFIED_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioSpecifierEnumeration" name="RioSpecifierEnumeration"/>\n <xs:complexType name="ListOfRioSpecifierEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioSpecifierEnumeration" name="RioSpecifierEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioSpecifierEnumeration" name="ListOfRioSpecifierEnumeration" nillable="true"/>\n <xs:simpleType name="RioSubstitutePolicyEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="USE_SUBSTITUTE_VALUE_0"/>\n   <xs:enumeration value="USE_LAST_VALID_VALUE_1"/>\n   <xs:enumeration value="USE_ACTUAL_VALUE_2"/>\n   <xs:enumeration value="Unspecified_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RioSubstitutePolicyEnumeration" name="RioSubstitutePolicyEnumeration"/>\n <xs:complexType name="ListOfRioSubstitutePolicyEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioSubstitutePolicyEnumeration" name="RioSubstitutePolicyEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioSubstitutePolicyEnumeration" name="ListOfRioSubstitutePolicyEnumeration" nillable="true"/>\n <xs:complexType name="RioBitFieldDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="BitData"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="BitUsed"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioBitFieldDataType" name="RioBitFieldDataType"/>\n <xs:complexType name="ListOfRioBitFieldDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioBitFieldDataType" name="RioBitFieldDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioBitFieldDataType" name="ListOfRioBitFieldDataType" nillable="true"/>\n <xs:complexType name="RioFaAnalogInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Damping"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SupplyVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="SubstituteValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaAnalogInputConfigDataType" name="RioFaAnalogInputConfigDataType"/>\n <xs:complexType name="ListOfRioFaAnalogInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaAnalogInputConfigDataType" name="RioFaAnalogInputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaAnalogInputConfigDataType" name="ListOfRioFaAnalogInputConfigDataType" nillable="true"/>\n <xs:complexType name="RioFaAnalogOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SupplyVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="LoadVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="SubstituteValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="SubstituteTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaAnalogOutputConfigDataType" name="RioFaAnalogOutputConfigDataType"/>\n <xs:complexType name="ListOfRioFaAnalogOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaAnalogOutputConfigDataType" name="RioFaAnalogOutputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaAnalogOutputConfigDataType" name="ListOfRioFaAnalogOutputConfigDataType" nillable="true"/>\n <xs:complexType name="RioFaAnalogValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Qualifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaAnalogValueDataType" name="RioFaAnalogValueDataType"/>\n <xs:complexType name="ListOfRioFaAnalogValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaAnalogValueDataType" name="RioFaAnalogValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaAnalogValueDataType" name="ListOfRioFaAnalogValueDataType" nillable="true"/>\n <xs:complexType name="RioFaAnalogProcessValueDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:RioFaAnalogValueDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Quality"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RioFaAnalogProcessValueDataType" name="RioFaAnalogProcessValueDataType"/>\n <xs:complexType name="ListOfRioFaAnalogProcessValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaAnalogProcessValueDataType" name="RioFaAnalogProcessValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaAnalogProcessValueDataType" name="ListOfRioFaAnalogProcessValueDataType" nillable="true"/>\n <xs:complexType name="RioFaDigitalInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SupplyVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SubstituteValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaDigitalInputConfigDataType" name="RioFaDigitalInputConfigDataType"/>\n <xs:complexType name="ListOfRioFaDigitalInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaDigitalInputConfigDataType" name="RioFaDigitalInputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaDigitalInputConfigDataType" name="ListOfRioFaDigitalInputConfigDataType" nillable="true"/>\n <xs:complexType name="RioFaDigitalOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SupplyVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="LoadVoltageCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SubstituteValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="SubstituteTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaDigitalOutputConfigDataType" name="RioFaDigitalOutputConfigDataType"/>\n <xs:complexType name="ListOfRioFaDigitalOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaDigitalOutputConfigDataType" name="RioFaDigitalOutputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaDigitalOutputConfigDataType" name="ListOfRioFaDigitalOutputConfigDataType" nillable="true"/>\n <xs:complexType name="RioFaDigitalValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Qualifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioFaDigitalValueDataType" name="RioFaDigitalValueDataType"/>\n <xs:complexType name="ListOfRioFaDigitalValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaDigitalValueDataType" name="RioFaDigitalValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaDigitalValueDataType" name="ListOfRioFaDigitalValueDataType" nillable="true"/>\n <xs:complexType name="RioFaDigitalProcessValueDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:RioFaDigitalValueDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Quality"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RioFaDigitalProcessValueDataType" name="RioFaDigitalProcessValueDataType"/>\n <xs:complexType name="ListOfRioFaDigitalProcessValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioFaDigitalProcessValueDataType" name="RioFaDigitalProcessValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioFaDigitalProcessValueDataType" name="ListOfRioFaDigitalProcessValueDataType" nillable="true"/>\n <xs:complexType name="RioPaAnalogInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Damping"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="SubstituteValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="HighLimit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="LowLimit"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaAnalogInputConfigDataType" name="RioPaAnalogInputConfigDataType"/>\n <xs:complexType name="ListOfRioPaAnalogInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaAnalogInputConfigDataType" name="RioPaAnalogInputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaAnalogInputConfigDataType" name="ListOfRioPaAnalogInputConfigDataType" nillable="true"/>\n <xs:complexType name="RioPaAnalogOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="SubstituteValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="SubstituteTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaAnalogOutputConfigDataType" name="RioPaAnalogOutputConfigDataType"/>\n <xs:complexType name="ListOfRioPaAnalogOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaAnalogOutputConfigDataType" name="RioPaAnalogOutputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaAnalogOutputConfigDataType" name="ListOfRioPaAnalogOutputConfigDataType" nillable="true"/>\n <xs:complexType name="RioPaAnalogValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioAnalogDataType" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Qualifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaAnalogValueDataType" name="RioPaAnalogValueDataType"/>\n <xs:complexType name="ListOfRioPaAnalogValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaAnalogValueDataType" name="RioPaAnalogValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaAnalogValueDataType" name="ListOfRioPaAnalogValueDataType" nillable="true"/>\n <xs:complexType name="RioPaAnalogProcessValueDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:RioPaAnalogValueDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Quality"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="NE_107"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Status_full"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RioPaAnalogProcessValueDataType" name="RioPaAnalogProcessValueDataType"/>\n <xs:complexType name="ListOfRioPaAnalogProcessValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaAnalogProcessValueDataType" name="RioPaAnalogProcessValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaAnalogProcessValueDataType" name="ListOfRioPaAnalogProcessValueDataType" nillable="true"/>\n <xs:complexType name="RioPaDigitalInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="InversionEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SubstituteValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaDigitalInputConfigDataType" name="RioPaDigitalInputConfigDataType"/>\n <xs:complexType name="ListOfRioPaDigitalInputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaDigitalInputConfigDataType" name="RioPaDigitalInputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaDigitalInputConfigDataType" name="ListOfRioPaDigitalInputConfigDataType" nillable="true"/>\n <xs:complexType name="RioPaDigitalOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSignalTypeEnumeration" name="SignalType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="WireCheckEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="InversionEnabled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RioSubstitutePolicyEnumeration" name="SubstitutePolicy"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="SubstituteValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="SubstituteTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaDigitalOutputConfigDataType" name="RioPaDigitalOutputConfigDataType"/>\n <xs:complexType name="ListOfRioPaDigitalOutputConfigDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaDigitalOutputConfigDataType" name="RioPaDigitalOutputConfigDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaDigitalOutputConfigDataType" name="ListOfRioPaDigitalOutputConfigDataType" nillable="true"/>\n <xs:complexType name="RioPaDigitalValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Qualifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioPaDigitalValueDataType" name="RioPaDigitalValueDataType"/>\n <xs:complexType name="ListOfRioPaDigitalValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaDigitalValueDataType" name="RioPaDigitalValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaDigitalValueDataType" name="ListOfRioPaDigitalValueDataType" nillable="true"/>\n <xs:complexType name="RioPaDigitalProcessValueDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:RioPaDigitalValueDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Quality"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="NE_107"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Status_full"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RioPaDigitalProcessValueDataType" name="RioPaDigitalProcessValueDataType"/>\n <xs:complexType name="ListOfRioPaDigitalProcessValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioPaDigitalProcessValueDataType" name="RioPaDigitalProcessValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioPaDigitalProcessValueDataType" name="ListOfRioPaDigitalProcessValueDataType" nillable="true"/>\n <xs:complexType name="RioAnalogDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Float_32"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Int_16"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Int_32"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="UInt_16"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="UInt_32"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RioAnalogDataType" name="RioAnalogDataType"/>\n <xs:complexType name="ListOfRioAnalogDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RioAnalogDataType" name="RioAnalogDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRioAnalogDataType" name="ListOfRioAnalogDataType" nillable="true"/>\n</xs:schema>\n',
)


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6205",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7003", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6205"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6218",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7004", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6218"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6219",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6220",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7021", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6219"]), outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6220"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6275",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7022", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6275"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pnrio;i=5054",
    browseName="ns=pnrio;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6221", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6222", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6223", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6224", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pnrio;i=7003"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7004"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7021"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7022"]),
    ],
)
o6.reference(pnrio_objtypes.RioChannelGroupType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=5054"])


ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7041", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6041"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7042", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6055",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6057",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7043", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6055"]), outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6057"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnrio;i=6119",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnrio;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnrio;i=7044", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pnrio;i=6119"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pnrio;i=5025",
    browseName="ns=pnrio;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6084", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6085", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6097", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6098", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pnrio;i=7041"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7042"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7043"]),
        o6.hasComponent(o6.ns["ns=pnrio;i=7044"]),
    ],
)
o6.reference(pnrio_objtypes.RioChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnrio;i=5025"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnrio_reftypes, pnrio_datypes, pnrio_vartypes, pnrio_objtypes
