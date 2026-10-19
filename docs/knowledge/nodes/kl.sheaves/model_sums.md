---
id: kl.detail.model_sums
title: Finite constructions from shifted boundary models
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.boundary_models
- kl.sheaves.finite_operations
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:672
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum
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

# Finite constructions from shifted boundary models

Let \(O_c\) be a family of graded sheaves indexed by vertices, and let \(U\) be a set of allowed centers. A model sum centered in \(U\) is a graded sheaf obtained by the following finite construction:

1. Start with the zero sheaf.
2. Given a previously constructed sheaf \(C\), choose a center \(c\in U\), a natural number \(m\), and shifts \(d_1,\ldots,d_m\in\mathbb N\). Form
   \[
   C\oplus\bigoplus_{j=1}^m O_c(d_j).
   \]

A witness of the model-sum predicate records such a finite sequence of steps. The source's two constructors are the zero case and addition of a finite shifted block. The family \(O\) can be arbitrary; the boundary-model assumptions supply the properties used by the decomposition theorem.

Repeated centers are allowed. A block with \(m=0\) is the zero sheaf. Every construction has finitely many summands, even when \(U\) itself is infinite.

## Multiplicity polynomials from the construction

For each center, collect all shifts of blocks added there and define
\[
\mu_c(q)=\sum_{\text{occurrences at }c}q^d.
\]
This is a polynomial with nonnegative integer coefficients. Its degree-\(n\) coefficient counts occurrences of the shift \(n\) at that center. Centers outside \(U\) have zero polynomial, and only finitely many centers occur.

A decomposition theorem produces a graded sheaf isomorphism from a given sheaf to one of these constructed model sums. Its component maps then transport both stalks and outgoing kernels.

## The one-edge example

For the two models \(O_x,O_y\) on \(x\to y\), build
\[
C=O_y\oplus O_x(2).
\]
First add \(O_y(0)\), then add \(O_x(2)\). The multiplicity polynomials are
\[
\mu_y(q)=1,\qquad\mu_x(q)=q^2.
\]

At \(x\), the stalk is \(A\oplus A(2)\), and the lower restriction only reads the first component modulo \(\alpha\). The full outgoing kernel is
\[
K_x(C)=\alpha A\oplus A(2).
\]
The second generator is in degree two and maps to zero on every outgoing edge. It accounts for the model centered at \(x\).

## Minimality away from the allowed centers

For a boundary-model family, every summand \(O_c(d)\) is minimal at any vertex different from \(c\). Finite sums preserve that kernel containment. Thus a model sum centered in \(U\) is minimal at every \(x\notin U\).

This is the induction invariant used when new centers are added in descending order.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

The constructors `zero` and `add` produce the zero sheaf and a product with a finite family of shifted models. The shift function has values in the natural numbers; the lifted finite index type records the \(m\) copies.

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum`: [MinimalExtensions.lean:672](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L672).
