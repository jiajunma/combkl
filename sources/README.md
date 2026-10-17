# Original paper and Lean sources

This directory preserves the upstream materials used by the blueprint, knowledge base, and review work. Files inside openai-math/ retain their original paths and contents.

## Provenance

- Repository used by the review: [agoramachina/openai-math](https://github.com/agoramachina/openai-math).
- Fixed revision: adc7f1241b42e322a6451854ab7e4b4c146bf78a.
- Retrieved: October 17, 2026.
- Scope: 81 upstream files, including the complete paper directory, all 34 KL solution modules, the associated Comparator challenge/configuration, toolchain and dependency metadata, compatibility patches, and licences.
- File manifest: [openai-math.manifest.tsv](openai-math.manifest.tsv). These are Git blob hashes, not plain-content SHA-1 values.
- Licences: [repository licence](openai-math/LICENSE) and [Lean licence](openai-math/lean/LICENSE).

This is the relevant source snapshot rather than a mirror of the entire upstream repository. External dependencies and compiled caches are not included.

## Paper

- [PDF](openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf)
- [LaTeX entry point](openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/paper.tex)
- [All chapters, bibliography, and figures](openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/)

## Lean

The main declaration is OAI.KLInvariance.combinatorial_invariance in [Invariance.lean](openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean). The full [KazhdanLusztig directory](openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/) is included.

[KLInvariance.json](openai-math/lean/ComparatorChallenges/KLInvariance.json) distinguishes the challenge module from the solution module. The sorry in the [challenge specification](openai-math/lean/ComparatorChallenges/KLInvariance.lean) is a placeholder for the statement to be compared; the actual proof is supplied by the separate solution development.

The internal OAI imports of these 34 modules are present in this snapshot. Their direct external import is Mathlib.

## Toolchain metadata

- Lean: leanprover/lean4:v4.34.1.
- Mathlib revision: d13f23b723b8a846827a245b89c10fc7d3f11612.
- The original lakefile, dependency manifest, and patches are preserved. They belong to the larger upstream library, so this source selection is not a newly configured minimal independent Lake project.

Keep experiments and explanatory edits outside the original snapshot. The documentation builder checks every preserved file against the manifest before generating the blueprint.
