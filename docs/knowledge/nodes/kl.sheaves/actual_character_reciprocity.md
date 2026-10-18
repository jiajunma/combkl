---
id: kl.duality.actual_character_reciprocity
title: R-reciprocity for the actual boundary-sheaf character
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.bott_character_decomposition
- kl.duality.stalk_character
- kl.foundations.rtilde
- kl.notes.character_cancellation
- kl.detail.costalk_reciprocity
- kl.detail.word_character_reciprocity
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:62
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:364
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# R-reciprocity for the actual boundary-sheaf character

In a finite-generator real realization, let \(C_{x,b}(q)\) be the stalk character of the constructed minimal-boundary sheaf. Then
\[
q^{d(x,b)}C_{x,b}(q^{-1})
=\sum_{x\le z\le b}R_{x,z}(q)C_{z,b}(q).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**How to read this entry:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the induction and choose a reduced word

Induct strongly on \(\ell(b)\), for all top elements \(b\) and all \(x\le b\). Fix the current \(b\), choose a reduced word for it, and let \(V=[1,b]\). Write
\(C_{z,y}=0\) when \(z\not\le y\), and otherwise use the actual boundary character with top \(y\).

The simultaneous word decomposition gives polynomials \(m_y\) and the identities
\[
C_z^{\mathrm{word}}=\sum_{y\in V}m_yC_{z,y},\qquad
K_x^{\mathrm{word}}=\sum_{y\in V}m_y\operatorname{reflect}_{d(x,y)}C_{x,y}.
\]
Its top calculation gives \(m_b=1\).

### Step 2. Write the word convolution before cancellation

The word-character calculation gives
\[
K_x^{\mathrm{word}}=\sum_{z\in V}R_{x,z}C_z^{\mathrm{word}}.
\]
This is proved for the tensor word object, using its Hecke character and bar action, before extracting the boundary summand. Substitute both decompositions from Step 1:
\[
\sum_y m_y\operatorname{reflect}_{d(x,y)}C_{x,y}
=\sum_zR_{x,z}\left(\sum_y m_yC_{z,y}\right).
\]

### Step 3. Verify every lower-summand identity

For \(y\ne b\) in \(V\), strict Bruhat comparison gives \(\ell(y)<\ell(b)\). If \(x\le y\), the induction hypothesis gives
\[
\operatorname{reflect}_{d(x,y)}C_{x,y}
=\sum_{x\le z\le y}R_{x,z}C_{z,y}.
\]
Regard this as a sum over \(V\): terms with \(z\not\le y\) have \(C_{z,y}=0\), and terms with \(x\not\le z\) have \(R_{x,z}=0\).

If \(x\not\le y\), the left side is zero by the convention \(C_{x,y}=0\). Every term on the right is also zero, since a nonzero term would require \(x\le z\le y\), contradicting \(x\not\le y\). Thus the lower identity holds in both cases.

### Step 4. Perform the finite algebraic cancellation

Interchange the two finite sums in Step 2 and move them to one side:
\[
0=\sum_y m_y
\left(\operatorname{reflect}_{d(x,y)}C_{x,y}
-\sum_zR_{x,z}C_{z,y}\right).
\]
Every \(y\ne b\) summand vanishes by Step 3. The remaining coefficient is \(m_b=1\), so
\[
\operatorname{reflect}_{d(x,b)}C_{x,b}
=\sum_zR_{x,z}C_{z,b}.
\]
This also handles the induction base, where there are no lower terms.

### Step 5. Explain the reciprocal notation without assuming a KL bound

Lean states the identity using polynomial reflection. The actual duality gives the weak bound \(\deg C_{x,b}\le d(x,b)\): a stalk basis vector of degree \(j\) corresponds to a nonzero kernel basis vector of degree \(d(x,b)-j\), which must be nonnegative. Therefore reflection evaluates as \(q^{d(x,b)}C_{x,b}(q^{-1})\).

The strict inequality \(2\deg P_{x,b}<d(x,b)\) for canonical KL polynomials is a different statement. It is not an input to this induction, and \(C_{x,b}\) has not been replaced here by \(P_{x,b}\).

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.stalkCharacter_reciprocity`: [DyerPaths.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62).

`OAI.KLInvariance.BruhatGraph.stalkCharacter_natDegree_le`: [EdgeLocalization.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L364).
