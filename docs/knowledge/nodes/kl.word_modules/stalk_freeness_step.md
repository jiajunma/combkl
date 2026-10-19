---
id: kl.word.stalk_freeness_step
title: Freeness of a new stalk from the two tail stalks
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.kernel_exactness
- kl.word.head_pair_equivalence
- kl.word.pair_lattice_exact_sequences
- kl.word.simple_frobenius_data
- kl.word.edge_annihilation
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalk_smul_injective
  - OAI.KLInvariance.TitsSpace.bottStalkFinite
  - OAI.KLInvariance.TitsSpace.bottStalk_free_cons
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:992
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_smul_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:997
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkFinite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1282
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_free_cons
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read both branches of bottStalk_free_cons, the coordinate-domain scalar-injectivity
    fact and the finite-image instance. Used the previously proved explicit split
    sequences and kept all old-word assumptions.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Freeness of a new stalk from the two tail stalks

Fix a finite-generator Coxeter system and its symmetric coefficient algebra \(A\). Suppose a word \(\mathbf t\) has exact reflection kernels and that every stalk \(M_{\mathbf t}^y\) is free over \(A\).

For every simple reflection \(s\) and every weight \(x\), the stalk \(M_{s\mathbf t}^x\) is finite free.

*Proof.*

### Step 1. Identify the new stalk with a reflected pair lattice

Put
\[
X=M_{\mathbf t}^x,\qquad Y=M_{\mathbf t}^{sx},
\qquad \tau=\chi_s,\quad \alpha=\alpha_s.
\]
Let \(f,g\) be the two old stalk projections. Their reflected pair lattice
\(L_x\subseteq X\oplus{}^\tau Y\) is isomorphic to \(M_{s\mathbf t}^x\) by the [[node:kl.word.head_pair_equivalence|head-pair theorem]]. It suffices to prove \(L_x\) free.

The old projections are surjective. Simple-root divisibility and edge annihilation give the two hypotheses defining the lattice.

### Step 2. Check injectivity of multiplication by the root

The coefficient algebra \(A\) is a domain, and \(\alpha\ne0\). Each old stalk is a submodule of a product of copies of \(A\). If \(\alpha z=0\), each coordinate satisfies \(\alpha z_\eta=0\), hence each \(z_\eta=0\). Thus multiplication by \(\alpha\) is injective on both \(X\) and \(Y\).

### Step 3. Split the first projection in the ascent case

Suppose \(\ell(x)<\ell(sx)\). Old-word exactness gives
\[
\{g(n):f(n)=0\}=\alpha Y.
\]
The first pair-lattice exact sequence is therefore
\[
0\longrightarrow{}^\tau Y
\xrightarrow{z\mapsto(0,\alpha z)}
L_x\longrightarrow X\longrightarrow0.
\]
Its hypotheses hold by Step 2 and surjectivity of \(f\).

The two tail stalks are free by assumption, and twisting preserves freeness. Lifting a basis of \(X\) splits the surjection, giving
\(L_x\simeq{}^\tau Y\oplus X\). Thus \(L_x\) is free.

### Step 4. Split the other projection in the descent case

Suppose \(\ell(sx)<\ell(x)\). Apply old exactness to the upward edge \(sx\to x=s(sx)\). It gives
\[
\{f(n):g(n)=0\}=\alpha X.
\]
Now the second pair-lattice exact sequence is
\[
0\longrightarrow X
\xrightarrow{z\mapsto(\alpha z,0)}
L_x\longrightarrow{}^\tau Y\longrightarrow0.
\]
Step 2 gives injectivity of its first map, and \(g\) is surjective. Lifting a basis of the free quotient \({}^\tau Y\) splits this sequence, so \(L_x\) is free.

These two cases exhaust the possibilities because simple multiplication changes length by one.

### Step 5. Transport freeness and prove finite generation

The head-pair isomorphism transports the free-module structure of \(L_x\) to the new stalk. The new word module is finite free, and its stalk projection is surjective. The images of a finite set of word-basis generators therefore generate the stalk.

Thus the new stalk is both free and finitely generated, hence finite free. The argument works for each \(x\), giving the freeness assertion needed in the next word-induction step.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalk_smul_injective`: [BottSamelson.lean:992](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L992).

`OAI.KLInvariance.TitsSpace.bottStalkFinite`: [BottSamelson.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L997).

`OAI.KLInvariance.TitsSpace.bottStalk_free_cons`: [BottSamelson.lean:1282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1282).
