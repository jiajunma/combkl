"""Keyword reading guides are required, linked and explicitly reviewed."""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import hashlib
import json
import unittest

from build_knowledge import validate_keyword_guides


class KeywordGuideTest(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory(prefix="combkl-keyword-guide-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "keywords").mkdir()
        (self.root / "reviews").mkdir()
        self.nodes = [
            SimpleNamespace(id="book.definition", kind="definition", primary_topic="book.topic", tags=["topic"]),
            SimpleNamespace(id="book.result", kind="theorem", primary_topic="book.topic", tags=["topic"]),
        ]
        self.path = self.root / "keywords/topic.md"
        self.path.write_text(
            "---\ntitle: Definition and result\nprimary_topic: book.topic\n---\n\n"
            "The definition supplies the input used by the result.\n\n"
            "## Reading sequence\n\n"
            "1. [[node:book.definition]] — Define the object.\n"
            "2. [[node:book.result]] — Prove the consequence.\n",
            encoding="utf-8",
        )
        self.record = {"keyword": "topic", "status": "reviewed",
                       "reading_nodes": ["book.definition", "book.result"]}
        self.review()

    def review(self):
        self.record["content_sha256"] = hashlib.sha256(self.path.read_bytes()).hexdigest()
        (self.root / "reviews/keyword-guide-review.json").write_text(
            json.dumps({"guides": [self.record]}), encoding="utf-8"
        )

    def test_valid_definition_to_proof_route(self):
        report = validate_keyword_guides(self.nodes, self.root)
        self.assertEqual(report["keyword_guides_checked"], 1)
        self.assertEqual(report["keyword_reading_references_checked"], 2)

    def test_missing_keyword_guide_fails(self):
        self.nodes[0].tags.append("new-subject")
        with self.assertRaisesRegex(ValueError, "Missing keyword guides"):
            validate_keyword_guides(self.nodes, self.root)

    def test_unreviewed_change_fails(self):
        self.path.write_text(self.path.read_text() + "\nNew explanation.\n")
        with self.assertRaisesRegex(ValueError, "changed since review"):
            validate_keyword_guides(self.nodes, self.root)

    def test_unknown_node_reference_fails(self):
        self.path.write_text(self.path.read_text().replace("book.result", "book.missing"))
        self.review()
        with self.assertRaisesRegex(ValueError, "Unknown keyword-guide node"):
            validate_keyword_guides(self.nodes, self.root)

    def test_reading_route_requires_definition_and_theorem(self):
        self.record["reading_nodes"] = ["book.result"]
        self.review()
        with self.assertRaisesRegex(ValueError, "definition and theorem"):
            validate_keyword_guides(self.nodes, self.root)

    def test_index_without_exposition_fails(self):
        self.path.write_text(
            "---\ntitle: Definition and result\nprimary_topic: book.topic\n---\n\n"
            "## Reading sequence\n\n[[node:book.definition]] [[node:book.result]]\n"
        )
        self.review()
        with self.assertRaisesRegex(ValueError, "introductory exposition"):
            validate_keyword_guides(self.nodes, self.root)

    def test_unknown_scope_fails(self):
        self.path.write_text(self.path.read_text().replace("primary_topic: book.topic", "primary_topic: missing"))
        self.review()
        with self.assertRaisesRegex(ValueError, "keyword-guide topic"):
            validate_keyword_guides(self.nodes, self.root)
