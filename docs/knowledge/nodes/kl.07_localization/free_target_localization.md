---
id: kl.local.free_target_localization
title: Height-one membership in a free target
kind: theorem
status: proved
primary_topic: kl.07_localization
topics:
- kl.07_localization
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
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
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

### Step 1. Translate localized membership into denominators

The implication \(x\in M\Rightarrow x/1\in M_{\mathfrak p}\) is immediate.
For the converse, the generic-span hypothesis provides \(c\ne0\) with \(cx\in M\).

For an irreducible element \(p\), the ideal \((p)\) is prime of height one in the stated Noetherian UFD. The localized membership assumption gives a denominator \(a\notin(p)\) with \(ax\in M\). Equivalently \(p\nmid a\). If equality in the localization initially uses two denominators, multiply them; both lie outside the prime, so their product still does.

### Step 2. Remove one prime factor from c

Suppose \(c=pc_1\). In the free module \(M\), let \(m=pc_1x\) and \(n=ax\). They satisfy
\(am=pc_1n\).
Choose a free basis \((e_i)\) of \(M\) and expand both vectors in their finitely supported coordinates:
\[
a\,m_i=pc_1n_i\quad\text{for every }i.
\]
Since \(p\) is prime and does not divide \(a\), it divides every \(m_i\). Write \(m_i=pu_i\), retaining finite support, and put \(m'=\sum_i u_ie_i\in M\). Then \(m=pm'\).

### Step 3. Cancel in the ambient module

The two expressions for \(m\) give
\(p(c_1x-m')=0\) in \(E\). The ambient module is torsion-free and \(p\ne0\), so \(c_1x=m'\in M\). Thus one prime factor of the denominator has been removed.

### Step 4. Finish by unique factorization

Factor the original nonzero \(c\) into a unit times finitely many irreducibles, counted with multiplicity. Repeat Steps 1–3 for every factor. When only a unit \(u\) remains, \(ux\in M\) implies \(x=u^{-1}(ux)\in M\).

This proves the equivalence. If the ring is a field, every nonzero denominator is already a unit, so the same argument covers the empty family of height-one primes.

### Step 5. Keep the direction of application straight

The free module is the target in which membership is being tested. The theorem does not say that two arbitrary submodules with equal height-one localizations are equal. For example \((s,t)\subsetneq k[s,t]\) has the same localization as the whole ring at every height-one prime. The later Hilbert comparison, not localization alone, detects that possible remaining quotient.

## References

[5. Comparison of edge images](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L1).

## Lean formalization

`OAI.KLInvariance.EdgeLattice.mem_iff_localized_at_height_one`: [ModuleAlgebra.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L106).
