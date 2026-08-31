#!/usr/bin/env python3
"""Validate REAL-UI FULL redesign contracts and rendered evidence.

This verifier measures style-blind structure, capability coverage, scope
fidelity, and reproducible render artifacts. It does not score visual taste.
"""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
import struct
import sys
from typing import Any


STRUCTURAL_DIMENSIONS = (
    "navigation_model",
    "zones",
    "sequence",
    "grouping",
    "representations",
    "primary_interactions",
    "density",
    "responsive_model",
    "silhouette",
)
PRODUCT_FIELDS = (
    "purpose",
    "users",
    "user_intents",
    "primary_tasks",
    "capabilities",
    "workflows",
    "entities",
    "relationships",
    "content_data",
    "routes",
    "business_logic",
    "technical_constraints",
    "seo_requirements",
    "accessibility_requirements",
    "platform_context",
)
PRESENTATION_FIELDS = STRUCTURAL_DIMENSIONS + ("component_tree", "visual_system")
BRIEF_FIELDS = (
    "product_priorities",
    "user_priorities",
    "capabilities_to_preserve",
    "research_findings",
    "real_ui_knowledge",
    "ia_direction",
    "navigation_direction",
    "content_representation",
    "interaction_direction",
    "responsive_priorities",
    "structures_to_preserve",
    "structures_to_change",
    "out_of_scope_features",
)
CAPABILITY_STATUSES = {
    "PRESERVE",
    "TRANSFORM",
    "MERGE",
    "RELOCATE",
    "REMOVE WITH JUSTIFICATION",
}
SCOPE_CLASSES = {
    "EXISTING REQUIREMENT",
    "EXPLICIT USER REQUEST",
    "STRICTLY NECESSARY SUPPORTING UX",
    "HYPOTHESIS",
    "OUT OF SCOPE",
}
IMPLEMENTABLE_SCOPE = {
    "EXISTING REQUIREMENT",
    "EXPLICIT USER REQUEST",
    "STRICTLY NECESSARY SUPPORTING UX",
}
EVIDENCE_LABELS = {
    "SOURCE-OBSERVED",
    "RUNTIME-OBSERVED",
    "RENDER-OBSERVED",
    "INFERRED",
    "RECOMMENDED",
    "UNCERTAIN",
    "PLATFORM RULE",
    "DESIGN PRINCIPLE",
}


