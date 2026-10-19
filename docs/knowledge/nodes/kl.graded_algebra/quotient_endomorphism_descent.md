---
id: kl.algebra.quotient_endomorphism_descent
title: Descending an endomorphism through projections and edge quotients
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.pair_projection
- kl.detail.graded_maps_shifts
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.LinearDescent.descend
  - OAI.LinearDescent.descend_apply
  - OAI.LinearDescent.descend_idempotent
  - OAI.KLInvariance.Graded.ModuleData.descended
  - OAI.KLInvariance.Graded.ModuleData.lower_kernel_preserved
  - OAI.KLInvariance.Graded.ModuleData.descendedEdge
  - OAI.KLInvariance.Graded.ModuleData.descendedEdge_lower
  - OAI.KLInvariance.Graded.ModuleData.descendedEdge_upper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:603
    format: lean-location
    note: OAI.LinearDescent.descend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:607
    format: lean-location
    note: OAI.LinearDescent.descend_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:613
    format: lean-location
    note: OAI.LinearDescent.descend_idempotent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:637
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.descended
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:646
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.lower_kernel_preserved
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:654
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.descendedEdge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:664
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.descendedEdge_lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:669
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.descendedEdge_upper
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Descending an endomorphism through projections and edge quotients

Let \(f:M\twoheadrightarrow X\) be a surjective linear map over a commutative ring, and let \(h:M\to M\) be an endomorphism preserving \(\ker f\). There is a unique linear map
\[
h_X:X\to X,\qquad h_X(f(m))=f(h(m)).
\]
If \(h\) is idempotent, then \(h_X\) is idempotent. If \(M,X\) are graded and \(f,h\) preserve degrees, then \(h_X\) preserves degrees.

Now let \(g:M\twoheadrightarrow Y\) be another surjection whose kernel is preserved by \(h\). On the pair-projection quotient \(Q\), there is a unique endomorphism \(h_Q\) satisfying
\[
h_Q\ell=\ell h_X,\qquad h_Qu=u h_Y.
\]
For graded maps, all three descended endomorphisms preserve degree.

*Proof.*

### Step 1. Define the map by choosing a lift

For \(x\in X\), choose \(m\) with \(f(m)=x\), and set \(h_X(x)=f(h(m))\).

If \(m'\) is another lift, then \(m-m'\in\ker f\). Kernel preservation gives
\[
f(h(m))-f(h(m'))=f(h(m-m'))=0.
\]
Thus the value is independent of the lift. Lifts of sums and scalar multiples show linearity. Surjectivity of \(f\) also gives uniqueness, because the equation specifies the map on every element of \(X\).

### Step 2. Check idempotence and grading

If \(h^2=h\), then for every \(m\),
\[
h_X^2(f(m))=f(h^2(m))=f(h(m))=h_X(f(m)).
\]
Every \(x\) is some \(f(m)\), so \(h_X^2=h_X\).

Suppose \(x\in X_n\). Choose any lift \(m\), decompose it into homogeneous components, and take \(m_n\). Since \(f\) preserves degree,
\(f(m_n)\) is the degree-\(n\) component of \(f(m)=x\), hence equals \(x\).
Then \(h_X(x)=f(h(m_n))\in X_n\).

The same construction gives \(h_Y\).

### Step 3. Preserve the lower quotient kernel

Suppose \(\ell(x)=0\). The pair-projection kernel description supplies \(m\) with \(f(m)=x\) and \(g(m)=0\). Kernel preservation for \(g\) gives \(g(h(m))=0\), while
\(f(h(m))=h_X(x)\). Applying the same kernel description gives
\(\ell(h_X(x))=0\).

### Step 4. Descend once more to the edge quotient

Surjectivity of \(g\) makes \(\ell:X\to Q\) surjective. Step 3 lets us apply Step 1 to this surjection and \(h_X\), defining
\[
h_Q(\ell(x))=\ell(h_X(x)).
\]
This proves the lower commuting square. The homogeneous-lift argument in Step 2 proves degree preservation.

### Step 5. Check the upper commuting square

Take \(y\in Y\), and choose \(m\) with \(g(m)=y\). Compatibility of the original pair projections and the lower square give
\[
\begin{aligned}
h_Q(u(y))
&=h_Q(u(g(m)))\\
&=h_Q(\ell(f(m)))\\
&=\ell(h_X(f(m)))\\
&=\ell(f(h(m)))\\
&=u(g(h(m)))\\
&=u(h_Y(g(m)))=u(h_Y(y)).
\end{aligned}
\]
This proves the upper square. Uniqueness of \(h_Q\) follows from surjectivity of \(\ell\).

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.LinearDescent.descend`: [BalancedPairings.lean:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L603).

`OAI.LinearDescent.descend_apply`: [BalancedPairings.lean:607](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L607).

`OAI.LinearDescent.descend_idempotent`: [BalancedPairings.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L613).

`OAI.KLInvariance.Graded.ModuleData.descended`: [BalancedPairings.lean:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L637).

`OAI.KLInvariance.Graded.ModuleData.lower_kernel_preserved`: [BalancedPairings.lean:646](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L646).

`OAI.KLInvariance.Graded.ModuleData.descendedEdge`: [BalancedPairings.lean:654](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L654).

`OAI.KLInvariance.Graded.ModuleData.descendedEdge_lower`: [BalancedPairings.lean:664](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L664).

`OAI.KLInvariance.Graded.ModuleData.descendedEdge_upper`: [BalancedPairings.lean:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L669).
