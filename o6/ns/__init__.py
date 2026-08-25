# Copyright 2026 (c) o6 Automation GmbH
"""The process-wide OPC UA namespace registry and generated namespace package."""

import o6

import importlib.util
import os
import sys
from types import ModuleType
from typing import Any, cast


from ._generated_nodesets import _GLOBAL_NAMESPACES

_PACKAGED_SHORTNAMES = frozenset(entry[0] for entry in _GLOBAL_NAMESPACES)

_REGISTER_NAMESPACE = o6._o6._register_namespace
_SET_NAMESPACE_RESOLVER = o6._o6._set_namespace_resolver
_NODEID_PREFIXES = ("i=", "s=", "g=", "b=", "ns=", "nsu=")
_GLOBAL_SCOPE = "::global"


def _register_namespace(
    shortname: str,
    uri: str,
    scope: str,
    *,
    version: str | None = None,
    publication_date: str | None = None,
) -> "NamespaceModule":
    version = version or ""
    publication_date = publication_date or ""
    existing_index = _INDEX_BY_SHORTNAME.get(shortname)
    if existing_index is not None:
        existing = _NAMESPACE_TABLE[existing_index]
        identity = (uri, scope, version)
        if (existing.uri, existing.scope, existing.version) != identity:
            raise ValueError(f"shortname {shortname!r} is already registered for " f"{(existing.uri, existing.scope, existing.version)!r}")
        if publication_date and not existing.publicationDate:
            existing.publicationDate = publication_date
        return existing

    index = len(_NAMESPACE_TABLE)
    module_name = f"o6.ns.{shortname}"
    module = NamespaceModule(module_name)
    module.__dict__.update(
        version=version,
        shortname=shortname,
        uri=uri,
        publicationDate=publication_date,
        scope=scope,
        index=index,
        __package__="o6.ns",
        __O6_NODEIDS__={},
        __O6_INSTANCES__=[],
        __O6_NEXT_NODEID__=6000,
    )
    if shortname in _PACKAGED_SHORTNAMES:
        module.__dict__["_o6_source"] = os.path.join(os.path.dirname(__file__), shortname, "__init__.py")
        module.__dict__["_o6_loaded"] = False
    else:
        module.__dict__["_o6_loaded"] = True

    _INDEX_BY_SHORTNAME[shortname] = index
    _NAMESPACE_TABLE.append(module)
    if index == 0:
        _NAMESPACE_TABLE.append(None)  # ns=1 is application-local
    sys.modules[module_name] = module
    setattr(sys.modules[__name__], shortname, module)
    _REGISTER_NAMESPACE(shortname, index, module)
    return module


def _remove_instance_root(value: Any) -> None:
    """Remove a declaration once another declaration owns its construction."""
    from o6._declarations import _instance_declaration

    try:
        declaration = _instance_declaration(value)
    except TypeError:
        declaration = value
    for namespace in _NAMESPACE_TABLE:
        if not isinstance(namespace, NamespaceModule):
            continue
        instances = namespace.__dict__.get("__O6_INSTANCES__", ())
        for index, existing in enumerate(instances):
            if existing is declaration:
                del instances[index]
                return


def _register_declaration(value: Any, *, instance: bool = False) -> Any:
    """Register a completed declaration in its calling namespace module."""
    import inspect
    from o6._declarations import _declaration_nodeid, _instance_declaration

    registered = _instance_declaration(value) if instance else value

    frame = inspect.currentframe()
    try:
        frame = frame.f_back if frame is not None else None
        while frame is not None:
            globals_ = frame.f_globals
            if frame.f_code.co_name == "<module>" and "__NAMESPACES__" in globals_:
                host = sys.modules.get(globals_.get("__name__", ""))
                nodeid = _declaration_nodeid(registered)
                if instance and isinstance(host, NamespaceModule):
                    if registered.parent is not None or nodeid is not None:
                        instances = host.__dict__.setdefault("__O6_INSTANCES__", [])
                        if not any(existing is registered for existing in instances):
                            instances.append(registered)
                if nodeid is None:
                    return value
                namespace_module = nodeid.ns
                if isinstance(namespace_module, int):
                    namespace_module = _module_for_index(namespace_module)
                if not isinstance(namespace_module, NamespaceModule):
                    return value
                declarations = namespace_module.__dict__.setdefault("__O6_NODEIDS__", {})
                key = str(nodeid)
                existing = declarations.get(key)
                if existing is not None and existing is not registered:
                    # Instantiating a type may materialize a detached mandatory
                    # child carrying the declaration's NodeId. Keep the first
                    # explicit declaration in this module authoritative.
                    return value
                declarations[key] = registered
                return value
            frame = frame.f_back
    finally:
        del frame
    return value


