---
id: kl.paths.later_count
title: Later-edge counts in transported dihedral intervals
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.graph_invariance
- kl.foundations.rank_preservation
- kl.notes.relative_dihedral_transport
- kl.dihedral.good_indices
- kl.dihedral.signed_period
- kl.dihedral.lower_signed_sums
- kl.dihedral.signed_comparison_tables
- kl.dihedral.signed_residue_comparison
- kl.dihedral.signed_count_difference
- kl.dihedral.signed_lengths
- kl.dihedral.plane_coset_graph
- kl.dihedral.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table
  - OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference
  - OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount
  - OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1814
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1833
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:1974
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2030
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2064
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2145
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2200
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all
  - artifact: openai-kl-paper
    locator: 3. Later edges and the degree formula; dih:count
    format: section
    note: Transported endpoint counts and the signed-index computation.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Refined the full source setup and both rank cases of transported_count_difference_all.
    Replaced the compressed numerical table by the separately proved signed-count
    theorem, and corrected the finite-label description to odd residues with constrained
    Before comparisons. The detailed actual angular-root identification and full relative-interval
    transport remain tracked expository prerequisites for O3.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Later-edge counts in transported dihedral intervals

Fix finite-generator real Coxeter systems \(W,W'\), an interval order isomorphism
\[
\varphi:[u,b]_W\xrightarrow{\sim}[u',b']_{W'},
\]
and the geometric slope on the target positive roots.

In \(W\), choose a root plane with a plane basis, its induced dihedral group \(D\), and a representative \(a_0\) satisfying
\(\ell(a_0)\le\ell(da_0)\) for all \(d\in D\). Choose \(x\le_Dc\) with
\[
u\le_Wxa_0,\qquad ca_0\le_Wb,
\]
and an edge \(x\to_Dy\) with \(y\le_Dc\). The [[node:kl.dihedral.plane_coset_graph|least-coset order comparison]] puts \(za_0\) in \([u,b]_W\) for every \(z\in[x,c]_D\), so all the following values of \(\varphi\) are defined.

Let \(\alpha'\) be the positive target root of the image edge
\(\varphi(xa_0)\to\varphi(ya_0)\). Write \(\varepsilon(p,\alpha',q)\) for the target after-indicator: it is one exactly when \(p\to q\) is an upward reflection edge with root slope strictly greater than that of \(\alpha'\), and zero otherwise.

Define
\[
h_x=\sum_{z\in[x,c]_D}\varepsilon(\varphi(xa_0),\alpha',\varphi(za_0)),
\qquad
h_y=\sum_{z\in[x,c]_D}\varepsilon(\varphi(ya_0),\alpha',\varphi(za_0)).
\]
Then
\[
h_x=h_y+\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]
The intrinsic edge has a positive odd length gap, so the correction is a nonnegative integer.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**A full-interval reindexing followed by the signed count.**

**OpenAI notes:** The proof treats relative rank one separately, then transports the full relative interval to a target dihedral coset and applies the target angular count while preserving the relative length gap. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** The transport theorem returns coordinate equality, injectivity, full interval range, edge/order correspondence and relative length identities. These identify the actual target root and both finite sums. The small-rank branch proves there are exactly two vertices and checks each indicator is zero. [DihedralIntervals:2064](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2064), [DihedralIntervals:2145](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2145), [DihedralIntervals:2200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2200).

**Role in the proof:** The numerical calculation, actual angular-root comparison and full-interval transport are distinct inputs to the final identity. The Blueprint states the interval and coset bounds and separates finite root residues from the constrained raw signed comparisons.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport a relative interval of rank at least two

First suppose \(\ell_D(c)\ge\ell_D(x)+2\). The [[node:kl.notes.relative_dihedral_transport|full relative-interval transport theorem]] applies with the displayed ambient lower and upper bounds.

It supplies a target plane subgroup \(D'\), a least representative \(a'_0\), and a bijection \(F\) onto the full relative interval \([F(x),F(c)]_{D'}\). It preserves and reflects relative order and reflection edges, preserves length differences, and satisfies
\[
F(z)a'_0=\varphi(za_0)
\qquad(z\in[x,c]_D).
\]

The coordinate identity identifies the current target root with the intrinsic root of \(F(x)\to F(y)\): their left reflections are both
\[
\varphi(ya_0)\varphi(xa_0)^{-1}
=(F(y)a'_0)(F(x)a'_0)^{-1}
=F(y)F(x)^{-1}.
\]
The same identity identifies every root used in the two after-indicators.

### Step 2. Reindex the two sums and enlarge to a lower ideal

The full range and injectivity of \(F\) give a bijection of the finite interval index sets. Thus \(h_x,h_y\) become the actual target dihedral later counts based at \(F(x),F(y)\), over \([F(x),F(c)]_{D'}\).

They can also be summed over the full lower ideal \([1,F(c)]_{D'}\). A vertex outside the relative interval is not above \(F(x)\). An outgoing edge from either \(F(x)\) or \(F(y)\) would put its target above \(F(x)\), since \(F(x)\le F(y)\). Therefore every added term is zero. This is the interval_laterCount step.

### Step 3. Choose the signed representatives and compare labels

Choose admissible signed representatives \(i,j,k\) of
\(F(x),F(y),F(c)\), with their correct absolute lengths. If \(F(c)=F(y)\), choose \(k=j\); otherwise strict Bruhat length gives \(|j|<|k|\).

The edge criterion gives \(|i|<|j|\) and odd \(i+j\). At each internal rank \(0\le r<|k|\), the [[node:kl.dihedral.signed_lengths|signed-length theorem]] gives the correct lengths for \(w_r,w_{-r}\). If lengths are bounded, write \(m\) for the maximum length; then \(r<|k|\le m\) makes both indices admissible. In the unbounded case every index is admissible. The top index \(k\) and reference index \(j\) were chosen admissible.

The [[node:kl.dihedral.signed_reflection_action|signed edge criterion]] makes both indicators zero when the length or parity condition fails. In the remaining edge cases, the actual angular comparison lemmas identify the two endpoint indicators with
\[
\operatorname{aft}(i,i+j,z),\qquad
\operatorname{aft}(j,i+j,z)
\]
at each signed representative \(z\).

In the unbounded case the actual odd labels have the signed Before order. In the bounded case of maximum length \(m\), actual labels are ordered by their odd residues modulo \(2m\). The admissible vertex bounds and the [[node:kl.dihedral.signed_residue_comparison|finite-residue comparison theorem]] give the same Before tests for the same-source and next-source pairs used here.

The [[node:kl.dihedral.lower_signed_sums|lower-interval signed-sum theorem]] now identifies the two sums as
\[
h_x=\operatorname{cnt}(i,i+j,k),\qquad
h_y=\operatorname{cnt}(j,i+j,k).
\]
Its zero-at-identity hypothesis holds because an upward reflection edge cannot end at the identity.

### Step 4. Apply the complete numerical count

The [[node:kl.dihedral.signed_count_difference|signed-count difference theorem]] applies: the length gap is positive and odd, and the top satisfies \(k=j\) or \(|j|<|k|\). It gives
\[
h_x=h_y+\frac{|j|-|i|-1}{2}.
\]
The relative length-difference identity supplied by \(F\) gives
\[
|j|-|i|=\ell_D(y)-\ell_D(x).
\]
Substitution proves the required formula in this case.

### Step 5. Treat the smaller relative interval

Suppose \(\ell_D(c)<\ell_D(x)+2\). The edge and \(y\le_Dc\) force
\[
\ell_D(y)=\ell_D(c)=\ell_D(x)+1.
\]
Equal length under Bruhat comparison gives \(y=c\). Every vertex strictly between \(x\) and \(c\) would have an integer length strictly between these consecutive lengths, so the interval has exactly the two vertices \(x,y\).

For the lower count, the term at \(x\) is zero because it is not an upward edge, and the term at \(y\) is zero because the current edge has the threshold root itself. For the upper count, the term at \(y\) is again zero and the term at \(x\) cannot be upward. Thus both counts are zero.

The length correction is \((1-1)/2=0\), proving the identity in this final case.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_same_table`: [DihedralIntervals.lean:1814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1814).

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_next_table`: [DihedralIntervals.lean:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1833).

`OAI.KLInvariance.TitsSpace.PlaneBasis.laterCount_difference`: [DihedralIntervals.lean:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1974).

`OAI.KLInvariance.TitsSpace.PlaneBasis.interval_laterCount`: [DihedralIntervals.lean:2030](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2030).

`OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count`: [DihedralIntervals.lean:2064](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2064).

`OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference`: [DihedralIntervals.lean:2145](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2145).

`OAI.KLInvariance.TitsSpace.PlaneBasis.transported_count_difference_all`: [DihedralIntervals.lean:2200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2200).
