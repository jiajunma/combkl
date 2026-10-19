---
id: kl.dihedral.induced_reflections_length
title: Reflections, length, and reflection edges of the induced plane system
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.induced_inversions
- kl.realization.plane_reflection_membership
- kl.dihedral.plane_length
- kl.detail.root_inversion_count
- kl.foundations.bruhat_step
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.inversionEquiv
  - OAI.KLInvariance.TitsSpace.PlaneBasis.length_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.leftInversion_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.bruhatStep_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1058
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1083
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.inversionEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1108
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.length_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1141
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.leftInversion_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1153
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.bruhatStep_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Reflections, length, and reflection edges of the induced plane system

Let \(D_P\) have the Coxeter system constructed from a plane basis of a root plane \(P\). Then:

- An element of \(D_P\) is an intrinsic reflection exactly when it is an ambient reflection in \(W\).
- For \(w\in D_P\), its intrinsic length is the ambient plane inversion count:
  \[
  \ell_P(w)=L_P(w).
  \]
- Left inversions agree in the two systems for \(w,t\in D_P\).
- For \(g,h\in D_P\), a directed intrinsic reflection edge \(g\to h\) is exactly an ambient directed reflection edge between those same elements.

*Proof.*

### Step 1. Send intrinsic reflections to ambient reflections

An intrinsic reflection is a conjugate \(u s_i u^{-1}\) of an induced simple reflection. The two simple reflections are the ambient reflections of the plane endpoints.

The inclusion \(D_P\hookrightarrow W\) preserves products and inverses, and ambient reflections are closed under conjugation. Thus every intrinsic reflection is an ambient one.

### Step 2. Recover intrinsic reflections from ambient ones

Let \(t\in D_P\) be an ambient reflection, and let \(a\) be its positive representing root. The [[node:kl.realization.plane_reflection_membership|reflection-membership theorem]] gives \(a\in P\).

Since \(t^{-1}=t\) and \(t(a)=-a\), the root \(a\) is negative under \(t^{-1}\). Apply the [[node:kl.dihedral.induced_inversions|induced inversion-sign theorem]] with \(w=t\). It makes \(t\) an intrinsic left inversion of itself, which in particular makes it an intrinsic reflection.

### Step 3. Construct the inversion bijection and count it

For fixed \(w\in D_P\), send a positive plane root inverted by \(w\) to its reflection:
\[
a\longmapsto r_a\in D_P.
\]
The sign theorem makes this an intrinsic left inversion of \(w\).

Conversely, an intrinsic left inversion \(t\) is an ambient reflection by Step 1. Its unique positive root lies in \(P\), and the sign theorem makes that root an ambient inversion of \(w\). Uniqueness of positive representing roots shows that these two maps are inverse.

The left inversions of a Coxeter element are in bijection with the positions of a reduced word: the inversion sequence lists them without repetition. There are \(\ell_P(w)\) such positions. The other side of our bijection has cardinality \(L_P(w)\). Therefore \(L_P(w)=\ell_P(w)\).

### Step 4. Compare the two left-inversion conditions

If \(t\) is not an ambient reflection, Step 1 shows it is not an intrinsic reflection, so both left-inversion conditions are false.

Otherwise let \(a\in\Phi^+\cap P\) represent \(t\). The [[node:kl.dihedral.induced_inversions|intrinsic sign theorem]] and the [[node:kl.detail.root_inversion_count|ambient root-sign theorem]] both characterize their respective left-inversion condition by negativity of the same root \(w^{-1}a\). Thus the conditions agree.

### Step 5. Compare directed reflection edges

Suppose \(g\to h\) is an ambient edge, so \(h=tg\) for an ambient reflection \(t\), with \(\ell_W(g)<\ell_W(h)\). Since \(g,h\in D_P\),
\(t=hg^{-1}\in D_P\).
Also \(th=g\), so \(t\) is an ambient left inversion of \(h\).

Steps 2 and 4 make it an intrinsic reflection and an intrinsic left inversion of \(h\). Therefore \(\ell_P(g)<\ell_P(h)\), giving the intrinsic edge.

Conversely, start with an intrinsic edge \(h=tg\). Step 1 makes \(t\) ambient, and Step 4 transfers its left-inversion condition at \(h\), giving the ambient length inequality. The edge relation and its reflection label are the same in both directions.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.reflection_iff`: [Decomposition.lean:1058](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1058).

`OAI.KLInvariance.TitsSpace.PlaneBasis.inversionEquiv`: [Decomposition.lean:1083](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1083).

`OAI.KLInvariance.TitsSpace.PlaneBasis.length_eq`: [Decomposition.lean:1108](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1108).

`OAI.KLInvariance.TitsSpace.PlaneBasis.leftInversion_iff`: [Decomposition.lean:1141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1141).

`OAI.KLInvariance.TitsSpace.PlaneBasis.bruhatStep_iff`: [Decomposition.lean:1153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1153).
