---
id: kl.realization.plane_reflection_membership
title: Reflections in a subspace subgroup are detected by their roots
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.root_subgroups
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.planeSubgroup_le_moving
  - OAI.KLInvariance.TitsSpace.Represents.mem_of_moving
  - OAI.KLInvariance.TitsSpace.Represents.planeSubgroup_mem_iff
  - OAI.KLInvariance.TitsSpace.planeSubgroup_preserves
  - OAI.KLInvariance.TitsSpace.reflection_between_coset_mem
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2113
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeSubgroup_le_moving
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2122
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.mem_of_moving
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2134
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.planeSubgroup_mem_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2183
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.planeSubgroup_preserves
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2144
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflection_between_coset_mem
verification:
  statement: accepted
  proof: accepted
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

# Reflections in a subspace subgroup are detected by their roots

For a finite-generator Coxeter system and a subspace \(P\) of its original root space,
\[
D_P\subseteq G_P.
\]
Every element of \(D_P\) preserves \(P\). If a root \(a\) represents the ambient reflection \(t\), then
\[
t\in D_P\quad\Longleftrightarrow\quad a\in P.
\]

Consequently, a reflection carrying one element of a coset \(D_Px\) to another has its root in \(P\).

*Proof.*

### Step 1. Check the displacement of a generating reflection

For \(a\in P\), the reflection formula gives
\[
r_a(v)-v=-B(a,v)a\in P.
\]
Thus each generator \(r_a\) of \(D_P\) belongs to \(G_P\). The subgroup laws for \(G_P\) imply that all products of these generators belong to it, proving \(D_P\subseteq G_P\).

### Step 2. Recover a root from its own displacement

Suppose \(t\in G_P\) is represented by \(a\). Since \(B(a,a)=2\),
\[
\rho(t)a-a=(a-2a)-a=-2a\in P.
\]
Multiplying by \(-1/2\) gives \(a\in P\).

If \(t\in D_P\), Step 1 places it in \(G_P\), and this argument proves \(a\in P\). Conversely, if \(a\in P\), its representing reflection is one of the generators of \(D_P\). This proves the equivalence.

### Step 3. Preserve the subspace

For \(w\in D_P\) and \(v\in P\), Step 1 gives \(\rho(w)v-v\in P\). Adding \(v\) yields \(\rho(w)v\in P\). Applying the same argument to \(w^{-1}\) gives equality \(\rho(w)P=P\).

### Step 4. Identify a reflection between coset vertices

Let \(g,h\in D_P\), and suppose an ambient reflection \(t\) satisfies
\[
hx=t(gx).
\]
Right cancellation gives \(h=tg\), so \(t=hg^{-1}\in D_P\). Step 2 then places its root in \(P\).

This identifies the possible reflection labels of the ambient graph restricted to the coset.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.planeSubgroup_le_moving`: [Tits.lean:2113](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2113).

`OAI.KLInvariance.TitsSpace.Represents.mem_of_moving`: [Tits.lean:2122](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2122).

`OAI.KLInvariance.TitsSpace.Represents.planeSubgroup_mem_iff`: [Tits.lean:2134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2134).

`OAI.KLInvariance.TitsSpace.planeSubgroup_preserves`: [Tits.lean:2183](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2183).

`OAI.KLInvariance.TitsSpace.reflection_between_coset_mem`: [Tits.lean:2144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2144).
