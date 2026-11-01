---
title: The rank-two systems used by the proof
primary_topic: kl.reflection_combinatorics
---

A dihedral Coxeter system has two simple generators, and its reduced words alternate between them. Its nonempty Bruhat intervals have two vertices at each strict internal rank and a single vertex at each endpoint. A directed reflection edge is characterized by a positive odd length difference.

The geometric construction obtains such a system inside each root plane. A plane basis selects the two angular boundary roots; their reflections generate the induced group. Its intrinsic length and order are then related to the ambient graph through a least coset representative. These coordinates are the ones used for the local sheaf models.

The same rank-two structure has several outputs. It supplies interval geometry for [[node:kl.detail.diamond_reconstruction|reflection-edge reconstruction]], interpolation sections for flabby structure models, and the later-edge count used to compare reduced label products. [[node:kl.notes.relative_dihedral_transport|Full interval transport]] carries the necessary relative interval into the target system before the count is evaluated there.

The internal-rank flip also acts on full interval paths. The middle-descent slope test reverses every adjacent label comparison after the flip, and the resulting path involution proves the [[node:kl.dihedral.plane_path_reversal|plane-path reversal theorem]].

## Reading sequence

1. [[node:kl.coxeter.alternating_words]] — Define the two alternating word families.
2. [[node:kl.coxeter.dihedral_bruhat_order]] — Describe their Bruhat comparisons.
3. [[node:kl.dihedral.odd_reflection_edges]] — Identify reflection edges by parity.
4. [[node:kl.detail.plane_basis]] — Choose the geometric boundary roots.
5. [[node:kl.dihedral.induced_system]] — Construct the actual induced Coxeter system.
6. [[node:kl.dihedral.plane_coset_graph]] — Relate intrinsic and ambient edges.
7. [[node:kl.notes.relative_dihedral_transport]] — Transport a full relative interval.
8. [[node:kl.dihedral.interval_flip]] — Define the internal-rank vertex and edge involutions.
9. [[node:kl.dihedral.plane_path_reversal]] — Pair equal-length paths in the opposite schedules.