def _present(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return value is not None


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _require_fields(obj: dict[str, Any], fields: tuple[str, ...], prefix: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj or not _present(obj[field]):
            errors.append(f"{prefix}.{field} is required and cannot be empty")


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.landmarks: set[str] = set()
        self.zones: list[str] = []
        self.capabilities: set[str] = set()
        self.features: set[str] = set()
        self.h1_count = 0
        self.skip_link = False
        self.html_lang = ""
        self.main_ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag in {"header", "nav", "main", "footer"}:
            self.landmarks.add(tag)
        if tag == "h1":
            self.h1_count += 1
        if tag == "html":
            self.html_lang = values.get("lang", "")
        if tag == "main" and values.get("id"):
            self.main_ids.add(values["id"])
        if tag == "a" and values.get("href", "").startswith("#"):
            if values["href"][1:] in self.main_ids or "skip" in values.get("class", "").lower():
                self.skip_link = True
        zone = values.get("data-zone")
        if zone and zone not in self.zones:
            self.zones.append(zone)
        for capability in values.get("data-capability", "").split():
            if capability:
                self.capabilities.add(capability)
        feature = values.get("data-feature")
        if feature:
            self.features.add(feature)


def inspect_html(path: Path) -> StructureParser:
    parser = StructureParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a valid PNG")
    return struct.unpack(">II", header[16:24])


def _resolve(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (base / path).resolve()


def validate_plan(case: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    if case.get("depth") != "FULL REDESIGN":
        errors.append("depth must be FULL REDESIGN")
    if "full redesign" not in str(case.get("request", "")).lower():
        errors.append("request must preserve the normal FULL REDESIGN test wording")

    product = case.get("product")
    before = case.get("presentation_before")
    brief = case.get("design_brief")
    after = case.get("proposed_structure")
    if not isinstance(product, dict):
        errors.append("product object is required")
        product = {}
    if not isinstance(before, dict):
        errors.append("presentation_before object is required")
        before = {}
    if not isinstance(brief, dict):
        errors.append("design_brief object is required")
        brief = {}
    if not isinstance(after, dict):
        errors.append("proposed_structure object is required")
        after = {}
    _require_fields(product, PRODUCT_FIELDS, "product", errors)
    _require_fields(before, PRESENTATION_FIELDS, "presentation_before", errors)
    _require_fields(brief, BRIEF_FIELDS, "design_brief", errors)
    _require_fields(after, STRUCTURAL_DIMENSIONS, "proposed_structure", errors)

    research = case.get("research", [])
    if not isinstance(research, list) or not research:
        errors.append("research must contain at least one targeted finding")
    else:
        for index, item in enumerate(research):
            if not isinstance(item, dict):
                errors.append(f"research[{index}] must be an object")
                continue
            _require_fields(item, ("source", "label", "finding", "product_use"), f"research[{index}]", errors)
            if item.get("label") not in EVIDENCE_LABELS:
                errors.append(f"research[{index}].label is not an accepted evidence label")

    decisions = case.get("decisions", [])
    if not isinstance(decisions, list) or not decisions:
        errors.append("decisions must trace important design choices")
    else:
        for index, item in enumerate(decisions):
            if not isinstance(item, dict):
                errors.append(f"decisions[{index}] must be an object")
                continue
            _require_fields(
                item,
                ("decision", "evidence", "knowledge", "product_reason", "confidence"),
                f"decisions[{index}]",
                errors,
            )

    capabilities = case.get("capability_ledger", [])
    capability_ids: set[str] = set()
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("capability_ledger cannot be empty")
    else:
        for index, item in enumerate(capabilities):
            prefix = f"capability_ledger[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            _require_fields(item, ("id", "status", "source", "before"), prefix, errors)
            capability_id = item.get("id")
            if capability_id in capability_ids:
                errors.append(f"duplicate capability id: {capability_id}")
            capability_ids.add(capability_id)
            status = item.get("status")
            if status not in CAPABILITY_STATUSES:
                errors.append(f"{prefix}.status is invalid")
            if status == "REMOVE WITH JUSTIFICATION":
                if not _present(item.get("justification")):
                    errors.append(f"{prefix}.justification is required for removal")
            elif not _present(item.get("after")):
                errors.append(f"{prefix}.after is required for retained capabilities")

    product_capabilities = set(product.get("capabilities", [])) if isinstance(product.get("capabilities"), list) else set()
    if product_capabilities and product_capabilities != capability_ids:
        missing = sorted(product_capabilities - capability_ids)
        extra = sorted(capability_ids - product_capabilities)
        if missing:
            errors.append(f"capability ledger missing product capabilities: {', '.join(missing)}")
        if extra:
            errors.append(f"capability ledger contains unmodeled capabilities: {', '.join(extra)}")

    scope = case.get("scope_ledger", [])
    scope_ids: set[str] = set()
    if not isinstance(scope, list) or not scope:
        errors.append("scope_ledger cannot be empty")
    else:
        for index, item in enumerate(scope):
            prefix = f"scope_ledger[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            _require_fields(item, ("id", "classification", "reason"), prefix, errors)
            scope_id = item.get("id")
            if scope_id in scope_ids:
                errors.append(f"duplicate scope id: {scope_id}")
            scope_ids.add(scope_id)
            classification = item.get("classification")
            if classification not in SCOPE_CLASSES:
                errors.append(f"{prefix}.classification is invalid")
            if item.get("implemented") and classification not in IMPLEMENTABLE_SCOPE:
                errors.append(f"{prefix} implements unsupported scope ({classification})")

    changed = []
    kept = []
    for dimension in STRUCTURAL_DIMENSIONS:
        if dimension in before and dimension in after:
            if _canonical(before[dimension]) == _canonical(after[dimension]):
                kept.append(dimension)
            else:
                changed.append(dimension)
    if len(changed) < 5:
        errors.append(
            "FULL redesign changes fewer than five style-blind dimensions; "
            "manual review is required instead of an automatic PLAN PASS"
        )

    structural_decisions = case.get("structural_decisions", [])
    decision_dimensions = set()
    if not isinstance(structural_decisions, list):
        errors.append("structural_decisions must be a list")
    else:
        for index, item in enumerate(structural_decisions):
            prefix = f"structural_decisions[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            _require_fields(item, ("dimension", "before", "after", "evidence", "product_reason"), prefix, errors)
            dimension = item.get("dimension")
            if dimension not in STRUCTURAL_DIMENSIONS:
                errors.append(f"{prefix}.dimension is invalid")
            decision_dimensions.add(dimension)
    uncovered = set(changed) - decision_dimensions
    if uncovered:
        errors.append(f"structural changes lack decisions: {', '.join(sorted(uncovered))}")

    keep_audit = case.get("kept_structure", [])
    keep_dimensions = set()
    if not isinstance(keep_audit, list):
        errors.append("kept_structure must be a list")
    else:
        for index, item in enumerate(keep_audit):
            prefix = f"kept_structure[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            _require_fields(item, ("dimension", "reason", "evidence"), prefix, errors)
            keep_dimensions.add(item.get("dimension"))
    unaudited = set(kept) - keep_dimensions
    if unaudited:
        errors.append(f"preserved structural dimensions lack still-correct audit: {', '.join(sorted(unaudited))}")

    notes.append(f"style-blind dimensions changed: {len(changed)}/9 ({', '.join(changed)})")
    notes.append(f"capabilities covered: {len(capability_ids)}")
    notes.append(f"scope entries checked: {len(scope_ids)}")
    return errors, notes


def _validate_snapshot(path: Path, expected: tuple[int, int], declared_zones: list[str], errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid DOM snapshot {path}: {exc}")
        return
    viewport = data.get("viewport", {})
    if (viewport.get("width"), viewport.get("height")) != expected:
        errors.append(f"DOM snapshot {path.name} has wrong viewport")
    zones = [item.get("id") for item in data.get("zones", [])]
    if zones != declared_zones:
        errors.append(f"DOM snapshot {path.name} zones do not match contract")
    if data.get("console_errors"):
        errors.append(f"DOM snapshot {path.name} contains console errors")


def _validate_a11y(path: Path, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid accessibility report {path}: {exc}")
        return
    counts = data.get("counts", data.get("data", {}).get("counts", {}))
    violation_count = counts.get("violations", len(data.get("violations", [])))
    if violation_count:
        errors.append(f"accessibility report {path.name} contains {violation_count} violations")


def validate_render(case: dict[str, Any], case_path: Path) -> tuple[list[str], list[str]]:
    errors, notes = validate_plan(case)
    base = case_path.parent
    implementation = case.get("implementation", {})
    if not isinstance(implementation, dict):
        errors.append("implementation object is required")
        return errors, notes

    html_parsers: dict[str, StructureParser] = {}
    for state in ("before", "after"):
        raw = implementation.get(state)
        if not raw:
            errors.append(f"implementation.{state} is required")
            continue
        path = _resolve(base, raw)
        if not path.is_file():
            errors.append(f"implementation file missing: {path}")
            continue
        html_parsers[state] = inspect_html(path)

    for state, parser in html_parsers.items():
        missing_landmarks = {"header", "nav", "main", "footer"} - parser.landmarks
        if missing_landmarks:
            errors.append(f"{state} implementation missing landmarks: {', '.join(sorted(missing_landmarks))}")
        if parser.h1_count != 1:
            errors.append(f"{state} implementation must contain exactly one h1")
        if not parser.html_lang:
            errors.append(f"{state} implementation must declare html lang")
        if not parser.skip_link:
            errors.append(f"{state} implementation must include a skip link")

    before_structure = case.get("presentation_before", {})
    after_structure = case.get("proposed_structure", {})
    if "before" in html_parsers and html_parsers["before"].zones != before_structure.get("zones"):
        errors.append("before HTML data-zone order does not match presentation extraction")
    if "after" in html_parsers and html_parsers["after"].zones != after_structure.get("zones"):
        errors.append("after HTML data-zone order does not match proposed structure")

    capabilities = case.get("capability_ledger", [])
    expected_capabilities = {
        item.get("id")
        for item in capabilities
        if item.get("status") != "REMOVE WITH JUSTIFICATION"
    }
    if "after" in html_parsers:
        missing = expected_capabilities - html_parsers["after"].capabilities
        extra = html_parsers["after"].capabilities - expected_capabilities
        if missing:
            errors.append(f"after HTML missing capability markers: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"after HTML has unmodeled capability markers: {', '.join(sorted(extra))}")

        scope_by_id = {item.get("id"): item for item in case.get("scope_ledger", [])}
        for feature in html_parsers["after"].features:
            entry = scope_by_id.get(feature)
            if not entry or entry.get("classification") not in IMPLEMENTABLE_SCOPE:
                errors.append(f"after HTML implements unsupported feature marker: {feature}")
        expected_features = {item.get("id") for item in case.get("scope_ledger", []) if item.get("implemented")}
        missing_features = expected_features - html_parsers["after"].features
        if missing_features:
            errors.append(f"after HTML lacks implemented scope markers: {', '.join(sorted(missing_features))}")

    render = case.get("render", {})
    viewports = render.get("viewports", {}) if isinstance(render, dict) else {}
    for device in ("desktop", "mobile"):
        viewport = viewports.get(device, {})
        expected = (viewport.get("width"), viewport.get("height"))
        if not all(isinstance(value, int) and value > 0 for value in expected):
            errors.append(f"render.viewports.{device} must provide positive width/height")
            continue
        for state in ("before", "after"):
            for artifact_kind, suffix in (("screenshots", ".png"), ("snapshots", ".json"), ("a11y", ".json")):
                raw = render.get(artifact_kind, {}).get(f"{state}_{device}")
                if not raw:
                    errors.append(f"render.{artifact_kind}.{state}_{device} is required")
                    continue
                path = _resolve(base, raw)
                if not path.is_file():
                    errors.append(f"render artifact missing: {path}")
                    continue
                if artifact_kind == "screenshots":
                    try:
                        actual = png_size(path)
                    except (OSError, ValueError) as exc:
                        errors.append(f"invalid screenshot {path}: {exc}")
                    else:
                        if actual != expected:
                            errors.append(f"screenshot {path.name} is {actual}, expected {expected}")
                elif artifact_kind == "snapshots":
                    declared = before_structure.get("zones", []) if state == "before" else after_structure.get("zones", [])
                    _validate_snapshot(path, expected, declared, errors)
                else:
                    _validate_a11y(path, errors)

    notes.append("implementation markers and render artifacts checked")
    return errors, notes


def validate_case(case_path: Path, phase: str = "render") -> tuple[list[str], list[str]]:
    try:
        case = json.loads(case_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read case: {exc}"], []
    if not isinstance(case, dict):
        return ["case root must be an object"], []
    if phase == "plan":
        return validate_plan(case)
    return validate_render(case, case_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", type=Path, help="Path to a FULL redesign case JSON")
    parser.add_argument("--phase", choices=("plan", "render"), default="render")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    case_path = args.case.resolve()
    errors, notes = validate_case(case_path, args.phase)
    result = {
        "case": str(case_path),
        "phase": args.phase,
        "status": "FAIL" if errors else f"{args.phase.upper()} PASS",
        "notes": notes,
        "errors": errors,
    }
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["status"])
        for note in notes:
            print(f"  - {note}")
        for error in errors:
            print(f"  ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
