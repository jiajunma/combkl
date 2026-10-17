#!/usr/bin/env python3
"""Pin blueprint source links to a verified snapshot commit in combkl."""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "docs" / "knowledge"
WEB = "https://github.com/jiajunma/combkl"
UPSTREAM = "https://github.com/agoramachina/openai-math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/"
PREFIX = "sources/openai-math/"


def update_links(revision: str) -> int:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Use the complete 40-character combkl snapshot commit")
    tree = subprocess.check_output(["git", "ls-tree", "-rz", revision, "--", PREFIX], cwd=ROOT)
    blobs = {}
    for entry in tree.decode().split("\0"):
        if entry:
            metadata, path = entry.split("\t", 1)
            blobs[path] = metadata.split()[2]
    with (ROOT / "sources/openai-math.manifest.tsv").open(newline="") as handle:
        expected = {PREFIX + row["upstream_path"]: row["git_blob_sha1"]
                    for row in csv.DictReader(handle, delimiter="\t")}
    if blobs != expected:
        raise ValueError("The specified combkl commit does not contain the exact source snapshot")

    config_path = KNOWLEDGE / "mdblueprint.yml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    repository = next(r for r in config["lean"]["repositories"] if r["id"] == "openai-kl")
    prefixes = {UPSTREAM}
    if repository["web_url"] == WEB:
        prefixes.add(f"{WEB}/blob/{repository['revision']}/{PREFIX}")
    destination = f"{WEB}/blob/{revision}/{PREFIX}"
    changed = 0
    for path in sorted((KNOWLEDGE / "nodes").rglob("*.md")):
        old = path.read_text(encoding="utf-8")
        new = old
        for prefix in sorted(prefixes):
            new = new.replace(prefix, destination)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed += 1
    repository.update(web_url=WEB, revision=revision,
                      subdir=PREFIX + "lean/OAI/RepresentationTheory/KazhdanLusztig")
    config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("revision", help="Already published combkl commit holding the source snapshot")
    print(f"Updated {update_links(parser.parse_args().revision)} node files and the Lean repository configuration.")
