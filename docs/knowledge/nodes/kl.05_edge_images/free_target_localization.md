---
id: kl.local.free_target_localization
title: Height-one membership in a free target
kind: theorem
status: proved
primary_topic: kl.05_edge_images
topics:
- kl.05_edge_images
uses: []
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:106
    format: lean-location
    note: OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; sec:edge
    format: section
    note: Chapter organization follows the paper; Lean references identify the precise
      formal statements.
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
- edge_images
---

# Height-one membership in a free target

Let \(R\) be a Noetherian unique factorization domain, let \(E\) be a torsion-free \(R\)-module, and let \(M\subseteq E\) be a free submodule that spans \(E\) over the fraction field. Then
\[
x\in M
\quad\Longleftrightarrow\quad
x/1\in M_{\mathfrak p}
\quad\text{for every height-one prime }\mathfrak p.
\]

*Proof.*

The forward implication follows by localization. For the converse, choose a nonzero denominator \(c\) with \(cx\in M\), and induct on its prime factorization. At each prime factor \(p\), localized membership supplies a second denominator not divisible by \(p\). Compare the two expressions in a free basis of \(M\); divisibility of the coordinates allows \(p\) to be removed from the first denominator. Torsion-freeness of \(E\) justifies cancellation. Repeating the argument gives \(x\in M\).

## What localization can and cannot recover

The freeness assumption concerns the target \(M\) in which membership is tested. The argument uses its free coordinates to clear denominators. It does not require the submodule being compared with \(M\) to be reflexive.

For an explicit distinction, let \(C=k[s,t]\) and \(I=(s,t)\). At every height-one prime, at least one of \(s,t\) is invertible, so
\[
I_{\mathfrak p}=C_{\mathfrak p}.
\]
Nevertheless \(I\ne C\), since \(C/I\simeq k\). This quotient is concentrated at the origin and is invisible to those localizations.

Thus the edge argument first proves an inclusion into a free target. Its later global Hilbert comparison detects the remaining quotient, including a quotient of finite length like this one. The two steps have different mathematical jobs.

## References

[5. Comparison of edge images](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L1).

## Lean formalization

`OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one`: [ModuleAlgebra.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L106).
