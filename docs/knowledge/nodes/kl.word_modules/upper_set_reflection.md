---
id: kl.word.upper_set_reflection
title: Reflected upper sets and their crossing edges
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.reflected_sets
- kl.detail.bruhat_lifting
- kl.coxeter.simple_edge_transport
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleUnion
  - OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleInter
  - OAI.KLInvariance.TitsSpace.BruhatUpper.simpleUnion
  - OAI.KLInvariance.TitsSpace.BruhatUpper.simpleInter
  - OAI.KLInvariance.TitsSpace.simpleUnion_stable
  - OAI.KLInvariance.TitsSpace.simpleInter_stable
  - OAI.KLInvariance.TitsSpace.cross_edge_is_simple
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:391
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleUnion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:406
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleInter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:419
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BruhatUpper.simpleUnion
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:427
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BruhatUpper.simpleInter
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:435
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleUnion_stable
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:441
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleInter_stable
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:447
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.cross_edge_is_simple
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read both envelope membership equivalences, monotonicity applications,
    stability identities and cross_edge_is_simple. Preserved the upward edge and excluded-endpoint
    conditions.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Reflected upper sets and their crossing edges

Fix a Coxeter system with finite simple-generator set, a simple reflection \(s\), and a Bruhat upper set \(U\). Put
\[
J=U\cup sU,\qquad K=U\cap sU.
\]
Both \(J\) and \(K\) are reflection-stable Bruhat upper sets.

For an upward reflection edge \(x\to y\), if \(sx\in U\) and \(sy\notin U\), then \(y=sx\).

*Proof.*

### Step 1. Express membership using the simple envelopes

The elements \(x,sx\) are comparable in Bruhat order. Write \(U_s(x)\) for the higher one and \(L_s(x)\) for the lower one.

If either \(x\) or \(sx\) lies in the upper set \(U\), then their higher element lies in \(U\). Conversely, \(U_s(x)\) is one of the two elements. Thus
\[
x\in J\quad\Longleftrightarrow\quad U_s(x)\in U.
\]

If both \(x,sx\) lie in \(U\), their lower element lies in \(U\). Conversely, membership of \(L_s(x)\) and upward closure give membership of both elements. Hence
\[
x\in K\quad\Longleftrightarrow\quad L_s(x)\in U.
\]

### Step 2. Prove upward closure

The [[node:kl.detail.bruhat_lifting|simple-envelope theorem]] gives
\[
x\le y\Longrightarrow U_s(x)\le U_s(y),
\qquad
x\le y\Longrightarrow L_s(x)\le L_s(y).
\]
If \(x\in J\), Step 1 puts \(U_s(x)\) in \(U\); upward closure then puts \(U_s(y)\) in \(U\), so \(y\in J\). The same reasoning with \(L_s\) proves upward closure of \(K\).

### Step 3. Prove reflection stability

Since \(s(sx)=x\),
\[
sx\in J\iff(sx\in U\text{ or }x\in U)\iff x\in J.
\]
Replacing “or” with “and” gives \(sx\in K\iff x\in K\).

### Step 4. Identify a crossing edge

Suppose \(x\to y\), \(sx\in U\), and \(sy\notin U\). If \(y\ne sx\), the [[node:kl.coxeter.simple_edge_transport|simple edge-transport theorem]] gives an upward edge \(sx\to sy\). Upward closure of \(U\) would then imply \(sy\in U\), contradicting the hypothesis. Therefore \(y=sx\).

This last statement identifies the edge where a tuple patched from the two tails needs a root-divisibility calculation.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleUnion`: [IntegralPairings.lean:391](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L391).

`OAI.KLInvariance.TitsSpace.BruhatUpper.mem_simpleInter`: [IntegralPairings.lean:406](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L406).

`OAI.KLInvariance.TitsSpace.BruhatUpper.simpleUnion`: [IntegralPairings.lean:419](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L419).

`OAI.KLInvariance.TitsSpace.BruhatUpper.simpleInter`: [IntegralPairings.lean:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L427).

`OAI.KLInvariance.TitsSpace.simpleUnion_stable`: [IntegralPairings.lean:435](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L435).

`OAI.KLInvariance.TitsSpace.simpleInter_stable`: [IntegralPairings.lean:441](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L441).

`OAI.KLInvariance.TitsSpace.cross_edge_is_simple`: [IntegralPairings.lean:447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L447).
