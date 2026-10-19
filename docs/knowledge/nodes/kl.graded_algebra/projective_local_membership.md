---
id: kl.algebra.projective_local_membership
title: Prime-denominator membership in a projective target
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.localized_membership
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  - ModuleAlgebra
  declarations:
  - OAI.KLInvariance.ProjectiveLattice.finsupp_divide
  - OAI.KLInvariance.ProjectiveLattice.prime_divide_of_relation
  - OAI.KLInvariance.ProjectiveLattice.mem_of_prime_local_membership
  - OAI.KLInvariance.EdgeLattice.mem_of_prime_local_membership
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1870
    format: lean-location
    note: OAI.KLInvariance.ProjectiveLattice.finsupp_divide
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1886
    format: lean-location
    note: OAI.KLInvariance.ProjectiveLattice.prime_divide_of_relation
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1904
    format: lean-location
    note: OAI.KLInvariance.ProjectiveLattice.mem_of_prime_local_membership
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ModuleAlgebra:45
    format: lean-location
    note: OAI.KLInvariance.EdgeLattice.mem_of_prime_local_membership
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read the free and projective prime-removal arguments. Used the source canonical
    free-module section and evaluation retraction, finite-support division, ambient
    torsion-free cancellation and UFD induction.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Prime-denominator membership in a projective target

Let \(R\) be a unique factorization domain, \(E\) a torsion-free \(R\)-module, and \(M\subseteq E\) a projective submodule. Fix \(x\in E\). Assume
\[
\exists c\ne0,\quad cx\in M,
\]
and, for every prime element \(p\),
\[
\exists a,\quad p\nmid a,\quad ax\in M.
\]
Then \(x\in M\). The free-target theorem is the special case where \(M\) is free.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**General module interface for the local membership test.**

**OpenAI notes:** The free-target lemma uses a polynomial coefficient ring and a finite free ambient module. Basis coordinates in the fraction field lie in every height-one local ring, so their denominators are units. [edge:lattice](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26).

**Lean (primary):** The free-target interface allows a torsion-free ambient module over a UFD and states generic span through nonzero scalar multipliers. Its proof removes prime factors from those multipliers. A separate projective-target version obtains finite-support coordinates through a free-module section and retraction. [ModuleAlgebra:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L45), [ModuleAlgebra:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L106), [IntegralPairings:1904](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1904).

**Role in the proof:** The proofs below expose the exact generic-span and prime-denominator witnesses used by local-to-global membership.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Obtain coordinates with a retraction

There is a canonical free module on the underlying elements of \(M\), whose vectors are finitely supported coefficient families. Its evaluation map
\[
\varepsilon:R^{(M)}\twoheadrightarrow M,\qquad
(c_m)\longmapsto\sum_m c_m m
\]
is surjective: the single basis vector indexed by \(m\) evaluates to \(m\).

Projectivity of \(M\) gives a linear section \(s:M\to R^{(M)}\), with \(\varepsilon s=1_M\). These maps provide free coordinates for the divisibility calculation while retaining a map back into \(M\).

### Step 2. Divide a projective vector using a prime relation

Suppose \(p\) is prime, \(p\nmid a\), and \(m,n\in M\) satisfy
\[
am=pc\,n.
\]
Apply the linear map \(s\) and take a coordinate:
\[
a(s(m))_i=pc(s(n))_i.
\]
Primality and \(p\nmid a\) imply \(p\mid(s(m))_i\) for every \(i\).

The vector \(s(m)\) has finite support. Divide those finitely many coefficients by \(p\), putting zero outside that support, to obtain a finitely supported vector \(z\) with \(pz=s(m)\).

Apply \(\varepsilon\):
\[
p\,\varepsilon(z)=\varepsilon(s(m))=m.
\]
Thus \(m\) is divisible by \(p\) inside \(M\). If \(M\) is free, its basis coordinates and inverse basis map give this same calculation directly.

### Step 3. Remove a prime factor from a generic denominator

Start with \(cx\in M\), \(c\ne0\), and factor \(c\). If \(c\) is a unit, then \(x=c^{-1}(cx)\in M\).

Otherwise write \(c=pc_1\), with \(p\) prime and \(c_1\ne0\). Choose the local witness \(a\) with \(p\nmid a\) and \(ax\in M\). In \(M\), set
\[
m=pc_1x,\qquad n=ax.
\]
Commutativity of scalar multiplication gives \(am=pc_1n\). Step 2 supplies \(m'\in M\) with \(pm'=m\).

### Step 4. Cancel in the ambient module

Inside \(E\), the last equality is \(pm'=pc_1x\). Since \(p\ne0\) and \(E\) is torsion-free,
\[
m'=c_1x.
\]
Thus the smaller denominator \(c_1\) also sends \(x\) into \(M\).

### Step 5. Finish the finite factorization induction

A nonzero element of a UFD is a unit times finitely many prime factors, counted with multiplicity. Repeating Steps 3–4 removes one factor at a time. The final unit case gives \(x\in M\).

The hypotheses for every prime concern the fixed vector \(x\), so they remain available at each factor-removal step.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ProjectiveLattice.finsupp_divide`: [IntegralPairings.lean:1870](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1870).

`OAI.KLInvariance.ProjectiveLattice.prime_divide_of_relation`: [IntegralPairings.lean:1886](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1886).

`OAI.KLInvariance.ProjectiveLattice.mem_of_prime_local_membership`: [IntegralPairings.lean:1904](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1904).

`OAI.KLInvariance.EdgeLattice.mem_of_prime_local_membership`: [ModuleAlgebra.lean:45](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L45).
