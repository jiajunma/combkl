---
id: kl.local.dihedral_interpolation
title: Polynomial interpolation on external dihedral vertices
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.coxeter.external_vertices
- kl.coxeter.lower_interval_parity
- kl.dihedral.odd_reflection_edges
- kl.local.orbit_splines
- kl.local.orbit_spline_congruence
- kl.local.orbit_spline_factors
- kl.notes.dihedral_models
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.Dihedral.interpolation_exists
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:251
    format: lean-location
    note: OAI.KLInvariance.Dihedral.interpolation_exists
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: 'Read the full interpolation_exists construction: finite parity injection,
    the reflection-inverse identity for x*y^-1, the unique paired vertex, both factor
    cases, quotient-ring product congruence and both parity zero cases. Added a hand-derived
    A2 example as an illustration of the same construction.'
tags:
- Kazhdan-Lusztig
- interpolation
---

# Polynomial interpolation on external dihedral vertices

Let \(H\) be a two-generator Coxeter system, \(W\) a finite-generator Coxeter system, and \(\phi:H\to W\) an injective group homomorphism carrying reflections to reflections. Use the ambient polynomial algebra \(A\), extended action \(\rho\), and coefficient map \(\Lambda:V\to A\).

Fix \(x\le_Hc\). Let \(Y=Y(x,c)\) and \(Z=Z(x,c)\) be the external parity classes: opposite and equal to the length parity of \(x\), respectively. For \(y\in Y\), let \(a_y\) be the interpolation root representing \(\phi(yx^{-1})\), and write \(\lambda(a_y)=\Lambda(i_0a_y)\).

There is a function \(F:H\to A\) such that:

- for every reflection \(t\in H\), every root \(a\) representing \(\phi(t)\), and every \(v\in H\),
  \(\lambda(a)\mid F(v)-F(tv)\);
