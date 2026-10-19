---
id: kl.local.localized_relative_primality
title: Relative primality of prime labels after localization
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.localization_rings
- kl.algebra.linear_primes
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.LocalizationRelativePrime.not_dvd_map
  - OAI.KLInvariance.LocalizationRelativePrime.map_prime
  - OAI.KLInvariance.LocalizationRelativePrime.map_relPrime
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:901
    format: lean-location
    note: OAI.KLInvariance.LocalizationRelativePrime.not_dvd_map
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:909
    format: lean-location
    note: OAI.KLInvariance.LocalizationRelativePrime.map_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:918
    format: lean-location
    note: OAI.KLInvariance.LocalizationRelativePrime.map_relPrime
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read not_dvd_map, map_prime and map_relPrime with the omitted domain hypothesis
    on the first lemma. Expanded denominator clearing, the prime-element alternatives,
    nonzero/nonunit of the surviving prime, and the unit case. Explained relative
    primality by common divisors in the local ring.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Relative primality of prime labels after localization

Let \(A\) be a commutative domain, \(\mathfrak p\) a prime ideal, and
\[
\eta:A\longrightarrow A_{\mathfrak p}
\]
the localization map. Let \(a\in A\) be a prime element and assume \(a\nmid b\). Then
\[
\eta(a),\eta(b)
\]
are relatively prime: every element dividing both is a unit.

More precisely, if \(a\in\mathfrak p\), then \(\eta(a)\) is prime and does not divide \(\eta(b)\). If \(a\notin\mathfrak p\), then \(\eta(a)\) is a unit. The nondivisibility assertion in the first case holds for an arbitrary commutative ring; the domain hypothesis is used to retain primality.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Selected products and actual edge-image maps.**

**OpenAI notes:** The notes express the outgoing kernel as the product of the supported labels in the local unique factorization domain, and extend this formula to arbitrary subsets of outgoing edges. Unsupported edges impose no condition. [loc:boundary-product](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L346), [loc:arbitrary-edge-subsets](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L404).

**Lean (primary):** The general kernel theorem assumes the DecompositionMonoid product-divisibility structure and pairwise relative primality only for the supported selected labels. Separate lower- and upper-image theorems use restriction surjectivity to identify the scalar-image submodules. Prime-label relative primality is proved after localization before specialization to the actual coset graph. [PlaneLocalization:791](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L791), [PlaneLocalization:795](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L795), [PlaneLocalization:823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L823), [PlaneLocalization:867](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L867), [PlaneLocalization:878](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L878), [PlaneLocalization:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918), [PlaneLocalization:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L973).

**Role in the proof:** The Blueprint retains the selected-set indexing and writes both image equalities inside the same model edge module. The polynomial-domain specialization supplies every relative-primality and product-divisibility hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Clear a denominator in a localized divisibility

Suppose \(a\in\mathfrak p\) and, toward a contradiction,
\(\eta(a)\mid\eta(b)\). Write a quotient witnessing the divisibility as \(u/t\), with \(t\notin\mathfrak p\), so \(b/1=au/t\). Equality of these localization fractions means that some \(h\notin\mathfrak p\) satisfies
\[
h(tb-au)=0.
\]
Consequently \((ht)b=a(hu)\). The complement of a prime ideal is closed under multiplication, so \(s=ht\notin\mathfrak p\). We have obtained
\[
a\mid sb
\]
for some \(s\notin\mathfrak p\).

Primality of \(a\) gives \(a\mid s\) or \(a\mid b\). The second contradicts the hypothesis. The first would put \(s\) in \(\mathfrak p\), since \(a\in\mathfrak p\) and an ideal contains all multiples of its elements. This also contradicts the choice of \(s\).

Thus \(\eta(a)\nmid\eta(b)\). This argument does not use cancellation in a domain.

### Step 2. Retain primality when the element lies in the prime ideal

Now use that \(A\) is a domain. If \(\eta(z)=0\), the fraction criterion gives \(hz=0\) for some \(h\notin\mathfrak p\). Such \(h\) is nonzero, and cancellation gives \(z=0\). Thus the localization map is injective and \(\eta(a)\ne0\). Its image belongs to the maximal ideal of \(A_{\mathfrak p}\), hence is not a unit.

Suppose \(\eta(a)\) divides a product
\((u/s)(v/t)\), where \(s,t\notin\mathfrak p\). Multiplication by the denominator units reduces this to divisibility of \(\eta(uv)\). Clearing a denominator as in Step 1 gives
\[
a\mid huv
\qquad\text{with }h\notin\mathfrak p.
\]
Primality of \(a\) and \(a\in\mathfrak p\) exclude \(a\mid h\), so \(a\mid uv\). Hence \(a\mid u\) or \(a\mid v\).

After applying \(\eta\) and dividing by the denominator units, \(\eta(a)\) divides \(u/s\) or \(v/t\). Together with nonzero and nonunit, this proves that \(\eta(a)\) is prime.

### Step 3. Deduce relative primality in this case

A prime element is irreducible. If a nonunit \(d\) divided both \(\eta(a)\) and \(\eta(b)\), irreducibility of \(\eta(a)\) would make \(d\) associated to \(\eta(a)\).

Then \(\eta(a)\mid\eta(b)\), contradicting Step 1. Therefore every common divisor is a unit.

### Step 4. Treat a label outside the localization prime

If \(a\notin\mathfrak p\), it is one of the inverted elements, with inverse \(1/a\). Any divisor of a unit is a unit, so \(\eta(a)\) is relatively prime to every element, including \(\eta(b)\).

The two cases prove the theorem.

For example, over a field \(k\), the two coordinate labels \(a,b\) in \(k[a,b]_{(a,b)}\) are relatively prime and both belong to the maximal ideal. Their common-divisor property is the one used to combine divisibility conditions into a product.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalizationRelativePrime.not_dvd_map`: [PlaneLocalization.lean:901](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L901).

`OAI.KLInvariance.LocalizationRelativePrime.map_prime`: [PlaneLocalization.lean:909](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L909).

`OAI.KLInvariance.LocalizationRelativePrime.map_relPrime`: [PlaneLocalization.lean:918](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L918).
