---
id: kl.local.root_factor_divisibility
title: Root factors and plane primes in the edge quotient
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.algebra.root_quotient_coordinates
- kl.local.plane_prime_membership
- kl.local.edge_factor_lift_properties
- kl.local.outgoing_label_product
- kl.foundations.bruhat_step
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.planePrime_span
  - OAI.KLInvariance.BruhatGraph.reducedRoot_dvd_iff_mem_plane
  - OAI.KLInvariance.BruhatGraph.reducedFactor_ne_zero
  - OAI.KLInvariance.BruhatGraph.prime_dvd_reducedFactor
  - OAI.KLInvariance.BruhatGraph.incoming_root_ne_outgoing
  - OAI.KLInvariance.BruhatGraph.reducedKernelProduct_ne_zero
  - OAI.KLInvariance.BruhatGraph.prime_dvd_reducedKernelProduct
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:546
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.planePrime_span
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:732
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.reducedRoot_dvd_iff_mem_plane
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:746
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.reducedFactor_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:752
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.prime_dvd_reducedFactor
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:822
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incoming_root_ne_outgoing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:827
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.reducedKernelProduct_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:838
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.prime_dvd_reducedKernelProduct
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Checked the generic quotient-divisibility/plane-ideal equivalence, including
    equal roots, and the actual edge-product hypotheses for nonzero factors and prime-divisor
    classification in the quotient domain.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Root factors and plane primes in the edge quotient

Let \(W\) be a finite-generator real Coxeter system, let \(A\) be the polynomial coefficient algebra from a real basis of its extended realization, and write \(\lambda(a)\) for a root polynomial. Fix a positive root \(a\), with quotient map
\[
q:A\to C_a=A/(\lambda(a)),\qquad \overline z=q(z).
\]
For every positive root \(\beta\) and \(z\in A\),
\[
\overline{\lambda(\beta)}\mid\overline z
\quad\Longleftrightarrow\quad
z\in\mathfrak p_{\operatorname{span}\{a,\beta\}}
=(\lambda(a),\lambda(\beta)).
\]

Now let \(e:x\to y\) be an edge of a finite Bruhat interval with positive root \(a\), and let \(G\) be any selection of outgoing edges at \(y\). Put
\[
f=F_{x,a},\qquad
g=\prod_{h\in G}\lambda(a_h),\qquad c=fg,
\]
where \(F_{x,a}\) is the polynomial lift of the correction factor and \(a_h\) is the positive root of \(h\). Then \(\overline f,\overline g,\overline c\) are nonzero.

Every prime element \(\pi\in C_a\) dividing \(\overline c\) is associated to \(\overline{\lambda(\beta)}\) for some positive root \(\beta\ne a\). Association means equality up to a unit of \(C_a\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The correction and outgoing products supply one global multiplier.**

**OpenAI notes:** The notes multiply the upper outgoing labels to obtain a nonzero reduced scalar whose multiples lie in the upper image. The correction factor gives a free target of full generic rank, and primes containing reduced roots are related to plane primes. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The outgoing product is defined for any finite graph and selection. Label annihilation and an upper lift prove its image containment. The actual reduced outgoing and correction products are nonzero, and every prime divisor of their product is associated to one reduced independent root. Quotient divisibility by that root is equivalent to membership in its plane ideal. [TerminalKernels:781](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L781), [TerminalKernels:798](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L798), [TerminalKernels:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L732), [TerminalKernels:752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L752), [TerminalKernels:838](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L838).

**Role in the proof:** The Blueprint gives the explicit global multiplier and the complete factor classification used by the membership theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the plane ideal and quotient divisibility

The ideal attached to the linear span of \(a,\beta\) is generated by their two root polynomials. Indeed, linearity makes the polynomial of every vector \(ra+s\beta\) equal to \(r\lambda(a)+s\lambda(\beta)\); conversely both generators come from vectors in that span.

If \(\overline{\lambda(\beta)}\mid\overline z\), choose a quotient scalar \(\overline w\) with
\(\overline z=\overline{\lambda(\beta)}\,\overline w\), and lift it to \(w\in A\). Then \(z-\lambda(\beta)w\in(\lambda(a))\), so
\[
z=\lambda(\beta)w+\lambda(a)v
\]
for some \(v\in A\). Hence \(z\) belongs to the displayed plane ideal. Conversely such an expression reduces to the divisibility identity in \(C_a\). This proves the first assertion for every \(\beta\).

### Step 2. Establish the nonzero reduced factors

The [[node:kl.local.edge_factor_lift_properties|polynomial-lift properties theorem]] gives \(\lambda(a)\nmid f\). The quotient criterion therefore gives \(\overline f\ne0\).

For each \(h:y\to z\) in \(G\), the roots of the consecutive edges \(x\to y\to z\) are distinct. Otherwise the same reflection would give \(z=x\), contrary to increasing length. Thus \(a_h\ne a\).

The [[node:kl.algebra.root_quotient_coordinates|root-quotient coordinate theorem]] makes each \(\overline{\lambda(a_h)}\) a prime, hence nonzero, element of the domain \(C_a\). A finite product of nonzero elements is nonzero, including the empty product \(1\), so \(\overline g\ne0\). Consequently \(\overline c=\overline f\,\overline g\ne0\).

### Step 3. Classify prime divisors of the reduced correction

The polynomial lift is a finite product of representative-root powers. If a prime \(\pi\) divides \(\overline f\), primality supplies a factor
\(\overline{\lambda(\beta)}^{\,k}\)
which it divides. Primality again gives \(\pi\mid\overline{\lambda(\beta)}\). The representative-root construction ensures \(\beta\ne a\).

The reduced root is prime by the [[node:kl.algebra.root_quotient_coordinates|root-quotient coordinate theorem]]. In an integral domain, if a prime element divides another prime element, their quotient is a unit: write the second as the first times a factor, and use irreducibility of the second and the fact that the first is not a unit. Hence the two primes are associated.

### Step 4. Classify prime divisors of the reduced outgoing product

If \(\pi\mid\overline g\), primality in the finite product gives some \(h\in G\) with
\(\pi\mid\overline{\lambda(a_h)}\).
Step 2 gives \(a_h\ne a\), and its reduced root is prime. The same argument as in Step 3 makes \(\pi\) associated to this reduced root.

### Step 5. Split the prime divisors of the combined multiplier

If \(\pi\mid\overline c=\overline f\,\overline g\), primality gives
\(\pi\mid\overline f\) or \(\pi\mid\overline g\).
Step 3 or Step 4 supplies the required positive root \(\beta\ne a\) and the association. This completes the classification.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.planePrime_span`: [TerminalKernels.lean:546](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L546).

`OAI.KLInvariance.BruhatGraph.reducedRoot_dvd_iff_mem_plane`: [TerminalKernels.lean:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L732).

`OAI.KLInvariance.BruhatGraph.reducedFactor_ne_zero`: [TerminalKernels.lean:746](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L746).

`OAI.KLInvariance.BruhatGraph.prime_dvd_reducedFactor`: [TerminalKernels.lean:752](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L752).

`OAI.KLInvariance.BruhatGraph.incoming_root_ne_outgoing`: [TerminalKernels.lean:822](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L822).

`OAI.KLInvariance.BruhatGraph.reducedKernelProduct_ne_zero`: [TerminalKernels.lean:827](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L827).

`OAI.KLInvariance.BruhatGraph.prime_dvd_reducedKernelProduct`: [TerminalKernels.lean:838](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L838).
