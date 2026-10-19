---
id: kl.dihedral.induced_inversions
title: Ambient root signs detect inversions of the induced system
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.induced_signed_action
- kl.coxeter.word_sign_record
- kl.detail.root_inversion_count
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.inversion_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:1010
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.inversion_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# Ambient root signs detect inversions of the induced system

Let \(P\) be a root plane in a finite-generator Coxeter system, with a plane basis and its induced Coxeter system on \(D_P\). Let \(t\in D_P\), and let \(a\in\Phi^+\cap P\) be an ambient root representing \(t\).

For every \(w\in D_P\),
\[
w^{-1}a\text{ is negative}
\quad\Longleftrightarrow\quad
t\text{ is a left inversion of }w\text{ in the induced system}.
\]
On the right, being a left inversion means that \(t\) is an intrinsic reflection and
\(\ell_P(tw)<\ell_P(w)\).

*Proof.*

### Step 1. Record the sign change along a reduced induced word

Choose a reduced word \(\omega\) for \(w\) in the two induced simple generators. Let \(c\in\mathbb Z/2\mathbb Z\) be the multiplicity of \(t\) in its left inversion sequence, reduced modulo two.

The [[node:kl.coxeter.word_sign_record|word-record theorem]] for a Coxeter signed action gives
\[
A_w(w^{-1}tw,c)=(t,c+c)=(t,0).
\]
Apply the inverse group action:
\[
A_{w^{-1}}(t,0)=(w^{-1}tw,c).
\]

### Step 2. Transfer this signed pair to the ambient root

The positive root \(a\) satisfies the induced signed relation for \((t,0)\). Compatibility of the induced signed action with ambient roots therefore makes
\(w^{-1}a\) realize the pair \((w^{-1}tw,c)\).

If \(c=0\), its coordinates are nonnegative. If \(c=1\), they are nonpositive. Since it is a nonzero root, the two signs are exclusive. Thus
\[
w^{-1}a\text{ is negative}\quad\Longleftrightarrow\quad c=1.
\]

### Step 3. Convert parity into occurrence

A reduced inversion sequence has no repetitions: equality of two prefix-conjugated simple reflections deletes the corresponding two letters from the word, contradicting reducedness. Hence the multiplicity of \(t\) is either zero or one.

Therefore \(c=1\) exactly when \(t\) occurs in the sequence.

### Step 4. Identify occurrence with the intrinsic left inversions

If \(t\) occurs, deleting that letter expresses \(tw\) with one fewer letter, so \(t\) is a reflection lowering \(w\).

Conversely, an intrinsic reflection lowering \(w\) deletes a letter by strong exchange; multiplying the resulting equality by \(w^{-1}\) identifies \(t\) with the prefix-conjugated simple label at that position. Thus it occurs in the inversion sequence.

Combining Steps 2–4 proves the equivalence, including the assertion that a negative ambient sign forces \(t\) to be an intrinsic reflection.

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.inversion_iff`: [Decomposition.lean:1010](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L1010).
