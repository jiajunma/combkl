---
id: kl.algebra.coefficient_duals
title: Coefficient transport of dual modules and perfect pairings
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.coefficient_change
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.CoefficientChange.mapEquiv
  - OAI.KLInvariance.CoefficientChange.dualTo
  - OAI.KLInvariance.CoefficientChange.dualFrom
  - OAI.KLInvariance.CoefficientChange.dualEquiv
  - OAI.KLInvariance.CoefficientChange.pairingEquiv
  - OAI.KLInvariance.CoefficientChange.pairingEquiv_apply
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1771
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.mapEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1778
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.dualTo
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1787
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.dualFrom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1802
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.dualEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1824
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.pairingEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1829
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.pairingEquiv_apply
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read dualTo, dualFrom, dualEquiv, mapEquiv and pairingEquiv. Verified both
    scalar directions, inverses, linearity on the dual space and the evaluation formula;
    grading consequences follow from the exact transported pieces.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Coefficient transport of dual modules and perfect pairings

Let \(k\) be a field, \(e:A\xrightarrow{\sim}B\) an isomorphism of commutative \(k\)-algebras, and \(M\) an \(A\)-module with compatible \(k\)-scalar action. Write \({}^eM\) for coefficient transport, with \(b\star m=e^{-1}(b)m\).

The dual module is \(\operatorname{Hom}_A(M,A)\). There is a \(B\)-linear isomorphism
\[
{}^e\operatorname{Hom}_A(M,A)
\xrightarrow{\sim}\operatorname{Hom}_B({}^eM,B),
\]
sending \(\lambda\) to the functional
\[
\lambda^e(m)=e(\lambda(m)).
\]

A perfect pairing represented by an \(A\)-linear isomorphism \(D:M\to\operatorname{Hom}_A(M,A)\) transports to a perfect pairing with value
\[
D^e(m,n)=e(D(m,n)).
\]

*Proof.*

### Step 1. Check the forward functional

For \(b\in B\),
\[
\lambda^e(b\star m)
=e(\lambda(e^{-1}(b)m))
=e(e^{-1}(b)\lambda(m))
=b\,e(\lambda(m)).
\]
Additivity follows from additivity of \(\lambda\) and \(e\). Thus \(\lambda^e\) is \(B\)-linear.

### Step 2. Construct the inverse functional

For a \(B\)-linear functional \(\mu:{}^eM\to B\), set
\[
\lambda(m)=e^{-1}(\mu(m)).
\]
Old multiplication by \(a\in A\) is new multiplication by \(e(a)\). Hence
\[
\lambda(am)
=e^{-1}(e(a)\mu(m))
=a\,e^{-1}(\mu(m)),
\]
so \(\lambda\) is \(A\)-linear.

The composites are identities because \(e^{-1}e=1_A\) and \(ee^{-1}=1_B\).

### Step 3. Verify linearity on the dual modules

The transported scalar action on the old dual is
\(b\star\lambda=e^{-1}(b)\lambda\).
Evaluating its forward image at \(m\) gives
\[
e(e^{-1}(b)\lambda(m))=b\,e(\lambda(m)).
\]
Thus the forward functional correspondence is itself \(B\)-linear. Together with Step 2 it is the stated linear isomorphism.

### Step 4. Transport the pairing isomorphism

Coefficient transport sends the given isomorphism \(D\) to an isomorphism
\[
{}^eM\longrightarrow{}^e\operatorname{Hom}_A(M,A).
\]
On underlying vectors this is the original \(D\), and its inverse is the transported original inverse.

Compose it with the dual isomorphism from Steps 1–3. The result is a \(B\)-linear isomorphism from \({}^eM\) to its \(B\)-dual, hence a perfect pairing. Evaluating that composite gives \(D^e(m,n)=e(D(m,n))\).

### Step 5. Preserve the relevant degree and symmetry identities

If \(e(A_j)=B_j\) and the module grading is transported, a homogeneous functional of degree \(r\) still sends degree \(n\) into degree \(n+r\).

Likewise, if the old pairing sends degrees \(i,j\) into \(A_{i+j-L}\), the new value lies in \(B_{i+j-L}\), preserving its shift \(L\). Applying \(e\) to a symmetry equation preserves symmetry.

This is the coefficient-level functional calculation used when symmetric coefficient rings are replaced by polynomial coordinates.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CoefficientChange.mapEquiv`: [Support.lean:1771](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1771).

`OAI.KLInvariance.CoefficientChange.dualTo`: [Support.lean:1778](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1778).

`OAI.KLInvariance.CoefficientChange.dualFrom`: [Support.lean:1787](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1787).

`OAI.KLInvariance.CoefficientChange.dualEquiv`: [Support.lean:1802](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1802).

`OAI.KLInvariance.CoefficientChange.pairingEquiv`: [Support.lean:1824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1824).

`OAI.KLInvariance.CoefficientChange.pairingEquiv_apply`: [Support.lean:1829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1829).
