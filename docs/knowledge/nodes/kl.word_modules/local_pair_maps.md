---
id: kl.word.local_pair_maps
title: Tail pairs recover word-stalk projections and their divisibility
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.tail_maps
- kl.word.head_pair_equivalence
- kl.word.evaluation_maps
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottTensor_maps_eq
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_coordinates
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_mem
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_zero_iff
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_value
  - OAI.KLInvariance.TitsSpace.bottHeadLocalPair_toStalk
  - OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible_of_pair
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:70
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensor_maps_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:820
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:828
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:836
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_zero_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:853
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_value
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:859
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLocalPair_toStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:866
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible_of_pair
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the seed-to-linear-map identity, injective-coordinate membership lemma,
    zero equivalence and divisible-pair descent. Explained the membership recovery
    before treating P_x(m) as a lattice vector.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Tail pairs recover word-stalk projections and their divisibility

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), a simple reflection \(s\), a tail word \(\mathbf t\), and a weight \(x\). Let
\[
P_x:M_{s\mathbf t}\to
M_{\mathbf t}^x\oplus{}^\tau M_{\mathbf t}^{sx}
\]
be the local pair of the ordinary and reflected tail maps, where \(\tau=\chi_s\). Denote the ordinary tail map by \(\mu\) and the reflected tail map by \(\nu\). Let \(L_x\) be the reflected pair lattice and
\(C_x:L_x\xrightarrow{\sim}M_{s\mathbf t}^x\) its coordinate isomorphism.

Every \(P_x(m)\) lies in \(L_x\), and
\[
C_x(P_x(m))=\pi_x^{s\mathbf t}(m).
\]
Moreover,
\[
\pi_x^{s\mathbf t}(m)=0
\quad\Longleftrightarrow\quad
\pi_x^{\mathbf t}(\mu(m))=0
\quad\text{and}\quad
\pi_{sx}^{\mathbf t}(\nu(m))=0.
\]
If \(P_x(m)=\beta p\) with \(p\in L_x\), then
\(\pi_x^{s\mathbf t}(m)=\beta C_x(p)\).

*Proof.*

### Step 1. Check the coordinate identity on tensor generators

First regard the coordinate map \(C_x\) as defined on the whole pair module, with values in the ambient new weight-coordinate module. Both \(C_xP_x\) and the new weight projection \(E_x\) are \(A\)-linear.

On a tensor \(1\otimes n\), the tail formulas give
\(P_x(1\otimes n)=(\pi_x(n),\pi_{sx}(n))\).
The head-coordinate formula then gives
\[
C_xP_x(1\otimes n)=E_x(1\otimes n).
\]
For \(a\otimes n=a(1\otimes n)\), linearity gives the same equality after multiplication by \(a\). Every tensor is a finite sum of pure tensors, so \(C_xP_x=E_x\) on the entire word module.

### Step 2. Recover lattice membership from coordinates

The head-pair equivalence says that every vector in the image stalk has coordinates \(C_x(p)\) for some \(p\in L_x\). Apply this to \(E_x(m)\), choosing \(p\in L_x\) with
\(C_x(p)=E_x(m)\).

Step 1 gives \(C_x(p)=C_x(P_x(m))\). The ambient coordinate map is injective, so \(p=P_x(m)\). Thus \(P_x(m)\in L_x\). Restricting the coordinate identity to the image stalk gives
\(C_x(P_x(m))=\pi_x^{s\mathbf t}(m)\).

### Step 3. Recover the two vanishing conditions

Since \(C_x\) is injective and linear,
\[
C_x(P_x(m))=0\quad\Longleftrightarrow\quad P_x(m)=0.
\]
A vector in a product module is zero exactly when both its components are zero. Substituting the definition of \(P_x\) gives the stated equivalence. The second zero is the zero of the underlying tail stalk; the twist preserves zero.

### Step 4. Descend a divisible lattice pair

Suppose \(P_x(m)=\beta p\) with \(p\in L_x\). Both sides are now elements of the lattice, and its coordinate isomorphism is \(A\)-linear. Therefore
\[
\pi_x^{s\mathbf t}(m)
=C_x(P_x(m))
=C_x(\beta p)
=\beta C_x(p).
\]
This supplies an actual stalk vector representing the quotient by \(\beta\).

The remaining input in the non-head reflection argument is to prove that the divided pair \(p\) lies in \(L_x\). Saturation of the lattice provides exactly that assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottTensor_maps_eq`: [BottSamelson.lean:70](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L70).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_coordinates`: [BottSamelson.lean:820](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L820).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_mem`: [BottSamelson.lean:828](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L828).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_zero_iff`: [BottSamelson.lean:836](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L836).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_value`: [BottSamelson.lean:853](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L853).

`OAI.KLInvariance.TitsSpace.bottHeadLocalPair_toStalk`: [BottSamelson.lean:859](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L859).

`OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible_of_pair`: [BottSamelson.lean:866](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L866).
