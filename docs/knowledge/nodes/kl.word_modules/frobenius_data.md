---
id: kl.word.frobenius_data
title: Frobenius traces and trace duality
kind: definition
status: formalized
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
  - OAI.KLInvariance.FrobeniusDuality.restrictPairing
  - OAI.KLInvariance.FrobeniusDuality.inducedModule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:180
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.restrictPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:270
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedModule
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the trace/duality/compatibility parameters and the separate finite-free
    hypotheses in FrobeniusDuality. Defined the actual parameter interface with an
    arbitrary algebra map and an explicit trace representative.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Frobenius traces and trace duality

Let \(R,A\) be commutative rings and let \(\eta:R\to A\) give \(A\) its \(R\)-algebra structure. An \(R\)-linear trace is a map
\[
t:A\to R,\qquad t(a+b)=t(a)+t(b),\qquad t(\eta(r)a)=r\,t(a).
\]
Its associated trace pairing is the \(R\)-bilinear map
\[
A\times A\longrightarrow R,\qquad (a,b)\longmapsto t(ab).
\]
The word “trace” here names this chosen linear map. Its normalization is part of the data.

Trace-duality data consist of this trace and an \(R\)-linear isomorphism
\[
D:A\xrightarrow{\sim}\operatorname{Hom}_R(A,R)
\quad\text{with}\quad D(a)(b)=t(ab).
\]
Thus, for each \(R\)-linear functional \(\lambda:A\to R\), there is exactly one \(c\in A\) such that
\[
\lambda(b)=t(cb)\qquad\text{for every }b\in A.
\]
This representative is \(D^{-1}(\lambda)\). Commutativity gives symmetry \(t(ab)=t(ba)\) and the identity
\[
D(ca)(b)=D(a)(cb).
\]

## The finite free extension used in tensor induction

A finite free Frobenius extension in this development is an algebra map \(\eta:R\to A\) with:

1. a finite \(R\)-basis of \(A\);
2. an \(R\)-linear trace \(t\);
3. the perfect trace pairing \(D\) above.

The source passes these as parameters: `tr` is \(t\), `d` is \(D\), and `hd` is the formula \(D(a)(b)=t(ab)\). The typeclass hypotheses `Module.Free R A` and `Module.Finite R A` supply the finite free module. The next construction combines this data with a finite free paired \(A\)-module.

Restriction of a perfect pairing through the trace uses the trace-duality data alone. Finite freeness supplies a finite basis when the construction subsequently extends scalars by \(A\otimes_R-\).

## The reflection example

For \(A=k[X]\), where \(k\) is a characteristic-zero field, take \(R=k[X^2]\), with its inclusion into \(A\). Write
\[
f=f_0(X^2)+Xf_1(X^2),\qquad t(f)=f_1(X^2).
\]
The \(R\)-basis is \(1,X\). If \(\lambda:A\to R\) is \(R\)-linear, its trace representative is
\[
c=\lambda(X)+X\lambda(1).
\]
Indeed,
\[
t\bigl(c(b_0+Xb_1)\bigr)
=\lambda(X)b_1+\lambda(1)b_0
=\lambda(b_0+Xb_1).
\]
Testing against \(1\) and \(X\) proves uniqueness. This computation is the model for the general [[node:kl.notes.reflection_frobenius|reflection Frobenius theorem]].

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.restrictPairing`: [Frobenius.lean:180](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L180).

`OAI.KLInvariance.FrobeniusDuality.inducedModule`: [Frobenius.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L270).
