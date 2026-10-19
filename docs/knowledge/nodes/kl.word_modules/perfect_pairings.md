---
id: kl.notes.perfect_pairings
title: Perfect pairings and balanced bimodules
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses: []
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.FrobeniusDuality.PairedModule
  - OAI.KLInvariance.FrobeniusDuality.unitPairing
  - OAI.KLInvariance.FrobeniusDuality.unitModule
  - OAI.KLInvariance.FrobeniusDuality.PairedBimodule
  - OAI.KLInvariance.FrobeniusDuality.unitBimodule
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:226
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:237
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.unitPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:249
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.unitModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:295
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.PairedBimodule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:301
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.unitBimodule
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read all PairedModule and PairedBimodule fields, unitPairing inverse and
    unitBimodule. Explained dual orientation and finite freeness; kept symmetry and
    balance in the bimodule structure where the source places them.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Perfect pairings and balanced bimodules

Let \(A\) be a commutative ring and \(M\) an \(A\)-module. The linear dual
\[
M^*=\operatorname{Hom}_A(M,A)
\]
consists of the additive maps \(\lambda:M\to A\) satisfying \(\lambda(am)=a\lambda(m)\). Its addition and scalar action are defined pointwise.

A perfect pairing is an \(A\)-linear isomorphism
\[
p:M\xrightarrow{\sim}M^*,\qquad B(m,n)=p(m)(n).
\]
Linearity of \(p\) gives linearity of \(B\) in its first argument; each \(p(m)\) is a linear functional, giving linearity in its second argument. Perfection means that each functional \(\lambda\) has a unique representing vector \(m=p^{-1}(\lambda)\) with \(B(m,n)=\lambda(n)\) for every \(n\).

## The finite free paired-module structure

The source's `PairedModule` packages these fields:

| Field | Mathematical content |
|---|---|
| `carrier` | The underlying set \(M\). |
| `add` | The abelian-group operations on \(M\). |
| `module` | The left \(A\)-module action. |
| `free` | Existence of an \(A\)-basis. |
| `finite` | Finite generation over \(A\); together with freeness, a finite basis is available. |
| `pairing` | The isomorphism \(p:M\to M^*\) representing the perfect pairing. |

A finite basis \(b_1,\ldots,b_r\) gives the pairing matrix \(G_{ij}=B(b_i,b_j)\). For \(m=\sum_i x_i b_i\), the functional \(p(m)\) has values \(\sum_i x_iG_{ij}\) on the \(b_j\). Thus perfection is equivalent to invertibility of \(G\) over \(A\).

The unit paired module is \(M=A\), with \(B(a,b)=ab\). For any \(A\)-linear functional \(\lambda:A\to A\),
\[
\lambda(b)=b\lambda(1).
\]
Its representing element is \(\lambda(1)\), so evaluation at \(1\) is the inverse of the pairing map. These are `unitPairing` and `unitModule`.

For the related example \(B(a,b)=cab\), this map is multiplication by \(c\) under the same dual identification. It is perfect exactly when \(c\) is a unit.

## A right action commuting with the left action

Let \(\operatorname{End}_A(M)\) be the ring of \(A\)-linear endomorphisms of \(M\), with multiplication given by composition. A unital ring homomorphism
\[
\rho:A\longrightarrow\operatorname{End}_A(M)
\]
specifies the right action \(m\cdot a=\rho(a)m\). Since \(A\) is commutative, its images commute, and
\[
(m\cdot a)\cdot b=\rho(b)\rho(a)m=\rho(ab)m=m\cdot(ab).
\]
The \(A\)-linearity of each \(\rho(a)\) means that the two scalar actions commute:
\[
c(m\cdot a)=(cm)\cdot a.
\]

## The balanced symmetric paired-bimodule structure

The source's `PairedBimodule` has four fields:

| Field | Mathematical content |
|---|---|
| `obj` | A finite free paired \(A\)-module \((M,p)\). |
| `right` | The ring homomorphism \(\rho\) defining the commuting right action. |
| `balanced` | \(B(m\cdot a,n)=B(m,n\cdot a)\) for every \(a,m,n\). |
| `symmetric` | \(B(m,n)=B(n,m)\) for every \(m,n\). |

Balance moves a right scalar from one argument to the other. Symmetry exchanges the arguments. These are the additional pairing identities in the bimodule structure.

For the unit bimodule, both actions are ordinary multiplication on \(A\), and \(B(m,n)=mn\). Its balance identity is \((ma)n=m(na)\), and symmetry is commutativity. This gives the empty-word datum from which repeated tensor induction starts.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FrobeniusDuality.PairedModule`: [Frobenius.lean:226](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L226).

`OAI.KLInvariance.FrobeniusDuality.unitPairing`: [Frobenius.lean:237](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L237).

`OAI.KLInvariance.FrobeniusDuality.unitModule`: [Frobenius.lean:249](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L249).

`OAI.KLInvariance.FrobeniusDuality.PairedBimodule`: [Frobenius.lean:295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L295).

`OAI.KLInvariance.FrobeniusDuality.unitBimodule`: [Frobenius.lean:301](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L301).
