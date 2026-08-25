# Registry

OPC UA namespace indices introduce an additional layer of complexity. o6\\Python manages them in the process-wide `o6.ns` registry, so application code can normally use namespace shortnames and URIs instead of numeric indices.

!!! info
    This page assumes the spec-level picture: a stable namespace URI versus a
    server-local index, the namespace array that maps between them, and why
    `ns0` and `ns1` are fixed. That background is
    [Namespace](../../opcua-fundamentals/namespace.md) in OPC UA Fundamentals.

```python
print(o6.ns)
```

We can print the current state of this global registry and see something like:

    o6.ns (count=128):
      name      uri                                    scope    version  pub_date    index
      ns0       http://opcfoundation.org/UA/           ::global 1.05.06              0
      amb       http://opcfoundation.org/UA/AMB/       ::global 1.01.1               ...
      ...

---

## Process wide namespace indices

The indices in the last column are valid process wide. Different clients and
servers in the same process therefore use the same canonical index for a given
registry entry. Index 1 remains reserved for the application namespace;
packaged namespaces receive indices as they are registered.

The same object provides metadata and declaration lookup:

```python
di_namespace = o6.ns.di
same_namespace = o6.ns[di_namespace.index]
device_set = o6.ns["ns=di;i=5001"]
```

Shortnames are accessed as attributes. Numeric indices return the same
namespace module. NodeId strings and `NodeId` objects return generated
declarations; use `filter()` for URI, scope, or version queries.

---

## Shortnames

very table entry has a **name** or **shortname**. This name uniquely identifies a namespace at a specific **URI**, **scope**, and **version**.

---

## URI identity

The URI of a OPC UA nodeset specification should be uniquely identifying it. However in practice we are often required to have specific versions of a companion spec to deal with legacy systems. Even though the version has to be specified in a nodeset, the URI doesn't change with version updates.

    o6.ns (count=129):
      name               uri                                                         scope    version  pub_date    index
      ns0                http://opcfoundation.org/UA/                                ::global 1.05.06              0
      di                 http://opcfoundation.org/UA/DI/                             ::global 1.05.0               ...
      ...
      di_1040            http://opcfoundation.org/UA/DI/                             ::global 1.04.0               51

In this case `di` is registered in two different versions. Note that the 'second' `di` has to use a different shortname and will be assined a unique global index.

---

## Scope

> **Note** that **scope** is a niche usecase for applications, where multiple clients and/or servers have to interact in the same process. You may skip this part.

A server's namespace 1 is automatically mapped once a client connects. Since this namespace is only relevant to the specific client it's scope is the actual endpoint of the server.

Once any nodeset is loaded into the address space of a server, it may also be modified by it. To address this, the **scope** poses as an indicator of where a namespace is valid. As a rule of thumb `::global` namespace should be treated as immutable, meaning that no objects, datatypes, references, etc. are injected into this namespace by the server. This is, however, not enforced and a client may still source the `::global` namespace `di` and connect to a server that modifies it's own `di` namespace after loading.

    o6.ns (count=130):
      name               uri                                                         scope                              version     pub_date    index
      ns0                http://opcfoundation.org/UA/                                ::global                           1.05.06                 0
      di                 http://opcfoundation.org/UA/DI/                             ::global                           1.05.0                  ...
      ...
      client1_ns1        urn:o6-python:testserver:enhanced                           opc.tcp://my_server_endpoint:4840                          51

---

## Automatic Namespace Translation

With this **o6\Python** doesn't need explicit management of namespace indices. Namepsaces can be identified by their human-readable shortname, which makes creating `NodeId`s extremely simple and easy to understand:

```python
nodeId = o6.NodeId("ns=di;i=5001")
browseName = o6.QualifiedName("ns=di;DeviceSet")
```

On a client the can map this to the global namespace index for `di` and map it to the corresponding local index to which this particular client is connected. The exchange of the needed information for this mapping happens transparently immediately after the client has connected.

---

## Packaged Companion specs

