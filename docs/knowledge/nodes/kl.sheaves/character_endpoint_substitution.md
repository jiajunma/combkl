---
id: kl.duality.character_endpoint_substitution
title: KL endpoint formulas under character identification
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.character_identity_condition
- kl.comparison.normalized_kernel
- kl.foundations.scaled_kl
- kl.sheaves.hilbert_free
- kl.detail.costalk_reciprocity
- kl.sheaves.upper_interval_kernels
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_of_character
  - OAI.KLInvariance.BruhatGraph.normalized_fullKernel_of_duality_character
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:693
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_of_character
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:708
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_fullKernel_of_duality_character
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both PositiveTransfer endpoint lemmas and their surrounding parameters.
    Preserved arbitrary bottom for the empty endpoint, lower-interval/degree-shift
    duality for the full endpoint, pointwise character equality and the positive real
    parameter range.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# KL endpoint formulas under character identification

Fix a finite-generator Coxeter system and its real polynomial coefficient algebra \(A\) in \(N\) degree-one variables. Let \(B\) be any normalized boundary sheaf on \([u,b]\), and let \(x\in[u,b]\). Suppose its actual character satisfies the vertex equality
\[
C_x^{[u,b]}(q)=P_{x,b}(q).
\]
For \(0<t<1\), define the normalized kernel state and scaled KL polynomial by
\[
D_x(t,F)=(1-t^2)^N t^{\ell(x)-\ell(b)}H_{L_x(F)}(t^2),
\qquad
p_{x,b}(t)=t^{\ell(x)-\ell(b)}P_{x,b}(t^2).
\]
Here \(L_x(F)\) imposes the selected outgoing vanishing conditions and
\(H_M(q)=\sum_{n\ge0}\dim_{\mathbb R}M_n\,q^n\).

Then
\[
D_x(t,\varnothing)=p_{x,b}(t).
\]
For the full-kernel assertion, take \(u=1\) and additionally supply section duality with homogeneous pairing shift \(\ell(b)\). Under the same character equality at \(x\),
\[
D_x(t,U_x)=p_{x,b}(t^{-1}),
\]
where \(U_x\) is the full outgoing edge set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compute the stalk Hilbert value in the supplied model

The given \(B\) is graded-isomorphic to the chosen boundary sheaf used to define \(C_x^{[u,b]}\). Its stalk therefore has that same character.

With no outgoing conditions, \(L_x(\varnothing)=B^x\). The [[node:kl.sheaves.hilbert_free|homogeneous free-basis formula]] gives
\[
H_{L_x(\varnothing)}(t^2)
=C_x^{[u,b]}(t^2)(1-t^2)^{-N}.
\]
The range \(0<t<1\) ensures \(0<t^2<1\), as required for this convergent Hilbert value.

### Step 2. Substitute the character equality at the empty endpoint

Evaluate the polynomial equality at \(t^2\). After multiplying by the state scale, the factors \((1-t^2)^N\) and \((1-t^2)^{-N}\) cancel, since \(1-t^2\ne0\). Thus
\[
D_x(t,\varnothing)
=t^{\ell(x)-\ell(b)}P_{x,b}(t^2)
=p_{x,b}(t).
\]

### Step 3. Compute the full-kernel Hilbert value

Work now on \([1,b]\) with the stated section duality. Put \(d=\ell(b)-\ell(x)\). Its pairing shift is \(\ell(b)\), and there are \(\ell(x)\) incoming edges at \(x\). Stalk–costalk reciprocity gives
\[
H_{L_x(U_x)}(t^2)
=(t^2)^d C_{x,b}(t^{-2})(1-t^2)^{-N}.
\]
Use the character equality at \(t^{-2}\) to replace \(C_{x,b}\) by \(P_{x,b}\). This is a finite polynomial evaluation; the Hilbert sum itself remains at \(t^2\).

### Step 4. Cancel the full-kernel scale

The coefficient factors again cancel. Since \(t\ne0\),
\[
t^{-d}(t^2)^d=t^d=(t^{-1})^{-d}.
\]
Consequently
\[
D_x(t,U_x)
=t^dP_{x,b}(t^{-2})
=(t^{-1})^{-d}P_{x,b}((t^{-1})^2)
=p_{x,b}(t^{-1}).
\]
This proves the second formula with precisely the supplied duality and character hypotheses.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_of_character`: [PositiveTransfer.lean:693](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L693).

`OAI.KLInvariance.BruhatGraph.normalized_fullKernel_of_duality_character`: [PositiveTransfer.lean:708](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L708).
