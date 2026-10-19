---
id: kl.word.tensor_dual_base_change
title: Extending a finite free dual and pairing by tensor product
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.extendPairing
  - OAI.KLInvariance.FrobeniusDuality.extendPairing_tmul
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:196
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.extendPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:201
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.extendPairing_tmul
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the extendPairing composite and tmul proof. Expanded the canonical
    dual base-change isomorphism by finite basis and coordinate inverse, preserving
    the arbitrary algebra map and first-argument pairing convention.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Extending a finite free dual and pairing by tensor product

Let \(\eta:R\to A\) be an algebra map between commutative rings, and let \(M\) be a finite free \(R\)-module. Write \(M^*=\operatorname{Hom}_R(M,R)\). There is a canonical \(A\)-linear isomorphism
\[
Q:A\otimes_R M^*\xrightarrow{\sim}
 \operatorname{Hom}_A(A\otimes_R M,A),
\]
defined by
\[
Q(a\otimes\lambda)(b\otimes m)=ab\,\eta(\lambda(m)).
\]
If \(p:M\xrightarrow{\sim}M^*\) is a perfect pairing, the composite
\[
A\otimes_R M\xrightarrow{\,1\otimes p\,}
A\otimes_R M^*\xrightarrow{\,Q\,}
\operatorname{Hom}_A(A\otimes_R M,A)
\]
is a perfect pairing, and
\[
B_A(a\otimes m,b\otimes n)=ab\,\eta(p(m)(n)).
\]

*Proof.*

### Step 1. Verify the tensor relations

The tensor product \(A\otimes_R M\) is generated additively by symbols \(a\otimes m\), subject to additivity in each factor and
\[
a\eta(r)\otimes m=a\otimes rm.
\]
For the proposed evaluation formula,
\[
ab\eta(\lambda(rm))
=ab\eta(r\lambda(m))
=a\eta(r)b\eta(\lambda(m)).
\]
Thus moving \(r\) between \(b\) and \(m\) preserves the value. Moving \(r\) between \(a\) and \(\lambda\) does too, since
\((r\lambda)(m)=r\lambda(m)\).
Additivity is inherited from multiplication, \(\eta\) and \(\lambda\). The formula therefore defines a linear map on each tensor product, with the target functional \(A\)-linear in its argument.

### Step 2. Construct a basis after scalar extension

Choose a finite \(R\)-basis \(e_1,\ldots,e_r\) of \(M\), with coordinate functionals \(e_i^*\), so \(e_i^*(e_j)=\delta_{ij}\).

Every tensor has an expansion in \(u_i=1\otimes e_i\): if \(m=\sum_i m_i e_i\), then
\[
a\otimes m=\sum_i a\eta(m_i)u_i.
\]
The coordinate maps \(a\otimes m\mapsto a\eta(e_i^*(m))\) are well defined by the tensor relations and take \(u_j\) to \(\delta_{ij}\). They prove linear independence. Thus \(u_1,\ldots,u_r\) is an \(A\)-basis.

Every functional on \(M\) has the finite expansion
\(\lambda=\sum_i\lambda(e_i)e_i^*\). The same argument shows that
\(1\otimes e_i^*\) form an \(A\)-basis of \(A\otimes_R M^*\).

### Step 3. Invert the dual base-change map

The formula for \(Q\) gives
\[
Q(1\otimes e_i^*)(u_j)=\eta(\delta_{ij})=\delta_{ij}.
\]
Thus these basis vectors map to the coordinate functionals of the basis \((u_j)\). Explicitly, for
\(F\in\operatorname{Hom}_A(A\otimes_R M,A)\), define
\[
Q^{-1}(F)=\sum_i F(u_i)(1\otimes e_i^*).
\]
Evaluating \(Q(Q^{-1}(F))\) at each \(u_j\) gives \(F(u_j)\), so the composite equals \(F\). Evaluating on the basis \(1\otimes e_i^*\) proves the other composite is the identity. This proves that \(Q\) is an isomorphism.

### Step 4. Extend the original pairing

The map \(1\otimes p\) sends \(a\otimes m\) to \(a\otimes p(m)\). Its inverse is \(1\otimes p^{-1}\), as both composite identities can be checked on the generating pure tensors.

Composing with \(Q\) therefore yields a perfect pairing. Substitution into its defining evaluation gives
\[
Q(a\otimes p(m))(b\otimes n)=ab\eta(p(m)(n)),
\]
the asserted formula.

The local source defines extendPairing as exactly this composite, using its dual base-change isomorphism, and proves extendPairing_tmul by evaluation and scalar linearity. The basis calculation above makes that finite free isomorphism explicit.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.extendPairing`: [Frobenius.lean:196](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L196).

`OAI.KLInvariance.FrobeniusDuality.extendPairing_tmul`: [Frobenius.lean:201](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L201).
