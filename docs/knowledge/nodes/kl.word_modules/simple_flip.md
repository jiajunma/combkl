---
id: kl.word.simple_flip
title: The first-factor reflection and first-bit exchange
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.evaluation_maps
- kl.word.simple_frobenius_data
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.simpleFixedAction
  - OAI.KLInvariance.TitsSpace.bottSimpleFlip
  - OAI.KLInvariance.TitsSpace.bottSimpleFlip_tmul
  - OAI.KLInvariance.TitsSpace.bottIndexFlip
  - OAI.KLInvariance.TitsSpace.bottWeight_flip
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1885
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simpleFixedAction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1896
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1901
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleFlip_tmul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1925
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottIndexFlip
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1929
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_flip
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read simpleFixedAction, the tensor-map definition, bit flip and weight
    identity. Explained R-linearity and derived tau-semilinearity with examples separating
    the two tensor factors.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The first-factor reflection and first-bit exchange

Fix a finite-generator Coxeter system and the symmetric coefficient algebra \(A\) of its real extended realization. Fix a simple reflection \(s\), put \(R=A^s\), and let \(\tau=\chi_s\) act on the symmetric coefficient algebra. A word beginning with \(s\) has module
\[
M_{s\mathbf t}=A\otimes_R M_{\mathbf t}.
\]
The first-factor reflection is
\[
F_s:M_{s\mathbf t}\to M_{s\mathbf t},
\qquad F_s(a\otimes m)=\tau(a)\otimes m.
\]
This is `bottSimpleFlip`.

## Scalar behavior and tensor relations

The automorphism \(\tau\) fixes \(R\). Therefore the two tensors representing a balancing relation have the same image:
\[
F_s(ar\otimes m)=\tau(a)r\otimes m
=\tau(a)\otimes rm=F_s(a\otimes rm).
\]
The formula extends additively to the tensor product and is \(R\)-linear. With respect to the full coefficient ring it satisfies
\[
F_s(cv)=\tau(c)F_s(v).
\]
This is semilinearity with scalar automorphism \(\tau\). Applying \(F_s\) twice gives the identity, since \(\tau^2=1\).

For one letter, \(F_s\) fixes \(1\otimes1\) and \(1\otimes\alpha_s\), whose outer factors are \(1\). On the other hand,
\[
F_s(\alpha_s\otimes1)=-\alpha_s\otimes1.
\]
The formula singles out the outer tensor factor.

## The first-bit exchange

For a subexpression \((\varepsilon,\eta)\) of \(s\mathbf t\), define
\[
\sigma(\varepsilon,\eta)=(1-\varepsilon,\eta).
\]
This is `bottIndexFlip`. It exchanges the choice to omit the first reflection with the choice to retain it.

Its weights satisfy
\[
w(\sigma(\varepsilon,\eta))=s\,w(\varepsilon,\eta).
\]
For \(\varepsilon=0\), this is the weight recursion. For \(\varepsilon=1\), it follows from \(s(s w_{\mathbf t}(\eta))=w_{\mathbf t}(\eta)\).

The [[node:kl.word.simple_wall_kernel|simple-wall kernel theorem]] relates this bit exchange to the first-factor reflection by an explicit evaluation identity.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.simpleFixedAction`: [Frobenius.lean:1885](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1885).

`OAI.KLInvariance.TitsSpace.bottSimpleFlip`: [Frobenius.lean:1896](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1896).

`OAI.KLInvariance.TitsSpace.bottSimpleFlip_tmul`: [Frobenius.lean:1901](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1901).

`OAI.KLInvariance.TitsSpace.bottIndexFlip`: [Frobenius.lean:1925](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1925).

`OAI.KLInvariance.TitsSpace.bottWeight_flip`: [Frobenius.lean:1929](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1929).
