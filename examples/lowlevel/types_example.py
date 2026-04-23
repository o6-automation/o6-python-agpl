from o6 import _o6
from o6._o6 import types
from enum import Enum
from datetime import datetime
import numpy as np

x = types.NodeId("ns=1;i=5")
print(x)  # ns=1;i=5
# print(repr(x)) # 'o6.types.NodeId(ns=1;i=5)'
print(x.id)  # 5
print(x.ns)  # 1

y = types.NodeId("g=09087e75-8e5e-499b-954f-f2a9603db28a")
print(y.id)  #  UUID('09087e75-8e5e-499b-954f-f2a9603db28a')

s = types.StatusCode()
print(s)
# print(repr(s))

s2 = types.StatusCode(5)
# print(repr(s2))

s3 = types.StatusCode(0x80020000)
# print(repr(s3))
# print(s3.name)
# print(s3.code)


# s4 = types.RedundancySupport()
# print(s4)


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


weekday = Weekday(2)
print(weekday)  # Weekday.MONDAY
print(type(weekday))

s5 = types.NamingRuleType(2)
print(s5)
print(types.NamingRuleType.Mandatory)

print("type:")
print(types.UserTokenType)

s7 = types.UserTokenType.ANONYMOUS
print(s7)


print("assigned enum:")
s6 = types.UserTokenType(1)
print(s6)
print(type(s6))


print(vars(types.UserTokenType))
print("\n")
print(vars(Weekday))


print(types.UserTokenType.__bases__)  # 'RED'
print(Weekday.__bases__)  # 'RED'

print("\n" + "=" * 60)
print("ADDITIONAL EXAMPLES: QualifiedName, LocalizedText & Enums")
print("=" * 60)

print("\n--- QualifiedName Examples ---")
# Create QualifiedName with namespace and name

# First check if it's actually available
qn_type = getattr(types, "QualifiedName", None)
if qn_type is None:
    print("QualifiedName not available in this build")
else:
    qn1 = types.QualifiedName("1:MyVariable")
    print(f"QualifiedName: {qn1} (ns={qn1.ns}, name={qn1.name})")
    # Create QualifiedName without namespace (defaults to 0)
    qn2 = types.QualifiedName("SimpleVariable")
    print(f"QualifiedName (default ns): {qn2} (ns={qn2.ns}, name={qn2.name})")
    # Copy QualifiedName
    qn3 = types.QualifiedName(qn1.ns, qn1.name)
    print(f"Copied QualifiedName: {qn3} (equal: {qn3 == qn1})")

print("\n--- LocalizedText Examples ---")
# Create LocalizedText with just text

# First check if it's actually available
lt_type = getattr(types, "LocalizedText", None)
if lt_type is None:
    print("LocalizedText not available in this build")
else:
    lt1 = types.LocalizedText("Hello World")
    print(f"LocalizedText: {lt1} (text='{lt1.text}', locale='{lt1.locale}')")
    # Create LocalizedText with text and locale
    lt2 = types.LocalizedText("fr", "Bonjour le monde")
    print(f"LocalizedText (fr): {lt2} (text='{lt2.text}', locale='{lt2.locale}')")
    # Copy LocalizedText
    lt3 = types.LocalizedText(lt2.locale, lt2.text)
    print(f"Copied LocalizedText: {lt3} (equal: {lt3 == lt2})")


print("\n--- Enhanced Enum Examples ---")
# Show some enum usage

print(f"UserTokenType enum values: {list(types.UserTokenType)}")
print(f"NodeClass enum values: {list(types.NodeClass)}")
# Create enum from value
enum_val = types.UserTokenType(1)
print(
    f"UserTokenType(1): {enum_val} (is UserName: {enum_val == types.UserTokenType.USERNAME})"
)
# Use enums in a dict
enum_dict = {types.NodeClass.OBJECT: "object", types.NodeClass.VARIABLE: "variable"}
print(f"Enum dict lookup: {enum_dict[types.NodeClass.VARIABLE]}")

# Practical examples with error handling
print("\n--- Practical Examples ---")

