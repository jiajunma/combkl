---
id: kl.dihedral.plane_basis_existence
title: Every root plane has two angular boundary roots
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.plane_basis
- kl.dihedral.angular_extremes_simple
- kl.order.slope_cone
- kl.detail.root_inversion_count
- kl.geometry.plane_weights
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.exists_plane_extreme_inverted
  - OAI.KLInvariance.TitsSpace.PlaneSimple.exists_nonpositive_pair
  - OAI.KLInvariance.TitsSpace.noninverted_ref_of_pairing_nonpos
  - OAI.KLInvariance.TitsSpace.exists_opposite_plane_extreme
  - OAI.KLInvariance.TitsSpace.nonempty_planeBasis
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:456
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_plane_extreme_inverted
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:554
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneSimple.exists_nonpositive_pair
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:566
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.noninverted_ref_of_pairing_nonpos
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:576
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_opposite_plane_extreme
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:627
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.nonempty_planeBasis
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

# Every root plane has two angular boundary roots

Let \(P=P(a,b)\) be spanned by distinct positive roots in a finite-generator Coxeter system. For the chosen geometric slope, there exist distinct positive roots \(p,q\in P\) such that
\[
s(p)\le s(c)\le s(q)\qquad(c\in\Phi^+\cap P).
\]
Their span is \(P\), so they form a plane basis. Both are plane-simple.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same plane subgroup, different construction.**

**OpenAI notes:** The plane lemma invokes the reflection-subgroup theorem to obtain a canonical Coxeter system, then uses positivity in the plane to show that its rank is two. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20).

**Lean (primary):** Finite ambient inversion sets produce angular endpoints. Their plane-simple sign criterion and the plane inversion count prove generation by two endpoint reflections through a count-decreasing conjugation. A two-involution presentation constructs the Coxeter system; the induced signed relation then identifies its inversions. [Decomposition:627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L627), [Decomposition:869](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L869), [Decomposition:906](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L906), [Decomposition:1010](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1010).

**Role in the proof:** The Blueprint follows the endpoint-existence, generation, presentation, and signed-inversion proofs in that order.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Find extrema in a finite inversion set

Consider
\[
S=\{c\in\Phi^+\cap P:r_a(c)\text{ is negative}\}.
\]
The inversion set of the group element \(r_a\) is finite, so \(S\) is finite. It is nonempty because \(r_a(a)=-a\).

Choose \(p\in S\) of minimum slope and \(q\in S\) of maximum slope. We first prove that at least one of these is an extreme among all positive roots in \(P\).

### Step 2. Use convex positivity to obtain a global extreme

Suppose \(p\) is not a global minimum and \(q\) is not a global maximum. Choose positive roots \(l,r\in P\) with
\[
s(l)<s(p)\le s(a)\le s(q)<s(r).
\]
The roots \(l,r\) are distinct and span \(P\). The [[node:kl.order.slope_cone|slope-cone theorem]] expresses
\(a=cl+dr\) with \(c,d>0\).

Neither \(l\) nor \(r\) is inverted by \(r_a\): otherwise it would belong to \(S\), contradicting the chosen minimum or maximum. Their images under \(r_a\) are therefore positive. Convex positivity makes
\(r_a(a)=c\,r_a(l)+d\,r_a(r)\) nonnegative. But \(r_a(a)=-a\) is a nonzero negative root. This is a contradiction.

Hence \(S\) contains a global angular extreme. Rename one such root \(p\). The [[node:kl.dihedral.angular_extremes_simple|angular-extreme theorem]] makes \(p\) plane-simple.

### Step 3. Produce another root with nonpositive pairing against p

The plane has dimension two, so choose a positive root \(r\in P\) different from \(p\).

If \(B(p,r)\le0\), put \(c=r\). If \(B(p,r)>0\), put \(c=r_p(r)\). Plane simplicity makes this image positive, and the reflection formula keeps it in \(P\). It differs from \(p\): otherwise applying \(r_p\) would give \(r=-p\).

In the second case,
\[
B(p,c)=B(p,r)-B(p,r)B(p,p)=-B(p,r)<0.
\]
Thus both cases supply \(c\in\Phi^+\cap P\), \(c\ne p\), and \(B(p,c)\le0\).

### Step 4. Find an extreme different from p

Symmetry of the Tits form gives
\[
r_c(p)=p-B(c,p)c.
\]
Because \(B(c,p)\le0\), this is a nonnegative combination of positive roots, and it is nonzero. Hence \(r_c\) does not invert \(p\).

The roots \(c,p\) span \(P\). Apply Steps 1–2 to this pair, using the inversion set of \(r_c\). We obtain a global angular extreme \(q\in P\) that is inverted by \(r_c\). It cannot equal \(p\).

### Step 5. Put the two extremes in the correct order

If \(p,q\) were both global minima, their extremal inequalities would give \(s(p)=s(q)\), and slope injectivity would give \(p=q\). The same applies to two global maxima.

Thus the two distinct extremes are opposite endpoints. Label the minimum \(p\) and maximum \(q\). Their span is \(P\), because they are distinct positive roots in the same two-dimensional plane. The four plane-basis conditions now hold. The [[node:kl.dihedral.angular_extremes_simple|angular-extreme theorem]] makes both endpoints plane-simple.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.exists_plane_extreme_inverted`: [Decomposition.lean:456](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L456).

`OAI.KLInvariance.TitsSpace.PlaneSimple.exists_nonpositive_pair`: [Decomposition.lean:554](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L554).

`OAI.KLInvariance.TitsSpace.noninverted_ref_of_pairing_nonpos`: [Decomposition.lean:566](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L566).

`OAI.KLInvariance.TitsSpace.exists_opposite_plane_extreme`: [Decomposition.lean:576](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L576).

`OAI.KLInvariance.TitsSpace.nonempty_planeBasis`: [Decomposition.lean:627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L627).
