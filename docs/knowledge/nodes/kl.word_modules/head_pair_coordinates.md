---
id: kl.word.head_pair_coordinates
title: The reflected two-stalk coordinates of a longer word
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.twisted_pair_lattice
- kl.word.edge_annihilation
- kl.word.evaluation_maps
- kl.notes.word_stalks
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottWeight_tail_zero
  - OAI.KLInvariance.TitsSpace.bottWeight_tail_one
  - OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates
  - OAI.KLInvariance.TitsSpace.simpleReverseDivisibility
  - OAI.KLInvariance.TitsSpace.bottHeadPairLattice
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:99
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_tail_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:105
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_tail_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:112
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:156
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleReverseDivisibility
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:162
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairLattice
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the tail-weight identities, twisted coordinate map and actual lattice
    instantiation. Explained why the second block applies tau and how its scalar twist
    restores A-linearity.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The reflected two-stalk coordinates of a longer word

Fix a finite-generator Coxeter system, a word \(\mathbf t\), a simple reflection \(s\), and a group element \(x\). Let \(\tau=\chi_s\) on the symmetric coefficient algebra \(A\), and write \(\alpha=\alpha_s\).

Use the two tail stalks
\[
X=M_{\mathbf t}^x,\qquad Y=M_{\mathbf t}^{sx},
\qquad f=\pi_x,\quad g=\pi_{sx}.
\]
The reflected pair lattice is
\[
L_x=\{(f(n),g(n)):n\in M_{\mathbf t}\}
\subseteq X\oplus{}^\tau Y,
\]
with action \(a\cdot(p,q)=(ap,\tau(a)q)\).

The source's `bottHeadPairLattice` instantiates the general twisted pair lattice. Its two hypotheses come from
\[
\alpha\mid\tau(a)-a
\]
and the [[node:kl.word.edge_annihilation|reflection-label annihilation theorem]], which supplies a common preimage for every pair \((0,\alpha q)\).

## Splitting the new weight block by its first bit

A subexpression \((0,\eta)\) of \(s\mathbf t\) has weight \(x\) exactly when the tail weight is \(x\). A subexpression \((1,\eta)\) has weight \(x\) exactly when the tail weight is \(sx\), because
\[
s\,w_{\mathbf t}(\eta)=x
\quad\Longleftrightarrow\quad
w_{\mathbf t}(\eta)=sx.
\]
Thus the coordinate set for the new \(x\)-stalk splits into a zero-bit copy of \(J_x\) and a one-bit copy of \(J_{sx}\) for the tail.

## The coordinate map

For \((p,q)\in X\oplus{}^\tau Y\), define
\[
C_x(p,q)_{(0,\eta)}=p_\eta,\qquad
C_x(p,q)_{(1,\eta)}=\tau(q_\eta).
\]
Its target is the full coordinate module for the new \(x\)-weight block. This is `bottHeadPairCoordinates`.

The scalar twist makes \(C_x\) \(A\)-linear. On the second block,
\[
\tau((a\cdot q)_\eta)
=\tau(\tau(a)q_\eta)
=a\,\tau(q_\eta),
\]
while the first block has ordinary scalar linearity.

For a pair with common preimage \(n\),
\[
C_x(f(n),g(n))
=E_{s\mathbf t,x}(1\otimes n).
\]
This equality follows directly from the two evaluation formulas. The [[node:kl.word.head_pair_equivalence|head-pair equivalence theorem]] proves that restricting \(C_x\) to \(L_x\) gives exactly the new image stalk.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottWeight_tail_zero`: [BottSamelson.lean:99](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L99).

`OAI.KLInvariance.TitsSpace.bottWeight_tail_one`: [BottSamelson.lean:105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L105).

`OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates`: [BottSamelson.lean:112](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L112).

`OAI.KLInvariance.TitsSpace.simpleReverseDivisibility`: [BottSamelson.lean:156](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L156).

`OAI.KLInvariance.TitsSpace.bottHeadPairLattice`: [BottSamelson.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L162).
