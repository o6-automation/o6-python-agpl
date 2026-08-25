# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Generate and verify every enabled companion specification."""

from __future__ import annotations

import argparse
import enum
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from typing import Any

from .compile_all import (
    CompileResult,
    Specification,
    _transitive_dependencies,
    _write_if_changed,
    compatibility_registry,
    compile_registry,
    dependency_order,
    registry,
)

_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_OUT = Path(tempfile.gettempdir()) / "o6-nodeset-matrix"
_DEFAULT_MATRIX = _ROOT / "tools" / "nodeset_compiler" / "GENERATION_MATRIX.md"
_RUNTIME_CHECKS = (
    "prerequisites",
    "imported",
    "loaded",
    "instantiated",
    "mandatory_children",
    "references",
    "method_arguments",
    "values",
    "namespace_roundtrip",
)


def _runtime_order(
    specification: Specification, specifications: tuple[Specification, ...]
) -> tuple[Specification, ...]:
    dependencies = _transitive_dependencies(specification, specifications)
    by_shortname = {item.shortname: item for item in (*specifications, *compatibility_registry())}
    ordered: list[Specification] = []
    for dependency in (by_shortname[item.shortname] for item in dependencies):
        if dependency not in specifications:
            current = next((item for item in specifications if item.uri == dependency.uri), None)
            if current is not None and current not in ordered:
                ordered.append(current)
        if dependency not in ordered:
            ordered.append(dependency)
    return (*ordered, specification)


def _package_members(module: Any) -> dict[str, Any]:
    """Merge a generated namespace package's own attributes with those of its
    generated submodules (objtypes, vartypes, reftypes, datatypes, instances),
    mirroring the pre-split flat-module layout the runtime checks were written for."""
    merged = dict(vars(module))
    for value in list(merged.values()):
        if isinstance(value, types.ModuleType) and value.__name__.startswith(f"{module.__name__}."):
            merged.update(vars(value))
    return merged


def _declared_in_package(value: Any, module: Any) -> bool:
    owner = getattr(value, "__module__", None)
    return owner is not None and (
        owner == module.__name__ or owner.startswith(f"{module.__name__}.")
    )


def _representative(server: Any, module: Any) -> str:
    from o6._declarations import ObjectTypeSpec, VariableTypeSpec

    members = _package_members(module)
    candidates = []
    abstract_types = []
    for name, value in members.items():
        if not isinstance(value, type) or not _declared_in_package(value, module):
            continue
        declaration = getattr(value, "__o6_declaration__", None)
        attributes = getattr(declaration, "attributes", None)
        if not isinstance(attributes, (ObjectTypeSpec, VariableTypeSpec)):
            continue
        if bool(getattr(attributes, "is_abstract", False)):
            abstract_types.append((name, declaration.nodeid))
            continue
        candidates.append((name, value))
    if not candidates:
        enums = [
            (name, value)
            for name, value in members.items()
            if isinstance(value, type)
            and _declared_in_package(value, module)
            and issubclass(value, enum.Enum)
            and list(value)
        ]
        if enums:
            name, candidate = min(enums)
            candidate(next(iter(candidate)).value)
            return name
        if abstract_types:
            name, nodeid = min(abstract_types)
            server.read(nodeid, attr="browsename")
            return f"{name} (abstract type registered)"
        declarations = sorted(
            (name, value._nodeid)
            for name, value in members.items()
            if getattr(value, "_nodeid", None) is not None
        )
        if not declarations:
            raise RuntimeError("the namespace has no type or declared node to verify")
        name, nodeid = declarations[0]
        server.read(nodeid, attr="browsename")
        return f"{name} (declared node registered)"
    name, candidate = min(candidates)
    candidate(server=None)
    return name


def _node_types(module: Any) -> list[tuple[str, type]]:
    from o6._declarations import ObjectTypeSpec, VariableTypeSpec

    return sorted(
        (name, value)
        for name, value in _package_members(module).items()
        if isinstance(value, type)
        and _declared_in_package(value, module)
        and isinstance(
            getattr(getattr(value, "__o6_declaration__", None), "attributes", None),
            (ObjectTypeSpec, VariableTypeSpec),
        )
        and not bool(
            getattr(
                getattr(getattr(value, "__o6_declaration__", None), "attributes", None),
                "is_abstract",
                False,
            )
        )
    )


