"""Regression checks for the document builder and source index."""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import json
import unittest

from build_knowledge import Links, inspect_site
from tools.knowledge import lean_index


class NamespaceIndexTest(unittest.TestCase):
    def test_sibling_noncomputable_sections_preserve_namespace(self):
        source = """namespace OAI
section
namespace Example
noncomputable section
def first : Nat := 0
end
noncomputable section
theorem second : True := True.intro
end
end Example
end
namespace Following
def third : Nat := 1
end Following
end OAI
"""
        with TemporaryDirectory(prefix="combkl-doc-index-") as directory:
            root = Path(directory)
            (root / "Example.lean").write_text(source, encoding="utf-8")
            index = lean_index.index_lean_project(root)
        self.assertEqual(set(index.declarations), {
            "OAI.Example.first", "OAI.Example.second", "OAI.Following.third",
        })
        self.assertEqual(index.declarations["OAI.Example.second"].line, 8)
        self.assertEqual(index.warnings, [])


class PublishedHTMLTest(unittest.TestCase):
    def test_code_is_preserved_but_excluded_from_formula_text(self):
        parser = Links()
        parser.feed(
            '<script>const fake = "\\(bad\\)";</script>'
            '<pre><code>theorem t : 1 &lt; 2 := by\n  norm_num</code></pre>'
            '<p>Formula: \\(x &lt; y\\)</p><a href="next.html">Next page</a>'
        )
        self.assertEqual(parser.code_blocks, ["theorem t : 1 < 2 := by\n  norm_num"])
        visible = "".join(parser.text_parts)
        self.assertIn(r"\(x < y\)", visible)
        self.assertNotIn("bad", visible)
        self.assertNotIn("norm_num", visible)
        self.assertEqual(parser.targets, ["next.html"])

    def test_raw_wiki_reference_is_rejected(self):
        with TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text("<p>[[kl.some.definition]]</p>")
            with self.assertRaisesRegex(ValueError, "Unrendered node reference"):
                inspect_site(site, [], lambda n: n.primary_topic, lambda t: t)

    def test_graph_detail_links_are_checked_from_site_root(self):
        with TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text("<p>Notes</p>")
            payloads = site / "node_payloads"
            payloads.mkdir()
            (payloads / "example.json").write_text(
                json.dumps({"body_html": '<a href="missing.html">term</a>'})
            )
            with self.assertRaisesRegex(ValueError, "Broken local links"):
                inspect_site(site, [], lambda n: n.primary_topic, lambda t: t)

    def test_existing_but_wrong_definition_page_is_rejected(self):
        with TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "chapter").mkdir()
            node = SimpleNamespace(id="kl.term", kind="definition", primary_topic="chapter")
            (site / "chapter" / "kl_term.html").write_text("<p>Definition</p>")
            (site / "index.html").write_text(
                '<a class="definition-ref" data-node-id="kl.term" href="index.html">term</a>'
            )
            with self.assertRaisesRegex(ValueError, "Wrong definition destination"):
                inspect_site(site, [node], lambda n: n.primary_topic, lambda t: t)


if __name__ == "__main__":
    unittest.main()
