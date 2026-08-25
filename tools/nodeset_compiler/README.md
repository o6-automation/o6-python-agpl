# open62541-based NodeSet compiler

This is a parallel implementation. It does not import, modify, or replace the
current `tools/nodeset_compiler` pipeline.

The frontend delegates XML parsing, dependency merging, alias and namespace
resolution, datatype parsing, inverse-reference completion, parent resolution,
and node sorting to the vendored open62541 NodeSet compiler.

Descriptions are deterministic inputs. Ordinary XML ``Description`` text is
emitted unchanged. A URL-valued ``Description`` is replaced only from the
checked-in ``tools/nodeset_compiler/link_cache.json``; a cache miss fails
generation. Network access is available solely through the explicit
``--refresh-description-cache`` operation, which atomically updates the sorted
cache and does not generate source in the same invocation. ``Documentation``
URLs and NodeIds are never added to emitted descriptions.

URL-only descriptions in dictionary NodeSets are external entry identifiers
rather than prose. They are deliberately omitted and do not require cache
entries. Ordinary text descriptions in dictionary and supplementary inputs are
retained.

References are canonicalized as forward ``(subject, verb, object)`` triples and
deduplicated against the inverse references completed by the frontend. Every
reference with at least one generated endpoint must be represented either by a
node declaration/decorator or by the final ``o6.reference`` pass; generation
fails if that accounting is incomplete. Remote ``ExpandedNodeId`` endpoints are
preserved outside the open62541 graph and emitted explicitly, since the
vendored frontend accepts only local ``NodeId`` endpoints.

Generated source is ordered by namespace URI and NodeId, not XML container,
namespace-index, dependency-input, alias-map, or Python set/dict iteration
order. Enum members are ordered by numeric value and name; structure member
order remains untouched because it defines the binary layout.

Each loadable namespace module is accompanied by a generated ``.pyi`` static
API projection. The stub omits decorators and information-model construction,
but retains public declarations and description docstrings. Native datatype
members use properties so reads keep their exact OPC UA type while writes expose
the conversions implemented by the C boundary. All Python and NumPy integer
types are accepted for integer fields; the runtime performs signedness and width
checks and raises ``OverflowError`` when the value does not fit.

The current UA-Nodeset checkout supplies canonical modules such as ``irdi``.
Only these canonical models belong to the default generation registry.
Historical compatibility inputs live in a separate catalog and receive stable
versioned shortnames such as ``irdi_v1_00``. They are considered only when a
canonical model's declared dependency cannot use the current release; merely
being available never makes an older release a default generation target.
Dependency selection first tries the canonical current release and uses it when
it contains every referenced endpoint. Only if that fails does it try the
version declared by the dependent model. Publication dates do not participate
in selection. A single generated AddressSpace contains at most one
release of each namespace URI, while the resulting Python modules can coexist
in the process-wide ``o6.ns`` table.

The command-line compiler can override this preference with a repeatable
``--force-version MODEL=VERSION`` option. ``MODEL`` may be a canonical
shortname (for example ``irdi``) or a full Model URI. Forced releases must
still provide every referenced endpoint; an incompatible override fails rather
than generating a broken namespace.

The Python backend is intentionally strict and is being implemented one
NodeClass at a time. Any unsupported generated node or supported node attribute
fails compilation instead of producing an incomplete module. The existing
generator remains authoritative until representative companion specifications
produce semantically equivalent, loadable modules.

Current backend coverage:

- DataType: structures, enums, inheritance, fields, optional/array members, and
  Default Binary encoding ids.
- ReferenceType: inheritance, inverse names, symmetry, abstractness, and common
  node metadata.
- VariableType: inheritance, DataType, ValueRank, ArrayDimensions,
  abstractness, and common node metadata. Default values are rejected pending
  the value-encoding slice.
- Variable: TypeDefinition, DataType, ValueRank, ArrayDimensions, modelling
  rules, access level, metadata, and external hierarchical placement. Values
  are decoded by open62541 using temporary o6 datatype registrations, then a
  datatype-aware renderer emits ordinary Python constructors recursively. The
  backend contains no XML-tag-specific value construction. Nested variables
  are emitted detached for their owning Object/ObjectType slice to link later.
  Distinct UserAccessLevel, MinimumSamplingInterval, and Historizing fail
  explicitly because the instance API cannot yet represent them faithfully.
- ObjectType: inheritance, abstractness, and common node metadata. Interfaces
  and declarations will be added after the instance NodeClasses can be emitted.

Object, Method, and View are not supported yet.

Run the inventory backend:

```shell
python -m tools.nodeset_compiler.backend_python model.xml \
  --existing ns0=Opc.Ua.NodeSet2.xml --out model_inventory.py
```

Generate a supported o6 type module by also supplying its namespace shortname:

```shell
python -m tools.nodeset_compiler.backend_python model.xml \
  --existing ns0=Opc.Ua.NodeSet2.xml --shortname model --out model.py
```

Compile every enabled companion specification through the same registry used by
the original generator:

```shell
python -m tools.nodeset_compiler.compile_all --keep-going
```

The batch compiler reads ``RequiredModel`` metadata, resolves the transitive
dependency closure, and generates specifications in a stable topological order.
Without ``--keep-going`` it stops after the first unsupported or failed model;
with it, every model is attempted and reported. Output is formatted at the
``o6/ns`` line length and is atomically replaced only when its contents change.

Run the complete parse-to-server verification and update the checked-in matrix:

```shell
python -m tools.nodeset_compiler.generation_matrix
```

Each specification is checked for parsing, generation, Python compilation,
dependency-complete isolated import, and loading into a fresh server. The live
address space is then checked for representative type instantiation, mandatory
child creation, forward and inverse browsing, method argument metadata, value
binary round-trips, and namespace identity round-trips. A check with no matching
construct in a model is vacuously successful; otherwise a deterministic first
representative is exercised. Failed stages are recorded as explicit fail-closed
limitations in ``GENERATION_MATRIX.md``.