def _check_mandatory_children(server: Any, module: Any) -> None:
    import o6
    from o6._declarations import _all_children

    for _, candidate in _node_types(module):
        mandatory = [
            child
            for child in _all_children(candidate)
            if str(child.modelling_rule) in {"i=78", "ns=0;i=78"}
        ]
        if not mandatory:
            continue
        instance = candidate(
            server=server,
            parent=server.objectsNode,
            browseName=f"Matrix{candidate.__name__}",
        )
        children = {
            reference.browseName.name for reference in server.browse(instance._nodeid).references
        }
        missing = {child.browsename for child in mandatory} - children
        if missing:
            raise RuntimeError(f"mandatory children were not created: {sorted(missing)}")
        return


def _check_reference_direction(server: Any, module: Any) -> None:
    import o6
    from o6._declarations import _instance_declaration
    from o6.ns import ns0

    declarations = sorted(
        (
            str(getattr(value, "_nodeid", "")),
            value,
        )
        for value in _package_members(module).values()
        if getattr(value, "_nodeid", None) is not None
    )
    for _, subject in declarations:
        try:
            subject_declaration = _instance_declaration(subject)
        except TypeError:
            continue
        for reference in subject_declaration.references:
            target = reference.target
            target_id = getattr(target, "_nodeid", None) or target
            if target_id is None or isinstance(target_id, o6.ExpandedNodeId):
                continue
            source_id = o6.NodeId(subject._nodeid)
            target_id = o6.NodeId(target_id)
            forward_source, forward_target = (
                (target_id, source_id) if reference.inverse else (source_id, target_id)
            )
            forward = server.browse(
                forward_source,
                reftype=reference.reference_type,
                refsubtypes=False,
                resultMask=ns0.datatypes.BrowseResultMask.REFERENCE_TYPE_ID,
            )
            if not any(
                o6.NodeId(reference.nodeId) == forward_target for reference in forward.references
            ):
                raise RuntimeError(
                    f"forward reference {forward_source} --[{reference.reference_type}]--> "
                    f"{forward_target} is not browseable; got "
                    f"{[reference.nodeId for reference in forward.references]}"
                )
            inverse_result = server.browse(
                forward_target,
                direction=ns0.datatypes.BrowseDirection.INVERSE,
                reftype=reference.reference_type,
                refsubtypes=False,
                resultMask=ns0.datatypes.BrowseResultMask.REFERENCE_TYPE_ID,
            )
            if not any(
                o6.NodeId(reference.nodeId) == forward_source
                for reference in inverse_result.references
            ):
                raise RuntimeError("inverse reference is not browseable")
            return


def _check_method_arguments(server: Any, module: Any) -> None:
    from o6._declarations import MethodSpec, _instance_declaration

    methods = []
    for value in _package_members(module).values():
        try:
            declaration = _instance_declaration(value)
        except TypeError:
            continue
        if isinstance(declaration.attributes, MethodSpec) and (
            declaration.attributes.input_args or declaration.attributes.output_args
        ):
            methods.append((str(declaration.nodeid or ""), declaration.attributes))
    for _, method in sorted(methods, key=lambda item: item[0]):
        for expected, nodeid in (
            (method.input_args, method.input_args_nodeid),
            (method.output_args, method.output_args_nodeid),
        ):
            if not expected or nodeid is None:
                continue
            actual = server.read(nodeid)
            expected_shape = [
                (argument.name, argument.dataType, argument.valueRank) for argument in expected
            ]
            actual_shape = [
                (argument.name, argument.dataType, argument.valueRank) for argument in actual
            ]
            if actual_shape != expected_shape:
                raise RuntimeError(
                    f"method Argument metadata changed at {nodeid}: "
                    f"expected {expected_shape}, got {actual_shape}"
                )
        return


def _check_value_roundtrip(server: Any, module: Any, checkpoint: Any = None) -> None:
    import o6
    from o6._declarations import VariableSpec, _instance_declaration

    declarations = []
    for value in _package_members(module).values():
        try:
            declaration = _instance_declaration(value)
        except TypeError:
            continue
        payload = declaration.attributes
        if (
            declaration.nodeid is not None
            and isinstance(payload, VariableSpec)
            and payload.value is not None
        ):
            declarations.append((str(declaration.nodeid), declaration))
    declarations.sort(key=lambda item: item[0])
    if not declarations:
        return
    nodeid, declaration = declarations[0]
    if checkpoint is not None:
        checkpoint(f"value read {nodeid} ({type(declaration.attributes.value).__name__})")
    value = server.read(nodeid)
    if checkpoint is not None:
        checkpoint(f"value encode {nodeid} ({type(value).__name__})")
    encoded = o6.encodeBinary(o6.DataValue(value=value))
    decoded = o6.decodeBinary(encoded, o6.DataValue)
    if o6.encodeBinary(decoded) != encoded:
        raise RuntimeError("value changed during binary encode/decode")