# Practical: Internationalization with LocalizedText
print("\nLocalizedText Internationalization:")
lt_type = getattr(types, "LocalizedText", None)
if lt_type is None:
    print("LocalizedText not available for internationalization example")
else:
    greetings = [
        types.LocalizedText("en", "Hello"),
        types.LocalizedText("fr", "Bonjour"),
        types.LocalizedText("es", "Hola"),
    ]
    for g in greetings:
        print(f"  {g.locale}: {g.text}")

# Practical: QualifiedName for browse paths
print("\nQualifiedName Browse Path Example:")
qn_type = getattr(types, "QualifiedName", None)
if qn_type is None:
    print("QualifiedName not available for browse path example")
else:
    browse_path = [
        types.QualifiedName("0:Objects"),
        types.QualifiedName("2:MyDevice"),
        types.QualifiedName("2:TemperatureSensor"),
    ]
    print("Browse path:")
    for qn in browse_path:
        print(f"  ns={qn.ns}: {qn.name}")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)

print(types.UserTokenType.__qualname__)  # 'Color'

print("All members and their types in call_request:")
call_request = types.CallRequest()
for name in dir(call_request):
    if not name.startswith("_"):
        value = getattr(call_request, name)
        print(f"{name}: {type(value)}")

print(types.CallRequest.__doc__)

print("All members and their types in RequestHeader:")
request_header = types.RequestHeader()
for name in dir(request_header):
    if not name.startswith("_"):
        value = getattr(request_header, name)
        print(f"{name}: {type(value)}")

call_request = types.CallRequest()
call_request.request_header.timeout_hint = 1000
call_request.request_header.return_diagnostics = 0
print(call_request.request_header.timeout_hint)
# aisgn new header object
call_request.request_header = types.RequestHeader()
print(call_request.request_header.timeout_hint)

print(type(call_request.request_header.return_diagnostics))  # 0

# Add two CallMethodRequest objects to the MethodsToCall list
method1 = types.CallMethodRequest()
method1.object_id = types.NodeId("ns=2;i=123")
method1.method_id = types.NodeId("ns=2;i=456")
# method1.InputArguments = []
print("All members and their types in method1:")
for name in dir(method1):
    if not name.startswith("_"):
        value = getattr(method1, name)
        print(f"{name}: {type(value)}")

method2 = types.CallMethodRequest()
method2.object_id = types.NodeId("ns=2;i=789")
method2.method_id = types.NodeId("ns=2;i=1011")
# method2.InputArguments = []

call_request.methods_to_call.append(method1)
call_request.methods_to_call.append(method2)

print("Number of methods to call:", len(call_request.methods_to_call))
for idx, m in enumerate(call_request.methods_to_call, 1):
    print(
        f"Method {idx}: ObjectId={m.object_id}, MethodId={m.method_id}, InputArguments={m.input_arguments}"
    )


# DataValue examples
print("\n=== DataValue Examples ===")

# Create a simple DataValue with an integer value
dv1 = types.DataValue()
dv1.value = types.Int32(42)
print(f"Integer DataValue: {dv1}")

# Create a DataValue with a string value and status code
dv2 = types.DataValue()
dv2.value = types.String("Hello World")
dv2.status = types.StatusCode(0x00000000)
print(f"String DataValue with status: {dv2}")

# Create a DataValue with timestamps
import time

now = datetime.now()
dv3 = types.DataValue()
dv3.value = types.Double(3.14159)
dv3.source_timestamp = types.DateTime(now)
dv3.server_timestamp = types.DateTime(now)

print(f"DataValue with timestamps: {dv3}")

# Modify DataValue properties
dv4 = types.DataValue()
dv4.value = types.Boolean(True)
dv4.status = types.StatusCode(0x00000000)
print(f"Modified DataValue: {dv4}")

# Access individual properties
print(f"Value: {dv4.value}")
# print(f"Status: {hex(dv4.status) if dv4.status is not None else None}")
print(f"Source timestamp: {dv4.source_timestamp}")
print(f"Server timestamp: {dv4.server_timestamp}")

print("type:")
print(types.UserTokenType)
