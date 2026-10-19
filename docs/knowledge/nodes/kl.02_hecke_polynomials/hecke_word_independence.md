---
id: kl.hecke.word_independence
title: Cyclicity of the right action and reduced-word independence
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.word_actions
- kl.hecke.commutation
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.leftWord_one
  - OAI.KLInvariance.Hecke.rightWord_one
  - OAI.KLInvariance.Hecke.commuting_ext
  - OAI.KLInvariance.Hecke.leftWord_independent
  - OAI.KLInvariance.Hecke.standardUnit_word
  - OAI.KLInvariance.Hecke.standardUnit_simple_mul
  - OAI.KLInvariance.Hecke.standardUnit_mul_simple
  - OAI.KLInvariance.HeckeQ.leftWord_one
  - OAI.KLInvariance.HeckeQ.rightWord_one
  - OAI.KLInvariance.HeckeQ.commuting_ext
  - OAI.KLInvariance.HeckeQ.leftWord_independent
  - OAI.KLInvariance.HeckeQ.standardUnit_word
  - OAI.KLInvariance.HeckeQ.standardUnit_simple_mul
  - OAI.KLInvariance.HeckeQ.standardUnit_mul_simple
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:139
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftWord_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:161
    format: lean-location
    note: OAI.KLInvariance.Hecke.rightWord_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:191
    format: lean-location
    note: OAI.KLInvariance.Hecke.commuting_ext
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:218
    format: lean-location
    note: OAI.KLInvariance.Hecke.leftWord_independent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:256
    format: lean-location
    note: OAI.KLInvariance.Hecke.standardUnit_word
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:272
    format: lean-location
    note: OAI.KLInvariance.Hecke.standardUnit_simple_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:286
    format: lean-location
    note: OAI.KLInvariance.Hecke.standardUnit_mul_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:626
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftWord_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:648
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.rightWord_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:678
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.commuting_ext
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:705
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.leftWord_independent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:743
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.standardUnit_word
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:759
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.standardUnit_simple_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:773
    format: lean-location
    note: OAI.KLInvariance.HeckeQ.standardUnit_mul_simple
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual coefficient hypotheses, conventions and source proof retained?
  verdict: Read the parallel normalized/unnormalized cyclic-action proofs. Expanded
    reduced-tail induction, inversion in the right action, commuting-map extensionality
    and the standard ascent products.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Cyclicity of the right action and reduced-word independence

In either Hecke convention, a reduced word \(\omega\) with product \(w\) satisfies
\[
L_\omega e_1=e_w,\qquad D_\omega e_1=e_{w^{-1}}.
\]
If two linear operators commute with every right simple operator and agree on \(e_1\), they agree everywhere. Consequently two reduced words for the same \(w\) define the same left operator.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Algebraic construction behind the polynomial conventions.**

**OpenAI notes:** The conventions specify the ordinary R descent recurrence. The reflection-order path theorem introduces the normalized family through path counting and states its square-parameter relation to ordinary R. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The regular operators are built from Coxeter length. Left/right commutation and the cyclic identity vector prove reduced-word independence. Inverse operators define R-values; their recurrence proves polynomiality, and a second matching-recurrence argument proves signed parameter reciprocity. [Hecke:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L705), [Hecke:1000](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L1000), [OrdinaryR:31](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean#L31), [Dihedral:440](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L440).

**Role in the proof:** The KB develops these algebraic constructions before the geometric path formula. The recurrence and inverse-parameter coefficient identities used by the character argument follow from the constructed operators.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Evaluate a reduced left word

Induct on the number of letters. The empty word acts as the identity and has product \(1\).

Write a nonempty reduced word as \(s\omega\), with tail product \(u\). The tail is reduced, and reducedness of the whole word gives \(\ell(su)=\ell(u)+1\). By induction, \(L_\omega e_1=e_u\). The ascent branch in either convention gives
\[
L_{s\omega}e_1=L_s e_u=e_{su}.
\]

### Step 2. Evaluate the right word

Use the same induction. The tail gives \(D_\omega e_1=e_{u^{-1}}\). Inversion preserves length, so
\[
\ell(u^{-1}s)=\ell(su)=\ell(u)+1=\ell(u^{-1})+1.
\]
The right operation is therefore an ascent:
\[
D_{s\omega}e_1=D_s e_{u^{-1}}=e_{u^{-1}s}=e_{(su)^{-1}}.
\]

Every \(w\) is reached from \(e_1\) by choosing a reduced word for \(w^{-1}\) and applying its right word. This is the cyclicity of the right action: the orbit operations applied to one vector span the module.

### Step 3. Determine commuting maps from the cyclic vector

Let \(F,G\) commute with all \(D_t\), and suppose \(F(e_1)=G(e_1)\). Commuting past each letter makes them commute with every \(D_\omega\).

For a reduced word \(\omega\) of \(w^{-1}\), Step 2 gives
\[
F(e_w)=F(D_\omega e_1)
=D_\omega F(e_1)
=D_\omega G(e_1)
=G(D_\omega e_1)=G(e_w).
\]
Thus the maps agree on the basis, hence everywhere.

### Step 4. Compare reduced left words

Every \(L_s\) commutes with every \(D_t\). Moving \(D_t\) past a product one factor at a time shows that each \(L_\omega\) also commutes with it.

If \(\omega,\eta\) are reduced with the same product \(w\), Step 1 gives
\(L_\omega e_1=e_w=L_\eta e_1\).
Step 3 now yields \(L_\omega=L_\eta\). Since both are units in the inverse-operator setting, their inverses agree as well.

### Step 5. Recover the standard ascent identities

When \(\ell(sw)=\ell(w)+1\), prepend \(s\) to any reduced word for \(w\). The resulting word is reduced for \(sw\), so word independence gives \(U_{sw}=L_sU_w\).

Appending \(s\) in a right ascent gives \(U_{ws}=U_wL_s\). The empty word gives \(U_1=I\), and Step 1 gives \(U_we_1=e_w\).

In a rank-two system, alternating reduced expressions of a common element therefore yield equal alternating operator products. This is the braid relation as a consequence of the regular action construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Hecke.leftWord_one`: [Hecke.lean:139](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L139).

`OAI.KLInvariance.Hecke.rightWord_one`: [Hecke.lean:161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L161).

`OAI.KLInvariance.Hecke.commuting_ext`: [Hecke.lean:191](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L191).

`OAI.KLInvariance.Hecke.leftWord_independent`: [Hecke.lean:218](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L218).

`OAI.KLInvariance.Hecke.standardUnit_word`: [Hecke.lean:256](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L256).

`OAI.KLInvariance.Hecke.standardUnit_simple_mul`: [Hecke.lean:272](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L272).

`OAI.KLInvariance.Hecke.standardUnit_mul_simple`: [Hecke.lean:286](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L286).

`OAI.KLInvariance.HeckeQ.leftWord_one`: [Hecke.lean:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L626).

`OAI.KLInvariance.HeckeQ.rightWord_one`: [Hecke.lean:648](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L648).

`OAI.KLInvariance.HeckeQ.commuting_ext`: [Hecke.lean:678](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L678).

`OAI.KLInvariance.HeckeQ.leftWord_independent`: [Hecke.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L705).

`OAI.KLInvariance.HeckeQ.standardUnit_word`: [Hecke.lean:743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L743).

`OAI.KLInvariance.HeckeQ.standardUnit_simple_mul`: [Hecke.lean:759](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L759).

`OAI.KLInvariance.HeckeQ.standardUnit_mul_simple`: [Hecke.lean:773](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L773).