def _check_namespace_roundtrip(server: Any, module: Any, shortname: str) -> None:
    import o6

    infos = [info for info in module.__NAMESPACES__ if info.shortname == shortname]
    if len(infos) != 1 or getattr(o6.ns, shortname).uri != infos[0].uri:
        raise RuntimeError("namespace shortname/URI registration did not round-trip")
    nodeids = sorted(
        str(nodeid)
        for value in _package_members(module).values()
        if (nodeid := getattr(getattr(value, "__o6_declaration__", None), "nodeid", None))
        is not None
    )
    if not nodeids:
        return
    server.read(o6.NodeId(nodeids[0]), attr="browsename")


def _runtime_worker(shortname: str, out_dir: Path, result_path: Path) -> int:
    import o6
    import o6.ns

    specifications = registry()
    specification = next(
        item for item in (*specifications, *compatibility_registry()) if item.shortname == shortname
    )
    result: dict[str, Any] = dict.fromkeys(_RUNTIME_CHECKS, False)

    def checkpoint(check: str) -> None:
        result["active_check"] = check
        result_path.write_text(json.dumps(result, sort_keys=True), encoding="utf-8")

    server = None
    try:
        checkpoint("prerequisites/import")
        modules = []
        for item in _runtime_order(specification, specifications):
            module_name = f"o6.ns.{item.shortname}"
            module_spec = importlib.util.spec_from_file_location(
                module_name, out_dir / item.shortname / "__init__.py"
            )
            if module_spec is None or module_spec.loader is None:
                raise ImportError(f"cannot load generated module {item.shortname}")
            module = importlib.util.module_from_spec(module_spec)
            sys.modules[module_name] = module
            setattr(o6.ns, item.shortname, module)
            module_spec.loader.exec_module(module)
            modules.append(module)
        result["imported"] = True
        result["prerequisites"] = True

        checkpoint("server loading")
        server = o6.Server()
        for item, module in zip(_runtime_order(specification, specifications), modules):
            if item.shortname == "ns0":
                continue  # Every Server already contains the standard namespace.
            server.ns.append(module)
        result["loaded"] = True
        checkpoint("type instantiation")
        result["representative"] = _representative(server, modules[-1])
        result["instantiated"] = True
        checkpoint("mandatory child creation")
        _check_mandatory_children(server, modules[-1])
        result["mandatory_children"] = True
        checkpoint("reference browsing")
        _check_reference_direction(server, modules[-1])
        result["references"] = True
        checkpoint("method argument metadata")
        _check_method_arguments(server, modules[-1])
        result["method_arguments"] = True
        checkpoint("value encoding/decoding")
        _check_value_roundtrip(server, modules[-1], checkpoint)
        result["values"] = True
        checkpoint("namespace round-trip")
        _check_namespace_roundtrip(server, modules[-1], shortname)
        result["namespace_roundtrip"] = True
        result.pop("active_check", None)
    except Exception as exc:  # noqa: BLE001 - serialized as matrix evidence
        notes = "; ".join(getattr(exc, "__notes__", ()))
        result["failure"] = (
            f"during {result.get('active_check', 'runtime verification')}: "
            f"{type(exc).__name__}: {exc}" + (f"; {notes}" if notes else "")
        )
    finally:
        if server is not None:
            try:
                server.stop()
            except Exception:
                pass
        result_path.write_text(json.dumps(result, sort_keys=True), encoding="utf-8")
    return 0 if all(result[check] for check in _RUNTIME_CHECKS) else 1


def _verify_runtime(specification: Specification, out_dir: Path, timeout: float) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as temporary:
        result_path = Path(temporary) / "result.json"
        try:
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.nodeset_compiler.generation_matrix",
                    "--worker",
                    specification.shortname,
                    "--out-dir",
                    str(out_dir),
                    "--result",
                    str(result_path),
                ],
                cwd=_ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return {
                "imported": False,
                "loaded": False,
                "instantiated": False,
                "failure": f"runtime verification exceeded {timeout:g}s",
            }
        if not result_path.exists():
            return {
                "imported": False,
                "loaded": False,
                "instantiated": False,
                "failure": "runtime verifier terminated without a result",
            }
        result = json.loads(result_path.read_text(encoding="utf-8"))
        if completed.returncode and "failure" not in result:
            result["failure"] = (
                f"runtime verifier terminated during "
                f"{result.get('active_check', 'runtime verification')} "
                f"(exit {completed.returncode})"
            )
        return result