**o6\Python** comes with prepacked companion specs sourced from the offical [UA-Nodeset git](https://github.com/OPCFoundation/UA-Nodeset). All entries below are available out of the box by using `o6.ns.<shortname>`.

| Shortname | URI | Version |
|---|---|---|
| `adi` | `http://opcfoundation.org/UA/ADI/` | 1.01 |
| `amb` | `http://opcfoundation.org/UA/AMB/` | 1.01.1 |
| `aml` | `http://opcfoundation.org/UA/AML/` | 1.00 |
| `auto_id` | `http://opcfoundation.org/UA/AutoID/` | 1.01 |
| `bacnet` | `http://opcfoundation.org/UA/BACnet_V2/` | 2.00.1 |
| `cas` | `http://opcfoundation.org/UA/CAS/` | 1.00.1 |
| `cnc` | `http://opcfoundation.org/UA/CNC` | 1.0.0 |
| `commercial_kitchen` | `http://opcfoundation.org/UA/CommercialKitchenEquipment/` | 1.0 |
| `cranes_hoists` | `http://opcfoundation.org/UA/CranesHoists/` | 1.00 |
| `csp_plus` | `http://opcfoundation.org/UA/CSPPlusForMachine/` | 1.00 |
| `cutting_tool` | `http://opcfoundation.org/UA/CuttingTool/` | 1.0.0 |
| `dexpi` | `http://opcfoundation.org/UA/DEXPI/` | 1.0.0 |
| `di` | `http://opcfoundation.org/UA/DI/` | 1.05.0 |
| `ecm` | `http://opcfoundation.org/UA/ECM/` | 1.0.0 |
| `fdi` | `http://fdi-cooperation.com/OPCUA/FDI5/` | 1.1 |
| `fdt` | `http://opcfoundation.org/UA/FDT/` | 1.01.00 |
| `gds` | `http://opcfoundation.org/UA/GDS/` | 1.05.06 |
| `gms` | `http://opcfoundation.org/UA/GMS/` | 1.0.0 |
| `gpos` | `http://opcfoundation.org/UA/GPOS/` | 1.0.0 |
| `i4aas` | `http://opcfoundation.org/UA/I4AAS/` | 5.0.0 |
| `ia` | `http://opcfoundation.org/UA/IA/` | 1.01.4 |
| `ijt` | `http://opcfoundation.org/UA/IJT/Base/` | 1.01.0 |
| `io_link` | `http://opcfoundation.org/UA/IOLink/` | 1.00.1 |
| `iredes` | `http://opcfoundation.org/UA/Mining/ExternalStandards/IREDES` | 1.0.0 |
| `isa95` | `http://www.OPCFoundation.org/UA/2013/01/ISA95` | 1.00 |
| `isa95_jobcontrol` | `http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/` | 2.0.0 |
| `lads` | `http://opcfoundation.org/UA/LADS/` | 1.0.0 |
| `laser_systems` | `http://opcfoundation.org/UA/LaserSystems/` | 1.0.0 |
| `machine_tool` | `http://opcfoundation.org/UA/MachineTool/` | 1.02.0 |
| `machine_vision` | `http://opcfoundation.org/UA/MachineVision` | 1.0.0 |
| `machinery` | `http://opcfoundation.org/UA/Machinery/` | 1.04.1 |
| `mdis` | `http://opcfoundation.org/UA/MDIS` | 1.3 |
| `metal_forming` | `http://opcfoundation.org/UA/MetalForming/` | 1.0.0 |
| `mining` | `http://opcfoundation.org/UA/Mining/General/` | 1.01.0 |
| `mt_connect` | `http://opcfoundation.org/UA/MTConnect/v2/` | 2.00.01 |
| `ns0` | `http://opcfoundation.org/UA/` | 1.05.06 |
| `onboarding` | `http://opcfoundation.org/UA/Onboarding/` | 1.05.04 |
| `open_scs` | `http://opcfoundation.org/UA/OPENSCS-SER/` | 1.00 |
| `pack_ml` | `http://opcfoundation.org/UA/PackML/` | 1.01 |
| `padim` | `http://opcfoundation.org/UA/PADIM/` | 1.02.0 |
| `paefs` | `http://opcfoundation.org/UA/PAEFS/` | 1.0.1 |
| `plastics_rubber` | `http://opcfoundation.org/UA/PlasticsRubber/GeneralTypes/` | 1.02 |
| `plcopen` | `http://PLCopen.org/OpcUa/IEC61131-3/` | 1.02 |
| `pndrv` | `http://opcfoundation.org/UA/PDRV/` | 1.0.0 |
| `pnem` | `http://opcfoundation.org/UA/PNEM/` | 1.0.0 |
| `pnenc` | `http://opcfoundation.org/UA/PNENC/` | 1.0.0 |
| `pngsdgm` | `http://opcfoundation.org/UA/PNGSDGM/` | 1.0.0 |
| `pnrio` | `http://opcfoundation.org/UA/PNRIO/` | 1.00.1 |
| `powerlink` | `http://opcfoundation.org/UA/POWERLINK/` | 1.0.0 |
| `powertrain` | `http://opcfoundation.org/UA/Powertrain/` | 1.0.0 |
| `profinet` | `http://opcfoundation.org/UA/PROFINET/` | 1.0.1 |
| `pumps` | `http://opcfoundation.org/UA/Pumps/` | 1.0.0 |
| `robotics` | `http://opcfoundation.org/UA/Robotics/` | 1.02 |
| `rsl` | `http://opcfoundation.org/UA/RSL/` | 1.00.1 |
| `safety` | `http://opcfoundation.org/UA/Safety` | 1.05.04 |
| `scales` | `http://opcfoundation.org/UA/Scales/V2/` | 2.00 |
| `scheduler` | `http://opcfoundation.org/UA/Scheduler/` | 1.05.02 |
| `sercos` | `http://sercos.org/UA/` | 1.00 |
| `shotblasting` | `http://opcfoundation.org/UA/SurfaceTechnology/ShotBlasting/` | 1.0.0 |
| `surface_technology` | `http://opcfoundation.org/UA/SurfaceTechnology/Plasma/` | 1.0.0 |
| `tmc` | `http://opcfoundation.org/UA/TMC/v2/` | 2.00.1 |
| `ttd` | `http://opcfoundation.org/UA/TTD/` | 1.0.0 |
| `uafx` | `http://opcfoundation.org/UA/FX/AC/` | 1.00.03 |
| `weihenstephan` | `http://opcfoundation.org/UA/Weihenstephan/` | 1.00.0 |
| `wire_harness` | `http://opcfoundation.org/UA/WireHarness/` | 1.0.0 |
| `wmtp` | `http://opcfoundation.org/UA/WMTP/` | 1.0.0 |
| `woodworking` | `http://opcfoundation.org/UA/Woodworking/` | 1.02.0 |
| `wot` | `http://opcfoundation.org/UA/WoT-Con/` | 1.02.0 |

---

## See also

- The OPC UA spec's normative treatment of namespaces and URIs:
  [Part 3, §4.2 — URIs](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.2)
  and [Part 3, §4.4 — Node Model](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.4).
- How a server publishes its URI ↔ index table to clients, and where `ns=1` (the local Server) is reserved:
  [Part 5, §8.5 — Server Array and Namespace Array](https://reference.opcfoundation.org/Core/Part5/v105/docs/8.5)
  and [Part 5, §6.3.1 — ServerType](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1).
- The conceptual overview of namespaces, including `ns0` / `ns1` and the relationship to nodesets:
  [Namespace](../../opcua-fundamentals/namespace.md) and
  [Nodeset Files & Companion Specs](../../opcua-fundamentals/nodesets-and-companion-specs.md).
- How a namespace enters the global `o6.ns` registry, reaches a server's address space, and exposes its Python types:
  [Loading & Using Nodesets](loading-and-using-nodesets.md).
- How a `*.NodeSet2.xml` becomes an importable namespace package:
  [Compiling Nodesets](compiling-nodesets.md).
- The o6-side `NodeId` / `ExpandedNodeId` / `QualifiedName` types that carry the index (or shortname / URI) in practice:
  [Address & Identity Types](../builtin/address-types.md).
