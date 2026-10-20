---
id: kl.dihedral.native_count_difference
title: The native dihedral later-count difference
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.native_later_counts
- kl.dihedral.angular_indicator_tables
- kl.dihedral.lower_signed_sums
- kl.dihedral.signed_lengths
- kl.dihedral.good_indices
- kl.dihedral.signed_period
- kl.dihedral.signed_count_difference
- kl.dihedral.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_same
  - OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_next
  - OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference
  - OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_eq_zero
  - OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1923
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_same
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1948
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_next
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1974
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2022
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_eq_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2030
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient and intrinsic systems, root signs, signed lengths, finite
    representative bounds and counting domains explicit?
  verdict: Reviewed the exact good-index choices including c=y, zero-at-identity rank
    expansion, internal positive/negative admissibility, both indicator substitutions,
    parity of the gap, and the full zero-added-term argument for arbitrary threshold
    and lower bound.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# The native dihedral later-count difference

Fix a plane basis \(B\) in a finite-generator real Coxeter system and let \(D\) be its induced dihedral group. For an intrinsic edge \(e:x\to_Dy\), write \(\alpha_e\) for its actual plane edge root. Given an upper bound \(y\le_Dc\), the native later-edge counts satisfy
\[
h_D(x,\alpha_e;c)
=
h_D(y,\alpha_e;c)
+\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]
All counts and the correction are natural numbers. The length gap is a positive odd integer, so the quotient is an integer.

