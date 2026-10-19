---
id: kl.algebra.tensor_scalar_quotient
title: Tensor extension of a principal scalar quotient
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.scalar_quotient
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul
  - OAI.KLInvariance.MomentGraph.Sheaf.span_map
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient_tmul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1228
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1230
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1235
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.span_map
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1239
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1244
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient_tmul
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read baseChangeScalar, span_map and the exact S-linear baseChangeQuotient
    construction/formula. Expanded the balanced forward map, inverse quotient map
    and both inverse identities for an arbitrary commutative scalar extension.
tags:
- Kazhdan-Lusztig
- coefficient-rings
---

# Tensor extension of a principal scalar quotient

Let \(\varphi:R\to S\) be a homomorphism of commutative rings and let \(a\in R\). There is an \(S\)-linear equivalence
\[
\Theta_a:S\otimes_R R/(a)\xrightarrow{\sim}S/(\varphi(a))
\]
given by
\[
\Theta_a(s\otimes[r])=[s\varphi(r)].
\]
Its inverse sends \([s]\) to \(s\otimes[1]\). These are the source's baseChangeQuotient and its pure-tensor formula.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coefficient maps and scalar reduction.**

**OpenAI notes:** The edge-image proof localizes at the plane prime, passes to the quotient by the current root label, and expresses the remaining plane labels as uniformizers times units in the resulting localized edge ring. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The coefficient operations are explicit tensor and quotient maps. A real-linear reduction kills the current root; writing another root as s*a+r*b gives a nonzero field coefficient r and therefore a unit multiple after reduction. The root-label compatibility formulas identify these elements with the actual polynomial labels. [MinimalExtensions:1239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1239), [PlaneLocalization:1315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1315), [PlaneLocalization:1268](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1268), [PlaneLocalization:1330](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1330), [PlaneLocalization:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1555).

**Role in the proof:** The reduced-label comparison is an equality up to an explicitly obtained unit. Later product arguments use associated elements in the localized quotient ring to compare actual scalar-image submodules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the extended principal ideal

The ideal generated in \(S\) by the image of \((a)\) is exactly \((\varphi(a))\).

Indeed an image \(\varphi(ar)=\varphi(a)\varphi(r)\) belongs to this principal ideal, and \(\varphi(a)\) itself is the image of an element of \((a)\). Taking ideal closures proves both containments. This is span_map.

### Step 2. Define the forward tensor map

For \(s\in S\) and \([r]\in R/(a)\), set
\[
F(s,[r])=[s\varphi(r)].
\]
If \(r\) changes by \(at\), the value changes by
\(s\varphi(a)\varphi(t)\), which is zero in the target quotient. Thus it is well defined in \([r]\).

It is additive in both variables and is \(R\)-balanced:
\[
F(s\varphi(u),[r])
=[s\varphi(u)\varphi(r)]
=F(s,[ur]).
\]
Therefore it induces the displayed \(S\)-linear map \(\Theta_a\).

### Step 3. Define the inverse quotient map

Start with the \(S\)-linear map
\[
G:S\to S\otimes_R R/(a),\qquad G(s)=s\otimes[1].
\]
A multiple of \(\varphi(a)\) goes to zero:
\[
G(t\varphi(a))
=t\varphi(a)\otimes[1]
=t\otimes[a]=0.
\]
Hence \(G\) factors through an \(S\)-linear map
\(\overline G:S/(\varphi(a))\to S\otimes_RR/(a)\).

### Step 4. Verify both inverse identities

On a quotient class,
\[
\Theta_a\overline G([s])
=\Theta_a(s\otimes[1])=[s].
\]
On a pure tensor,
\[
\overline G\Theta_a(s\otimes[r])
=s\varphi(r)\otimes[1]
=s\otimes[r].
\]
Pure tensors generate the tensor product, so the latter equality extends to every tensor. The maps are inverse.

The source builds this equivalence from the canonical tensor/quotient equivalence and the ideal equality in Step 1. The formulas above identify its maps.

### Step 5. Specialize to a localized edge quotient

For a polynomial coefficient algebra \(A\), a plane prime \(\mathfrak p_P\) and a root label \(r_\alpha\), take \(R=A\), \(S=A_{\mathfrak p_P}\), \(a=r_\alpha\), and let \(\eta_P:A\to S\) be the localization map. The theorem becomes
\[
A_{\mathfrak p_P}\otimes_A A/(r_\alpha)
\simeq
A_{\mathfrak p_P}/(\eta_P(r_\alpha)).
\]
It sends \(s\otimes[f]\) to \([s\eta_P(f)]\). This is the coefficient compatibility between extending the edge ring and reducing the root label after localization.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar`: [MinimalExtensions.lean:1228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1228).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeScalar_tmul`: [MinimalExtensions.lean:1230](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1230).

`OAI.KLInvariance.MomentGraph.Sheaf.span_map`: [MinimalExtensions.lean:1235](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1235).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient`: [MinimalExtensions.lean:1239](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1239).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChangeQuotient_tmul`: [MinimalExtensions.lean:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1244).
