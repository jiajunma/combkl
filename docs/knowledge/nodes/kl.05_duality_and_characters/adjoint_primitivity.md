---
id: kl.detail.adjoint_primitivity
title: Primitivity is preserved by the adjoint operation
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.integral_adjoints
- kl.detail.primitive_projectors
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  - BalancedPairings
  declarations:
  - OAI.PerfectAdjoint.adjoint_comp
  - OAI.PerfectAdjoint.adjoint_adjoint
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_of_antiInvolution
  - OAI.KLInvariance.TitsSpace.bottAdjointSheaf_primitive
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2228
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_comp
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2257
    format: lean-location
    note: OAI.PerfectAdjoint.adjoint_adjoint
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1652
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_of_antiInvolution
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1736
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointSheaf_primitive
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Primitivity is preserved by the adjoint operation

An involutive operation \(a\) on sheaf endomorphisms that reverses composition and sends zero to zero preserves primitive projectors. For a reduced word in the finite-generator real realization, the constructed integral word-sheaf adjoint is such an operation, so it preserves primitive projectors.

*Proof.*

### Step 1. Check the algebraic adjoint identities

For a perfect pairing, evaluate against an arbitrary vector \(n\):
\[
\langle(fg)^*m,n\rangle=\langle m,fgn\rangle
=\langle f^*m,gn\rangle=\langle g^*f^*m,n\rangle.
\]
Injectivity of the pairing map gives \((fg)^*=g^*f^*\). For a symmetric pairing,
\(\langle(f^*)^*m,n\rangle=\langle m,f^*n\rangle=\langle fm,n\rangle\), hence \((f^*)^*=f\). The same defining identity gives \(0^*=0\).

The word-sheaf adjoint is the descended integral module adjoint; its stalk and edge maps satisfy these identities. The descent uses the balance and support construction in the boundary-pairing proof. The following argument needs exactly these three identities.

### Step 2. Check that the new projector is idempotent

Let \(p\) be primitive. Then
\[
a(p)a(p)=a(pp)=a(p).
\]
Thus \(a(p)\) is a projector.

### Step 3. Pull a proposed subprojector back through the involution

Suppose \(f^2=f\), \(fa(p)=f\), and \(a(p)f=f\). Applying \(a\) and reversing the products gives
\[
a(f)^2=a(f),\qquad pa(f)=a(f),\qquad a(f)p=a(f).
\]
Primitivity of \(p\) therefore gives \(a(f)=0\) or \(a(f)=p\).

### Step 4. Return to the original subprojector

Apply \(a\) again. Involutivity and preservation of zero give respectively \(f=0\) or \(f=a(p)\). This is precisely the defining condition for primitivity of \(a(p)\).

For the actual word sheaf, substitute the proved adjoint operation. The argument concerns an endomorphism and its adjoint; it does not assume that restricting a perfect form to an arbitrary summand is perfect.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.PerfectAdjoint.adjoint_comp`: [IntegralPairings.lean:2228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2228).

`OAI.PerfectAdjoint.adjoint_adjoint`: [IntegralPairings.lean:2257](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2257).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_of_antiInvolution`: [BalancedPairings.lean:1652](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1652).

`OAI.KLInvariance.TitsSpace.bottAdjointSheaf_primitive`: [BalancedPairings.lean:1736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1736).
