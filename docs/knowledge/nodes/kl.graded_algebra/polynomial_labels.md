---
id: kl.detail.polynomial_labels
title: Reflection roots as polynomial edge labels
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.foundations.bruhat_step
- kl.notes.extended_realization
- kl.detail.positive_roots
- kl.detail.root_reflection_correspondence
- kl.realization.radical_extension
- kl.algebra.coefficient_algebra
- kl.detail.ordered_graph
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  - Tits
  declarations:
  - OAI.KLInvariance.BruhatGraph.Edge
  - OAI.KLInvariance.BruhatGraph.source
  - OAI.KLInvariance.BruhatGraph.target
  - OAI.KLInvariance.BruhatGraph.graph
  - OAI.KLInvariance.BruhatGraph.root
  - OAI.KLInvariance.BruhatGraph.polynomialLabel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:22
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.Edge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:29
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:30
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.target
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:32
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.graph
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:141
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:144
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialLabel
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- realizations_and_grading
---

# Reflection roots as polynomial edge labels

Fix a Coxeter system with finitely many simple generators and an interval \([u,b]\). Let \(V_0\) be its original real root space, let \(E\) be the nondegenerate extension, and write \(\iota:V_0\to E\) for the embedding. The coefficient algebra is
\[
A=\operatorname{Sym}_{\mathbb R}(E).
\]

## The underlying Bruhat interval graph

The vertex set is \([u,b]\). An edge is a pair \((x,y)\) satisfying
\[
y=tx,\qquad t\text{ a reflection},\qquad\ell(x)<\ell(y).
\]
Its source and target are \(x,y\). A Bruhat step gives \(x<y\), so this is an ordered graph.

The left reflection label is determined by the endpoints:
\[
t=yx^{-1}.
\]
The interval is finite, and its edge set is a subset of the finite vertex-pair set.

In type \(A_2\), \(w_0=sts\) is a reflection of length three. Thus the graph on \([1,w_0]\) includes the edge \(1\to w_0\), along with the covering edges and saturated paths.

## From the reflection to its linear polynomial

Let \(a_e\) be the unique positive root representing the left reflection label of \(e\). Let \(\kappa:E\to\operatorname{Sym}_{\mathbb R}(E)\) be the degree-one inclusion. Embed the root in \(E\), then apply this map:
\[
\alpha_e=\kappa(\iota(a_e)).
\]
This is a nonzero element of degree one.

Choose a basis \(v_1,\ldots,v_N\) of \(E\), and identify its symmetric algebra with
\(\mathbb R[X_1,\ldots,X_N]\). If
\[
\iota(a_e)=\sum_j c_jv_j,
\]
then the polynomial label is
\[
\alpha_e=\sum_jc_jX_j.
\]
The coordinates describe the same degree-one symmetric-algebra element. The embedded root is nonzero, so some coefficient \(c_j\) is nonzero. It is the coefficient of \(X_j\) in the label, proving \(\alpha_e\ne0\).

## The edge coefficient ring

The principal ideal \((\alpha_e)\) gives the edge coefficient quotient
\[
A/(\alpha_e).
\]
For a sheaf satisfying the upper-quotient rule, the upper stalk modulo multiplication by this label is its edge module. In root-plane localization, the position of the root vector determines whether its label becomes a unit.

The reflection \(t\), its positive root \(a_e\), the embedded vector \(\iota(a_e)\), and the polynomial \(\alpha_e\) are linked by these explicit maps.

The [[node:kl.algebra.root_label_primes|root-label primality theorem]] proves divisibility and regularity properties of these labels. The [[node:kl.algebra.root_quotient_coordinates|edge-quotient presentation]] gives their coefficient ring after reduction.

## References

The source declarations below define the interval graph and polynomial label map.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.Edge`: [Tits.lean:22](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L22).

`OAI.KLInvariance.BruhatGraph.source`: [Tits.lean:29](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L29).

`OAI.KLInvariance.BruhatGraph.target`: [Tits.lean:30](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L30).

`OAI.KLInvariance.BruhatGraph.graph`: [Tits.lean:32](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L32).

`OAI.KLInvariance.BruhatGraph.root`: [SheafMorphisms.lean:141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L141).

`OAI.KLInvariance.BruhatGraph.polynomialLabel`: [SheafMorphisms.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L144).
