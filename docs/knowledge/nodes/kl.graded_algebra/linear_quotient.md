---
id: kl.detail.linear_quotient
title: Symmetric-algebra quotients by linear ideals
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.SymmetricPlaneIdeal.ideal_le_ker
  - OAI.KLInvariance.SymmetricPlaneIdeal.forward
  - OAI.KLInvariance.SymmetricPlaneIdeal.linearQuotient
  - OAI.KLInvariance.SymmetricPlaneIdeal.backward
  - OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv
  - OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv_mk_ι
  - OAI.KLInvariance.SymmetricPlaneIdeal.ι_mem_iff
  - OAI.KLInvariance.SymmetricPlaneIdeal.ideal_eq_ker
  - OAI.KLInvariance.SymmetricPlaneIdeal.ideal_isPrime
  - OAI.KLInvariance.SymmetricPlaneIdeal.ideal_span_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:27
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.ideal_le_ker
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:33
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.forward
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:37
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.linearQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:44
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.backward
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:56
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:76
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv_mk_ι
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:80
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.ι_mem_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:98
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.ideal_eq_ker
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:107
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.ideal_isPrime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:111
    format: lean-location
    note: OAI.KLInvariance.SymmetricPlaneIdeal.ideal_span_eq
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read quotientEquiv and both inverse identities, the functional argument
    for degree-one membership, primality and ideal_span_eq. Kept the theorem generic
    and separated localization from this algebraic quotient.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Symmetric-algebra quotients by linear ideals

Let \(V\) be a vector space over a field \(k\), let \(P\subseteq V\), and let \(I_P\) be its linear ideal in \(A=\operatorname{Sym}_k(V)\). Then
\[
A/I_P\simeq\operatorname{Sym}_k(V/P).
\]
The ideal \(I_P\) is prime, and
\[
\iota(v)\in I_P\quad\Longleftrightarrow\quad v\in P.
\]

*Proof.*

### Step 1. Construct the forward map

The map \(Q_P:A\to\operatorname{Sym}_k(V/P)\) sends \(\iota(v)\) to \(\iota([v])\). If \(v\in P\), then \([v]=0\), so this generator maps to zero.

The kernel of \(Q_P\) is an ideal containing all the generators of \(I_P\), hence contains \(I_P\). Therefore
\[
F:A/I_P\to\operatorname{Sym}_k(V/P),\qquad [z]\mapsto Q_P(z)
\]
is a well-defined algebra map.

### Step 2. Construct the inverse map on vector generators

The linear map \(v\mapsto[\iota(v)]\in A/I_P\) vanishes on \(P\). It therefore descends to
\[
V/P\longrightarrow A/I_P,\qquad [v]\longmapsto[\iota(v)].
\]
The symmetric-algebra universal property extends it to an algebra map
\(G:\operatorname{Sym}_k(V/P)\to A/I_P\).

### Step 3. Verify both composites

On a generator \(\iota([v])\) of \(\operatorname{Sym}_k(V/P)\),
\[
FG(\iota([v]))=F([\iota(v)])=\iota([v]).
\]
On a generator class of \(A/I_P\),
\[
GF([\iota(v)])=G(\iota([v]))=[\iota(v)].
\]
Every element of a symmetric algebra is a polynomial in its vector generators, and every quotient element has a representative in \(A\). Thus the two algebra-map identities on generators prove \(FG=1\) and \(GF=1\).

This also proves \(I_P=\ker Q_P\): if \(Q_P(z)=0\), then \(F([z])=0\), so the injective map \(F\) gives \([z]=0\).

### Step 4. Detect membership of a linear generator

If \(v\in P\), then \(\iota(v)\) is an ideal generator.

Conversely, \(\iota(v)\in I_P\) implies \(\iota([v])=0\) in \(\operatorname{Sym}(V/P)\). If \([v]\ne0\), extend this nonzero vector to a basis and choose a linear functional \(\lambda:V/P\to k\) with \(\lambda([v])\ne0\).

Its extension to the symmetric algebra sends \(\iota([v])\) to the nonzero scalar \(\lambda([v])\), a contradiction. Hence \([v]=0\), which means \(v\in P\).

### Step 5. Prove primality

Choose a basis of \(V/P\). Its symmetric algebra is a polynomial algebra over the field \(k\), and therefore a domain. The isomorphism from Steps 1–3 makes \(A/I_P\) a domain. This is exactly the primality of \(I_P\).

### Step 6. Reduce the generating set

If \(P\) is spanned by a set \(S\), then
\[
I_P=(\iota(s):s\in S).
\]
One containment follows from \(S\subseteq P\). For the other, every \(v\in P\) is a finite linear combination of elements of \(S\); linearity of \(\iota\) expresses \(\iota(v)\) in the ideal on the right. This is the source's ideal_span_eq statement.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SymmetricPlaneIdeal.ideal_le_ker`: [PlaneLocalization.lean:27](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L27).

`OAI.KLInvariance.SymmetricPlaneIdeal.forward`: [PlaneLocalization.lean:33](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L33).

`OAI.KLInvariance.SymmetricPlaneIdeal.linearQuotient`: [PlaneLocalization.lean:37](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L37).

`OAI.KLInvariance.SymmetricPlaneIdeal.backward`: [PlaneLocalization.lean:44](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L44).

`OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv`: [PlaneLocalization.lean:56](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L56).

`OAI.KLInvariance.SymmetricPlaneIdeal.quotientEquiv_mk_ι`: [PlaneLocalization.lean:76](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L76).

`OAI.KLInvariance.SymmetricPlaneIdeal.ι_mem_iff`: [PlaneLocalization.lean:80](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L80).

`OAI.KLInvariance.SymmetricPlaneIdeal.ideal_eq_ker`: [PlaneLocalization.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L98).

`OAI.KLInvariance.SymmetricPlaneIdeal.ideal_isPrime`: [PlaneLocalization.lean:107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L107).

`OAI.KLInvariance.SymmetricPlaneIdeal.ideal_span_eq`: [PlaneLocalization.lean:111](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L111).
