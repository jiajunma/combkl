---
id: kl.local.structure_sheaf_properties
title: Basic properties and local minimality of structure sheaves
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.structure_sheaves
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_free
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_finite
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_support
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_generated
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_upperQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:898
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:901
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:904
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:917
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:925
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:944
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_minimal
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all basic structureSheaf property lemmas and the local minimality
    proof. Preserved arbitrary commutative rings for the basic properties, and the
    separate local-ring, maximal-ideal-label and outgoing-edge hypotheses for minimality.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Basic properties and local minimality of structure sheaves

Let \(R\) be a commutative ring, \(G\) an ordered graph with labels \(\alpha_e\), and \(\mathcal O_c\) its structure sheaf supported on \(\{x:x\le c\}\).

Every stalk is finite free, the sheaf is globally generated, and its upper restrictions are surjective with kernels
\[
\ker\rho^+_e=\alpha_e\mathcal O_c^{t(e)}.
\]

For the local-minimality assertion, assume \(R\) is a local ring with maximal ideal \(\mathfrak m\), every \(\alpha_e\in\mathfrak m\), and
\[
x<c\Longrightarrow
\exists e,\quad s(e)=x,\quad t(e)\le c.
\]
Then at every \(x\ne c\),
\[
K_x(\mathcal O_c)\subseteq\mathfrak m\,\mathcal O_c^x,
\]
where \(K_x\) is the full outgoing kernel.

*Proof.*

### Step 1. Identify the stalks and their bases

For \(x\le c\), evaluation at the unique support coordinate gives \(\mathcal O_c^x\simeq R\), with basis \((1)\).

For \(x\not\le c\), the support index is empty, so the stalk is zero and has the empty basis. Both cases give a finite free module.

### Step 2. Generate any stalk value by a global section

For \(x\le c\) and a desired scalar \(r\), assign \(r\) to every supported vertex and zero to every other stalk. On a supported edge, both restrictions are \([r]\); on an unsupported edge, both have zero target. This is a global section taking value \(r\) at \(x\).

For an unsupported stalk, its only value is zero, supplied by the zero section. Thus the sheaf is globally generated.

### Step 3. Check the upper-quotient rule

If \(t(e)\le c\), the upper map is \(R\to R/(\alpha_e)\), which is surjective and has kernel \(\alpha_eR\).

If \(t(e)\not\le c\), both the upper stalk and edge module are zero. The map is surjective and its kernel is \(0=\alpha_e\cdot0\).

These cases give the stated rule on every edge.

### Step 4. Use an outgoing edge at a proper supported vertex

Assume the local-ring hypotheses and take \(x\ne c\). If \(x\not\le c\), the stalk is zero and the claimed containment holds.

If \(x\le c\), then \(x<c\). Choose an edge \(e:x\to y\) with \(y\le c\) as in the hypothesis. For \(v\in K_x(\mathcal O_c)\), the corresponding quotient restriction vanishes, so its scalar coordinate satisfies
\[
v_x\in(\alpha_e)\subseteq\mathfrak m.
\]
The final inclusion uses \(\alpha_e\in\mathfrak m\).

### Step 5. Return to the stalk submodule

In the supported stalk, \(v=v_x\cdot1_x\), where \(1_x\) is its standard generator. Since \(v_x\in\mathfrak m\), this lies in
\(\mathfrak m\,\mathcal O_c^x\). This proves the local-minimality containment.

The finite relative coset graph supplies the outgoing-edge hypothesis through its outgoing-step-below theorem; plane labels belong to the local maximal ideal after root-plane localization.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_free`: [MinimalExtensions.lean:898](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L898).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_finite`: [MinimalExtensions.lean:901](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L901).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_support`: [MinimalExtensions.lean:904](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L904).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_generated`: [MinimalExtensions.lean:917](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L917).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_upperQuotient`: [MinimalExtensions.lean:925](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L925).

`OAI.KLInvariance.MomentGraph.Sheaf.structureSheaf_minimal`: [MinimalExtensions.lean:944](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L944).
