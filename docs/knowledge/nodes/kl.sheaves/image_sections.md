---
id: kl.sheaves.image_sections
title: Sections of an image sheaf are the image of the section projector
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.projector_image
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSection_fixed
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap_bijective
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:927
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSection_fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:937
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:943
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:958
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionEquiv
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

# Sections of an image sheaf are the image of the section projector

Let \(B\) be a graded sheaf over a Noetherian algebra, and let \(h:B\to B\) be a graded endomorphism whose vertex maps satisfy \(h_x^2=h_x\). For any vertex subset \(\Omega\), let \(H_\Omega\) denote its induced map on the ambient section module \(\Gamma(B,\Omega)\). Then inclusion of image coordinates gives an isomorphism
\[
\Gamma(\operatorname{im}h,\Omega)
\xrightarrow{\sim}\operatorname{im}H_\Omega.
\]
In this section convention, assignments have values at every vertex and satisfy compatibility on edges whose endpoints are both in \(\Omega\).

*Proof.*

### Step 1. Include an image-sheaf section

A section \(s\) of the image sheaf has values \(s_x\in\operatorname{im}h_x\). Forgetting that image membership gives an ambient assignment in \(B\). The edge-image inclusions carry its compatibility equations to those in \(B\), so this assignment is a section on \(\Omega\).

### Step 2. Show the included section is fixed

At each vertex, write \(s_x=h_x(v_x)\). Idempotence gives
\[
h_x(s_x)=h_x^2(v_x)=h_x(v_x)=s_x.
\]
Thus \(H_\Omega(s)=s\), and \(s\) belongs to the image of \(H_\Omega\), with itself as a preimage. This defines the displayed linear map.

### Step 3. Recover a section of the image sheaf

An element of \(\operatorname{im}H_\Omega\) has the form \(H_\Omega(m)\) for a section \(m\) of \(B\). At vertex \(x\), view \(h_x(m_x)\) as an element of \(\operatorname{im}h_x\).

On an edge with both endpoints in \(\Omega\), the two restrictions are
\[
\rho^-_e(h_x(m_x))=h_e(\rho^-_e(m_x)),\qquad
\rho^+_e(h_y(m_y))=h_e(\rho^+_e(m_y)).
\]
They agree because \(m\) is compatible. Hence these image-valued coordinates define a section of \(\operatorname{im}h\). Its inclusion is exactly \(H_\Omega(m)\), proving surjectivity.

### Step 4. Check injectivity

If two image-sheaf sections have the same included assignment, their values agree as vectors of \(B^x\) at every vertex. Since each image module is a submodule of \(B^x\), their image-valued coordinates agree too. The sections are equal, proving injectivity.

For \(\Omega=V\), this identifies all global sections of a projector image with the actual range of the global section map. Under the word-module section equivalence, the same construction identifies them with the range of the corresponding word endomorphism.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSection_fixed`: [BalancedPairings.lean:927](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L927).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap`: [BalancedPairings.lean:937](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L937).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionMap_bijective`: [BalancedPairings.lean:943](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L943).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.imageSectionEquiv`: [BalancedPairings.lean:958](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L958).
