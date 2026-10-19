---
id: kl.word.upper_image_lifting
title: Projective upper images give compatible-tuple lifting
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.upper_image_properties
- kl.word.word_local_lifting
- kl.algebra.projective_local_membership
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottFlabby_of_projective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2057
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFlabby_of_projective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read bottFlabby_of_projective and checked its UFD, projective target, torsion-free
    ambient and both denominator inputs against the already expanded generic membership
    theorem.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Projective upper images give compatible-tuple lifting

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), and a word \(\mathbf t\). Suppose
\(L_{\mathbf t}(U)\) is projective over \(A\) for every Bruhat upper set \(U\).
Then every compatible stalk tuple on an upper set has a common word lift. In source notation,
\[
\operatorname{BottProjectiveUpper}(\mathbf t)
\Longrightarrow \operatorname{BottFlabby}(\mathbf t).
\]

*Proof.*

### Step 1. Specify the module and the vector to be lifted

Let \(U\) be upper and \(z\) compatible on \(U\). Put
\[
E=\prod_{x\in U}M_{\mathbf t}^x,\qquad L=L_{\mathbf t}(U)\subseteq E.
\]
By the hypothesis, \(L\) is projective.

Every stalk is a submodule of a product of copies of the coefficient domain \(A\). Multiplication by a nonzero coefficient is therefore injective in each stalk, coordinate by coordinate. It is consequently injective in the product \(E\). Thus \(E\) is torsion-free over \(A\).

### Step 2. Verify the coefficient-ring hypothesis

A finite basis of the extended real realization identifies \(A\) with a polynomial ring over \(\mathbb R\). This is a unique factorization domain, as required by the [[node:kl.algebra.projective_local_membership|prime-denominator membership theorem]].

### Step 3. Supply the generic and prime-local witnesses

The [[node:kl.word.word_local_lifting|word-local lifting theorem]] gives
\[
\Delta_{\mathbf t}\ne0,\qquad \Delta_{\mathbf t}z\in L.
\]
For every prime element \(p\), compatibility supplies another scalar \(d_p\) with
\[
p\nmid d_p,\qquad d_pz\in L.
\]
These are exactly the generic-span and prime-local membership hypotheses.

### Step 4. Remove the denominators inside the image

Apply the [[node:kl.algebra.projective_local_membership|prime-denominator membership theorem]] to the projective submodule \(L\subseteq E\) and the fixed vector \(z\). It removes the prime factors of the generic multiplier and gives \(z\in L\).

Concretely, for a factorization \(c=pc_1\) with \(cz\in L\), use \(d_pz\in L\) and \(p\nmid d_p\). Projective free coordinates divide \(pc_1z\) by \(p\) inside \(L\); torsion-free cancellation in \(E\) then gives \(c_1z\in L\). Repeating through the finite factorization of \(\Delta_{\mathbf t}\) reaches \(z\).

### Step 5. Read membership as a word lift

By definition of \(L_{\mathbf t}(U)\), membership \(z\in L\) supplies
\(m\in M_{\mathbf t}\) with \(\pi_x(m)=z_x\) for every \(x\in U\).
This is compatible-tuple lifting on \(U\). Since \(U,z\) were arbitrary, the word has BottFlabby.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottFlabby_of_projective`: [IntegralPairings.lean:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057).
