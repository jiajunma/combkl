---
id: kl.detail.boundary_pairing
title: Symmetric perfect pairings on the actual boundary sheaf
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.top_splitting
- kl.detail.indecomposable_boundary
- kl.detail.word_flabbiness
- kl.notes.tensor_pairing
- kl.notes.supported_pairings
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:1006
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Symmetric perfect pairings on the actual boundary sheaf

For the actual minimal-boundary sheaf \(B_b\) on \([1,b]\) in a finite-generator real realization, its global sections admit a symmetric, integral, support-orthogonal perfect pairing. If sections \(m,n\) are homogeneous of degrees \(i,j\), its value has degree
\[
i+j-\ell(b).
\]

*Proof.*

Choose a reduced word for \(b\). The normalized top stalk allows the boundary sheaf to split out of its word sheaf. The word module already carries an integral perfect duality obtained by iterating Frobenius tensor induction.

To descend this duality, use the split projector and its integral adjoint. The primitive-projector recognition identifies the appropriate dual summand and produces the canonical pairing on the boundary summand. Symmetry and support orthogonality are preserved by this construction. Simply restricting a perfect form to an arbitrary summand would not establish perfection, which is why the adjoint and recognition steps are needed.

Finally change coefficients from the symmetric algebra to polynomial coordinates and use graded uniqueness of the minimal-boundary sheaf. The pairing transfers to the actual chosen boundary sheaf with degree shift \(\ell(b)\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing`: [EdgeLocalization.lean:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).
