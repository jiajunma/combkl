---
id: kl.sheaves.interval_word_extension
title: Extending an interval assignment to its ambient upper closure
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.word.weight_support
- kl.word.reflected_sets
- kl.detail.word_sheaf
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalk_subsingleton_of_not_bruhat
  - OAI.KLInvariance.TitsSpace.intervalUpperClosure
  - OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper
  - OAI.KLInvariance.TitsSpace.intervalUpperClosure_member
  - OAI.KLInvariance.TitsSpace.bottIntervalExtension
  - OAI.KLInvariance.TitsSpace.bottIntervalExtension_apply
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2134
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_subsingleton_of_not_bruhat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2142
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.intervalUpperClosure
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2146
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2152
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.intervalUpperClosure_member
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2158
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIntervalExtension
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2164
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIntervalExtension_apply
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the ambient upper closure, its intersection with the interval, the
    actual full-assignment zero-extension definition and support lemma. Preserved
    the source convention of compatibility on a subset of a full assignment.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Extending an interval assignment to its ambient upper closure

Fix a Coxeter system and \(b\in W\), and write \(I=[1,b]\). For any subset \(U\subseteq I\), define its ambient upper closure by
\[
\overline U=\{x\in W:\text{some }a\in U\text{ satisfies }a\le x\}.
\]
This is intervalUpperClosure.

It is upper in \(W\): if \(a\le x\le y\), then \(a\le y\). If \(U\) is upper within the interval, then
\[
\overline U\cap[1,b]=U.
\]
The inclusion from right to left uses \(x\le x\). For the reverse, if \(a\in U\), \(a\le x\), and \(x\le b\), then \(x\) is an interval vertex above \(a\). Upward closure of \(U\) within the interval gives \(x\in U\).

## The source's assignment convention

Now take a finite-generator system, a word \(\mathbf t\) with product \(b\), and its pair-projection sheaf on \(I\). An assignment \(f\) specifies a value \(f_x\) at every vertex \(x\in I\). The condition “compatible on \(U\)” imposes edge equations only for edges whose two endpoints lie in \(U\). An extension must agree with \(f\) on \(U\).

For any such assignment, define a tuple on \(\overline U\) by
\[
\widetilde f_x=
\begin{cases}
f_x,&x\le b,\\
0,&x\not\le b.
\end{cases}
\]
This is bottIntervalExtension. When \(U\) is upper within \(I\), its intersection property shows that every first-branch value comes from a vertex in \(U\).

## Reduced-word support

If \(\mathbf t\) is reduced, the reduced-word support theorem gives
\[
M_{\mathbf t}^x=0\qquad(x\not\le b).
\]
Thus the second branch is then the unique vector of its stalk. The extension agrees with the original assignment at every vertex of \(U\).

For a reduced word and an upper interval set, the [[node:kl.detail.word_flabbiness|word-sheaf flabbiness theorem]] proves that \(\widetilde f\) is compatible on the ambient upper closure, lifts it to one word vector, and projects that vector back to a global section on \(I\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalk_subsingleton_of_not_bruhat`: [IntegralPairings.lean:2134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2134).

`OAI.KLInvariance.TitsSpace.intervalUpperClosure`: [IntegralPairings.lean:2142](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2142).

`OAI.KLInvariance.TitsSpace.intervalUpperClosure_upper`: [IntegralPairings.lean:2146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2146).

`OAI.KLInvariance.TitsSpace.intervalUpperClosure_member`: [IntegralPairings.lean:2152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2152).

`OAI.KLInvariance.TitsSpace.bottIntervalExtension`: [IntegralPairings.lean:2158](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2158).

`OAI.KLInvariance.TitsSpace.bottIntervalExtension_apply`: [IntegralPairings.lean:2164](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2164).
