#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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

"""
Low-level OPC UA Types Example
==============================

Constructs and inspects the OPC UA built-in datatypes at the top level
of the ``o6`` package.

Topics covered:

- Constructing and inspecting ``o6.NodeId`` values (numeric, string, GUID)
- Using ``o6.StatusCode`` as an ``IntFlag`` enum
- Iterating OPC UA enum types (``UserTokenType``, ``NodeClass``, ...)
- Building ``o6.QualifiedName`` and ``o6.LocalizedText`` values
- Wrapping raw numbers, booleans, dates and strings in typed wrappers
  (``o6.Int32``, ``o6.Double``, ``o6.Boolean``, ``o6.DateTime``, ...)
- Building ``o6.DataValue`` and setting its ``value``, ``status`` and
  timestamp fields
- Working with NS0 struct types (``RequestHeader``, ``CallRequest``,
  ``CallMethodRequest``) from ``o6.ns.ns0``

No server is required; the example only constructs and prints values.
"""



from datetime import datetime
from enum import Enum

import o6
from o6.ns import ns0


print("--- 1. NodeId - parsing and inspection ---")

# Parse a numeric NodeId from the standard 'ns=<n>;i=<id>' form.
n_numeric = o6.NodeId("ns=2;i=5")
print(f"numeric: {n_numeric}")  # -> 'ns=2;i=5'
print(f"  id:    {n_numeric.id}")  # -> 5
print(f"  ns:    {n_numeric.ns.index}")  # ns is a Namespace object,
# .index is the numeric index

# String-id form: 'ns=<n>;s=<name>'.
n_str = o6.NodeId("ns=3;s=Temperature")
print(f"\nstring:  {n_str}")
print(f"  id:    {n_str.id}")  # -> 'Temperature'

# GUID form: the id comes back as a stdlib uuid.UUID.
n_guid = o6.NodeId("g=09087e75-8e5e-499b-954f-f2a9603db28a")
print(f"\nguid:    {n_guid}")
print(f"  id:    {n_guid.id} (type={type(n_guid.id).__name__})")

# Build a NodeId from keyword arguments or by copying another.
n_kw = o6.NodeId(ns=2, i=1234)
n_copy = o6.NodeId(n_numeric)
print(f"\nkeyword: {n_kw}")
print(f"copy:    {n_copy}")



print("\n--- 2. StatusCode - IntFlag, auto-generated ---")

s_good = o6.StatusCode(0)  # -> Good
s_bad_internal = o6.StatusCode(0x80020000)  # -> BadInternalError

# Comparing a numeric value against a named member is just equality.
print(f"is BadInternalError? {s_bad_internal == o6.StatusCode.BAD_INTERNAL_ERROR}")

# Severity lives in the top 2 bits.
print(f"severity (top 2 bits): {hex(int(s_bad_internal) & 0xC0000000)}")



print("\n--- 3. Generated OPC UA enums ---")

UserTokenType = ns0.datatypes.UserTokenType
NodeClass = ns0.datatypes.NodeClass
NamingRuleType = ns0.datatypes.NamingRuleType

print(f"UserTokenType members:    {list(UserTokenType)}")
print(f"NodeClass members:        {list(NodeClass)}")
print(f"NamingRuleType.MANDATORY: {NamingRuleType.MANDATORY}")

# Look up an enum member by integer value.
tok_username = UserTokenType(1)
print(
    f"UserTokenType(1):         {tok_username} "
    f"(== USERNAME: {tok_username == UserTokenType.USER_NAME})"
)


# Stdlib Enum works the same way for comparison.
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3


print(f"Python enum for compare:  {Weekday(2)}")



print("\n--- 4. QualifiedName - locale-independent browse names ---")

# The 'ns:name' shorthand assigns the namespace index before the colon.
qn_default = o6.QualifiedName("MyVariable")
print(
    f"QualifiedName('MyVariable'):     {qn_default}  "
    f"(ns.index={qn_default.ns.index}, name={qn_default.name!r})"
)

qn_explicit = o6.QualifiedName("2:MyDevice")
print(
    f"QualifiedName('2:MyDevice'):     {qn_explicit}  "
    f"(ns.index={qn_explicit.ns.index}, name={qn_explicit.name!r})"
)

# Or build it positionally: (ns_index, name).
qn_pos = o6.QualifiedName(0, "Temperature")
print(
    f"QualifiedName(0, 'Temperature'): {qn_pos}  "
    f"(ns.index={qn_pos.ns.index}, name={qn_pos.name!r})"
)



print("\n--- 5. LocalizedText - text + locale ---")

# Single-argument form: text only, no locale.
lt_no_locale = o6.LocalizedText("Hello World")
print(f"LocalizedText('Hello World'):       {lt_no_locale}")
print(f"  text:   {lt_no_locale.text!r}")
print(f"  locale: {lt_no_locale.locale!r}")

