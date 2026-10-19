---
id: kl.duality.normalized_character_endpoints
title: Normalized empty and full kernels from the actual character
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.scaled_stalk
- kl.detail.costalk_reciprocity
- kl.duality.boundary_kernel_character
- kl.comparison.normalized_kernel
- kl.detail.boundary_pairing
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.ActualBoundary
  - OAI.KLInvariance.BruhatGraph.actualSectionDuality
  - OAI.KLInvariance.BruhatGraph.actualSectionDuality_homogeneous
  - OAI.KLInvariance.BruhatGraph.emptyKernel_hilbert
  - OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_scaledStalk
  - OAI.KLInvariance.BruhatGraph.normalized_fullKernel_scaledStalk
  - OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_restrictBoundary
  - OAI.KLInvariance.BruhatGraph.normalized_fullKernel_restrictBoundary
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:94
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.ActualBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:100
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actualSectionDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:119
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actualSectionDuality_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:677
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.emptyKernel_hilbert
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1273
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_scaledStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1284
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_fullKernel_scaledStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:793
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_restrictBoundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:800
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.normalized_fullKernel_restrictBoundary
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the unconditional actual-character endpoint lemmas and the upper-restriction
    identities. Used the actual section duality, kept the Hilbert argument at t^2
    in (0,1), and displayed both coefficient-factor and integer-power cancellations.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Normalized empty and full kernels from the actual character

Fix a finite-generator Coxeter system, a basis of its extended realization, and the actual normalized boundary sheaf \(B\) on \([1,b]\). Let its coefficient algebra have \(N\) degree-one variables.

For \(x\in[1,b]\) and \(0<t<1\), write
\[
D_x(t,F)=(1-t^2)^N t^{-d(x,b)}H_{L_x(F)}(t^2),
\]
where \(d(x,b)=\ell(b)-\ell(x)\). The selected outgoing kernel is
\[
L_x(F)=\{m\in B^x:\rho^-_e(m)=0\text{ for every }e\in F\},
\]
with the grading induced from the stalk. Its Hilbert value is
\[
H_{L_x(F)}(q)=\sum_{n\ge0}\dim_{\mathbb R}(L_x(F))_n\,q^n
\qquad(0<q<1).
\]
Writing \(c_x^b(t)=t^{-d(x,b)}C_{x,b}(t^2)\) for the scaled actual-stalk character, one has
\[
D_x(t,\varnothing)=c_x^b(t),\qquad
D_x(t,\mathrm{all})=c_x^b(t^{-1}).
\]
These formulas also hold for the restriction of this same boundary sheaf to an upper interval \([a,b]\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Evaluate the empty-condition module

With no outgoing conditions, \(L_x(\varnothing)=B^x\): the defining vanishing requirement is vacuous.

The [[node:kl.sheaves.hilbert_free|free-stalk Hilbert formula]] therefore gives
\[
H_{L_x(\varnothing)}(t^2)
=C_{x,b}(t^2)(1-t^2)^{-N}.
\]
Since \(0<t<1\), the scalar \(1-t^2\) is nonzero. Multiplying by the state scale cancels its \(N\)-th power:
\[
D_x(t,\varnothing)=t^{-d(x,b)}C_{x,b}(t^2)=c_x^b(t).
\]

### Step 2. Evaluate the full outgoing kernel

The actual boundary's section duality has pairing shift \(\ell(b)\). Its incoming-edge count at \(x\) is \(\ell(x)\). The [[node:kl.detail.costalk_reciprocity|stalk–costalk Hilbert formula]] thus gives
\[
H_{L_x(\mathrm{all})}(t^2)
=(t^2)^{d(x,b)}C_{x,b}(t^{-2})(1-t^2)^{-N}.
\]
The Hilbert sum is evaluated at \(t^2\in(0,1)\); \(C_{x,b}(t^{-2})\) is a finite polynomial evaluation.

### Step 3. Cancel the scale at the full kernel

Again the coefficient factors cancel. The remaining power is
\[
t^{-d(x,b)}(t^2)^{d(x,b)}
=t^{d(x,b)}=(t^{-1})^{-d(x,b)}.
\]
Hence
\[
D_x(t,\mathrm{all})
=t^{d(x,b)}C_{x,b}(t^{-2})
=c_x^b(t^{-1}).
\]

### Step 4. Check restriction to an upper interval

For \(x\in[a,b]\), every outgoing edge \(x\to y\) of the original \([1,b]\) graph has \(a\le x<y\le b\). Thus all its outgoing conditions remain in the upper-interval restriction. The vertex modules and restriction maps are unchanged under their natural identifications.

Consequently both the empty-condition module and the full outgoing kernel are the same modules before and after restriction. The state scale uses the same \(\ell(x),\ell(b)\) and \(N\), so the two identities persist.

### Step 5. Evaluate the one-edge example

For \([1,s]\), \(C_{1,s}=C_{s,s}=1\). At the lower vertex, \(d=1\), the empty kernel is \(A\), and the full kernel is \(\alpha_s A\). The normalized values are
\[
D_1(t,\varnothing)=t^{-1},\qquad D_1(t,\mathrm{all})=t.
\]
At the top vertex, both values are \(1\). These are the actual-character vectors appearing at the ends of a schedule.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.ActualBoundary`: [PositiveTransfer.lean:94](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L94).

`OAI.KLInvariance.BruhatGraph.actualSectionDuality`: [PositiveTransfer.lean:100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L100).

`OAI.KLInvariance.BruhatGraph.actualSectionDuality_homogeneous`: [PositiveTransfer.lean:119](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L119).

`OAI.KLInvariance.BruhatGraph.emptyKernel_hilbert`: [PositiveTransfer.lean:677](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L677).

`OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_scaledStalk`: [TerminalKernels.lean:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273).

`OAI.KLInvariance.BruhatGraph.normalized_fullKernel_scaledStalk`: [TerminalKernels.lean:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

`OAI.KLInvariance.BruhatGraph.normalized_emptyKernel_restrictBoundary`: [PositiveTransfer.lean:793](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L793).

`OAI.KLInvariance.BruhatGraph.normalized_fullKernel_restrictBoundary`: [PositiveTransfer.lean:800](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L800).
