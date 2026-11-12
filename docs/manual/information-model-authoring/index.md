# Information Model Authoring

Use this chapter to compile an existing information model, declare one in Python,
or implement the behavior of its types. Client developers can compile vendor
models to decode custom values; server developers can publish and instantiate
those same declarations.

Read [SDK Fundamentals](../sdk-fundamentals/index.md) first for values,
identifiers, namespace mapping, and using packaged models. Server publication
and behavior examples also assume the [Server](../server/index.md) chapter.

A *declaration* describes an OPC UA type or node. Publishing makes that
model available in a server; instantiating an ObjectType or VariableType creates
live nodes. An *implementation* supplies the application behavior of those nodes.

Start with compilation when XML already defines your model. For a model you own,
write a namespace module and declare its types in dependency order. Both routes
produce Python declarations used by the publication and implementation pages.

## Contents

| Topic | What it covers |
|---|---|
| [Compiling Nodesets](compiling-nodesets.md) | Generating Python packages from existing XML models and their dependencies. |
| [Writing a Namespace Module](namespace-modules.md) | Registering a handwritten namespace and choosing stable identities. |
| [Declaring ObjectTypes & VariableTypes](object-variable-types.md) | Reusable node hierarchies, children, inheritance, and interfaces. |
| [Declaring Custom DataTypes](datatypes.md) | Structures, enumerations, unions, and OptionSets. |
| [Declaring ReferenceTypes & Model Instances](references-and-instances.md) | Custom relationships and instances published with a model. |
| [Publishing & Instantiating Models](publishing.md) | Publishing declarations, seeding instance values, and selecting a server. |
| [Implementing Declared Types](implementing-types.md) | Application behavior for handwritten or compiled type declarations. |
| [Callback Binding & Overrides](callback-binding.md) | Target names, inheritance, precedence, and runtime overrides. |
