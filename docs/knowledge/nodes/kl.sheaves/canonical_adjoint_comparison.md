---
id: kl.sheaves.canonical_adjoint_comparison
title: The canonical comparison with the adjoint image is an isomorphism
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.adjoint_boundary_recognition
- kl.sheaves.adjoint_fixed_stalk
- kl.sheaves.boundary_top_detection
- kl.sheaves.split_sheaf_properties
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom_top_bijective
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso_vertex
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:785
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:822
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:826
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom_top_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:847
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso_vertex
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
- duality_and_characters
---

# The canonical comparison with the adjoint image is an isomorphism

Fix a finite-generator Coxeter system and a basis of its real extended realization, and use the graded symmetric coefficient algebra. Let \(B\) be a normalized boundary sheaf split into the graded sheaf \(W\) of a reduced word, on its lower Bruhat interval. Write
\[
i:B\to W,\quad p:W\to B,\quad pi=1,\qquad e=ip.
\]
For the adjoint image \(C=\operatorname{im}e^*\), write
\[
j:C\to W,\quad q:W\to C,\quad qj=1,\qquad jq=e^*.
\]
The canonical comparison
\[
h=qi:B\longrightarrow C
\]
is a graded sheaf isomorphism. At each stalk its inclusion in the word stalk is
\[
j_xh_x(v)=e_x^*i_x(v).
\]

*Proof.*

### Step 1. Construct the comparison from the split maps

Both \(i\) and \(q\) are graded sheaf morphisms, so their composite \(h\) is one as well. The identity \(jq=e^*\) gives
\(jh=e^*i\), which is the stated component formula.

### Step 2. Exhibit its inverse at the top

At the top vertex \(b\), the [[node:kl.sheaves.adjoint_fixed_stalk|normalized-projector theorem]] gives
\[
i_bp_b=1_{W^b},\qquad j_bq_b=1_{W^b}.
\]
Define \(g_b=p_bj_b:C^b\to B^b\). Then
\[
g_bh_b=p_bj_bq_bi_b=p_bi_b=1_{B^b},
\]
\[
h_bg_b=q_bi_bp_bj_b=q_bj_b=1_{C^b}.
\]
Thus the specified map \(h_b\) is bijective.

### Step 3. Use recognition to place the map between boundary objects

The [[node:kl.sheaves.adjoint_boundary_recognition|adjoint-image recognition theorem]] supplies a graded sheaf isomorphism \(r:B\to C\). The [[node:kl.sheaves.split_sheaf_properties|split-summand theorem]] gives \(C\) the same upper-quotient rule as \(W\) and \(B\).

The coefficient algebra is a connected nonnegative graded Noetherian domain, and the interval has finite vertices and edges. All hypotheses of the recognized-target form of the [[node:kl.sheaves.boundary_top_detection|top-detection theorem]] therefore hold.

### Step 4. Obtain global bijectivity for the specified map

Apply that theorem to \(h\) and the recognition isomorphism \(r\). Concretely, \(r^{-1}h\) is a boundary-sheaf endomorphism bijective at the top. Downward comparison of the minimal stalk covers makes it bijective at every stalk. Upper quotients give the edge bijections. Thus \(r^{-1}h\), and hence \(h\), is a graded sheaf isomorphism.

The resulting isomorphism has exactly the component maps \(h_x=q_xi_x\), so the identity \(j_xh_x=e_x^*i_x\) remains part of its description. This formula determines the pairing pulled back to \(B\).

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.comparison_bijective`: [EdgeLocalization.lean:785](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L785).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom`: [EdgeLocalization.lean:822](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L822).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointHom_top_bijective`: [EdgeLocalization.lean:826](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L826).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso`: [EdgeLocalization.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L833).

`OAI.KLInvariance.TitsSpace.bottCanonicalAdjointIso_vertex`: [EdgeLocalization.lean:847](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L847).
