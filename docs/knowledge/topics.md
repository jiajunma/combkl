# Blueprint organization

The blueprint has one root subject: **combinatorial invariance of Kazhdan–Lusztig polynomials**.

Its six chapter topics follow the paper:

| Topic | Paper section |
|---|---|
| kl.01_introduction | Introduction and conventions |
| kl.02_background | Real realizations and moment-graph sheaves |
| kl.03_dihedral | Dihedral intervals and transported reflection orders |
| kl.04_localization | Localization at a root plane |
| kl.05_edge_images | Comparison of edge images |
| kl.06_induction | Reciprocity and simultaneous induction |

Mathematical definitions and intermediate results live within these chapters. Their granularity follows the exposition and proof, rather than source-file boundaries.

Chapter reading introductions are reserved topics.md files under nodes/kl/. Individual entries use a flat canonical chapter directory such as nodes/kl.02_background/, as required by the current mdblueprint checker.

Stable node IDs need not repeat their current chapter path. The primary_topic and topics fields determine their place in the book. Their uses fields remain genuine mathematical dependencies.

Every entry points to Lean declarations and a paper location. Module imports and source inventories are supporting metadata, not a parallel classification of the subject.
