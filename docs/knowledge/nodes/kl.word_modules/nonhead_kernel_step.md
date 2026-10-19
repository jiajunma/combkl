---
id: kl.word.nonhead_kernel_step
title: Exact kernels for a reflection distinct from the first letter
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.local_pair_maps
- kl.word.head_pair_saturation
- kl.coxeter.simple_edge_transport
- kl.algebra.linear_primes
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.represents_polynomial_not_dvd
  - OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead
  - OAI.KLInvariance.TitsSpace.Represents.act
  - OAI.KLInvariance.TitsSpace.Represents.independent_of_ne
  - OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:982
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.represents_polynomial_not_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1130
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1714
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.act
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1983
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.independent_of_ne
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1998
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read bottKernelExact_cons_nonhead including edge orientation, conjugated
    root, both tail applications, transformed scalar, nondivisibility and saturation.
    Made every substituted weight and root explicit.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Exact kernels for a reflection distinct from the first letter

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\). Assume the tail word \(\mathbf t\) has exact reflection kernels and free stalks at every weight. Prepend a simple reflection \(s\), with coefficient action \(\tau=\chi_s\) and root polynomial \(\alpha_s\).

Let \(t\ne s\) be a reflection represented by a root \(a\), put
\[
y=tx,\qquad \beta=\iota(\operatorname{embed}(a)),
\]
and assume \(\ell(x)<\ell(y)\). If \(m\in M_{s\mathbf t}\) satisfies
\(\pi_x^{s\mathbf t}(m)=0\), then
\[
\pi_y^{s\mathbf t}(m)=\beta z
\quad\text{for some }z\in M_{s\mathbf t}^y.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport the upward edge by the first reflection

Because \(t\ne s\), the equality \(tx=sx\) is impossible by cancellation on the right. The [[node:kl.coxeter.simple_edge_transport|simple edge-transport theorem]] therefore takes the upward edge \(x\to y\) to an upward edge
\[
sx\longrightarrow sy.
\]
Its reflection is \(sts^{-1}=sts\), since
\[
(sts^{-1})(sx)=s(tx)=sy.
\]
The transformed root \(s(a)\) represents this conjugate reflection. Indeed, if \(a=z(r_i)\) and \(t=z s_i z^{-1}\), then \(s(a)=(sz)(r_i)\) and \(sts^{-1}=(sz)s_i(sz)^{-1}\). These are the two defining equations for the transformed root to represent the conjugated reflection.

### Step 2. Extract two tail vectors with zero lower projections

Let \(m_0=\mu(m)\) be the ordinary tail vector and let \(m_1\) be the underlying vector of the reflected tail \(\nu(m)\).

The local-pair zero criterion applied at \(x\) turns the hypothesis into
\[
\pi_x^{\mathbf t}(m_0)=0,\qquad
\pi_{sx}^{\mathbf t}(m_1)=0.
\]

### Step 3. Apply old-word exactness to each upward edge

Apply exact reflection kernels of the shorter word to \(x\to tx=y\), root \(a\), and vector \(m_0\). It supplies \(p\in M_{\mathbf t}^y\) with
\[
\pi_y^{\mathbf t}(m_0)=\beta p.
\]

Apply the same induction hypothesis to the transported edge \(sx\to sy\), root \(s(a)\), and vector \(m_1\). It supplies \(q\in M_{\mathbf t}^{sy}\) with
\[
\pi_{sy}^{\mathbf t}(m_1)
=\iota(\operatorname{embed}(s(a)))q.
\]
The extended action restricts to the geometric action on embedded roots, so
\[
\iota(\operatorname{embed}(s(a)))=\chi_s(\beta)=\tau(\beta).
\]
Thus the two old projections are \(\beta p\) and \(\tau(\beta)q\).

### Step 4. Assemble the divided pair in the twisted module

The local pair of \(m\) at the new upper weight \(y\) is
\[
P_y(m)=\bigl(\pi_y(m_0),\pi_{sy}(m_1)\bigr)
=(\beta p,\tau(\beta)q).
\]
The second factor has scalar action \(r\star q=\tau(r)q\). Therefore this is exactly
\[
P_y(m)=\beta\cdot(p,q)
\]
in \(M_{\mathbf t}^y\oplus{}^\tau M_{\mathbf t}^{sy}\).

### Step 5. Exclude divisibility by the first root

We claim \(\alpha_s\nmid\beta\). If divisibility held, the [[node:kl.algebra.linear_primes|linear-generator divisibility criterion]] would give
\[
\operatorname{embed}(a)=c\,\operatorname{embed}(r_s)
\]
for a real scalar \(c\), where \(r_s\) is the simple root. Projection to the original realization gives \(a=c r_s\).

Let \(B\) be its geometric bilinear form. Both roots have squared norm two, so
\[
2=B(a,a)=c^2B(r_s,r_s)=2c^2.
\]
Thus \(c^2=1\), and the real scalar \(c\) is \(1\) or \(-1\). Hence \(a=r_s\) or \(a=-r_s\). Both represent \(s\), and uniqueness of the reflection represented by a root forces \(t=s\), a contradiction.

This is the norm calculation behind the source's independence lemma and represents_polynomial_not_dvd.

### Step 6. Remove the scalar inside the head pair lattice

The [[node:kl.word.local_pair_maps|local-pair theorem]] gives \(P_y(m)\in L_y\). By Step 4, the multiple \(\beta(p,q)\) lies in \(L_y\). [[node:kl.word.head_pair_saturation|Head-pair saturation]] applies because the tail has exact reflection kernels and free stalks, and Step 5 gives \(\alpha_s\nmid\beta\). Hence \((p,q)\in L_y\).

The head-pair isomorphism now supplies \(z=C_y(p,q)\in M_{s\mathbf t}^y\), and its linearity gives
\[
\pi_y^{s\mathbf t}(m)=C_y(P_y(m))
=C_y(\beta(p,q))=\beta z.
\]
This is the required exact-kernel divisibility.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.represents_polynomial_not_dvd`: [BottSamelson.lean:982](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L982).

`OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead`: [BottSamelson.lean:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130).

`OAI.KLInvariance.TitsSpace.Represents.act`: [Tits.lean:1714](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1714).

`OAI.KLInvariance.TitsSpace.Represents.independent_of_ne`: [Tits.lean:1983](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1983).

`OAI.KLInvariance.TitsSpace.Represents.extended_independent_of_ne`: [Tits.lean:1998](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1998).
