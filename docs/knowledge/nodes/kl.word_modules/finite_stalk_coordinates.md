---
id: kl.word.finite_stalk_coordinates
title: A finite coordinate presentation over an arbitrary weight set
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.coordinate_images
- kl.word.evaluation_maps
- kl.word.diagonal_stabilizer
- kl.word.evaluation_right_action
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.BottUpperIndex
  - OAI.KLInvariance.TitsSpace.bottIndexSetEval
  - OAI.KLInvariance.TitsSpace.bottIndexSetEval_stable
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2013
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottUpperIndex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2015
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIndexSetEval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2020
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIndexSetEval_stable
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read BottUpperIndex, bottIndexSetEval and its right-action stability. Explained
    that the finite index is a subexpression and each coordinate is a whole stalk,
    including duplicate weights and the outer/inner-coordinate recovery.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# A finite coordinate presentation over an arbitrary weight set

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), and a word \(\mathbf t\). Let \(J_{\mathbf t}\) be its finite set of subexpressions, with weight map \(w:J_{\mathbf t}\to W\).

For any set \(U\subseteq W\), define
\[
J_U=\{\varepsilon\in J_{\mathbf t}:w(\varepsilon)\in U\}.
\]
This finite set is BottUpperIndex. It indexes subexpressions whose weights lie in \(U\).

The source uses the finite coordinate map
\[
\widehat p_U:M_{\mathbf t}\longrightarrow
\prod_{\varepsilon\in J_U}M_{\mathbf t}^{w(\varepsilon)},
\qquad
\widehat p_U(m)_\varepsilon=\pi_{w(\varepsilon)}(m).
\]
This is bottIndexSetEval. Each coordinate is an entire weight-stalk vector. Several indices may carry the same stalk.

## Repeated weights

For the word \((s,s)\), the four choices and their weights are
\[
(0,0)\mapsto1,\qquad
(0,1)\mapsto s,\qquad
(1,0)\mapsto s,\qquad
(1,1)\mapsto1.
\]
With \(U=\{1,s\}\), the finite target is
\[
M_{ss}^{1}\times M_{ss}^{s}\times M_{ss}^{s}\times M_{ss}^{1}.
\]
The map repeats each of the two stalk projections twice. If \(U=\{1\}\), its target repeats the \(1\)-stalk at the two corresponding subexpressions.

A tuple \(z=(z_x)_{x\in U}\) induces the finite tuple
\[
\widehat z_\varepsilon=z_{w(\varepsilon)}.
\]

## Recovering the original tuple

Suppose \(\widehat p_U(m)=d\widehat z\). To prove \(\pi_x(m)=dz_x\) for \(x\in U\), compare any subexpression coordinate \(\varepsilon\) in that stalk. Its weight is \(x\), so \(\varepsilon\in J_U\). The finite equality at this outer index is an equality of \(x\)-stalk vectors; evaluating its \(\varepsilon\)-coordinate gives the required scalar equality.

Every coordinate of the \(x\)-stalk therefore agrees. This proves
\(p_U(m)=dz\) on the original set \(U\), including stalks with an empty coordinate set.

## Stable coefficient weights on the finite presentation

For \(a\in A\), define
\[
\widehat\chi_a(\varepsilon)=\chi_{w(\varepsilon)}(a).
\]
The image of \(\widehat p_U\) is preserved by these diagonal weights, because
\[
\widehat p_U(m\cdot a)_\varepsilon
=\chi_{w(\varepsilon)}(a)\pi_{w(\varepsilon)}(m).
\]
This supplies the finite stable-character module needed by the [[node:kl.word.class_lift_assembly|class-lift assembly theorem]]. Its residue classes may repeat a weight many times; the geometric classification concerns the distinct group weights represented in each class.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BottUpperIndex`: [IntegralPairings.lean:2013](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2013).

`OAI.KLInvariance.TitsSpace.bottIndexSetEval`: [IntegralPairings.lean:2015](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2015).

`OAI.KLInvariance.TitsSpace.bottIndexSetEval_stable`: [IntegralPairings.lean:2020](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2020).
