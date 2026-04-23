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
from o6._o6.types_builtin import *
from o6._o6.types_builtin import (
    Boolean as Boolean,
    SByte as SByte,
    Byte as Byte,
    Int16 as Int16,
    UInt16 as UInt16,
    Int32 as Int32,
    UInt32 as UInt32,
    Int64 as Int64,
    UInt64 as UInt64,
    Float as Float,
    Double as Double,
    String as String,
    StatusCode as StatusCode,
    DateTime as DateTime,
    NodeId as NodeId,
    NodeIdLike as NodeIdLike,
    ExpandedNodeId as ExpandedNodeId,
    QualifiedName as QualifiedName,
    LocalizedText as LocalizedText,
    DataValue as DataValue,
)
from o6._o6.types_gen import *

# EventFilter is excluded from types_gen.__all__
# (o6.types re-exports it); here we add any extra API that the
# C extension exposes but the auto-generated stub cannot describe.
from o6._o6.types_gen import EventFilter as _EventFilterBase
from o6._o6.types_gen import DataChangeFilter as DataChangeFilter
from o6._o6.types_gen import SimpleAttributeOperand as SimpleAttributeOperand
from o6._o6.types_gen import RelativePath as RelativePath
from o6._o6.types_gen import ReadValueId as ReadValueId
from typing import Any
import enum

def _parseRelativePath(s: str) -> RelativePath: ...
def _printRelativePath(r: RelativePath) -> str: ...
def _parseSimpleAttributeOperand(s: str) -> SimpleAttributeOperand: ...
def _printSimpleAttributeOperand(o: SimpleAttributeOperand) -> str: ...
def _parseReadValueId(s: str) -> ReadValueId: ...
def _printReadValueId(r: ReadValueId) -> str: ...

# UA_DataTypeKind from open62541/types.h — not part of the OPC UA spec, so
# the autogenerator never produces it.  Registered by hand in src/types.c.
class DataTypeKind(enum.IntEnum):
    Boolean = 0
    SByte = 1
    Byte = 2
    Int16 = 3
    UInt16 = 4
    Int32 = 5
    UInt32 = 6
    Int64 = 7
    UInt64 = 8
    Float = 9
    Double = 10
    String = 11
    DateTime = 12
    Guid = 13
    ByteString = 14
    XmlElement = 15
    NodeId = 16
    ExpandedNodeId = 17
    StatusCode = 18
    QualifiedName = 19
    LocalizedText = 20
    ExtensionObject = 21
    DataValue = 22
    Variant = 23
    DiagnosticInfo = 24
    Decimal = 25
    Enum = 26
    Structure = 27
    OptStruct = 28
    Union = 29
    BitFieldCluster = 30

# EventFilter.parse is added as C extension method, so we update the type signature here.
class EventFilter(_EventFilterBase):
    """OPC UA EventFilter; includes the parse() classmethod added by the C extension."""

    @classmethod
    def parse(cls, query: str, logger: Any = ...) -> EventFilter: ...