def _next_nodeid(shortname: str) -> str:
    """Allocate one import-time NodeId in a registered namespace."""
    namespace = _module_for_shortname(shortname)
    next_id = int(namespace.__dict__.get("__O6_NEXT_NODEID__", 6000)) + 1
    namespace.__dict__["__O6_NEXT_NODEID__"] = next_id
    return f"ns={shortname};i={next_id}"


class NamespaceModule(ModuleType):
    """A generated OPC UA namespace exposed as a normal Python module.

    Reached by attribute on `o6.ns`, for example `o6.ns.di`, and returned by the
    `ns` property of a [`NodeId`][o6.NodeId],
    [`ExpandedNodeId`][o6.ExpandedNodeId], or
    [`QualifiedName`][o6.QualifiedName]. Namespace metadata sits directly on the
    module, and the generated child modules `datatypes`, `objtypes`, `vartypes`,
    `reftypes`, and `instances` hold the declarations.

    Packaged namespaces load lazily: the module exists as soon as it is
    registered, and its generated source is imported on first attribute access.

    See [Namespace Mapping in o6\\Python](../manual/sdk-fundamentals/namespace/namespace-mapping-in-o6.md).
    """

    version: str
    """Model version string, e.g. `"1.05.0"`."""

    shortname: str
    """Short name the namespace is registered under, e.g. `"di"`."""

    uri: str
    """Namespace URI as published by the model."""

    publicationDate: str
    """Publication date declared by the model, empty when unknown."""

    scope: str
    """Registration scope, which separates identically named namespaces."""

    index: int
    """Namespace index in the process-wide namespace table."""

    def _prepare(self) -> None:
        """Give the module its package dunders without running its body.

        Answering `__path__` and `__spec__` has to be separable from executing the
        body, because the import machinery reads them *while* importing a
        submodule: `_find_and_load_unlocked` re-checks `sys.modules` for the
        submodule before it reads the parent's `__path__`, so a body that imports
        the submodule itself — which every generated package does — would leave the
        importer to load and execute it a second time, registering every DataType
        in it twice.
        """
        state = self.__dict__
        if "__path__" in state:
            return
        source = state.get("_o6_source")
        if source is None:
            return
        package_dir = os.path.dirname(source)
        spec = importlib.util.spec_from_file_location(self.__name__, source, submodule_search_locations=[package_dir])
        if spec is None or spec.loader is None:
            raise ImportError(f"cannot load namespace package {self.__name__!r}")
        state.update(
            __file__=source,
            __loader__=spec.loader,
            __package__=self.__name__,
            __path__=[package_dir],
            __spec__=spec,
        )

    def _load(self) -> None:
        state = self.__dict__
        if state.get("_o6_loaded", True) or state.get("_o6_loading", False):
            return
        if state.get("_o6_source") is None:
            return

        self._prepare()
        state["_o6_loading"] = True
        loader = state["__loader__"]
        try:
            loader.exec_module(self)
        except Exception:
            state.pop("_o6_loading", None)
            raise
        state["_o6_loaded"] = True
        state.pop("_o6_loading", None)

    def __getattr__(self, name: str) -> Any:
        if name in _PACKAGE_DUNDERS:
            self._prepare()
        else:
            self._load()
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(f"module {self.__name__!r} has no attribute {name!r}") from None

    def __repr__(self) -> str:
        if "shortname" not in self.__dict__:
            return ModuleType.__repr__(self)
        return f"<o6 namespace {self.shortname!r} version={self.version!r} uri={self.uri!r}>"


