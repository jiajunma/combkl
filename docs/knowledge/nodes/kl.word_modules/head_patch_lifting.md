---
id: kl.word.head_patch_lifting
title: Compatibility and lifting of a patched tail assignment
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.head_patch
- kl.word.upper_set_reflection
- kl.word.edge_annihilation
- kl.algebra.pair_projection
- kl.word.set_tail_detection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.PairProjection.cross_lift
  - OAI.KLInvariance.TitsSpace.bottHeadPatch_compatible
  - OAI.KLInvariance.TitsSpace.bottHeadPatch_lift
  - OAI.KLInvariance.TitsSpace.bottHeadPatch_lift_of_zero_inter
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:794
    format: lean-location
    note: OAI.KLInvariance.PairProjection.cross_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPatch_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:857
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPatch_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1123
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPatch_lift_of_zero_inter
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read all branch cases of bottHeadPatch_compatible, the quotient cross_lift
    argument, the upper-union lift and the zero-intersection specialization. Included
    the full crossing-edge calculation and both output restrictions.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Compatibility and lifting of a patched tail assignment

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), a simple reflection \(s\), a word \(\mathbf t\), and a Bruhat upper set \(U\). Put \(J=U\cup sU\), \(K=U\cap sU\).

For \(m\in M_{s\mathbf t}\), let \(p=\mu(m)\) and \(q=\nu(m)\) be the underlying tail vectors. Assume
\[
\pi_x(p)=\pi_x(q)\qquad(x\in K).
\]
Then the head patch on \(J\) is compatible.

If the tail word has compatible-tuple lifting on upper sets, there is \(n\in M_{\mathbf t}\) with
\[
\pi_x(n)=\pi_x(p)\quad(x\in U),\qquad
\pi_x(n)=\pi_x(q)\quad(x\in sU).
\]
In particular, this applies when the new vector \(m\) vanishes on \(K\).

*Proof.*

### Step 1. Handle edges lying in one piece

Let \(x\to y\) be an upward reflection edge with both endpoints in \(J\).

If \(x\in U\), upward closure gives \(y\in U\). Both patch values come from \(p\), which is their common preimage.

If \(x\notin U\) and \(y\notin U\), both values come from \(q\). The vector \(q\) gives their common preimage.

The remaining case is \(x\notin U\), \(y\in U\).

### Step 2. Handle an upper endpoint in the overlap

In the remaining case, suppose \(sy\in U\). Then \(y\in K\), so the assumed equality gives \(\pi_y(p)=\pi_y(q)\).

The patch values are \(\pi_x(q)\) and \(\pi_y(p)\). They are also \(\pi_x(q)\) and \(\pi_y(q)\), hence have the common preimage \(q\).

### Step 3. Identify the crossing edge and lift its mixed values

It remains to treat \(x\notin U\), \(y\in U\), and \(sy\notin U\). Since \(x\in J\), we have \(sx\in U\). The [[node:kl.word.upper_set_reflection|crossing-edge theorem]] gives \(y=sx\).

Let \(Q\) be the old pair-projection quotient for the stalks at \(x,sx\), with maps
\(\lambda,\rho\) from those stalks. The simple-root label \(\alpha_s\) annihilates \(Q\).

The tail-difference calculation gives \(p-q=\alpha_s n_0\). Applying the composite \(\lambda\pi_x\) yields
\[
\lambda(\pi_x(p))-\lambda(\pi_x(q))
=\alpha_s\lambda(\pi_x(n_0))=0.
\]
Compatibility of the two projections of \(p\) gives
\(\lambda(\pi_x(p))=\rho(\pi_y(p))\).
Therefore
\[
\lambda(\pi_x(q))=\rho(\pi_y(p)).
\]
The pair-projection compatibility criterion gives a tail vector with these two mixed values. These are exactly the patch values at \(x,y\).

Steps 1–3 cover every edge in \(J\), proving compatibility.

### Step 4. Apply the tail lifting property

The reflected union \(J\) is upper. Compatible-tuple lifting for the tail word therefore supplies \(n\) with the patch values at every point of \(J\).

On \(U\), the defining branch is \(\pi_x(p)\), giving the first desired equality. At \(x\in sU\setminus U\), it is \(\pi_x(q)\). At \(x\in sU\cap U=K\), the branch gives \(\pi_x(p)=\pi_x(q)\) by hypothesis. This proves the second equality on all of \(sU\).

### Step 5. Obtain agreement from zero overlap

If \(p_K'(m)=0\), [[node:kl.word.set_tail_detection|set-tail detection]] gives vanishing of the first tail on \(K\) and of the second tail on \(sK\). Since \(sK=K\), both tail projections are zero on the overlap. The required equality there follows, so Steps 1–4 apply.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.PairProjection.cross_lift`: [IntegralPairings.lean:794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L794).

`OAI.KLInvariance.TitsSpace.bottHeadPatch_compatible`: [IntegralPairings.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L833).

`OAI.KLInvariance.TitsSpace.bottHeadPatch_lift`: [IntegralPairings.lean:857](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L857).

`OAI.KLInvariance.TitsSpace.bottHeadPatch_lift_of_zero_inter`: [IntegralPairings.lean:1123](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1123).
