---
id: kl.detail.boundary_pairing
title: Symmetric perfect pairings on the actual boundary sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.top_splitting
- kl.detail.word_flabbiness
- kl.detail.word_evaluation_injective
- kl.notes.tensor_pairing
- kl.word.pairing_degree
- kl.sheaves.word_adjoint_descent
- kl.sheaves.adjoint_boundary_recognition
- kl.sheaves.canonical_adjoint_comparison
- kl.sheaves.image_sections
- kl.sheaves.adjoint_summand_duality
- kl.word.support_duality
- kl.sheaves.boundary_coefficient_transport
- kl.sheaves.pairing_transport
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply
  - OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing_word
  - OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:1006
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:906
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:977
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing_word
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:988
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing
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

Fix a Coxeter system with finitely many simple generators, an element \(b\), and a basis of the real extended realization \(V\). Let
\[
A=\mathbb R[X_1,\ldots,X_N]
\]
be the resulting polynomial coefficient algebra, with variables in degree one, and let \(B_A\) be the chosen normalized boundary sheaf on \([1,b]\).

Its global section module has an \(A\)-bilinear symmetric perfect pairing with support orthogonality and degree shift \(\ell(b)\):
\[
\langle\Gamma(B_A)_i,\Gamma(B_A)_j\rangle
\subseteq A_{i+j-\ell(b)}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the boundary duality.**

**OpenAI notes:** The normalization proof uses the normalized self-dual projective and the cited moment-graph/Soergel equivalence to relate the stalk and lower-support layer, before translating grading conventions. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word pairing is constructed by tensor induction. Supported weight submodules prove adjoint kernel preservation, which descends the adjoint to a graded sheaf map. The adjoint image is dual to the original boundary summand; primitive recognition and the canonical comparison isomorphism produce its perfect symmetric pairing. [BalancedPairings:717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L717), [EdgeLocalization:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833), [EdgeLocalization:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L906), [EdgeLocalization:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).

**Role in the proof:** The proof follows the integral adjoint, image-section duality, primitive recognition, and canonical-comparison maps. The trace lowers degree once per word letter. Coefficient transport and a boundary-recognition isomorphism deliver the pairing on the chosen polynomial-coordinate sheaf.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the symmetric-coefficient boundary summand

Write \(R=\operatorname{Sym}_{\mathbb R}(V)\), with the same degree-one grading, and choose a reduced word \(\mathbf s\) for \(b\). Its length is \(\ell(b)\).

Let \(B_R\) be the normalized boundary sheaf over \(R\), and let \(W\) be the graded word sheaf of \(\mathbf s\). The word theorems supply free stalks, the upper-quotient rule, flabbiness, and global generation for \(W\). Its top stalk is \(R\) in degree zero.

The normalized top identifications and the [[node:kl.detail.top_splitting|top-splitting theorem]] give
\[
i:B_R\to W,\qquad p:W\to B_R,\qquad pi=1.
\]
The word module \(M=M_{\mathbf s}\) is isomorphic to \(\Gamma(W)\), by the word lifting theorem and injectivity of full evaluation. We use this identification for the induced maps on sections, writing
\(i:\Gamma(B_R)\to M\) and \(p:M\to\Gamma(B_R)\).

The tensor construction gives a symmetric perfect pairing \(D\) on \(M\). The [[node:kl.word.pairing_degree|word-degree theorem]] gives its shift \(|\mathbf s|=\ell(b)\).

### Step 2. Construct and recognize the adjoint image

The sheaf projector \(e=ip\) induces the module projector \(F=ip\) on \(M\). The integral adjoint
\[
F^*=D^{-1}F^\vee D
\]
descends to a graded sheaf projector \(e^*\), by the supported-stalk annihilator and quotient-descent argument.

Let \(C=\operatorname{im}e^*\), with inclusion \(j:C\to W\) and projection \(q:W\to C\). The [[node:kl.sheaves.adjoint_boundary_recognition|adjoint-image recognition theorem]] verifies its inherited free stalks, upper quotients, flabbiness, global generation, primitive identity, and normalized top, and gives \(C\simeq B_R\).

The [[node:kl.sheaves.canonical_adjoint_comparison|canonical-comparison theorem]] proves that the specified map
\[
h=qi:B_R\xrightarrow{\sim}C
\]
is an isomorphism. Its inclusion satisfies \(jh=e^*i\).

### Step 3. Identify the adjoint-image sections with the dual

The [[node:kl.sheaves.image_sections|image-section theorem]] identifies
\[
\Gamma(C)\simeq\operatorname{im}F^*.
\]
For the split module maps \(i,p\), the [[node:kl.sheaves.adjoint_summand_duality|adjoint-summand theorem]] gives a perfect pairing between \(\operatorname{im}F^*\) and \(\Gamma(B_R)\):
\[
Q(c,n)=\langle j(c),i(n)\rangle_M.
\]
Here both included sections are viewed as word elements.

Its associated linear isomorphism is \(\Gamma(C)\to\Gamma(B_R)^*\). To represent a functional \(\lambda\), first form \(\lambda\circ p\) on \(M\), then take \(D^{-1}(\lambda\circ p)\). The [[node:kl.sheaves.adjoint_summand_duality|adjoint-summand theorem]] places this element in \(\operatorname{im}F^*\) and proves uniqueness.

### Step 4. Pull back through the canonical comparison

Define
\[
P(m,n)=Q(h(m),n),\qquad m,n\in\Gamma(B_R).
\]
The map \(h\) is a section isomorphism and the map associated to \(Q\) is an isomorphism to the dual. Their composite proves perfection of \(P\).

The canonical formula identifies this pairing explicitly:
\[
\begin{aligned}
P(m,n)
&=\langle F^*i(m),i(n)\rangle_M\\
&=\langle i(m),Fi(n)\rangle_M\\
&=\langle i(m),i(n)\rangle_M.
\end{aligned}
\]
The last equality follows from \(Fi=ipi=i\). Symmetry of the word form therefore gives symmetry of \(P\).

### Step 5. Verify the degree and support equations

The inclusion \(i\) preserves degree. For inputs of degrees \(r,s\), the displayed formula and the [[node:kl.word.pairing_degree|word-degree theorem]] give
\[
P(m,n)\in R_{r+s-\ell(b)}.
\]

If \(m\) is supported at a vertex \(x\), the included section has zero value at every other vertex because each inclusion component is linear. If \(n_x=0\), its included section also has zero \(x\)-value. Word support orthogonality gives \(P(m,n)=0\). Symmetry gives the right support equation as well.

Thus \(P\) is a symmetric perfect support-orthogonal section pairing over \(R\).

### Step 6. Transfer the result to the chosen polynomial sheaf

The chosen basis gives a graded algebra isomorphism
\[
\varphi:R\xrightarrow{\sim}A.
\]
It sends every symmetric root label to the corresponding polynomial label. The [[node:kl.sheaves.boundary_coefficient_transport|coefficient-transport recognition theorem]] gives a graded sheaf isomorphism
\[
\psi:B_A\xrightarrow{\sim}{}^\varphi B_R.
\]

Transport \(P\) along \(\varphi\), then pull it back along \(\psi\). Explicitly, if \(\overline\psi(m)\) denotes the underlying \(R\)-section corresponding to \(\psi(m)\), set
\[
\langle m,n\rangle_A
=\varphi\!\left(P(\overline\psi(m),\overline\psi(n))\right).
\]
The [[node:kl.sheaves.pairing_transport|pairing-transport theorem]] proves perfection, symmetry, both support equations, and preservation of the shift. This produces the required pairing on the actual chosen polynomial-coordinate boundary sheaf \(B_A\).

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.boundarySheaf_symmetricPairing`: [EdgeLocalization.lean:1006](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L1006).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso`: [EdgeLocalization.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833).

`OAI.KLInvariance.TitsSpace.bottCanonicalPerfectPairing_apply`: [EdgeLocalization.lean:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L906).

`OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing_word`: [EdgeLocalization.lean:977](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L977).

`OAI.KLInvariance.TitsSpace.symmetricBoundarySheaf_symmetricPairing`: [EdgeLocalization.lean:988](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L988).
