"""Executable regression tests for the FULL redesign behavior gate."""

import copy
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_redesign", ROOT / "scripts" / "validate_redesign.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def valid_case():
    before = {
        "navigation_model": "top-links",
        "zones": ["hero", "promotion", "catalog"],
        "sequence": ["hero", "promotion", "catalog"],
        "grouping": {"home": ["hero", "promotion", "catalog"]},
        "representations": {"play": "split-hero", "discover": "card-grid"},
        "primary_interactions": ["hero-play", "filter-chips"],
        "density": "uniform-medium",
        "responsive_model": "stack-desktop-sections",
        "silhouette": "hero-band-grid",
        "component_tree": ["Home", "Hero", "Ad", "Grid"],
        "visual_system": ["dark", "rounded", "cards"],
    }
    after = {
        "navigation_model": "task-dock-and-library",
        "zones": ["resume-dock", "play-stage", "library-explorer"],
        "sequence": ["resume-dock", "play-stage", "library-explorer"],
        "grouping": {"play": ["resume-dock", "play-stage"], "browse": ["library-explorer"]},
        "representations": {"play": "persistent-stage", "discover": "ranked-list-explorer"},
        "primary_interactions": ["resume", "quick-switch", "search-library"],
        "density": "play-focus-with-dense-library",
        "responsive_model": "desktop-two-zone-mobile-task-tabs",
        "silhouette": "stage-with-docked-library",
    }
    product_fields = {
        "purpose": "Let returning players resume or launch a browser game quickly",
        "users": ["casual players"],
        "user_intents": ["resume", "play", "browse"],
        "primary_tasks": ["resume a game", "launch a game", "find another game"],
        "capabilities": ["play", "discovery", "resume"],
        "workflows": ["return -> resume", "browse -> choose -> play"],
        "entities": ["game", "session", "category"],
        "relationships": ["category has games", "session belongs to game"],
        "content_data": ["titles", "progress", "categories"],
        "routes": ["/", "/game/:slug"],
        "business_logic": ["local progress"],
        "technical_constraints": ["static web"],
        "seo_requirements": ["one h1"],
        "accessibility_requirements": ["keyboard path"],
        "platform_context": ["responsive web", "touch and pointer"],
    }
    brief = {
        "product_priorities": ["play speed"],
        "user_priorities": ["resume"],
        "capabilities_to_preserve": ["play", "discovery", "resume"],
        "research_findings": ["consistent navigation supports access"],
        "real_ui_knowledge": ["product-modeling", "gaming"],
        "ia_direction": "tasks instead of promotional sections",
        "navigation_direction": "task dock",
        "content_representation": "stage plus explorer",
        "interaction_direction": "one-step resume",
        "responsive_priorities": ["play first"],
        "structures_to_preserve": ["route names"],
        "structures_to_change": ["hero-grid composition"],
        "out_of_scope_features": ["advertising"],
    }
    changes = []
    for dimension in VALIDATOR.STRUCTURAL_DIMENSIONS:
        changes.append(
            {
                "dimension": dimension,
                "before": before[dimension],
                "after": after[dimension],
                "evidence": "product task model",
                "product_reason": "shortens the play/resume path",
            }
        )
    return {
        "case_id": "test-gaming",
        "depth": "FULL REDESIGN",
        "request": "Use REAL-UI for a FULL REDESIGN of this product.",
        "product": product_fields,
        "presentation_before": before,
        "research": [
            {
                "source": "https://example.test/evidence",
                "label": "DESIGN PRINCIPLE",
                "finding": "navigation must remain predictable",
                "product_use": "keeps game switching consistent",
            }
        ],
        "design_brief": brief,
        "decisions": [
            {
                "decision": "lead with resume/play",
                "evidence": "top task model",
                "knowledge": "foundations/product-modeling.md",
                "product_reason": "returning play is the highest-frequency task",
                "confidence": "HIGH",
            }
        ],
        "capability_ledger": [
            {"id": "play", "status": "TRANSFORM", "source": "existing", "before": "hero", "after": "play-stage"},
            {"id": "discovery", "status": "TRANSFORM", "source": "existing", "before": "grid", "after": "library-explorer"},
            {"id": "resume", "status": "RELOCATE", "source": "existing", "before": "rail", "after": "resume-dock"},
        ],
        "scope_ledger": [
            {"id": "play", "classification": "EXISTING REQUIREMENT", "implemented": True, "reason": "existing route"},
            {"id": "advertising", "classification": "OUT OF SCOPE", "implemented": False, "reason": "not requested"},
        ],
        "proposed_structure": after,
        "structural_decisions": changes,
        "kept_structure": [],
    }


class FullRedesignGateTest(unittest.TestCase):
    def test_valid_evidence_driven_plan_passes(self):
        errors, notes = VALIDATOR.validate_plan(valid_case())
        self.assertEqual([], errors)
        self.assertTrue(any("9/9" in note for note in notes))

    def test_cosmetic_only_full_redesign_fails(self):
        case = valid_case()
        case["proposed_structure"] = {
            key: copy.deepcopy(case["presentation_before"][key])
            for key in VALIDATOR.STRUCTURAL_DIMENSIONS
        }
        case["structural_decisions"] = []
        case["kept_structure"] = [
            {"dimension": key, "reason": "it existed", "evidence": "old UI"}
            for key in VALIDATOR.STRUCTURAL_DIMENSIONS
        ]
        errors, _ = VALIDATOR.validate_plan(case)
        self.assertTrue(any("fewer than five" in error for error in errors))

    def test_unsupported_advertising_fails(self):
        case = valid_case()
        ad = next(row for row in case["scope_ledger"] if row["id"] == "advertising")
        ad["implemented"] = True
        errors, _ = VALIDATOR.validate_plan(case)
        self.assertTrue(any("unsupported scope" in error for error in errors))

    def test_silent_capability_loss_fails(self):
        case = valid_case()
        case["capability_ledger"] = [
            row for row in case["capability_ledger"] if row["id"] != "resume"
        ]
        errors, _ = VALIDATOR.validate_plan(case)
        self.assertTrue(any("missing product capabilities" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
