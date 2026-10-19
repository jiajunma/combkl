---
id: kl.sheaves.pullback_selected_kernels
title: Selected kernels under outgoing-complete graph pullback
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graph_transport
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.stalkMap_assignment
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback_kernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1590
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.stalkMap_assignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1596
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullback_kernel
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read both containments of pullback_kernel and its stalkMap_assignment transport.
    Retained outgoing lifting only at the fixed vertex, arbitrary selected ambient
    edges and zero outside modules; no vertex injectivity, finiteness or flabbiness
    hypothesis is used.
tags:
- Kazhdan-Lusztig
- localization
---

# Selected kernels under outgoing-complete graph pullback

Let \(R\) be a commutative ring, \(f:G\to H\) a graph map, and \(B\) an \(R\)-linear sheaf on \(H\). Fix a vertex \(x\in V_G\) and an arbitrary set \(T\subseteq E_H\).

Choose \(L\subseteq E_H\) with \(B^e=0\) for every \(e\notin L\). Suppose each edge of \(L\) starting at \(f_V(x)\) has a lift starting at \(x\):
\[
e\in L,\quad s_H(e)=f_V(x)
\Longrightarrow
\exists a,\quad s_G(a)=x,\quad f_E(a)=e.
\]

For a set of ambient edges, let \(K_y^B(T)\) impose vanishing only on those members of \(T\) starting at \(y\). Then, in the common stalk
\((f^*B)^x=B^{f_V(x)}\),
\[
K_x^{f^*B}(f_E^{-1}(T))=K_{f_V(x)}^B(T).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Write both selected systems

A vector \(v\in B^{f_V(x)}\) belongs to the left kernel exactly when
\[
\rho^{f^*B,-}_a(v)=0
\]
for every edge \(a\) starting at \(x\) with \(f_E(a)\in T\).

The pullback formula identifies this restriction with
\(\rho^{B,-}_{f_E(a)}(v)\), through
\(s_H(f_E(a))=f_V(x)\).
The right kernel requires this same vanishing for every target-graph edge in \(T\) starting at \(f_V(x)\).

### Step 2. Pull ambient conditions back

Suppose \(v\) lies in the right kernel. For any selected outgoing edge \(a\) at \(x\), the endpoint identity makes \(f_E(a)\) an outgoing edge at \(f_V(x)\), and it belongs to \(T\) by selection. Its restriction vanishes, so the pullback restriction vanishes. Thus \(v\) belongs to the left kernel.

### Step 3. Recover every surviving ambient condition

Conversely, suppose \(v\) lies in the left kernel. Let \(e\in T\) start at \(f_V(x)\).

If \(e\in L\), take an outgoing lift \(a\) with \(f_E(a)=e\). It is selected in the pullback, so
\[
0=\rho^{f^*B,-}_a(v)=\rho^{B,-}_e(v).
\]

If \(e\notin L\), its edge module is zero and the restriction vanishes. Every required ambient condition is therefore satisfied.

### Step 4. Identify the underlying stalk vector

Both containments used the same vector \(v\) in \(B^{f_V(x)}\), proving equality as submodules.

The source expresses the endpoint identifications by the assignment supported at \(f_V(x)\) with value \(v\). Its pullback has value \(v\) at \(x\), and stalkMap_assignment rewrites each component restriction. The resulting equations are exactly those checked above.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.stalkMap_assignment`: [MinimalExtensions.lean:1590](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1590).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback_kernel`: [MinimalExtensions.lean:1596](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1596).
