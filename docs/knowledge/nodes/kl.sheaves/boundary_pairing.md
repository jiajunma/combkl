---
id: kl.detail.boundary_pairing
title: Symmetric perfect pairings on the actual boundary sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
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
- kl.sheaves.word_adjoint_descent
- kl.sheaves.image_sections
- kl.sheaves.adjoint_summand_duality
- kl.sheaves.projector_image
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

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the boundary duality.**

**OpenAI notes:** The normalization proof uses the normalized self-dual projective and the cited moment-graph/Soergel equivalence to relate the stalk and lower-support layer, before translating grading conventions. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word pairing is constructed by tensor induction. Supported weight submodules prove adjoint kernel preservation, which descends the adjoint to a graded sheaf map. The adjoint image is dual to the original boundary summand; primitive recognition and the canonical comparison isomorphism produce its perfect symmetric pairing. [BalancedPairings:717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L717), [EdgeLocalization:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833), [EdgeLocalization:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L906), [EdgeLocalization:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).

**Role in the proof:** The proof below follows the integral adjoint, image-section, recognition, and canonical-comparison maps. Homogeneous inverse calculations then determine the stalk–costalk degree shift.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Obtain the actual normalized summand of a word sheaf

Choose a reduced word \(\mathbf s\) for \(b\). Its word sheaf has a rank-one top stalk with the same normalization as the boundary sheaf \(B\). The top-splitting theorem supplies sheaf maps
\(i:B\to W\), \(p:W\to B\), with \(pi=1\). Put \(e=ip\), so \(e^2=e\) and its image is the specified boundary summand.

The word module identifies with all global sections of \(W\): surjectivity follows from the word lifting theorem, and injectivity follows from the injective full weight evaluation. The word pairing is a symmetric integral perfect pairing on this module \(M\); write \(D:M\to M^*\) for its pairing isomorphism and \(\pi_x\) for its stalk projections. We also write \(i,p\) for the induced maps on global sections, using the section equivalence to regard the word sections as elements of \(M\).

### Step 2. Descend the integral adjoint through the actual stalk projections

Let \(F\) be the word-module endomorphism induced by the sheaf projector \(e\). The integral adjoint is
\[
F^*=D^{-1}F^\vee D,\qquad
\langle F^*m,n\rangle=\langle m,Fn\rangle.
\]
The adjoint identities imply \((F^*)^2=F^*\), and the homogeneous-representative theorem makes \(F^*\) degree zero.

The descent in [[node:kl.sheaves.word_adjoint_descent]] uses the supported weight submodules \(S_x\). The original sheaf map acts componentwise, so \(F(S_x)\subseteq S_x\). If \(\pi_x(m)=0\) and \(s\in S_x\), symmetry gives
\[
\langle s,F^*m\rangle=\langle Fs,m\rangle=0.
\]
The projection-kernel annihilator theorem therefore gives \(\pi_x(F^*m)=0\). This makes
\[
e_x^*(\pi_x(m))=\pi_x(F^*m)
\]
well defined. Descent through each pair-projection quotient gives the edge maps and both restriction squares. The resulting \(e^*\) is a graded sheaf endomorphism.

Its vertex maps are idempotent by lifting a stalk vector to \(M\) and applying \((F^*)^2=F^*\). The lower edge maps of the pair-projection sheaf are surjective, so their commuting squares transfer the same idempotence to the edge components. Thus \(e^*\) is a sheaf projector.

### Step 3. Recognize its image as another copy of B

Let \(C=\operatorname{im}e^*\) be the image sheaf, with the componentwise inclusion and projection. It is a sheaf direct summand of \(W\), so it inherits the quotient rule, flabbiness, and global generation. Its stalks are finite graded projective, hence graded free.

The projector \(e\) is primitive because its image \(B\) is indecomposable. Adjoint reverses composition and is involutive, so a nontrivial projector splitting \(e^*\) would, after taking adjoints, split \(e\). Hence \(e^*\) is primitive. At the top, both projectors are the identity on the normalized rank-one stalk. Top splitting places a copy of \(B\) inside \(C\); primitivity and the nonzero top force its complementary summand to be zero. Therefore \(C\simeq B\).

### Step 4. Prove that the canonical comparison map is an isomorphism

Write \(j:C\to W\) and \(q:W\to C\) for the adjoint-image splitting. Define the canonical map \(h=qi:B\to C\); after inclusion in \(W\), its value is \(e^*i(v)\).

At the top vertex, \(ip\) and \(jq\) are both the identity on the word stalk. The map \(g=pj\) at that vertex satisfies
\[
gh=pjqi=pi=1,\qquad hg=qipj=qj=1.
\]
Hence \(h\) is bijective at the top. Compose \(h\) with any recognition isomorphism \(C\simeq B\). The composite is a boundary-sheaf endomorphism invertible at the top, hence invertible everywhere by the downward minimal-cover argument. Consequently \(h\) itself is an isomorphism.

### Step 5. Identify the perfect pairing through the adjoint image

The image-section theorem [[node:kl.sheaves.image_sections]] identifies
\(\Gamma(C)\) with \(\operatorname{im}F^*\). The original splitting similarly identifies \(\Gamma(B)\) with \(\operatorname{im}F\) in the word module.

The adjoint-summand theorem [[node:kl.sheaves.adjoint_summand_duality]] gives a linear isomorphism
\[
\Gamma(C)\xrightarrow{\sim}\Gamma(B)^*,\qquad
c\longmapsto\bigl(w\mapsto\langle c,i(w)\rangle\bigr).
\]
Explicitly, a functional \(\lambda\) on \(\Gamma(B)\) extends to \(\lambda\circ p\) on \(M\). Its perfect-pairing representative \(D^{-1}(\lambda\circ p)\) lies in \(\operatorname{im}F^*\), and supplies the inverse map.

Compose this duality with the section isomorphism induced by the canonical comparison \(h\) from Step 4. For \(v,w\in\Gamma(B)\), its value is
\[
\begin{aligned}
\langle h(v),i(w)\rangle
&=\langle F^*i(v),i(w)\rangle\\
&=\langle i(v),Fi(w)\rangle\\
&=\langle i(v),i(w)\rangle.
\end{aligned}
\]
The last equality uses \(Fi=ipi=i\). The resulting perfect pairing is therefore the word pairing evaluated on the two included sections. Symmetry of the word form gives symmetry on \(\Gamma(B)\).

### Step 6. Preserve grading, support, and coefficient coordinates

All inclusion, projection, and comparison maps have degree zero. The word pairing has degree shift \(\ell(b)\), so the restricted pairing has that same shift. If \(v\) is supported at \(x\), its included section is also supported at \(x\), since the component maps send zero to zero. If \(w_x=0\), its inclusion still has zero \(x\)-coordinate. Word support orthogonality therefore gives the first orthogonality equation for the restricted form. Symmetry gives the second. Finally transfer along the symmetric-algebra-to-polynomial-coordinate isomorphism and the graded boundary-sheaf isomorphism. These isomorphisms preserve all three properties, yielding the stated pairing on the actual chosen polynomial-coordinate boundary sheaf.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing`: [EdgeLocalization.lean:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso`: [EdgeLocalization.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833).

`OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply`: [EdgeLocalization.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L906).
