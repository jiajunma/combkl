---
id: kl.detail.section_duality
title: Balanced perfect duality on global sections
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.free_quotient_sheaf
- kl.sheaves.integral_cuts
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.SectionDuality
  - OAI.KLInvariance.BruhatGraph.SectionDuality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:170
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.SectionDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1432
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.SectionDuality
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
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

# Balanced perfect duality on global sections

Let \(B\) be a free sheaf on a Bruhat interval, with its polynomial labels and finitely many edges. Write \(\Gamma=\Gamma(B)\), let \(p\) be the product of all edge labels, and define
\[
C_xm=p\,\delta_x(m_x).
\]
The upper-quotient condition ensures these assignments are global sections.

A section duality is an \(A\)-linear isomorphism
\[
D:\Gamma\xrightarrow{\sim}\operatorname{Hom}_A(\Gamma,A)
\]
satisfying cut balance:
\[
\langle C_xm,n\rangle=\langle m,C_xn\rangle
\quad\text{for every }x,m,n,
\qquad \langle m,n\rangle=D(m)(n).
\]
The isomorphism supplies a unique section representing each functional. Balance makes each cut self-adjoint: applying the cut in either argument has the same effect.

## The two recorded fields

The pairing field records \(D\), including its inverse and \(A\)-linearity. The balance field records the displayed equation for the cuts made with the actual edge-label product.

The boundary-sheaf version specializes this same construction to a boundary sheaf. In the free-sheaf version the objects may also be word sheaves, because the cut construction uses their upper quotients and the later stalk-duality argument uses their free stalks and global generation.

A perfect graded section pairing supplies \(D\) and, by [[node:kl.sheaves.cut_balance]], satisfies cut balance. Its separate homogeneity equation then controls the degrees of the resulting stalk-duality maps. The section-duality structure itself records the pairing and balance.

## Recovering a functional from a supported section

For \(m\) supported at \(x\), the cut identities give \(C_xm=pm\). If \(n_x=0\), then \(C_xn=0\). Balance yields
\[
p\langle m,n\rangle
=\langle C_xm,n\rangle
=\langle m,C_xn\rangle=0.
\]
The label product is nonzero, and \(A\) is a domain, so \(\langle m,n\rangle=0\). Consequently pairing with \(m\) depends only on \(n_x\). Global generation supplies a section with any prescribed \(x\)-value, so this defines a functional on \(B^x\).

Conversely, a stalk functional \(\lambda\) gives the global functional \(\lambda\circ\pi_x\). The inverse of \(D\) represents it by a section. Applying the balance equation at every other vertex proves that representative is supported at \(x\), as shown in [[node:kl.sheaves.support_annihilator]] and [[node:kl.sheaves.supported_stalk_duality]].

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the stalk–costalk relation.**

**OpenAI notes:** The normalization proof describes a lower-support layer, relates it to the outgoing kernel using flabbiness, and obtains its graded rank through the cited moment-graph and Soergel-module results. It temporarily doubles degrees and uses the shift convention M(k)^j = M^{j+k}. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-upward-rank](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L349).

**Lean (primary):** The local construction starts with a free sheaf and a specified balanced perfect section pairing. Integral cuts identify vertex support with an evaluation-kernel annihilator. The incoming label product identifies that support module with the outgoing kernel, giving an explicit linear equivalence with the stalk dual. [Support:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L521), [CharacterReciprocity:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L150), [CharacterReciprocity:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L185).

**Role in the proof:** The Blueprint follows these integral maps. The pairing construction and its homogeneity equation supply the later graded reciprocity statement. Degree shifts use the Lean convention M(d)_n = M_{n-d}.
<!-- source-comparison:end -->

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

In both declarations, `pairing` is the linear equivalence with the dual and `balanced` is the cut-balance equation.

`OAI.KLInvariance.BruhatGraph.FreeSheaf.SectionDuality`: [CharacterReciprocity.lean:170](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L170).

`OAI.KLInvariance.BruhatGraph.SectionDuality`: [Support.lean:1432](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1432).
