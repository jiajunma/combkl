---
id: kl.detail.root_reflection_correspondence
title: Unique positive roots representing reflections
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
- kl.realization.faithful_actions
- kl.realization.extended_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.Represents.formula
  - OAI.KLInvariance.TitsSpace.Represents.action_formula
  - OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign
  - OAI.KLInvariance.TitsSpace.Represents.reflection_unique
  - OAI.KLInvariance.TitsSpace.exists_positive_root
  - OAI.KLInvariance.TitsSpace.positiveRootEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1723
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1737
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.action_formula
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1743
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1765
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.reflection_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1789
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_positive_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1821
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveRootEquiv
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Unique positive roots representing reflections

In a finite-generator Coxeter system, every reflection has exactly one positive representing root. The resulting correspondence is a bijection between the reflections of \(W\) and its positive real roots.

*Proof.*

### Step 1. Norm and conjugated reflection formula

Suppose \(a=\rho_0(w)\alpha_i\) represents \(t=ws_iw^{-1}\). Invariance of the Tits form gives
\[
B(a,a)=B(\alpha_i,\alpha_i)=2.
\]
Write \(\widetilde a=(a,0)=\rho(w)\widetilde\alpha_i\). For \(z\in E\), conjugate the simple-reflection formula:
\[
\begin{aligned}
\rho(t)z
 &=\rho(w)\left(\rho(w^{-1})z-
   \widetilde B(\widetilde\alpha_i,\rho(w^{-1})z)\widetilde\alpha_i\right)\\
 &=z-\widetilde B(\widetilde a,z)\widetilde a.
\end{aligned}
\]
The coefficient equality uses preservation of the extended form by \(\rho(w)\). Restricting to the embedded ordinary root space gives
\[
\rho_0(t)v=v-B(a,v)a.
\]

Replacing \(w\) by \(ws_i\) replaces \(a\) by \(-a\), while
\[
(ws_i)s_i(ws_i)^{-1}=ws_iw^{-1}=t.
\]
Thus the negative root represents the same reflection.

### Step 2. Uniqueness up to sign

Suppose \(a,b\) represent the same reflection \(t\). Its formula using \(a\), applied to \(a\), gives \(\rho_0(t)a=-a\). Its formula using \(b\) gives \(\rho_0(t)a=a-B(b,a)b\). Equating them yields
\[
B(b,a)b=2a,\qquad a=c b,\quad c=B(b,a)/2.
\]
Taking norms and using \(B(a,a)=B(b,b)=2\) gives \(2=2c^2\). Hence \(c=1\) or \(c=-1\), and \(a=b\) or \(a=-b\).

If both are positive, the alternative \(a=-b\) would make every coordinate of \(a\) both nonnegative and nonpositive. It would be zero, contradicting norm two. Positive representatives are therefore unique.

### Step 3. A root determines its reflection

If the same root \(a\) represents \(t\) and \(r\), Step 1 gives the same formula for \(\rho(t)\) and \(\rho(r)\) on every vector of \(E\). The extended action is faithful, so \(t=r\).

### Step 4. Existence of a positive representative

A reflection is a conjugate of a simple reflection, so its definition supplies a representing root. The root-sign theorem makes that root positive or negative. In the negative case, Step 1 allows its negative as a representing root, and that negative is positive. Thus every reflection has a positive representative.

Every positive real root has an expression \(a=\rho_0(w)\alpha_i\), which supplies the reflection \(ws_iw^{-1}\). Step 3 makes that reflection independent of the expression.

### Step 5. The inverse maps

Starting with a reflection, choose its unique positive root and then the root's reflection. Step 3 returns the original reflection.

Starting with a positive root, take its reflection and then that reflection's positive root. Step 2 returns the original root.

These two constructions are inverse, proving the bijection.

## References

The local statements and proof steps are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.Represents.formula`: [Tits.lean:1723](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1723).

`OAI.KLInvariance.TitsSpace.Represents.action_formula`: [Tits.lean:1737](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1737).

`OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign`: [Tits.lean:1743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1743).

`OAI.KLInvariance.TitsSpace.Represents.reflection_unique`: [Tits.lean:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1765).

`OAI.KLInvariance.TitsSpace.exists_positive_root`: [Tits.lean:1789](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1789).

`OAI.KLInvariance.TitsSpace.positiveRootEquiv`: [Tits.lean:1821](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1821).
