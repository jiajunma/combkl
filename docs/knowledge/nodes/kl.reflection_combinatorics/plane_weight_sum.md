---
id: kl.geometry.plane_weight_sum
title: The geometric plane-weight sum equals the excess length
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.geometry.plane_weights
- kl.detail.root_inversion_count
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source root-sign and finiteness hypotheses retained?
  verdict: The definitions apply to any x and positive alpha in finite generator rank;
    the theorem states the noninversion hypothesis used in the sign argument.
tags:
- Kazhdan-Lusztig
- root-geometry
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.negative_pair_not_both
  - OAI.KLInvariance.TitsSpace.rootChange_pair
  - OAI.KLInvariance.TitsSpace.planeDefect_eq_double_weight
  - OAI.KLInvariance.TitsSpace.sum_planeWeight
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:267
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.negative_pair_not_both
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:469
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootChange_pair
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:596
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeDefect_eq_double_weight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:621
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.sum_planeWeight
---

# The geometric plane-weight sum equals the excess length

Let \((W,S)\) have finitely many simple generators. Fix \(x\in W\) and \(\alpha\in\Phi^+\) with \(x^{-1}\alpha\) positive, and put \(y=r_\alpha x\). For the geometric plane weights,
\[
D_P(x,y;\alpha)=2k_P(x,\alpha)
\]
for every plane \(P\), and
\[
2\sum_P k_P(x,\alpha)=\ell(y)-\ell(x)-1.
\]

*Proof.*

### Step 1. Count the total change and the distinguished root

Put \(\Delta(\beta)=n_y(\beta)-n_x(\beta)\). The inversion-count theorem gives
\[
\sum_\beta\Delta(\beta)=\ell(y)-\ell(x).
\]
The identity \(y^{-1}=x^{-1}r_\alpha\) gives \(y^{-1}\alpha=-x^{-1}\alpha\). By hypothesis the latter is negative. Thus \(n_x(\alpha)=0\), \(n_y(\alpha)=1\), and \(\Delta(\alpha)=1\).

Removing the distinguished root leaves
\[
\sum_{\beta\ne\alpha}\Delta(\beta)=\ell(y)-\ell(x)-1.
\]

### Step 2. Calculate each partner pair

If \(r_\alpha\beta\) is positive, it equals \(\beta^*\), and \(r_\alpha\beta^*=\beta\). Consequently
\[
n_y(\beta)=n_x(\beta^*),\qquad
n_y(\beta^*)=n_x(\beta).
\]
Adding the two changes gives zero.

If \(r_\alpha\beta\) is negative, it equals \(-\beta^*\), and \(r_\alpha\beta^*=-\beta\). Therefore
\[
n_y(\beta)=1-n_x(\beta^*),\qquad
n_y(\beta^*)=1-n_x(\beta),
\]
so
\[
\Delta(\beta)+\Delta(\beta^*)
=2-2\bigl(n_x(\beta)+n_x(\beta^*)\bigr).
\]

The two indicators on the right cannot both be one. To see this, use
\[
\beta+\beta^*=c\alpha,\qquad c=B(\alpha,\beta)>0.
\]
If \(x^{-1}\beta\) and \(x^{-1}\beta^*\) were both negative, applying \(x^{-1}\) would make the left side coordinatewise nonpositive. The right side is \(c\,x^{-1}\alpha\), which is nonzero and coordinatewise nonnegative. At a coordinate where \(x^{-1}\alpha\) is positive the equality is impossible.

Thus a flipped pair contributes two when both indicators are zero, and zero when exactly one is one. These are precisely the contributing pairs in the definition.

### Step 3. Show that a contributing root has a distinct partner

Suppose \(\beta^*=\beta\) in the flipped case. Then \(2\beta=c\alpha\), with \(c>0\). Both roots have squared Tits norm two. Substituting \(\beta=(c/2)\alpha\) into that norm equation gives \((c/2)^2=1\); positivity gives \(c/2=1\). Hence \(\beta=\alpha\).

After excluding \(\alpha\), each contributing orbit therefore has exactly two elements. Injectivity of the slope gives unequal slopes for them, and exactly one satisfies the half-root inequality.

A fixed root in the positive case has \(\Delta(\beta)=0\) by Step 2, so it contributes nothing.

### Step 4. Sum within a plane

Taking partners preserves the plane spanned with \(\alpha\). Group the changes in a fixed plane into partner orbits. This can be done on a finite set: start with the support of \(\Delta\), add its partner images, and remove \(\alpha\).

Every noncontributing orbit has total change zero. Every contributing orbit has total change two, and it contains one half-root. Therefore the sum in that plane is exactly twice the number of its half-roots:
\[
D_P(x,y;\alpha)=2k_P(x,\alpha).
\]

### Step 5. Sum over the planes

Only finitely many weights are nonzero. Each root different from \(\alpha\) belongs to the unique plane specified in the definition of the defect, so summing Step 4 and then using Step 1 gives
\[
2\sum_P k_P(x,\alpha)
=\sum_P D_P(x,y;\alpha)
=\ell(y)-\ell(x)-1.
\]

## References

The local root-sign and plane-weight calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.negative_pair_not_both`: [ReflectionSchedules.lean:267](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L267).

`OAI.KLInvariance.TitsSpace.rootChange_pair`: [ReflectionSchedules.lean:469](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L469).

`OAI.KLInvariance.TitsSpace.planeDefect_eq_double_weight`: [ReflectionSchedules.lean:596](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L596).

`OAI.KLInvariance.TitsSpace.sum_planeWeight`: [ReflectionSchedules.lean:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L621).
