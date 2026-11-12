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

"""
Type usage examples for the high-level o6 library.

Uses the OPC UA types of the ``o6`` package. Scalar wrappers live at
the top level (``o6.NodeId``, ``o6.Int32``, ...). NS0 struct and enum
types live under ``o6.ns.ns0.datatypes``.
"""

import o6
from o6.ns import ns0


def main():

    print("--- 1. NodeId Creation ---")

    node1 = o6.NodeId("ns=1;s=Temperature")
    print(f"String NodeId: {node1}")

    node2 = o6.NodeId("ns=2;i=1234")
    print(f"Numeric NodeId: {node2}")


    print("\n--- 2. Scalar Type Wrappers ---")

    var1 = o6.Int32(42)
    print(f"Int32: {var1}")

    var2 = o6.Double(3.14159)
    print(f"Double: {var2}")

    var3 = o6.String("Hello World")
    print(f"String: {var3}")

    var4 = o6.Boolean(True)
    print(f"Boolean: {var4}")

    var5 = o6.UInt32(42)
    print(f"UInt32: {var5}")

    var6 = o6.Float(3.14)
    print(f"Float: {var6}")


    print("\n--- 3. DataValue Creation ---")

    dv1 = o6.DataValue()
    dv1.value = o6.Double(25.5)
    print(f"DataValue: {dv1}")
    print(f"  value: {dv1.value}")


    print("\n--- 4. Localized Text ---")

    lt1 = o6.LocalizedText("Hello World")
    print(f"LocalizedText: {lt1}")

    lt2 = o6.LocalizedText("Hallo Welt", "de")
    print(f"German locale: {lt2}")

    lt3 = o6.LocalizedText("Bonjour le monde", "fr")
    print(f"French locale: {lt3}")


    print("\n--- 5. Qualified Name ---")

    qn1 = o6.QualifiedName("0:MyVariable")
    print(f"Default namespace: {qn1}")

    qn2 = o6.QualifiedName("1:Temperature")
    print(f"Namespace 1: {qn2}")


    print("\n--- 6. OPC UA Struct Types ---")

    app_desc = ns0.datatypes.ApplicationDescription()
    app_desc.applicationUri = "urn:example:app"
    app_desc.applicationName = o6.LocalizedText("My Application")
    app_desc.applicationType = ns0.datatypes.ApplicationType.CLIENT
    app_desc.productUri = "urn:example:product"
    print(f"ApplicationDescription: {app_desc}")
    print(f"  application_uri: {app_desc.applicationUri}")
    print(f"  application_name: {app_desc.applicationName}")
    print(f"  application_type: {app_desc.applicationType}")

    read_val_id = ns0.datatypes.ReadValueId()
    read_val_id.nodeId = o6.NodeId("ns=1;s=Temperature")
    read_val_id.attributeId = o6.UInt32(13)  # Value attribute
    print(f"\nReadValueId: {read_val_id}")


    print("\n--- 7. Available Struct/Enum Types ---")

    type_names = sorted(
        [name for name in dir(ns0.datatypes) if not name.startswith("_") and name[0].isupper()]
    )
    print(f"Total available types: {len(type_names)}")
    print(f"First 20: {type_names[:20]}")

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()