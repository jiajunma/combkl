---
id: kl.word.top_stalk
title: The top stalk of a reduced word is the graded coefficient module
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.word_stalks
- kl.coxeter.word_data
- kl.word.evaluation_maps
- kl.word.evaluation_grading
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottFullIndex
  - OAI.KLInvariance.TitsSpace.bottWeight_eq_top
  - OAI.KLInvariance.TitsSpace.bottUnit
  - OAI.KLInvariance.TitsSpace.bottEvaluation_unit
  - OAI.KLInvariance.TitsSpace.bottTopCoordinate_bijective
  - OAI.KLInvariance.TitsSpace.bottTopStalkEquiv
  - OAI.KLInvariance.TitsSpace.bottTopStalkEquiv_homogeneous
  - OAI.KLInvariance.TitsSpace.bottTopHom
  - OAI.KLInvariance.TitsSpace.bottTopInvHom
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:237
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFullIndex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:269
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_eq_top
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:276
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:280
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:300
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopCoordinate_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:314
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopStalkEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:502
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopStalkEquiv_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:2066
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:2075
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTopInvHom
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

# The top stalk of a reduced word is the graded coefficient module

Let \(\mathbf s=(s_1,\ldots,s_m)\) be a reduced word in a finite-generator Coxeter system, with product \(b\). Let \(A\) be the symmetric coefficient algebra, with its degree-one grading.

The only subexpression of \(\mathbf s\) with weight \(b\) is the full subexpression retaining every letter. Evaluation at that coordinate gives a graded \(A\)-linear isomorphism
\[
M_{\mathbf s}^{\,b}\xrightarrow{\sim}A.
\]
Thus the top weight stalk is free of rank one with generator in degree zero.

*Proof.*

### Step 1. Force a top-weight subexpression to retain every letter

Let \(\varepsilon\) be a subexpression with weight \(b\), and let \(\mathbf t\) be its selected subword. If it retains \(r\) letters, then \(r\le m\).

The length of the product of any \(r\)-letter word is at most \(r\). Since the selected product is \(b\) and the original word is reduced,
\[
m=\ell(b)=\ell(w(\mathbf t))\le r\le m.
\]
Hence \(r=m\). A subexpression retaining \(m\) of the \(m\) positions retains all of them, proving uniqueness of the full index.

### Step 2. Realize every value of the surviving coordinate

Define a word element \(u_{\mathbf s}\) recursively by
\[
u_{\varnothing}=1,\qquad u_{s\mathbf t}=1\otimes u_{\mathbf t}.
\]
Every evaluation sends this element to \(1\). For the empty word this is immediate. At each tensor step, the evaluation formula multiplies by the first scalar \(1\) and either keeps or reflects the remaining evaluation. The reflection fixes \(1\), so induction preserves that value.

For any \(a\in A\), \(A\)-linearity therefore gives
\(E_\varepsilon(a u_{\mathbf s})=a\).
In particular, the full coordinate takes every value in \(A\).

### Step 3. Identify the top image stalk

The top stalk is an image inside the product indexed by top-weight subexpressions. Step 1 says that this index set has exactly one element. Two stalk vectors with the same full-coordinate value therefore agree in every coordinate, proving injectivity of evaluation on the stalk.

Step 2 gives surjectivity. The coordinate map is linear, so it defines the asserted module isomorphism.

### Step 4. Check both grading directions

A stalk vector belongs to degree \(n\) exactly when all its coordinates belong to \(A_n\). There is only the full coordinate, so
\[
v\in(M_{\mathbf s}^{\,b})_n
\quad\Longleftrightarrow\quad E_{\mathrm{full}}(v)\in A_n.
\]
This proves that the isomorphism and its inverse preserve degree. The scalar \(1\in A_0\) thus corresponds to a degree-zero basis vector of the top stalk.

For the one-letter word \(s\), the full coordinate is the second coordinate of the congruence pair \((f,g)\). Its image stalk is \(A\), with \(g\) as the top coordinate.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottFullIndex`: [BottSamelson.lean:237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L237).

`OAI.KLInvariance.TitsSpace.bottWeight_eq_top`: [BottSamelson.lean:269](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L269).

`OAI.KLInvariance.TitsSpace.bottUnit`: [BottSamelson.lean:276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L276).

`OAI.KLInvariance.TitsSpace.bottEvaluation_unit`: [BottSamelson.lean:280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L280).

`OAI.KLInvariance.TitsSpace.bottTopCoordinate_bijective`: [BottSamelson.lean:300](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L300).

`OAI.KLInvariance.TitsSpace.bottTopStalkEquiv`: [BottSamelson.lean:314](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L314).

`OAI.KLInvariance.TitsSpace.bottTopStalkEquiv_homogeneous`: [BottSamelson.lean:502](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L502).

`OAI.KLInvariance.TitsSpace.bottTopHom`: [BalancedPairings.lean:2066](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L2066).

`OAI.KLInvariance.TitsSpace.bottTopInvHom`: [BalancedPairings.lean:2075](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L2075).