- \(F(x)=\prod_{y\in Y}\lambda(a_y)\);
- \(F(z)=0\) whenever \(z\le_Hc\) and \(z\not\le_Hx\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Match the same-parity vertices to distinct opposite-parity vertices

The [[node:kl.coxeter.lower_interval_parity|lower-interval parity theorem]] gives \(|Z|\le|Y|\). Choose an injection
\[
j:Z\hookrightarrow Y.
\]
Each \(y\in Y\) therefore has either no assigned vertex or a unique assigned vertex \(z\in Z\).

### Step 2. Choose one normalized orbit factor for each opposite-parity vertex

Fix \(y\in Y\). The element \(t_y=yx^{-1}\) is a reflection. Since it is an involution,
\[
xy^{-1}=(yx^{-1})^{-1}=yx^{-1}.
\]
Applying \(\phi\) gives
\(\phi(x)\phi(y)^{-1}=\phi(t_y)\), the group identity required by the [[node:kl.local.orbit_spline_factors|orbit-spline factor theorem]].

If no \(z\) is assigned to \(y\), use the [[node:kl.local.orbit_spline_factors|single-zero factor]] with reference vertex \(\phi(y)\), normalized to have value \(\lambda(a_y)\) at \(\phi(x)\).

If \(j(z)=y\), then \(z\) and \(y\) have opposite parities, so \(zy^{-1}\) is a reflection. The homomorphism identity \(\phi(z)\phi(y)^{-1}=\phi(zy^{-1})\) supplies the second reflection required by the factor theorem. Also \(z\not\le_Hx\) implies \(z\ne x\), and injectivity gives \(\phi(z)\ne\phi(x)\). The [[node:kl.local.orbit_spline_factors|two-zero factor theorem]] supplies a vector \(v_y\in V\) such that the orbit spline
\[
f_y(w)=F_{\phi(y),v_y}(w)
\]
has values
\[
f_y(\phi(x))=\lambda(a_y),\qquad
f_y(\phi(y))=0,\qquad
f_y(\phi(z))=0.
\]
Its two representing roots are the chosen positive roots of \(\phi(yx^{-1})\) and \(\phi(zy^{-1})\). Uniqueness of the assigned \(z\) makes this factor satisfy every requirement attached to \(y\).

In either case denote the chosen vector by \(v_y\) and its orbit factor by \(f_y=F_{\phi(y),v_y}\). Every factor has the prescribed value at \(\phi(x)\) and the reference zero at \(\phi(y)\); the matched factors also have the assigned zero.

### Step 3. Multiply the factors and preserve each reflection congruence

Define
\[
F(v)=\prod_{y\in Y}f_y(\phi(v)).
\]
For a reflection \(t\in H\) and a root \(a\) representing \(\phi(t)\), the [[node:kl.local.orbit_spline_congruence|orbit-spline congruence theorem]] gives
\[
f_y(\phi(v))\equiv f_y(\phi(t)\phi(v))
=f_y(\phi(tv))\pmod{\lambda(a)}
\]
for every factor.

Reduction modulo \(\lambda(a)\) is a ring homomorphism, so multiplying these equalities gives
\(F(v)\equiv F(tv)\pmod{\lambda(a)}\). This is the first assertion.

### Step 4. Evaluate at the distinguished vertex

Every chosen factor has value \(\lambda(a_y)\) at \(\phi(x)\). Hence
\[
F(x)=\prod_{y\in Y}\lambda(a_y).
\]
For \(x=c\), the external set is empty and this construction gives the empty product \(F=1\).

### Step 5. Check every external zero

If \(z\le_Hc\) but \(z\not\le_Hx\), it belongs to the external set.

If \(z\in Y\), the factor \(f_z\) vanishes at its reference vertex \(\phi(z)\), so the product is zero.

If \(z\in Z\), the factor \(f_{j(z)}\) was chosen to vanish at \(\phi(z)\). Again one factor of the product is zero. These cases exhaust the external vertices.

### Step 6. Work through the interval from 1 to st in type A2

As an illustration, take \(H=W\) of type \(A_2\), \(\phi=\operatorname{id}\), \(x=s\) and \(c=st\). Identify the simple roots \(a,b\) with their embedded vectors in the extended realization, with
\[
\widetilde B(a,a)=\widetilde B(b,b)=2,\qquad
\widetilde B(a,b)=-1,
\]
and write \(\alpha=\Lambda(a)\), \(\beta=\Lambda(b)\). Here \(Y=\{st\}\), \(Z=\{t\}\), so \(t\) is matched to \(st\).

The reflection \(sts\) is represented by \(a+b\), since \(s(b)=a+b\). One choice for the factor vector is
\[
v_0=-\tfrac13a-\tfrac23b.
\]
Its normal values are
\(\widetilde B(a,v_0)=0\) and
\(\widetilde B(a+b,v_0)=-1\).
Use the orbit spline with reference vertex \(st\). Its values on the interval are

| Vertex | Spline value |
|---|---|
| \(1\) | \(\beta\) |
| \(s\) | \(\alpha+\beta\) |
| \(t\) | \(0\) |
| \(st\) | \(0\) |

At \(1\), the action of \((st)^{-1}=ts\) first fixes \(v_0\) under \(s\) and then adds \(b\) under \(t\), giving \(\beta\). The other three values follow from the prescribed normals and the reference zero.

The four reflection edges give the following compatibility checks. Each difference is the lower value minus the upper value.

| Edge | Difference | Label dividing the difference |
|---|---|---|
| \(1\to s\) | \(-\alpha\) | \(\alpha\) |
| \(1\to t\) | \(\beta\) | \(\beta\) |
| \(s\to st\) | \(\alpha+\beta\) | \(\alpha+\beta\) |
| \(t\to st\) | \(0\) | \(\alpha\) |

The value at \(s\) is exactly its supported outgoing label product.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.interpolation_exists`: [DihedralIntervals.lean:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251).
