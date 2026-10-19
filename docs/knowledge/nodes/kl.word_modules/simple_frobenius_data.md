---
id: kl.word.simple_frobenius_data
title: Frobenius data for the simple reflections of the extended realization
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.reflection_algebra_action
- kl.word.reflection_trace_degree
- kl.notes.extended_realization
- kl.realization.extended_action
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.coefficientAction_simple
  - OAI.KLInvariance.TitsSpace.simpleFixed
  - OAI.KLInvariance.TitsSpace.simpleRootPolynomial
  - OAI.KLInvariance.TitsSpace.simple_involutive
  - OAI.KLInvariance.TitsSpace.simpleRootPolynomial_ne_zero
  - OAI.KLInvariance.TitsSpace.simple_anti
  - OAI.KLInvariance.TitsSpace.simple_divisible
  - OAI.KLInvariance.TitsSpace.simpleCoordinates
  - OAI.KLInvariance.TitsSpace.simpleTrace
  - OAI.KLInvariance.TitsSpace.simpleDuality
  - OAI.KLInvariance.TitsSpace.simpleDuality_apply
  - OAI.KLInvariance.TitsSpace.simpleRoot_homogeneous
  - OAI.KLInvariance.TitsSpace.coefficientAction_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:28
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.coefficientAction_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:45
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleFixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:48
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleRootPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:51
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:55
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleRootPolynomial_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:58
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_anti
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:63
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_divisible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:68
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleCoordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:79
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleTrace
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:83
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:88
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleDuality_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:819
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleRoot_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:824
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.coefficientAction_homogeneous
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the actual TitsSpace simple data, generic instantiation and grading
    lemmas. Identified the extended root/coroot pair with self-pairing two and the
    exact trace normalization used by bottSamelson.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Frobenius data for the simple reflections of the extended realization

Fix a Coxeter system on a finite set \(I\) of simple generators. Let \(V\) be its real extended realization, with bilinear form \(B\) and simple roots \(r_i\). Its coefficient algebra is
\[
A=\operatorname{Sym}_{\mathbb R}(V).
\]
For \(s_i\), the simple reflection indexed by \(i\), the extended action has formula
\[
s_i(v)=v-B(r_i,v)r_i,\qquad B(r_i,r_i)=2.
\]
Thus \(r_i\) and the functional \(\varphi_i(v)=B(r_i,v)\) are the root-coroot data of the [[node:kl.word.reflection_algebra_action|symmetric-algebra reflection theorem]].

## Invariant ring, coordinates and trace

Let \(\tau_i\) be the coefficient action of \(s_i\), and put
\[
R_i=A^{\tau_i},\qquad \alpha_i=\iota(r_i).
\]
The source's `simpleFixed` is \(R_i\), and `simpleRootPolynomial` is \(\alpha_i\). The generic reflection theorem proves
\[
\tau_i^2=1,\quad \alpha_i\ne0,\quad
\tau_i(\alpha_i)=-\alpha_i,\quad
\alpha_i\mid a-\tau_i(a).
\]

Applying the coordinate and trace constructions gives
\[
C_i:A\xrightarrow{\sim}R_i^2,\qquad
a=a_0+\alpha_i a_1,\qquad t_i(a)=a_1.
\]
These are `simpleCoordinates` and `simpleTrace`. The two coordinates give a finite \(R_i\)-basis \(1,\alpha_i\) of \(A\). The source registers this freeness and finiteness for the tensor constructors.

The perfect trace pairing is
\[
D_i:A\xrightarrow{\sim}\operatorname{Hom}_{R_i}(A,R_i),
\qquad D_i(a)(b)=t_i(ab).
\]
It is `simpleDuality`, and its displayed evaluation formula is `simpleDuality_apply`. These three objects—\(R_i,t_i,D_i\)—are exactly the data used when prepending \(s_i\) to a word.

## Degree conventions

Choose a basis of \(V\). The source's symmetric grading is the polynomial total-degree grading transported through this basis, with each linear generator in degree one. Consequently
\[
\alpha_i\in A_1,\qquad \tau_i(A_n)\subseteq A_n.
\]
The second statement follows because the extended action is linear on \(V\): a product of \(n\) linear generators maps to a sum of products of \(n\) linear generators. The transported grading has zero negative pieces.

The [[node:kl.word.reflection_trace_degree|reflection trace degree theorem]] therefore gives
\[
t_i(A_n)\subseteq R_i\cap A_{n-1}.
\]
This one-degree shift is the input to the word-pairing degree induction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.coefficientAction_simple`: [Frobenius.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L28).

`OAI.KLInvariance.TitsSpace.simpleFixed`: [Frobenius.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L45).

`OAI.KLInvariance.TitsSpace.simpleRootPolynomial`: [Frobenius.lean:48](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L48).

`OAI.KLInvariance.TitsSpace.simple_involutive`: [Frobenius.lean:51](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L51).

`OAI.KLInvariance.TitsSpace.simpleRootPolynomial_ne_zero`: [Frobenius.lean:55](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L55).

`OAI.KLInvariance.TitsSpace.simple_anti`: [Frobenius.lean:58](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L58).

`OAI.KLInvariance.TitsSpace.simple_divisible`: [Frobenius.lean:63](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L63).

`OAI.KLInvariance.TitsSpace.simpleCoordinates`: [Frobenius.lean:68](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L68).

`OAI.KLInvariance.TitsSpace.simpleTrace`: [Frobenius.lean:79](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L79).

`OAI.KLInvariance.TitsSpace.simpleDuality`: [Frobenius.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L83).

`OAI.KLInvariance.TitsSpace.simpleDuality_apply`: [Frobenius.lean:88](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L88).

`OAI.KLInvariance.TitsSpace.simpleRoot_homogeneous`: [Frobenius.lean:819](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L819).

`OAI.KLInvariance.TitsSpace.coefficientAction_homogeneous`: [Frobenius.lean:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L824).
