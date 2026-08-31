"""Executable structural and evidence-integrity checks for real-ui.

These tests verify repository contracts. They do not simulate an agent,
render an interface, or prove runtime design quality.
"""
import importlib.util
from pathlib import Path
import re
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
TOOLS = ROOT / "research" / "tools"


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def expand_braces(path):
    output = [path]
    while any("{" in item for item in output):
        expanded = []
        for item in output:
            match = re.search(r"\{([^}]+)\}", item)
            if not match:
                expanded.append(item)
                continue
            for option in match.group(1).split(","):
                expanded.append(item[:match.start()] + option.strip() + item[match.end():])
        output = expanded
    return output


class SkillContractsTest(unittest.TestCase):
    def test_retrieval_map_has_no_ghosts_or_orphans(self):
        skill = read("SKILL.md")
        promised = set()
        for line in skill.splitlines():
            if line.strip().startswith("|") and ".md" in line:
                for raw in re.findall(r"([A-Za-z0-9_{}/,-]+\.md)", line):
                    promised.update(expand_braces(raw))
        actual = {
            path.relative_to(KNOWLEDGE).as_posix()
            for path in KNOWLEDGE.rglob("*.md")
        }
        self.assertEqual(set(), promised - actual, "retrieval map contains missing files")
        self.assertEqual(set(), actual - promised, "knowledge file is orphaned from map")

    def test_scope_and_page_authority_are_mandatory(self):
        skill = read("SKILL.md")
        product = read("knowledge/foundations/product-modeling.md")
        industry = read("knowledge/industries/README.md")
        pages = read("knowledge/pages/README.md")
        self.assertIn("industries/README.md before industries/*", skill)
        self.assertIn("pages/README.md before pages/*", skill)
        for status in ("KNOWN", "REQUESTED", "NECESSARY SUPPORT UX", "HYPOTHESIS", "OUT OF SCOPE"):
            self.assertIn(status, product)
            self.assertIn(status, industry)
        self.assertIn("required content/action -> user task or decision", pages)

    def test_known_template_shortcuts_are_removed(self):
        checks = {
            "knowledge/visual-dna/dna-selector.md": "Industry default table",
            "knowledge/pages/homepage.md": "Universal homepage structure (adapt ratios, keep order)",
            "knowledge/pages/landing.md": "Anatomy (the proven section order)",
            "knowledge/pages/product-detail.md": "Universal anatomy",
        }
        for path, phrase in checks.items():
            self.assertNotIn(phrase, read(path), path)

    def test_accessibility_levels_are_not_conflated(self):
        floor = read("knowledge/accessibility/floor.md")
        contrast = read("knowledge/accessibility/contrast-motion.md")
        self.assertIn("2.5.8", floor)
        self.assertIn("24×24 CSS px", floor)
        self.assertNotIn("44×44px minimum (WCAG 2.2)", floor)
        self.assertRegex(contrast, r"2\.4\.13 Focus Appearance, AAA")
        self.assertIn("320 CSS px", floor)
        self.assertIn("400%", floor)

    def test_current_android_width_classes_are_present(self):
        for path in (
            "knowledge/responsive/adaptive-models.md",
            "knowledge/platforms/android.md",
            "knowledge/platforms/jetpack-compose.md",
        ):
            content = read(path)
            for boundary in ("840", "1200", "1600"):
                self.assertIn(boundary, content, path)
            self.assertIn("extra-large", content, path)

    def test_markdown_suites_are_not_claimed_as_executable(self):
        for path in ROOT.joinpath("tests").glob("*.md"):
            if "behavioral" in path.name:
                text = path.read_text(encoding="utf-8").lower()
                self.assertTrue(
                    "reasoned" in text or "specification" in text,
                    f"{path.name} must disclose its non-executable method",
                )

    def test_redesign_hard_gates_and_depth_precedence(self):
        workflow = read("knowledge/redesign/workflow.md")
        depth = read("knowledge/redesign/depth.md")
        self.assertIn("Extract (REDESIGN/FULL", workflow)
        self.assertIn("ALL depths: scope gate", workflow)
        self.assertNotIn("POLISH–REDESIGN: industry gap", workflow)
        for gate in ("DEPTH", "CAPABILITY LOSS", "SCOPE FIDELITY"):
            self.assertIn(gate, workflow)
        self.assertIn("a FAIL returns work to stage 3.5", workflow)
        self.assertIn("POLISH/REFRESH skip", depth)

    def test_industry_catalog_headings_do_not_claim_template_authority(self):
        banned = (
            "## Information architecture\n",
            "## Information architecture (real-world standard)",
            "## Components that define the genre",
            "## Conventions (follow)",
            "## DNA rules",
        )
        for path in ROOT.joinpath("knowledge", "industries").glob("*.md"):
            content = path.read_text(encoding="utf-8")
            for phrase in banned:
                self.assertNotIn(phrase, content, path.name)

    def test_normal_and_deep_mode_routing_contract(self):
        skill = read("SKILL.md")
        readme = read("README.md")
        normal_requests = (
            "Design a new ecommerce website",
            "Full redesign this existing gaming website",
            "Design a Flutter finance app",
        )
        deep_requests = (
            "Audit the entire REAL-UI knowledge base",
            "Validate all REAL-UI research and repair unsupported claims",
        )
        for request in normal_requests:
            self.assertRegex(skill, rf"(?m)^\| `{re.escape(request)}` \| NORMAL \|$")
        for request in deep_requests:
            self.assertRegex(skill, rf"(?m)^\| `{re.escape(request)}` \| DEEP / AUDIT \|$")
        self.assertIn("including **FULL REDESIGN**", skill)
        self.assertIn("A full redesign is normal use", readme)
        self.assertNotIn("major redesigns", readme)
        self.assertNotRegex(skill, r"(?i)triggers?:[^\n]*major redesign")


class ResearchToolTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(TOOLS))
        from metrics import site_value_prevalence
        cls.site_value_prevalence = staticmethod(site_value_prevalence)

        spec = importlib.util.spec_from_file_location("fetch_analyze", TOOLS / "fetch_analyze.py")
        cls.fetch_analyze = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.fetch_analyze)

    def test_breakpoint_prevalence_counts_each_site_once(self):
        sites = {
            "a": {"css": {"breakpoints": [["768", 99], ["1024", 2]]}},
            "b": {"css": {"breakpoints": [["768", 1]]}},
        }
        result = self.site_value_prevalence(sites, "css", "breakpoints", transform=int)
        self.assertEqual(2, result[768])
        self.assertEqual(1, result[1024])

    def test_css_validation_rejects_html(self):
        html = "<!doctype html><html>" + ("x" * 600) + "</html>"
        css = ".button { color: red; }" * 40
        self.assertFalse(self.fetch_analyze.looks_like_css(html, "text/html", "https://x.test/a.css"))
        self.assertTrue(self.fetch_analyze.looks_like_css(css, "text/css", "https://x.test/a.css"))

    def test_stylesheet_discovery_is_same_origin_and_deduplicated(self):
        html = """
        <link rel="stylesheet" href="/a.css">
        <link rel="stylesheet" href="/a.css">
        <link rel="stylesheet" href="https://cdn.test/b.css">
        """
        self.assertEqual(["https://example.test/a.css"], self.fetch_analyze.get_css_links(html, "https://example.test/page"))

    def test_framework_hint_does_not_call_generic_grid_tailwind(self):
        generic = self.fetch_analyze.analyze_html('<div class="flex grid">x</div>')
        distinctive = self.fetch_analyze.analyze_html('<div class="md:flex hover:bg-slate-900">x</div>')
        self.assertNotIn("tailwind", generic["framework_hints"])
        self.assertIn("tailwind", distinctive["framework_hints"])

    def test_modern_media_query_ranges_are_extracted(self):
        css = "@media (width >= 48rem) {} @media (1200px <= width) {} @media (max-width: 640px) {}"
        self.assertEqual([768, 1200, 640], self.fetch_analyze.extract_breakpoint_widths(css))

    def test_documented_breakpoint_counts_match_available_evidence(self):
        import json
        sites = {}
        for path in ROOT.joinpath("research", "reports").glob("*.json"):
            report = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(report, list):
                continue
            for site in report:
                if site.get("status") == "ok" and site.get("css"):
                    sites[site["name"]] = site
        if sites:
            result = self.site_value_prevalence(
                sites, "css", "breakpoints", transform=int
            )
            site_count = len(sites)
        else:
            summary = read("research/reports/aggregate-summary.txt")
            corpus = re.search(r"corpus:\s+(\d+) sites with CSS evidence", summary)
            self.assertIsNotNone(corpus, "published aggregate lacks corpus count")
            site_count = int(corpus.group(1))
            result = {}
            for width in (768, 1024):
                match = re.search(rf"(?m)^\s*{width}px\s+(\d+)\s*$", summary)
                self.assertIsNotNone(
                    match, f"published aggregate lacks {width}px count"
                )
                result[width] = int(match.group(1))
        findings = read("knowledge/research/observed-findings.md")
        self.assertIn(f"768px ({result[768]}/{site_count} sites", findings)
        self.assertIn(f"1024px ({result[1024]}/{site_count}", findings)

    def test_readme_knowledge_count_is_current(self):
        actual = len(list(KNOWLEDGE.rglob("*.md")))
        self.assertIn(f"**{actual} files**", read("README.md"))


class InstallerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts" / "install.py")
        cls.installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.installer)

    def test_path_normalization_deduplicates_windows_separators(self):
        values = {
            self.installer.normalized_relative(".agents/skills"),
            self.installer.normalized_relative(".agents\\skills"),
        }
        self.assertEqual(1, len(values))

    def test_verifier_has_no_machine_specific_source_path(self):
        verifier = read("research/tools/verify_install.py")
        self.assertIn("os.path.abspath(__file__)", verifier)
        self.assertNotRegex(verifier, r"(?i)[A-Z]:[/\\\\]Users[/\\\\]")

    def test_remove_path_handles_directory_symlink_without_traversal(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "target"
            target.mkdir()
            marker = target / "keep.txt"
            marker.write_text("keep", encoding="utf-8")
            link = root / "link"
            try:
                link.symlink_to(target, target_is_directory=True)
            except OSError:
                self.skipTest("directory symlinks unavailable in this environment")
            self.installer.remove_path(str(link))
            self.assertFalse(link.exists())
            self.assertTrue(marker.exists())


if __name__ == "__main__":
    unittest.main()
