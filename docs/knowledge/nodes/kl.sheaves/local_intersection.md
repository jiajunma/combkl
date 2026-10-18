---
id: kl.detail.local_intersection
title: The local intersection map from a stalk dual into the stalk
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.costalk_duality
- kl.detail.boundary_pairing
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.localIntersection
  - OAI.KLInvariance.BruhatGraph.localIntersection_range
  - OAI.KLInvariance.BruhatGraph.localIntersection_symmetric
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:132
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:146
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_range
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:180
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_symmetric
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
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

# The local intersection map from a stalk dual into the stalk

For the actual boundary sheaf \(B_b\), let \(K_x\subseteq B_b^x\) be the full outgoing kernel. Compose the inverse of the stalk–costalk duality with its inclusion into the stalk:
\[
I_x:(B_b^x)^*\xrightarrow{\sim}K_x\hookrightarrow B_b^x.
\]
This is the local intersection map. It is injective, its image is exactly \(K_x\), and symmetry of the global pairing gives
\[
\lambda(I_x\mu)=\mu(I_x\lambda).
\]

For \(x<b\), minimality of the boundary cover says
\[
\operatorname{im}I_x\subseteq A_+B_b^x.
\]
Thus its matrix entries satisfy positive-degree constraints. For a homogeneous basis, the diagonal entry associated with a generator of degree \(d_i\) has degree \(d(x,b)-2d_i\).

The map itself is distinct from a numerical bilinear form obtained by specializing coefficients. The strict degree conclusion for a particular diagonal entry includes an explicit nonvanishing hypothesis, stated separately.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.localIntersection`: [PositiveTransfer.lean:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L132).

`OAI.KLInvariance.BruhatGraph.localIntersection_range`: [PositiveTransfer.lean:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L146).

`OAI.KLInvariance.BruhatGraph.localIntersection_symmetric`: [PositiveTransfer.lean:180](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L180).
