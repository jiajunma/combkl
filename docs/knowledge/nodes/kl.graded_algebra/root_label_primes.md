---
id: kl.algebra.root_label_primes
title: Root-label primality, relative primality and regularity
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.polynomial_labels
- kl.algebra.linear_primes
- kl.algebra.root_quotient_coordinates
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_prime
  - OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd
  - OAI.KLInvariance.BruhatGraph.root_injective_on_labels
  - OAI.KLInvariance.BruhatGraph.polynomialLabel_prime
  - OAI.KLInvariance.BruhatGraph.label_eq_of_polynomialLabel_dvd
  - OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime
  - OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1360
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1372
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1379
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1061
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.root_injective_on_labels
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1065
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.polynomialLabel_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1071
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.label_eq_of_polynomialLabel_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1090
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1100
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read the polynomial-root and edge-label divisibility proofs in PlaneLocalization
    and Support. Expanded the embedding step, reflection equality at an endpoint,
    prime relative primality and cancellation on a free quotient module.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Root-label primality, relative primality and regularity

Fix a finite-generator Coxeter system, a basis of its real extended realization, and the resulting polynomial coefficient ring \(A\). Choose a Bruhat interval \([u,b]\) with its root-labelled graph. Every root label is a nonzero prime linear polynomial.

Distinct positive roots have labels that do not divide one another. For an edge pair, divisibility of the labels forces equality of the reflection labels. At a fixed vertex, distinct incoming edge labels are relatively prime, and an outgoing label does not divide an incoming label.

A nonzero reduced label acts injectively on a free module over the corresponding edge coefficient ring.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Canonical labels for the same principal ideals.**

**OpenAI notes:** The coefficient discussion uses degree-one linear root labels and permits any nonzero real scalar multiple, because only the principal ideal matters. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The label is the coordinate polynomial of the embedded canonical positive root for the reflection. Its primality and quotient are proved for that actual element. [SheafMorphisms:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L144), [Support:1065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1065), [ReflectionSchedules:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L824).

**Role in the proof:** Multiplying a label by a nonzero field scalar leaves its principal ideal unchanged. The fixed label used by the code therefore presents the same scalar quotient described in the notes.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport linear primality to polynomial coordinates

A positive root is nonzero, and its embedding into the extended realization is injective. The [[node:kl.algebra.linear_primes|linear-prime theorem]] therefore makes its symmetric generator prime.

The chosen algebra isomorphism from the symmetric algebra to \(A\) preserves primality and nonvanishing. Its coordinate formula is a linear combination of variables, proving degree one.

### Step 2. Turn label divisibility into proportional roots

If one polynomial root label divides another, apply the inverse coordinate isomorphism. The corresponding symmetric generators satisfy the same divisibility.

The [[node:kl.algebra.linear_primes|linear-prime theorem]] puts the second embedded root in the line of the first. Injectivity of the original-to-extended embedding then makes the original roots proportional. Distinct positive roots are linearly independent by the root correspondence, so the two roots must coincide.

For edge labels, equality of their positive roots implies equality of their reflections, because each positive root represents a unique reflection.

### Step 3. Prove relative primality of distinct incoming labels

Two incoming edges with the same target and the same reflection have the same source: if the target is \(x\), the source is obtained by applying that reflection to \(x\). They are therefore the same edge.

Distinct incoming edges consequently have distinct reflection labels, and Step 2 excludes divisibility between their prime polynomial labels. A common nonunit divisor of two prime elements would be associated to each, forcing divisibility. Thus every common divisor is a unit, which is relative primality.

### Step 4. Compare an outgoing and an incoming label

Suppose an outgoing edge and an incoming edge at \(x\) had the same reflection \(t\). The outgoing orientation would require \(\ell(tx)>\ell(x)\); the incoming orientation would require \(\ell(tx)<\ell(x)\). This is impossible.

By Step 2, their labels therefore cannot satisfy the stated divisibility.

### Step 5. Cancel a surviving scalar in a free edge module

If a root label \(\beta\) is not divisible by \(\alpha\), its class in \(A/(\alpha)\) is nonzero. That edge coefficient ring is a domain by the [[node:kl.algebra.root_quotient_coordinates|root-quotient theorem]].

Let \(E\) be free over \(A/(\alpha)\). If \(\overline\beta v=0\), expand \(v\) in a free basis. Each coefficient is killed by the nonzero scalar \(\overline\beta\), hence is zero in the domain. Therefore \(v=0\).

This regularity supplies the scalar-injectivity hypotheses in saturated-kernel and support calculations.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.polynomialRoot_homogeneous`: [PlaneLocalization.lean:1360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1360).

`OAI.KLInvariance.BruhatGraph.polynomialRoot_prime`: [PlaneLocalization.lean:1372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1372).

`OAI.KLInvariance.BruhatGraph.polynomialRoot_not_dvd`: [PlaneLocalization.lean:1379](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1379).

`OAI.KLInvariance.BruhatGraph.root_injective_on_labels`: [Support.lean:1061](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1061).

`OAI.KLInvariance.BruhatGraph.polynomialLabel_prime`: [Support.lean:1065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1065).

`OAI.KLInvariance.BruhatGraph.label_eq_of_polynomialLabel_dvd`: [Support.lean:1071](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1071).

`OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime`: [Support.lean:1090](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1090).

`OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd`: [Support.lean:1100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1100).
