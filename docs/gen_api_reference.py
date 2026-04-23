"""mkdocstrings-safe API generator for o6 / _o6 (deduplicated + stable)."""

from __future__ import annotations

import argparse
import importlib
import inspect
import pkgutil
from pathlib import Path

try:
    mkdocs_gen_files = importlib.import_module("mkdocs_gen_files")
except ImportError:
    mkdocs_gen_files = None


ROOT_PACKAGES = ["o6"]

EXPLICIT_CLASSES = [
    "o6.client.Client",
    "o6.server.Server",
]

STUB_MODULES = [
    "o6._o6.types",
    "o6._o6.types_builtin",
]


# -------------------------------------------------
# PUBLIC FILTER
# -------------------------------------------------
def is_public_name(name: str) -> bool:
    """Return True only if every component of *name* is public (no leading _)."""
    return all(not part.startswith("_") for part in name.split("."))


# -------------------------------------------------
# STRICT PACKAGE FILTER
# -------------------------------------------------
def is_allowed(name: str) -> bool:
    return (
        name == "o6"
        or name.startswith("o6.")
        or name == "o6._o6"
        or name.startswith("o6._o6.")
    )


# -------------------------------------------------
# Fix module names
# -------------------------------------------------
def fix_module_name(detected_module: str, source_module: str) -> str:
    """Fix module names that lost underscores (e.g., o6 -> o6._o6)
    
    Only fixes if we're scanning o6._o6 module but class reports o6 module.
    """
    if source_module.startswith("o6._o6") and detected_module.startswith("o6") and not detected_module.startswith("o6._o6"):
        return detected_module.replace("o6", "o6._o6", 1)
    
    return detected_module


# -------------------------------------------------
# Safe import
# -------------------------------------------------
def safe_resolve(name: str):
    try:
        parts = name.split(".")
        obj = importlib.import_module(parts[0])
        for p in parts[1:]:
            obj = getattr(obj, p)
        return obj
    except Exception:
        return None


# -------------------------------------------------
# SOURCE SAFETY
# -------------------------------------------------
def is_source_safe(obj) -> bool:
    try:
        if not (inspect.isclass(obj) or inspect.isfunction(obj)):
            return False

        file = inspect.getsourcefile(obj)
        if file is None:
            return False

        inspect.getsource(obj)
        return True

    except Exception:
        return False


# -------------------------------------------------
# Resolve target
# -------------------------------------------------
def resolve_target(name: str):
    obj = safe_resolve(name)
    if obj is None:
        return None, None

    if not is_source_safe(obj):
        print(f"[skip no-source] {name}")
        return None, None

    return obj, name


# -------------------------------------------------
# Module discovery
# -------------------------------------------------
def discover_modules(package_name: str) -> list[str]:
    modules = [package_name]

    pkg = importlib.import_module(package_name)

    if hasattr(pkg, "__path__"):
        for mod in pkgutil.walk_packages(pkg.__path__, package_name + "."):
            if is_allowed(mod.name):
                modules.append(mod.name)

    return sorted(set(modules))


# -------------------------------------------------
# Class discovery
# -------------------------------------------------
def discover_classes(module_name: str) -> dict[str, str]:

    if not is_allowed(module_name):
        return {}

    try:
        mod = importlib.import_module(module_name)
    except Exception:
        return {}

    results: dict[str, str] = {}

    for _, obj in inspect.getmembers(mod, inspect.isclass):

        module = getattr(obj, "__module__", None)
        name = getattr(obj, "__name__", None)

        if not module or not name:
            continue

        module = fix_module_name(module, module_name)
        fq = f"{module}.{name}"

        if not is_allowed(fq):
            continue

        resolved_obj, resolved_path = resolve_target(fq)

        if resolved_path is None:
            continue

        results[fq] = resolved_path

    return results


# -------------------------------------------------
# Render normal module/class page
# -------------------------------------------------
def render_page(target: str) -> str:
    return f"""# {target}

::: {target}
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true
"""


