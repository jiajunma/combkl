---
id: kl.detail.bruhat_lifting
title: Monotone simple envelopes and the Bruhat lifting property
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.detail.simple_envelopes
- kl.detail.strong_exchange
- kl.coxeter.simple_edge_transport
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.bruhatStep_simple_mul
  - OAI.KLInvariance.lowerSimple_mono
  - OAI.KLInvariance.upperSimple_mono
  - OAI.KLInvariance.bruhat_lifting
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:262
    format: lean-location
    note: OAI.KLInvariance.bruhatStep_simple_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:387
    format: lean-location
    note: OAI.KLInvariance.lowerSimple_mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:394
    format: lean-location
    note: OAI.KLInvariance.upperSimple_mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:403
    format: lean-location
    note: OAI.KLInvariance.bruhat_lifting
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Monotone simple envelopes and the Bruhat lifting property

Let \((W,S)\) be a Coxeter system, fix a **simple reflection** \(s\in S\), and write \(\le\) for strong Bruhat order. The lower and upper simple-reflection envelopes are
\[
L_s(w)=\min_{\le}\{w,sw\},\qquad
U_s(w)=\max_{\le}\{w,sw\}.
\]
These minima and maxima exist because \(w\) and \(sw\) are comparable. Both maps are monotone, in the precise sense that
\[
x\le y\quad\Longrightarrow\quad
L_s(x)\le L_s(y)\ \text{and}\ U_s(x)\le U_s(y).
\]
In particular, if \(x\le y\), \(\ell(x)<\ell(sx)\), and \(\ell(sy)<\ell(y)\), then
\[
x\le sy,\qquad sx\le y.
\]
For a simple reflection, the two length conditions are equivalent to \(x<sx\) and \(sy<y\) in Bruhat order. The multiplication here is on the left.

Monotonicity does not mean preservation of strict inequalities: \(1<s\), but \(L_s(1)=L_s(s)=1\) and \(U_s(1)=U_s(s)=s\). Left multiplication itself is also not monotone, since it sends \(1<s\) to \(s>1\).

*Proof.*

### Step 1. Transport an upward reflection edge

Suppose \(x\to y=tx\), and exclude \(y=sx\). The conjugate \(sts\) is a reflection taking \(sx\) to \(sy\). We must check orientation.

If \(\ell(sy)=\ell(y)+1\), then \(\ell(sx)\le\ell(x)+1<\ell(y)+1=\ell(sy)\). Otherwise choose a reduced word \(\omega\) for \(sy\). Then \(s\omega\) is reduced for \(y\). Strong exchange for \(ty=x\) deletes one letter from \(s\omega\). Deleting its first letter would give \(x=sy\), which is excluded. Thus a letter of \(\omega\) is deleted and \(sx\) is represented by the shortened word. Its length is at most \(\ell(sy)-1\). Hence \(sx\to sy\) is upward in both cases.

### Step 2. Check both envelopes on a single edge

If \(y=sx\), the two endpoints have the same lower envelope and the same upper envelope. Otherwise Step 1 supplies \(sx\le sy\). There are four cases according to whether \(s\) lowers each endpoint.

- It lowers both: lower envelopes compare by \(sx\le sy\), and upper envelopes by \(x\le y\).
- It lowers \(x\) and raises \(y\): use \(sx\le x\le y\) for the lower envelopes and \(x\le y\le sy\) for the upper ones.
- It raises \(x\) and lowers \(y\): use \(x\le sx\le sy\) for the lower envelopes and \(sx\le sy\le y\) for the upper ones.
- It raises both: lower envelopes compare by \(x\le y\), and upper envelopes by \(sx\le sy\).

These are precisely the four branches of the formal edge-monotonicity proof.

### Step 3. Pass to Bruhat chains and specialize

Bruhat order is the reflexive transitive closure of upward reflection edges. On a chain, apply Step 2 to every edge and compose the inequalities; on a zero-length chain use reflexivity. Therefore both envelopes are monotone.

Under the stated ascent/descent hypotheses,
\(L_s(x)=x\), \(L_s(y)=sy\), \(U_s(x)=sx\), and \(U_s(y)=y\). Substituting these four values into monotonicity gives the two required inequalities.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.bruhatStep_simple_mul`: [Bruhat.lean:262](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L262).

`OAI.KLInvariance.lowerSimple_mono`: [Bruhat.lean:387](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L387).

`OAI.KLInvariance.upperSimple_mono`: [Bruhat.lean:394](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L394).

`OAI.KLInvariance.bruhat_lifting`: [Bruhat.lean:403](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L403).
