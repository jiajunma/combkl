---
id: kl.word.trace_restriction_duality
title: Recovering linear functionals through a Frobenius trace
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.frobenius_data
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.restrictDual
  - OAI.KLInvariance.FrobeniusDuality.fiber
  - OAI.KLInvariance.FrobeniusDuality.trace_recover_fiber
  - OAI.KLInvariance.FrobeniusDuality.recover_fiber_smul
  - OAI.KLInvariance.FrobeniusDuality.recoverDual
  - OAI.KLInvariance.FrobeniusDuality.restrict_recover
  - OAI.KLInvariance.FrobeniusDuality.recover_restrict
  - OAI.KLInvariance.FrobeniusDuality.restrictionEquiv
  - OAI.KLInvariance.FrobeniusDuality.restrictionEquiv_apply
  - OAI.KLInvariance.FrobeniusDuality.restrictPairing
  - OAI.KLInvariance.FrobeniusDuality.restrictPairing_apply
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:112
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:117
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.fiber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:124
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.trace_recover_fiber
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:129
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.recover_fiber_smul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:139
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.recoverDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:152
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrict_recover
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:158
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.recover_restrict
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:168
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictionEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:175
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictionEquiv_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:180
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:183
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictPairing_apply
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Followed restrictDual/fiber/recoverDual and both inverse identities line
    by line. Included the A-linearity proof by evaluation through D and retained the
    theorem for arbitrary M without finite-free assumptions.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Recovering linear functionals through a Frobenius trace

Let \(\eta:R\to A\) be an algebra map between commutative rings. Let \(t:A\to R\) and
\(D:A\xrightarrow{\sim}\operatorname{Hom}_R(A,R)\) be trace-duality data:
\[
D(a)(b)=t(ab).
\]
Let \(M\) be an \(A\)-module, regarded as an \(R\)-module by \(r m=\eta(r)m\). Then
\[
T:\operatorname{Hom}_A(M,A)\xrightarrow{\sim}
  \operatorname{Hom}_R(M,R),\qquad T(\lambda)=t\circ\lambda
\]
is an \(R\)-linear isomorphism.

If \(p:M\xrightarrow{\sim}\operatorname{Hom}_A(M,A)\) is a perfect pairing, composition with \(T\) gives a perfect \(R\)-pairing
\[
B_R(m,n)=t(p(m)(n)).
\]
These statements hold for every \(A\)-module \(M\).

*Proof.*

### Step 1. Restrict a functional

If \(\lambda:M\to A\) is \(A\)-linear, then
\[
t(\lambda(\eta(r)m))
=t(\eta(r)\lambda(m))
=r\,t(\lambda(m)).
\]
Thus \(t\circ\lambda\) is \(R\)-linear. Additivity and \(R\)-scalar linearity in \(\lambda\) follow from the same properties of \(t\). This defines the source's restrictDual map \(T\).

### Step 2. Form a functional on the coefficient ring

Fix \(f\in\operatorname{Hom}_R(M,R)\) and \(m\in M\). Define
\[
f_m:A\to R,\qquad f_m(a)=f(am).
\]
This is \(R\)-linear: for \(r\in R\),
\(f_m(\eta(r)a)=f(\eta(r)(am))=r f_m(a)\), and additivity follows from the module laws.

Use \(D^{-1}\) to represent it by
\[
c_f(m)=D^{-1}(f_m)\in A.
\]
The defining equation is
\[
t(c_f(m)a)=f(am)\qquad(a\in A).
\]
This is trace_recover_fiber. It determines \(c_f(m)\) uniquely.

### Step 3. Prove that the recovered map is \(A\)-linear

For addition, \(f_{m+n}=f_m+f_n\), and linearity of \(D^{-1}\) gives
\(c_f(m+n)=c_f(m)+c_f(n)\).

For a scalar \(a\in A\), test the two candidates \(c_f(am)\) and \(a c_f(m)\) against an arbitrary \(b\in A\):
\[
\begin{aligned}
D(c_f(am))(b)&=f(b(am))=f((ba)m),\\
D(a c_f(m))(b)&=t(a c_f(m)b)\\
&=t(c_f(m)(ba))=f((ba)m).
\end{aligned}
\]
Their \(D\)-images agree on every \(b\), so injectivity of \(D\) gives
\(c_f(am)=a c_f(m)\). Thus \(c_f:M\to A\) is \(A\)-linear. It is the source's recoverDual map applied to \(f\).

### Step 4. Verify both inverse identities

Taking \(a=1\) in the representing equation gives
\[
T(c_f)(m)=t(c_f(m))=f(m).
\]
Hence restriction after recovery is the identity.

Conversely, start with \(\lambda\in\operatorname{Hom}_A(M,A)\) and put \(f=t\circ\lambda\). For every \(a\in A\),
\[
f_m(a)=t(\lambda(am))
=t(a\lambda(m))
=D(\lambda(m))(a).
\]
Thus \(f_m=D(\lambda(m))\), so \(c_f(m)=\lambda(m)\). Recovery after restriction is also the identity.

Since \(T\) is \(R\)-linear and has this inverse, it is the asserted \(R\)-linear isomorphism.

### Step 5. Restrict a perfect pairing

The map \(p\), viewed over \(R\), is still an isomorphism. Compose it with \(T\):
\[
M\xrightarrow{p}\operatorname{Hom}_A(M,A)
 \xrightarrow{T}\operatorname{Hom}_R(M,R).
\]
Its value at \(m\), evaluated on \(n\), is \(t(p(m)(n))\). Its inverse sends \(f\) first to \(c_f\), then to \(p^{-1}(c_f)\). This gives the unique representing vector for every \(R\)-functional and proves perfection.

For \(M=A\) with multiplication pairing, this construction recovers \(c_f=D^{-1}(f)\), the trace representative from the reflection example.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.restrictDual`: [Frobenius.lean:112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L112).

`OAI.KLInvariance.FrobeniusDuality.fiber`: [Frobenius.lean:117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L117).

`OAI.KLInvariance.FrobeniusDuality.trace_recover_fiber`: [Frobenius.lean:124](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L124).

`OAI.KLInvariance.FrobeniusDuality.recover_fiber_smul`: [Frobenius.lean:129](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L129).

`OAI.KLInvariance.FrobeniusDuality.recoverDual`: [Frobenius.lean:139](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L139).

`OAI.KLInvariance.FrobeniusDuality.restrict_recover`: [Frobenius.lean:152](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L152).

`OAI.KLInvariance.FrobeniusDuality.recover_restrict`: [Frobenius.lean:158](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L158).

`OAI.KLInvariance.FrobeniusDuality.restrictionEquiv`: [Frobenius.lean:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L168).

`OAI.KLInvariance.FrobeniusDuality.restrictionEquiv_apply`: [Frobenius.lean:175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L175).

`OAI.KLInvariance.FrobeniusDuality.restrictPairing`: [Frobenius.lean:180](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L180).

`OAI.KLInvariance.FrobeniusDuality.restrictPairing_apply`: [Frobenius.lean:183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L183).
