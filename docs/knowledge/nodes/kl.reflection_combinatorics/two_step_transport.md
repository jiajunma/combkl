---
id: kl.dihedral.two_step_transport
title: Exact two-edge intermediate sets survive interval transport
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.two_step_planes
- kl.dihedral.relative_rank_fibers
- kl.dihedral.coset_interval_embedding
- kl.dihedral.plane_coset_graph
- kl.paths.graph_invariance
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_two_step_rank_two
  - OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_interval_iff
  - OAI.KLInvariance.intervalIso_twoStep_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:302
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_two_step_rank_two
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:687
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_interval_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:634
    format: lean-location
    note: OAI.KLInvariance.intervalIso_twoStep_iff
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: Checked all ambient intermediates, coset confinement, the least-representative
    graph equivalence, relative-interval membership, and the general arbitrary-generator
    interval-isomorphism transport by inverse images.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Exact two-edge intermediate sets survive interval transport

Fix a plane basis \(B\) in a finite-generator real Coxeter system \(W\), its induced group \(D\), and a least coset representative \(a_0\), meaning
\(\ell_W(a_0)\le\ell_W(da_0)\) for all \(d\in D\).

If \(x,y\in D\) satisfy \(\ell_D(y)=\ell_D(x)+2\), there are distinct \(a,c\in D\) such that, for every ambient vertex \(z\in W\),
\[
xa_0\to_W z\to_Wya_0
\quad\Longleftrightarrow\quad
z=aa_0\text{ or }z=ca_0.
\]
If \(x,y\) belong to a relative interval \(J=[g,k]_D\), the two vertices \(a,c\) belong to \(J\) as well.

There is also a general transport assertion. Let
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\)
be an interval order isomorphism between arbitrary Coxeter systems. Suppose \(x,y,a,c\in[u,b]_W\) satisfy
\[
x\to_W z\to_Wy\quad\Longleftrightarrow\quad z=a\text{ or }z=c
\qquad(z\in W).
\]
Then, for every \(z'\in W'\),
\[
\varphi(x)\to_{W'}z'\to_{W'}\varphi(y)
\quad\Longleftrightarrow\quad
z'=\varphi(a)\text{ or }z'=\varphi(c).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Exact intermediates and the three-vertex contradiction.**

**OpenAI notes:** The interval-shape lemma counts exactly r two-edge paths when the positive relative length gap r is even. The transport proof uses the equality of ambient intermediate sets to conclude that the target gap is two. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:relative-paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L148), [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The native gap-two result lists two intermediates. For the converse, a gap at least four produces two distinct vertices one rank above the bottom and a third three ranks above it. All three are two-edge intermediates, contradicting the assumed two-value bound. Ambient interval membership then permits inverse transport of every target intermediate. [ReflectionSchedules:1717](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1717), [ReflectionSchedules:1673](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1673), [DyerPaths:302](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L302), [DyerPaths:341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L341), [DyerPaths:634](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L634).

**Role in the proof:** The Blueprint follows the three-intermediate contradiction and proves the ambient and transported intermediate-set equivalences in both directions.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose the two intrinsic intermediates

The [[node:kl.dihedral.relative_rank_fibers|relative-rank fiber theorem]] gives distinct \(a,c\) with
\[
x\to_Dd\to_Dy\quad\Longleftrightarrow\quad d=a\text{ or }d=c.
\]
The [[node:kl.dihedral.plane_coset_graph|least-coset graph theorem]] turns their two paths into ambient paths through \(aa_0\) and \(ca_0\). The two products remain distinct by right cancellation.

If \(x,y\in J\), each \(d\in\{a,c\}\) satisfies
\(g\le_Dx<_Dd<_Dy\le_Dk\), so both intermediates belong to \(J\).

### Step 2. Recover every ambient intermediate in the same coset

Take an arbitrary path \(xa_0\to_Wz\to_Wya_0\). One of the paths from Step 1, for example through \(aa_0\), is entirely in \(Da_0\). The [[node:kl.dihedral.two_step_planes|two-edge coset-confinement theorem]] gives
\(d=za_0^{-1}\in D\).
Then \(da_0=z\).

Using the [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] on both edges gives \(x\to_Dd\to_Dy\). Step 1 forces \(d=a\) or \(d=c\), hence \(z=aa_0\) or \(z=ca_0\). Conversely each of those two products is already the intermediate of an ambient path. This proves the first assertion over all of \(W\).

### Step 3. Put every target intermediate inside the ambient target interval

For the general transport assertion, suppose
\(\varphi(x)\to_{W'}z'\to_{W'}\varphi(y)\).
Each edge is a Bruhat comparison. Since \(\varphi(x),\varphi(y)\in[u',b']\), transitivity gives
\[
u'\le_{W'}\varphi(x)\le_{W'}z'
\le_{W'}\varphi(y)\le_{W'}b'.
\]
Thus \(\varphi^{-1}(z')\) is defined.

### Step 4. Pull back both edges and use the exact source set

The [[node:kl.paths.graph_invariance|reflection-graph invariance theorem]] preserves and reflects edges under an interval order isomorphism. It gives
\[
x\to_W\varphi^{-1}(z')\to_Wy.
\]
The assumed source equivalence makes \(\varphi^{-1}(z')\) equal to \(a\) or \(c\). Applying \(\varphi\) gives the required two target possibilities.

Conversely, the source equivalence gives both edges through \(a\) and through \(c\). Graph invariance sends them to the two target paths. This proves the target equivalence in both directions.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.ambient_two_step_rank_two`: [DyerPaths.lean:302](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L302).

`OAI.KLInvariance.TitsSpace.PlaneBasis.twoStep_interval_iff`: [DyerPaths.lean:687](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L687).

`OAI.KLInvariance.intervalIso_twoStep_iff`: [DyerPaths.lean:634](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L634).