#: What the import machinery reads on a package before it can load a submodule.
#: These are answered by `NamespaceModule._prepare`, which does not run the
#: package body — see the note there.
_PACKAGE_DUNDERS = frozenset({"__path__", "__spec__", "__loader__", "__file__"})

_INDEX_BY_SHORTNAME: dict[str, int] = {}
_NAMESPACE_TABLE: list[NamespaceModule | None] = []


def _adopt_namespace_module(module: ModuleType, namespace: NamespaceModule) -> NamespaceModule:
    """Make an existing caller module the canonical namespace module."""
    if module is namespace:
        return namespace
    if not isinstance(module, NamespaceModule):
        module.__class__ = NamespaceModule
    module.__dict__.update(
        version=namespace.version,
        shortname=namespace.shortname,
        uri=namespace.uri,
        publicationDate=namespace.publicationDate,
        scope=namespace.scope,
        index=namespace.index,
        _o6_loaded=True,
    )
    canonical = cast(NamespaceModule, module)
    canonical.__dict__.setdefault("__O6_NODEIDS__", {})
    canonical.__dict__.setdefault("__O6_INSTANCES__", [])
    canonical.__dict__.setdefault("__O6_NEXT_NODEID__", 6000)
    _NAMESPACE_TABLE[namespace.index] = canonical
    _REGISTER_NAMESPACE(namespace.shortname, namespace.index, canonical)
    setattr(sys.modules[__name__], namespace.shortname, canonical)
    sys.modules[f"o6.ns.{namespace.shortname}"] = canonical
    return canonical


def _module_for_shortname(shortname: str) -> NamespaceModule:
    index = _INDEX_BY_SHORTNAME.get(shortname)
    if index is None:
        raise KeyError(f"namespace shortname {shortname!r} is not registered")
    namespace = _NAMESPACE_TABLE[index]
    assert isinstance(namespace, NamespaceModule)
    return namespace


def _module_for_index(index: int) -> NamespaceModule | int:
    if index < 0 or index >= len(_NAMESPACE_TABLE):
        return index
    namespace = _NAMESPACE_TABLE[index]
    return namespace if namespace is not None else index


def _resolve_namespace_token(token: str) -> int:
    uri_end = len(token)
    for delimiter in ("@", "!"):
        position = token.find(delimiter)
        if position >= 0:
            uri_end = min(uri_end, position)
    uri = token[:uri_end]
    scope: str | None = None
    version: str | None = None
    remainder = token[uri_end:]
    while remainder:
        delimiter = remainder[0]
        remainder = remainder[1:]
        next_positions = [p for p in (remainder.find("@"), remainder.find("!")) if p >= 0]
        end = min(next_positions) if next_positions else len(remainder)
        value, remainder = remainder[:end], remainder[end:]
        if delimiter == "@":
            scope = value
        elif delimiter == "!":
            version = value

    matches = [
        index
        for index, entry in enumerate(_NAMESPACE_TABLE)
        if entry is not None
        if entry.uri == uri and (scope is None or entry.scope == scope) and (version is None or entry.version == version)
    ]
    if len(matches) != 1:
        raise KeyError(f"namespace token {token!r} is not uniquely registered")
    return matches[0]


def _initialize_namespace(
    module_name: str,
    *,
    shortname: str,
    uri: str,
    version: str = "1.0",
    publication_date: str = "",
) -> NamespaceModule:
    """Register and explicitly initialize an imported namespace module."""
    module = sys.modules[module_name]
    namespace_module = _register_namespace(
        shortname=shortname,
        uri=uri,
        scope=_GLOBAL_SCOPE,
        version=version,
        publication_date=publication_date,
    )
    namespace_module = _adopt_namespace_module(module, namespace_module)
    module.__dict__.setdefault("__NAMESPACES__", set()).add(namespace_module)
    return namespace_module


