---
id: kl.local.orbit_spline_congruence
title: The reflection congruence of an orbit spline
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.orbit_splines
- kl.detail.root_reflection_correspondence
- kl.realization.extended_action
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.orbitSpline_self
  - OAI.KLInvariance.TitsSpace.orbitSpline_reflection
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:144
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.orbitSpline_self
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:147
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.orbitSpline_reflection
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact displacement calculation in orbitSpline_reflection and its
    coefficient c. Retained a general representing root, the left reflection action
    and the order x*y^-1 before taking the polynomial image.
tags:
- Kazhdan-Lusztig
- interpolation
---

# The reflection congruence of an orbit spline

Fix the extended realization and coefficient map \(\Lambda:V\to A\) of a finite-generator Coxeter system. Let \(F_{y,v_0}\) be an orbit spline.

Suppose a root \(a\) represents the reflection \(t\), and write
\(\widetilde a=i_0a\), \(\lambda(a)=\Lambda(\widetilde a)\). For every \(x\in W\),
\[
F_{y,v_0}(x)-F_{y,v_0}(tx)
=\widetilde B\bigl(\widetilde a,\rho(xy^{-1})v_0\bigr)\lambda(a).
\]
Thus \(\lambda(a)\) divides the difference. Also \(F_{y,v_0}(y)=0\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the represented reflection to the translated vector

Put \(u=\rho(xy^{-1})v_0\) and
\(c=\widetilde B(\widetilde a,u)\in\mathbb R\).
The action law and the reflection formula give
\[
\rho(txy^{-1})v_0=\rho(t)u=u-c\widetilde a.
\]

### Step 2. Subtract the two displacement vectors

The vectors defining the two spline values are \(u-v_0\) and
\(u-c\widetilde a-v_0\). Their difference is \(c\widetilde a\). By linearity,
\[
\begin{aligned}
F_{y,v_0}(x)-F_{y,v_0}(tx)
&=\Lambda(c\widetilde a)\\
&=c\,\Lambda(\widetilde a)=c\,\lambda(a).
\end{aligned}
\]
The scalar \(c\) acts through the constant-polynomial map \(\mathbb R\to A\), so this is a polynomial multiple of the root label.

### Step 3. Read the congruence and the reference value

The displayed factorization is precisely equality of the two spline values in \(A/(\lambda(a))\).

At \(x=y\), the definition uses \(\rho(1)v_0-v_0=0\), giving \(F_{y,v_0}(y)=0\). These are orbitSpline_reflection and orbitSpline_self.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.orbitSpline_self`: [DihedralIntervals.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L144).

`OAI.KLInvariance.TitsSpace.orbitSpline_reflection`: [DihedralIntervals.lean:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L147).
