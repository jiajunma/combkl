---
id: kl.algebra.character_operations
title: Characters under graded equivalences, sums and shifts
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.graded_character
- kl.algebra.character_basis_independence
- kl.algebra.module_operations
- kl.detail.graded_maps_shifts
- kl.detail.coefficient_change
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.mapNonnegativeBasis
  - OAI.KLInvariance.Graded.ModuleData.character_eq_of_gradedEquiv
  - OAI.KLInvariance.Graded.ModuleData.shiftedBasis
  - OAI.KLInvariance.Graded.ModuleData.char_shift
  - OAI.KLInvariance.Graded.ModuleData.productBasis
  - OAI.KLInvariance.Graded.ModuleData.char_prod
  - OAI.KLInvariance.Graded.ModuleData.piBasis
  - OAI.KLInvariance.Graded.ModuleData.char_pi
  - OAI.KLInvariance.Graded.ModuleData.char_zero
  - OAI.KLInvariance.CoefficientChange.equiv
  - OAI.KLInvariance.CoefficientChange.kEquiv
  - OAI.KLInvariance.Graded.ModuleData.mem_changePiece
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1708
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.mapNonnegativeBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1717
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.character_eq_of_gradedEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1745
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.shiftedBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1758
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_shift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1765
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.productBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1789
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_prod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1799
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.piBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1823
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_pi
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1835
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1805
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1815
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.kEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1864
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.mem_changePiece
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read map/shift/product/pi bases and all character identities; the coefficient-transport
    consequence follows from the explicit semilinear equivalence and changePiece membership
    formula.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Characters under graded equivalences, sums and shifts

Let \(A=k[X_1,\ldots,X_N]\), with \(k\) a field and variables of degree one. For finite free nonnegatively graded \(A\)-modules,
\[
\operatorname{ch}(0;z)=0,\qquad
\operatorname{ch}(M(d);z)=z^d\operatorname{ch}(M;z)\quad(d\ge0),
\]
\[
\operatorname{ch}\left(\bigoplus_iM_i;z\right)
=\sum_i\operatorname{ch}(M_i;z)
\]
for a finite family. A degree-preserving module equivalence preserves the character.

Transporting a homogeneous basis through a grading-preserving coefficient-algebra isomorphism also preserves its basis-degree polynomial.

*Proof.*

### Step 1. Transport through a graded equivalence

Let \(e:M\to N\) be a linear bijection preserving degree. If \((b_i)\) is a homogeneous basis of \(M\), then \((e(b_i))\) is a basis of \(N\): apply \(e\) to a spanning expression, and apply \(e^{-1}\) to any linear relation.

Each \(e(b_i)\) has the same prescribed degree \(d_i\). The two basis-degree sums are therefore identical. [[node:kl.algebra.character_basis_independence|Basis independence]] identifies them with the two intrinsic characters.

### Step 2. Shift the homogeneous degrees

The shift \(M(d)\) has piece \(M_{n-d}\), so the same underlying basis vector of degree \(c_i\) now has degree \(c_i+d\). Hence
\[
\operatorname{ch}(M(d);z)
=\sum_i z^{c_i+d}
=z^d\sum_i z^{c_i}.
\]

### Step 3. Assemble a basis of a finite sum

For each \(M_i\), choose a homogeneous basis \(b_{i,j}\) with degrees \(d_{i,j}\). Insert each basis vector in its own coordinate, with zero in all others. The resulting family is a basis of the finite product: coordinatewise expansion proves spanning, and coordinatewise independence proves uniqueness.

Its degree is still \(d_{i,j}\), so
\[
\operatorname{ch}\left(\bigoplus_iM_i;z\right)
=\sum_{i,j}z^{d_{i,j}}
=\sum_i\operatorname{ch}(M_i;z).
\]
For the zero module the homogeneous basis is empty, and its sum is zero.

### Step 4. Translate a basis through a coefficient isomorphism

Let \(e:A\to A'\) be a degree-preserving \(k\)-algebra isomorphism. The transported action is \(a'\cdot m=e^{-1}(a')m\).

An old expression \(\sum_i a_ib_i\) becomes \(\sum_i e(a_i)\cdot b_i\). The bijection on coefficients transports spanning and independence, so the same vectors form an \(A'\)-basis. The transported pieces contain exactly the same underlying vectors, preserving the degrees \(d_i\). Hence the basis-degree polynomial remains \(\sum_i z^{d_i}\).

The underlying \(k\)-linear map identifies every homogeneous vector space as well, so this transport also preserves the Hilbert function.

For \(A\oplus A(2)\), shifting by one gives character \(z+z^3\); adding one further copy of \(A(2)\) gives \(1+2z^2\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.mapNonnegativeBasis`: [SheafMorphisms.lean:1708](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1708).

`OAI.KLInvariance.Graded.ModuleData.character_eq_of_gradedEquiv`: [SheafMorphisms.lean:1717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1717).

`OAI.KLInvariance.Graded.ModuleData.shiftedBasis`: [SheafMorphisms.lean:1745](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1745).

`OAI.KLInvariance.Graded.ModuleData.char_shift`: [SheafMorphisms.lean:1758](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1758).

`OAI.KLInvariance.Graded.ModuleData.productBasis`: [SheafMorphisms.lean:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1765).

`OAI.KLInvariance.Graded.ModuleData.char_prod`: [SheafMorphisms.lean:1789](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1789).

`OAI.KLInvariance.Graded.ModuleData.piBasis`: [SheafMorphisms.lean:1799](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1799).

`OAI.KLInvariance.Graded.ModuleData.char_pi`: [SheafMorphisms.lean:1823](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1823).

`OAI.KLInvariance.Graded.ModuleData.char_zero`: [SheafMorphisms.lean:1835](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1835).

`OAI.KLInvariance.CoefficientChange.equiv`: [BottSamelson.lean:1805](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1805).

`OAI.KLInvariance.CoefficientChange.kEquiv`: [BottSamelson.lean:1815](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1815).

`OAI.KLInvariance.Graded.ModuleData.mem_changePiece`: [BottSamelson.lean:1864](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1864).
