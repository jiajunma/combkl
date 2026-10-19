---
id: kl.algebra.projective_range_splittings
title: Descent maps and projective image splittings
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.ProjectiveRange.descend
  - OAI.KLInvariance.ProjectiveRange.descend_apply
  - OAI.KLInvariance.ProjectiveRange.projective_of_end
  - OAI.KLInvariance.ProjectiveRange.kernelRetraction
  - OAI.KLInvariance.ProjectiveRange.kernel_projective
  - OAI.KLInvariance.ProjectiveRange.splitEquiv
  - OAI.KLInvariance.ProjectiveRange.projective_of_kernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:490
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.descend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:494
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.descend_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:500
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.projective_of_end
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:509
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.kernelRetraction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:515
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.kernel_projective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:526
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.splitEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:541
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.projective_of_kernel
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the general kernel descent, projective image criterion and both kernel/splitting
    arguments. Expanded lift independence and the actual section and retraction formulas.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Descent maps and projective image splittings

Let \(R\) be a commutative ring and \(q:M\to P\) a surjective linear map.

If \(M\) is projective and an endomorphism \(e:M\to M\) satisfies
\[
q(e(m))=q(m),\qquad q(m)=0\Longrightarrow e(m)=0,
\]
then \(P\) is projective.

For the same surjection, the following split-sequence facts also hold:

- if \(M,P\) are projective, then \(\ker q\) is projective;
- if \(P,\ker q\) are projective, then \(M\) is projective.

*Proof.*

### Step 1. Descend a map through a surjection

More generally, let \(g:M\to Q\) be linear and assume \(\ker q\subseteq\ker g\). For \(p\in P\), choose \(m\) with \(q(m)=p\), and define \(\bar g(p)=g(m)\).

If \(q(m')=p\) too, then \(m-m'\in\ker q\), so \(g(m-m')=0\) and \(g(m)=g(m')\). Thus the value is independent of the lift. To check addition, lift \(p,p'\) by \(m,m'\); then \(m+m'\) lifts \(p+p'\), giving \(\bar g(p+p')=\bar g(p)+\bar g(p')\). A scalar multiple \(rm\) similarly proves scalar linearity.

The descended map satisfies \(\bar gq=g\). It is unique because \(q\) is surjective. This is ProjectiveRange.descend.

### Step 2. Descend the endomorphism to a section

Apply Step 1 to \(g=e\). Its second hypothesis gives the needed kernel containment. The resulting map \(\bar e:P\to M\) satisfies
\[
q\bar e(q(m))=q(e(m))=q(m).
\]
Surjectivity of \(q\) therefore gives \(q\bar e=1_P\). Thus \(P\) is a direct summand of the projective module \(M\), and is projective.

### Step 3. Construct the kernel retraction

Suppose \(P\) is projective. Lift \(1_P\) through \(q\) to obtain a section \(\sigma:P\to M\) with \(q\sigma=1_P\).

Define
\[
r:M\to\ker q,\qquad r(m)=m-\sigma(q(m)).
\]
This vector lies in the kernel because
\(q(m)-q\sigma(q(m))=0\).
For \(k\in\ker q\), \(r(k)=k-\sigma(0)=k\). Hence \(r\) retracts the kernel inclusion.

If \(M\) is projective, its direct summand \(\ker q\) is projective. This proves the second claim.

### Step 4. Exhibit the splitting isomorphism

The maps
\[
m\longmapsto(r(m),q(m)),\qquad
(k,p)\longmapsto k+\sigma(p)
\]
are inverse linear maps between \(M\) and \(\ker q\oplus P\).
For \(m\), the returned vector is \(m-\sigma(q(m))+\sigma(q(m))=m\).
For \((k,p)\), applying \(q\) gives \(p\), and subtracting \(\sigma(p)\) leaves \(k\).

If both \(\ker q\) and \(P\) are projective, their direct sum is projective, so this isomorphism proves that \(M\) is projective.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ProjectiveRange.descend`: [IntegralPairings.lean:490](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L490).

`OAI.KLInvariance.ProjectiveRange.descend_apply`: [IntegralPairings.lean:494](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L494).

`OAI.KLInvariance.ProjectiveRange.projective_of_end`: [IntegralPairings.lean:500](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L500).

`OAI.KLInvariance.ProjectiveRange.kernelRetraction`: [IntegralPairings.lean:509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L509).

`OAI.KLInvariance.ProjectiveRange.kernel_projective`: [IntegralPairings.lean:515](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L515).

`OAI.KLInvariance.ProjectiveRange.splitEquiv`: [IntegralPairings.lean:526](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L526).

`OAI.KLInvariance.ProjectiveRange.projective_of_kernel`: [IntegralPairings.lean:541](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L541).
