---
id: kl.sheaves.graph_sheaf
title: Module-valued sheaves on an ordered graph
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.ordered_graph
lean:
  repository: openai-kl
  modules:
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:28
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Module-valued sheaves on an ordered graph

Fix an ordered graph \(G\), with source and target maps \(s,t\), and a commutative coefficient ring \(A\). A module-valued graph sheaf \(B\) consists of:

- an \(A\)-module \(B^x\) at every vertex \(x\);
- an \(A\)-module \(B^e\) at every edge \(e\);
- a lower restriction \(\rho^-_e:B^{s(e)}\to B^e\);
- an upper restriction \(\rho^+_e:B^{t(e)}\to B^e\).

Both restriction maps are \(A\)-linear. A vertex module is also called a stalk.

The edge module is a common target for comparing two endpoint values. For a tuple \(m=(m_x)\), compatibility on the edge means
\[
\rho^-_e(m_{s(e)})=\rho^+_e(m_{t(e)}).
\]
A global section is an assignment satisfying this equality on every edge.

## A sheaf of congruences on one edge

Take one edge \(x\to y\), a ring \(A=k[\alpha]\), and modules
\[
B^x=B^y=A,\qquad B^e=A/(\alpha).
\]
Let both restrictions be quotient maps. A section is a pair \((f,g)\) with \(f-g\in\alpha A\).

Every such pair has a unique expression
\[
(f,g)=g(1,1)+h(\alpha,0),\qquad f-g=\alpha h.
\]
Thus, over this polynomial ring, its global section module is free with basis \((1,1),(\alpha,0)\).

The stalk \(A\), edge module \(A/(\alpha)\), and section module of pairs have different roles. The restrictions turn the divisibility equation into the compatibility condition.

## Properties used in later constructions

The upper-quotient property specifies the kernel and surjectivity of \(\rho^+_e\). Global generation specifies the images of the evaluation maps from global sections to individual stalks. Flabbiness specifies extension of compatible values on upper sets. Each property is stated for these same modules and restriction maps.

## References

The local definitions and constructions are listed below.

## Lean formalization

The fields `vertex`, `edge`, `lower`, and `upper` are the modules and restriction maps.

`OAI.KLInvariance.MomentGraph.Sheaf`: [Sheaves.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L28).
