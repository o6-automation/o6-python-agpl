#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Low-level OPC UA Types Example
==============================

Demonstrates how to construct and inspect the OPC UA built-in datatypes
exposed at the top level of the ``o6`` package.

Topics covered:

- Constructing and inspecting ``o6.NodeId`` values (numeric, string, GUID)
- Using ``o6.StatusCode`` as an ``IntFlag`` enum
- Iterating OPC UA enum types (``UserTokenType``, ``NodeClass``, ...)
- Building ``o6.QualifiedName`` and ``o6.LocalizedText`` values
- Wrapping raw numbers, booleans, dates, and strings in typed wrappers
  (``o6.Int32``, ``o6.Double``, ``o6.Boolean``, ``o6.DateTime``, ...)
- Building ``o6.DataValue`` and setting its ``value`` / ``status`` /
  timestamps fields
- Working with NS0 struct types (``RequestHeader``, ``CallRequest``,
  ``CallMethodRequest``) reached via ``o6.ns.ns0``

No server is required — the example only constructs values and prints them.
"""

# BEGIN MD
# END MD


from datetime import datetime
from enum import Enum

import o6
from o6.ns import ns0


def header(title: str) -> None:
    """Tiny helper to print a banner around each section."""
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)


# ---------------------------------------------------------------------------
# 1. NodeId — the unique handle of a node in a server's address space.
# ---------------------------------------------------------------------------
header("1. NodeId — parsing and inspection")

# BEGIN MD
# ## 1. NodeId - parsing and inspection
# A `NodeId` is the machine-readable identity of every node in an OPC UA
# address space. It is composed of two fields:
#
# - a **namespace index** — which naming authority the identifier belongs to, and
# - an **id** — a numeric, string, GUID, or byte-string identifier.
#
# Note that `NodeId.ns` is **not** a bare integer — it's an `o6.Namespace`
# object that also carries the namespace URI, shortname, version, etc. Use
# `n.ns.index` for the numeric index and `n.ns.uri` / `n.ns.shortname` for
# human-readable metadata.
# END MD

# BEGIN CODE
# Parse a numeric NodeId from the standard 'ns=<n>;i=<id>' form.
n_numeric = o6.NodeId("ns=1;i=5")
print(f"numeric: {n_numeric}")  # -> 'ns=1;i=5'
print(f"  id:    {n_numeric.id}")  # -> 5
print(f"  ns:    {n_numeric.ns.index}")  # ns is a Namespace object,
# .index is the numeric index

# String-id form: 'ns=<n>;s=<name>'.
n_str = o6.NodeId("ns=2;s=Temperature")
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
# END CODE


# ---------------------------------------------------------------------------
# 2. StatusCode — an IntFlag enum auto-generated from the OPC UA spec.
# ---------------------------------------------------------------------------
header("2. StatusCode — IntFlag, auto-generated")

# BEGIN MD
# ## 2. StatusCode - IntFlag, auto-generated
# Every service response in OPC UA carries a 32-bit `StatusCode`.
# `o6.StatusCode` is a Python `IntFlag` generated from the OPC UA
# status-code table, so values can be compared, looked up by name, and
# combined with bitwise operators.
#
# The top two bits encode the severity:
#
# | Bits 31–30 | Severity |
# |---|---|
# | `00` | Good |
# | `01` | Uncertain |
# | `10` | Bad |
# END MD

# BEGIN CODE
s_good = o6.StatusCode(0)  # -> Good
s_bad_internal = o6.StatusCode(0x80020000)  # -> BadInternalError

# Comparing a numeric value against a named member is just equality.
print(f"is BadInternalError? " f"{s_bad_internal == o6.StatusCode.BAD_INTERNAL_ERROR}")

# Severity lives in the top 2 bits.
print(f"severity (top 2 bits): " f"{hex(int(s_bad_internal) & 0xC0000000)}")
# END CODE


# ---------------------------------------------------------------------------
# 3. Generated enums — every OPC UA enum from the spec is exposed.
# ---------------------------------------------------------------------------
header("3. Generated OPC UA enums")

# BEGIN MD
# ## 3. Generated OPC UA enums
# NS0 enum types generated from the spec (`UserTokenType`, `NodeClass`,
# `NamingRuleType`, ...) live under `o6.ns.ns0`. Members use the
# upper-case spelling from the spec. The generated enums look and behave
# just like `enum.IntEnum` / `enum.IntFlag` in the standard library.
# END MD

# BEGIN CODE
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
# END CODE


# ---------------------------------------------------------------------------
# 4. QualifiedName — (namespace, name) pair used as a browse name.
# ---------------------------------------------------------------------------
header("4. QualifiedName — locale-independent browse names")

# BEGIN MD
# ## 4. QualifiedName - locale-independent browse names
# A `QualifiedName` is a `(namespace, name)` pair used as the
# locale-independent, human-readable vocabulary of an address space. The
# `ns` attribute is a `Namespace` object — use `.index` for the numeric
# value, `.uri` for the full URI, `.shortname` for the snake-case name.
# END MD

# BEGIN CODE
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
# END CODE


# ---------------------------------------------------------------------------
# 5. LocalizedText — string paired with an IETF language tag.
# ---------------------------------------------------------------------------
header("5. LocalizedText — text + locale")

# BEGIN MD
# ## 5. LocalizedText - text + locale
# A `LocalizedText` pairs a string with an IETF language tag
# (`en`, `de-DE`, `fr-CA`, ...). The locale is **part of the value's
# identity**: two `LocalizedText` values with the same text but different
# locales are *not* equal.
# END MD

# BEGIN CODE
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
# END CODE


# ---------------------------------------------------------------------------
# 6. Primitive type wrappers — Int32, Double, Boolean, DateTime, String.
# ---------------------------------------------------------------------------
header("6. Primitive type wrappers")

# BEGIN MD
# ## 6. Primitive type wrappers
# The 25 OPC UA built-in types from Part 3 §8 each have a fixed-width
# wrapper class. Numeric wrappers are NumPy scalars so the wire-format
# width matches exactly:
#
# | Wrapper | Underlying type |
# |---|---|
# | `o6.Boolean` | `bool` |
# | `o6.Int32`, `o6.UInt32`, ... | `np.int32`, `np.uint32`, ... |
# | `o6.Float`, `o6.Double` | `np.float32`, `np.float64` |
# | `o6.String` | `str` |
# | `o6.DateTime` | `datetime.datetime` |
# | `o6.Guid` | `uuid.UUID` |
# | `o6.ByteString` | `bytes` |
# | `o6.XmlElement` | `str` |
# END MD

# BEGIN CODE
# Numeric wrappers are NumPy scalars with a fixed width matching the OPC UA
# wire format.
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
# END CODE


# ---------------------------------------------------------------------------
# 7. DataValue — value + status + (optional) timestamps.
# ---------------------------------------------------------------------------
header("7. DataValue — value + status + timestamps")

# BEGIN MD
# ## 7. DataValue - value + status + timestamps
# Every read, write, and monitored-item notification in OPC UA carries a
# `DataValue` — a wrapper bundling the raw value, a status code, and
# optional source/server timestamps. All four fields are optional and can
# be set independently.
# END MD

# BEGIN CODE
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
print(f"\n  dv3.value:             {dv3.value}")
print(f"  dv3.status:            {dv3.status}")
print(f"  dv3.sourceTimestamp:  {dv3.sourceTimestamp}")
print(f"  dv3.serverTimestamp:  {dv3.serverTimestamp}")
# END CODE


# ---------------------------------------------------------------------------
# 8. NS0 struct types — RequestHeader, CallRequest, CallMethodRequest.
# ---------------------------------------------------------------------------
header("8. NS0 struct types (RequestHeader / CallRequest)")

# BEGIN MD
# ## 8. NS0 struct types - RequestHeader, CallRequest, CallMethodRequest
# The NS0 service-request struct types — `RequestHeader`, `CallRequest`,
# `CallMethodRequest`, `Argument`, ... — live under
# `o6.ns.ns0`. They use plain attribute-style field access:
# just assign a value to set it.
#
# `CallRequest.methodsToCall` is a mutable list — append
# `CallMethodRequest` entries to batch multiple method calls into a
# single `serviceCall`.
# END MD

# BEGIN CODE
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
# END CODE


# ---------------------------------------------------------------------------
# Done.
# ---------------------------------------------------------------------------
header("End of low-level types example")