The same counts may be taken over a relative interval: for any \(a\le_Dx\), any \(c\in D\), and any positive ambient threshold root \(\alpha\),
\[
\sum_{z\in[a,c]_D}\varepsilon_D(x,\alpha,z)
=h_D(x,\alpha;c).
\]
Consequently the first identity holds when both sums are restricted to \([a,c]_D\), provided \(a\le_Dx\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**From actual root slopes to nonnegative endpoint counts.**

**OpenAI notes:** The later-edge lemma first transports a relative interval, then uses the midpoint-order table to calculate the difference of two outgoing counts. Its proof also treats reversal of the angular order by subtracting earlier and later edges from total outgoing counts. [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358), [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The native count is first defined over the full lower ideal in the induced dihedral group. Actual root comparisons are translated into signed indicators with explicit reduced-length and GoodIndex hypotheses. The two nonnegative counts are evaluated separately. interval_laterCount then removes zero terms to restrict either count to a relative interval. [DihedralIntervals:1852](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1852), [DihedralIntervals:1814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1814), [DihedralIntervals:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1833), [DihedralIntervals:1919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1919), [DihedralIntervals:1923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1923), [DihedralIntervals:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1948), [DihedralIntervals:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1974), [DihedralIntervals:2030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2030).

**Role in the proof:** The Blueprint gives the native count independently of interval transport, with the exact hypotheses of both indicator tables. Its slope orientation is the increasing orientation of the chosen PlaneBasis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose reduced admissible representatives

The [[node:kl.dihedral.signed_period|period-and-representative theorem]] supplies admissible signed indices \(i,j\) with
\[
w_i=x,\quad w_j=y,\qquad |i|=\ell_D(x),\quad |j|=\ell_D(y).
\]
Choose an admissible index \(k\) for \(c\) as follows.

If \(c=y\), take \(k=j\). Otherwise \(y\le_Dc\) and \(y\ne c\) imply \(\ell_D(y)<\ell_D(c)\). Choose any admissible reduced representative \(w_k=c\); it then satisfies \(|j|<|k|\).

Thus the exact top condition is
\[
k=j\quad\text{or}\quad |j|<|k|.
\]
The [[node:kl.dihedral.signed_reflection_action|signed edge criterion]] also gives \(|i|<|j|\) and odd \(i+j\).

### Step 2. Expand each lower-interval sum by ranks

Set \(C=|k|\). The [[node:kl.dihedral.lower_signed_sums|lower-interval signed-sum theorem]] says that for a function \(f\) with \(f(1)=0\),
\[
\sum_{z\le_Dw_k}f(z)
=f(w_k)+\sum_{n=0}^{C-1}\bigl(f(w_n)+f(w_{-n})\bigr).
\]
The top appears once. Positive ranks below \(C\) have two vertices. The two appearances of \(n=0\) contribute zero.

Apply this first to \(f(z)=\varepsilon_D(x,\alpha_e,z)\), and then to \(f(z)=\varepsilon_D(y,\alpha_e,z)\). The zero-at-identity assertion of the [[node:kl.dihedral.angular_indicator_tables|angular-indicator theorem]] verifies the required hypothesis in each case.

### Step 3. Check every index used in the indicator translation

The chosen \(j,k\) are admissible and reduced, so the [[node:kl.dihedral.angular_indicator_tables|angular-indicator theorem]] applies to the top terms.

For an internal rank \(0\le n<C=\ell_D(c)\), the [[node:kl.dihedral.signed_lengths|signed-length theorem]], using \(c\) as a witness, gives
\[
\ell_D(w_n)=n,\qquad \ell_D(w_{-n})=n.
\]
Both \(n\) and \(-n\) are admissible. Indeed, for any maximum length \(m\), one has \(n<C\le m\), hence
\(-m<-n\le0\le n<m\).
When lengths are unbounded the admissibility condition has no maximum-length element to test and holds for all indices.

All hypotheses of the same-source and next-source indicator formulas therefore hold at every term.

### Step 4. Identify the two numerical counts

Put \(q=i+j\). The [[node:kl.dihedral.angular_indicator_tables|actual angular-indicator theorem]] converts Step 2 into
\[
\begin{aligned}
h_D(x,\alpha_e;c)
&=\operatorname{aft}(i,q,k)
+\sum_{n=0}^{C-1}\bigl(\operatorname{aft}(i,q,n)+\operatorname{aft}(i,q,-n)\bigr)
=\operatorname{cnt}(i,q,k),\\
h_D(y,\alpha_e;c)
&=\operatorname{aft}(j,q,k)
+\sum_{n=0}^{C-1}\bigl(\operatorname{aft}(j,q,n)+\operatorname{aft}(j,q,-n)\bigr)
=\operatorname{cnt}(j,q,k).
\end{aligned}
\]
The final equalities are the definition of the finite signed count, including its singleton top.

These translations also establish the separate source lemmas `laterCount_same` and `laterCount_next`. The first requires admissibility of \(j,k\); the second requires only that of \(k\), in addition to the current edge and the three reduced-length identities.

### Step 5. Substitute the signed-count identity

The [[node:kl.dihedral.signed_count_difference|signed-count difference theorem]] requires a positive odd gap and the top condition from Step 1. Positivity follows from \(|i|<|j|\). Since \(|r|\equiv r\pmod2\) for every integer \(r\), odd \(i+j\) makes \(|j|-|i|\) odd.

That theorem gives
\[
\operatorname{cnt}(i,i+j,k)
=\operatorname{cnt}(j,i+j,k)+\frac{|j|-|i|-1}{2}.
\]
Substitute Step 4 and the lengths from Step 1 to obtain the stated native count difference.

### Step 6. Restrict a count to a relative interval

Let \(a\le_Dx\) and let \(\alpha\) be any positive ambient root. The set \([a,c]_D\) consists of those vertices of the lower interval of \(c\) which also satisfy \(a\le_Dz\).

For a removed vertex \(z\), suppose the indicator were nonzero. Its definition would give an upward edge \(x\to_Dz\), hence \(x\le_Dz\). Transitivity with \(a\le_Dx\) would give \(a\le_Dz\), contrary to the removal condition. Thus every removed term is zero.

The finite sums over the lower interval and over \([a,c]_D\) are therefore equal. For the count based at \(y\), use \(a\le_Dx\le_Dy\). Applying this restriction to both sides of the already proved difference completes the relative-interval form.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_same`: [DihedralIntervals.lean:1923](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1923).

`OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_next`: [DihedralIntervals.lean:1948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1948).

`OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference`: [DihedralIntervals.lean:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1974).

`OAI.KLInvariance.TitsSpace.PlaneBasis.afterIndicator_eq_zero`: [DihedralIntervals.lean:2022](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2022).

`OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount`: [DihedralIntervals.lean:2030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2030).
