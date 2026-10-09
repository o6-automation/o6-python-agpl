# open62541-based NodeSet compiler

This compiler generates the packaged namespaces in `o6/ns` from the registry
and verifies their runtime behavior with `generation_matrix`.

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
in the process-wide ``o6.ns`` table. The selected release must be published
before another module with the same URI.

The `irdi_v1_00` compatibility package supplements its historical dictionary
with missing entries from the current `deps/UA-Nodeset/PADIM` dictionary.
Metal Forming needs its historical entries and also depends on current PADIM.
Overlapping entries retain the historical definitions and metadata; the
canonical `irdi` package remains the current upstream release.

The command-line compiler can override this preference with a repeatable
``--force-version MODEL=VERSION`` option. ``MODEL`` may be a canonical
shortname (for example ``irdi``) or a full Model URI. Forced releases must
still provide every referenced endpoint; an incompatible override fails rather
than generating a broken namespace.

The Python backend rejects unsupported node features rather than producing an
incomplete module. It emits data types, reference types, variable types, object
types, objects, variables, methods, and views, including declared children,
interfaces, references, argument metadata, and values. The generated matrix
records which registered models pass the complete verification pipeline.

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
construct in a model is reported as `n/a`; otherwise a deterministic first
representative is exercised. Instance checks include registered declarations,
even when generated code does not assign them to module attributes. Value
checks compare against the declared value with runtime numeric coercion before
checking binary serialization. Failed stages are recorded as explicit fail-closed
limitations in ``GENERATION_MATRIX.md``.

For changes to verification code, reuse existing packages and check selected
models without generating source:

```shell
python -m tools.nodeset_compiler.generation_matrix --reuse-generated \
  --out-dir o6/ns --only di bacnet cnc --matrix /tmp/selected-nodesets.md
```

`--only` requires a separate report path so that a partial run cannot replace
the full matrix. A complete `--reuse-generated` run also includes required
historical compatibility models. Reused source must be up to date with the
NodeSet XML and generator; this mode does not establish regeneration freshness.

Check repository coverage independently of generation or server startup:

```shell
python -m tools.nodeset_compiler.inventory
```

Every NodeSet XML file in `deps/UA-Nodeset` must be a registered source, a
compatibility dependency, or an explicit exclusion in `inventory.py`.
Discovery uses the XML root element, including files named `NodeSet.xml`.
Exclusions cover example/demo/test models, historical alternatives, and the
alternate standard-namespace file. Unclassified models, stale exclusions, and registered models
that are also excluded fail the check. Matrix runs check this inventory first.

All 136 primary registry targets source their XML from `deps/UA-Nodeset`.
The inventory accounts for 150 NodeSet files: 136 primary sources, one
additional historical compatibility source, and 13 explicit exclusions.
Two older IRDI inputs live in `nodesets/compat/irdi`, with upstream commit and
checksum provenance beside each XML file. Two compatibility packages are
required by the current registry, making 138 matrix rows in total.