# -------------------------------------------------
# Render stub module 
# -------------------------------------------------
def render_stub_module(module: str) -> str:
    return f"""# {module}

::: {module}
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true
"""


# -------------------------------------------------
# File writer
# -------------------------------------------------
def ensure_md(path: str) -> str:
    return path if path.endswith(".md") else path + ".md"


def write_file(output_dir: str, path: str, content: str) -> None:
    path = ensure_md(path)
    full_path = Path(output_dir) / path if output_dir else Path(path)

    if mkdocs_gen_files:
        with mkdocs_gen_files.open(str(full_path), "w") as f:
            f.write(content)

        mkdocs_gen_files.set_edit_path(
            str(full_path),
            "docs/gen_api_reference.py",
        )
    else:
        p = Path("docs") / full_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


# -------------------------------------------------
# Markdown helper
# -------------------------------------------------
def md_link(title: str, path: str) -> str:
    path = ensure_md(path)
    return f"- [{title}]({path})"


# -------------------------------------------------
# INDEX
# -------------------------------------------------
def build_index_md(pages: dict[str, str]) -> str:

    public = {}
    internal = {}

    for name, path in pages.items():
        path = ensure_md(path)

        if not is_allowed(name):
            continue

        if name.startswith("o6._o6"):
            internal[name] = path
        else:
            public[name] = path

    lines = ["# API Reference", ""]

    # PUBLIC
    lines.append("## Public API")
    lines.append("")

    for name, path in sorted(public.items(), key=lambda x: x[0].split(".")[-1].lower()):
        short = name.split(".")[-1]
        lines.append(md_link(short, path))

    lines.append("")

    # INTERNAL
    lines.append("## Low-Level API")
    lines.append("")

    for name, path in sorted(internal.items(), key=lambda x: x[0].split(".")[-1].lower()):
        short = name.split(".")[-1]
        lines.append(md_link(short, path))

    return "\n".join(lines)


# -------------------------------------------------
# GENERATOR
# -------------------------------------------------
def generate(output_dir: str = "api_reference") -> None:

    all_modules = set()

    for pkg in ROOT_PACKAGES:
        try:
            all_modules.update(discover_modules(pkg))
        except Exception as e:
            print(f"[skip package] {pkg}: {e}")

    print(f"[gen-api] modules: {len(all_modules)}")

    pages: dict[str, str] = {}

    # -------------------------------------------------
    # NORMAL MODULES + CLASSES
    # -------------------------------------------------
    for mod in sorted(all_modules):

        if not is_allowed(mod):
            continue

        try:
            importlib.import_module(mod)
        except Exception:
            continue

        classes = discover_classes(mod)

        for fq, path in classes.items():
            if not is_public_name(fq):
                continue
            pages[fq] = path

        if not is_public_name(mod):
            continue
        mod_path = mod.replace(".", "/") + ".md"
        pages.setdefault(mod, mod_path)
        write_file(output_dir, mod_path, render_page(mod))

    # -------------------------------------------------
    # STUB MODULES
    # -------------------------------------------------
    for stub in STUB_MODULES:

        if not is_allowed(stub):
            continue

        path = stub.replace(".", "/") + ".md"

        pages.setdefault(stub, path)

        write_file(output_dir, path, render_stub_module(stub))

    # -------------------------------------------------
    # WRITE CLASS PAGES
    # -------------------------------------------------
    for name, path in pages.items():
        if not is_allowed(name):
            continue
        write_file(output_dir, path, render_page(name))

    # -------------------------------------------------
    # INDEX
    # -------------------------------------------------
    index = build_index_md(pages)
    write_file(output_dir, "index.md", index)


# -------------------------------------------------
# CLI
# -------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir", default="api_reference")
    args = parser.parse_args()

    generate(args.output_dir)


if mkdocs_gen_files is not None:
    generate()

if __name__ == "__main__":
    main()