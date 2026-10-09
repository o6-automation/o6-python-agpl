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

"""Account for every NodeSet XML model in the dependency checkout."""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.etree import ElementTree

from .compile_all import Specification, _metadata, compatibility_registry, registry

_ROOT = Path(__file__).resolve().parents[2] / "deps" / "UA-Nodeset"

EXCLUSIONS = {
    "AML/Topology.xml": "AutomationML example topology, not a companion model.",
    "AdditiveManufacturing/AdditiveManufacturing-Example.xml": "Example instance model.",
    "DemoModel/DemoModel.NodeSet2.xml": "SDK demonstration model.",
    "IA/Opc.Ua.IA.NodeSet2.examples.xml": "Example instance model.",
    "LaserSystems/LaserSystem-Example.NodeSet2.xml": "Example instance model.",
    "Machinery/Opc.Ua.Machinery.Examples.NodeSet2.xml": "Example instance model.",
    "MetalForming/MetalForming_Example.xml": "Example instance model.",
    "PlasticsRubber/Extrusion/GeneralTypes/1.00/Opc.Ua.PlasticsRubber.Extrusion.GeneralTypes.NodeSet2.xml": "Historical 1.00 release; the registered extrusion v1 model uses 1.01.",
    "PlasticsRubber/GeneralTypes/1.02/Opc.Ua.PlasticsRubber.GeneralTypes.NodeSet2.xml": "Historical 1.02 release; the registered model uses 1.03.",
    "PlasticsRubber/LDS/1.00/Opc.Ua.PlasticsRubber.LDS.NodeSet2.xml": "Historical 1.00.1 release; the registered model uses the 1.02 directory.",
    "Pumps/instanceexample.xml": "Example instance model.",
    "Schema/Opc.Ua.NodeSet2.xml": "Alternate standard namespace; ns0 uses Opc.Ua.NodeSet2.Services.xml.",
    "TestModel/TestModel.NodeSet2.xml": "SDK test model.",
}


def check_inventory(
    root: Path = _ROOT,
    *,
    specifications: tuple[Specification, ...] | None = None,
    compatibility: tuple[Specification, ...] | None = None,
    exclusions: dict[str, str] | None = None,
) -> dict[str, str]:
    specifications = registry() if specifications is None else specifications
    compatibility = compatibility_registry() if compatibility is None else compatibility
    exclusions = EXCLUSIONS if exclusions is None else exclusions
    sources = {
        path.resolve(): f"target {spec.shortname}" for spec in specifications for path in spec.paths
    }
    for spec in compatibility:
        for path in spec.paths:
            sources.setdefault(path.resolve(), f"compatibility {spec.shortname}")

    classified = {}
    errors = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() != ".xml":
            continue
        document = ElementTree.parse(path).getroot()
        if document.tag.rsplit("}", 1)[-1] != "UANodeSet":
            continue
        relative = path.relative_to(root).as_posix()
        if path.resolve() in sources:
            classified[relative] = sources[path.resolve()]
            if relative in exclusions:
                errors.append(f"registered model is also excluded: {relative}")
        elif exclusions.get(relative, "").strip():
            classified[relative] = f"excluded: {exclusions[relative]}"
        else:
            identity, _ = _metadata(path)
            errors.append(f"unclassified NodeSet: {relative} ({identity.uri}, {identity.version})")
    for relative in sorted(exclusions.keys() - classified.keys()):
        if not (root / relative).is_file():
            errors.append(f"stale exclusion: {relative}")
        elif relative not in classified and exclusions[relative].strip():
            errors.append(f"exclusion is not a NodeSet: {relative}")
    if not classified:
        errors.append(f"no NodeSets found in {root}")
    if errors:
        raise ValueError("\n".join(errors))
    return classified


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    try:
        classified = check_inventory()
    except (OSError, ValueError, ElementTree.ParseError) as exc:
        print(exc)
        return 1
    for path, classification in classified.items():
        print(f"{path}: {classification}")
    print(f"All {len(classified)} NodeSets accounted for.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
