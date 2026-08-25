#!/usr/bin/env python3
"""Python parity for open62541 tutorial_datatypes."""

from o6 import NodeId, types


def main() -> None:
    print("=== tutorial_datatypes (Python parity) ===")

    print("\n[Basic Data Handling]")
    i = types.Int32(42)
    d = types.Double(3.1415)
    s = types.String("hello")
    print("Int32:", i)
    print("Double:", d)
    print("String:", s)

    print("\n[NodeIds]")
    numeric = NodeId("ns=1;i=1001")
    string = NodeId("ns=1;s=Temperature")
    guid = NodeId("ns=1;g=09087e75-8e5e-499b-954f-f2a9603db28a")
    print("Numeric NodeId:", numeric)
    print("String NodeId:", string)
    print("Guid NodeId:", guid)

    print("\n[Variants / DataValue]")
    v1 = types.Variant(types.UInt32(7))
    v2 = types.Variant(types.Double(12.5))
    dv = types.DataValue(value=v2)
    print("Variant UInt32:", v1)
    print("Variant Double:", v2)
    print("DataValue:", dv)


if __name__ == "__main__":
    main()
