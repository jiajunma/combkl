---
id: kl.sheaves.pullback_live_flabbiness
title: Sheaf properties under pullback along surviving edges
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graph_transport
- kl.sheaves.relative_flabbiness
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.pullAssignment
  - OAI.KLInvariance.MomentGraph.Sheaf.pull_global
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback_generated
  - OAI.KLInvariance.MomentGraph.Sheaf.pushAssignment
  - OAI.KLInvariance.MomentGraph.Sheaf.pull_push
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback_flabby_live
  - OAI.KLInvariance.MomentGraph.Sheaf.pullback_quotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1479
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullAssignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1491
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pull_global
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1497
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullback_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1502
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pushAssignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1507
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pull_push
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1520
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullback_flabby_live
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1554
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pullback_quotient
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read pull/push assignments, both basic property transfers and the complete
    live-edge flabbiness proof. Preserved finite target vertices, vertex injectivity,
    zero modules outside the selected live set and outgoing lifts; generation and
    quotient transport use no such extra hypotheses.
tags:
- Kazhdan-Lusztig
- localization
---

# Sheaf properties under pullback along surviving edges

Let \(R\) be a commutative ring, let \(f:G\to H\) be a graph map with vertex map \(f_V\) and edge map \(f_E\), and let \(B\) be an \(R\)-linear sheaf on \(H\).

Global generation of \(B\) implies global generation of \(f^*B\). The upper-quotient rule with labels \(\alpha_e\) pulls back to the rule with labels \(\alpha_{f_E(a)}\).

For flabbiness, suppose the target graph \(H\) has finitely many vertices, \(f_V\) is injective, and \(B\) is flabby. Choose a set \(L\subseteq E_H\) such that
\[
B^e=0\qquad(e\notin L).
\]
Assume every surviving outgoing edge lifts:
\[
e\in L,\quad f_V(x)=s_H(e)
\quad\Longrightarrow\quad
\exists a\in E_G,\quad s_G(a)=x,\quad f_E(a)=e.
\]
Then \(f^*B\) is flabby for the order on \(G\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Pull back global sections and generating values

For a global section \(h\) of \(B\), define \(f^*h\) by
\[
(f^*h)_x=h_{f_V(x)}.
\]
On an edge \(a\), its compatibility equation is the old equation on \(f_E(a)\), after using the two endpoint identities of the graph map. Thus \(f^*h\) is global.

For the generation assertion, assume \(B\) is globally generated. Given a value in \((f^*B)^x=B^{f_V(x)}\), this supplies a section with that value at \(f_V(x)\). Pulling it back gives the required value at \(x\).

### Step 2. Pull back an upper quotient

For the quotient assertion, assume \(B\) has the upper-quotient rule. At an edge \(a:x\to y\), the pulled-back upper map is the original upper map at \(f_E(a)\), with the source module identified by
\(f_V(y)=t_H(f_E(a))\).
This identification is a linear isomorphism.

Surjectivity is preserved by composing with that isomorphism. Its inverse transports the original kernel
\(\alpha_{f_E(a)}B^{t_H(f_E(a))}\)
to
\(\alpha_{f_E(a)}(f^*B)^y\).
This proves the quotient rule. Steps 1 and 2 use only the graph-map identities.

### Step 3. Push an assignment to the vertex image

Assume now the flabbiness hypotheses. Let \(\Omega\subseteq V_G\) be upper and let \(g\) be compatible on \(\Omega\). Define an ambient assignment \(\widehat g\) on \(H\) by
\[
\widehat g_{f_V(x)}=g_x,\qquad
\widehat g_y=0\quad(y\notin f_V(V_G)).
\]
Injectivity of \(f_V\) makes the value on its image well defined, using the pullback stalk identification. Pulling \(\widehat g\) back recovers \(g\).

### Step 4. Show that the image subset is closed under surviving edges

Put \(\Omega'=f_V(\Omega)\). If \(e\in L\) starts at \(f_V(x)\) for \(x\in\Omega\), choose its lift \(a\) starting at \(x\).

Since \(G\) is ordered, \(x<t_G(a)\). Upper closure gives \(t_G(a)\in\Omega\). The target identity
\(f_V(t_G(a))=t_H(e)\)
then puts \(t_H(e)\) in \(\Omega'\). Hence \(\Omega'\) is closed under every edge in \(L\).

### Step 5. Verify the pushed assignment's compatibility

Consider an edge \(e\) with both endpoints in \(\Omega'\).

If \(e\notin L\), its module is zero, and both restriction values vanish.

If \(e\in L\), lift it from a source preimage \(x\in\Omega\) to an edge \(a\). If the target endpoint is \(f_V(y)\), injectivity of \(f_V\) and the target identity give \(t_G(a)=y\). Thus both endpoints of \(a\) lie in \(\Omega\). Compatibility of \(g\) on \(a\), together with the pullback restriction formulas, gives compatibility of \(\widehat g\) on \(e\).

### Step 6. Extend on the target and pull back

The [[node:kl.sheaves.relative_flabbiness|extension theorem for subsets closed under surviving edges]] applies to \(B,\Omega',\widehat g\): the target vertex set is finite, \(B\) is flabby, the outside edge modules are zero, and Steps 4–5 give closure and compatibility.

It supplies a global section \(h\) with \(h_y=\widehat g_y\) on \(\Omega'\). Step 1 makes \(f^*h\) global. For \(x\in\Omega\),
\[
(f^*h)_x=h_{f_V(x)}=\widehat g_{f_V(x)}=g_x.
\]
This proves flabbiness of the pullback.

For a simple illustration, take a two-vertex target \(x<y\) whose only edge module is zero, and pull back to the single vertex \(x\). With \(L=\varnothing\), a prescribed value at \(x\) extends by choosing zero at \(y\); the pullback section is exactly the prescribed value.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.pullAssignment`: [MinimalExtensions.lean:1479](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1479).

`OAI.KLInvariance.MomentGraph.Sheaf.pull_global`: [MinimalExtensions.lean:1491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1491).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback_generated`: [MinimalExtensions.lean:1497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1497).

`OAI.KLInvariance.MomentGraph.Sheaf.pushAssignment`: [MinimalExtensions.lean:1502](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1502).

`OAI.KLInvariance.MomentGraph.Sheaf.pull_push`: [MinimalExtensions.lean:1507](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1507).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback_flabby_live`: [MinimalExtensions.lean:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520).

`OAI.KLInvariance.MomentGraph.Sheaf.pullback_quotient`: [MinimalExtensions.lean:1554](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1554).