class _NamespacePackage(ModuleType):
    """The process-wide namespace registry and generated namespace package.

    Namespace modules are addressed by attribute, for example `o6.ns.di`.
    Numeric keys return namespace modules; NodeId keys return generated
    declarations.
    """

    def __getattr__(self, name: str) -> NamespaceModule:
        if name in _INDEX_BY_SHORTNAME:
            return _module_for_shortname(name)
        raise AttributeError(f"module {self.__name__!r} has no attribute {name!r}")

    def __dir__(self) -> list[str]:
        return sorted(set(__all__) | set(_INDEX_BY_SHORTNAME))

    def register(
        self,
        shortname: str,
        uri: str,
        *,
        scope: str | None = None,
        version: str | None = None,
        publicationDate: str | None = None,
    ) -> NamespaceModule:
        """Register a namespace and return its namespace module.

        Registering the same shortname again with identical metadata returns the
        existing module, so this is idempotent. A missing publication date is
        filled in on a repeat call.

        Args:
            shortname: Short name to register the namespace under, and the
                attribute it becomes on `o6.ns`.
            uri: Namespace URI as published by the model.
            scope: Registration scope, to separate identically named namespaces.
                Defaults to the global scope.
            version: Model version string.
            publicationDate: Publication date declared by the model.

        Returns:
            The [`NamespaceModule`][o6.ns.NamespaceModule] for this namespace.

        Raises:
            ValueError: The shortname is already registered for a different URI,
                scope, or version.
        """
        return _register_namespace(
            shortname,
            uri,
            _GLOBAL_SCOPE if scope is None else scope,
            version=version,
            publication_date=publicationDate,
        )

    def filter(
        self,
        *,
        uri: str | None = None,
        scope: str | None = None,
        version: str | None = None,
    ) -> list[NamespaceModule]:
        """Return namespace modules matching the supplied metadata.

        Every argument is optional and combines as an AND. With no arguments, this
        returns every registered namespace. Use it to find which release of a URI
        is loaded when several versions of one model can coexist.

        Args:
            uri: Match this namespace URI exactly.
            scope: Match this registration scope.
            version: Match this model version.

        Returns:
            The matching [`NamespaceModule`][o6.ns.NamespaceModule] objects, in
            namespace-index order.
        """
        return [
            _module_for_shortname(entry.shortname)
            for entry in _NAMESPACE_TABLE
            if entry is not None
            if (uri is None or entry.uri == uri) and (scope is None or entry.scope == scope) and (version is None or entry.version == version)
        ]

    def __getitem__(self, key: object) -> Any:
        if isinstance(key, int):
            namespace = _module_for_index(key)
            if isinstance(namespace, int):
                raise KeyError(f"namespace index {key} is not registered")
            return namespace
        if isinstance(key, str) and not key.startswith(_NODEID_PREFIXES):
            raise TypeError(f"use o6.ns.{key} for namespace shortname access; brackets are for " "namespace indices and NodeIds")
        if not isinstance(key, (str, o6.NodeId)):
            raise TypeError("o6.ns key must be an index or NodeId")

        nodeid = o6.NodeId(key)
        namespace = nodeid.ns
        if isinstance(namespace, int):
            namespace = _module_for_index(namespace)
        if not isinstance(namespace, NamespaceModule):
            raise KeyError(f"namespace index {namespace} is not registered")
        namespace._load()
        declarations = namespace.__dict__.get("__O6_NODEIDS__", {})
        try:
            return declarations[str(nodeid)]
        except KeyError:
            raise KeyError(f"namespace {namespace.shortname!r} has no declaration for NodeId {nodeid!s}") from None

    def __contains__(self, key: object) -> bool:
        if isinstance(key, o6.NodeId) or (isinstance(key, str) and key.startswith(_NODEID_PREFIXES)):
            try:
                self[key]
            except (KeyError, TypeError, ValueError):
                return False
            return True
        if isinstance(key, str):
            return key in _INDEX_BY_SHORTNAME
        try:
            self[key]
        except (KeyError, TypeError, ValueError):
            return False
        return True

    def __len__(self) -> int:
        return len(_INDEX_BY_SHORTNAME)

    def __iter__(self):
        return iter(_INDEX_BY_SHORTNAME)

    def __repr__(self) -> str:
        entries = [entry for entry in _NAMESPACE_TABLE if entry is not None]
        widths = {
            "name": max(len("name"), *(len(entry.shortname) for entry in entries)),
            "uri": max(len("uri"), *(len(entry.uri) for entry in entries)),
            "scope": max(len("scope"), *(len(entry.scope) for entry in entries)),
            "version": max(len("version"), *(len(entry.version) for entry in entries)),
            "pub_date": max(len("pub_date"), *(len(entry.publicationDate) for entry in entries)),
        }

        def row(name: str, uri: str, scope: str, version: str, pub_date: str, index: str) -> str:
            return f"  {name:<{widths['name']}} {uri:<{widths['uri']}} " f"{scope:<{widths['scope']}} {version:<{widths['version']}} " f"{pub_date:<{widths['pub_date']}} {index}"

        lines = [f"o6.ns (count={len(self)}):"]
        lines.append(row("name", "uri", "scope", "version", "pub_date", "index"))
        lines.extend(
            row(
                entry.shortname,
                entry.uri,
                entry.scope,
                entry.version,
                entry.publicationDate,
                str(entry.index),
            )
            for entry in entries
        )
        return "\n".join(lines)


