---
id: kl.notes.graded_nakayama
title: Graded Nakayama by induction on degree
kind: theorem
status: proved
primary_topic: kl.02_background
topics:
- kl.02_background
uses:
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.eq_top_of_positive_smul_sup
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:20
    format: lean-location
    note: OAI.KLInvariance.Graded.eq_top_of_positive_smul_sup
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Graded Nakayama by induction on degree

Let \(A\) be nonnegatively graded, and let \(M\) be a graded module bounded below. Let \(N\subseteq M\) be closed under homogeneous components. If
\[
N+A_{>0}M=M,
\]
then \(N=M\).

*Proof.*

Choose a lower degree bound \(d_0\), and induct on the nonnegative integer \(n-d_0\) for a homogeneous element \(m\in M_n\). By the assumed equality, write \(m\) as an element of \(N\) plus a finite sum of positive-degree multiples. Take the degree-\(n\) component of this expression.

The contribution from \(N\) stays in \(N\) because \(N\) is homogeneous. A term with coefficient in degree \(i>0\) can contribute in degree \(n\) only through a module component of degree \(n-i<n\). That component belongs to \(N\) by induction, so its multiple does too. Hence every homogeneous element lies in \(N\), and the direct-sum decomposition proves the claim.

The lower bound starts the induction. Positive grading alone, without a lower bound on the module, would not justify this argument. A useful special case is \(M=A_{>0}M\), which forces \(M=0\). This is the form used to eliminate redundant kernels in minimal covers.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.Graded.eq_top_of_positive_smul_sup`: [GradedModules.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L20).
