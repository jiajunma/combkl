---
id: kl.comparison.global_comparison
title: The transported comparison for actual characters
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.schedule_upper_freeness
- kl.duality.scaled_stalk
- kl.duality.normalized_character_endpoints
- kl.duality.character_endpoint_substitution
- kl.detail.schedule_state
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.schedule_final_scaledStalk
  - OAI.KLInvariance.BruhatGraph.transported_initial_scaledStalk
  - OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:1324
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.schedule_final_scaledStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:255
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.transported_initial_scaledStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:264
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness
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
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Matched the declared theorem to its actual dispatch conclusion. Checked
    all upper-freeness quantifiers, source actual character, full/empty kernel transport,
    positive denominator cancellation and integer exponent computation. Kept the later
    target R-matrix identification as the next linked result.
tags:
- Kazhdan-Lusztig
- induction
---

# The transported comparison for actual characters

Let \(W,W'\) be finite-generator Coxeter systems, \(a\le_W b\), and
\(\phi:[a,b]_W\simeq[a',b']_{W'}\) an order isomorphism. Fix a finite real basis \(\Sigma\) of the source extended realization, put \(A=\mathbb R[X_i:i\in\Sigma]\), \(N=|\Sigma|\), and restrict the actual boundary sheaf on \([1,b]_W\) to \([a,b]_W\).

Write \(P=\operatorname{chronologicalSchedule}(\phi)\) and
\(Q=\operatorname{transportedSchedule}(\phi)=P^{\mathrm{rev}}\).
For every suffix \(e::q\preceq_{\mathrm{suf}}P\), assume that the upper selected kernel \(K_{r(e)}(F_q(r(e)))\) is free over \(A\).

Let \(C_{x,b}(q)\in\mathbb Z[q]\) be the actual stalk character of the source boundary sheaf. For nonzero real \(t\), its [[node:kl.duality.scaled_stalk|scaled actual-stalk character]] is
\[
c_x(t)=t^{\ell_W(x)-\ell_W(b)}C_{x,b}(t^2).
\]
For \(0<t<1\), put \(T=t^{-1}-t\). Then
\[
c(t)\le\mathcal D_Q(T)c(t^{-1})
\tag{1}
\]
coordinatewise on the source interval. This is the exact dispatch-valued conclusion of `actual_comparison_of_upper_freeness`.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different proof route.**

**OpenAI notes:** The simultaneous induction compares normalized KL vectors, obtains P-invariance from the strict half-degree bound, and then recovers bottom terminal-kernel freeness from endpoint equality. [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:reciprocal-vector](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L311).

**Lean (primary):** The simultaneous induction first proves normalized R-invariance together with suffix-kernel freeness in both transported directions. It cancels known bottom R-row entries against one actual source-character vector. Canonical KL equality is proved afterwards in a separate induction using the now common R-matrix and the canonical degree bound. [Invariance:136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L136), [Invariance:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L190), [Invariance:427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L427).

**Role in the proof:** Proper upper intervals supply kernel freeness, and proper initial intervals supply known R-entries. The new R-equality gives exact endpoints and then current-rank suffix freeness. The canonical degree bound enters the subsequent P-induction.

**Transfer comparison before the target path-matrix identification.**

**OpenAI notes:** The notes identify the state endpoints with normalized KL vectors and present the accumulated bound using the target R-matrix. [eq:endpoints](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L250), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298).

**Lean (primary):** The declared actual_comparison_of_upper_freeness theorem concludes an inequality with the dispatch operator applied to the actual source-character vector at the inverse parameter. Its proof substitutes the full- and empty-kernel endpoint identities into the schedule bound. The path-matrix identification is a separate input to later comparison results. [TerminalKernels:1324](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1324), [SimultaneousInvariance:255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L255), [SimultaneousInvariance:264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L264).

**Role in the proof:** The entry states that exact dispatch conclusion, derives both endpoint substitutions, and links the subsequent geometric path identification. The actual source-character polynomial remains explicit.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The conditional complete-schedule bound

The sheaf, interval isomorphism, coefficient basis and free upper kernels satisfy the hypotheses of the [[node:kl.comparison.schedule_upper_freeness|comparison under upper-kernel freeness]]. It gives
\[
D_{[]}(t)\le\mathcal D_Q(T)D_P(t).
\tag{2}
\]
We identify its two state vectors using the [[node:kl.duality.normalized_character_endpoints|normalized endpoint identities]].

### Step 2. The empty-list state

At each \(x\), the empty-list selected kernel is the entire stalk, with Hilbert value
\[
H_{\mathcal B^x}(t^2)=\frac{C_{x,b}(t^2)}{(1-t^2)^N}.
\]
The stalk is the same as the corresponding stalk in \([1,b]_W\), since the sheaf was restricted along the upper-interval inclusion.
Multiplication by the state scale gives
\[
\begin{aligned}
D_{[]}(t)_x
&=(1-t^2)^N t^{\ell_W(x)-\ell_W(b)}
  \frac{C_{x,b}(t^2)}{(1-t^2)^N}\\
&=t^{\ell_W(x)-\ell_W(b)}C_{x,b}(t^2)
=c_x(t).
\end{aligned}
\]
The cancellation is valid because \(1-t^2>0\). This is `schedule_final_scaledStalk`.

### Step 3. The full-list kernel

The chronological schedule \(P\) contains every edge of the interval. Thus \(F_P(x)=\operatorname{Out}(x)\) at every vertex. Restriction to \([a,b]\) retains every upward edge from \(x\), so its full outgoing kernel equals the corresponding full kernel in \([1,b]\). In the actual boundary sheaf this is the costalk used by the [[node:kl.duality.normalized_character_endpoints|normalized endpoint identities]].

Put \(d_x=\ell_W(b)-\ell_W(x)\). The full-kernel formula established there is
\[
H_{K_x(\operatorname{Out}(x))}(t^2)
=\frac{(t^2)^{d_x} C_{x,b}(t^{-2})}{(1-t^2)^N}.
\]
Its derivation uses the actual homogeneous section duality and the count of incoming edges, as detailed in those endpoint proofs.

### Step 4. Scaling at the initial endpoint

Substitute this full-kernel value:
\[
\begin{aligned}
D_P(t)_x
&=(1-t^2)^N t^{-d_x}
  \frac{(t^2)^{d_x} C_{x,b}(t^{-2})}{(1-t^2)^N}\\
&=t^{-d_x+2d_x}C_{x,b}(t^{-2})\\
&=t^{d_x}C_{x,b}(t^{-2})\\
&=(t^{-1})^{-d_x}C_{x,b}((t^{-1})^2)
=c_x(t^{-1}).
\end{aligned}
\]
All inverse powers are defined because \(t>0\). This calculation is `transported_initial_scaledStalk` for the arbitrary interval isomorphism \(\phi\).

### Step 5. Substitution of the endpoint vectors

Steps 2 and 4 hold at every vertex, hence give equalities of vectors
\[
D_{[]}(t)=c(t),\qquad D_P(t)=c(t^{-1}).
\]
Replace the two states in (2) by these vectors to obtain (1).

The [[node:kl.paths.dyer_paths|geometric path identity]] identifies the ordered product \(\mathcal D_Q(T)\) with the target normalized R-matrix transported through \(\phi\). That subsequent identification converts (1) to the matrix inequality used in the R-induction. The vector in (1) is already defined entirely from the actual source sheaf.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.schedule_final_scaledStalk`: [TerminalKernels.lean:1324](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1324).

`OAI.KLInvariance.BruhatGraph.transported_initial_scaledStalk`: [SimultaneousInvariance.lean:255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L255).

`OAI.KLInvariance.BruhatGraph.actual_comparison_of_upper_freeness`: [SimultaneousInvariance.lean:264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L264).
