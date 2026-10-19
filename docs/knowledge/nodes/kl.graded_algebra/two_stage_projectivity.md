---
id: kl.algebra.two_stage_projectivity
title: Projectivity through two successive kernel sequences
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.projective_range_splittings
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.ProjectiveRange.onKernel
  - OAI.KLInvariance.ProjectiveRange.kernelOnKernelEquiv
  - OAI.KLInvariance.ProjectiveRange.projective_of_two_stage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1337
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.onKernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1340
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.kernelOnKernelEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1349
    format: lean-location
    note: OAI.KLInvariance.ProjectiveRange.projective_of_two_stage
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read onKernel, the underlying-vector kernel equivalence and both uses of
    projective_of_kernel. Stated every map, kernel and surjectivity hypothesis explicitly.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Projectivity through two successive kernel sequences

Let \(R\) be a commutative ring and let
\[
r:M\to H,\qquad f:M\to P,\qquad k:P\to S
\]
be linear maps. Assume
\[
r(m)=0\Longrightarrow k(f(m))=0.
\]
Then \(f\) induces a map
\[
\bar f:\ker r\to\ker k,\qquad m\mapsto f(m).
\]
Put \(D=\ker r\cap\ker f\), a submodule of \(M\).

If \(r\) and \(\bar f\) are surjective and the modules \(H,\ker k,D\) are projective, then \(M\) is projective.

*Proof.*

### Step 1. Define the map on the first kernel

For \(m\in\ker r\), the given implication places \(f(m)\) in \(\ker k\), so \(\bar f\) is well defined. Addition and scalar multiplication are inherited from \(f\). This is the source's onKernel map.

### Step 2. Identify its kernel

An element in \(\ker\bar f\) consists of \(m\in M\) with
\[
r(m)=0,\qquad f(m)=0.
\]
These are exactly the conditions for \(m\in D\). Keeping the underlying vector gives a linear isomorphism
\[
D\xrightarrow{\sim}\ker\bar f.
\]
Its inverse also keeps the underlying vector, now recording the two kernel conditions separately. The source calls it kernelOnKernelEquiv.

### Step 3. Split the inner sequence

Surjectivity of \(\bar f\) gives
\[
0\longrightarrow D\longrightarrow\ker r
\xrightarrow{\bar f}\ker k\longrightarrow0.
\]
Because \(\ker k\) is projective, the surjection has a linear section. The [[node:kl.algebra.projective_range_splittings|split-sequence theorem]] gives
\(\ker r\simeq D\oplus\ker k\).
Both summands are projective by assumption, so \(\ker r\) is projective.

### Step 4. Split the outer sequence

Surjectivity of \(r\) gives
\[
0\longrightarrow\ker r\longrightarrow M\xrightarrow{r}H\longrightarrow0.
\]
Projectivity of \(H\) gives a section. The [[node:kl.algebra.projective_range_splittings|splitting theorem]] now gives
\(M\simeq\ker r\oplus H\).
Step 3 proves the first summand projective, and \(H\) is projective by assumption. Thus \(M\) is projective.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ProjectiveRange.onKernel`: [IntegralPairings.lean:1337](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1337).

`OAI.KLInvariance.ProjectiveRange.kernelOnKernelEquiv`: [IntegralPairings.lean:1340](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1340).

`OAI.KLInvariance.ProjectiveRange.projective_of_two_stage`: [IntegralPairings.lean:1349](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1349).
