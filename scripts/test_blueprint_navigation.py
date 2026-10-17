from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.knowledge.definition_links import DefinitionLinks, link_definitions, rebase_payload_links
from tools.knowledge.context import KnowledgeContext
from tools.knowledge import renderer
from tools.knowledge.parser import scan_directory


class ConceptLinkTest(unittest.TestCase):
    def setUp(self):
        self.aliases = {
            "quadratic relation": ("kl.definitions.quadratic", "quadratic.html", "Quadratic relation"),
            "bar involution": ("kl.definitions.bar", "bar.html", "Bar involution"),
        }

    def test_terms_link_to_specific_definitions(self):
        out = link_definitions("<p>The quadratic relation and bar involution.</p>", self.aliases, renderer.TEX_MATH_RE)
        self.assertIn('href="quadratic.html"', out)
        self.assertIn('href="bar.html"', out)
        self.assertEqual(out.count('class="node-ref definition-ref"'), 2)

    def test_math_code_existing_links_and_wiki_are_preserved(self):
        original = '<h2>bar involution</h2><code>bar involution</code><a href="old">bar involution</a>' + r'<p>\(\text{bar involution}\)</p>[[node:x.y|bar involution]]'
        self.assertEqual(link_definitions(original, self.aliases, renderer.TEX_MATH_RE), original)

    def test_modal_links_are_relative_to_site_root(self):
        html = '<a href="../../kl/01_introduction/x.html">x</a><a href="https://github.com/a">source</a>'
        out = rebase_payload_links(html, "kl.02_background")
        self.assertIn('href="kl/01_introduction/x.html"', out)
        self.assertIn('href="https://github.com/a"', out)

    def test_longest_alias_wins(self):
        aliases = {"free cover": ("a", "a.html", "a"), "minimal free cover": ("b", "b.html", "b")}
        out = link_definitions("minimal free cover", aliases, renderer.TEX_MATH_RE)
        self.assertIn('href="b.html"', out)
        self.assertEqual(out.count("<a "), 1)

    def test_term_across_prose_line_break_is_linked(self):
        out = link_definitions("the quadratic\nrelation", self.aliases, renderer.TEX_MATH_RE)
        self.assertIn('href="quadratic.html"', out)
        self.assertIn(">quadratic\nrelation</a>", out)

    def test_word_boundaries_and_case(self):
        out = link_definitions("Quadratic Relation is not aquadratic relation", self.aliases, renderer.TEX_MATH_RE)
        self.assertEqual(out.count("<a "), 1)

    def test_linker_is_idempotent(self):
        once = link_definitions("quadratic relation", self.aliases, renderer.TEX_MATH_RE)
        self.assertEqual(link_definitions(once, self.aliases, renderer.TEX_MATH_RE), once)


class BlueprintNavigationIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1] / "docs" / "knowledge"
        self.nodes = scan_directory(self.root / "nodes")
        DefinitionLinks.load(self.root, self.nodes)

    def test_stable_id_uses_the_current_chapter(self):
        by_id = {n.id: n for n in self.nodes}
        html, missing = renderer._resolve_node_refs_in_html(
            "[[node:kl.notes.hecke_action|operators]]", by_id, "kl.02_hecke_polynomials"
        )
        self.assertFalse(missing)
        self.assertIn('href="kl_notes_hecke_action.html"', html)
        self.assertNotIn("../notes/", html)

    def test_users_example_is_linked_from_plain_prose(self):
        source = (self.root / "nodes" / "kl" / "02_hecke_polynomials" / "topics.md").read_text()
        self.assertIn("develops the operators, their quadratic relation, and the bar involution", source)
        html = renderer.render_topic(KnowledgeContext.load(self.root), "kl.02_hecke_polynomials")
        for node_id in ("hecke_operators", "hecke_quadratic_relation", "bar_involution"):
            self.assertIn(f'data-node-id="kl.definitions.{node_id}"', html)
            self.assertIn(f'href="kl_definitions_{node_id}.html"', html)

    def test_ambiguous_alias_is_rejected_before_rendering(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "concept-links.yml").write_text(
                "concepts:\n"
                "  - node: kl.definitions.bar_involution\n    terms: [operator]\n"
                "  - node: kl.definitions.hecke_operators\n    terms: [operator]\n"
            )
            with self.assertRaisesRegex(ValueError, "Ambiguous concept alias"):
                DefinitionLinks.load(root, self.nodes)

    def test_completed_development_has_no_admitted_entries(self):
        for node in self.nodes:
            expected = "proved" if node.kind == "theorem" else "formalized"
            self.assertEqual(node.status, expected, node.id)

    def test_each_entry_is_in_its_chapter_reading_sequence(self):
        for node in self.nodes:
            guide = self.root / "nodes" / Path(*node.primary_topic.split(".")) / "topics.md"
            self.assertIn("[[node:" + node.id + "]]", guide.read_text(), node.id)

    def test_published_proofs_match_their_exposition_review(self):
        from build_knowledge import validate_proof_walkthroughs
        result = validate_proof_walkthroughs(self.nodes)
        self.assertEqual(result["reviewed_theorem_walkthroughs"],
                         sum(node.kind == "theorem" for node in self.nodes))


if __name__ == "__main__":
    unittest.main()
