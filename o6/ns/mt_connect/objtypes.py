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

"""Generated OPC UA mt_connect namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mt_connect_reftypes
from . import datatypes as mt_connect_datypes
from . import vartypes as mt_connect_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=mt_connect;i=2044",
    browseName="ns=mt_connect;MTConfigurationType",
    displayName="MTConfigurationType",
    description="The abstract \\mtuatype{MTConfigurationType} currently has only one\n      sub-type, \\\\ \\mtuatype{MTSensorConfigurationType}. In the future, the\n      configurations will also contain component and device configuration\n      information as sub-types. An XML element that contains technical\n      information about a piece of equipment describing its physical layout or\n      functional characteristics.",
    isAbstract=True,
)
class MTConfigurationType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2021",
    browseName="ns=mt_connect;MTComponentType",
    displayName="MTComponentType",
    description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
    isAbstract=True,
)
class MTComponentType(ns0.objtypes.BaseObjectType):
    components: ns0.objtypes.FolderType | None = o6.organizes(
        ns0.objtypes.FolderType(
            nodeId="ns=mt_connect;i=2042",
            browseName="ns=mt_connect;Components",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
        )
    )
    compositions: ns0.objtypes.FolderType | None = o6.organizes(
        ns0.objtypes.FolderType(
            nodeId="ns=mt_connect;i=2043",
            browseName="ns=mt_connect;Compositions",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
        )
    )
    configuration: MTConfigurationType | None = o6.hasComponent(
        MTConfigurationType(
            nodeId="ns=mt_connect;i=2029",
            browseName="ns=mt_connect;Configuration",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            _allow_abstract=True,
        )
    )
    description: MTDescriptionType | None
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2023",
            browseName="ns=mt_connect;Name",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2024",
            browseName="ns=mt_connect;NativeName",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    sampleInterval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2027",
            browseName="ns=mt_connect;SampleInterval",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2026",
            browseName="ns=mt_connect;SampleRate",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    uuid: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2025",
            browseName="ns=mt_connect;Uuid",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2022",
            browseName="ns=mt_connect;XmlId",
            description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2046",
    browseName="ns=mt_connect;MTSensorConfigurationType",
    displayName="MTSensorConfigurationType",
    description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
)
class MTSensorConfigurationType(MTConfigurationType):
    calibrationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2048",
            browseName="ns=mt_connect;CalibrationDate",
            description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
        )
    )
    calibrationInitials: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2050",
            browseName="ns=mt_connect;CalibrationInitials",
            description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    channels: ns0.objtypes.FolderType | None = o6.organizes(
        ns0.objtypes.FolderType(
            nodeId="ns=mt_connect;i=2052",
            browseName="ns=mt_connect;Channels",
            description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
        )
    )
    firwareVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2047",
            browseName="ns=mt_connect;FirwareVersion",
            description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nextCalibrationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2049",
            browseName="ns=mt_connect;NextCalibrationDate",
            description="An MTConnect Sensor Configuration associated with the Component. See\n      SensorConfigurationType in type-specifications. An element that can\n      contain descriptive content defining the configuration information for\n      sensor.",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2053",
    browseName="ns=mt_connect;MTDescriptionType",
    displayName="MTDescriptionType",
    description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
)
class MTDescriptionType(ns0.objtypes.BaseObjectType):
    data: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2057",
            browseName="ns=mt_connect;Data",
            description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2056",
            browseName="ns=mt_connect;Manufacturer",
            description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2055",
            browseName="ns=mt_connect;SerialNumber",
            description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    station: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2054",
            browseName="ns=mt_connect;Station",
            description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2059",
    browseName="ns=mt_connect;MTChannelType",
    displayName="MTChannelType",
    description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
)
class MTChannelType(ns0.objtypes.BaseObjectType):
    calibrationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2063",
            browseName="ns=mt_connect;CalibrationDate",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
        )
    )
    calibrationInitials: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2065",
            browseName="ns=mt_connect;CalibrationInitials",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2062",
            browseName="ns=mt_connect;MTDescription",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2061",
            browseName="ns=mt_connect;Name",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nextCalibrationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2064",
            browseName="ns=mt_connect;NextCalibrationDate",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
        )
    )
    number: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2060",
            browseName="ns=mt_connect;Number",
            description="A Channel of a sensor. See ChannelType in type specifications. channel\n      represents each sensing element connected to a sensor unit.",
            dataType=o6.Int32,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2067",
    browseName="ns=mt_connect;MTCompositionType",
    displayName="MTCompositionType",
    description="The \\mtmodel{MTCompositionType} represents all composition entities. The\n      specification of how to form the \\gls{BrowseName} is specified in\n      Section~\\ref{sec:browse-name-rules}. The data items are added to the\n      relationship where the \\gls{MTDataItem} to \\gls{Composition} relationship\n      is represented by the \\gls{BrowseName} Composition property of the data\n      item. The data items are added to the \\gls{Composition} by their\n      \\glspl{BrowseName}. An XML element used to describe the lowest level\n      structural building blocks contained within a component element.",
)
class MTCompositionType(ns0.objtypes.BaseObjectType):
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2069",
            browseName="ns=mt_connect;MTTypeName",
            description="The \\mtmodel{MTCompositionType} represents all composition entities. The\n      specification of how to form the \\gls{BrowseName} is specified in\n      Section~\\ref{sec:browse-name-rules}. The data items are added to the\n      relationship where the \\gls{MTDataItem} to \\gls{Composition} relationship\n      is represented by the \\gls{BrowseName} Composition property of the data\n      item. The data items are added to the \\gls{Composition} by their\n      \\glspl{BrowseName}. An XML element used to describe the lowest level\n      structural building blocks contained within a component element.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2071",
            browseName="ns=mt_connect;Name",
            description="The \\mtmodel{MTCompositionType} represents all composition entities. The\n      specification of how to form the \\gls{BrowseName} is specified in\n      Section~\\ref{sec:browse-name-rules}. The data items are added to the\n      relationship where the \\gls{MTDataItem} to \\gls{Composition} relationship\n      is represented by the \\gls{BrowseName} Composition property of the data\n      item. The data items are added to the \\gls{Composition} by their\n      \\glspl{BrowseName}. An XML element used to describe the lowest level\n      structural building blocks contained within a component element.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    uuid: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2070",
            browseName="ns=mt_connect;Uuid",
            description="The \\mtmodel{MTCompositionType} represents all composition entities. The\n      specification of how to form the \\gls{BrowseName} is specified in\n      Section~\\ref{sec:browse-name-rules}. The data items are added to the\n      relationship where the \\gls{MTDataItem} to \\gls{Composition} relationship\n      is represented by the \\gls{BrowseName} Composition property of the data\n      item. The data items are added to the \\gls{Composition} by their\n      \\glspl{BrowseName}. An XML element used to describe the lowest level\n      structural building blocks contained within a component element.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2068",
            browseName="ns=mt_connect;XmlId",
            description="The \\mtmodel{MTCompositionType} represents all composition entities. The\n      specification of how to form the \\gls{BrowseName} is specified in\n      Section~\\ref{sec:browse-name-rules}. The data items are added to the\n      relationship where the \\gls{MTDataItem} to \\gls{Composition} relationship\n      is represented by the \\gls{BrowseName} Composition property of the data\n      item. The data items are added to the \\gls{Composition} by their\n      \\glspl{BrowseName}. An XML element used to describe the lowest level\n      structural building blocks contained within a component element.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2074",
    browseName="ns=mt_connect;ActuatorType",
    displayName="ActuatorType",
    description="the information for an apparatus for moving or controlling a mechanism or\n      system Redefined as a piece of equipment with the ability to be\n      represented as a lower level component of a parent component element or as\n      a composition element. See actuator type",
)
class ActuatorType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2076",
    browseName="ns=mt_connect;AuxiliariesType",
    displayName="AuxiliariesType",
    description="p {padding:0px; margin:0px;} &#160; An XML container used to organize\n      information for lower level elements representing functional sub-systems\n      that provide supplementary or extended capabilities for a piece of\n      equipment, but they are not required for the basic operation of the\n      equipment.",
)
class AuxiliariesType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2078",
    browseName="ns=mt_connect;AxesType",
    displayName="AxesType",
    description="Organizes parts of the device that perform linear or rotational motion An\n      XML container used to organize the structural element of a piece of\n      equipment that perform linear or rotational motion.",
)
class AxesType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2082",
    browseName="ns=mt_connect;BarFeederType",
    displayName="BarFeederType",
    description="a unit involved in delivering bar stock to a piece of equipment. barfeeder\n      is an XML container that represents the information for a unit involved in\n      delivering bar stock to a piece of equipment.",
)
class BarFeederType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2088",
    browseName="ns=mt_connect;ControllerType",
    displayName="ControllerType",
    description="intelligent or computational function within a piece of equipment An XML\n      container used to organize information about an intelligent or\n      computational function within a piece of equipment.",
)
class ControllerType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2096",
    browseName="ns=mt_connect;DoorType",
    displayName="DoorType",
    description="the information for a mechanical mechanism or closure that can cover, for\n      example, a physical access portal into a piece of equipment door component\n      is an XML container that represents the information for a mechanical\n      mechanism or closure that can cover.",
)
class DoorType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2102",
    browseName="ns=mt_connect;EnvironmentalType",
    displayName="EnvironmentalType",
    description="the information for a unit or function involved in monitoring, managing,\n      or conditioning the environment around or within a piece of equipment.\n      environmental is an XML container that represents the information for a\n      unit or function involved in monitoring, managing, or conditioning the\n      environment around or within a piece of equipment.",
)
class EnvironmentalType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2108",
    browseName="ns=mt_connect;InterfacesType",
    displayName="InterfacesType",
    description="An XML container that organizes information used to coordinate actions\n      and activities between pieces of equipment that communicate information\n      between each other.",
)
class InterfacesType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2080",
    browseName="ns=mt_connect;BarFeederInterfaceType",
    displayName="BarFeederInterfaceType",
    description="information used to coordinate the operations between a Bar Feeder and\n      another piece of equipment barfeederinterface provides the set of\n      information used to coordinate the operations between a Bar Feeder and\n      another piece of equipment.",
)
class BarFeederInterfaceType(InterfacesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2084",
    browseName="ns=mt_connect;ChuckInterfaceType",
    displayName="ChuckInterfaceType",
    description="information used to coordinate the operations between two pieces of\n      equipment, one of which controls the operation of a chuck chuckinterface\n      provides the set of information used to coordinate the operations between\n      two pieces of equipment, one of which controls the operation of a chuck.",
)
class ChuckInterfaceType(InterfacesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2094",
    browseName="ns=mt_connect;DoorInterfaceType",
    displayName="DoorInterfaceType",
    description="information used to coordinate the operations between two pieces of\n      equipment, one of which controls the operation of a door doorinterface\n      provides the set of information used to coordinate the operations between\n      two pieces of equipment, one of which controls the operation of a door.",
)
class DoorInterfaceType(InterfacesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2110",
    browseName="ns=mt_connect;LinearType",
    displayName="LinearType",
    description="the movement of a physical piece of equipment, or a portion of the\n      equipment, in a straight line. A linear axis represents the movement of a\n      physical piece of equipment, or a portion of the equipment, in a straight\n      line.",
)
class LinearType(AxesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2112",
    browseName="ns=mt_connect;LoaderType",
    displayName="LoaderType",
    description="the information for a unit comprised of all the parts involved in moving\n      and distributing materials, parts, tooling, and other items to or from a\n      piece of equipment loader is an XML container that represents the\n      information for a unit comprised of all the parts involved in moving and\n      distributing materials, parts, tooling, and other items to or from a piece\n      of equipment.",
)
class LoaderType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2116",
    browseName="ns=mt_connect;MaterialHandlerInterfaceType",
    displayName="MaterialHandlerInterfaceType",
    description="set of information used to coordinate the operations between a piece of\n      equipment and another associated piece of equipment used to automatically\n      handle various types of materials or services associated with the original\n      piece of equipment materialhandlerinterface provides the set of\n      information used to coordinate the operations between a piece of equipment\n      and another associated piece of equipment used to automatically handle\n      various types of materials or services associated with the original piece\n      of equipment.",
)
class MaterialHandlerInterfaceType(InterfacesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2120",
    browseName="ns=mt_connect;PathType",
    displayName="PathType",
    description="information for an independent operation or function within a\n      \\mtuatype{ControllerType} path is an XML container that represents the\n      information for an independent operation or function within a controller.",
)
class PathType(ControllerType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2130",
    browseName="ns=mt_connect;ResourcesType",
    displayName="ResourcesType",
    description="An XML container used to organize information for lower level elements\n      representing types of items, materials, and personnel that support the\n      operation of a piece of equipment or work to be performed at a location.\n      resources also represents materials or other items consumed or transformed\n      by a piece of equipment for production of parts or other types of goods.",
)
class ResourcesType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2118",
    browseName="ns=mt_connect;MaterialsType",
    displayName="MaterialsType",
    description="information about materials or other items consumed or used by the piece\n      of equipment for production of parts, materials, or other types of goods\n      materials is an XML container that provides information about materials or\n      other items consumed or used by the piece of equipment for production of\n      parts, materials, or other types of goods.",
)
class MaterialsType(ResourcesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2122",
    browseName="ns=mt_connect;PersonnelType",
    displayName="PersonnelType",
    description="personnel is an XML container that provides information about an\n      individual or individuals who either control, support, or otherwise\n      interface with a piece of equipment.",
)
class PersonnelType(ResourcesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2132",
    browseName="ns=mt_connect;RotaryType",
    displayName="RotaryType",
    description="rotary movement of a physical piece of equipment or a portion of the\n      equipment. A rotary axis represents any non-linear or rotary movement of a\n      physical piece of equipment or a portion of the equipment.",
)
class RotaryType(AxesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2086",
    browseName="ns=mt_connect;ChuckType",
    displayName="ChuckType",
    description="provides the information about a mechanism that holds a part or stock\n      material in place Chuck is an XML container that provides the information\n      about a mechanism that holds a part or stock material in place.",
)
class ChuckType(RotaryType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2134",
    browseName="ns=mt_connect;SensorType",
    displayName="SensorType",
    description="the information for a piece of equipment that responds to a physical\n      stimulus and transmits a resulting impulse or value from a sensing unit\n      The sensor unit is modeled as a lower level component called sensor.",
)
class SensorType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2136",
    browseName="ns=mt_connect;StockType",
    displayName="StockType",
    description="the information for the material that is used in a manufacturing process\n      and to which work is applied in a machine or piece of equipment to produce\n      parts. stock is an XML container that represents the information for the\n      material that is used in a manufacturing process and to which work is\n      applied in a machine or piece of equipment to produce parts.",
)
class StockType(MaterialsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2138",
    browseName="ns=mt_connect;SystemsType",
    displayName="SystemsType",
    description="major sub-systems that are permanently integrated into a piece of\n      equipment An XML container used to organize information for lower level\n      elements representing the major sub-systems that are permanently\n      integrated into a piece of equipment.",
)
class SystemsType(MTComponentType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2090",
    browseName="ns=mt_connect;CoolantType",
    displayName="CoolantType",
    description="a system comprised of all the parts involved in distribution and\n      management of fluids that remove heat from a piece of equipment. coolant\n      is an XML container that represents the information for a system comprised\n      of all the parts involved in distribution and management of fluids that\n      remove heat from a piece of equipment.",
)
class CoolantType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2092",
    browseName="ns=mt_connect;DielectricType",
    displayName="DielectricType",
    description="a system that manages a chemical mixture used in a manufacturing process\n      being performed at that piece of equipment. dielectric is an XML container\n      that represents the information for a system that manages a chemical\n      mixture used in a manufacturing process being performed at that piece of\n      equipment.",
)
class DielectricType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2098",
    browseName="ns=mt_connect;ElectricType",
    displayName="ElectricType",
    description="represents the information for the main power supply for device piece of\n      equipment and the distribution of that power throughout the equipment.\n      electric is an XML container that represents the information for the main\n      power supply for device piece of equipment and the distribution of that\n      power throughout the equipment.",
)
class ElectricType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2100",
    browseName="ns=mt_connect;EnclosureType",
    displayName="EnclosureType",
    description="a structure used to contain or isolate a piece of equipment or area.\n      enclosure is an XML container that represents the information for a\n      structure used to contain or isolate a piece of equipment or area.",
)
class EnclosureType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2104",
    browseName="ns=mt_connect;FeederType",
    displayName="FeederType",
    description="the information for a system that manages the delivery of materials within\n      a piece of equipment. feeder is an XML container that represents the\n      information for a system that manages the delivery of materials within a\n      piece of equipment.",
)
class FeederType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2106",
    browseName="ns=mt_connect;HydraulicType",
    displayName="HydraulicType",
    description="system comprised of all the parts involved in moving and distributing\n      pressurized liquid throughout the piece of equipment. hydraulic is an XML\n      container that represents the information for a system comprised of all\n      the parts involved in moving and distributing pressurized liquid\n      throughout the piece of equipment.",
)
class HydraulicType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2114",
    browseName="ns=mt_connect;LubricationType",
    displayName="LubricationType",
    description="a system comprised of all the parts involved in distribution and\n      management of fluids used to lubricate portions of the piece of equipment.\n      lubrication is an XML container that represents the information for a\n      system comprised of all the parts involved in distribution and management\n      of fluids used to lubricate portions of the piece of equipment.",
)
class LubricationType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2124",
    browseName="ns=mt_connect;PneumaticType",
    displayName="PneumaticType",
    description="a system comprised of all the parts involved in moving and distributing\n      pressurized gas throughout the piece of equipment. pneumatic is an XML\n      container that represents the information for a system comprised of all\n      the parts involved in moving and distributing pressurized gas throughout\n      the piece of equipment.",
)
class PneumaticType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2126",
    browseName="ns=mt_connect;ProcessPowerType",
    displayName="ProcessPowerType",
    description="the information for a power source associated with a piece of equipment\n      that supplies energy to the manufacturing process separate from the\n      Electric system processpower is an XML container that represents the\n      information for a power source associated with a piece of equipment that\n      supplies energy to the manufacturing process separate from the electric\n      system.",
)
class ProcessPowerType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2128",
    browseName="ns=mt_connect;ProtectiveType",
    displayName="ProtectiveType",
    description="the information for those functions that detect or prevent harm or damage\n      to equipment or personnel. Protective is an XML container that represents\n      the information for those functions that detect or prevent harm or damage\n      to equipment or personnel.",
)
class ProtectiveType(SystemsType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2140",
    browseName="ns=mt_connect;ToolingDeliveryType",
    displayName="ToolingDeliveryType",
    description="a unit involved in managing, positioning, storing, and delivering tooling\n      within a piece of equipment. toolingdelivery is an XML container that\n      represents the information for a unit involved in managing, positioning,\n      storing, and delivering tooling within a piece of equipment.",
)
class ToolingDeliveryType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2142",
    browseName="ns=mt_connect;WasteDisposalType",
    displayName="WasteDisposalType",
    description="the information for a unit comprised of all the parts involved in removing\n      manufacturing byproducts from a piece of equipment wastedisposal is an XML\n      container that represents the information for a unit comprised of all the\n      parts involved in removing manufacturing byproducts from a piece of\n      equipment.",
)
class WasteDisposalType(AuxiliariesType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2425",
    browseName="ns=mt_connect;MTDataItemClassType",
    displayName="MTDataItemClassType",
    description="Abstract base class for all the data item class types. The names are\n      created by pascal typing the names and then generating appending\n      \\mtmodel{Type}. data entity describing a piece of information reported\n      about a piece of equipment.",
    isAbstract=True,
)
class MTDataItemClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2345",
    browseName="ns=mt_connect;MTSampleClassType",
    displayName="MTSampleClassType",
    description="The base type class for all data items with a \\gls{category} of\n      \\mtmodel{SAMPLE}. An XML element that provides the information and data\n      reported from a piece of equipment for those dataitem elements defined\n      with a category attribute of sample category in the mtconnectdevices\n      document.",
    isAbstract=True,
)
class MTSampleClassType(MTDataItemClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2263",
    browseName="ns=mt_connect;LoadClassType",
    displayName="LoadClassType",
    description="The measurement of the actual versus the standard rating of a piece of\n      equipment. $PERCENT$ The measurement of the actual versus the standard\n      rating of a piece of equipment.",
)
class LoadClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2265",
    browseName="ns=mt_connect;AccelerationClassType",
    displayName="AccelerationClassType",
    description="Rate of change of velocity. $\\frac{MILLIMETER}{SECOND^{2}}$ The\n      measurement of the rate of change of velocity.",
)
class AccelerationClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2267",
    browseName="ns=mt_connect;AccumulatedTimeClassType",
    displayName="AccumulatedTimeClassType",
    description="The measurement of accumulated time for an activity or event. $SECOND$ The\n      measurement of accumulated time for an activity or event.",
)
class AccumulatedTimeClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2269",
    browseName="ns=mt_connect;AngularAccelerationClassType",
    displayName="AngularAccelerationClassType",
    description="Rate of change of angular velocity. $\\frac{DEGREE}{SECOND^{2}}$ The\n      measurement rate of change of angular velocity.",
)
class AngularAccelerationClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2271",
    browseName="ns=mt_connect;AngularVelocityClassType",
    displayName="AngularVelocityClassType",
    description="Rate of change of angular position. $\\frac{DEGREE}{SECOND}$ The\n      measurement of the rate of change of angular position.",
)
class AngularVelocityClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2273",
    browseName="ns=mt_connect;AmperageClassType",
    displayName="AmperageClassType",
    description="The measurement of electrical current. $AMPERE$ DEPRECATED in Version 1.6.\n      Replaced by amperageac sample and amperagedc sample.",
)
class AmperageClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2275",
    browseName="ns=mt_connect;AngleClassType",
    displayName="AngleClassType",
    description="The measurement of angular position. $DEGREE$ The measurement of angular\n      position.",
)
class AngleClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2277",
    browseName="ns=mt_connect;AxisFeedrateClassType",
    displayName="AxisFeedrateClassType",
    description="The feedrate of a linear axis. $\\frac{MILLIMETER}{SECOND}$ The measurement\n      of the feedrate of a linear axis.",
)
class AxisFeedrateClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2279",
    browseName="ns=mt_connect;ClockTimeClassType",
    displayName="ClockTimeClassType",
    description="The value provided by a timing device at a specific point in time.\n      $TIMESTAMP$ The value provided by a timing device at a specific point in\n      time.",
)
class ClockTimeClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2281",
    browseName="ns=mt_connect;ConcentrationClassType",
    displayName="ConcentrationClassType",
    description="Percentage of one component within a mixture of components. $PERCENT$ The\n      measurement of the percentage of one component within a mixture of\n      components",
)
class ConcentrationClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2283",
    browseName="ns=mt_connect;ConductivityClassType",
    displayName="ConductivityClassType",
    description="The ability of a material to conduct electricity. $\\frac{SIEMENS}{METER}$\n      The measurement of the ability of a material to conduct electricity.",
)
class ConductivityClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2285",
    browseName="ns=mt_connect;DisplacementClassType",
    displayName="DisplacementClassType",
    description="The change in position of an object. $MILLIMETER$ The measurement of the\n      change in position of an object.",
)
class DisplacementClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2287",
    browseName="ns=mt_connect;ElectricalEnergyClassType",
    displayName="ElectricalEnergyClassType",
    description="The measurement of electrical energy consumption by a component. $WATT\n      \\times SECOND$ The measurement of electrical energy consumption by a\n      component.",
)
class ElectricalEnergyClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2289",
    browseName="ns=mt_connect;EquipmentTimerClassType",
    displayName="EquipmentTimerClassType",
    description="The measurement of the amount of time a \\mtmodel{SECOND} piece of\n      equipment or a sub-part of a piece of equipment has performed specific\n      activities. Often used to determine when maintenance may be required for\n      the equipment. Multiple subTypes of \\mtmodel{EQUIPMENT_TIMER} MAY be\n      defined. A subType MUST always be specified. $SECOND$ The measurement of\n      the amount of time a piece of equipment or a sub-part of a piece of\n      equipment has performed specific activities.",
)
class EquipmentTimerClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2291",
    browseName="ns=mt_connect;FillLevelClassType",
    displayName="FillLevelClassType",
    description="The measurement of the amount of a substance remaining compared to the\n      planned maximum amount of that substance. $PERCENT$ The measurement of the\n      amount of a substance remaining compared to the planned maximum amount of\n      that substance.",
)
class FillLevelClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2293",
    browseName="ns=mt_connect;FlowClassType",
    displayName="FlowClassType",
    description="The rate of flow of a fluid. $\\frac{LITER}{SECOND}$ The measurement of the\n      rate of flow of a fluid.",
)
class FlowClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2295",
    browseName="ns=mt_connect;FrequencyClassType",
    displayName="FrequencyClassType",
    description="The measurement of the number of occurrences of a repeating event per unit\n      time. $HERTZ$ The measurement of the number of occurrences of a repeating\n      event per unit time.",
)
class FrequencyClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2297",
    browseName="ns=mt_connect;LengthClassType",
    displayName="LengthClassType",
    description="The length of an object. $MILLIMETER$ The measurement of the length of an\n      object.",
)
class LengthClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2299",
    browseName="ns=mt_connect;LinearForceClassType",
    displayName="LinearForceClassType",
    description="The measure of the push or pull introduced by an actuator or exerted on an\n      object. $NEWTON$ The measurement of the push or pull introduced by an\n      actuator or exerted on an object.",
)
class LinearForceClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2301",
    browseName="ns=mt_connect;MassClassType",
    displayName="MassClassType",
    description="The measurement of the mass of an object(s) or an amount of material.\n      $KILOGRAM$ The measurement of the mass of an object(s) or an amount of\n      material.",
)
class MassClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2303",
    browseName="ns=mt_connect;PathFeedrateClassType",
    displayName="PathFeedrateClassType",
    description="The feedrate for the axes, or a single axis, associated with a\n      \\mtmodel{Path} component a vector. $\\frac{MILLIMETER}{SECOND}$ The\n      measurement of the feedrate for the axes, or a single axis, associated\n      with a path component-a vector.",
)
class PathFeedrateClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2305",
    browseName="ns=mt_connect;PathPositionClassType",
    displayName="PathPositionClassType",
    description="A measured or calculated position of a control point associated with a\n      \\mtmodel{Controller} element, or PATH element if provided, of a piece of\n      equipment. The control point MUST be reported as a set of space-delimited\n      floating-point numbers representing a point in 3-D space. The position of\n      the control point MUST be reported in units of \\mtmodel{MILLIMETER} and\n      listed in order of X, Y, and Z referenced to the coordinate system of the\n      piece of equipment. $MILLIMETER (\\mathbb{R}^{3})$ A measured or calculated\n      position of a control point associated with a controller element, or path\n      element if provided, of a piece of equipment.",
)
class PathPositionClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2307",
    browseName="ns=mt_connect;PHClassType",
    displayName="PHClassType",
    description="The measure of the acidity or alkalinity. $PH$ A measure of the acidity or\n      alkalinity of a solution.",
)
class PHClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2309",
    browseName="ns=mt_connect;PositionClassType",
    displayName="PositionClassType",
    description="A calculated or measured position related to a Component element.\n      \\mtmodel{POSITION} SHOULD be further defined\n      withacoordinateSytemattribute. If a coordinateSystem attribute is not\n      specified, the position of the control point MUST be reported in\n      \\mtmodel{MACHINE} coordinates. $MILLIMETER$ A measured or calculated\n      position of a component element as reported by a piece of equipment.",
)
class PositionClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2311",
    browseName="ns=mt_connect;PowerFactorClassType",
    displayName="PowerFactorClassType",
    description="The measurement of the ratio of real power flowing to a load to the\n      apparent power in that AC circuit. $PERCENT$ The measurement of the ratio\n      of real power flowing to a load to the apparent power in that AC circuit.",
)
class PowerFactorClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2313",
    browseName="ns=mt_connect;PressureClassType",
    displayName="PressureClassType",
    description="The force per unit area exerted by a gas or liquid. $PASCAL$ The\n      measurement of force per unit area exerted by a gas or liquid.",
)
class PressureClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2315",
    browseName="ns=mt_connect;ProcessTimerClassType",
    displayName="ProcessTimerClassType",
    description="The measurement of the amount of time a piece of equipment has performed\n      different types of activities associated with the process being performed\n      at that piece of equipment. Multiple subtypes of \\mtmodel{PROCESS_TIMER}\n      may be defined. Typically, \\mtmodel{PROCESS_TIMER} SHOULD be modeled as a\n      data item for the Device element, but MAY be modeled for either a\n      Controller or Path Structural Element in the XML document. A \\gls{subType}\n      MUST always be specified. $SECOND$ The measurement of the amount of time a\n      piece of equipment has performed different types of activities associated\n      with the process being performed at that piece of equipment.",
)
class ProcessTimerClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2317",
    browseName="ns=mt_connect;ResistenceClassType",
    displayName="ResistenceClassType",
    description="The degree to which a substance opposes the passage of an electric\n      current. $OHM$",
)
class ResistenceClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2319",
    browseName="ns=mt_connect;RotaryVelocityClassType",
    displayName="RotaryVelocityClassType",
    description="The rotational speed of a rotary axis. $\\frac{REVOLUTION}{MINUTE}$ The\n      measurement of the rotational speed of a rotary axis.",
)
class RotaryVelocityClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2321",
    browseName="ns=mt_connect;SoundLevelClassType",
    displayName="SoundLevelClassType",
    description="Measurement of a sound level or sound pressure level relative to\n      atmospheric pressure. $DECIBEL$ The measurement of a sound level or sound\n      pressure level relative to atmospheric pressure.",
)
class SoundLevelClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2323",
    browseName="ns=mt_connect;StrainClassType",
    displayName="StrainClassType",
    description="The amount of deformation per unit length of an object when a load is\n      applied. $PERCENT$ The measurement of the amount of deformation per unit\n      length of an object when a load is applied.",
)
class StrainClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2325",
    browseName="ns=mt_connect;TemperatureClassType",
    displayName="TemperatureClassType",
    description="The measurement of temperature. $CELSIUS$ The measurement of temperature.",
)
class TemperatureClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2327",
    browseName="ns=mt_connect;TensionClassType",
    displayName="TensionClassType",
    description="A measurement of a force that stretches or elongates an object. $NEWTON$\n      The measurement of a force that stretches or elongates an object.",
)
class TensionClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2329",
    browseName="ns=mt_connect;TiltClassType",
    displayName="TiltClassType",
    description="A measurement of angular displacement. $MICRO \\cdot RADIAN$ The\n      measurement of angular displacement.",
)
class TiltClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2331",
    browseName="ns=mt_connect;TorqueClassType",
    displayName="TorqueClassType",
    description="The turning force exerted on an object or by an object. $NEWTON \\times\n      METER$ The measurement of the turning force exerted on an object or by an\n      object.",
)
class TorqueClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2333",
    browseName="ns=mt_connect;VoltAmpereClassType",
    displayName="VoltAmpereClassType",
    description="The measure of the apparent power in an electrical circuit, equal to the\n      product of root-mean-square (RMS) voltage and RMS current (commonly\n      referred to as VA). $VOLT \\times AMPERE$ The measurement of the apparent\n      power in an electrical circuit, equal to the product of root-mean-square\n      (RMS) voltage and RMS current (commonly referred to as VA).",
)
class VoltAmpereClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2335",
    browseName="ns=mt_connect;VelocityClassType",
    displayName="VelocityClassType",
    description="The rate of change of position. $\\frac{MILLIMETER}{SECOND}$ The\n      measurement of the rate of change of position of a component.",
)
class VelocityClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2337",
    browseName="ns=mt_connect;VoltAmpereReactiveClassType",
    displayName="VoltAmpereReactiveClassType",
    description="The measurement of reactive power in an AC electrical circuit (commonly\n      referred to as VAR). $VOLT \\times AMPERE (Reactive)$ The measurement of\n      reactive power in an AC electrical circuit (commonly referred to as VAR).",
)
class VoltAmpereReactiveClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2339",
    browseName="ns=mt_connect;ViscosityClassType",
    displayName="ViscosityClassType",
    description="A measurement of a fluid’s resistance to flow. $PASCAL \\times SECOND$. The\n      measurement of a fluids resistance to flow.",
)
class ViscosityClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2341",
    browseName="ns=mt_connect;VoltageClassType",
    displayName="VoltageClassType",
    description="The measurement of electrical potential between two points. $VOLT$\n      DEPRECATED in Version 1.6. Replaced by voltageac sample and voltagedc\n      sample.",
)
class VoltageClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2343",
    browseName="ns=mt_connect;WattageClassType",
    displayName="WattageClassType",
    description="The measurement of power flowing through or dissipated by an electrical\n      circuit or piece of equipment. $WATT$ The measurement of power flowing\n      through or dissipated by an electrical circuit or piece of equipment.",
)
class WattageClassType(MTSampleClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2476",
    browseName="ns=mt_connect;MTDataItemSubClassType",
    displayName="MTDataItemSubClassType",
    description="data entity describing a piece of information reported about a piece of\n      equipment.",
    isAbstract=True,
)
class MTDataItemSubClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2478",
    browseName="ns=mt_connect;AbsoluteSubClassType",
    displayName="AbsoluteSubClassType",
    description="The magnitude or measurement of a type irrespective of its relation to\n      other values. The position of a block of program code relative to the\n      beginning of the control program.",
)
class AbsoluteSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2480",
    browseName="ns=mt_connect;ActualSubClassType",
    displayName="ActualSubClassType",
    description="The measured value of the a type. The measured value of the data item type\n      given by a sensor or encoder.",
)
class ActualSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2482",
    browseName="ns=mt_connect;ActionSubClassType",
    displayName="ActionSubClassType",
    description="An indication of the operating state or value of a type. An indication of\n      the operating state of a mechanism represented by a composition type\n      component. The operating state indicates whether the composition element\n      is activated or disabled. The valid data value must be active value or\n      inactive value.",
)
class ActionSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2484",
    browseName="ns=mt_connect;AllSubClassType",
    displayName="AllSubClassType",
    description="The count of all the parts produced. If the subtype is not given, this is\n      the default.",
)
class AllSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2486",
    browseName="ns=mt_connect;AlternatingSubClassType",
    displayName="AlternatingSubClassType",
    description="The measurement of a type occurring in turn repeatedly. The measurement of\n      alternating voltage or current. If not specified further in statistic,\n      defaults to RMS voltage.",
)
class AlternatingSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2488",
    browseName="ns=mt_connect;AScaleSubClassType",
    displayName="AScaleSubClassType",
    description="A Scale weighting factor for the measurement of sound level.",
)
class AScaleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2490",
    browseName="ns=mt_connect;AuxiliarySubClassType",
    displayName="AuxiliarySubClassType",
    description="Example: When multiple locations on a piece of bar stock are referenced as\n      the indication for the \\mtmodel{END_OF_BAR}, the additional location(s)\n      MUST be designated as \\mtmodel{AUXILIARY} indication(s) for the\n      \\mtmodel{END_OF_BAR}. When multiple locations on a piece of bar stock are\n      referenced as the indication for the endofbar event, the additional\n      location(s) must be designated as auxiliary subtype indication(s) for the\n      endofbar event.",
)
class AuxiliarySubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2492",
    browseName="ns=mt_connect;BadSubClassType",
    displayName="BadSubClassType",
    description="Indicates the count of incorrect parts produced. Indicates the count of\n      incorrect parts produced.",
)
class BadSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2494",
    browseName="ns=mt_connect;BrinellSubClassType",
    displayName="BrinellSubClassType",
    description="A scale to measure the resistance to deformation of a surface. A scale to\n      measure the resistance to deformation of a surface.",
)
class BrinellSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2496",
    browseName="ns=mt_connect;BScaleSubClassType",
    displayName="BScaleSubClassType",
    description="B Scale weighting factor for the measurement of sound level.",
)
class BScaleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2498",
    browseName="ns=mt_connect;CommandedSubClassType",
    displayName="CommandedSubClassType",
    description="The value as specified by the Controller type component. A value specified\n      by the controller type component.",
)
class CommandedSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2500",
    browseName="ns=mt_connect;GoodSubClassType",
    displayName="GoodSubClassType",
    description="Indicates the count of correct parts made. Indicates the count of correct\n      parts made.",
)
class GoodSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2502",
    browseName="ns=mt_connect;ControlSubClassType",
    displayName="ControlSubClassType",
    description="The state of the enabling signal or control logic that enables or disables\n      the function or operation of the \\textit{Structural Element}. The state of\n      the enabling signal or control logic that enables or disables the function\n      or operation of the structural element.",
)
class ControlSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2504",
    browseName="ns=mt_connect;CScaleSubClassType",
    displayName="CScaleSubClassType",
    description="C Scale weighting factor for the measurement of sound level.",
)
class CScaleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2506",
    browseName="ns=mt_connect;DelaySubClassType",
    displayName="DelaySubClassType",
    description="Measurement of the time that a piece of equipment is waiting for an event\n      or an action to occur. A piece of equipment waiting for an event or an\n      action to occur.",
)
class DelaySubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2508",
    browseName="ns=mt_connect;DirectSubClassType",
    displayName="DirectSubClassType",
    description="Measurement of DC current or voltage. The measurement of DC current or voltage.",
)
class DirectSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2510",
    browseName="ns=mt_connect;DryRunSubClassType",
    displayName="DryRunSubClassType",
    description="A setting or operator selection used to execute a test mode to confirm the\n      execution of machine functions.",
)
class DryRunSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2512",
    browseName="ns=mt_connect;DScaleSubClassType",
    displayName="DScaleSubClassType",
    description="D Scale weighting factor for the measurement of sound level.",
)
class DScaleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2514",
    browseName="ns=mt_connect;FixtureSubClassType",
    displayName="FixtureSubClassType",
    description="Fixture denotes a specifc type of a piece of equipment.",
)
class FixtureSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2516",
    browseName="ns=mt_connect;IncrementalSubClassType",
    displayName="IncrementalSubClassType",
    description="A small change which could be either positive or negative in a Type's\n      value or function. Example: The position of a block of program code\n      relative to the occurrence of the last \\mtmodel{LINE_LABEL} encountered in\n      the control program. The position of a block of program code relative to\n      the occurrence of the last linelabel event encountered in the control\n      program.",
)
class IncrementalSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2518",
    browseName="ns=mt_connect;JobSubClassType",
    displayName="JobSubClassType",
    description="The value of a signal or calculation issued to adjust the feedrate of the\n      axes associated with a Path component when the axes, or a single axis, are\n      being operated in a manual mode or method (jogging).",
)
class JobSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(nodeId="ns=mt_connect;i=2520", browseName="ns=mt_connect;KineticSubClassType", displayName="KineticSubClassType")
class KineticSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2522",
    browseName="ns=mt_connect;LateralSubClassType",
    displayName="LateralSubClassType",
    description="An indication of the position of a mechanism that may move in a lateral\n      direction. The mechanism is represented by a \\mtmodel{Composition} type\n      component. An indication of the position of a mechanism that may move in a\n      lateral direction. The mechanism is represented by a composition type\n      component. The position information indicates whether the composition\n      element is positioned to the right, to the left, or is in transition. The\n      valid data value must be right value, left value, or transitioning value.",
)
class LateralSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2524",
    browseName="ns=mt_connect;LeebSubClassType",
    displayName="LeebSubClassType",
    description="A scale to measure the elasticity of a surface. A scale to measure the\n      elasticity of a surface.",
)
class LeebSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2526",
    browseName="ns=mt_connect;LengthSubClassType",
    displayName="LengthSubClassType",
    description="The measurement or extent of something from end to end. The measurement of\n      the length of an object.",
)
class LengthSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2528",
    browseName="ns=mt_connect;LinearSubClassType",
    displayName="LinearSubClassType",
    description="The direction of motion. A linear axis represents the movement of a\n      physical piece of equipment, or a portion of the equipment, in a straight\n      line.",
)
class LinearSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2530",
    browseName="ns=mt_connect;LineSubClassType",
    displayName="LineSubClassType",
    description="The state of the power source for the \\textit{Structural Element}.\n      DEPRECATED in Version 1.4.0.",
)
class LineSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2532",
    browseName="ns=mt_connect;LoadedSubClassType",
    displayName="LoadedSubClassType",
    description="An indication that the sub-parts of a piece of equipment are under load.\n      Subparts of a piece of equipment are under load.",
)
class LoadedSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2534",
    browseName="ns=mt_connect;MachineAxisLockSubClassType",
    displayName="MachineAxisLockSubClassType",
    description="A setting or operator selection that changes the behavior of the\n      controller on a piece of equipment.",
)
class MachineAxisLockSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2536",
    browseName="ns=mt_connect;MaintenanceSubClassType",
    displayName="MaintenanceSubClassType",
    description="The identifier of the person currently responsible for performing\n      maintenance on the piece of equipment. Action related to maintenance on\n      the piece of equipment.",
)
class MaintenanceSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2538",
    browseName="ns=mt_connect;ManualUnclampSubClassType",
    displayName="ManualUnclampSubClassType",
    description="An indication of the state of an operator controlled interlock that can\n      inhibit the ability to initiate an unclamp action of an electronically\n      controlled chuck.",
)
class ManualUnclampSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2540",
    browseName="ns=mt_connect;MaximumSubClassType",
    displayName="MaximumSubClassType",
    description="Maximum or peak value recorded for the data item during the calculation\n      period. The upper limit of data reported for a data item.",
)
class MaximumSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2542",
    browseName="ns=mt_connect;MinimumSubClassType",
    displayName="MinimumSubClassType",
    description="Minimum value recorded for the data item during the calculation period.\n      The lower limit of data reported for a data item.",
)
class MinimumSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2544",
    browseName="ns=mt_connect;MohsSubClassType",
    displayName="MohsSubClassType",
    description="A scale to measure the resistance to scratching of a surface. A scale to\n      measure the resistance to scratching of a surface.",
)
class MohsSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(nodeId="ns=mt_connect;i=2546", browseName="ns=mt_connect;MoleSubClassType", displayName="MoleSubClassType")
class MoleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2548",
    browseName="ns=mt_connect;MotionSubClassType",
    displayName="MotionSubClassType",
    description="An indication of the open or closed state of a mechanism. The mechanism is\n      represented by a \\mtmodel{Composition} type component. An indication of\n      the open or closed state of a mechanism. The mechanism is represented by a\n      composition type component. The operating state indicates whether the\n      state of the composition element is open, closed, or unlatched. The valid\n      data value must be open value, unlatched value, or closed value.",
)
class MotionSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2550",
    browseName="ns=mt_connect;NoScaleSubClassType",
    displayName="NoScaleSubClassType",
    description="No weighting factor on the frequency scale for the measurement of sound level.",
)
class NoScaleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2552",
    browseName="ns=mt_connect;OperatingSubClassType",
    displayName="OperatingSubClassType",
    description="An indication that the major sub-parts of a piece of equipment are powered\n      or performing any activity whether producing a part or product or not.\n      Example: For traditional machine tools, this includes when the piece of\n      equipment is \\mtmodel{WORKING} or it is idle. A piece of equipment are\n      powered or performing any activity.",
)
class OperatingSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2554",
    browseName="ns=mt_connect;OperatorSubClassType",
    displayName="OperatorSubClassType",
    description="The identifier of the person currently responsible for operating the piece\n      of equipment. The identifier of the person currently responsible for\n      operating the piece of equipment.",
)
class OperatorSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2556",
    browseName="ns=mt_connect;OptionalStopSubClassType",
    displayName="OptionalStopSubClassType",
    description="A setting or operator selection that changes the behavior of the\n      controller on a piece of equipment.",
)
class OptionalStopSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2558",
    browseName="ns=mt_connect;OverrideSubClassType",
    displayName="OverrideSubClassType",
    description="The operator's overridden value. DEPRECATED: The operators overridden\n      value.",
)
class OverrideSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2560",
    browseName="ns=mt_connect;PrimarySubClassType",
    displayName="PrimarySubClassType",
    description="Specific applications MAY reference one or more locations on a piece of\n      bar stock as the indication for the \\mtmodel{END_OF_BAR}. The main or most\n      important location MUST be designated as the \\mtmodel{PRIMARY} indication\n      for the \\mtmodel{END_OF_BAR}. Specific applications MAY reference one or\n      more locations on a piece of bar stock as the indication for the endofbar\n      event. The main or most important location must be designated as the\n      primary subtype indication for the endofbar event. If no subtype is\n      specified, primary subtype must be the default endofbar event indication.",
)
class PrimarySubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2562",
    browseName="ns=mt_connect;PoweredSubClassType",
    displayName="PoweredSubClassType",
    description="An indication that primary power is applied to the piece of equipment and,\n      as a minimum, the controller or logic portion of the piece of equipment is\n      powered and functioning or components that are required to remain on are\n      powered. Primary power is applied to the piece of equipment and, as a\n      minimum, the controller or logic portion of the piece of equipment is\n      powered and functioning or components that are required to remain on are\n      powered.",
)
class PoweredSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2564",
    browseName="ns=mt_connect;ProbeSubClassType",
    displayName="ProbeSubClassType",
    description="The position provided by a measurement probe. The position provided by a\n      measurement probe.",
)
class ProbeSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2566",
    browseName="ns=mt_connect;ProcessSubClassType",
    displayName="ProcessSubClassType",
    description="The measurement of the time from the beginning of production of a part or\n      product on a piece of equipment until the time that production is complete\n      for that part or product on that piece of equipment. This includes the\n      time that the piece of equipment is running, producing parts or products,\n      or in the process of producing parts. The measurement of the time from the\n      beginning of production of a part or product on a piece of equipment until\n      the time that production is complete for that part or product on that\n      piece of equipment. This includes the time that the piece of equipment is\n      running, producing parts or products, or in the process of producing\n      parts.",
)
class ProcessSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2568",
    browseName="ns=mt_connect;ProgrammedSubClassType",
    displayName="ProgrammedSubClassType",
    description="The value of a signal or calculation issued to adjust the feedrate of the\n      axes associated with a \\mtmodel{Path} component when the axes, or a single\n      axis, are operating as specified by a logic or motion program or set by a\n      switch. The value of a signal or calculation specified by a logic or\n      motion program or set by a switch.",
)
class ProgrammedSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2570",
    browseName="ns=mt_connect;RadialSubClassType",
    displayName="RadialSubClassType",
    description="A reference to a radial type tool offset variable. A reference to a radial\n      type tool offset variable.",
)
class RadialSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2572",
    browseName="ns=mt_connect;RapidSubClassType",
    displayName="RapidSubClassType",
    description="The value of a signal or calculation issued to adjust the feedrate of the\n      axes associated with a \\mtmodel{Path} component when the axes, or a single\n      axis, are being operated in a rapid positioning mode or method (rapid).\n      The value of a signal or calculation issued to adjust the feedrate of a\n      component or composition that is operating in a rapid positioning mode.",
)
class RapidSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(nodeId="ns=mt_connect;i=2574", browseName="ns=mt_connect;RelativeSubClassType", displayName="RelativeSubClassType")
class RelativeSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2576",
    browseName="ns=mt_connect;RemainingSubClassType",
    displayName="RemainingSubClassType",
    description="The remaining amount of the type specified. Remaining measure of an object\n      or an action.",
)
class RemainingSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2578",
    browseName="ns=mt_connect;RequestSubClassType",
    displayName="RequestSubClassType",
    description="\\mtmodel{Request} subtype identifies if the data item defined for\n      MTConnect Interaction Model \\cite{MTCPart5} represents a request. A\n      subtype of an interface dataitem type to communicate a request.",
)
class RequestSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2580",
    browseName="ns=mt_connect;ResponseSubClassType",
    displayName="ResponseSubClassType",
    description="\\mtmodel{Response} subtype identifies if the data item defined for\n      MTConnect Interaction Model \\cite{MTCPart5} represents a response. A\n      subtype of an interface dataitem type to communicate a response.",
)
class ResponseSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2582",
    browseName="ns=mt_connect;RockwellSubClassType",
    displayName="RockwellSubClassType",
    description="A scale to measure the resistance to deformation of a surface. A scale to\n      measure the resistance to deformation of a surface.",
)
class RockwellSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2584",
    browseName="ns=mt_connect;RotarySubClassType",
    displayName="RotarySubClassType",
    description="The rotational direction of a rotary motion using the right hand rule\n      convention. A rotary axis represents any non-linear or rotary movement of\n      a physical piece of equipment or a portion of the equipment.",
)
class RotarySubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2586",
    browseName="ns=mt_connect;SetUpSubClassType",
    displayName="SetUpSubClassType",
    description="The identifier of the person currently responsible for operating the piece\n      of equipment. A structural element is being prepared or modified to begin\n      production of product.",
)
class SetUpSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2588",
    browseName="ns=mt_connect;ShoreSubClassType",
    displayName="ShoreSubClassType",
    description="A scale to measure the resistance to deformation of a surface. A scale to\n      measure the resistance to deformation of a surface.",
)
class ShoreSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2590",
    browseName="ns=mt_connect;StandardSubClassType",
    displayName="StandardSubClassType",
    description="The standard or original value of an object. The standard or original\n      length of an object.",
)
class StandardSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2592",
    browseName="ns=mt_connect;SwitchedSubClassType",
    displayName="SwitchedSubClassType",
    description="An indication of the activation state of a mechanism represented by a\n      \\mtmodel{Composition} type component. The activation state indicates\n      whether the \\mtmodel{Composition} element is activated or not. An\n      indication of the activation state of a mechanism represented by a\n      composition type component. The activation state indicates whether the\n      composition element is activated or not. The valid data value must be on\n      value or off value.",
)
class SwitchedSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2594",
    browseName="ns=mt_connect;TargetSubClassType",
    displayName="TargetSubClassType",
    description="Indicates the number of parts that are projected or planned to be\n      produced. The desired measure or count for a data item value.",
)
class TargetSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2596",
    browseName="ns=mt_connect;ToolChangeStopSubClassType",
    displayName="ToolChangeStopSubClassType",
    description="A setting or operator selection that changes the behavior of the\n      controller on a piece of equipment.",
)
class ToolChangeStopSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(nodeId="ns=mt_connect;i=2598", browseName="ns=mt_connect;ToolEdgeSubClassType", displayName="ToolEdgeSubClassType")
class ToolEdgeSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2600",
    browseName="ns=mt_connect;ToolGroupSubClassType",
    displayName="ToolGroupSubClassType",
    description="The tool group a specific tool is assigned to in the part program. An\n      identifier for the tool group associated with a specific tool. Commonly\n      used to designate spare tools.",
)
class ToolGroupSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2602",
    browseName="ns=mt_connect;ToolSubClassType",
    displayName="ToolSubClassType",
    description="coordinate system referenced to the tool or to the end effector attached\n      to the mechanical interface. Ref:ISO 9787:2013",
)
class ToolSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2604", browseName="ns=mt_connect;UasbleSubClassType", displayName="UasbleSubClassType", description="The remaining useable value of an object."
)
class UasbleSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2606",
    browseName="ns=mt_connect;VerticalSubClassType",
    displayName="VerticalSubClassType",
    description="An indication of the position of a mechanism that may move in a vertical\n      direction. An indication of the position of a mechanism that may move in a\n      vertical direction. The mechanism is represented by a composition type\n      component. The position information indicates whether the composition\n      element is positioned to the top, to the bottom, or is in transition. The\n      valid data value must be up value, down value, or transitioning value.",
)
class VerticalSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2608",
    browseName="ns=mt_connect;VolumeSubClassType",
    displayName="VolumeSubClassType",
    description="A measurement of space accupied by a physical object.",
)
class VolumeSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2610",
    browseName="ns=mt_connect;VickersSubClassType",
    displayName="VickersSubClassType",
    description="A scale to measure the resistance to deformation of a surface. A scale to\n      measure the resistance to deformation of a surface.",
)
class VickersSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2612",
    browseName="ns=mt_connect;WeightSubClassType",
    displayName="WeightSubClassType",
    description="A physical object's relative mass. The total weight of the Cutting\n      Tool in grams. The force exerted by the mass of the Cutting Tool.",
)
class WeightSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2614",
    browseName="ns=mt_connect;WorkingSubClassType",
    displayName="WorkingSubClassType",
    description="An indication that a piece of equipment is performing any activity. A\n      piece of equipment performing any activity, the equipment is active and\n      performing a function under load or not.",
)
class WorkingSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2616",
    browseName="ns=mt_connect;WorkpieceSubClassType",
    displayName="WorkpieceSubClassType",
    description="A physical object being or to be worked on with a tool or machine. An\n      object or material on which a form of work is performed.",
)
class WorkpieceSubClassType(MTDataItemSubClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2629",
    browseName="ns=mt_connect;MTConditionClassType",
    displayName="MTConditionClassType",
    description="The abstract type for all data items types that are specifically for\n      \\mtmodel{CONDITION} \\gls{category}. An XML element which provides the\n      information and data reported from a piece of equipment for those dataitem\n      elements defined with a category attribute of condition category in the\n      mtconnectdevices document.",
    isAbstract=True,
)
class MTConditionClassType(MTDataItemClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2411",
    browseName="ns=mt_connect;ActuatorClassType",
    displayName="ActuatorClassType",
    description="Redefined as a piece of equipment with the ability to be represented as a\n      lower level component of a parent component element or as a composition\n      element. See actuator type",
)
class ActuatorClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2413",
    browseName="ns=mt_connect;CommunicationsClassType",
    displayName="CommunicationsClassType",
    description="An indication that the piece of equipment has experienced a\n      communications failure.",
)
class CommunicationsClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2415",
    browseName="ns=mt_connect;DataRangeClassType",
    displayName="DataRangeClassType",
    description="An indication that the value of the data associated with a measured value\n      or a calculation is outside of an expected range.",
)
class DataRangeClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2417",
    browseName="ns=mt_connect;LogicProgramClassType",
    displayName="LogicProgramClassType",
    description="An indication that an error occurred in the logic program or programmable\n      logic controller (PLC) associated with a piece of equipment.",
)
class LogicProgramClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2419",
    browseName="ns=mt_connect;HardwareClassType",
    displayName="HardwareClassType",
    description="An indication of a fault associated with the hardware subsystem of the\n      structural element.",
)
class HardwareClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2421",
    browseName="ns=mt_connect;MotionProgramClassType",
    displayName="MotionProgramClassType",
    description="An indication that an error occurred in the motion program associated\n      with a piece of equipment.",
)
class MotionProgramClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2423",
    browseName="ns=mt_connect;SystemClassType",
    displayName="SystemClassType",
    description="A general purpose indication associated with an electronic component of a\n      piece of equipment or a controller that represents a fault that is not\n      associated with the operator, program, or hardware.",
)
class SystemClassType(MTConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2631",
    browseName="ns=mt_connect;MTEventClassType",
    displayName="MTEventClassType",
    description="The base type class for all data items with a \\gls{category} of\n      \\mtmodel{EVENT}. An XML element which provides the information and data\n      reported from a piece of equipment for those dataitem elements defined\n      with a category attribute of event category in the mtconnectdevices\n      document.",
    isAbstract=True,
)
class MTEventClassType(MTDataItemClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2144",
    browseName="ns=mt_connect;MTControlledVocabEventClassType",
    displayName="MTControlledVocabEventClassType",
    description="The abstract base type for controlled events that represent states that\n      are provided in related enumerations. These data items will be represented\n      in an object of type \\mtuatype{MTControlledVocabEventType} derived from\n      the OPC UA type \\uamodel{MultiStateValueDiscreteType}",
    isAbstract=True,
)
class MTControlledVocabEventClassType(MTEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2146",
    browseName="ns=mt_connect;ActuatorStateClassType",
    displayName="ActuatorStateClassType",
    description="Represents the operational state of an apparatus for moving or\n      controlling. Represents the operational state of an apparatus for moving\n      or controlling a mechanism or system.",
)
class ActuatorStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2149",
    browseName="ns=mt_connect;AvailabilityClassType",
    displayName="AvailabilityClassType",
    description="Represents the Agent's ability to communicate with the data source.\n      This MUST be provided for a Device Element and MAY be provided for any\n      other Structural Element. Represents the agent's ability to\n      communicate with the data source.",
)
class AvailabilityClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2152",
    browseName="ns=mt_connect;AxisCouplingClassType",
    displayName="AxisCouplingClassType",
    description="Describes the way the axes will be associated to each other. This is used\n      in conjunction with \\mtmodel{COUPLED_AXES} to indicate the way they are\n      interacting. The coupling MUST be viewed from the perspective of a\n      specific axis. Therefore, a \\mtmodel{MASTER} coupling indicates that this\n      axis is the master for the \\mtmodel{COUPLED_AXES}. Describes the way the\n      axes will be associated to each other. This is used in conjunction with\n      coupledaxes event to indicate the way they are interacting.",
)
class AxisCouplingClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2155",
    browseName="ns=mt_connect;AxisInterlockClassType",
    displayName="AxisInterlockClassType",
    description="An indicator of the state of the axis lockout function when power has been\n      removed and the axis is allowed to move freely. An indicator of the state\n      of the axis lockout function when power has been removed and the axis is\n      allowed to move freely.",
)
class AxisInterlockClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2158",
    browseName="ns=mt_connect;AxisStateClassType",
    displayName="AxisStateClassType",
    description="An indicator of the controlled state of a \\mtmodel{LINEAR} or\n      \\mtmodel{ROTARY} component representing an axis. An indicator of the\n      controlled state of a linear or rotary component representing an axis.",
)
class AxisStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2161",
    browseName="ns=mt_connect;ChuckInterlockClassType",
    displayName="ChuckInterlockClassType",
    description="An indication of the state of an interlock function or control logic state\n      intended to prevent the associated \\mtmodel{Chuck} composition or function\n      from being operated. An indication of the state of an interlock function\n      or control logic state intended to prevent the associated chuck component\n      from being operated.",
)
class ChuckInterlockClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2164",
    browseName="ns=mt_connect;ChuckStateClassType",
    displayName="ChuckStateClassType",
    description="An indication of the operating state of a mechanism that holds a part or\n      stock material during a manufacturing process. It may also represent a\n      mechanism that holds any other mechanism in place within a piece of\n      equipment. An indication of the operating state of a mechanism that holds\n      a part or stock material during a manufacturing process. It may also\n      represent a mechanism that holds any other mechanism in place within a\n      piece of equipment.",
)
class ChuckStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2167",
    browseName="ns=mt_connect;ControllerModeClassType",
    displayName="ControllerModeClassType",
    description="The current mode of the \\mtmodel{Controller} component. The current\n      operating mode of the controller component.",
)
class ControllerModeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2170",
    browseName="ns=mt_connect;ExecutionClassType",
    displayName="ExecutionClassType",
    description="The execution status of the \\mtmodel{Controller} or \\mtmodel{Path}. The\n      execution status of the controller.",
)
class ExecutionClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2173",
    browseName="ns=mt_connect;CompositionStateClassType",
    displayName="CompositionStateClassType",
    description="An indication of the operating condition of a mechanism represented by a\n      \\mtmodel{Composition} type element. A \\gls{subType} MUST always be\n      specified. A \\mtmodel{compositionId} MUST always be specified. An\n      indication of the operating condition of a mechanism represented by a\n      composition type element.",
)
class CompositionStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2176",
    browseName="ns=mt_connect;ControllerModeOverrideClassType",
    displayName="ControllerModeOverrideClassType",
    description="A setting or operator selection that changes the behavior of a piece of\n      equipment. A setting or operator selection that changes the behavior of a\n      piece of equipment.",
)
class ControllerModeOverrideClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2179",
    browseName="ns=mt_connect;DirectionClassType",
    displayName="DirectionClassType",
    description="The direction of motion. A \\gls{subType} MUST always be specified. The\n      direction of motion.",
)
class DirectionClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2182",
    browseName="ns=mt_connect;DoorStateClassType",
    displayName="DoorStateClassType",
    description="The opened or closed state of the door. The operational state of a door\n      type component or composition element.",
)
class DoorStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2185",
    browseName="ns=mt_connect;EmergencyStopClassType",
    displayName="EmergencyStopClassType",
    description="The current state of the emergency stop signal. The current state of the\n      emergency stop signal for a piece of equipment, controller path, or any\n      other component or subsystem of a piece of equipment.",
)
class EmergencyStopClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2188",
    browseName="ns=mt_connect;EndOfBarClassType",
    displayName="EndOfBarClassType",
    description="An indication of whether the end of a piece of bar stock being feed by a\n      bar feeder has been reached. An indication of whether the end of a piece\n      of bar stock being feed by a bar feeder has been reached.",
)
class EndOfBarClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2191",
    browseName="ns=mt_connect;EquipmentModeClassType",
    displayName="EquipmentModeClassType",
    description="An indication that a piece of equipment, or a sub-part of a piece of\n      equipment, is performing specific types of activities. A \\gls{subType}\n      MUST always be specified. An indication that a piece of equipment, or a\n      sub-part of a piece of equipment, is performing specific types of\n      activities.",
)
class EquipmentModeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2194",
    browseName="ns=mt_connect;FunctionalModeClassType",
    displayName="FunctionalModeClassType",
    description="The current intended production status of the device or component.\n      Typically, the \\texttt{FUNCTIONAL_MODE} SHOULD be modeled as a data item\n      for the Device element, but MAY be modeled for any Structural Element in\n      the XML document. The current intended production status of the device or\n      component.",
)
class FunctionalModeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2212",
    browseName="ns=mt_connect;SpindleInterlockClassType",
    displayName="SpindleInterlockClassType",
    description="An indication of the status of the spindle for a piece of equipment when\n      power has been removed and it is free to rotate. An indication of the\n      status of the spindle for a piece of equipment when power has been removed\n      and it is free to rotate.",
)
class SpindleInterlockClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2215",
    browseName="ns=mt_connect;PathModeClassType",
    displayName="PathModeClassType",
    description="Describes the operational relationship between a \\mtmodel{PATH}\n      \\textit{Structural Element} and another \\mtmodel{PATH} \\textit{Structural\n      Element} for pieces of equipment comprised of multiple logical groupings\n      of controlled axes or other logical operations. Describes the operational\n      relationship between a path structural element and another path structural\n      element for pieces of equipment comprised of multiple logical groupings of\n      controlled axes or other logical operations.",
)
class PathModeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2218",
    browseName="ns=mt_connect;PowerStateClassType",
    displayName="PowerStateClassType",
    description="The indication of the status of the source of energy for a\n      \\textit{Structural Element} to allow it to perform its intended function\n      or the state of an enabling signal providing permission for the\n      \\textit{Structural Element} to perform its functions. DEPRECATION WARNING:\n      \\texttt{PowerState} may be deprecated in the future. The indication of the\n      status of the source of energy for a structural element to allow it to\n      perform its intended function or the state of an enabling signal providing\n      permission for the structural element to perform its functions.",
)
class PowerStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2221",
    browseName="ns=mt_connect;ProgramEditClassType",
    displayName="ProgramEditClassType",
    description="An indication of the status of the \\mtmodel{Controller} component’s\n      program editing mode. On many controls, a program can be edited while\n      another program is currently being executed. An indication of the status\n      of the controller components program editing mode. On many controls, a\n      program can be edited while another program is currently being executed.",
)
class ProgramEditClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2224",
    browseName="ns=mt_connect;RotaryModeClassType",
    displayName="RotaryModeClassType",
    description="The current operating mode for a \\mtmodel{Rotary} type axis. The current\n      operating mode for a rotary type axis.",
)
class RotaryModeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2227",
    browseName="ns=mt_connect;InterfaceStateClassType",
    displayName="InterfaceStateClassType",
    description="The current functional or operational state of an Interface type element\n      indicating whether the Interface is active or not currently functioning.\n      An indication of the operational state of an interface component\n      component.",
)
class InterfaceStateClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2231",
    browseName="ns=mt_connect;MaterialFeedClassType",
    displayName="MaterialFeedClassType",
    description="Service to advance material or feed product to a piece of equipment from a\n      continuous or bulk source. Service to advance material or feed product to\n      a piece of equipment from a continuous or bulk source.",
)
class MaterialFeedClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2235",
    browseName="ns=mt_connect;MaterialChangeClassType",
    displayName="MaterialChangeClassType",
    description="Service to change the type of material or product being loaded or fed to a\n      piece of equipment. Service to change the type of material or product\n      being loaded or fed to a piece of equipment.",
)
class MaterialChangeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2238",
    browseName="ns=mt_connect;MaterialRetractClassType",
    displayName="MaterialRetractClassType",
    description="Service to remove or retract material or product. Service to remove or\n      retract material or product.",
)
class MaterialRetractClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2241",
    browseName="ns=mt_connect;MaterialLoadClassType",
    displayName="MaterialLoadClassType",
    description="Service to load a piece of material or product. Service to load a piece of\n      material or product.",
)
class MaterialLoadClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2244",
    browseName="ns=mt_connect;MaterialUnloadClassType",
    displayName="MaterialUnloadClassType",
    description="Service to unload a piece of material or product. Service to unload a\n      piece of material or product.",
)
class MaterialUnloadClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2247", browseName="ns=mt_connect;OpenDoorClassType", displayName="OpenDoorClassType", description="Service to open a door. Service to open a door."
)
class OpenDoorClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2250", browseName="ns=mt_connect;CloseDoorClassType", displayName="CloseDoorClassType", description="Service to close a door. Service to close a door."
)
class CloseDoorClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2253", browseName="ns=mt_connect;OpenChuckClassType", displayName="OpenChuckClassType", description="Service to open a chuck. Service to open a chuck."
)
class OpenChuckClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2256",
    browseName="ns=mt_connect;CloseChuckClassType",
    displayName="CloseChuckClassType",
    description="Service to close a chuck. Service to close a chuck.",
)
class CloseChuckClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2259",
    browseName="ns=mt_connect;PartChangeClassType",
    displayName="PartChangeClassType",
    description="Service to change the part or product associated with a piece of equipment\n      to a different part or product. Service to change the part or product\n      associated with a piece of equipment to a different part or product.",
)
class PartChangeClassType(MTControlledVocabEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2359",
    browseName="ns=mt_connect;MTNumericEventClassType",
    displayName="MTNumericEventClassType",
    description="The root type for all of the event types that have numeric \\gls{CDATA}.",
    isAbstract=True,
)
class MTNumericEventClassType(MTEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2347",
    browseName="ns=mt_connect;AxisFeedrateOverrideClassType",
    displayName="AxisFeedrateOverrideClassType",
    description="The value of a signal or calculation issued to adjust the feedrate of an\n      individual linear type axis. The value provided for\n      \\mtmodel{AXIS_FEEDRATE_OVERRIDE} is expressed as a percentage of the\n      designated feedrate for the axis. When \\mtmodel{AXIS_FEEDRATE_OVERRIDE} is\n      applied, the resulting commanded feedrate for the axis is limited to the\n      value of the original feedrate multiplied by the value of the\n      \\mtmodel{AXIS_FEEDRATE_OVERRIDE}. There MAY be different subtypes of\n      \\mtmodel{AXIS_FEEDRATE_OVERRIDE}; each representing an override value for\n      a designated subtype of feedrate depending on the state of operation of\n      the axis. The subtypes of operation of an axis are currently defined as\n      \\mtmodel{PROGRAMMED}, \\mtmodel{JOG}, and \\mtmodel{RAPID}. The value of a\n      signal or calculation issued to adjust the feedrate of an individual\n      linear type axis.",
)
class AxisFeedrateOverrideClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2349",
    browseName="ns=mt_connect;BlockCountClassType",
    displayName="BlockCountClassType",
    description="The total count of the number of blocks of program code that have been\n      executed since execution started. \\mtmodel{BLOCK_COUNT} counts blocks of\n      program code executed regardless of program structure (e.g., looping or\n      branching within the program). The starting value for\n      \\mtmodel{BLOCK_COUNT} MAY be established by an initial value provided in\n      the Constraint element defined for the data item. The total count of the\n      number of blocks of program code that have been executed since execution\n      started.",
)
class BlockCountClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2351",
    browseName="ns=mt_connect;HardnessClassType",
    displayName="HardnessClassType",
    description="The measurement of the hardness of a material. The measurement does not\n      provide a unit. A \\gls{subType} MUST always be specified to designate the\n      hardness scale associated with the measurement. The measurement of the\n      hardness of a material.",
)
class HardnessClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2353",
    browseName="ns=mt_connect;LineNumberClassType",
    displayName="LineNumberClassType",
    description="A reference to the position of a block of program code within a control\n      program. The line number MAY represent either an absolute position\n      starting with the first line of the program or an incremental position\n      relative to the occurrence of the last \\mtmodel{LINE_LABEL}.\n      \\mtmodel{LINE_NUMBER} does not change subject to any looping or branching\n      in a control program. A \\gls{subType} MUST be defined. A reference to the\n      position of a block of program code within a control program.",
)
class LineNumberClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2355",
    browseName="ns=mt_connect;PartCountClassType",
    displayName="PartCountClassType",
    description="The current count of parts produced as represented by the Controller. The\n      valid data value MUST be an integer value. The count of parts produced.",
)
class PartCountClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2357",
    browseName="ns=mt_connect;RotaryVelocityOverrideClassType",
    displayName="RotaryVelocityOverrideClassType",
    description="A command issued to adjust the programmed velocity for a Rotary type axis.\n      This command represents a percentage change to the velocity calculated by\n      a logic or motion program or set by a switch for a Rotary type axis.\n      \\mtmodel{ROTARY_VELOCITY_OVERRIDE} is expressed as a percentage of the\n      programmed \\mtmodel{ROTARY_VELOCITY}. The value of a command issued to\n      adjust the programmed velocity for a rotary type axis. This command\n      represents a percentage change to the velocity calculated by a logic or\n      motion program or set by a switch for a rotary type axis.",
)
class RotaryVelocityOverrideClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2361",
    browseName="ns=mt_connect;MTStringEventClassType",
    displayName="MTStringEventClassType",
    description="The base UA \\gls{Type} for all \\glspl{MTDataItem} that have a non-specific\n      text representation.",
    isAbstract=True,
)
class MTStringEventClassType(MTEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2363",
    browseName="ns=mt_connect;BlockClassType",
    displayName="BlockClassType",
    description="The line of code or command being executed by a \\mtmodel{Controller}\n      \\mtterm{Structural Element}. The value reported for \\mtmodel{Block} MUST\n      include the entire expression for a line of program code, including all\n      parameters. The line of code or command being executed by a controller\n      structural element.",
)
class BlockClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2365",
    browseName="ns=mt_connect;CoupledAxesClassType",
    displayName="CoupledAxesClassType",
    description="Refers to the set of associated axes. The valid data value for\n      \\mtmodel{COUPLED_AXES} SHOULD be a space-delimited set of axes reported as\n      the value of the name attribute for each axis. If name is not available,\n      the piece of equipment MUST report the value of the nativeName attribute\n      for each axis. Refers to the set of associated axes.",
)
class CoupledAxesClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2367",
    browseName="ns=mt_connect;LineLabelClassType",
    displayName="LineLabelClassType",
    description="An optional identifier for a \\mtmodel{BLOCK} of code in a\n      \\mtmodel{PROGRAM}. An optional identifier for a block event of code in a\n      program event.",
)
class LineLabelClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2369",
    browseName="ns=mt_connect;MaterialClassType",
    displayName="MaterialClassType",
    description="The identifier of a material used or consumed in the manufacturing\n      process. The identifier of a material used or consumed in the\n      manufacturing process.",
)
class MaterialClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2371",
    browseName="ns=mt_connect;OperatorIdClassType",
    displayName="OperatorIdClassType",
    description="The identifier of the person currently responsible for operating the piece\n      of equipment. DEPRECATION WARNING: May be deprecated in the future. See\n      \\mtmodel{USER} below. The identifier of the person currently responsible\n      for operating the piece of equipment.",
)
class OperatorIdClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2373",
    browseName="ns=mt_connect;PalletIdClassType",
    displayName="PalletIdClassType",
    description="The identifier for a pallet. The identifier for a pallet.",
)
class PalletIdClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2375",
    browseName="ns=mt_connect;PartIdClassType",
    displayName="PartIdClassType",
    description="An identifier of a part in a manufacturing operation. An identifier of a\n      part in a manufacturing operation.",
)
class PartIdClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2377",
    browseName="ns=mt_connect;PartNumberClassType",
    displayName="PartNumberClassType",
    description="An identifier of a part or product moving through the manufacturing\n      process. An identifier of a part or product moving through the\n      manufacturing process. The valid data value must be a text string.",
)
class PartNumberClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2379",
    browseName="ns=mt_connect;ProgramClassType",
    displayName="ProgramClassType",
    description="The name of the logic or motion program being executed by the\n      \\mtmodel{Controller} or \\mtmodel{Path} component. The name of the logic or\n      motion program being executed by the controller component.",
)
class ProgramClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2381",
    browseName="ns=mt_connect;ProgramEditNameClassType",
    displayName="ProgramEditNameClassType",
    description="The name of the program being edited. This is used in conjunction with\n      \\mtmodel{PROGRAM_EDIT} when in \\mtmodel{ACTIVE} state. The name of the\n      program being edited. This is used in conjunction with programedit event\n      when in active value state. The valid data value must be a text string.",
)
class ProgramEditNameClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2383",
    browseName="ns=mt_connect;ProgramHeaderClassType",
    displayName="ProgramHeaderClassType",
    description="The non-executable header section of the control program. The\n      non-executable header section of the control program.",
)
class ProgramHeaderClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2385",
    browseName="ns=mt_connect;ProgramCommentClassType",
    displayName="ProgramCommentClassType",
    description="A comment or non-executable statement in the control program. A comment or\n      non-executable statement in the control program. The valid data value must\n      be a text string.",
)
class ProgramCommentClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2387",
    browseName="ns=mt_connect;SerialNumberClassType",
    displayName="SerialNumberClassType",
    description="The serial number associated with a \\mtmodel{Component}, \\mtmodel{Asset},\n      or \\mtmodel{Device}. The serial number associated with a component, asset\n      mtconnectassets, or device. The valid data value must be a text string.",
)
class SerialNumberClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2389",
    browseName="ns=mt_connect;ToolAssetIdClassType",
    displayName="ToolAssetIdClassType",
    description="The identifier of an individual tool asset The identifier of an individual\n      tool asset.The valid data value must be a text string.",
)
class ToolAssetIdClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2391",
    browseName="ns=mt_connect;ToolNumberClassType",
    displayName="ToolNumberClassType",
    description="The identifier of a tool provided by the piece of equipment controller.\n      The identifier assigned by the controller component to a cutting tool when\n      in use by a piece of equipment. The valid data value must be a text\n      string.",
)
class ToolNumberClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2393",
    browseName="ns=mt_connect;ToolOffsetClassType",
    displayName="ToolOffsetClassType",
    description="A reference to the tool offset variables applied to the active cutting\n      tool associated with a Path in a Controller type component. The valid data\n      value MUST be a text string. The reported value returned for\n      \\mtmodel{TOOL_OFFSET} identifies the location in a table or list where the\n      actual tool offset values are stored. A \\gls{subType} MUST always be\n      specified. A reference to the tool offset variables applied to the active\n      cutting tool associated with a path in a controller type component.",
)
class ToolOffsetClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2395",
    browseName="ns=mt_connect;UserClassType",
    displayName="UserClassType",
    description="The identifier of the person currently responsible for operating the piece\n      of equipment. A \\gls{subType} MUST always be specified. The identifier of\n      the person currently responsible for operating the piece of equipment.",
)
class UserClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2397",
    browseName="ns=mt_connect;WireClassType",
    displayName="WireClassType",
    description="The identifier for the type of wire used as the cutting mechanism in\n      Electrical Discharge Machining or similar processes. A string like piece\n      or filament of relatively rigid or flexible material provided in a variety\n      of diameters.",
)
class WireClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2399",
    browseName="ns=mt_connect;WorkholdingClassType",
    displayName="WorkholdingClassType",
    description="The identifier for the workholding currently in use.",
)
class WorkholdingClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2401",
    browseName="ns=mt_connect;WorkOffsetClassType",
    displayName="WorkOffsetClassType",
    description="A reference to the offset variables for a work piece or part associated\n      with a Path in a Controller type component. The valid data value MUST be a\n      text string. The reported value returned for \\mtmodel{WORK_OFFSET}\n      identifies the location in a table or list where the actual tool offset\n      values are stored. A reference to the offset variables for a work piece or\n      part associated with a path in a controller type component.",
)
class WorkOffsetClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2403",
    browseName="ns=mt_connect;MessageClassType",
    displayName="MessageClassType",
    description="Any text string of information to be transferred from a piece of\n      equipment to a client software application.",
)
class MessageClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2405",
    browseName="ns=mt_connect;AssetChangedClassType",
    displayName="AssetChangedClassType",
    description="The value of the cdata for the event MUST be the assetid of the asset\n      that has been added or changed. There will not be a separate message for\n      new assets.",
)
class AssetChangedClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2407",
    browseName="ns=mt_connect;AssetRemovedClassType",
    displayName="AssetRemovedClassType",
    description="The value of the cdata for the event MUST be the assetid of the asset\n      that has been removed. The asset will still be visible if requested with\n      the includeremoved parameter as described in the protocol section. When\n      assets are removed they are not moved to the beginning of the most\n      recently modified list.",
)
class AssetRemovedClassType(MTStringEventClassType):
    pass


@o6.objecttype(nodeId="ns=mt_connect;i=2409", browseName="ns=mt_connect;LineClassType", displayName="LineClassType", description="DEPRECATED in Version 1.4.0.")
class LineClassType(MTStringEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2427",
    browseName="ns=mt_connect;MTMessageClassType",
    displayName="MTMessageClassType",
    description="Any text string of information to be transferred from a piece of\n      equipment to a client software application.",
)
class MTMessageClassType(MTEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2647",
    browseName="ns=mt_connect;MTConstraintType",
    displayName="MTConstraintType",
    description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
)
class MTConstraintType(ns0.objtypes.BaseObjectType):
    maximum: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2650",
            browseName="ns=mt_connect;Maximum",
            description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    minimum: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2649",
            browseName="ns=mt_connect;Minimum",
            description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    nominal: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2651",
            browseName="ns=mt_connect;Nominal",
            description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    values: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2648",
            browseName="ns=mt_connect;Values",
            description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
            dataType=o6.String,
            valueRank=1,
        )
    )


@o6.objecttype(nodeId="ns=mt_connect;i=2656", browseName="ns=mt_connect;MTMessageEventType", displayName="MTMessageEventType")
class MTMessageEventType(ns0.objtypes.BaseEventType):
    nativeCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=2657", browseName="ns=mt_connect;NativeCode", dataType=o6.String, valueRank=-1)
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=2660",
    browseName="ns=mt_connect;MTConditionType",
    displayName="MTConditionType",
    description="An \\mtmodel{MTConditionType} instance will be created for event MTConnect\n      \\gls{MTDataItem} with a \\gls{category} of \\mtmodel{CONDITION}. The\n      \\gls{BrowseName} of the condition uses the same naming convention as the\n      MTConnect \\gls{MTDataItem} types with \\gls{MTCondition} appended as a\n      suffix. For example the condition with \\gls{type} of \\mtmodel{TEMPERATURE}\n      will have the browse name of \\mtmodel{TemperatureCondition} as opposed to\n      the \\mtuatype{MTSampleType} of \\mtmodel{Temperature}. An XML element which\n      provides the information and data reported from a piece of equipment for\n      those dataitem elements defined with a category attribute of condition\n      category in the mtconnectdevices document.",
)
class MTConditionType(ns0.objtypes.BaseObjectType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2917",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2919",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2918",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2916",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2923",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2922",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2921",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2920",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2915",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=3628",
    browseName="ns=mt_connect;PathFeedrateOverrideClassType",
    displayName="PathFeedrateOverrideClassType",
    description="The value of a signal or calculation issued to adjust the feedrate for\n      the axes associated with a path component that may represent a single axis\n      or the coordinated movement of multiple axes.",
)
class PathFeedrateOverrideClassType(MTNumericEventClassType):
    pass


@o6.objecttype(
    nodeId="ns=mt_connect;i=2015",
    browseName="ns=mt_connect;MTDeviceType",
    displayName="MTDeviceType",
    description="See DeviceType.tex. The primary container element for each piece of\n      equipment. device is organized within the devices container.",
)
class MTDeviceType(MTComponentType):
    iso841Class: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2017",
            browseName="ns=mt_connect;Iso841Class",
            description="See DeviceType.tex. The primary container element for each piece of\n      equipment. device is organized within the devices container.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3668",
            browseName="ns=mt_connect;Name",
            description="See DeviceType.tex. The primary container element for each piece of\n      equipment. device is organized within the devices container.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    uuid: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3669",
            browseName="ns=mt_connect;Uuid",
            description="See DeviceType.tex. The primary container element for each piece of\n      equipment. device is organized within the devices container.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    version: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2016",
            browseName="ns=mt_connect;Version",
            description="See DeviceType.tex. The primary container element for each piece of\n      equipment. device is organized within the devices container.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.objecttype(
    nodeId="ns=mt_connect;i=4326",
    browseName="ns=mt_connect;MTConditionEventType",
    displayName="MTConditionEventType",
    description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
)
class MTConditionEventType(ns0.objtypes.ConditionType):
    activeState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4336",
            browseName="ns=mt_connect;ActiveState",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.LocalizedText,
            valueRank=-1,
        )
    )
    dataItemId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4327",
            browseName="ns=mt_connect;DataItemId",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4328",
            browseName="ns=mt_connect;MTSeverity",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=mt_connect_datypes.MTSeverityDataType,
            valueRank=-1,
        )
    )
    mTSubTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4329",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4330",
            browseName="ns=mt_connect;MTTypeName",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4331",
            browseName="ns=mt_connect;NativeCode",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeSeverity: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4332",
            browseName="ns=mt_connect;NativeSeverity",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    qualifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=4333",
            browseName="ns=mt_connect;Qualifier",
            description="The condition type is derived from the UA \\uamodel{ContitionType}. When\n      the \\mtmodel{Warning} or \\mtmodel{Fault} state occurs, an\n      \\mtuatype{MTConditionEventType} \\uamodel{Event} is created with the\n      \\mtmodel{ActiveState} set to \\uamodel{True} and \\uamodel{Retain} set to\n      \\uamodel{True}. The severity is used to represent the MTConnect condition\n      states of Warning and Fault with the values of 500 and 1000 respectively.\n      A new \\uamodel{NodeId} will be created for every unique instance of the\n      MTConnect \\mtmodel{Condition} reported. When the \\mtmodel{Condition} goes\n      back to Normal, the \\mtmodel{ActiveState} is set to \\uamodel{False} and\n      \\uamodel{Retain} is also set to \\uamodel{False} with the \\uamodel{NodeId}\n      of the associated \\mtmodel{Condition}. If multiple MTConnect\n      \\mtmodel{Condition}s have been cleared at the same time, all currently\n      active \\mtuatype{MTConditionEventType} \\uamodel{Event}s will need to\n      deactivated. The \\mtuatype{MTConditionEventType} must set the\n      \\uamodel{BaseEvent} \\uamodel{SourceNode} to the related\n      \\mtuatype{MTConditionType} that represents the meta-data for this\n      Condition. The \\mtuatype{MTConditionEventType} will never be instantiated\n      in the \\uaterm{AddressSpace} as an \\uamodel{Object}.",
            dataType=mt_connect_datypes.QualifierDataType,
            valueRank=-1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, mt_connect_reftypes, mt_connect_datypes, mt_connect_vartypes
