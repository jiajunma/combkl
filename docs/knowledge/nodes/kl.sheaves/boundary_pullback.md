---
id: kl.sheaves.boundary_pullback
title: Boundary-sheaf pullback with complete outgoing edge lifts
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graph_transport
- kl.sheaves.boundary_sheaf
- kl.sheaves.flabbiness
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_edgeFlabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_kernelMinimal
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.pullback
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1660
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_edgeFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1690
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_kernelMinimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1716
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.pullback
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
- moment_graph_sheaves
---

# Boundary-sheaf pullback with complete outgoing edge lifts

Let \(B\) be a normalized boundary sheaf on an ordered graph \(H\), with distinguished vertex \(b\) and labels \(\alpha\). Let \(f:G\to H\) be a graph map satisfying:

- the vertex map \(f_V\) is injective;
- for every vertex \(x\) of \(G\) and every edge \(e\) of \(H\) with \(s_H(e)=f_V(x)\), there is an edge \(a\) of \(G\) with
  \[
  s_G(a)=x,\qquad f_E(a)=e.
  \]

Choose \(c\in V_G\) with \(f_V(c)=b\). Then \(f^*B\) is a normalized boundary sheaf at \(c\), with labels \(\alpha\circ f_E\).

*Proof.*

### Step 1. Inherit the stalk and quotient data

The pullback stalk at \(x\) is \(B^{f_V(x)}\), so it is free. Its edge modules and upper restrictions are copied from the target graph, with label \(\alpha(f_E(a))\). They therefore satisfy the same upper-quotient rule.

At \(c\), the stalk is \(B^b\), retaining the normalized graded unit module.

### Step 2. Transfer global generation

For a vector in the pullback stalk at \(x\), choose a target global section taking that value at \(f_V(x)\). Its pulled-back assignment is global and has the required value at \(x\).

### Step 3. Transfer edge flabbiness

Let \(U\subseteq V_G\) be closed under source edges and let a compatible assignment on \(U\) be given. The injective vertex map lets us view its values as an assignment on \(f_V(U)\), filling other target vertices by zero.

If a target edge begins at \(f_V(x)\), \(x\in U\), choose an outgoing lift \(a\) from \(x\). Edge closure gives \(t_G(a)\in U\), and the endpoint equation gives
\(t_H(f_E(a))=f_V(t_G(a))\).
Thus \(f_V(U)\) is edge-closed.

The source compatibility equation on a lifted edge is exactly the target equation on its image. Injectivity ensures the pushed endpoint values are the prescribed ones. Hence the assignment is compatible on \(f_V(U)\).

Target edge flabbiness gives a global extension. Pulling it back gives a global source section agreeing on \(U\).

### Step 4. Retain every outgoing kernel condition

At \(x\), the pullback and target stalk are the same underlying module. Each source outgoing restriction is a target outgoing restriction by the endpoint equations.

Conversely, every target outgoing edge at \(f_V(x)\) has a lift from \(x\). Therefore a vector is killed by all source outgoing restrictions exactly when it is killed by all target outgoing restrictions:
\[
K_x(f^*B)=K_{f_V(x)}(B).
\]

### Step 5. Preserve kernel minimality

If \(x\ne c\), injectivity and \(f_V(c)=b\) give \(f_V(x)\ne b\). Target minimality therefore gives
\[
K_{f_V(x)}(B)\subseteq J B^{f_V(x)}.
\]
Step 4 identifies this with the required containment for the pullback stalk. Together with Steps 1–3, all boundary-sheaf fields are supplied.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_edgeFlabby`: [MinimalExtensions.lean:1660](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1660).

`OAI.KLInvariance.MomentGraph.GradedSheaf.pullback_kernelMinimal`: [MinimalExtensions.lean:1690](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1690).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.pullback`: [MinimalExtensions.lean:1716](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1716).
