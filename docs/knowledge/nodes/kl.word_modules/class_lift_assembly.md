---
id: kl.word.class_lift_assembly
title: Assembling class lifts with one prime denominator
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.residue_class_projector
- kl.word.character_congruence
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.FiniteCharacterLocalization.partition_local_denominator
  - OAI.KLInvariance.FiniteCharacterLocalization.character_local_denominator
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1761
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.partition_local_denominator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1833
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.character_local_denominator
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read partition_local_denominator and its quotient-set application. Wrote
    the product-excluding-one-class coefficients and the coordinatewise single surviving
    summand explicitly.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Assembling class lifts with one prime denominator

Let \(R\) be a commutative ring, \(X\) a finite index set,
\(L\subseteq\prod_{x\in X}E_x\) a submodule, and \(\chi_a\) a family of stable weights. Fix a prime element \(p\) and a tuple \(z\in\prod_xE_x\).

Suppose each residue class has a lift in \(L\): for every \(x\in X\), there exists \(m\in L\) with
\[
m_y=z_y\qquad\text{whenever }x\sim_p y.
\]
Then there is \(D\in R\) such that
\[
p\nmid D,\qquad Dz\in L.
\]

The assembly calculation itself applies to an arbitrary index set \(X\) partitioned by a finite set \(Q\), whenever the stable weights and matching vectors in Steps 2–3 are supplied. The residue-class application below obtains such a finite partition from finite \(X\).

*Proof.*

### Step 1. Index the finitely many classes

Let \(Q=X/{\sim_p}\), and let \(q:X\to Q\) send an index to its class. Since \(X\) is finite, \(Q\) is finite.

For each class \(j\), choose one representative. The lifting hypothesis gives
\(m_j\in L\) whose coordinates agree with \(z\) on that class.

### Step 2. Select each class by a stable diagonal operator

The [[node:kl.word.residue_class_projector|residue-class projector theorem]] gives, for each \(j\), a scalar \(d_j\) and stable weight \(g_j\) such that
\[
p\nmid d_j,\qquad
g_j(x)=
\begin{cases}
d_j,&q(x)=j,\\
0,&q(x)\ne j.
\end{cases}
\]
Thus \(D_{g_j}m_j\) belongs to \(L\), equals \(d_jz_x\) on class \(j\), and is zero on all other classes.

### Step 3. Form a common scalar and a sum of class vectors

Put
\[
D=\prod_{j\in Q}d_j,\qquad
v=\sum_{j\in Q}\left(\prod_{k\ne j}d_k\right)D_{g_j}m_j.
\]
Every summand lies in \(L\), so \(v\in L\). Each \(d_j\) is not divisible by \(p\); primality gives \(p\nmid D\).

### Step 4. Evaluate the sum at one coordinate

Fix \(x\in X\), and put \(j_0=q(x)\). Every summand with \(j\ne j_0\) is zero at \(x\). The remaining one has value
\[
\left(\prod_{k\ne j_0}d_k\right)d_{j_0}z_x=Dz_x.
\]
Hence \(v=Dz\), proving \(Dz\in L\).

This is the source's partition_local_denominator calculation. It applies to any finite partition for which the displayed stable weights and matching vectors are supplied. The residue classes and their projectors provide those data in character_local_denominator. Empty products and sums give the same conclusion when \(X\) is empty.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteCharacterLocalization.partition_local_denominator`: [IntegralPairings.lean:1761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1761).

`OAI.KLInvariance.FiniteCharacterLocalization.character_local_denominator`: [IntegralPairings.lean:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833).
