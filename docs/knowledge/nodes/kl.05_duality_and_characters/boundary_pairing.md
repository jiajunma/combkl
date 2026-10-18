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
- kl.notes.graded_projective_free
- kl.detail.integral_adjoints
- kl.detail.adjoint_primitivity
- kl.detail.primitive_summand
- kl.detail.word_evaluation_injective
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply
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
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:906
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply
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

### Step 1. Obtain the actual normalized summand of a word sheaf

Choose a reduced word \(\mathbf s\) for \(b\). Its word sheaf has a rank-one top stalk with the same normalization as the boundary sheaf \(B\). The top-splitting theorem supplies sheaf maps
\(i:B\to W\), \(p:W\to B\), with \(pi=1\). Put \(e=ip\), so \(e^2=e\) and its image is the specified boundary summand.

The word module identifies with all global sections of \(W\): surjectivity follows from the word lifting theorem, and injectivity follows from the injective full weight evaluation. The word pairing is a symmetric integral perfect pairing on this module \(M\).

### Step 2. Define the integral adjoint and descend it to the sheaf

Perfection defines a unique \(A\)-linear adjoint \(e^*\) by
\(\langle e^*m,n\rangle=\langle m,en\rangle\).
It is defined over \(A\), not merely over its fraction field. The equation implies \((e^*)^2=e^*\).

Balance of the word pairing makes the adjoint commute with the right coefficient action, and homogeneity makes it degree zero. This preserves the kernels of weight projections: over the fraction field, different weights have distinct coefficient characters, so a commuting map cannot have a component between different weight blocks. The integral target stalks are torsion-free, so vanishing after this localization is vanishing before localization. The map therefore descends to stalk maps. Applying it simultaneously at both endpoints preserves the pair-projection relation, giving compatible edge maps. Thus \(e^*\) is an integral graded sheaf projector.

### Step 3. Recognize its image as another copy of B

Let \(C=\operatorname{im}e^*\). It is a sheaf direct summand of \(W\), so it inherits the quotient rule, flabbiness, and global generation. Its stalks are finite graded projective, hence graded free.

The projector \(e\) is primitive because its image \(B\) is indecomposable. Adjoint reverses composition and is involutive, so a nontrivial projector splitting \(e^*\) would, after taking adjoints, split \(e\). Hence \(e^*\) is primitive. At the top, both projectors are the identity on the normalized rank-one stalk. Top splitting places a copy of \(B\) inside \(C\); primitivity and the nonzero top force its complementary summand to be zero. Therefore \(C\simeq B\).

### Step 4. Prove that the canonical comparison map is an isomorphism

The canonical map is \(h:B\to C\), \(h(v)=e^*i(v)\), not an arbitrary chosen isomorphism. At the top it is bijective, since both projectors act there as the identity. Compose \(h\) with any recognition isomorphism \(C\simeq B\). The composite is a boundary-sheaf endomorphism invertible at the top, hence invertible everywhere by the downward minimal-cover argument. Consequently \(h\) itself is an isomorphism.

### Step 5. Identify the perfect pairing and prove symmetry

Pairing on \(M\) gives a perfect pairing between \(C=\operatorname{im}e^*\) and \(B=\operatorname{im}e\). To see surjectivity onto \(B^*\), extend a functional by \(p\) to \(M\), and use perfection on \(M\); its representative is fixed by \(e^*\). Injectivity follows because a vector in \(\operatorname{im}e^*\) pairing to zero with \(\operatorname{im}e\) pairs to zero with all of \(M\).

Pull this perfect pairing back through \(h\). For \(v,w\in B\),
\[
\langle h(v),i(w)\rangle
=\langle e^*i(v),i(w)\rangle
=\langle i(v),ei(w)\rangle
=\langle i(v),i(w)\rangle.
\]
Thus it is the restricted word form, and is symmetric. Perfection was proved using Step 4; it was not assumed for an arbitrary summand.

### Step 6. Preserve grading, support, and coefficient coordinates

All inclusion, projection, and comparison maps have degree zero. The word pairing has degree shift \(\ell(b)\), so the restricted pairing has that same shift. Disjoint vertex supports remain disjoint in the word coordinates, giving support orthogonality. Finally transfer along the symmetric-algebra-to-polynomial-coordinate isomorphism and the graded boundary-sheaf isomorphism. These isomorphisms preserve all three properties, yielding the stated pairing on the actual chosen polynomial-coordinate boundary sheaf.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing`: [EdgeLocalization.lean:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso`: [EdgeLocalization.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833).

`OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply`: [EdgeLocalization.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L906).
