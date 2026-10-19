---
id: kl.detail.sheaf_morphism
title: Morphisms and partial morphisms of graded graph sheaves
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Endomorphism
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.comp
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:570
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:578
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:996
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Endomorphism
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:591
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.comp
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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
- moment_graph_sheaves
---

# Morphisms and partial morphisms of graded graph sheaves

Let \(B,C\) be graded sheaves on the same ordered graph over \(A\). A morphism \(f:B\to C\) consists of degree-zero \(A\)-linear maps
\[
f_x:B^x\to C^x,\qquad f_e:B^e\to C^e
\]
for every vertex and edge, satisfying
\[
f_e\rho^{B,-}_e=\rho^{C,-}_ef_{s(e)},\qquad
f_e\rho^{B,+}_e=\rho^{C,+}_ef_{t(e)}.
\]
These equations say that applying a component map before restriction gives the same result as applying the edge map after restriction.

Composition and identity maps are componentwise. The commuting equations are preserved by composition: substitute the lower equation for \(f\), then the lower equation for the next map; the upper equation is identical in form.

A global section \(m\) maps to the tuple \((f_xm_x)_x\). Its compatibility follows by applying \(f_e\) to each original edge equation and then using the two commuting squares.

## Partial morphisms on a vertex subset

For any subset \(U\), partial morphism data consist of:

- a vertex map \(f_x\) for every \(x\in U\);
- an edge map \(f_e\) for every edge with \(t(e)\in U\);
- the lower commuting equation when both \(s(e),t(e)\) lie in \(U\);
- the upper commuting equation whenever \(t(e)\in U\).

All provided maps have degree zero. In particular, an edge entering \(U\) from outside already has an edge map and its upper commuting square.

For a single edge \(x\to y\) and \(U=\{y\}\), the data are \(f_y,f_e\) and \(f_e\rho^{B,+}_e=\rho^{C,+}_ef_y\). Adding the vertex \(x\) requires \(f_x\) with the lower commuting equation.

When \(U\) is the whole vertex set, these are exactly a full sheaf morphism. When \(U\) is upper and a new vertex is added below it, this is the data used in the descending extension theorem.

## Endomorphisms and projectors

An endomorphism has \(B=C\), with maps on every stalk and edge satisfying the same two equations. Identity, zero, addition, and composition define operations on these maps.

The complement \(1-f\) is again an endomorphism, since
\[
\rho(v-fv)=\rho(v)-\rho(fv)
=\rho(v)-f_e\rho(v).
\]
If \(f^2=f\), then \((1-f)^2=1-f\), component by component. Such idempotent endomorphisms give the sheaf projectors used in split decompositions.

For the one-edge congruence sheaf over \(k[\alpha]\), multiplication by a constant \(c\in k\) on both stalks and the edge is a degree-zero endomorphism. The quotient restrictions commute with that multiplication.

## References

The local definitions and constructions are listed below.

## Lean formalization

In Hom, OnHom, and Endomorphism, `vertex` and `edge` supply the component maps, while `lower` and `upper` supply the displayed commuting equations on their stated domains.

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom`: [SheafMorphisms.lean:570](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L570).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom`: [SheafMorphisms.lean:578](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L578).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Endomorphism`: [SheafMorphisms.lean:996](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L996).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.comp`: [SheafMorphisms.lean:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L591).
