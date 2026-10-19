---
id: kl.word.set_tail_detection
title: Detection of coordinate images by their two tail projections
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.set_tail_maps
- kl.word.local_pair_maps
- kl.algebra.projective_range_splittings
- kl.detail.word_evaluation_injective
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottHeadSet_zero_iff
  - OAI.KLInvariance.TitsSpace.bottSetComponents_injective
  - OAI.KLInvariance.TitsSpace.bottHead_components_injective
  - OAI.KLInvariance.TitsSpace.bottSeed_zero_stable
  - OAI.KLInvariance.TitsSpace.bottSeed_zero_inter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:645
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadSet_zero_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:696
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetComponents_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:732
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHead_components_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:935
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSeed_zero_stable
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:960
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSeed_zero_inter
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the pointwise-to-set zero equivalence and both directions of the sU
    reindexing. Expanded descent, joint injectivity, whole-word tail detection and
    the two seed-vanishing consequences.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Detection of coordinate images by their two tail projections

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), a simple reflection \(s\), a tail word \(\mathbf t\), and \(U\subseteq W\). Let \(\mu,\nu\) be the two tail maps, with \(\nu\) taking values in the twist by \(\tau=\chi_s\).

For every \(m\in M_{s\mathbf t}\),
\[
p_U'(m)=0
\quad\Longleftrightarrow\quad
p_U(\mu(m))=0\ \text{and}\ p_{sU}(\nu(m))=0.
\]
Therefore the two image tail maps \(F_U,G_U\) are well defined and their product is injective.

If \(U=sU\) and \(p_U(n)=0\), then \(p_U'(1\otimes n)=0\). More generally, if \(p_U(n)=0\), the inserted tensor vanishes on \(U\cap sU\).

*Proof.*

### Step 1. Apply the single-weight criterion

The [[node:kl.word.local_pair_maps|local-pair theorem]] gives, for each \(x\),
\[
\pi_x^{s\mathbf t}(m)=0
\quad\Longleftrightarrow\quad
\pi_x^{\mathbf t}(\mu(m))=0
\quad\text{and}\quad
\pi_{sx}^{\mathbf t}(\nu(m))=0.
\]
A coordinate-image projection is zero exactly when each selected stalk coordinate is zero. Hence vanishing on every \(x\in U\) gives the first tail condition on \(U\).

The second condition is vanishing at every \(sx\) with \(x\in U\). This set is \(sU\), so it is exactly \(p_{sU}(\nu(m))=0\).

Conversely, the two tail conditions give both right-hand conditions for each \(x\in U\), proving that every selected new coordinate vanishes.

### Step 2. Descend both tail projections

The two composites \(p_U\mu\) and the twisted \(p_{sU}\nu\) are \(A\)-linear. Step 1 says that they kill \(\ker p_U'\).

The [[node:kl.algebra.projective_range_splittings|general descent theorem]] therefore gives unique linear maps \(F_U,G_U\) satisfying their defining formulas. In particular, their values are independent of the chosen word lift of an image vector.

### Step 3. Prove joint injectivity

Suppose \(F_U(z)=F_U(w)\) and \(G_U(z)=G_U(w)\). Choose a word lift \(m\) of \(z-w\), using surjectivity of \(p_U'\).

Linearity gives \(F_U(p_U'(m))=0\) and \(G_U(p_U'(m))=0\). Their defining formulas give both tail conditions in Step 1. Hence \(p_U'(m)=0\), so \(z-w=0\), proving \(z=w\).

### Step 4. Detect a whole word vector by its tails

If \(\mu(m)=0\) and \(\nu(m)=0\), Step 1 with \(U=W\) gives zero projection to every stalk. Every subexpression evaluation appears in the stalk at its weight, so all evaluations of \(m\) vanish. Full evaluation is injective, hence \(m=0\).

This is the source's bottHead_components_injective fact used in tensor splitting.

### Step 5. Apply the criterion to the inserted tensor

For \(1\otimes n\), both tail vectors are \(n\). If \(U=sU\) and \(p_U(n)=0\), both conditions of Step 1 hold, so the new projection on \(U\) vanishes.

Put \(K=U\cap sU\). This set is reflection-stable and contained in \(U\). If \(p_U(n)=0\), then \(p_K(n)=0\), so the stable-set result gives \(p_K'(1\otimes n)=0\). This is the insertion used in the common-kernel construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottHeadSet_zero_iff`: [IntegralPairings.lean:645](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L645).

`OAI.KLInvariance.TitsSpace.bottSetComponents_injective`: [IntegralPairings.lean:696](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L696).

`OAI.KLInvariance.TitsSpace.bottHead_components_injective`: [IntegralPairings.lean:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L732).

`OAI.KLInvariance.TitsSpace.bottSeed_zero_stable`: [IntegralPairings.lean:935](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L935).

`OAI.KLInvariance.TitsSpace.bottSeed_zero_inter`: [IntegralPairings.lean:960](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L960).
