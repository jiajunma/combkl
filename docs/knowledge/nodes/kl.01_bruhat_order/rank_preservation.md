---
id: kl.foundations.rank_preservation
title: Interval isomorphisms preserve rank differences
kind: theorem
status: proved
primary_topic: kl.01_bruhat_order
topics:
- kl.01_bruhat_order
uses:
- kl.foundations.interval
- kl.foundations.subword
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.intervalIso_rankDifference
  - OAI.KLInvariance.intervalIso_full_rankDifference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:415
    format: lean-location
    note: OAI.KLInvariance.intervalIso_rankDifference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:458
    format: lean-location
    note: OAI.KLInvariance.intervalIso_full_rankDifference
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; sec:background
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
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

# Interval isomorphisms preserve rank differences

If \(\phi:[u,b]\simeq[u',b']\) is an order isomorphism, then every comparable pair \(x\le y\) satisfies
\[
\ell(y)-\ell(x)=\ell(\phi(y))-\ell(\phi(x)).
\]

*Proof.*

### Step 1. Produce a length-one successor inside any nontrivial interval

We use the elementary simple maps \(L_s,U_s\) and their monotonicity established in the subword proof. We claim that \(x<y\) admits \(x<z\le y\) with \(\ell(z)=\ell(x)+1\). Prove this by induction on \(\ell(y)\). Choose a simple descent \(s\) of \(y\).

If \(x\le sy\) and \(x=sy\), take \(z=y\). If \(x<sy\), apply induction inside \([x,sy]\), whose top is shorter, and retain the resulting \(z\).

It remains to treat \(x\not\le sy\). If \(s\) raised \(x\), monotonicity of \(L_s\) would give \(x=L_s(x)\le L_s(y)=sy\), a contradiction. Thus \(s\) lowers both \(x\) and \(y\), and monotonicity gives \(sx<sy\). Induction provides
\(sx<w\le sy\) with \(\ell(w)=\ell(sx)+1=\ell(x)\).

Monotonicity of \(U_s\) gives \(x=U_s(sx)\le U_s(w)\le U_s(sy)=y\).
The reflection \(s\) must raise \(w\): if it lowered \(w\), then \(U_s(w)=w\), so \(x\le w\) with equal lengths would force \(x=w\le sy\), again a contradiction. Take \(z=sw=U_s(w)\). Its length is \(\ell(x)+1\), proving the claim in every case.

### Step 2. Build a maximal-length chain

Repeat Step 1 on the remaining interval \([z,y]\). Each step raises length by exactly one, and the length cannot exceed \(\ell(y)\). We obtain a chain from \(x\) to \(y\) with exactly
\(d=\ell(y)-\ell(x)\) strict steps.

Every strictly increasing chain has at most \(d\) steps, since each strict Bruhat comparison raises integer length by at least one. Thus \(d\) is the maximum number of strict steps in a chain between the two endpoints.

### Step 3. Transport the chain and apply the inverse

An order isomorphism \(\phi\) preserves every strict comparison and takes distinct vertices to distinct vertices. Transporting the chain from Step 2 gives a chain of \(d\) strict steps between \(\phi(x)\) and \(\phi(y)\). Therefore
\(d(x,y)\le d(\phi(x),\phi(y))\).

Apply the same argument to \(\phi^{-1}\) to obtain the reverse inequality. The two rank differences are equal. Applying this to the bottom and top gives the full-interval statement, because an order isomorphism preserves the unique minimum and maximum.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L2).

## Lean formalization

`OAI.KLInvariance.intervalIso_rankDifference`: [CanonicalKL.lean:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

`OAI.KLInvariance.intervalIso_full_rankDifference`: [CanonicalKL.lean:458](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L458).
