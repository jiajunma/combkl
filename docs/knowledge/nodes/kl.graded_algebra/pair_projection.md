---
id: kl.algebra.pair_projection
title: The quotient comparing two module projections
kind: definition
status: formalized
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.homogeneous_subquotients
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.PairProjection.relation
  - OAI.KLInvariance.PairProjection.Edge
  - OAI.KLInvariance.PairProjection.lower
  - OAI.KLInvariance.PairProjection.upper
  - OAI.KLInvariance.PairProjection.compatible_iff
  - OAI.KLInvariance.PairProjection.kernel_lower
  - OAI.KLInvariance.PairProjection.lower_surjective
  - OAI.KLInvariance.PairProjection.upper_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:153
    format: lean-location
    note: OAI.KLInvariance.PairProjection.relation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:154
    format: lean-location
    note: OAI.KLInvariance.PairProjection.Edge
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:156
    format: lean-location
    note: OAI.KLInvariance.PairProjection.lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:157
    format: lean-location
    note: OAI.KLInvariance.PairProjection.upper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:168
    format: lean-location
    note: OAI.KLInvariance.PairProjection.compatible_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:181
    format: lean-location
    note: OAI.KLInvariance.PairProjection.kernel_lower
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:191
    format: lean-location
    note: OAI.KLInvariance.PairProjection.lower_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:201
    format: lean-location
    note: OAI.KLInvariance.PairProjection.upper_surjective
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# The quotient comparing two module projections

Let \(R\) be a commutative ring, and let \(f:M\to X\), \(g:M\to Y\) be \(R\)-linear maps. Their pair relation is the image submodule
\[
L=\{(f(m),g(m)):m\in M\}\subseteq X\oplus Y.
\]
The pair-projection quotient is
\[
Q=(X\oplus Y)/L.
\]
It compares the two projections through the linear maps
\[
\ell:X\to Q,\quad x\mapsto[(x,0)],\qquad
u:Y\to Q,\quad y\mapsto-[(0,y)].
\]

## Compatibility and simultaneous lifting

The equality \(\ell(x)=u(y)\) is equivalent to
\[
[(x,0)]+[(0,y)]=[(x,y)]=0.
\]
A class is zero exactly when its representative belongs to \(L\). Therefore
\[
\ell(x)=u(y)
\quad\Longleftrightarrow\quad
\exists m\in M,\ f(m)=x,\ g(m)=y.
\]
In particular, \(\ell(f(m))=u(g(m))\) for every \(m\).

Taking \(y=0\) gives the lower kernel:
\[
\ker\ell=\{f(m):g(m)=0\}.
\]
Thus a lower value maps to zero exactly when it can be lifted with zero upper projection.

## Surjective endpoint maps

If \(g\) is surjective, every quotient class is in the image of \(\ell\). Indeed, write it as \([(x,y)]\), choose \(m\) with \(g(m)=y\), and subtract the relation vector:
\[
[(x,y)]=[(x-f(m),0)]=\ell(x-f(m)).
\]

If \(f\) is surjective, choose \(m\) with \(f(m)=x\). Then
\[
[(x,y)]=[(0,y-g(m))]=u(g(m)-y),
\]
so \(u\) is surjective as well.

## The one-edge congruence quotient

Take \(M=\{(f,g)\in A^2:f-g\in\alpha A\}\), with \(X=Y=A\) and coordinate projections. The map
\[
X\oplus Y\longrightarrow A/(\alpha),\qquad
(x,y)\longmapsto x-y\bmod\alpha
\]
is surjective and has kernel exactly \(M\). It identifies \(Q\) with \(A/(\alpha)\).

Under this identification,
\(\ell(x)=x\bmod\alpha\), and
\(u(y)=-(-y\bmod\alpha)=y\bmod\alpha\).
Thus both sheaf restrictions are the usual quotient map; the minus sign in \(u\) produces their equality on compatible endpoint values.

## Graded projections

If \(f,g\) preserve degree, the map \(M\to X\oplus Y\) does too. Its image is a homogeneous submodule, so \(Q\) carries the quotient grading and \(\ell,u\) preserve degree. The word sheaf applies this construction to the two stalk projections at each edge.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.PairProjection.relation`: [Decomposition.lean:153](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L153).

`OAI.KLInvariance.PairProjection.Edge`: [Decomposition.lean:154](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L154).

`OAI.KLInvariance.PairProjection.lower`: [Decomposition.lean:156](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L156).

`OAI.KLInvariance.PairProjection.upper`: [Decomposition.lean:157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L157).

`OAI.KLInvariance.PairProjection.compatible_iff`: [Decomposition.lean:168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L168).

`OAI.KLInvariance.PairProjection.kernel_lower`: [Decomposition.lean:181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L181).

`OAI.KLInvariance.PairProjection.lower_surjective`: [Decomposition.lean:191](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L191).

`OAI.KLInvariance.PairProjection.upper_surjective`: [Decomposition.lean:201](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L201).
