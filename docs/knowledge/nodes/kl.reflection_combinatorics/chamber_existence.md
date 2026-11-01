---
id: kl.order.chamber_existence
title: A generic ratio order in every prescribed chamber
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.reflection_order
- kl.order.polynomial_functionals
- kl.order.root_slopes
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber_height
  - OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1266
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber_height
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1322
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the chamber, positivity, simple-label exclusions, two orders and exact
    induction hypotheses retained?
  verdict: Read the exact f0+tau*momentFunctional(tau) construction. Checked the finite
    open positivity set containing zero, normalized-root injectivity, nonzero difference
    polynomials, countability/finite-zero avoidance and all four RatioOrder fields.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# A generic ratio order in every prescribed chamber

Fix a finite-generator Coxeter system \(W\), its original real root space \(V_0=\mathbb R^I\), simple roots \(\alpha_i\), and root action \(\rho\). For every \(y\in W\), there is a ratio order \(O=(h,f)\) whose denominator is the height functional
\[
h(v)=\sum_{i\in I}v_i
\]
and whose numerator satisfies
\[
f(\rho(y)\alpha_i)>0\quad(i\in I).
\]
Its slopes are distinct on all positive roots, so this is an order in the prescribed chamber, including when the root system is infinite.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**An actual chamber numerator and the inversion-sign order.**

**OpenAI notes:** The notes cite the reflection-order path formula and construct separating ratios of linear functionals for the geometric orders used in comparison. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [sec:background](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

**Lean (primary):** The path proof chooses a numerator positive on the transformed simple roots of a prescribed chamber. It implies the inversion-sign condition and supplies a least simple descent. Existence uses height composed with the inverse action, a polynomial perturbation preserving finitely many strict inequalities, and avoidance of countably many root-tie polynomials. [DyerPaths:1240](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1240), [DyerPaths:1198](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1198), [DyerPaths:1242](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1242), [DyerPaths:1220](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1220), [DyerPaths:1266](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1266), [ReflectionSchedules:18](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L18), [ReflectionSchedules:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L39).

**Role in the proof:** The Blueprint distinguishes the Chamber and Adapted predicates and explains the coordinate-polynomial family used to satisfy genericity and chamber positivity together.
<!-- source-comparison:end -->

*Proof.*

### Step 1. A functional in the desired chamber

Start with
\[
f_0=h\circ\rho(y^{-1}).
\]
For each simple root, the action law gives
\[
f_0(\rho(y)\alpha_i)
=h(\rho(y^{-1})\rho(y)\alpha_i)
=h(\alpha_i)=1>0.
\]
Thus \(f_0\) already satisfies all chamber inequalities.

### Step 2. The polynomial perturbation and its positivity set

Use the [[node:kl.order.polynomial_functionals|coordinate-polynomial construction]] to define
\[
f_\tau=f_0+\tau m_\tau.
\]
For each fixed vector \(v\), \(f_\tau(v)=f_0(v)+\tau P_v(\tau)\) is a continuous function of the real parameter \(\tau\).
Therefore
\[
U=\{\tau:f_\tau(\rho(y)\alpha_i)>0\text{ for every }i\}
\]
is open: it is a finite intersection of strict positivity sets of continuous functions. Step 1 gives \(0\in U\). Consequently \(U\) contains a nonempty open interval.

### Step 3. A nonzero polynomial for each possible root tie

Normalize a positive root by \(\widehat a=a/h(a)\). Height is positive on positive roots, and normalized-root injectivity gives \(\widehat a\ne\widehat b\) for \(a\ne b\).
For such a pair put
\[
v_{a,b}=\widehat a-\widehat b,\qquad
d_{a,b}(X)=f_0(v_{a,b})+X P_{v_{a,b}}(X).
\]
The vector \(v_{a,b}\) is nonzero.
If \(d_{a,b}=0\), evaluation at zero gives \(f_0(v_{a,b})=0\). The remaining identity is \(XP_{v_{a,b}}=0\). Since \(\mathbb R[X]\) has no zero divisors and \(X\ne0\), \(P_{v_{a,b}}=0\). Coefficient recovery gives \(v_{a,b}=0\), a contradiction. Thus \(d_{a,b}\) is nonzero.

### Step 4. Avoiding all ties while retaining positivity

The group is countable because finite words in its finite simple alphabet map onto it. Its roots, and hence its pairs of positive roots, are countable.
Each nonzero polynomial \(d_{a,b}\) has finitely many real roots. Their union
\[
B=\bigcup_{a\ne b}\{\tau:d_{a,b}(\tau)=0\}
\]
is therefore countable.

The nonempty open interval inside \(U\) is uncountable. Choose \(\tau\in U\setminus B\).
Membership in \(U\) preserves every chamber inequality. Avoidance of \(B\) ensures that every \(d_{a,b}(\tau)\) is nonzero.

### Step 5. Injectivity of the resulting slope

Set \(f=f_\tau\). If two positive roots \(a,b\) had equal slopes, then
\[
f(\widehat a)=f(\widehat b),
\]
since \(f(\widehat a)=f(a)/h(a)\). Hence \(f(v_{a,b})=0\).
The perturbation formula gives
\[
f(v_{a,b})=f_0(v_{a,b})+\tau P_{v_{a,b}}(\tau)
=d_{a,b}(\tau).
\]
For \(a\ne b\), this contradicts \(\tau\notin B\). The slope is therefore injective.

### Step 6. The resulting ratio order

The denominator \(h\) is positive on all simple roots, Step 5 supplies the genericity field, and \(\tau\in U\) supplies the chamber condition. These data define the required ratio order.
The [[node:kl.order.chamber_adaptation|chamber and least-descent theorem]] then identifies its negative slopes with the inversion set of \(y\), preparing the simple-root rotation used in the path recursion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber_height`: [DyerPaths.lean:1266](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1266).

`OAI.KLInvariance.TitsSpace.exists_ratioOrder_chamber`: [DyerPaths.lean:1322](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1322).
