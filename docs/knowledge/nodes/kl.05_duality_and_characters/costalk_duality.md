---
id: kl.detail.costalk_duality
title: The full outgoing kernel is dual to the stalk
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.section_duality
- kl.sheaves.upward_kernel
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1447
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1459
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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

# The full outgoing kernel is dual to the stalk

Let \(B\) be a minimal-boundary sheaf on a finite Bruhat interval over its polynomial coefficient ring \(A\), equipped with section duality. At a vertex \(x\), let
\[
K_x=\ker\!\left(B^x\longrightarrow\bigoplus_{e:x\to y}B^e\right).
\]
Then there is an \(A\)-linear isomorphism
\[
K_x\simeq\operatorname{Hom}_A(B^x,A).
\]
In particular \(K_x\) is finite free because \(B^x\) is finite free.

*Proof.*

The quotient rules and coprimality of the appropriate incoming labels identify \(K_x\), after inserting the necessary incoming-label product, with global sections supported only at \(x\). Perfection and cut balance identify those supported sections with the dual of the stalk: a functional on \(B^x\) pulls back through evaluation to a functional on global sections, and its representing section has the required support.

Composing the two identifications gives the displayed equivalence. Its grading shift must still be tracked separately. The next reciprocity statement performs that calculation instead of treating this ungraded isomorphism as degree zero.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.costalkEquivDual`: [Support.lean:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1447).

`OAI.KLInvariance.BruhatGraph.costalk_free_of_duality`: [Support.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1459).
