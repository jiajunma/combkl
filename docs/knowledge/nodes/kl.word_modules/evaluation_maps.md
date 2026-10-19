---
id: kl.word.evaluation_maps
title: Subexpression evaluations of tensor word modules
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.bott_samelson
- kl.word.simple_frobenius_data
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottWeight
  - OAI.KLInvariance.TitsSpace.weightFunctional
  - OAI.KLInvariance.TitsSpace.inducedFunctional
  - OAI.KLInvariance.TitsSpace.bottEvaluation
  - OAI.KLInvariance.TitsSpace.bottEvaluation_tmul
  - OAI.KLInvariance.TitsSpace.bottUnit
  - OAI.KLInvariance.TitsSpace.bottEvaluation_unit
  - OAI.KLInvariance.TitsSpace.bottEvaluation_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1056
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1062
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.weightFunctional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1078
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.inducedFunctional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1085
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1091
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:276
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottUnit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:280
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:289
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_surjective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the two functional constructors, recursive evaluations and unit tensor.
    Explained scalar balance over the actual fixed algebra, the untouched outer coefficient
    and the distinction between one evaluation and their joint map.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Subexpression evaluations of tensor word modules

Fix a Coxeter system with finite simple-generator set \(I\), its real extended realization \(V\), and \(A=\operatorname{Sym}_{\mathbb R}(V)\). Write \(\chi_w:A\to A\) for the coefficient action of \(w\in W\). For a simple reflection \(s\), put \(\tau=\chi_s\) and \(R=A^s\).

A word \(\mathbf t=(s_1,\ldots,s_m)\) has a tensor word module \(M_{\mathbf t}\), with
\[
M_\varnothing=A,\qquad M_{s\mathbf t}=A\otimes_R M_{\mathbf t}.
\]
Its set \(J_{\mathbf t}\) of subexpressions consists of choices of \(0\) or \(1\) at each position. The empty word has one empty choice. Recursively,
\[
J_{s\mathbf t}=\{0,1\}\times J_{\mathbf t}.
\]

## Group weights

The weight of a subexpression is the product of the retained letters in their original order:
\[
w_\varnothing(())=1,\qquad
w_{s\mathbf t}(\varepsilon,\eta)=
\begin{cases}
w_{\mathbf t}(\eta),&\varepsilon=0,\\
s\,w_{\mathbf t}(\eta),&\varepsilon=1.
\end{cases}
\]
This is `bottWeight`. For example, the choices \((1,0,1)\) in \((s,t,u)\) have weight \(su\).

The coefficient character at a group weight \(x\) is the algebra automorphism \(\chi_x:A\to A\). The [[node:kl.word.evaluation_right_action|evaluation right-action theorem]] proves that right multiplication by \(a\) transforms the weight-\(x\) coordinate by the scalar \(\chi_x(a)\).

## Evaluation maps

For each \(\eta\in J_{\mathbf t}\), evaluation is an \(A\)-linear map
\[
E_{\mathbf t,\eta}:M_{\mathbf t}\to A.
\]
The empty-word evaluation is the identity of \(A\). Prepending \(s\) gives
\[
\begin{aligned}
E_{s\mathbf t,(0,\eta)}(a\otimes m)&=a\,E_{\mathbf t,\eta}(m),\\
E_{s\mathbf t,(1,\eta)}(a\otimes m)&=a\,\tau(E_{\mathbf t,\eta}(m)).
\end{aligned}
\]
The outer coefficient \(a\) stays outside the reflection.

These formulas respect the tensor relations over \(R\). If \(r\in R\), then \(\tau(r)=r\); hence
\[
\tau(E_{\mathbf t,\eta}(rm))
=\tau(rE_{\mathbf t,\eta}(m))
=r\,\tau(E_{\mathbf t,\eta}(m)).
\]
Thus both \(m\mapsto E_{\mathbf t,\eta}(m)\) and \(m\mapsto\tau(E_{\mathbf t,\eta}(m))\) are \(R\)-linear. Multiplication by the outer factor extends each to \(A\otimes_R M_{\mathbf t}\). The source implements these two steps as `weightFunctional` and `inducedFunctional`.

Full evaluation collects all coordinates:
\[
E_{\mathbf t}:M_{\mathbf t}\to A^{J_{\mathbf t}},
\qquad m\mapsto(E_{\mathbf t,\eta}(m))_{\eta\in J_{\mathbf t}}.
\]
Its injectivity is proved by the reflection block matrix.

## A vector with every evaluation equal to one

Define the unit tensor recursively by
\[
u_\varnothing=1,\qquad u_{s\mathbf t}=1\otimes u_{\mathbf t}.
\]
Both evaluation formulas send this tensor to \(1\), since \(\tau(1)=1\). Induction gives \(E_{\mathbf t,\eta}(u_{\mathbf t})=1\) for every \(\eta\).

For any \(a\in A\), the vector \(a u_{\mathbf t}\) therefore evaluates to \(a\) at each coordinate. In particular, every individual evaluation is surjective. The source calls these constructions and properties `bottUnit`, `bottEvaluation_unit` and `bottEvaluation_surjective`.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottWeight`: [Frobenius.lean:1056](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1056).

`OAI.KLInvariance.TitsSpace.weightFunctional`: [Frobenius.lean:1062](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1062).

`OAI.KLInvariance.TitsSpace.inducedFunctional`: [Frobenius.lean:1078](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1078).

`OAI.KLInvariance.TitsSpace.bottEvaluation`: [Frobenius.lean:1085](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1085).

`OAI.KLInvariance.TitsSpace.bottEvaluation_tmul`: [Frobenius.lean:1091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1091).

`OAI.KLInvariance.TitsSpace.bottUnit`: [BottSamelson.lean:276](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L276).

`OAI.KLInvariance.TitsSpace.bottEvaluation_unit`: [BottSamelson.lean:280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L280).

`OAI.KLInvariance.TitsSpace.bottEvaluation_surjective`: [BottSamelson.lean:289](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L289).
