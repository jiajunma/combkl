---
id: kl.sheaves.adjoint_summand_duality
title: The adjoint image is dual to a split summand
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.integral_adjoints
- kl.sheaves.adjoint_properties
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.AdjointSummandDuality.dualSection
  - OAI.AdjointSummandDuality.dualProjection
  - OAI.AdjointSummandDuality.projection_section
  - OAI.AdjointSummandDuality.adjointSummand
  - OAI.AdjointSummandDuality.adjointEquivDual
  - OAI.PerfectAdjoint.adjoint_projector_eq
  - OAI.PerfectAdjoint.rangeAdjointEquivDual
  - OAI.PerfectAdjoint.rangeAdjointEquivDualRange
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1025
    format: lean-location
    note: OAI.AdjointSummandDuality.dualSection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1028
    format: lean-location
    note: OAI.AdjointSummandDuality.dualProjection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1031
    format: lean-location
    note: OAI.AdjointSummandDuality.projection_section
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1049
    format: lean-location
    note: OAI.AdjointSummandDuality.adjointSummand
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1067
    format: lean-location
    note: OAI.AdjointSummandDuality.adjointEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1136
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_projector_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1142
    format: lean-location
    note: OAI.PerfectAdjoint.rangeAdjointEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1173
    format: lean-location
    note: OAI.PerfectAdjoint.rangeAdjointEquivDualRange
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

# The adjoint image is dual to a split summand

Let \(M,N\) be modules over a commutative ring \(R\). Suppose
\[
D:M\xrightarrow{\sim}M^*,\qquad
i:N\to M,\quad p:M\to N,\quad pi=1_N.
\]
Put \(e=ip\), an idempotent endomorphism of \(M\), and let \(e^*\) be its adjoint for \(D\).

Then
\[
\operatorname{im}e^*\xrightarrow{\sim}N^*,
\qquad
m\longmapsto\bigl(n\mapsto\langle m,i(n)\rangle\bigr)
\]
is an \(R\)-linear isomorphism. Its inverse sends \(\lambda\in N^*\) to \(D^{-1}(\lambda\circ p)\).

*Proof.*

### Step 1. Construct two maps between the dual and the ambient module

Define
\[
j:N^*\to M,\qquad j(\lambda)=D^{-1}(\lambda\circ p),
\]
\[
q:M\to N^*,\qquad q(m)(n)=\langle m,i(n)\rangle.
\]
These maps are linear by linearity of \(D^{-1}\), precomposition, and the pairing.

For \(\lambda\in N^*\) and \(n\in N\),
\[
q(j(\lambda))(n)
=D(D^{-1}(\lambda\circ p))(i(n))
=\lambda(p(i(n)))=\lambda(n).
\]
Thus \(qj=1_{N^*}\).

### Step 2. Identify the adjoint projector

For \(m,z\in M\),
\[
\begin{aligned}
\langle jq(m),z\rangle
&=q(m)(p(z))\\
&=\langle m,i(p(z))\rangle\\
&=\langle m,e(z)\rangle.
\end{aligned}
\]
This is the defining equation of \(e^*\). Perfection gives \(e^*=jq\).
In particular,
\[
(e^*)^2=jqjq=j(qj)q=jq=e^*.
\]

### Step 3. Identify its image

Every \(e^*m=jq(m)\) lies in \(\operatorname{im}j\). Conversely,
\[
e^*(j(\lambda))=jqj(\lambda)=j(\lambda),
\]
so every element of \(\operatorname{im}j\) lies in \(\operatorname{im}e^*\). Hence
\(\operatorname{im}e^*=\operatorname{im}j\).

The map \(q\) restricts to this image. The identity \(qj=1\) proves it is surjective. If \(m=j(\lambda)\) and \(q(m)=0\), then \(\lambda=qj(\lambda)=0\), so \(m=0\). This proves injectivity and the asserted inverse.

### Step 4. Specialize to a projector's own image

For an idempotent \(f:M\to M\), take \(N=\operatorname{im}f\), let \(i\) be inclusion, and let \(p\) send \(m\) to \(f(m)\) viewed in its image. If \(n=f(z)\), then \(f(n)=f^2(z)=f(z)=n\), so \(pi=1_N\).

The result becomes
\[
\operatorname{im}f^*\simeq(\operatorname{im}f)^*,
\]
with pairing given by the ambient form on the two image modules.

### Step 5. Evaluate the coordinate-line example

For \(M=R^2\) with \(\langle(a,b),(c,d)\rangle=ad+bc\), take \(N=R\),
\(i(c)=(c,0)\), and \(p(a,b)=a\). Then \(e^*(a,b)=(0,b)\), and the isomorphism sends
\[
(0,b)\longmapsto(c\mapsto bc).
\]
The functional \(c\mapsto bc\) pulls back to \((0,b)\). Thus the dual summand is realized by the other coordinate line.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.AdjointSummandDuality.dualSection`: [BalancedPairings.lean:1025](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1025).

`OAI.AdjointSummandDuality.dualProjection`: [BalancedPairings.lean:1028](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1028).

`OAI.AdjointSummandDuality.projection_section`: [BalancedPairings.lean:1031](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1031).

`OAI.AdjointSummandDuality.adjointSummand`: [BalancedPairings.lean:1049](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1049).

`OAI.AdjointSummandDuality.adjointEquivDual`: [BalancedPairings.lean:1067](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1067).

`OAI.PerfectAdjoint.adjoint_projector_eq`: [BalancedPairings.lean:1136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1136).

`OAI.PerfectAdjoint.rangeAdjointEquivDual`: [BalancedPairings.lean:1142](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1142).

`OAI.PerfectAdjoint.rangeAdjointEquivDualRange`: [BalancedPairings.lean:1173](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1173).
