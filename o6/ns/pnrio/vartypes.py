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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=pnrio;i=2002", browseName="ns=pnrio;RioPaProcessValueQualifierVariableType", displayName="RioPaProcessValueQualifierVariableType", dataType=o6.Byte)
class RioPaProcessValueQualifierVariableType(ns0.vartypes.BaseDataVariableType):
    nE_107: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6048", browseName="ns=pnrio;NE_107", dataType=pnrio_datypes.RioSpecifierEnumeration)
    )
    quality: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6047", browseName="ns=pnrio;Quality", dataType=pnrio_datypes.RioQualityEnumeration)
    )
    status_full: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6049", browseName="ns=pnrio;Status_full", dataType=pnrio_datypes.RioQualifierEnumeration)
    )


@o6.variabletype(nodeId="ns=pnrio;i=2003", browseName="ns=pnrio;RioFaProcessValueQualifierVariableType", displayName="RioFaProcessValueQualifierVariableType", dataType=o6.Boolean)
class RioFaProcessValueQualifierVariableType(ns0.vartypes.BaseDataVariableType):
    quality: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6050", browseName="ns=pnrio;Quality", dataType=pnrio_datypes.RioQualityEnumeration)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2004",
    browseName="ns=pnrio;RioPaDigitalProcessValueVariableType",
    displayName="RioPaDigitalProcessValueVariableType",
    dataType=pnrio_datypes.RioPaDigitalProcessValueDataType,
    value=pnrio_datypes.RioPaDigitalProcessValueDataType(value=False, qualifier=0, quality=0, nE_107=0, status_full=0),
)
class RioPaDigitalProcessValueVariableType(ns0.vartypes.BaseDataVariableType):
    dataValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6051", browseName="ns=pnrio;DataValue", dataType=o6.Boolean)
    )
    qualifierValue: RioPaProcessValueQualifierVariableType | None = o6.hasComponent(
        RioPaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6052", browseName="ns=pnrio;QualifierValue", dataType=o6.Byte)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2005",
    browseName="ns=pnrio;RioFaDigitalProcessValueVariableType",
    displayName="RioFaDigitalProcessValueVariableType",
    dataType=pnrio_datypes.RioFaDigitalProcessValueDataType,
    value=pnrio_datypes.RioFaDigitalProcessValueDataType(value=False, qualifier=False, quality=0),
)
class RioFaDigitalProcessValueVariableType(ns0.vartypes.BaseDataVariableType):
    dataValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnrio;i=6053", browseName="ns=pnrio;DataValue", dataType=o6.Boolean)
    )
    qualifierValue: RioFaProcessValueQualifierVariableType | None = o6.hasComponent(
        RioFaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6054", browseName="ns=pnrio;QualifierValue", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2006",
    browseName="ns=pnrio;RioPaAnalogProcessValueVariableType",
    displayName="RioPaAnalogProcessValueVariableType",
    dataType=pnrio_datypes.RioPaAnalogProcessValueDataType,
)
class RioPaAnalogProcessValueVariableType(ns0.vartypes.BaseDataVariableType):
    dataValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6035", browseName="ns=pnrio;DataValue", dataType=ns0.datatypes.Number)
    )
    qualifierValue: RioPaProcessValueQualifierVariableType | None = o6.hasComponent(
        RioPaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6056", browseName="ns=pnrio;QualifierValue", dataType=o6.Byte)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2007",
    browseName="ns=pnrio;RioFaAnalogProcessValueVariableType",
    displayName="RioFaAnalogProcessValueVariableType",
    dataType=pnrio_datypes.RioFaAnalogProcessValueDataType,
)
class RioFaAnalogProcessValueVariableType(ns0.vartypes.BaseDataVariableType):
    dataValue: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnrio;i=6036", browseName="ns=pnrio;DataValue", dataType=ns0.datatypes.Number)
    )
    qualifierValue: RioFaProcessValueQualifierVariableType | None = o6.hasComponent(
        RioFaProcessValueQualifierVariableType(nodeId="ns=pnrio;i=6058", browseName="ns=pnrio;QualifierValue", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2012",
    browseName="ns=pnrio;RioPaAnalogInputConfigVariableType",
    displayName="RioPaAnalogInputConfigVariableType",
    dataType=pnrio_datypes.RioPaAnalogInputConfigDataType,
    value=pnrio_datypes.RioPaAnalogInputConfigDataType(
        damping=0.0,
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
        highLimit=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
        lowLimit=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
    ),
)
class RioPaAnalogInputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    damping: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6081", browseName="ns=pnrio;Damping", dataType=o6.Float))
    highLimit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6088", browseName="ns=pnrio;HighLimit", dataType=pnrio_datypes.RioAnalogDataType)
    )
    lowLimit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6089", browseName="ns=pnrio;LowLimit", dataType=pnrio_datypes.RioAnalogDataType)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6082", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6086", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6087", browseName="ns=pnrio;SubstituteValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6083", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2014",
    browseName="ns=pnrio;RioPaAnalogOutputConfigVariableType",
    displayName="RioPaAnalogOutputConfigVariableType",
    dataType=pnrio_datypes.RioPaAnalogOutputConfigDataType,
    value=pnrio_datypes.RioPaAnalogOutputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
        substituteTime=0.0,
    ),
)
class RioPaAnalogOutputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6095", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6099", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteTime: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6101", browseName="ns=pnrio;SubstituteTime", dataType=o6.Float))
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6100", browseName="ns=pnrio;SubstituteValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6096", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2016",
    browseName="ns=pnrio;RioBitFieldVariableType",
    displayName="RioBitFieldVariableType",
    dataType=pnrio_datypes.RioBitFieldDataType,
    value=pnrio_datypes.RioBitFieldDataType(bitData=0, bitUsed=0),
)
class RioBitFieldVariableType(ns0.vartypes.BaseDataVariableType):
    offset: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6185", browseName="ns=pnrio;Offset", dataType=o6.UInt16))


