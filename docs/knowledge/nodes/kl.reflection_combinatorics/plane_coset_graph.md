---
id: kl.dihedral.plane_coset_graph
title: The induced reflection graph and inversion count on a plane-subgroup coset
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.minimal_plane_cosets
- kl.dihedral.induced_reflections_length
- kl.foundations.interval
- kl.foundations.bruhat_order
lean:
  repository: openai-kl
  modules:
  - Decomposition
  - ReflectionOrders
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.bruhatStep_coset_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_step_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_bruhat
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient
  - OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2244
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bruhatStep_coset_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1178
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_step_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1185
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_bruhat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1196
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:410
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionOrders:413
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient_injective
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

# The induced reflection graph and inversion count on a plane-subgroup coset

Let \(P\) be a root plane with its induced system on \(D_P\), and let \(a_0\) have least ambient length in \(D_Pa_0\). The bijection
\[
D_P\longrightarrow D_Pa_0,\qquad w\longmapsto wa_0
\]
preserves and reflects directed reflection edges and their left reflection labels.

Moreover,
\[
L_P(wa_0)=\ell_P(w).
\]
Intrinsic Bruhat paths therefore map to ambient Bruhat paths, and \(a_0\) is the unique element of least ambient length in its coset.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The graph and count statements are separated in Lean.**

**OpenAI notes:** One lemma states the unique least ambient-length representative, the coset reflection-graph identification, the relative inversion count, and the implication from relative to ambient order. [dih:plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L20).

**Lean (primary):** The source first proves existence of a least representative and sign preservation, then exports the graph, count, and path statements under that least-length hypothesis. [Tits:2166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2166), [Decomposition:1178](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1178), [Decomposition:1196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1196), [Decomposition:1185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1185).

**Role in the proof:** The proof below uses those exported statements and derives uniqueness explicitly from the plane count and the length-zero characterization of the identity.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compare plane inversion counts

For every positive root \(r\in P\), the [[node:kl.dihedral.minimal_plane_cosets|least-coset sign theorem]] gives
\[
(wa_0)^{-1}r\text{ negative}
\quad\Longleftrightarrow\quad
w^{-1}r\text{ negative}.
\]
The two finite plane inversion sets are therefore equal. Their counts give
\[
L_P(wa_0)=L_P(w)=\ell_P(w),
\]
using the [[node:kl.dihedral.induced_reflections_length|intrinsic length theorem]] for the second equality.

### Step 2. Recover a subgroup reflection from an ambient coset edge

Suppose \(ga_0\to ha_0\) is an ambient edge with left reflection label \(t\). The relation
\(ha_0=tga_0\) gives \(h=tg\) by cancellation, hence
\(t=hg^{-1}\in D_P\).

Since \(t^2=1\), it also gives \(tha_0=ga_0\). Thus the edge orientation says exactly that \(t\) lowers \(ha_0\). The [[node:kl.dihedral.minimal_plane_cosets|least-coset sign theorem]] transfers this to the assertion that \(t\) lowers \(h\).

The intrinsic and ambient left-inversion conditions agree on \(D_P\), so \(t\) is an intrinsic left inversion of \(h\). Therefore \(g\to h\) is an induced reflection edge with the same label \(t\).

### Step 3. Map an induced edge into the coset

Conversely, an induced edge \(g\to h\) has \(h=tg\), where \(t\in D_P\) is an intrinsic reflection lowering \(h\). It is an ambient reflection, and the [[node:kl.dihedral.minimal_plane_cosets|least-coset sign theorem]] makes it lower \(ha_0\).

The identity \(tha_0=ga_0\) now gives the ambient directed edge \(ga_0\to ha_0\), with label \(t\). This proves the two edge directions.

### Step 4. Transfer paths and relative intervals

A finite path of induced reflection edges maps, edge by edge, to an ambient reflection path. Since strong Bruhat order is the reflexive transitive closure of those edges,
\[
g\le_P h\quad\Longrightarrow\quad ga_0\le_W ha_0.
\]

Consequently the map \(z\mapsto za_0\) sends the relative interval \([g,h]_P\) into the ambient interval \([ga_0,ha_0]_W\), and preserves order. It is injective because \(za_0=z'a_0\) implies \(z=z'\) by right cancellation.

### Step 5. Prove uniqueness of the minimum

Let \(a_1\) be another element of least ambient length in the same coset. Write \(a_1=wa_0\), \(w\in D_P\).

Minimality of \(a_1\) makes \(a_1^{-1}\) preserve every positive root in \(P\), so \(L_P(a_1)=0\). Step 1 gives
\[
0=L_P(a_1)=\ell_P(w).
\]
A Coxeter element of length zero is the identity. Hence \(w=1\) and \(a_1=a_0\).

This last argument derives uniqueness explicitly from the proved sign and count formulas.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bruhatStep_coset_iff`: [Tits.lean:2244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2244).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_step_iff`: [Decomposition.lean:1178](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1178).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_bruhat`: [Decomposition.lean:1185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1185).

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_length_eq`: [Decomposition.lean:1196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1196).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient`: [ReflectionOrders.lean:410](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L410).

`OAI.KLInvariance.TitsSpace.PlaneBasis.intervalToAmbient_injective`: [ReflectionOrders.lean:413](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L413).
