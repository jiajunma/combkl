---
id: kl.detail.endpoint_equality
title: R-matrix equality makes the comparison endpoints exact
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.detail.schedule_state
- kl.duality.actual_character_reciprocity
- kl.paths.dyer_paths
- kl.detail.transported_schedule
- kl.detail.costalk_reciprocity
- kl.duality.normalized_character_endpoints
- kl.duality.scaled_reciprocity
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:278
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- combinatorial_invariance
---

# R-matrix equality makes the comparison endpoints exact

Let \(\phi:[a,b]\simeq[a',b']\), and assume equality of the normalized R-polynomials for every corresponding subinterval:
\[
\widetilde R_{x,z}=\widetilde R'_{\phi(x),\phi(z)}
\qquad(a\leq x\leq z\leq b).
\]
For the actual boundary sheaf restricted to \([a,b]\), the schedule comparison has equal endpoints for every \(0<t<1\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**Role in the proof:** Proper upper intervals supply kernel freeness, and proper initial intervals supply known R-entries. The new R-equality gives exact endpoints and then current-rank suffix freeness. The canonical degree bound enters the subsequent P-induction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the initial and final states

Let \(p\) be the full chronological schedule and let \(c_x(t)\) be the scaled actual source stalk character. The empty schedule uses the whole stalk, while the full schedule uses its full outgoing kernel. With \(q=t^2\), their Hilbert values are \(C_{x,b}(q)/(1-q)^N\) and \(q^{d(x,b)}C_{x,b}(q^{-1})/(1-q)^N\), respectively, by [[node:kl.detail.costalk_reciprocity]]. Multiplying by the scale \((1-t^2)^Nt^{-d(x,b)}\) cancels the common denominator, and the exponents become \(-d(x,b)\) and \(d(x,b)\). Hence
\[
D_{[]}(t)=c(t),\qquad D_p(t)=c(t^{-1}).
\]
The full list contains every outgoing condition; the empty list contains none. This is the precise reason those two character vectors occur.

### Step 2. Expand the transported product

For \(T=t^{-1}-t\), the ordered-path formula gives, coordinatewise,
\[
\left(\operatorname{Dispatch}_{p^{\mathrm{rev}}}(T)D_p(t)\right)_x
=\sum_{z\in[a,b]}
\widetilde R'_{\phi(x),\phi(z)}(T)c_z(t^{-1}).
\]
The decreasing schedule is \(p^{\mathrm{rev}}\). The root labels used to define its scores belong to the target system, which explains the prime on the R-polynomials.

### Step 3. Use all-entry R equality

For comparable \(x\le z\), substitute the assumed equality
\(\widetilde R'_{\phi(x),\phi(z)}=\widetilde R_{x,z}\).
For noncomparable pairs, both polynomials vanish, since \(\phi\) preserves the order. Thus every summand becomes its source-system counterpart:
\[
\sum_z\widetilde R_{x,z}(T)c_z(t^{-1}).
\]

### Step 4. Apply the source reciprocity identity

The [[node:kl.duality.scaled_reciprocity|scaled actual-character reciprocity theorem]] states that this last sum is \(c_x(t)\). By Step 1, it is \(D_{[]}(t)_x\). This holds for each \(x\), so the two vectors are equal:
\[
D_{[]}(t)=\operatorname{Dispatch}_{p^{\mathrm{rev}}}(T)D_p(t).
\]
This completes the coordinatewise endpoint identity.

In the simultaneous induction, the smaller subintervals supply the other comparable R-entries, and the newly proved current entry completes the matrix equality used here. Choosing \(t=\tfrac12\) gives one concrete exact endpoint, sufficient for the later Hilbert-equality argument.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.actual_endpoint_of_rTilde_eq`: [SimultaneousInvariance.lean:278](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L278).
