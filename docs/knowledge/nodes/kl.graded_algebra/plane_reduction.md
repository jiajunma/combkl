---
id: kl.algebra.plane_reduction
title: Reduction of a plane along one direction
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.PlaneReduction.scalar_reduction
  - OAI.KLInvariance.PlaneReduction.associated_reduction
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1268
    format: lean-location
    note: OAI.KLInvariance.PlaneReduction.scalar_reduction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1281
    format: lean-location
    note: OAI.KLInvariance.PlaneReduction.associated_reduction
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the two PlaneReduction lemmas. Retained arbitrary vector spaces and
    commutative target algebras, extracted the nonzero transverse coefficient and
    exhibited its inverse in the target; the scalar-image consequence is derived explicitly.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# Reduction of a plane along one direction

Let \(k\) be a field, \(V\) a \(k\)-vector space, \(S\) a commutative \(k\)-algebra, and \(l:V\to S\) a \(k\)-linear map. Let \(a,b,c\in V\) satisfy
\[
l(a)=0,\qquad
c\in\operatorname{span}_k\{a,b\},\qquad
c\notin ka.
\]
Then there is \(r\in k\), \(r\ne0\), with
\[
l(c)=r\,l(b).
\]
Here the scalar action is through the algebra map \(k\to S\). Consequently \(l(c)\) and \(l(b)\) are associated scalars: one is a unit multiple of the other.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coefficient maps and scalar reduction.**

**OpenAI notes:** The edge-image proof localizes at the plane prime, passes to the quotient by the current root label, and expresses the remaining plane labels as uniformizers times units in the resulting localized edge ring. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The coefficient operations are explicit tensor and quotient maps. A real-linear reduction kills the current root; writing another root as s*a+r*b gives a nonzero field coefficient r and therefore a unit multiple after reduction. The root-label compatibility formulas identify these elements with the actual polynomial labels. [MinimalExtensions:1239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1239), [PlaneLocalization:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1315), [PlaneLocalization:1268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1268), [PlaneLocalization:1330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1330), [PlaneLocalization:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1555).

**Role in the proof:** The reduced-label comparison is an equality up to an explicitly obtained unit. Later product arguments use associated elements in the localized quotient ring to compare actual scalar-image submodules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Write the two spanning coefficients

Membership in the two-vector span gives scalars \(s,r\in k\) with
\[
c=sa+rb.
\]
If \(r=0\), this becomes \(c=sa\in ka\), contradicting the hypothesis. Hence \(r\ne0\).

### Step 2. Apply the linear map

Linearity and \(l(a)=0\) give
\[
l(c)=s\,l(a)+r\,l(b)=r\,l(b).
\]
This is scalar_reduction, with the nonzero coefficient from Step 1.

### Step 3. Exhibit the unit in the target algebra

Let \(u\) be the image of \(r\) in \(S\). The image of \(r^{-1}\) is its inverse, since
\[
u\,\operatorname{algebraMap}(r^{-1})
=\operatorname{algebraMap}(rr^{-1})=1.
\]
Thus \(u\) is a unit and \(l(c)=u\,l(b)\), proving associated_reduction.

### Step 4. Interpret the equality on scalar images

For any \(S\)-module \(M\), a unit acts bijectively. Therefore
\[
l(c)M=u\,l(b)M=l(b)M.
\]
Explicitly, \(l(c)m=l(b)(um)\), while
\(l(b)m=l(c)(u^{-1}m)\). These give both inclusions.

For example, if \(c=3a+2b\) over \(\mathbb R\) and \(l(a)=0\), then \(l(c)=2l(b)\). The unit is the image of the scalar \(2\), with inverse the image of \(1/2\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.PlaneReduction.scalar_reduction`: [PlaneLocalization.lean:1268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1268).

`OAI.KLInvariance.PlaneReduction.associated_reduction`: [PlaneLocalization.lean:1281](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1281).
