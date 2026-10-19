---
id: kl.local.orbit_spline_factors
title: Orbit-spline factors with prescribed zeros
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.orbit_splines
- kl.realization.form_pair_surjective
- kl.notes.extended_realization
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.Represents.independent_of_ne
  - OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne
  - OAI.KLInvariance.TitsSpace.exists_pair_vector
  - OAI.KLInvariance.TitsSpace.orbitSpline_single_factor
  - OAI.KLInvariance.TitsSpace.orbitSpline_pair_factor
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1983
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.independent_of_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1998
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:162
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_pair_vector
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:193
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.orbitSpline_single_factor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:176
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.orbitSpline_pair_factor
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the single-factor vector, root-independence norm argument, extended
    normal-form independence, prescribed (-1,0) pair and three value calculations.
    Kept both representing-root hypotheses, the group product directions and x!=z.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Orbit-spline factors with prescribed zeros

Fix the extended realization \(V\) and polynomial coefficient map \(\Lambda\) of a finite-generator Coxeter system.

Suppose \(xy^{-1}=t\), and a root \(a\) represents \(t\). There exists \(v_0\in V\) such that
\[
F_{y,v_0}(x)=\lambda(a),\qquad F_{y,v_0}(y)=0.
\]

If additionally \(zy^{-1}=r\), a root \(d\) represents \(r\), and \(x\ne z\), then \(v_0\) can be chosen so that also
\[
F_{y,v_0}(z)=0.
\]
Here \(\lambda(a)=\Lambda(i_0a)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct a factor with one prescribed zero

A representing root has squared norm two in the extended form:
\(\widetilde B(i_0a,i_0a)=2\).
Take
\[
v_0=-\tfrac12 i_0a.
\]
Then \(\widetilde B(i_0a,v_0)=-1\). Since \(xy^{-1}=t\),
\[
\rho(xy^{-1})v_0-v_0
=-\widetilde B(i_0a,v_0)i_0a=i_0a.
\]
Applying \(\Lambda\) gives the required value \(\lambda(a)\) at \(x\). The orbit spline vanishes at \(y\) by definition.

### Step 2. Prove independence of the two representing roots

For the two-zero construction, \(x\ne z\) implies \(t\ne r\): equality of \(xy^{-1}\) and \(zy^{-1}\) would give \(x=z\).

Both roots are nonzero because their squared norms are two. A dependence would therefore have the form \(d=ca\). The norm equation gives
\[
2=\widetilde B(i_0d,i_0d)=2c^2,
\]
hence \(c=1\) or \(c=-1\). The roots \(a\) and \(-a\) represent the same reflection. Uniqueness of the reflection represented by a root would therefore give \(r=t\), a contradiction.

Thus \(a,d\) are independent, and the injective embedding makes \(i_0a,i_0d\) independent in \(V\).

### Step 3. Prescribe the two normal forms

Define
\[
n_a(v)=\widetilde B(i_0a,v),\qquad
n_d(v)=\widetilde B(i_0d,v).
\]
If \(p n_a+q n_d=0\), then
\(\widetilde B(p\,i_0a+q\,i_0d,v)=0\) for every \(v\).
Nondegeneracy of the extended form gives
\(p\,i_0a+q\,i_0d=0\), and Step 2 gives \(p=q=0\).

The two normal forms are therefore independent. The [[node:kl.realization.form_pair_surjective|independent-form surjectivity theorem]] supplies \(v_0\in V\) with
\[
n_a(v_0)=-1,\qquad n_d(v_0)=0.
\]
This is the source's exists_pair_vector construction.

### Step 4. Evaluate the three spline values

At \(x\), the first normal value gives the displacement \(i_0a\), exactly as in Step 1. Thus \(F_{y,v_0}(x)=\lambda(a)\).

At \(y\), the displacement is zero.

At \(z\), use \(zy^{-1}=r\) and the second normal value:
\[
\rho(r)v_0-v_0=-n_d(v_0)i_0d=0.
\]
Hence \(F_{y,v_0}(z)=0\).

The nondegenerate extended form supplies the independent normal equations used in this interpolation factor.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.Represents.independent_of_ne`: [Tits.lean:1983](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1983).

`OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne`: [Tits.lean:1998](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1998).

`OAI.KLInvariance.TitsSpace.exists_pair_vector`: [DihedralIntervals.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L162).

`OAI.KLInvariance.TitsSpace.orbitSpline_single_factor`: [DihedralIntervals.lean:193](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L193).

`OAI.KLInvariance.TitsSpace.orbitSpline_pair_factor`: [DihedralIntervals.lean:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176).
