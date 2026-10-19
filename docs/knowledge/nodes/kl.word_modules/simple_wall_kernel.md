---
id: kl.word.simple_wall_kernel
title: The exact stalk kernel across the first reflection
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.simple_flip
- kl.word.edge_annihilation
- kl.algebra.pair_projection
- kl.notes.word_stalks
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSimpleFlip_divisible
  - OAI.KLInvariance.TitsSpace.bottEvaluation_flip
  - OAI.KLInvariance.TitsSpace.bottStalkProjection_flip_zero
  - OAI.KLInvariance.TitsSpace.bottSimpleWall_kernel_projection
  - OAI.KLInvariance.TitsSpace.bottSimpleWall_annihilated
  - OAI.KLInvariance.TitsSpace.bottSimpleWall_upper_kernel
  - OAI.KLInvariance.PairProjection.kernel_upper
  - OAI.KLInvariance.PairProjection.upper_kernel_of_divisibility
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1907
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleFlip_divisible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1934
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_flip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1954
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection_flip_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1968
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleWall_kernel_projection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2011
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleWall_annihilated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2018
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleWall_upper_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1848
    format: lean-location
    note: OAI.KLInvariance.PairProjection.kernel_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1853
    format: lean-location
    note: OAI.KLInvariance.PairProjection.upper_kernel_of_divisibility
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read tensor difference divisibility, both evaluation-flip cases, projection
    vanishing and the generic upper-kernel criterion. Kept the first-letter hypothesis
    and proved each kernel containment with its distinct input.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The exact stalk kernel across the first reflection

Fix a finite-generator Coxeter system and \(A=\operatorname{Sym}_{\mathbb R}(V)\) for its real extended realization \(V\). Let \(M_{s\mathbf t}=A\otimes_{A^s}M_{\mathbf t}\) be a word module beginning with the simple reflection \(s\), and let \(\alpha_s\) be its root polynomial. For any weight \(x\), put
\[
X=M_{s\mathbf t}^x,\qquad Y=M_{s\mathbf t}^{sx},
\qquad f=\pi_x,\quad g=\pi_{sx}.
\]
Then
\[
f(m)=0\quad\Longrightarrow\quad
g(m)=\alpha_s y\ \text{for some }y\in Y.
\]
For the pair-projection upper map \(u:Y\to Q\), this gives the exact formula
\[
\ker u=\alpha_s Y.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Relate the reflected tensor to exchanged evaluations

Write \(\tau=\chi_s\), let \(F_s\) reflect the first tensor factor, and let \(\sigma\) exchange the first subexpression bit. We prove
\[
E_e(F_s(m))=\tau(E_{\sigma(e)}(m)).
\]
It is enough to check a pure tensor \(m=a\otimes n\), then extend by additivity.

For \(e=(0,\eta)\), the two sides are
\[
\tau(a)E_\eta(n)
\quad\text{and}\quad
\tau(a\,\tau(E_\eta(n)))=\tau(a)E_\eta(n),
\]
using \(\tau^2=1\).
For \(e=(1,\eta)\), they are
\(\tau(a)\tau(E_\eta(n))\) and \(\tau(aE_\eta(n))\), equal by multiplicativity.

### Step 2. Prove divisibility of the difference of tensors

For a pure tensor, simple-root divisibility supplies \(b\in A\) with
\(a-\tau(a)=\alpha_s b\). Therefore
\[
a\otimes n-F_s(a\otimes n)
=(a-\tau(a))\otimes n
=\alpha_s(b\otimes n).
\]
A finite sum of pure tensors has difference equal to the sum of these root multiples. Hence every \(m\) satisfies
\[
m-F_s(m)=\alpha_s v
\]
for some \(v\in M_{s\mathbf t}\).

### Step 3. Transport vanishing to the opposite weight

Assume \(\pi_x(m)=0\). If \(e\) has weight \(sx\), then \(\sigma(e)\) has weight
\(s(sx)=x\). Thus \(E_{\sigma(e)}(m)=0\), and Step 1 gives \(E_e(F_s(m))=0\).

Every coordinate in the \(sx\)-stalk of \(F_s(m)\) is zero, so
\(\pi_{sx}(F_s(m))=0\). Project Step 2 to that stalk:
\[
\pi_{sx}(m)=\alpha_s\pi_{sx}(v).
\]
This proves the first assertion with \(y=\pi_{sx}(v)\).

### Step 4. Prove both kernel inclusions

If \(z\in\ker u\), the pair-projection kernel criterion gives \(m\) with
\(f(m)=0\) and \(g(m)=z\). Step 3 gives \(z\in\alpha_s Y\).

Conversely, the [[node:kl.word.edge_annihilation|reflection-label annihilation theorem]] gives
\(\alpha_s q=0\) for every \(q\in Q\). Hence for \(y\in Y\),
\[
u(\alpha_s y)=\alpha_s u(y)=0.
\]
Therefore \(\alpha_s Y\subseteq\ker u\), proving equality.

The argument works for every \(x\), and it uses the actual image stalks. In the one-letter example, \(X=Y=A\), \(Q=A/(\alpha_s)\), and the formula is the familiar kernel of the quotient map.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSimpleFlip_divisible`: [Frobenius.lean:1907](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1907).

`OAI.KLInvariance.TitsSpace.bottEvaluation_flip`: [Frobenius.lean:1934](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1934).

`OAI.KLInvariance.TitsSpace.bottStalkProjection_flip_zero`: [Frobenius.lean:1954](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1954).

`OAI.KLInvariance.TitsSpace.bottSimpleWall_kernel_projection`: [Frobenius.lean:1968](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1968).

`OAI.KLInvariance.TitsSpace.bottSimpleWall_annihilated`: [Frobenius.lean:2011](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2011).

`OAI.KLInvariance.TitsSpace.bottSimpleWall_upper_kernel`: [Frobenius.lean:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018).

`OAI.KLInvariance.PairProjection.kernel_upper`: [Frobenius.lean:1848](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1848).

`OAI.KLInvariance.PairProjection.upper_kernel_of_divisibility`: [Frobenius.lean:1853](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1853).
