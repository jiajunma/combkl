---
id: kl.local.free_target_localization
title: Height-one membership in a free target
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.algebra.localized_membership
- kl.algebra.projective_local_membership
lean:
  repository: openai-kl
  modules:
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.EdgeLattice.exists_denominator_of_localized_mem
  - OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one
  - OAI.KLInvariance.EdgeLattice.eq_iInf_height_one_localizations
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:89
    format: lean-location
    note: OAI.KLInvariance.EdgeLattice.exists_denominator_of_localized_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:106
    format: lean-location
    note: OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:129
    format: lean-location
    note: OAI.KLInvariance.EdgeLattice.eq_iInf_height_one_localizations
  - artifact: openai-kl-paper
    locator: 5. Comparison of edge images; sec:edge
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read the exact Noetherian-UFD height-one equivalence and intersection theorem.
    Retained global scalar generic span and free target, and linked the fully expanded
    prime-removal proof.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Height-one membership in a free target

Let \(R\) be a Noetherian unique factorization domain, let \(E\) be torsion-free, and let \(M\subseteq E\) be free. Assume full generic span in the scalar form
\[
\forall x\in E,\quad\exists c\ne0,\quad cx\in M.
\]
Then
\[
x\in M\quad\Longleftrightarrow\quad
x/1\in M_{\mathfrak p}
\text{ for every prime ideal }\mathfrak p\text{ of height one}.
\]
Equivalently, \(M\) is the intersection of the preimages of those localized submodules in \(E\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**General module interface for the local membership test.**

**OpenAI notes:** The free-target lemma uses a polynomial coefficient ring and a finite free ambient module. Basis coordinates in the fraction field lie in every height-one local ring, so their denominators are units. [edge:lattice](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

**Lean (primary):** The free-target interface allows a torsion-free ambient module over a Noetherian UFD and states generic span through nonzero scalar multipliers. Its proof removes prime factors from those multipliers. A separate projective-target version obtains finite-support coordinates through a free-module section and retraction. [ModuleAlgebra:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L45), [ModuleAlgebra:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L106), [IntegralPairings:1904](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1904).

**Role in the proof:** The proofs below expose the exact generic-span and prime-denominator witnesses used by local-to-global membership.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Localize an existing member

If \(x\in M\), the fraction \(x/1\) has a numerator in \(M\), so it belongs to every \(M_{\mathfrak p}\).

### Step 2. Obtain scalar witnesses at the principal prime ideals

Assume all the localized membership conditions. Let \(p\) be any prime element. Its ideal \((p)\) is a prime of height one.

The hypothesis at \((p)\), followed by the denominator-clearing calculation, gives \(a\notin(p)\) with \(ax\in M\). Equivalently \(p\nmid a\).

### Step 3. Apply prime-denominator membership

The generic-span assumption gives a nonzero \(c\) with \(cx\in M\). Step 2 gives the required witness for every prime element.

The [[node:kl.algebra.projective_local_membership|prime-denominator theorem]] applies to the free target \(M\), which is projective, inside the torsion-free ambient module \(E\). It yields \(x\in M\).

### Step 4. Express the result as an intersection

A vector lies in the preimage of \(M_{\mathfrak p}\) exactly when its localized image \(x/1\) lies in that submodule. Membership in the intersection means that this holds for every height-one prime. The equivalence just proved identifies the intersection with \(M\).

If \(R\) is a field, every nonzero generic denominator is a unit. The generic-span condition then gives \(M=E\), agreeing with the intersection over the empty family of height-one primes.

For \(R=k[X,Y]\) and \(M=XR\subseteq R\), the prime \((X)\) tests divisibility by \(X\): \(ax\in XR\) with \(X\nmid a\) implies \(X\mid x\). At a different height-one prime, \(X\) is a unit and the localized ideal fills the localized ring.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.EdgeLattice.exists_denominator_of_localized_mem`: [ModuleAlgebra.lean:89](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L89).

`OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one`: [ModuleAlgebra.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L106).

`OAI.KLInvariance.EdgeLattice.eq_iInf_height_one_localizations`: [ModuleAlgebra.lean:129](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L129).
