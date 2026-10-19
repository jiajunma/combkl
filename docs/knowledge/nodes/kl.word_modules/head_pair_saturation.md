---
id: kl.word.head_pair_saturation
title: Regular edge scalars and saturation of the head pair lattice
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.kernel_exactness
- kl.word.edge_annihilation
- kl.word.twisted_lattice_saturation
- kl.algebra.scalar_quotient_regular
- kl.algebra.linear_primes
- kl.word.local_pair_maps
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.simple_represents
  - OAI.KLInvariance.TitsSpace.represents_polynomial_prime
  - OAI.KLInvariance.TitsSpace.bottStalkFinite
  - OAI.KLInvariance.TitsSpace.bottSimpleEdge_regular
  - OAI.KLInvariance.TitsSpace.bottHeadPairLattice_saturated
  - OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:971
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.simple_represents
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:976
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.represents_polynomial_prime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:997
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkFinite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1060
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSimpleEdge_regular
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1088
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairLattice_saturated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1116
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read both ascent/descent quotient-regularity applications and their finite-basis
    input, then the lattice saturation and stalk descent. Preserved both old-word
    induction hypotheses and the nondivisibility condition.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Regular edge scalars and saturation of the head pair lattice

Fix a finite-generator Coxeter system, its symmetric coefficient algebra \(A\), and a word \(\mathbf t\). Assume:

1. \(\mathbf t\) has exact reflection kernels;
2. every stalk \(M_{\mathbf t}^y\) is free over \(A\).

Let \(s\) be simple, let \(\alpha=\alpha_s\), and write \(\tau=\chi_s\). For any weight \(x\), form the edge quotient \(Q_x\) comparing the old stalks at \(x,sx\), and their reflected pair lattice \(L_x\).

For \(\beta\in A\) with \(\alpha\nmid\beta\), multiplication by \(\beta\) is injective on \(Q_x\). Consequently
\[
\beta p\in L_x\quad\Longleftrightarrow\quad p\in L_x
\]
for every \(p\in M_{\mathbf t}^x\oplus{}^\tau M_{\mathbf t}^{sx}\).

*Proof.*

### Step 1. Check primality and finite freeness

The simple root is nonzero in the extended realization, so its symmetric-algebra generator \(\alpha\) is a prime element by the [[node:kl.algebra.linear_primes|linear-prime theorem]].

Every old stalk is a surjective image of the finite free word module, and hence is finitely generated. Together with the assumed freeness, this gives a finite basis for each stalk used below.

Put \(X=M_{\mathbf t}^x\), \(Y=M_{\mathbf t}^{sx}\), with projections \(f,g\) from the old word module. Let \(\lambda:X\to Q_x\) and \(u:Y\to Q_x\) be the pair-projection maps.

### Step 2. Use the upper stalk when x is an ascent

Suppose \(\ell(x)<\ell(sx)\). Exact reflection kernels for the old word give
\[
\ker u=\alpha Y.
\]
The map \(u\) is surjective because \(f\) is. Its domain \(Y\) is finite free by Step 1. Apply the [[node:kl.algebra.scalar_quotient_regular|regular-scalar quotient theorem]] to
\(q=u\), prime \(\alpha\), and scalar \(\beta\). The hypothesis \(\alpha\nmid\beta\) proves that multiplication by \(\beta\) is injective on \(Q_x\).

### Step 3. Use the opposite endpoint when x is a descent

Suppose \(\ell(sx)<\ell(x)\). Apply the old exact-kernel condition to the upward edge from \(sx\) to \(x=s(sx)\). It says
\[
\{f(n):g(n)=0\}=\alpha X.
\]
The pair-projection lower-kernel criterion identifies the left side with \(\ker\lambda\). Thus \(\ker\lambda=\alpha X\).

The map \(\lambda\) is surjective because \(g\) is, and \(X\) is finite free. The same [[node:kl.algebra.scalar_quotient_regular|regular-scalar quotient theorem]], now applied to \(q=\lambda\), proves injectivity of multiplication by \(\beta\) on \(Q_x\).

Simple multiplication changes length by one, so these two cases cover every \(x\).

### Step 4. Cancel the scalar in the pair relation

The old simple-edge quotient is annihilated by \(\alpha\), and
\(\tau(\beta)-\beta\) is divisible by \(\alpha\). Hence \(\tau(\beta)\) and \(\beta\) act identically on \(Q_x\).

If \(\beta p\in L_x\), write \(p=(p_0,p_1)\). Compatibility gives
\[
\beta\,\lambda(p_0)=\tau(\beta)\,u(p_1)=\beta\,u(p_1).
\]
Steps 2–3 let us cancel \(\beta\) in \(Q_x\), giving
\(\lambda(p_0)=u(p_1)\). The pair-projection compatibility criterion provides a common old-word preimage, so \(p\in L_x\).

The converse follows from scalar closure of \(L_x\). This is the source's application of the [[node:kl.word.twisted_lattice_saturation|twisted-lattice saturation theorem]].

### Step 5. Apply saturation to a new stalk projection

If a new word vector \(m\) has local pair \(P_x(m)=\beta p\), the [[node:kl.word.local_pair_maps|local-pair theorem]] gives \(P_x(m)\in L_x\). Step 4 places \(p\) in \(L_x\), and the same theorem then gives
\[
\pi_x^{s\mathbf t}(m)=\beta C_x(p).
\]
This converts coordinate divisibility into divisibility within the actual new stalk.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.simple_represents`: [BottSamelson.lean:971](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L971).

`OAI.KLInvariance.TitsSpace.represents_polynomial_prime`: [BottSamelson.lean:976](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L976).

`OAI.KLInvariance.TitsSpace.bottStalkFinite`: [BottSamelson.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L997).

`OAI.KLInvariance.TitsSpace.bottSimpleEdge_regular`: [BottSamelson.lean:1060](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1060).

`OAI.KLInvariance.TitsSpace.bottHeadPairLattice_saturated`: [BottSamelson.lean:1088](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1088).

`OAI.KLInvariance.TitsSpace.bottHeadStalk_divisible`: [BottSamelson.lean:1116](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1116).
