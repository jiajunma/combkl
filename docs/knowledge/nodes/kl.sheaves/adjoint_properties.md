---
id: kl.sheaves.adjoint_properties
title: Composition, balance, and grading of adjoints
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.integral_adjoints
- kl.algebra.perfect_inverse_degree
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - IntegralPairings
  declarations:
  - OAI.PerfectAdjoint.adjoint_comp
  - OAI.PerfectAdjoint.adjoint_idempotent
  - OAI.PerfectAdjoint.commutes_of_balanced
  - OAI.PerfectAdjoint.symmetric_pairing
  - OAI.PerfectAdjoint.adjoint_adjoint
  - OAI.PerfectAdjoint.adjoint_zero
  - OAI.KLInvariance.Graded.adjoint_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2228
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_comp
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2238
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_idempotent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2245
    format: lean-location
    note: OAI.PerfectAdjoint.commutes_of_balanced
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2253
    format: lean-location
    note: OAI.PerfectAdjoint.symmetric_pairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2257
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_adjoint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1691
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2340
    format: lean-location
    note: OAI.KLInvariance.Graded.adjoint_homogeneous
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

# Composition, balance, and grading of adjoints

Let \(D:M\xrightarrow{\sim}M^*\) be a perfect pairing over a commutative ring \(R\), and define adjoints by
\(\langle f^*m,n\rangle=\langle m,fn\rangle\). Composition is written \(fg=f\circ g\). Then
\[
(fg)^*=g^*f^*,\qquad 0^*=0.
\]
In particular, \(f^2=f\) implies \((f^*)^2=f^*\).

If the pairing is symmetric, then
\[
\langle m,f^*n\rangle=\langle fm,n\rangle,\qquad
(f^*)^*=f.
\]
If an operator \(t\) is balanced, meaning
\(\langle tm,n\rangle=\langle m,tn\rangle\), and \(ft=tf\), then \(f^*t=tf^*\).

Finally suppose \(R=A\) is a graded algebra over a field, \(M\) has an integer grading, and
\(\langle M_i,M_j\rangle\subseteq A_{i+j-L}\).
If \(f\) preserves degrees, then \(f^*\) preserves degrees.

*Proof.*

### Step 1. Detect equality by pairing

If \(\langle u,n\rangle=\langle v,n\rangle\) for every \(n\), then \(D(u)=D(v)\). Injectivity of \(D\) gives \(u=v\). We use this test for the operator identities.

### Step 2. Reverse a composition

For arbitrary \(m,n\),
\[
\begin{aligned}
\langle(fg)^*m,n\rangle
&=\langle m,f(gn)\rangle\\
&=\langle f^*m,gn\rangle\\
&=\langle g^*f^*m,n\rangle.
\end{aligned}
\]
Step 1 proves \((fg)^*=g^*f^*\). Likewise
\(\langle0^*m,n\rangle=\langle m,0\rangle=0\), so \(0^*=0\).
Taking \(g=f\) and \(f^2=f\) gives
\((f^*)^2=(f^2)^*=f^*\).

### Step 3. Use symmetry for the double adjoint

Symmetry and the adjoint equation yield
\[
\langle m,f^*n\rangle
=\langle f^*n,m\rangle
=\langle n,fm\rangle
=\langle fm,n\rangle.
\]
Consequently
\[
\langle(f^*)^*m,n\rangle=\langle m,f^*n\rangle=\langle fm,n\rangle.
\]
Step 1 gives \((f^*)^*=f\).

### Step 4. Transport commutation with a balanced operator

For every \(m,n\),
\[
\begin{aligned}
\langle f^*tm,n\rangle
&=\langle tm,fn\rangle\\
&=\langle m,tfn\rangle\\
&=\langle m,ftn\rangle\\
&=\langle f^*m,tn\rangle\\
&=\langle tf^*m,n\rangle.
\end{aligned}
\]
The second and last equalities use balance, and the middle equality uses \(tf=ft\). Step 1 proves commutation of \(f^*\) and \(t\).

### Step 5. Recover the adjoint's degree from its functional

Let \(m\in M_n\). The functional
\(\lambda(v)=\langle m,fv\rangle\) sends \(M_j\) into \(A_{n+j-L}\), because \(f\) preserves degrees. In the convention \(\lambda(M_j)\subseteq A_{j+r}\), it has degree \(r=n-L\).

The homogeneous-representative theorem therefore gives
\[
f^*m=D^{-1}(\lambda)\in M_{(n-L)+L}=M_n.
\]
This proves degree preservation.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.PerfectAdjoint.adjoint_comp`: [IntegralPairings.lean:2228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2228).

`OAI.PerfectAdjoint.adjoint_idempotent`: [IntegralPairings.lean:2238](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2238).

`OAI.PerfectAdjoint.commutes_of_balanced`: [IntegralPairings.lean:2245](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2245).

`OAI.PerfectAdjoint.symmetric_pairing`: [IntegralPairings.lean:2253](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2253).

`OAI.PerfectAdjoint.adjoint_adjoint`: [IntegralPairings.lean:2257](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2257).

`OAI.PerfectAdjoint.adjoint_zero`: [BalancedPairings.lean:1691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1691).

`OAI.KLInvariance.Graded.adjoint_homogeneous`: [IntegralPairings.lean:2340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2340).
