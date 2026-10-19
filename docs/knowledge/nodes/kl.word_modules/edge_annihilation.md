---
id: kl.word.edge_annihilation
title: Reflection labels annihilate word edge quotients
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.evaluation_right_action
- kl.algebra.eigenvalue_difference
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.reflectionCoefficient_anti
  - OAI.KLInvariance.TitsSpace.reflectionCoefficient_difference
  - OAI.KLInvariance.TitsSpace.simpleCoefficient_difference
  - OAI.KLInvariance.TitsSpace.bottSimpleEdge_annihilated
  - OAI.KLInvariance.TitsSpace.bottSimpleEdge_kernel_inclusion
  - OAI.KLInvariance.TitsSpace.bottReflectionEdge_annihilated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1638
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionCoefficient_anti
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1650
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionCoefficient_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1978
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleCoefficient_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1991
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleEdge_annihilated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:2002
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleEdge_kernel_inclusion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1001
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottReflectionEdge_annihilated
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the root-character difference and its application to arbitrary reflection-edge
    quotients, including the simple-edge kernel inclusion. Preserved the arbitrary
    word and absence of an ascent assumption.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Reflection labels annihilate word edge quotients

Fix a finite-generator Coxeter system and its symmetric coefficient algebra \(A\). Let \(t\) be a reflection represented by a geometric root \(a\), and let
\[
\beta=\iota(\operatorname{embed}(a))\in A
\]
be its linear polynomial in the extended realization. For any word \(\mathbf t\) and weight \(x\), set
\[
X=M_{\mathbf t}^x,\qquad Y=M_{\mathbf t}^{tx},\qquad
f=\pi_x,\quad g=\pi_{tx}.
\]
The pair-projection quotient \(Q\) of \(f,g\) is annihilated by \(\beta\):
\[
\beta q=0\qquad(q\in Q).
\]
Consequently, for every \(y\in Y\), there exists \(m\in M_{\mathbf t}\) with
\[
f(m)=0,\qquad g(m)=\beta y.
\]
The assertion holds for every weight \(x\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose a coefficient with a prescribed character difference

The reflection action sends its root polynomial to its negative:
\(\chi_t(\beta)=-\beta\).
Choose
\[
p=\chi_x^{-1}\left(\frac{\beta}{2}\right).
\]
Then \(\chi_x(p)=\beta/2\). The group-action identity gives
\[
\chi_{tx}(p)=\chi_t(\chi_x(p))
=\chi_t(\beta/2)=-\beta/2.
\]
Hence
\[
\chi_x(p)-\chi_{tx}(p)=\beta.
\]
The source's reflectionCoefficient_difference constructs exactly this \(p\).

### Step 2. Apply the [[node:kl.algebra.eigenvalue_difference|scalar-difference theorem]]

Right multiplication by \(p\) is an \(A\)-linear endomorphism \(T\) of the word module. The [[node:kl.word.evaluation_right_action|evaluation right-action theorem]] gives
\[
f(Tm)=\chi_x(p)f(m),\qquad
g(Tm)=\chi_{tx}(p)g(m).
\]
Both stalk projections are surjective by their image definitions. Thus the [[node:kl.algebra.eigenvalue_difference|scalar-difference theorem]] applies and says that their character difference annihilates \(Q\). Step 1 identifies that difference with \(\beta\).

### Step 3. Lift a root multiple with zero first projection

For \(y\in Y\), linearity and Step 2 give
\[
u(\beta y)=\beta u(y)=0.
\]
The pair-projection compatibility criterion at \((0,\beta y)\) says
\[
u(\beta y)=0
\quad\Longleftrightarrow\quad
\exists m,\ f(m)=0,\ g(m)=\beta y.
\]
This gives the requested lift.

For a simple reflection \(s\), the root polynomial is \(\alpha_s\), and the witness coefficient is \(\chi_x^{-1}(\alpha_s/2)\). The resulting lift of \((0,\alpha_s y)\) is the input that makes the twisted two-stalk lattice closed under scalars.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.reflectionCoefficient_anti`: [Frobenius.lean:1638](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1638).

`OAI.KLInvariance.TitsSpace.reflectionCoefficient_difference`: [Frobenius.lean:1650](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1650).

`OAI.KLInvariance.TitsSpace.simpleCoefficient_difference`: [Frobenius.lean:1978](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1978).

`OAI.KLInvariance.TitsSpace.bottSimpleEdge_annihilated`: [Frobenius.lean:1991](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1991).

`OAI.KLInvariance.TitsSpace.bottSimpleEdge_kernel_inclusion`: [Frobenius.lean:2002](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2002).

`OAI.KLInvariance.TitsSpace.bottReflectionEdge_annihilated`: [BottSamelson.lean:1001](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1001).
