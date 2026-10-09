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

"""Generated OPC UA plastics_dosing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_dosing_datypes
from . import objtypes as plastics_dosing_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashDosingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_dosing;i=5001",
    browseName="ns=plastics_dosing;http://opcfoundation.org/UA/PlasticsRubber/Dosing/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-07-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Dosing/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=plastics_dosing;i=6020",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6021", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=plastics_dosing;i=6022",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6023", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6074",
    browseName="ns=plastics_dosing;MaterialClass",
    description="Provides information about the material class, which can be used for the recipe calculation by the server or client.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6075",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MAIN"), description=o6.LocalizedText("Main material")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ADDITIVE"), description=o6.LocalizedText("Additive e.g. coloring material")),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("REGRIND_CLOSED_LOOP"),
                        description=o6.LocalizedText(
                            "Regrind with known composition, which is already considered in the internal dosing control and therefore excluded from the recipe calculation."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("REGRIND_OPEN_LOOP"),
                        description=o6.LocalizedText("Regrind with unknown composition. Included in the recipe calculation."),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6076", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6090",
    browseName="EnumValues",
    parent="ns=plastics_dosing;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Off"), description=o6.LocalizedText("The component has been switched off")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Ready"), description=o6.LocalizedText("The component is waiting for a start dosing signal")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Dosing"), description=o6.LocalizedText("The component is actively feeding material")),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Calibration"),
            description=o6.LocalizedText("Component is in calibration mode and can typically not be used for dosing or filling"),
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("The component has an active error")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Cleaning"), description=o6.LocalizedText("The component is in cleaning mode e.g. hopper draining")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Purging"), description=o6.LocalizedText("The component is in purging mode")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Priming"), description=o6.LocalizedText("The component is in priming mode")),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6095",
    browseName="ns=plastics_dosing;DosingMode",
    description="Provides information, how the dosing of the component is controlled.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6103",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("ONLY_CONVEYING"),
                        description=o6.LocalizedText(
                            "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6104", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6122", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6123", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6128",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6129", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5037",
    browseName="ns=plastics_dosing;DrivePercentage",
    description="Relative value (0-100%) of the maximum drive power of the component drive.",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=6128"])],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6130",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6131", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5043",
    browseName="ns=plastics_dosing;Percentage",
    description="Part (%) of the recipe dosed by this component (recipe).",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=6130"])],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6036",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6039", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6133", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6134", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6135",
    browseName="EnumValues",
    parent="ns=plastics_dosing;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OFF"), description=o6.LocalizedText("Remote control switched off (local/HMI control)")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("SEPARATE_INTERFACE"),
            description=o6.LocalizedText("Using a separate interface from the production machine for remote controlling this dosing device"),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("OPC_UA"), description=o6.LocalizedText("Using this OPC UA connection for remote controlling this dosing device")
        ),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6018",
    browseName="ns=plastics_dosing;MaterialClass",
    description="Provides information about the material class, which can be used for the recipe calculation by the server or client.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6019",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MAIN"), description=o6.LocalizedText("Main material")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ADDITIVE"), description=o6.LocalizedText("Additive e.g. coloring material")),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("REGRIND_CLOSED_LOOP"),
                        description=o6.LocalizedText(
                            "Regrind with known composition, which is already considered in the internal dosing control and therefore excluded from the recipe calculation."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("REGRIND_OPEN_LOOP"),
                        description=o6.LocalizedText("Regrind with unknown composition. Included in the recipe calculation."),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6140", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.DosingMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6018"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6141",
    browseName="EnumValues",
    parent="ns=plastics_dosing;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OFF"), description=o6.LocalizedText("Remote control switched off (local/HMI control)")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("SEPARATE_INTERFACE"),
            description=o6.LocalizedText("Using a separate interface from the production machine for remote controlling this dosing device"),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("OPC_UA"), description=o6.LocalizedText("Using this OPC UA connection for remote controlling this dosing device")
        ),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6032",
    browseName="ns=plastics_dosing;MixingMode",
    description="Can be used to set the required mixing mode.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6051",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_MIXING"), description=o6.LocalizedText("No mixer available or mixing OFF")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("CONTINUOUS_MIXING"),
                        description=o6.LocalizedText("Mixer is activated after the first batch (blender) and is mixing continuous until the dosing device is stopped"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("TIMED_MIXING"),
                        description=o6.LocalizedText("The mixer is started after each batch (blender) and mixes for a defined duration (MixingDuration 9.4)"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("INTERVAL_MIXING"),
                        description=o6.LocalizedText(
                            "The mixer device is started after a defined number of shots, IMM (MixingInterval 9.3). Duration of mixing is set by MixingDuration"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6143", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.MixingType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6032"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6144",
    browseName="EnumValues",
    parent="ns=plastics_dosing;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("ONLY_CONVEYING"),
            description=o6.LocalizedText(
                "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
        ),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6145",
    browseName="ns=plastics_dosing;MixingMode",
    description="Can be used to set the required mixing mode.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6146",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_MIXING"), description=o6.LocalizedText("No mixer available or mixing OFF")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("CONTINUOUS_MIXING"),
                        description=o6.LocalizedText("Mixer is activated after the first batch (blender) and is mixing continuous until the dosing device is stopped"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("TIMED_MIXING"),
                        description=o6.LocalizedText("The mixer is started after each batch (blender) and mixes for a defined duration (MixingDuration 9.4)"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("INTERVAL_MIXING"),
                        description=o6.LocalizedText(
                            "The mixer device is started after a defined number of shots, IMM (MixingInterval 9.3). Duration of mixing is set by MixingDuration"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6147", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6054",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6152", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6153",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6154", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6155", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6165",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6166", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6167", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6174",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6175", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6176", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6157",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6158", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6159",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6160", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6182", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6161",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6162", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6163",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6184", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6168",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6169", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6170",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6171", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6172",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6173", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6177",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6178", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6188", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6179",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6180", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_dosing;i=6055",
    browseName="ns=plastics_dosing;TestWeight",
    description="Weight of the material of this component.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6056", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6192", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6193", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6194", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.WeighingProcessType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6055"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6053",
    browseName="ns=plastics_dosing;BulkDensity",
    description="Bulk density of the material which is dosed (not to be confused with the density of the material itself defined in MaterialType).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6148", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6195", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6196", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6197", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6198", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6053"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6071",
    browseName="ns=plastics_dosing;DosingMode",
    description="Provides information, how the dosing of the component is controlled.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6072",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("ONLY_CONVEYING"),
                        description=o6.LocalizedText(
                            "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6073", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6199", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6200", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6071"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6201",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6202", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6203",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6205",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6206", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5021",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the component.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6201"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6203"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6205"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6207", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5021"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6208",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6209", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6210", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6220",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6221", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6222", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6229",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6230", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6231", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6100",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6212",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6213", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6237", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6214",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6215", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6238", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6216",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6217", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6218",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6219", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6240", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6223",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6241", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6225",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6242", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6227",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6228", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6232",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6233", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6244", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6234",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6235", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6150",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6190", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6246", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6247", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_dosing_objtypes.DosingMaintenanceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6150"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6061",
    browseName="ns=plastics_dosing;Scrap",
    description="Total mass or volume of fed scrap since last reset.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6062", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6249", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6250", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6251", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6252", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_dosing_objtypes.MaterialConsumptionType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6061"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6059",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6253", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6254", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6255", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6256", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_dosing_objtypes.MaterialConsumptionType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6059"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6078",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6257", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6258", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6259", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6260", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6261",
    browseName="ns=plastics_dosing;Scrap",
    description="Total mass or volume of fed scrap since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6262", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6263", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6265", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6266", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6069",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6267", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6268", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6269", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6270", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6271",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6272", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6273", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6299", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6300", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6052",
    browseName="ns=plastics_dosing;Weight",
    description="Weight of the Material (e.g. inside the hopper).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6149", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6305", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6306", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6307", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6308", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=6052"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6093",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6094", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6309", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6310", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6311", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6312", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6313",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6314", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6315", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6341", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6342", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6088",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6089", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6347", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6348", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6349", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6350", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6351",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6352", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6353", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6379", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6380", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6355",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6356", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6384", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6385", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6386", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6387", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6357",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6358", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6388", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6390", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6391", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6359",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6360", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6392", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6394", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6395", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6361",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6396", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6397", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6398", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6399", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6363",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6364", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6365", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6400", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6401", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6366",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6367", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6402", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6403", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6404", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6405", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6368",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6369", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6406", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6408", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6409", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6370",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6371", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6410", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6411", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6412", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6413", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6372",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6373", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6374", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6414", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6415", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6375",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6376", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6416", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6417", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6418", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6419", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_dosing;i=6081",
    browseName="ns=plastics_dosing;TestWeight",
    description="Weight of the material of this component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6083", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6423", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6424", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6425", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_dosing_objtypes.WeighingProcessType(
    nodeId="ns=plastics_dosing;i=5026",
    browseName="ns=plastics_dosing;WeighingProcess",
    description="The weighing process can be used to perform a material pre-calibration or to determine the feedrate of the dosing system used by this component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6132",
                browseName="ns=plastics_dosing;WeighingTime",
                description="Duration of the weighing process.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6081"]),
    ],
)
o6.reference(plastics_dosing_objtypes.ContinuousComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5026"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6109",
    browseName="ns=plastics_dosing;DosingMode",
    description="Provides information, how the dosing of the component is controlled.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6110",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("ONLY_CONVEYING"),
                        description=o6.LocalizedText(
                            "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6111", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6426", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6427", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6077",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_dosing_objtypes.DosingMaterialType(
    nodeId="ns=plastics_dosing;i=5022",
    browseName="ns=plastics_dosing;Material",
    description="Information about the material used in the component.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6435", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6436", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6074"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6077"]),
    ],
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5022"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6428",
    browseName="ns=plastics_dosing;BulkDensity",
    description="Bulk density of the material which is dosed (not to be confused with the density of the material itself defined in MaterialType).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6429", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6445", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6446", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6447", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6448", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_dosing;i=6136",
    browseName="ns=plastics_dosing;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Dosing/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6137", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Dosing/")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6457",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Dosing/" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Dosing/" DefaultByteOrder="LittleEndian" xmlns:ua="http://opcfoundation.org/UA/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:opc="http://opcfoundation.org/BinarySchema/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType Name="ActivateRemoteControl" LengthInBits="32">\n  <opc:EnumeratedValue Name="OFF" Value="0"/>\n  <opc:EnumeratedValue Name="SEPARATE_INTERFACE" Value="1"/>\n  <opc:EnumeratedValue Name="OPC_UA" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="ComponentStateEnumeration" LengthInBits="32">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Ready" Value="1"/>\n  <opc:EnumeratedValue Name="Dosing" Value="2"/>\n  <opc:EnumeratedValue Name="Calibration" Value="3"/>\n  <opc:EnumeratedValue Name="Error" Value="4"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="5"/>\n  <opc:EnumeratedValue Name="Purging" Value="6"/>\n  <opc:EnumeratedValue Name="Priming" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="DosingModeEnumeration" LengthInBits="32">\n  <opc:EnumeratedValue Name="ONLY_CONVEYING" Value="0"/>\n  <opc:EnumeratedValue Name="VOLUMETRIC" Value="1"/>\n  <opc:EnumeratedValue Name="GRAVIMETRIC" Value="2"/>\n  <opc:EnumeratedValue Name="OTHER" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="RemoteControlActivated" LengthInBits="32">\n  <opc:EnumeratedValue Name="OFF" Value="0"/>\n  <opc:EnumeratedValue Name="SEPARATE_INTERFACE" Value="1"/>\n  <opc:EnumeratedValue Name="OPC_UA" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_dosing;i=6138",
    browseName="ns=plastics_dosing;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Dosing/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6139", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Dosing/Types.xsd"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6458",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Dosing/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Dosing/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ActivateRemoteControl">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFF_0"/>\n   <xs:enumeration value="SEPARATE_INTERFACE_1"/>\n   <xs:enumeration value="OPC_UA_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ActivateRemoteControl" name="ActivateRemoteControl"/>\n <xs:complexType name="ListOfActivateRemoteControl">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:ActivateRemoteControl" minOccurs="0" name="ActivateRemoteControl" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfActivateRemoteControl" name="ListOfActivateRemoteControl"/>\n <xs:simpleType name="ComponentStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Ready_1"/>\n   <xs:enumeration value="Dosing_2"/>\n   <xs:enumeration value="Calibration_3"/>\n   <xs:enumeration value="Error_4"/>\n   <xs:enumeration value="Cleaning_5"/>\n   <xs:enumeration value="Purging_6"/>\n   <xs:enumeration value="Priming_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ComponentStateEnumeration" name="ComponentStateEnumeration"/>\n <xs:complexType name="ListOfComponentStateEnumeration">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:ComponentStateEnumeration" minOccurs="0" name="ComponentStateEnumeration" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfComponentStateEnumeration" name="ListOfComponentStateEnumeration"/>\n <xs:simpleType name="DosingModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ONLY_CONVEYING_0"/>\n   <xs:enumeration value="VOLUMETRIC_1"/>\n   <xs:enumeration value="GRAVIMETRIC_2"/>\n   <xs:enumeration value="OTHER_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DosingModeEnumeration" name="DosingModeEnumeration"/>\n <xs:complexType name="ListOfDosingModeEnumeration">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:DosingModeEnumeration" minOccurs="0" name="DosingModeEnumeration" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfDosingModeEnumeration" name="ListOfDosingModeEnumeration"/>\n <xs:simpleType name="RemoteControlActivated">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFF_0"/>\n   <xs:enumeration value="SEPARATE_INTERFACE_1"/>\n   <xs:enumeration value="OPC_UA_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RemoteControlActivated" name="RemoteControlActivated"/>\n <xs:complexType name="ListOfRemoteControlActivated">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:RemoteControlActivated" minOccurs="0" name="RemoteControlActivated" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfRemoteControlActivated" name="ListOfRemoteControlActivated"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6275",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6276", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6304", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6442", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6461", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6277",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6278", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6462", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6463", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6464", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6465", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6279",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6280", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6466", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6467", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6468", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6469", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6281",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6282", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6470", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6471", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6472", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6473", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6283",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6284", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6285", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6474", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6475", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6286",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6287", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6476", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6477", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6478", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6479", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6288",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6480", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6481", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6482", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6483", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6290",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6291", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6484", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6485", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6486", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6487", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6443",
    browseName="ns=plastics_dosing;Weight",
    description="Weight of the Material (e.g. inside the hopper).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6489", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6490", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6491", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6492", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6459",
    browseName="ns=plastics_dosing;Scrap",
    description="Total mass or volume of fed scrap since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6460", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6521", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6522", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6523", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6524", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6438",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6439", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6525", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6526", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6527", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6528", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6292",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6293", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6294", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6488", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6529", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6295",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6296", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6530", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6531", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6532", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6533", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6297",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6534", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6535", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6536", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6537", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=plastics_dosing;i=6437",
    browseName="ns=plastics_dosing;TestWeight",
    description="Weight of the material of this component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6549", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6550", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6317",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6318", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6346", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6580", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6581", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6319",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6320", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6582", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6583", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6584", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6585", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6114",
    browseName="ns=plastics_dosing;DosingMode",
    description="Provides information, how the dosing of the component is controlled.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6115",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("ONLY_CONVEYING"),
                        description=o6.LocalizedText(
                            "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6116", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6589", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6590", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6321",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6322", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6586", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6587", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6588", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6593", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_dosing_objtypes.WeighingProcessType(
    nodeId="ns=plastics_dosing;i=5048",
    browseName="ns=plastics_dosing;WeighingProcess",
    description="The weighing process can be used to perform a material pre-calibration or to determine the feedrate of the dosing system used by this component.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6597",
                browseName="ns=plastics_dosing;WeighingTime",
                description="Duration of the weighing process.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6437"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6598",
    browseName="ns=plastics_dosing;BulkDensity",
    description="Bulk density of the material which is dosed (not to be confused with the density of the material itself defined in MaterialType).",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6599", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6591",
    browseName="ns=plastics_dosing;BulkDensity",
    description="Bulk density of the material which is dosed (not to be confused with the density of the material itself defined in MaterialType).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6592", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6608", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6609", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6610", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6611", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6612",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6107", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6118", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6124", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6613", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6026",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6033", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6538", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6605", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6624", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6606",
    browseName="ns=plastics_dosing;Weight",
    description="Weight of the Material (e.g. inside the hopper).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6607", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6652", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6653", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6654", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6655", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6622",
    browseName="ns=plastics_dosing;Scrap",
    description="Total mass or volume of fed scrap since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6623", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6684", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6685", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6686", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6687", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6601",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6602", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6688", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6689", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6690", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6691", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6625",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6626", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6627", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6693", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6694", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6629",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6630", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6698", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6700", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6701", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6712",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6713", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6714",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6715", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6716",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6717", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5019",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the DosingSystem.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6712"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6714"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6716"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6718", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5019"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6040",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6126", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6248", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6430", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6456", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6719", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6721",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6722", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6725", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6723",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6724", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6726", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6323",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6324", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6619", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6620", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6621", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6727", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6325",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6326", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6327", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6728", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6729", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6614",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6125", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6615", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6731", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6732", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6733", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_dosing_objtypes.MixingType(
    nodeId="ns=plastics_dosing;i=5012",
    browseName="ns=plastics_dosing;Mixing",
    description="In case the dosing station is equipped with an active mixing device like a batch blender, this object provides information about the mixing process.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6738",
                browseName="ns=plastics_dosing;MixingDuration",
                description="Duration of a mixing process.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6739",
                browseName="ns=plastics_dosing;MixingInterval",
                description="Interval between two mixing processes, in number of shots.",
                dataType=o6.UInt16,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6145"]),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5012"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6616",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6617", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6734", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6735", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6736", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6755", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5040",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6612"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6614"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6616"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6618", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6757",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6758", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5051",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=6757"])],
)
plastics_dosing_objtypes.LevelsType(
    nodeId="ns=plastics_dosing;i=5050",
    browseName="ns=plastics_dosing;Levels",
    description="Information about the filling of the dosing component.",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=5051"])],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6759",
    browseName="ns=plastics_rubber;Density",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6760", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6328",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6329", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6730", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6737", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6761", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6762", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6330",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6331", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6763", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6764", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6765", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6766", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6332",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6333", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6767", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6768", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6769", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6770", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6334",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6335", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6336", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6771", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6772", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6337",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6338", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6773", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6774", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6775", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6776", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6339",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6340", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6777", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6778", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6779", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6780", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6377",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6378", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6420", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6422", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6781", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6086",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6087", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6782", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6783", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6784", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6785", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6786",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6787", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6788", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6814", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6815", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6790",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6791", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6819", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6820", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6821", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6822", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6792",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6793", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6823", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6824", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6825", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6826", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6794",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6795", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6827", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6828", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6829", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6830", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6796",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6797", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6831", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6832", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6833", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6834", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6798",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6799", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6800", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6835", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6836", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6838",
    browseName="ns=plastics_dosing;MaterialClass",
    description="Provides information about the material class, which can be used for the recipe calculation by the server or client.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6839",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MAIN"), description=o6.LocalizedText("Main material")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ADDITIVE"), description=o6.LocalizedText("Additive e.g. coloring material")),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("REGRIND_CLOSED_LOOP"),
                        description=o6.LocalizedText(
                            "Regrind with known composition, which is already considered in the internal dosing control and therefore excluded from the recipe calculation."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("REGRIND_OPEN_LOOP"),
                        description=o6.LocalizedText("Regrind with unknown composition. Included in the recipe calculation."),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6840", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_dosing_objtypes.DosingMaterialType(
    nodeId="ns=plastics_dosing;i=5052",
    browseName="ns=plastics_dosing;Material",
    description="Information about the material used in the component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6837", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6841", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6759"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6838"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6842",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6843", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6845",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6846", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5067",
    browseName="ns=plastics_dosing;Throughput",
    description="Material Output per time.",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=6845"])],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6847",
    browseName="ns=plastics_dosing;Weight",
    description="Weight of the Material (e.g. inside the hopper).",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6848", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6849",
    browseName="ns=plastics_dosing;DosingMode",
    description="Provides information, how the dosing of the component is controlled.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6850",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(
                        value=0,
                        displayName=o6.LocalizedText("ONLY_CONVEYING"),
                        description=o6.LocalizedText(
                            "The throughput is not controlled. The feeder only transports the material (e.g. by screw, conveyor belt) or the material is only falling through a feed opening."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=1, displayName=o6.LocalizedText("VOLUMETRIC"), description=o6.LocalizedText("The throughput is controlled by a volumetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2, displayName=o6.LocalizedText("GRAVIMETRIC"), description=o6.LocalizedText("The throughput is controlled by a gravimetric dosing system.")
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Throughput is controlled, but in another mode than these above.")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6851", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6856", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6857", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6631",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6632", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6852", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6853", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6872", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6873", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6633",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6634", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6874", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6875", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6876", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6877", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6635",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6636", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6878", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6879", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6880", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6881", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6637",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6638", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6639", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6882", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6883", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6640",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6641", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6884", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6885", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6886", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6887", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6642",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6643", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6888", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6889", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6890", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6891", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6644",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6645", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6892", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6893", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6894", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6895", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6646",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6647", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6648", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6896", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6897", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6801",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6802", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6867", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6868", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6869", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6904", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6858",
    browseName="ns=plastics_dosing;BulkDensity",
    description="Bulk density of the material which is dosed (not to be confused with the density of the material itself defined in MaterialType).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6859", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6912", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6913", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6914", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6915", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6649",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6650", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6898", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6899", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6943", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6944", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6651",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6692", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6945", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6946", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6947", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6948", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6034",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6949", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6950", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6951", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6952", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=plastics_dosing;i=5002",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6008",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6009",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6010",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6968",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6969",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6970",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6971",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6972",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6973",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6974",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6975",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6976",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6977",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6978",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6980",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(
                nodeId="ns=plastics_dosing;i=6979", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.DosingSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=plastics_dosing;i=5002"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=plastics_dosing;i=6983",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6984", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=plastics_dosing;i=5007",
    browseName="ns=machinery;MachineryItemState",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6020"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6981", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6982", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6983"]),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=plastics_dosing;i=6987",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6988", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=plastics_dosing;i=5008",
    browseName="ns=machinery;MachineryOperationMode",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6022"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6985", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6986", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6987"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=plastics_dosing;i=5003",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=plastics_dosing;i=5007"]), o6.hasAddIn(o6.ns["ns=plastics_dosing;i=5008"])],
)
o6.reference(plastics_dosing_objtypes.DosingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5003"])
o6.reference(o6.ns["ns=plastics_dosing;i=5003"], "i=17604", o6.ns["ns=plastics_dosing;i=5002"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6803",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6804", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6905", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6906", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6993", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6994", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6910",
    browseName="ns=plastics_dosing;Weight",
    description="Weight of the Material (e.g. inside the hopper).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6911", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6990", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6991", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6992", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6995", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.NodeId("i=13"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=o6.NodeId("i=8912"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7001",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6012"]),
)

plastics_dosing_objtypes.DosingMaintenanceType(
    nodeId="ns=plastics_dosing;i=5015",
    browseName="ns=plastics_dosing;Maintenance",
    description="Information on the maintenance status of the dosing system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6127",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6720",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6040"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6721"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6723"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7008", browseName="ns=plastics_rubber;Reset", description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0"
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5015"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7009",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6043"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6044"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6045",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6046",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7010",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6045"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6046"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6047",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6048",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7011",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6047"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6048"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_dosing;i=5018",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6042", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7009"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7010"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7011"]),
    ],
    eventNotifier=1,
)
plastics_dosing_objtypes.MaterialConsumptionType(
    nodeId="ns=plastics_dosing;i=5023",
    browseName="ns=plastics_dosing;MaterialConsumption",
    description="Information about the material consumption of the component.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6078"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6261"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7016", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5023"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5032",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6156",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6054"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6153"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6157"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6159"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6161"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6163"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6165"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6168"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6170"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6172"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6174"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6177"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6179"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7025",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.LevelsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5032"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5033",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6211",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6208"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6212"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6214"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6216"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6218"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6220"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6223"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6225"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6227"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6229"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6232"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6234"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7026",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_dosing_objtypes.LevelsType(
    nodeId="ns=plastics_dosing;i=5024",
    browseName="ns=plastics_dosing;Levels",
    description="Information about the filling of the dosing component.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5033"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7027", browseName="ns=plastics_dosing;AbortFilling", description="Method to abort filling the Component.")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7028",
                browseName="ns=plastics_dosing;StartFilling",
                description="Method to fill the Component up to the MaxValue of the MonitoredParameterType in the Level Variable.",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5024"])
plastics_dosing_objtypes.MaterialConsumptionType(
    nodeId="ns=plastics_dosing;i=5038",
    browseName="ns=plastics_dosing;MaterialConsumption",
    description="Information about the material consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6438"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6459"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7035", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
        ),
    ],
)
plastics_dosing_objtypes.MaterialConsumptionType(
    nodeId="ns=plastics_dosing;i=5044",
    browseName="ns=plastics_dosing;MaterialConsumption",
    description="Information about the material consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6601"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6622"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7044", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5039",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6301",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6302",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6303",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7039",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7048", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5020",
    browseName="ns=plastics_dosing;Throughput",
    description="Material Output per time.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6274",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5039"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6069"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6275"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6277"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6279"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6281"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6283"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6286"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6288"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6290"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6292"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6295"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6297"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7029",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.ComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5020"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6741",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Components", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7050",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6741"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6743",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7051",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6743"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_dosing;i=5017",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6041",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6740",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6742",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7050"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7051"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6744",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6745",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7052",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6744"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6745"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6747",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="NameFilter", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="MouldId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6748",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7053",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6747"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6748"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6749",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=plastics_dosing;i=7054", browseName="ns=plastics_rubber;SendProductionDatasetList", inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6749"]))

plastics_rubber.objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_dosing;i=5047",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=7053"]), o6.hasComponent(o6.ns["ns=plastics_dosing;i=7054"])],
    eventNotifier=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6750",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7055",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6750"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6752",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Components", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7056",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6752"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6754",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7057",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6754"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_dosing;i=5046",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6746",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6751",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6753",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7056"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7057"]),
    ],
)
plastics_rubber.objtypes.ProductionDatasetManagementType(
    nodeId="ns=plastics_dosing;i=5016",
    browseName="ns=plastics_dosing;ProductionDataSetManagement",
    description="Provides functionalities for the management of recipes/machine settings.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5017"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5046"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5047"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7052"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7055"]),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5016"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5062",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6343",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6344",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6345",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7058",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7059", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5028",
    browseName="ns=plastics_dosing;Percentage",
    description="Part (%) of the recipe dosed by this component (recipe).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6316",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5062"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6093"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6313"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6317"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6319"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6321"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6323"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6325"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6328"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6330"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6332"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6334"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6337"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6339"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7030",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.BatchComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5028"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6963",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6964",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=o6.NodeId("i=30"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7068",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6963"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6964"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6965",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6966",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=o6.NodeId("i=30"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7069",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6965"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6966"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_dosing;i=5004",
    browseName="ns=plastics_dosing;MachineConfiguration",
    description="represents the current configuration of the Dosing System.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6011",
                browseName="ns=plastics_rubber;LocationName",
                description="Description of the location of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6013",
                browseName="ns=plastics_rubber;TimeZoneOffset",
                description="Difference of the local time to Coordinated Universal Time (UTC) given by the machine operator or OPC client",
                dataType=ns0.datatypes.TimeZoneDataType,
                value=ns0.datatypes.TimeZoneDataType(offset=0, daylightSavingInOffset=False),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6014",
                browseName="ns=plastics_rubber;UserMachineName",
                description="Description of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6967",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7001"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7068"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7069"]),
    ],
)
o6.reference(plastics_dosing_objtypes.DosingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5004"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7082",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7080",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7081"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7082"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7084",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7085",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7083",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7084"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7085"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7087",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7088",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId("i=17"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7086",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7087"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7088"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_dosing;i=5061",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7079", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7080"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7083"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7086"]),
    ],
    eventNotifier=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7091",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7090",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Id", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("Id of the error, listed in ActiveErrors, that shall be reset.")
        )
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7090",
    browseName="ns=plastics_dosing;ResetErrorById",
    description="Method to reset one error of the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7091"]),
)

plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5063",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6381",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6382",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6383",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7032",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7092", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5027",
    browseName="ns=plastics_dosing;DrivePercentage",
    description="Relative value (0-100%) of the maximum drive power of the component drive.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6354",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5063"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6088"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6351"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6355"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6357"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6359"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6361"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6363"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6366"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6368"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6370"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6372"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6375"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6377"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7031",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.ContinuousComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5027"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5066",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6816",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6817",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6818",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7094",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7098", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6805",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6806", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7099", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7100", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7101", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7102", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6807",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6808", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6809", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7103", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7104", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6810",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6811", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7105", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7106", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7107", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7108", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6812",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6813", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7109", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7111", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7112", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5025",
    browseName="ns=plastics_dosing;Percentage",
    description="Part (%) of the recipe dosed by this component (recipe).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6789",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5066"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6086"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6786"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6790"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6792"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6794"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6796"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6798"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6801"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6803"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6805"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6807"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6810"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6812"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7093",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.ContinuousComponentType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5025"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5045",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6695",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6696",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6697",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7113",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7114", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5010",
    browseName="ns=plastics_dosing;Throughput",
    description="Current throughput of the DosingSystem in mass or volume per time.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6628",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5045"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6026"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6625"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6629"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6631"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6633"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6635"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6637"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6640"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6642"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6644"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6646"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6649"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6651"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7066",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5010"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7147",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7148",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7146",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7147"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7148"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7151",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7150",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="NameFilter", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="MouldId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7152",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7150",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7150",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7151"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7152"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7154",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7153",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=plastics_dosing;i=7153", browseName="ns=plastics_rubber;SendProductionDatasetList", inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7154"]))

plastics_rubber.objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_dosing;i=5065",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=7150"]), o6.hasComponent(o6.ns["ns=plastics_dosing;i=7153"])],
    eventNotifier=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7156",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7155",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7155",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7156"]),
)

ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7115",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7116", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7117", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7171", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7172", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5053",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7173",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7176",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7177",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7174",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7175", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7119",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7178", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7180", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7181", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7121",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7122", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7182", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7184", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7185", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7123",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7124", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7186", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7187", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7188", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7189", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7125",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7126", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7190", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7192", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7193", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7127",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7128", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7143", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7194", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7195", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7158",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7159", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7196", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7198", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7199", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7160",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7161", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7200", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7202", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7203", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7162",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7204", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7205", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7206", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7207", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7164",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7165", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7166", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7208", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7209", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7167",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7168", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7210", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7212", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7213", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7169",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7170", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7214", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7216", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7217", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5011",
    browseName="ns=plastics_dosing;ShotWeight",
    description="Current shotweight of the parts produced by the production machine in mass.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7118",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5053"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6034"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7115"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7119"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7121"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7123"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7125"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7127"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7157",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7158"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7160"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7162"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7164"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7167"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7169"]),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5011"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6551",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6552", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6553", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7218", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7219", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5054",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7220",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7223",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7224",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7221",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7222", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6595",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6596", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7142", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7228", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7229", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6656",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6657", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6658", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7230", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7231", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6660",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6661", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6703", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7232", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7233", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7234", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7238",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7237",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Components", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7237",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7238"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7241",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7240",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7240",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7241"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_dosing;i=5060",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7078",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7236",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7239",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7237"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7240"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7244",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7243",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Components", dataType=o6.NodeId("i=5"), valueRank=1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7243",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7244"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=7247",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7246",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7246",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=7247"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_dosing;i=5064",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7149",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[""],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7242",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7245",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7243"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7246"]),
    ],
)
plastics_rubber.objtypes.ProductionDatasetManagementType(
    nodeId="ns=plastics_dosing;i=5059",
    browseName="ns=plastics_dosing;ProductionDataSetManagement",
    description="Provides functionalities for the management of recipes/machine settings.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5060"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5061"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5064"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5065"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7146"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7155"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6555",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6556", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7248", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7250", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7251", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6557",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6558", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7252", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7253", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7254", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7255", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6559",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6560", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7256", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7258", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7259", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6561",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6562", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7260", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7261", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7262", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7263", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6563",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6564", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6565", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7264", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7265", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6566",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6567", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7266", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7267", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7268", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7269", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6568",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6569", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7270", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7271", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7272", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7273", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6570",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6571", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7274", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7275", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7276", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7277", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6572",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6573", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6574", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7278", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7279", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6575",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6576", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7280", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7281", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7282", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7283", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6577",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6578", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7284", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7285", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7286", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7287", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5013",
    browseName="ns=plastics_dosing;BatchWeight",
    description="Target batch weight for batch blenders in absolute values.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6554",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5054"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6036"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6551"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6555"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6557"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6559"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6561"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6563"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6566"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6568"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6570"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6572"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6575"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6577"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7041",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5013"])
plastics_dosing_objtypes.MaterialConsumptionType(
    nodeId="ns=plastics_dosing;i=5057",
    browseName="ns=plastics_dosing;MaterialConsumption",
    description="Information about the material consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6842"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7289", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
        ),
    ],
)
plastics_dosing_objtypes.ContinuousComponentType(
    nodeId="ns=plastics_dosing;i=5006",
    browseName="ns=plastics_dosing;Feeder",
    description="A feeder can be used for starve feeding (under feeding) of a production machine.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6105",
                browseName="ns=plastics_dosing;IsPresent",
                description="Indicates if the hardware of this component is installed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6600",
                browseName="ns=plastics_dosing;FeedRateScalingFactor",
                description="Material-specific output of the Component per DrivePercentage.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6756",
                browseName="ns=plastics_dosing;IsActive",
                description="Provides information if the dosing component is active in the current production.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5037"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5043"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5048"]),
        o6.hasComponent(
            plastics_rubber.objtypes.EnergyType(
                nodeId="ns=plastics_dosing;i=5049",
                browseName="ns=plastics_dosing;ElectricalEnergy",
                description="Information about the electrical power and energy consumption of the component.",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5050"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5052"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5067"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6095"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6106",
                browseName="ns=plastics_dosing;State",
                description="The actual working state of the component.",
                dataType=plastics_dosing_datypes.ComponentStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6598"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6844",
                browseName="ns=plastics_dosing;SetActive",
                description="Activates the dosing component for the current production.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6847"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7064", browseName="ns=plastics_dosing;StartPriming", description="Method to start the priming function on the component.")
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7065", browseName="ns=plastics_dosing;StopPriming", description="Method to stop the priming function on the component.")
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7067", browseName="ns=plastics_dosing;AbortCalibration", description="Abort the current calibration sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7095", browseName="ns=plastics_dosing;AbortCleaning", description="Method without arguments to abort the current cleaning sequence."
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7288",
                browseName="ns=plastics_dosing;IdentifyComponent",
                description="The dosing component on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7290", browseName="ns=plastics_dosing;StartCalibration", description="Start the automated calibration sequence for this component."
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7291", browseName="ns=plastics_dosing;StartCleaning", description="Start the automated cleaning sequence for this component.")
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.DosingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5006"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6916",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6917", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7000", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7305", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7306", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6918",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6919", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7307", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7308", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7309", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7310", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6920",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6921", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7311", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7312", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7313", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7314", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5077",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6916"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6918"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6920"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6922", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6864",
    browseName="ns=plastics_rubber;Density",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6865", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7344", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7345", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7346", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7347", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6870",
    browseName="ns=plastics_dosing;MaterialClass",
    description="Provides information about the material class, which can be used for the recipe calculation by the server or client.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6871",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MAIN"), description=o6.LocalizedText("Main material")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ADDITIVE"), description=o6.LocalizedText("Additive e.g. coloring material")),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("REGRIND_CLOSED_LOOP"),
                        description=o6.LocalizedText(
                            "Regrind with known composition, which is already considered in the internal dosing control and therefore excluded from the recipe calculation."
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("REGRIND_OPEN_LOOP"),
                        description=o6.LocalizedText("Regrind with unknown composition. Included in the recipe calculation."),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6900", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7348", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7349", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_dosing_objtypes.DosingMaterialType(
    nodeId="ns=plastics_dosing;i=5080",
    browseName="ns=plastics_dosing;Material",
    description="Information about the material used in the component.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6866", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6901", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6864"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6870"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6924",
    browseName="ns=plastics_dosing;Scrap",
    description="Total mass or volume of fed scrap since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6925", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7350", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7351", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7352", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7353", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6902",
    browseName="ns=plastics_dosing;TotalConsumption",
    description="Total mass or volume of fed material (good + scrap) since last reset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6903", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7354", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7355", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7356", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7357", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_dosing_objtypes.MaterialConsumptionType(
    nodeId="ns=plastics_dosing;i=5081",
    browseName="ns=plastics_dosing;MaterialConsumption",
    description="Information about the material consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6902"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6924"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7298", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6908",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6909", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7358", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7359", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7360", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7361", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6926",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6927", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6928", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7362", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7363", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5083",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7364",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7367",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7368",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7365",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7366", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6930",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6931", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7369", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7371", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7372", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6932",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6933", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7373", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7374", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7375", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7376", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6934",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6935", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7377", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7378", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7379", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7380", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6936",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6937", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7381", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7382", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7383", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7384", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6938",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6939", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6940", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7385", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7386", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6941",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6942", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7387", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7388", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7389", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7390", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6953",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6954", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7391", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7392", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7393", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7394", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6955",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6956", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7395", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7396", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7397", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7398", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6957",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6958", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6959", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7399", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7400", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6960",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6961", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7401", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7402", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7403", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7404", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6962",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6989", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7405", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7406", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7407", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7408", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5082",
    browseName="ns=plastics_dosing;Throughput",
    description="Material Output per time.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6929",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5083"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6908"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6926"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6930"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6932"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6934"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6936"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6938"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6941"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6953"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6955"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6957"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6960"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6962"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7303",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6862",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6863", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7409", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7410", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7411", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7412", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7315",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7316", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7317", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7413", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7414", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7319",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7320", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7415", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7416", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7417", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7418", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7321",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7322", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7419", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7420", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7421", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7422", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=7129",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7130", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7424", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7425", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7426", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7427", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=7131",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7428", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7429", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7430", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7431", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=7133",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7134", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7432", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7433", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7434", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7435", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5055",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the DosingSystem.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7129"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7131"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7133"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=7135", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6997",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6998", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7436", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7437", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7438", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7137",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7138", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7439", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7440", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7441", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7139",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7140", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7442", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7443", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7444", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
plastics_dosing_objtypes.DosingMaintenanceType(
    nodeId="ns=plastics_dosing;i=5056",
    browseName="ns=plastics_dosing;Maintenance",
    description="Information on the maintenance status of the dosing system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6999",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7136",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6997"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7072", browseName="ns=plastics_rubber;Reset", description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0"
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7137"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7139"]),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7075",
    browseName="ns=plastics_dosing;MixingMode",
    description="Can be used to set the required mixing mode.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7076",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_MIXING"), description=o6.LocalizedText("No mixer available or mixing OFF")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("CONTINUOUS_MIXING"),
                        description=o6.LocalizedText("Mixer is activated after the first batch (blender) and is mixing continuous until the dosing device is stopped"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("TIMED_MIXING"),
                        description=o6.LocalizedText("The mixer is started after each batch (blender) and mixes for a defined duration (MixingDuration 9.4)"),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("INTERVAL_MIXING"),
                        description=o6.LocalizedText(
                            "The mixer device is started after a defined number of shots, IMM (MixingInterval 9.3). Duration of mixing is set by MixingDuration"
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7077", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7445", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7446", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_dosing_objtypes.MixingType(
    nodeId="ns=plastics_dosing;i=5058",
    browseName="ns=plastics_dosing;Mixing",
    description="In case the dosing station is equipped with an active mixing device like a batch blender, this object provides information about the mixing process.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7144",
                browseName="ns=plastics_dosing;MixingDuration",
                description="Duration of a mixing process.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7145",
                browseName="ns=plastics_dosing;MixingInterval",
                description="Interval between two mixing processes, in number of shots.",
                dataType=o6.UInt16,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7075"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=7423",
                browseName="ns=plastics_dosing;IdleMixing",
                description="With idle mixing the mixer of the batch blender rotates once in a while to keep the material in the mixer flowing and material does not get blocked by the mixer blades.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7447",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7448", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7541", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7543", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7544", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7454",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7455", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7456", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7545", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7546", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5072",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7547",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7550",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7551",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7548",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7549", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7458",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7552", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7553", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7554", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7555", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7460",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7461", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7556", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7557", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7558", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7559", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7462",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7463", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7560", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7561", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7562", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7563", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7464",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7465", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7564", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7565", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7566", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7567", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7466",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7467", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7468", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7568", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7569", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7470",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7471", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7570", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7571", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7572", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7573", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7472",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7473", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7574", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7575", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7576", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7577", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7474",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7475", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7578", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7580", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7581", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7476",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7477", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7478", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7582", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7583", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7479",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7480", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7584", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7585", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7586", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7587", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7481",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7482", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7588", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7589", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7590", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7591", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5069",
    browseName="ns=plastics_dosing;BatchWeight",
    description="Target batch weight for batch blenders in absolute values.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7457",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5072"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7447"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7454"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7458"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7460"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7462"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7464"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7466"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7469",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7470"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7472"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7474"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7476"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7479"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7481"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7450",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7451", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7592", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7593", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7594", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7595", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7483",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7484", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7485", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7596", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7597", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5073",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7598",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7601",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7602",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7599",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7600", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7487",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7488", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7603", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7605", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7606", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7489",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7490", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7607", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7608", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7609", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7610", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7491",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7492", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7611", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7612", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7613", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7614", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7493",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7494", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7615", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7616", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7617", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7618", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7495",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7496", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7497", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7619", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7620", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7499",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7500", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7621", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7622", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7623", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7624", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7501",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7502", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7625", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7626", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7627", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7628", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7503",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7504", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7629", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7630", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7631", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7632", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7505",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7506", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7507", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7633", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7634", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7508",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7635", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7636", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7637", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7638", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7510",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7511", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7639", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7640", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7641", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7642", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5070",
    browseName="ns=plastics_dosing;ShotWeight",
    description="Current shotweight of the parts produced by the production machine in mass.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7486",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5073"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7450"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7483"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7487"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7489"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7491"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7493"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7495"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7498",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7499"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7501"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7503"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7505"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7508"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7510"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7452",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7643", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7645", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7646", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7512",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7513", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7514", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7647", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7648", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5074",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7649",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7652",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7653",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7650",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7651", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7516",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7517", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7654", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7655", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7656", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7657", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7518",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7519", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7658", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7659", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7660", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7661", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7520",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7521", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7662", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7663", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7664", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7665", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7522",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7523", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7666", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7668", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7669", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7524",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7525", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7526", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7670", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7671", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7528",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7529", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7672", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7674", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7675", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7530",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7531", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7676", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7677", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7678", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7679", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7532",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7533", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7680", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7681", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7682", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7683", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7534",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7535", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7536", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7684", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7685", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7537",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7538", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7686", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7688", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7689", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7539",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7540", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7690", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7691", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7692", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7693", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5071",
    browseName="ns=plastics_dosing;Throughput",
    description="Current throughput of the DosingSystem in mass or volume per time.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7515",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5074"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7452"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7512"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7516"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7518"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7520"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7522"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7524"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7527",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7528"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7530"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7532"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7534"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7537"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7539"]),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6449",
    browseName="ns=plastics_rubber;ActualPower",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6450", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7695", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7696", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7697", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7698", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6451",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6452", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7699", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7700", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7701", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7702", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_dosing;i=6453",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6454", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7703", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7704", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7705", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7706", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_dosing;i=5034",
    browseName="ns=plastics_dosing;ElectricalEnergy",
    description="Information about the electrical power and energy consumption of the component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6449"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6451"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6453"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_dosing;i=6455", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7323",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7324", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7707", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7709", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7710", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6432",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6433", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6539", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7711", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7712", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7713", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6493",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6494", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6495", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7714", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7715", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6497",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6540", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7716", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7717", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7718", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6499",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6500", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6541", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7719", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7720", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7721", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6501",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6502", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7722", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7723", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7724", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6503",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6504", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6543", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7725", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7726", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7727", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6505",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6506", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6507", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7728", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7729", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6508",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6544", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7730", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7731", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7732", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6510",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6511", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6545", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7733", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7734", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7735", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6512",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6513", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6546", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7736", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7737", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7738", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6514",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6515", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6516", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7739", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7740", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6517",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6518", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6547", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7741", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7742", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7743", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6519",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6520", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6548", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7744", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7745", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7746", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5036",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6496",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6432"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6493"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6497"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6499"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6501"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6503"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6505"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6508"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6510"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6512"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6514"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6517"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6519"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7040",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_dosing_objtypes.LevelsType(
    nodeId="ns=plastics_dosing;i=5035",
    browseName="ns=plastics_dosing;Levels",
    description="Information about the filling of the dosing component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5036"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7037", browseName="ns=plastics_dosing;AbortFilling", description="Method to abort filling the Component.")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7038",
                browseName="ns=plastics_dosing;StartFilling",
                description="Method to fill the Component up to the MaxValue of the MonitoredParameterType in the Level Variable.",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=7694",
                browseName="ns=plastics_dosing;Filling",
                description="Flag to indicate if the hopper is being filled right now.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7748",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7749", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7779", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7780", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7781", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7782", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7750",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7751", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7752", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7783", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7784", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_dosing;i=5076",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7785",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7788",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7789",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7786",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7787", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7754",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7755", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7790", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7791", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7792", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7793", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7756",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7757", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7794", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7795", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7796", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7797", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7758",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7759", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7798", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7799", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7800", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7801", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7760",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7761", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7802", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7803", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7804", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7805", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7762",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7763", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7764", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7806", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7807", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7766",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7767", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7808", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7809", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7810", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7811", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7768",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7769", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7812", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7813", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7814", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7815", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7770",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7771", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7816", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7817", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7818", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7819", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7772",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7773", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7774", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7820", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7821", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7775",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7776", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7822", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7823", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7824", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7825", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7777",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7778", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7826", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7827", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7828", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7829", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5075",
    browseName="ns=plastics_dosing;Throughput",
    description="Material Output per time.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7753",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5076"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7748"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7750"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7754"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7756"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7758"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7760"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7762"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7765",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7766"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7768"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7770"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7772"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7775"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7777"]),
    ],
)
plastics_dosing_objtypes.ComponentType(
    nodeId="ns=plastics_dosing;i=5030",
    browseName="ns=plastics_dosing;<Component_Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6112",
                browseName="ns=plastics_dosing;IsPresent",
                description="Indicates if the hardware of this component is installed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6431",
                browseName="ns=plastics_dosing;IsActive",
                description="Provides information if the dosing component is active in the current production.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7747",
                browseName="ns=plastics_dosing;FeedRateScalingFactor",
                description="Material-specific output of the Component per DrivePercentage.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5034"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5035"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5038"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5075"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6097",
                browseName="ns=plastics_dosing;State",
                description="The actual working state of the component.",
                dataType=plastics_dosing_datypes.ComponentStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6109"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6428"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6440",
                browseName="ns=plastics_dosing;SetActive",
                description="Activates the dosing component for the current production.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6443"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7033", browseName="ns=plastics_dosing;AbortCleaning", description="Method without arguments to abort the current cleaning sequence."
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7034",
                browseName="ns=plastics_dosing;IdentifyComponent",
                description="The dosing component on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7036", browseName="ns=plastics_dosing;StartCleaning", description="Start the automated cleaning sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7074", browseName="ns=plastics_dosing;AbortCalibration", description="Abort the current calibration sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7141", browseName="ns=plastics_dosing;StartCalibration", description="Start the automated calibration sequence for this component."
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(plastics_dosing_objtypes.ComponentsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5030"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6662",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6663", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6704", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7235", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7830", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7831", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6664",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6665", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6705", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7832", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7833", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7834", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6666",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6667", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6706", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7835", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7836", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7837", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6668",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6669", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6670", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7838", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7839", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6671",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6672", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6707", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7840", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7841", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7842", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6673",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6674", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6708", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7843", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7844", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7845", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6675",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6676", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6709", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7846", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7847", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7848", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=6677",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6678", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6679", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7849", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7850", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6680",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6681", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6710", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7851", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7852", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7853", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=6682",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6683", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6711", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7854", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7855", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7856", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5042",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6659",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6595"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6656"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6660"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6664"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6666"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6668"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6671"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6673"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6675"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6677"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6680"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6682"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7049",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_dosing_objtypes.LevelsType(
    nodeId="ns=plastics_dosing;i=5041",
    browseName="ns=plastics_dosing;Levels",
    description="Information about the filling of the dosing component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5042"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6063",
                browseName="ns=plastics_dosing;Filling",
                description="Flag to indicate if the hopper is being filled right now.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7046", browseName="ns=plastics_dosing;AbortFilling", description="Method to abort filling the Component.")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7047",
                browseName="ns=plastics_dosing;StartFilling",
                description="Method to fill the Component up to the MaxValue of the MonitoredParameterType in the Level Variable.",
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7860",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7861", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.ControlledParameterType(
    nodeId="ns=plastics_dosing;i=5014",
    browseName="ns=plastics_dosing;Throughput",
    description="Material Output per time.",
    references=[o6.hasComponent(o6.ns["ns=plastics_dosing;i=7860"])],
)
plastics_dosing_objtypes.ComponentType(
    nodeId="ns=plastics_dosing;i=5029",
    browseName="ns=plastics_dosing;<Component_Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6117",
                browseName="ns=plastics_dosing;IsPresent",
                description="Indicates if the hardware of this component is installed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6594",
                browseName="ns=plastics_dosing;IsActive",
                description="Provides information if the dosing component is active in the current production.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7858",
                browseName="ns=plastics_dosing;FeedRateScalingFactor",
                description="Material-specific output of the Component per DrivePercentage.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5014"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5040"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5041"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5044"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6096",
                browseName="ns=plastics_dosing;State",
                description="The actual working state of the component.",
                dataType=plastics_dosing_datypes.ComponentStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6114"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6591"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6603",
                browseName="ns=plastics_dosing;SetActive",
                description="Activates the dosing component for the current production.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6606"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7042", browseName="ns=plastics_dosing;AbortCleaning", description="Method without arguments to abort the current cleaning sequence."
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7043",
                browseName="ns=plastics_dosing;IdentifyComponent",
                description="The dosing component on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7045", browseName="ns=plastics_dosing;StartCleaning", description="Start the automated cleaning sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7857", browseName="ns=plastics_dosing;AbortCalibration", description="Abort the current calibration sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7859", browseName="ns=plastics_dosing;StartCalibration", description="Start the automated calibration sequence for this component."
            )
        ),
    ],
    _allow_abstract=True,
)
plastics_dosing_objtypes.ComponentsType(
    nodeId="ns=plastics_dosing;i=5009",
    browseName="ns=plastics_dosing;Components",
    description="Container Object for all Components in the DosingSystem.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6119", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5029"]),
    ],
)
o6.reference(plastics_dosing_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5009"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7325",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7326", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7862", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7863", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7864", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7865", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7327",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7328", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7329", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7866", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7867", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7331",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7332", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7868", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7869", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7870", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7871", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7333",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7334", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7872", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7873", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7874", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7875", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7335",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7876", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7877", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7878", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7879", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_dosing;i=7337",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7338", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7339", browseName="ValueAsText", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7880", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7881", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7340",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7341", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7882", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7883", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7884", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7885", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_dosing;i=7342",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7343", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7886", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7887", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7888", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=7889", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_dosing;i=5079",
    browseName="ns=plastics_dosing;Level",
    description="The actual level of the material inside the component (e.g. actual hopper level).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=7318",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6862"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7315"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7319"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7321"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7323"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7325"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7327"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7330",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7331"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7333"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7335"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7337"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7340"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7342"]),
    ],
)
plastics_dosing_objtypes.LevelsType(
    nodeId="ns=plastics_dosing;i=5078",
    browseName="ns=plastics_dosing;Levels",
    description="Information about the filling of the dosing component.",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5079"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6923",
                browseName="ns=plastics_dosing;Filling",
                description="Flag to indicate if the hopper is being filled right now.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7301", browseName="ns=plastics_dosing;AbortFilling", description="Method to abort filling the Component.")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7302",
                browseName="ns=plastics_dosing;StartFilling",
                description="Method to fill the Component up to the MaxValue of the MonitoredParameterType in the Level Variable.",
            )
        ),
    ],
)
plastics_dosing_objtypes.ComponentType(
    nodeId="ns=plastics_dosing;i=5068",
    browseName="ns=plastics_dosing;<Component_Nr>",
    description="The ComponentType represents a device which brings material into the dosing system.",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6854",
                browseName="ns=plastics_dosing;IsPresent",
                description="Indicates if the hardware of this component is installed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6860",
                browseName="ns=plastics_dosing;FeedRateScalingFactor",
                description="Material-specific output of the Component per DrivePercentage.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6861",
                browseName="ns=plastics_dosing;IsActive",
                description="Provides information if the dosing component is active in the current production.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5077"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5078"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5080"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5081"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5082"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6849"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6855",
                browseName="ns=plastics_dosing;State",
                description="The actual working state of the component.",
                dataType=plastics_dosing_datypes.ComponentStateEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6858"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6907",
                browseName="ns=plastics_dosing;SetActive",
                description="Activates the dosing component for the current production.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=6910"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7295", browseName="ns=plastics_dosing;AbortCalibration", description="Abort the current calibration sequence for this component.")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7296", browseName="ns=plastics_dosing;AbortCleaning", description="Method without arguments to abort the current cleaning sequence."
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7297",
                browseName="ns=plastics_dosing;IdentifyComponent",
                description="The dosing component on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7299", browseName="ns=plastics_dosing;StartCalibration", description="Start the automated calibration sequence for this component."
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7300", browseName="ns=plastics_dosing;StartCleaning", description="Start the automated cleaning sequence for this component.")
        ),
    ],
    _allow_abstract=True,
)
plastics_dosing_objtypes.ComponentsType(
    nodeId="ns=plastics_dosing;i=5031",
    browseName="ns=plastics_dosing;Components",
    description="Container Object for all Components in the DosingSystem.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6120", browseName="NodeVersion", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5068"]),
    ],
)
plastics_dosing_objtypes.OperationType(
    nodeId="ns=plastics_dosing;i=5005",
    browseName="ns=plastics_dosing;Operation",
    description="Contains objects which are necessary to operate the DosingSystem.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6099",
                browseName="ns=plastics_dosing;HighestActiveAlarmSeverity",
                description="Indication of the severity of the highest active alarm.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_dosing;i=6996",
                browseName="ns=plastics_dosing;IsActive",
                description="The IsActive Property provides information if the dosing unit is active in the current production.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5031"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5055"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5069"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5070"]),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=5071"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6029", browseName="ns=plastics_dosing;RemoteControlOpcUa", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6030",
                browseName="ns=plastics_dosing;PurgeDuration",
                description="Duration of the purging function of the dosing system.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6098",
                browseName="ns=plastics_dosing;ActiveErrors",
                description="List of the active errors of the device.",
                dataType=plastics_rubber.datatypes.ActiveErrorDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=6121",
                browseName="ns=plastics_dosing;EnableDosingOpcUa",
                description="Variable to set and read the actual state how the dosing signal is transferred from the client to the dosing system in addition to RemoteControlOpcUa.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7022",
                browseName="ns=plastics_dosing;EnableDevice",
                description="Enables the device, for example activate motor drives. Triggers the transition from MachineryItemState NotAvailable to NotExecuting.",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7023", browseName="ns=plastics_dosing;DisableDevice", description="Disables the device, for example deactivate motor drives.")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7070",
                browseName="ns=plastics_dosing;FirstFilling",
                description="Method to fill the DosingSystem for the first time with the mixture of materials from the current recipe.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7071",
                browseName="ns=plastics_dosing;IdentifyDevice",
                description="The DosingSystem on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7089", browseName="ns=plastics_dosing;ResetAllErrors", description="Method to reset all errors of the device.")),
        o6.hasComponent(o6.ns["ns=plastics_dosing;i=7090"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_dosing;i=7096", browseName="ns=plastics_dosing;StopDosing", description="Method to stop dosing immediately.")),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7097",
                browseName="ns=plastics_dosing;StopDosingAfterCycle",
                description="Method to stop dosing after the current dosing cycle (e.g. to get a valid batch mix with batch blending).",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7292",
                browseName="ns=plastics_dosing;StartDosingContinuous",
                description="If EnableDosingOpcUa is TRUE, this method can be used to start dosing continuously.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_dosing;i=7293",
                browseName="ns=plastics_dosing;StartDosingShot",
                description="If EnableDosingOpcUa is TRUE, this method can be used to start dosing for one shot with a defined duration specified by DosingDuration.",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_dosing;i=7294", browseName="ns=plastics_dosing;StartPurge", description="Method to start the purging function on the dosing system.")
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_dosing;i=7449",
                browseName="ns=plastics_dosing;SetActive",
                description="Activates the dosing unit for the current production.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(plastics_dosing_objtypes.DosingSystemType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_dosing;i=5005"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber, plastics_dosing_datypes, plastics_dosing_objtypes