@o6.variabletype(
    nodeId="ns=pnrio;i=2008",
    browseName="ns=pnrio;RioPaDigitalInputConfigVariableType",
    displayName="RioPaDigitalInputConfigVariableType",
    dataType=pnrio_datypes.RioPaDigitalInputConfigDataType,
    value=pnrio_datypes.RioPaDigitalInputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        inversionEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=False,
    ),
)
class RioPaDigitalInputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    inversionEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6280", browseName="ns=pnrio;InversionEnabled", dataType=o6.Boolean)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6059", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6063", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6064", browseName="ns=pnrio;SubstituteValue", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6060", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2009",
    browseName="ns=pnrio;RioFaDigitalInputConfigVariableType",
    displayName="RioFaDigitalInputConfigVariableType",
    dataType=pnrio_datypes.RioFaDigitalInputConfigDataType,
    value=pnrio_datypes.RioFaDigitalInputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        supplyVoltageCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=False,
    ),
)
class RioFaDigitalInputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6065", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6067", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6068", browseName="ns=pnrio;SubstituteValue", dataType=o6.Boolean)
    )
    supplyVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6281", browseName="ns=pnrio;SupplyVoltageCheckEnabled", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6066", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2010",
    browseName="ns=pnrio;RioPaDigitalOutputConfigVariableType",
    displayName="RioPaDigitalOutputConfigVariableType",
    dataType=pnrio_datypes.RioPaDigitalOutputConfigDataType,
    value=pnrio_datypes.RioPaDigitalOutputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        inversionEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=False,
        substituteTime=0.0,
    ),
)
class RioPaDigitalOutputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    inversionEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6282", browseName="ns=pnrio;InversionEnabled", dataType=o6.Boolean)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6069", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6073", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteTime: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6075", browseName="ns=pnrio;SubstituteTime", dataType=o6.Float))
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6074", browseName="ns=pnrio;SubstituteValue", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6070", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2011",
    browseName="ns=pnrio;RioFaDigitalOutputConfigVariableType",
    displayName="RioFaDigitalOutputConfigVariableType",
    dataType=pnrio_datypes.RioFaDigitalOutputConfigDataType,
    value=pnrio_datypes.RioFaDigitalOutputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        supplyVoltageCheckEnabled=False,
        loadVoltageCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=False,
        substituteTime=0.0,
    ),
)
class RioFaDigitalOutputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    loadVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6284", browseName="ns=pnrio;LoadVoltageCheckEnabled", dataType=o6.Boolean)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6076", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6078", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteTime: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6080", browseName="ns=pnrio;SubstituteTime", dataType=o6.Float))
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6079", browseName="ns=pnrio;SubstituteValue", dataType=o6.Boolean)
    )
    supplyVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6283", browseName="ns=pnrio;SupplyVoltageCheckEnabled", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6077", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2013",
    browseName="ns=pnrio;RioFaAnalogInputConfigVariableType",
    displayName="RioFaAnalogInputConfigVariableType",
    dataType=pnrio_datypes.RioFaAnalogInputConfigDataType,
    value=pnrio_datypes.RioFaAnalogInputConfigDataType(
        damping=0.0,
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        supplyVoltageCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
    ),
)
class RioFaAnalogInputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    damping: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6090", browseName="ns=pnrio;Damping", dataType=o6.Float))
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6091", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6093", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6094", browseName="ns=pnrio;SubstituteValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    supplyVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6285", browseName="ns=pnrio;SupplyVoltageCheckEnabled", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6092", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


@o6.variabletype(
    nodeId="ns=pnrio;i=2015",
    browseName="ns=pnrio;RioFaAnalogOutputConfigVariableType",
    displayName="RioFaAnalogOutputConfigVariableType",
    dataType=pnrio_datypes.RioFaAnalogOutputConfigDataType,
    value=pnrio_datypes.RioFaAnalogOutputConfigDataType(
        signalType=pnrio_datypes.RioSignalTypeEnumeration.CURRENT_4_20_M_A,
        wireCheckEnabled=False,
        supplyVoltageCheckEnabled=False,
        loadVoltageCheckEnabled=False,
        substitutePolicy=pnrio_datypes.RioSubstitutePolicyEnumeration.USE_SUBSTITUTE_VALUE,
        substituteValue=pnrio_datypes.RioAnalogDataType(float_32=0.0, int_16=0, int_32=0, uInt_16=0, uInt_32=0),
        substituteTime=0.0,
    ),
)
class RioFaAnalogOutputConfigVariableType(ns0.vartypes.BaseDataVariableType):
    loadVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6287", browseName="ns=pnrio;LoadVoltageCheckEnabled", dataType=o6.Boolean)
    )
    signalType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6102", browseName="ns=pnrio;SignalType", dataType=pnrio_datypes.RioSignalTypeEnumeration)
    )
    substitutePolicy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6104", browseName="ns=pnrio;SubstitutePolicy", dataType=pnrio_datypes.RioSubstitutePolicyEnumeration)
    )
    substituteTime: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6106", browseName="ns=pnrio;SubstituteTime", dataType=o6.Float))
    substituteValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6105", browseName="ns=pnrio;SubstituteValue", dataType=pnrio_datypes.RioAnalogDataType)
    )
    supplyVoltageCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6286", browseName="ns=pnrio;SupplyVoltageCheckEnabled", dataType=o6.Boolean)
    )
    wireCheckEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnrio;i=6103", browseName="ns=pnrio;WireCheckEnabled", dataType=o6.Boolean)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnrio_reftypes, pnrio_datypes
