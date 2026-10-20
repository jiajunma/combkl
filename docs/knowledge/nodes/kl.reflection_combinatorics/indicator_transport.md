---
id: kl.dihedral.indicator_transport
title: Coset root identities and reindexing of actual later counts
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.ambient_after_indicator
- kl.dihedral.prefix_roots
- kl.dihedral.native_later_counts
- kl.dihedral.native_count_difference
- kl.dihedral.plane_coset_graph
- kl.foundations.interval
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset
  - OAI.KLInvariance.TitsSpace.PlaneBasis.ambientAfterIndicator_coset
  - OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2048
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2128
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.ambientAfterIndicator_coset
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:2064
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Checked exact left-label cancellation and both indicator branches. For
    reindexing, retained only injectivity and full interval range as hypotheses, constructed
    the actual finite bijection and derived the lower-bound comparison from range
    membership.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Coset root identities and reindexing of actual later counts

Fix a plane basis \(B\) in a finite-generator real Coxeter system \(W\), its induced dihedral group \(D\), and a least coset representative \(a_0\):
\[
\ell_W(a_0)\le\ell_W(da_0)\qquad(d\in D).
\]
Write \(\varepsilon_W\) for the ambient after-indicator, \(\varepsilon_D\) for the actual dihedral after-indicator, and \(h_D\) for the native later-edge count. For every intrinsic edge \(e:x\to_Dy\), its actual plane edge root equals the root of the ambient edge \(xa_0\to_Wya_0\). For every \(x,z\in D\) and every positive ambient root \(\alpha\),
\[
\varepsilon_W(xa_0,\alpha,za_0)=\varepsilon_D(x,\alpha,z).
\]

There is a separate finite-sum statement. Let \(B'\) be a plane basis in another finite-generator real Coxeter system \(W'\), with induced subgroup \(D'\). Fix \(a\le_Dc\), put \(J=[a,c]_D\), and suppose
\[
F:J\longrightarrow D'
\]
is injective and has the full range
\[
\operatorname{range}(F)=[F(a),F(c)]_{D'}.
\]
For any \(x\in J\) and any positive root \(\alpha'\) of \(W'\),
\[
\sum_{z\in J}\varepsilon_{D'}(F(x),\alpha',F(z))
=h_{D'}(F(x),\alpha';F(c)).
\]
If \(a'_0\) is a least representative for \(D'a'_0\), the same right side equals
\[
\sum_{z\in J}
\varepsilon_{W'}(F(x)a'_0,\alpha',F(z)a'_0).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Root equality and a bijection of the full interval index sets.**

**OpenAI notes:** The later-edge proof identifies the transported schedule with the actual target root order after identifying the target coset with its dihedral group. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464).

**Lean (primary):** edgeRoot_coset checks the unchanged left reflection under multiplication by the representative. The indicator equality treats edges and nonedges. interval_map_count constructs a bijection from injectivity and full range alone, reindexes the finite sum, and then uses the zero terms outside the relative interval to obtain the native lower-ideal count. [DihedralIntervals:2107](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2107), [DihedralIntervals:2048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2048), [DihedralIntervals:2128](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2128), [DihedralIntervals:2064](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2064).

**Role in the proof:** The Blueprint explains the actual threshold predicate, each root and indicator identity, and the finite reindexing map with their separate hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the coset edge root through its reflection

The [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] gives the ambient upward edge associated with \(e:x\to_Dy\). Its reflection is
\[
(ya_0)(xa_0)^{-1}
=ya_0a_0^{-1}x^{-1}
=yx^{-1}.
\]
This is exactly the reflection represented by the actual plane edge root of \(e\). The positive root representing a reflection is unique, so the roots are equal.

### Step 2. Compare both branches of the indicator

If \(x\to_Dz\), the [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] gives \(xa_0\to_Wza_0\), and Step 1 identifies their roots. Both indicators are one precisely when that common root has slope larger than \(\alpha\), and zero otherwise.

If \(x\to_Dz\) fails, the reverse implication of the [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] shows that \(xa_0\to_Wza_0\) also fails. Both indicators are zero. This proves their equality for all \(x,z\) and every threshold \(\alpha\).

### Step 3. Build a bijection of the finite interval index sets

For every \(z\in J\), the range identity gives
\[
F(a)\le_{D'}F(z)\le_{D'}F(c).
\]
Thus \(z\mapsto F(z)\) defines a map
\[
E:J\longrightarrow [F(a),F(c)]_{D'}.
\]
Injectivity follows from that of \(F\). For a vertex \(w\) of the target interval, the reverse containment in the range identity supplies \(z\in J\) with \(F(z)=w\). Hence \(E\) is surjective as well.

Both Bruhat intervals are finite, so reindexing the sum by this bijection gives
\[
\sum_{z\in J}\varepsilon_{D'}(F(x),\alpha',F(z))
=
\sum_{w\in[F(a),F(c)]_{D'}}
\varepsilon_{D'}(F(x),\alpha',w).
\]

### Step 4. Enlarge the relative interval to the full lower ideal

The range identity applied to \(x\) gives \(F(a)\le_{D'}F(x)\). The relative-interval part of the [[node:kl.dihedral.native_count_difference|native count-difference theorem]] therefore applies with lower bound \(F(a)\), source \(F(x)\), top \(F(c)\), and threshold \(\alpha'\).

It says that the last sum in Step 3 equals
\(h_{D'}(F(x),\alpha';F(c))\):
every vertex removed from the full lower ideal is not above \(F(a)\), so it cannot be the target of an edge from \(F(x)\). This proves the finite-sum statement.

### Step 5. Return to ambient target vertices

Apply Step 2 in \(W'\) with least representative \(a'_0\), separately at each source \(F(x)\) and target \(F(z)\). It identifies every summand of the final displayed ambient sum with the intrinsic summand in Step 3. Their sums are equal, completing the last assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.edgeRoot_coset`: [DihedralIntervals.lean:2048](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2048).

`OAI.KLInvariance.TitsSpace.PlaneBasis.ambientAfterIndicator_coset`: [DihedralIntervals.lean:2128](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2128).

`OAI.KLInvariance.TitsSpace.PlaneBasis.interval_map_count`: [DihedralIntervals.lean:2064](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L2064).
