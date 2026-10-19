---
id: kl.algebra.root_quotient_coordinates
title: Polynomial coordinates on an edge coefficient ring
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.linear_ideals
- kl.detail.linear_quotient
- kl.algebra.linear_primes
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial
  - OAI.KLInvariance.EdgeAlgebra.linear_homogeneous
  - OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous
  - OAI.KLInvariance.TitsSpace.EdgeCoefficient
  - OAI.KLInvariance.TitsSpace.edgePolynomial
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:824
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:845
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:871
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:861
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.linear_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:875
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:930
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.EdgeCoefficient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:950
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgePolynomial
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read rootQuotientEquiv, its generator formula, rootQuotientPolynomial and
    reduced-root homogeneity, plus the actual EdgeCoefficient/edgePolynomial definitions.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Polynomial coordinates on an edge coefficient ring

Let \(V\) be a vector space over a field \(k\). For a vector \(a\in V\), choose a basis \((e_j)\) of \(V/ka\). The source constructs
\[
\operatorname{Sym}_k(V)/(\iota(a))
\simeq\operatorname{Sym}_k(V/ka)
\simeq k[X_j].
\]
The class of another linear generator \(\iota(v)\) becomes the linear polynomial with the coordinates of \([v]\) in that basis.

For a nonzero root in the finite-dimensional real extended realization, this is the polynomial presentation of its edge coefficient ring.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Canonical labels for the same principal ideals.**

**OpenAI notes:** The coefficient discussion uses degree-one linear root labels and permits any nonzero real scalar multiple, because only the principal ideal matters. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The label is the coordinate polynomial of the embedded canonical positive root for the reflection. Its primality and quotient are proved for that actual element. [SheafMorphisms:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L144), [Support:1065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1065), [ReflectionSchedules:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L824).

**Role in the proof:** Multiplying a label by a nonzero field scalar leaves its principal ideal unchanged. The fixed label used by the code therefore presents the same scalar quotient described in the notes.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the root-line quotient isomorphism

The generic [[node:kl.detail.linear_quotient|linear-quotient theorem]] at \(P=ka\) gives the first isomorphism. Its formula on generators is
\[
[\iota(v)]\longmapsto\iota_{V/ka}([v]).
\]

### Step 2. Use the chosen quotient-space basis

The symmetric-algebra coordinate isomorphism sends
\(\iota_{V/ka}(e_j)\) to \(X_j\). If
\([v]=\sum_j c_je_j\),
linearity gives
\[
[\iota(v)]\longmapsto\sum_j c_jX_j.
\]
Composing the two algebra isomorphisms is the source's rootQuotientPolynomial.

### Step 3. Check degree and nonvanishing

Every \(X_j\) has degree one, so the displayed polynomial is homogeneous of degree one. It is nonzero exactly when at least one \(c_j\) is nonzero, equivalently when \([v]\ne0\), or \(v\notin ka\).

The [[node:kl.algebra.linear_primes|linear-prime theorem]] then also proves primality of every surviving reduced linear generator.

### Step 4. Specialize to an actual root label

Let \(V\) be the real extended realization and embed a positive root \(a\) from the original root space. The source defines EdgeCoefficient as the symmetric algebra modulo that embedded root's ideal.

It chooses a finite basis of the quotient space and composes the two isomorphisms above, producing edgePolynomial. If \(\dim V=N\) and \(a\ne0\), the quotient space has dimension \(N-1\), so the edge ring has \(N-1\) polynomial variables. Finite-variable polynomial rings over a field are Noetherian unique factorization domains; these coordinates supply those coefficient-ring hypotheses in the local membership argument.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv`: [ReflectionSchedules.lean:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L824).

`OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι`: [ReflectionSchedules.lean:845](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L845).

`OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial`: [ReflectionSchedules.lean:871](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L871).

`OAI.KLInvariance.EdgeAlgebra.linear_homogeneous`: [ReflectionSchedules.lean:861](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L861).

`OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous`: [ReflectionSchedules.lean:875](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L875).

`OAI.KLInvariance.TitsSpace.EdgeCoefficient`: [ReflectionSchedules.lean:930](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L930).

`OAI.KLInvariance.TitsSpace.edgePolynomial`: [ReflectionSchedules.lean:950](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L950).