def _mark(value: bool) -> str:
    return "yes" if value else "—"


def _matrix(results: tuple[CompileResult, ...], runtime: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# companion-specification generation matrix",
        "",
        "Generated by `python -m tools.nodeset_compiler.generation_matrix`.",
        "Every failure below is an explicit fail-closed limitation; no model that fails a stage is treated as supported.",
        "",
        "| Specification | Parsed | Generated | Compiled | Prerequisites | Imported | Server | Instantiated | Mandatory children | References | Method arguments | Values | Namespace round-trip |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    limitations: list[tuple[str, str]] = []
    for result in results:
        verification = runtime.get(result.specification.shortname, {})
        lines.append(
            f"| `{result.specification.shortname}` | {_mark(result.parsed)} | "
            f"{_mark(result.generated)} | {_mark(result.compiled)} | "
            f"{_mark(bool(verification.get('prerequisites')))} | "
            f"{_mark(bool(verification.get('imported')))} | "
            f"{_mark(bool(verification.get('loaded')))} | "
            f"{_mark(bool(verification.get('instantiated')))} | "
            f"{_mark(bool(verification.get('mandatory_children')))} | "
            f"{_mark(bool(verification.get('references')))} | "
            f"{_mark(bool(verification.get('method_arguments')))} | "
            f"{_mark(bool(verification.get('values')))} | "
            f"{_mark(bool(verification.get('namespace_roundtrip')))} |"
        )
        limitation = "; ".join(result.unsupported) or result.error or verification.get("failure")
        if limitation:
            limitations.append((result.specification.shortname, limitation))
    lines.extend(["", "## Intentional fail-closed limitations", ""])
    if limitations:
        lines.extend(f"- `{shortname}`: {limitation}" for shortname, limitation in limitations)
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=_DEFAULT_OUT)
    parser.add_argument("--matrix", type=Path, default=_DEFAULT_MATRIX)
    parser.add_argument("--runtime-timeout", type=float, default=120.0)
    parser.add_argument(
        "--reuse-generated",
        action="store_true",
        help="verify already-generated modules instead of compiling the registry again",
    )
    parser.add_argument("--worker", metavar="SHORTNAME", help=argparse.SUPPRESS)
    parser.add_argument("--result", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if args.worker:
        if args.result is None:
            parser.error("--worker requires --result")
        return _runtime_worker(args.worker, args.out_dir, args.result)

    specifications = dependency_order(registry())
    if args.reuse_generated:
        missing = [item for item in specifications if not (args.out_dir / item.shortname).is_dir()]
        if missing:
            parser.error(
                "--reuse-generated is missing: " + ", ".join(item.shortname for item in missing)
            )
        results = tuple(
            CompileResult(item, "generated", parsed=True, generated=True, compiled=True)
            for item in specifications
        )
    else:
        results = compile_registry(specifications, args.out_dir, keep_going=True)
    successful = {result.specification.shortname for result in results if result.compiled}
    if args.reuse_generated:
        successful.update(
            item.shortname
            for item in compatibility_registry()
            if (args.out_dir / item.shortname).is_dir()
        )
    runtime: dict[str, dict[str, Any]] = {}
    runtime_targets = [result for result in results if result.compiled]
    for index, result in enumerate(runtime_targets, start=1):
        specification = result.specification
        dependencies = _runtime_order(specification, specifications)[:-1]
        missing = [item.shortname for item in dependencies if item.shortname not in successful]
        if missing:
            verification = {"failure": f"generated dependency unavailable: {', '.join(missing)}"}
        else:
            verification = _verify_runtime(specification, args.out_dir, args.runtime_timeout)
        runtime[specification.shortname] = verification
        outcome = "pass" if all(verification.get(check) for check in _RUNTIME_CHECKS) else "fail"
        detail = f": {verification['failure']}" if "failure" in verification else ""
        print(
            f"[{index}/{len(runtime_targets)}] {specification.shortname} runtime: {outcome}{detail}"
        )
    _write_if_changed(args.matrix, _matrix(results, runtime))
    return (
        1
        if any(result.status in {"unsupported", "failed"} for result in results)
        or any(
            not all(verification.get(check) for check in _RUNTIME_CHECKS)
            for verification in runtime.values()
        )
        else 0
    )


if __name__ == "__main__":
    raise SystemExit(main())
