# BrowseName to Python Names

An OPC UA BrowseName can contain spaces, punctuation or a leading digit, or be empty. A Python identifier cannot. Every name you reach through `o6` (a generated class, a generated member, an attribute on a browsed node) is the BrowseName converted into a valid Python identifier.

!!! info "One spelling, whichever way you arrive"
    These rules apply equally to a name in a [generated package](../information-model-authoring/compiling-nodesets.md) and to an attribute on a node you browsed at runtime, so code written against one keeps working against the other.

---

## The rules

In order:

1. **Normalize**, NFKC — the same normalization Python applies to identifiers in source. `A²` becomes `A2`.
2. **Replace each run of invalid characters with one `_`.** `_` counts as one of them, so `Temperature_<No.>` gives `Temperature_No_`, not `Temperature__No__`.
3. **Drop a leading `_`**, so `<Placeholder>` gives `Placeholder_`. A leading `_` would read as private and be unreachable by dot access.
4. **Spell out a leading digit**, capitalizing what follows: `3DPosition` gives `ThreeDPosition`. Digits elsewhere are kept.
5. **Use `_` if nothing is left.**
6. **Append `_` to a Python keyword.** `Class` gives `class_`.

---

## Type names and member names

The rules end one of two ways. *Type names* — ObjectType, VariableType, ReferenceType, DataType, anything that becomes a `class` — keep the BrowseName's initial case. *Member names* — instances, properties, components, and the attributes of a browsed node — lowercase the first character.

```python
di.objtypes.DeviceType          # type name
di.instances.deviceSet          # member name
```

The keyword check runs after that lowercasing, which is why `None` gives the member `none` rather than `none_`.

---

## Examples

### Ordinary names

| BrowseName | Type name | Member name | Why |
|---|---|---|---|
| `SerialNumber` | `SerialNumber` | `serialNumber` | nothing to change |
| `EURange` | `EURange` | `eURange` | only the first character is lowercased |
| `Class` | `Class` | `class_` | Python keyword |
| `None` | `None_` | `none` | keyword check follows member casing |

### Separators

| BrowseName | Type name | Member name | Why |
|---|---|---|---|
| `A B` | `A_B` | `a_B` | one `_` per run |
| `My Variable` | `My_Variable` | `my_Variable` | space |
| `My-Variable` | `My_Variable` | `my_Variable` | hyphen — same spelling |
| `My_Variable` | `My_Variable` | `my_Variable` | underscore — same spelling |
| `A\x00B` | `A_B` | `a_B` | control characters count as invalid |
| `" Leading  spaces "` | `Leading_spaces_` | `leading_spaces_` | leading run dropped, trailing kept |
| `Temperature_<No.>` | `Temperature_No_` | `temperature_No_` | `_<` and `.>` are each one run |
| `http://example.org/UA/` | `http_example_org_UA_` | `http_example_org_UA_` | URI-shaped; both forms coincide |

### Leading digits and placeholders

| BrowseName | Type name | Member name | Why |
|---|---|---|---|
| `3DPosition` | `ThreeDPosition` | `threeDPosition` | leading digit spelled out |
| `123-Value` | `One23_Value` | `one23_Value` | only the leading digit is spelled out |
| `<GearIdentifier>` | `GearIdentifier_` | `gearIdentifier_` | leading `_` dropped, trailing kept |
| `<3DVector>` | `ThreeDVector_` | `threeDVector_` | bracket dropped before the digit rule |
| `""` | `_` | `_` | empty name |

### Unicode

| BrowseName | Type name | Member name | Why |
|---|---|---|---|
| `A²` | `A2` | `a2` | superscript folds to a digit |
| `ﬁle` | `file` | `file` | ligature folds; collides with plain `file` |
| `KValue` | `KValue` | `kValue` | Kelvin sign folds to an ASCII `K` |
| `ⅨValue` | `IXValue` | `iXValue` | roman numeral folds to `IX` |
| `½Share` | `One_2Share` | `one_2Share` | fraction folds to `1⁄2`; the slash is invalid |
| `Grösse` | `Grösse` | `grösse` | combining diaeresis composes |

!!! warning "Normalization can merge two names"
    `ﬁle` and `file` are one identifier to Python, as are any two BrowseNames differing only by normalization. They do not shadow each other — they are a [collision](#collisions).

---

## Collisions

Steps 2 and 3 are lossy, so distinct BrowseNames can land on one spelling: `My Variable`, `My-Variable` and `My_Variable` all give `my_Variable`.

In a generated package, the compiler appends `_2`, `_3` in node order, so every declaration keeps a distinct symbol. A `_2` in generated source is usually a literal part of the BrowseName, not a disambiguator, and you cannot tell which by reading it. Don't depend on a suffixed spelling.

At runtime there is no numbering: a browsed child is discovered, not declared, and any number would shift as siblings appear. Access to an ambiguous name raises instead:

```python
>>> node.my_Variable
AttributeError: ... ambiguous ...
```

---

## Reaching a name you cannot spell

The conversion never changes the information model. The BrowseName is stored unchanged and stays the authoritative identity. There are four ways to reach a node:

```python
client.objects.my_Variable()                 # the Python alias
getattr(client.objects, "My Variable")()     # the exact BrowseName
client.objects["/1:My Variable"][0]()        # a browse path, namespace index 1
client[o6.NodeId("ns=1;i=4711")]()           # by NodeId
```

An exact BrowseName match takes precedence. Otherwise, lookup matches BrowseNames and aliases case-insensitively. Use a NodeId when a name is ambiguous, empty or a placeholder. A declaration with no hierarchical parent may have no public name at all.

---

## Enumeration members

Enum and OptionSet members are constants and follow a different rule: the name is split on case boundaries, upper-cased and joined with `_`.

| Field name | Member |
|---|---|
| `Running` | `RUNNING` |
| `InProgress` | `IN_PROGRESS` |
| `HIGH_VOLTAGE` | `HIGH_VOLTAGE` |
| `Zone 0` | `ZONE_0` |
| `16BIT` | `_16_BIT` |

`16BIT` keeps its leading `_`, because spelling out only the first digit would give `ONE6_BIT`. Enum members are read from the generated class and never browsed, so the leading `_` does no harm.

---

## Related topics

| Topic | What it covers |
|---|---|
| [Navigation & Lookup](navigation.md) | Dotted navigation, `dir()`, and attribute precedence. |
| [Loading & Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md) | Importing and using generated namespace packages. |
| [Compiling Nodesets](../information-model-authoring/compiling-nodesets.md) | Generating a namespace package from nodeset XML. |
| [Namespace Mapping in o6\\Python](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md) | Looking up declarations by NodeId in the namespace registry. |
