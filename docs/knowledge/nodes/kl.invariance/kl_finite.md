---
id: kl.main.kl_finite
title: KL invariance for finite-generator Coxeter systems
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.rtilde_invariance
- kl.foundations.scaled_kl
- kl.comparison.reciprocal_rigidity
- kl.foundations.rank_preservation
lean:
  repository: openai-kl
  modules:
  - Invariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Invariance:427
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
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
- induction
---

# KL invariance for finite-generator Coxeter systems

If the simple-generator sets of two Coxeter systems are finite and \([u,b]\simeq[u',b']\), then
\[
P_{u,b}(q)=P'_{u',b'}(q).
\]
The groups themselves may be infinite.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**How to read this entry:** Proper upper intervals supply kernel freeness, and proper initial intervals supply known R-entries. The new R-equality gives exact endpoints and then current-rank suffix freeness. The canonical degree bound enters the subsequent P-induction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Fix the already proved R-matrix equality

The simultaneous theorem gives R-tilde invariance on every restricted interval. Thus, for \(x,z\in[a,b]\),
\[
\widetilde R_{x,z}=\widetilde R'_{\phi(x),\phi(z)}.
\]
For comparable pairs this is the theorem applied to the restricted isomorphism; for noncomparable pairs both entries vanish. Denote their common evaluated matrix at \(T=t^{-1}-t\) by \(A(T)\).

At this stage we use canonical KL polynomials, whose strict degree bound and reciprocity have been established independently of the sheaf character.

### Step 2. Induct on the rank with fixed top endpoints

Induct strongly on \(d(a,b)\), keeping \(b,b'\) fixed and allowing the lower endpoints and their interval isomorphism to vary. At rank zero, \(a=b\) and \(a'=b'\), so the two diagonal polynomials are both \(1\).

Suppose the rank is positive. For every \(y>a\), the restriction
\([y,b]\simeq[\phi(y),b']\) has smaller rank. The induction hypothesis gives
\(P_{y,b}=P'_{\phi(y),b'}\).

### Step 3. Put the two canonical vectors in the same normalization

For \(x\in[a,b]\), set
\[
k_x(t)=t^{-d(x,b)}P_{x,b}(t^2),\qquad
k'_x(t)=t^{-d(x,b)}P'_{\phi(x),b'}(t^2).
\]
The common exponent is valid because \(\phi\) preserves rank differences. The higher-entry equalities in Step 2 give \(k_y(t)=k'_y(t)\) for \(y>a\), and the same holds at \(t^{-1}\).

Scaled canonical reciprocity, together with Step 1, gives
\(k(t)=A(T)k(t^{-1})\) and \(k'(t)=A(T)k'(t^{-1})\).

### Step 4. Isolate the bottom difference

Subtract the two equalities in coordinate \(a\). All terms indexed by \(y>a\) vanish by Step 3. The coefficient at \(a\) is \(\widetilde R_{a,a}(T)=1\). Therefore, with \(\Delta(t)=k_a(t)-k'_a(t)\),
\[
\Delta(t)=\Delta(t^{-1}).
\]
In Lean, the common comparison interface is applied in both directions to obtain the same equality from its two inequalities; the exact identities above provide those inequalities.

### Step 5. Remove the normalization and use the degree bound

Write \(d=d(a,b)=d(a',b')>0\) and \(p=P_{a,b}-P'_{a',b'}\). Step 4 says
\[
t^{-d}p(t^2)=t^dp(t^{-2}).
\]
Multiply by \(t^d\) and put \(q=t^2\). Every \(0<q<1\) has the choice \(t=\sqrt q\in(0,1)\), so
\(p(q)=q^dp(q^{-1})\) throughout that interval.

Both canonical polynomials have degree strictly below \(d/2\). [[node:kl.comparison.reciprocal_rigidity]] therefore gives \(p=0\), which is the required equality. This closes the KL induction after the R/freeness induction has already finished.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.klPolynomial_invariance_finite`: [Invariance.lean:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).
