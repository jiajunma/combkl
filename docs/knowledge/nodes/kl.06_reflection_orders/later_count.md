---
id: kl.paths.later_count
title: Later-edge counts in transported dihedral intervals
kind: theorem
status: proved
primary_topic: kl.06_reflection_orders
topics:
- kl.06_reflection_orders
uses:
- kl.paths.graph_invariance
- kl.foundations.rank_preservation
- kl.notes.relative_dihedral_transport
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2200
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; sec:dihedral
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
- dihedral
---

# Later-edge counts in transported dihedral intervals

Fix a root plane in a real realization, a minimal representative of its dihedral coset, and a relative interval lying in the ambient interval being compared. For an edge \(x\to y\), compare its labels through the target system's reflection order. If \(h_x,h_y\) count the relative upward edges strictly later than this edge at the two endpoints, then
\[
h_x-h_y=\frac{\ell_D(y)-\ell_D(x)-1}{2},
\]
where \(\ell_D\) is the relative dihedral length.

*Proof.*

### Step 1. Reduce the transported count to one genuine target dihedral interval

For relative rank at least two, use the full interval transport theorem. It supplies a bijection onto a target dihedral interval, preserving relative length differences and actual reflection edges. The coordinate equality \(F(z)a'=\phi(za_0)\) identifies the target root label of each transported edge, not just its incidence.

Therefore the two sums of later-edge indicators in the statement equal the corresponding later counts in this target interval. Surjectivity of the range is essential: without it, a count could omit target vertices.

### Step 2. Write the signed-index rule

Index target dihedral elements by integers, with length \(|i|\). An edge \(i\to j\) has \(|i|<|j|\), odd \(|i|+|j|\), and reflection parameter \(i+j\). The angular order lists positive odd parameters increasingly, followed by negative odd parameters increasingly. Denote this comparison by \(\prec\).

For an endpoint \(a\), a vertex \(z\) contributes to the later count exactly when
\[
|a|<|z|,\qquad a+z\text{ is odd},\qquad i+j\prec a+z.
\]
A lower ideal has two elements in each internal positive rank and a single top \(c\). Its count is consequently the sum of these indicators at \(z=r,-r\), for \(r<|c|\), plus the indicator at \(c\).

### Step 3. Evaluate the two possible sign cases

Put \(L=|i|\), \(M=|j|\), \(C=|c|\), and \(k=(M-L-1)/2\). The edge parity says \(M-L=2k+1\).
Among the ranks strictly between \(L\) and \(M\), the eligible ranks are
\[
L+1,L+3,\ldots,L+2k-1;
\]
the map \(a\mapsto L+1+2a\), \(0\le a<k\), is a bijection, so there are \(k\).

Substitution in the signed comparison gives the following exact counts:
\[
\begin{array}{c|cc}
&h_i&h_j\\
j>0&k+(C-M)&C-M\\
j<0&k&0.
\end{array}
\]
For \(j>0\), each eligible rank beyond \(M\) contributes its two opposite-sign vertices; the possible singleton top completes this alternating-parity count to \(C-M\). For \(j<0\), the signed angular inequality excludes all those later ranks. At ranks between \(L\) and \(M\), precisely one vertex contributes to the lower count and none to the upper count. The distinguished edge itself is excluded by strictness.

The tail term \(C-M\) can also be checked without an ellipsis. For the upper endpoint, if \(C-M=2s\), there are \(s\) eligible internal ranks contributing two vertices each and no top contribution, giving \(2s\). If \(C-M=2s+1\), there are \(s\) such ranks plus the singleton top, giving \(2s+1\). For the lower endpoint with \(j>0\) and \(C>M\), the formerly excluded partner at rank \(M\) contributes one. An even difference gives \(1+2(s-1)+1=2s\); an odd difference gives \(1+2s=2s+1\). The \(k\) contributions below rank \(M\) are unchanged.

Subtracting either row therefore gives \(h_i-h_j=k\).

### Step 4. Handle the small relative interval separately

If the source relative interval has rank below two but contains the specified edge, its rank is one. Its only vertices are the lower endpoint and that edge's upper endpoint. No strictly later upward edge occurs at either vertex, so both counts are zero, and \((1-1)/2=0\).

### Step 5. Transport the integer result back

For larger rank, Step 1 identifies the counts, and relative rank preservation identifies
\(M-L=\ell_D(y)-\ell_D(x)\).
Thus Step 3 gives exactly the stated formula. This uses the target system's genuine angular order, even when its transported ordering is not itself a reflection order in the source system.

## References

[3. Dihedral intervals and transported reflection orders](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all`: [DihedralIntervals.lean:2200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2200).