# Two-argument form: (text, locale).
lt_en = o6.LocalizedText("Hello", "en")
lt_de = o6.LocalizedText("Hallo Welt", "de")
print(
    f"\nLocalizedText('Hello', 'en'):       {lt_en}  "
    f"(text={lt_en.text!r}, locale={lt_en.locale!r})"
)
print(
    f"LocalizedText('Hallo Welt', 'de'):  {lt_de}  "
    f"(text={lt_de.text!r}, locale={lt_de.locale!r})"
)

# A handful of localised greetings — useful for human-readable labels.
print("\nGreetings in three languages:")
for text, locale in [("Hello", "en"), ("Bonjour", "fr"), ("Hola", "es")]:
    lt = o6.LocalizedText(text, locale)
    print(f"  {lt.locale}: {lt.text}")



print("\n--- 6. Primitive type wrappers ---")

v_int = o6.Int32(42)
v_dbl = o6.Double(3.14159)
v_flt = o6.Float(3.14)
v_u32 = o6.UInt32(42)
v_bool = o6.Boolean(True)
v_str = o6.String("Hello World")

print(f"Int32(42):     {v_int}   (underlying: {type(v_int).__name__})")
print(f"Double(pi):    {v_dbl}   (underlying: {type(v_dbl).__name__})")
print(f"Float(3.14):   {v_flt}   (underlying: {type(v_flt).__name__})")
print(f"UInt32(42):    {v_u32}   (underlying: {type(v_u32).__name__})")
print(f"Boolean(True): {v_bool}")
print(f"String(...):   {v_str}")

# DateTime wraps Python's stdlib datetime.
now = datetime.now()
v_dt = o6.DateTime(now)
print(f"\nDateTime(now): {v_dt}")



print("\n--- 7. DataValue - value + status + timestamps ---")

# Simple integer DataValue, no status / timestamps set.
dv1 = o6.DataValue()
dv1.value = o6.Int32(42)
print(f"integer DataValue:       {dv1}")

# DataValue with an explicit status code (Good = success).
dv2 = o6.DataValue()
dv2.value = o6.String("Hello World")
dv2.status = o6.StatusCode(0)
print(f"string + status=Good:    {dv2}")

# DataValue with both source- and server-timestamps. Source timestamp is
# the time the value was *observed* at its source; server timestamp is
# the time the server *received* it.
dv3 = o6.DataValue()
dv3.value = o6.Double(3.14159)
dv3.sourceTimestamp = o6.DateTime(now)
dv3.serverTimestamp = o6.DateTime(now)
print(f"value + 2 timestamps:    {dv3}")

# All fields can be read back independently.
print(f"\n  dv3.value:            {dv3.value}")
print(f"  dv3.status:           {dv3.status}")
print(f"  dv3.sourceTimestamp:  {dv3.sourceTimestamp}")
print(f"  dv3.serverTimestamp:  {dv3.serverTimestamp}")



print("\n--- 8. NS0 struct types - RequestHeader, CallRequest, CallMethodRequest ---")

RequestHeader = ns0.datatypes.RequestHeader
CallRequest = ns0.datatypes.CallRequest
CallMethodRequest = ns0.datatypes.CallMethodRequest

# RequestHeader carries the standard timeout / diagnostics fields.
rh = RequestHeader()
rh.timeoutHint = 1000  # request timeout in ms
rh.returnDiagnostics = 0
print(f"RequestHeader.timeoutHint:       {rh.timeoutHint}")
print(
    f"RequestHeader.returnDiagnostics: {rh.returnDiagnostics} "
    f"(type: {type(rh.returnDiagnostics).__name__})"
)

# A CallRequest is a header plus a list of CallMethodRequests.
call_request = CallRequest()
call_request.requestHeader = RequestHeader()
call_request.requestHeader.timeoutHint = 1000
call_request.requestHeader.returnDiagnostics = 0

# First call: invoke method ns=2;i=456 on object ns=2;i=123.
m1 = CallMethodRequest()
m1.objectId = o6.NodeId("ns=2;i=123")
m1.methodId = o6.NodeId("ns=2;i=456")
call_request.methodsToCall.append(m1)

# Second call: another object/method pair. input_arguments defaults to [].
m2 = CallMethodRequest()
m2.objectId = o6.NodeId("ns=2;i=789")
m2.methodId = o6.NodeId("ns=2;i=1011")
call_request.methodsToCall.append(m2)

print(f"\nCallRequest.methodsToCall has {len(call_request.methodsToCall)} entries")
for idx, m in enumerate(call_request.methodsToCall, 1):
    print(
        f"  method {idx}: object_id={m.objectId}, "
        f"method_id={m.methodId}, input_arguments={m.inputArguments}"
    )

print("\n=== Example completed ===")