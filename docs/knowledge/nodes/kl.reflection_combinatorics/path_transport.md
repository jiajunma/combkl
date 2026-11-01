---
id: kl.paths.path_transport
title: Graph maps and local label comparisons transport selected paths
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.paths.directed_paths
- kl.paths.sorted_path_selection
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.SchedulePaths.IsPath.map
  - OAI.KLInvariance.SchedulePaths.IsPath.isChain
  - OAI.KLInvariance.SchedulePaths.IsPath.pairwise_map_of_local
  - OAI.KLInvariance.SchedulePaths.subpaths_map_of_sorted
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1659
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.IsPath.map
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1670
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.IsPath.isChain
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1684
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.IsPath.pairwise_map_of_local
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1828
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.subpaths_map_of_sorted
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the graph, scalar, list, label-order and interval hypotheses explicit,
    with the exact path sets and source proof?
  verdict: Read IsPath.map, its adjacent-incidence proof, pairwise_map_of_local and
    the exact same-graph sorted-schedule specialization. Retained arbitrary graph
    maps, linearly ordered labels, target fullness, source tie hypothesis and fixed
    endpoints.
tags:
- Kazhdan-Lusztig
- reflection_orders
---

# Graph maps and local label comparisons transport selected paths

Let \(V,E\) and \(V',E'\) be directed graphs with endpoint maps \(s,r\) and \(s',r'\). A pair of maps \(f:V\to V'\), \(g:E\to E'\) preserves endpoints when
\[
s'(g(e))=f(s(e)),\qquad r'(g(e))=f(r(e))
\quad(e\in E).
\tag{1}
\]
It then sends every directed path \(q\) from \(x\) to \(y\) to the edgewise image \(g(q)\), a path from \(f(x)\) to \(f(y)\).

Let \(\lambda:E\to\Lambda\), \(\lambda':E'\to\Lambda'\) be labels in linearly ordered sets. Suppose
\[
r(e)=s(h),\ \lambda(e)<\lambda(h)
\quad\Longrightarrow\quad
\lambda'(g(e))<\lambda'(g(h)).
\tag{2}
\]
Then \(g(q)\) has strictly increasing labels whenever \(q\) is a strictly increasing directed path. The corresponding conclusion holds with all label orders reversed.

The sorted-schedule application uses one graph \(V,E\), real labels \(\lambda,\lambda'\), schedules \(p,p'\), and maps \(f:V\to V\), \(g:E\to E\). Assume:

- \(p\) is weakly decreasing for \(\lambda\), and \(p'\) is weakly decreasing for \(\lambda'\);
- every edge of \(E\) occurs in \(p'\);
- equal \(\lambda\)-labels cannot occur on composable edges;
- (1) holds, and \(f(x)=x\), \(f(y)=y\);
- for composable \(e,h\), \(\lambda(h)<\lambda(e)\) implies \(\lambda'(g(h))<\lambda'(g(e))\).

Then
\[
q\in\mathcal P_p(x,y)\quad\Longrightarrow\quad
g(q)\in\mathcal P_{p'}(x,y).
\tag{3}
\]
This is the source's `subpaths_map_of_sorted`.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Local comparisons determine the selected path transport.**

**OpenAI notes:** The notes use strict reflection-label paths and observe that equal-label reflection edges are disjoint. Relative graph identifications transport the underlying directed edges. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185), [dih:relative-paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L148).

**Lean (primary):** The list lemmas separate weak sorting, strict path order and sublist recovery. A graph map transports incidence, and comparisons only on composable adjacent edges imply the full strict order on a mapped path. An edge involution with both path-membership directions preserves lengths and reindexes the two finite path sums. [ReflectionSchedules:1233](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1233), [ReflectionSchedules:1260](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1260), [DyerPaths:1659](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1659), [DyerPaths:1684](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1684), [DyerPaths:1828](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1828), [DyerPaths:1803](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1803).

**Role in the proof:** Each map, membership condition and order hypothesis is explicit. The path-set transport supplies the finite bijection used in the root-plane reversal calculation.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Preservation of the path predicate

For the empty path, \(x=y\); applying \(f\) gives \(f(x)=f(y)\), the empty-path condition in the target graph.

For \(q=e::h\), the path predicate gives \(s(e)=x\) and a path \(h\) from \(r(e)\) to \(y\). The induction hypothesis maps this tail to a path from \(f(r(e))\) to \(f(y)\). By (1), its first endpoint is \(r'(g(e))\), while \(s'(g(e))=f(s(e))=f(x)\). The path recursion therefore joins \(g(e)\) to the mapped tail and gives the desired path from \(f(x)\) to \(f(y)\).

### Step 2. Local comparisons on adjacent edges

Write a nonempty path as \([e_1,\ldots,e_m]\). Its path predicate gives
\(r(e_i)=s(e_{i+1})\) for every adjacent pair.
If its labels are strictly increasing, (2) therefore gives
\[
\lambda'(g(e_i))<\lambda'(g(e_{i+1}))
\quad(1\le i<m).
\]
For \(i<j\), transitivity along the finite chain from \(i\) to \(j\) gives the comparison of those two mapped labels. Explicitly, induction on \(j-i\) starts with the adjacent case; the longer case combines the comparison up to \(j-1\) with the last adjacent comparison. Empty and singleton lists have no comparisons to prove.

Thus the image list is pairwise strictly increasing. The same argument with \(>\) throughout proves the decreasing-label version used below.

### Step 3. Strictness of a selected source path

Suppose \(q\in\mathcal P_p(x,y)\). It is a sublist of \(p\) and a directed path. Weak decrease of \(p\) restricts to \(q\). The equal-label noncomposability hypothesis and the [[node:kl.paths.sorted_path_selection|sorted-path selection theorem]] make \(q\) strictly decreasing for \(\lambda\).

### Step 4. The mapped path and its strict labels

Step 1 maps \(q\) to a path from \(f(x)\) to \(f(y)\). The fixed-endpoint assumptions make these vertices \(x,y\).
Apply the decreasing version of Step 2 to the stated local comparison hypothesis. This makes \(g(q)\) strictly decreasing for \(\lambda'\).

### Step 5. Recovery of the target sublist

Every edge of \(g(q)\) occurs in \(p'\), because \(p'\) contains every edge of \(E\). The target schedule is weakly decreasing for \(\lambda'\), and \(g(q)\) is strict. The sublist part of the [[node:kl.paths.sorted_path_selection|sorted-path selection theorem]] therefore gives
\[
g(q)\preceq_{\mathrm{sub}}p'.
\]
Together with the mapped path from Step 4, this proves (3). The graph-map equations control incidence; the adjacent comparison hypothesis controls label order; and fullness of \(p'\) supplies membership in the target schedule.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.SchedulePaths.IsPath.map`: [DyerPaths.lean:1659](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1659).

`OAI.KLInvariance.SchedulePaths.IsPath.isChain`: [DyerPaths.lean:1670](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1670).

`OAI.KLInvariance.SchedulePaths.IsPath.pairwise_map_of_local`: [DyerPaths.lean:1684](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1684).

`OAI.KLInvariance.SchedulePaths.subpaths_map_of_sorted`: [DyerPaths.lean:1828](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1828).
