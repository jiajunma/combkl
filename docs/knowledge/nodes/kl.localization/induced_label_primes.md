---
id: kl.local.induced_label_primes
title: Prime induced labels and relative primality at a vertex
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.notes.dihedral_models
- kl.algebra.linear_primes
- kl.realization.root_planes
- kl.detail.root_reflection_correspondence
- kl.detail.structure_sheaves
- kl.local.flow_down_flabbiness
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.inducedLabel_prime
  - OAI.KLInvariance.Dihedral.label_eq_of_induced_dvd
  - OAI.KLInvariance.Dihedral.model_flabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:554
    format: lean-location
    note: OAI.KLInvariance.Dihedral.inducedLabel_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:561
    format: lean-location
    note: OAI.KLInvariance.Dihedral.label_eq_of_induced_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:580
    format: lean-location
    note: OAI.KLInvariance.Dihedral.model_flabby
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read inducedLabel_prime and the complete divisibility-to-reflection argument,
    then the fixed-source edge identification used inside model_flabby. Kept injectivity
    only for label identification and relative primality, and restricted the distinct-edge
    conclusion to a common source.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Prime induced labels and relative primality at a vertex

Let \(H\) be a two-generator Coxeter system, \(W\) a finite-generator Coxeter system, and \(\phi:H\to W\) a group homomorphism carrying reflections to reflections. For an edge \(e:x\to y\) in \([1,b]_H\), write \(\tau_e=yx^{-1}\). Its induced ambient label is \(\alpha_e=\Lambda(i_0\beta_e)\), where \(\beta_e\) is the canonical positive ambient root representing \(\phi(\tau_e)\), \(i_0\) embeds the original root space into the extended realization, and \(\Lambda\) takes vectors to their linear polynomials in the ambient coefficient algebra \(A\). Every \(\alpha_e\) is prime in \(A\).

If \(\phi\) is injective and \(\alpha_e\mid\alpha_f\), then the intrinsic reflection labels of \(e,f\) are equal. Consequently, for an injective \(\phi\), distinct edges with the same source have relatively prime polynomial labels.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prove primality of each label

Write \(\beta_e\) for the canonical positive ambient root representing \(\phi(\tau_e)\). It is nonzero. The embedding \(i_0\) is injective, so \(i_0\beta_e\ne0\).

The [[node:kl.algebra.linear_primes|linear-prime theorem]] makes \(\iota(i_0\beta_e)\) prime in the symmetric algebra. The polynomial coordinate isomorphism carries it to \(\alpha_e\), preserving primality.

### Step 2. Recover the root from divisibility

Suppose \(\alpha_e\mid\alpha_f\). Transport this divisibility back through the coordinate isomorphism. The [[node:kl.algebra.linear_primes|linear-generator divisibility theorem]] gives
\[
i_0\beta_f\in\mathbb R(i_0\beta_e).
\]
Projecting to the original root space gives
\(\beta_f=r\beta_e\) for some real \(r\).

Distinct positive roots are independent, so the two positive roots must be equal. The positive-root/reflection correspondence therefore gives
\[
\phi(\tau_e)=\phi(\tau_f).
\]
Injectivity of \(\phi\) yields \(\tau_e=\tau_f\).

### Step 3. Use the common source to identify an edge

If \(e,f\) have the same source \(x\) and \(\tau_e=\tau_f\), their targets are both \(\tau_ex\). Thus their endpoint pairs agree, so \(e=f\).

For distinct edges with the same source, Step 2 therefore rules out \(\alpha_e\mid\alpha_f\).

### Step 4. Prove relative primality

A prime polynomial is irreducible. Any nonunit divisor of \(\alpha_e\) is consequently associated to \(\alpha_e\).

If a nonunit divided both \(\alpha_e\) and \(\alpha_f\), this association would imply \(\alpha_e\mid\alpha_f\), contradicting Step 3. Hence every common divisor is a unit, which is relative primality.

In particular the labels in each supported outgoing set \(\operatorname{Out}_c(x)\) are pairwise relatively prime. This is the precise input to the [[node:kl.local.flow_down_flabbiness|flow-down flabbiness theorem]].

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.inducedLabel_prime`: [DihedralIntervals.lean:554](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L554).

`OAI.KLInvariance.Dihedral.label_eq_of_induced_dvd`: [DihedralIntervals.lean:561](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L561).

`OAI.KLInvariance.Dihedral.model_flabby`: [DihedralIntervals.lean:580](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L580).
