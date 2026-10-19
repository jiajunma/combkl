---
id: kl.sheaves.word_section_equivalence
title: A reduced tensor word realizes all global sections
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_sheaf
- kl.word.weight_support
- kl.word.scaled_coordinate_lifts
- kl.word.prime_character_class
- kl.word.class_lift_assembly
- kl.algebra.projective_local_membership
- kl.detail.word_evaluation_injective
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottVertexProjection
  - OAI.KLInvariance.TitsSpace.bottVertexProjection_injective
  - OAI.KLInvariance.TitsSpace.bottVertexProjection_stable
  - OAI.KLInvariance.TitsSpace.bottVertexProjection_scaled
  - OAI.KLInvariance.TitsSpace.bottSection_pair_lift
  - OAI.KLInvariance.TitsSpace.bottSection_prime_lift
  - OAI.KLInvariance.TitsSpace.bottSection_local_denominator
  - OAI.KLInvariance.TitsSpace.bottSection_surjective
  - OAI.KLInvariance.TitsSpace.bottSectionEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:174
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottVertexProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:179
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottVertexProjection_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:185
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottVertexProjection_stable
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:194
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottVertexProjection_scaled
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:212
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_pair_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:231
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_prime_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:262
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_local_denominator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:277
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:292
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSectionEquiv
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the BalancedPairings vertex image proof, including its free-image
    route, interval class lifting and free-target denominator removal. Kept the reduced
    word and full interval hypotheses, separate from upper-image projectivity.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A reduced tensor word realizes all global sections

Fix a finite-generator Coxeter system and a reduced word \(\mathbf t\) with product \(b\). Let \(S\) be its pair-projection sheaf on \(I=[1,b]\), over the symmetric coefficient algebra \(A\).

The section map
\[
\Psi:M_{\mathbf t}\longrightarrow\Gamma(S),\qquad
\Psi(m)=(\pi_x(m))_{x\in I}
\]
is an \(A\)-linear isomorphism. Thus every compatible global assignment is realized by a unique word vector.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove injectivity of the full vertex projection

Let
\[
E=\prod_{x\in I}M_{\mathbf t}^x,\qquad
v:M_{\mathbf t}\to E,\quad v(m)=(\pi_x(m))_x,
\]
and put \(L=\operatorname{im}v\).

Every subexpression weight of the reduced word lies in \(I\). If \(v(m)=0\), the stalk at each such weight is zero on \(m\), so every subexpression evaluation of \(m\) vanishes. Full evaluation is injective, giving \(m=0\).

Thus \(v\) identifies the finite free word module with \(L\), making \(L\) free. The same argument proves injectivity of \(\Psi\).

### Step 2. Supply a nonzero scalar lift of any vertex assignment

For a tuple \(z\in E\), define
\[
c_\varepsilon=(z_{w(\varepsilon)})_\varepsilon.
\]
This is defined for every subexpression because its weight lies in \(I\). [[node:kl.word.scaled_coordinate_lifts|Scaled coordinate lifting]] gives a word vector whose evaluations are
\(\Delta_{\mathbf t}c_\varepsilon\). Its vertex projections are therefore
\(\Delta_{\mathbf t}z_x\) at every \(x\), so
\[
\Delta_{\mathbf t}z\in L,\qquad \Delta_{\mathbf t}\ne0.
\]

### Step 3. Supply a prime-local scalar lift of a section

Now suppose \(z\) is a compatible global section, and fix a prime \(p\).
The interval \(I\) is finite. Its coefficient weights \(x\mapsto\chi_x(a)\) stabilize \(L\), since right multiplication on the word module has those projection scalars.

A singleton residue class lifts by stalk surjectivity. A class with two distinct weights is a reflection pair by the [[node:kl.word.prime_character_class|prime-character theorem]]. The two lengths differ, so compatibility on the corresponding upward interval edge gives one word vector realizing both class values.

The [[node:kl.word.class_lift_assembly|class-lift assembly theorem]] therefore supplies \(d_p\) with
\[
p\nmid d_p,\qquad d_pz\in L.
\]
This is the source's bottSection_local_denominator argument on the finite interval itself.

### Step 4. Remove the scalar multipliers

The coefficient algebra is a polynomial UFD over \(\mathbb R\). Each stalk, and therefore \(E\), is torsion-free. Step 1 makes \(L\) a free submodule of \(E\); Step 2 gives its generic multiplier, and Step 3 gives the multiplier avoiding each prime.

Apply the [[node:kl.algebra.projective_local_membership|free-target prime-denominator membership theorem]]. It gives \(z\in L\), so some \(m\in M_{\mathbf t}\) has \(v(m)=z\). Because both tuples are compatible, this is precisely \(\Psi(m)=z\). Thus \(\Psi\) is surjective.

### Step 5. Obtain the isomorphism and its one-letter form

The section map is linear, injective and surjective, so it is the isomorphism bottSectionEquiv.

For one letter, it sends the basis coordinates \(u,v\) of
\(u(1\otimes1)+v(1\otimes\alpha)\) to
\[
(f,g)=(u+\alpha v,u-\alpha v).
\]
A compatible pair has \(f-g\in\alpha A\), and its inverse coordinates are
\[
u=(f+g)/2,\qquad v=(f-g)/(2\alpha).
\]
The divisibility condition makes the second coordinate an element of \(A\). This is the explicit instance of the general section-realization isomorphism.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottVertexProjection`: [BalancedPairings.lean:174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L174).

`OAI.KLInvariance.TitsSpace.bottVertexProjection_injective`: [BalancedPairings.lean:179](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L179).

`OAI.KLInvariance.TitsSpace.bottVertexProjection_stable`: [BalancedPairings.lean:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L185).

`OAI.KLInvariance.TitsSpace.bottVertexProjection_scaled`: [BalancedPairings.lean:194](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L194).

`OAI.KLInvariance.TitsSpace.bottSection_pair_lift`: [BalancedPairings.lean:212](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L212).

`OAI.KLInvariance.TitsSpace.bottSection_prime_lift`: [BalancedPairings.lean:231](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L231).

`OAI.KLInvariance.TitsSpace.bottSection_local_denominator`: [BalancedPairings.lean:262](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L262).

`OAI.KLInvariance.TitsSpace.bottSection_surjective`: [BalancedPairings.lean:277](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L277).

`OAI.KLInvariance.TitsSpace.bottSectionEquiv`: [BalancedPairings.lean:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292).