def namespace(shortname: str, uri: str, version: str = "1.0", publicationDate: str = "") -> None:
    """Register a namespace in the global namespace table.

    Called at the top of a namespace module, before the decorated classes below
    it, so that the declarations know which namespace they belong to:

    ```python
    o6.ns.namespace("plant", uri="http://example.org/Plant/", version="1.0")
    ```

    Unlike [`o6.ns.register`][o6.ns.register] this returns nothing, and when the
    calling module is itself the namespace module it adopts that module rather
    than creating a second one.

    Args:
        shortname: Short name to register the namespace under, and the attribute
            it becomes on `o6.ns`.
        uri: Namespace URI published by this model.
        version: Model version string.
        publicationDate: Publication date declared by the model.

    Raises:
        ValueError: The shortname is already registered for a different URI,
            scope, or version.

    See [Writing a Nodeset in Python](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#the-shape-of-a-namespace-module).
    """
    namespace_module = _register_namespace(
        shortname=shortname,
        uri=uri,
        scope=_GLOBAL_SCOPE,
        version=version,
        publication_date=publicationDate,
    )
    # Inject the shortname into the caller module's __NAMESPACE__ list for later retrieval by o6.server.Server.ns.append().
    import inspect

    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back if current_frame is not None else None
    module = inspect.getmodule(caller_frame)

    if module is not None:
        ns = module.__dict__.setdefault("__NAMESPACES__", set())
        configured_shortname = module.__dict__.get("shortname")
        if configured_shortname in (None, shortname):
            namespace_module = _adopt_namespace_module(module, namespace_module)
        else:
            namespace_module = _module_for_shortname(shortname)
        ns.add(namespace_module)


# Pin the shipped companion specs to their deterministic global indices as soon
# as the ``o6.ns`` package is imported.  Every ``import o6.ns.<name>`` runs
# this package ``__init__`` first, so any companion module's own
# ``namespace()`` call dedups against these entries rather than defining a new
# (import-order-dependent) index.
_SET_NAMESPACE_RESOLVER(_resolve_namespace_token)
for _shortname, _uri, _version in _GLOBAL_NAMESPACES:
    _register_namespace(shortname=_shortname, uri=_uri, scope=_GLOBAL_SCOPE, version=_version)
del _shortname, _uri, _version

sys.modules[__name__].__class__ = _NamespacePackage

__all__ = [
    "NamespaceModule",
    "filter",
    "namespace",
    "register",
]
