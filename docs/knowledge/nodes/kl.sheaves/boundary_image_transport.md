---
id: kl.sheaves.boundary_image_transport
title: Boundary and stalk images under an isomorphism above a vertex
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_isomorphisms
- kl.detail.compatible_sections
- kl.sheaves.boundary_image_identity
- kl.sheaves.graph_sheaf
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.symm
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment_at
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.compatible
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundary
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundaryMap
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_boundaryImage
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_stalk_image
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:704
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.symm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:714
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:719
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment_at
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:724
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:732
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundary
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:735
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundaryMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:743
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_boundaryImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:756
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_stalk_image
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read AboveIso.mapAssignment, compatible, boundary, boundaryMap, map_boundaryImage
    and map_stalk_image. Kept the zero extension outside the strict upper set and
    proved both image containments, without claiming an isomorphism of the full assignment
    modules.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Boundary and stalk images under an isomorphism above a vertex

Let \(R\) be a commutative ring, \(G\) an ordered graph, \(B,C\) sheaves on \(G\), and \(x\) a vertex. Suppose \(j\) is an isomorphism above \(x\): it gives vertex isomorphisms \(j_y:B^y\simeq C^y\) for \(y>x\), edge isomorphisms \(j_e:B^e\simeq C^e\) when \(t(e)>x\), and the corresponding restriction squares.

Let
\[
\Delta_x(B)=\prod_{e:s(e)=x}B^e
\]
be the boundary module. The product of the outgoing edge isomorphisms gives
\[
J:\Delta_x(B)\xrightarrow{\sim}\Delta_x(C).
\]
Then \(J\) carries the upper-section boundary image of \(B\) onto that of \(C\).

If both sheaves are globally generated and flabby, it also carries the outgoing stalk image onto the outgoing stalk image:
\[
J(\operatorname{im}d_x^B)=\operatorname{im}d_x^C,
\]
where \(d_x^B(v)=(\rho^{B,-}_e(v))_{s(e)=x}\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same descent with explicit upper-endpoint edge data.**

**OpenAI notes:** The proof descends through the relative coset vertices, splits the current stalk over the existing boundary image, adds copies of the model centered there and retains both endpoint restrictions. Incoming edge identifications are supplied when their lower vertices are processed, using the upper quotient rule. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The generic local-ring theorem maintains an OnIso on the processed upper set, already including all edges whose upper endpoints have been processed. A maximal unprocessed vertex is added by a finite free kernel block. The new incoming edge maps are induced from the new upper-stalk isomorphism, and strong induction on the remaining finite vertex set gives a full Iso. The boundary-sheaf localization theorem verifies the five sheaf hypotheses and supplies the actual cosetModels. [GradedSheaves:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756), [PlaneLocalization:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147), [PlaneLocalization:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207), [TerminalKernels:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).

**Role in the proof:** The Blueprint follows the Lean invariant: an edge isomorphism is supplied when its upper endpoint is processed, and its lower restriction square is checked when its lower endpoint is processed. The notes describe incoming-edge identifications later in the descent. The generic Lean theorem uses a finite vertex set; the final application supplies the actual localized coset modules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport an assignment on the strict upper set

For an assignment \(f\) of \(B\), define
\[
(T_jf)_y=
\begin{cases}
j_y(f_y),&y>x,\\
0,&y\not>x.
\end{cases}
\]
This is the source's mapAssignment. Values outside the strict upper set are set to zero; only values above \(x\) enter the boundary calculation.

Suppose \(f\) is compatible on \(U_x=\{y:y>x\}\). For an edge with both endpoints in \(U_x\), the restriction squares give
\[
\rho^{C,-}_e(j_{s(e)}f_{s(e)})
=j_e(\rho^{B,-}_e f_{s(e)})
=j_e(\rho^{B,+}_e f_{t(e)})
=\rho^{C,+}_e(j_{t(e)}f_{t(e)}).
\]
Thus \(T_jf\) is compatible on \(U_x\).

### Step 2. Write the boundary coordinate map

Every outgoing edge from \(x\) has target strictly above \(x\). Hence its edge isomorphism is available, and
\[
J((v_e)_e)=(j_e(v_e))_e
\]
is defined. Its inverse applies \(j_e^{-1}\) in each coordinate.

The boundary value of a section \(f\) on \(U_x\) is
\[
\beta_x^B(f)=(\rho^{B,+}_e(f_{t(e)}))_e.
\]
For each outgoing edge, the upper restriction square gives
\[
j_e(\rho^{B,+}_e(f_{t(e)}))
=\rho^{C,+}_e(j_{t(e)}(f_{t(e)})).
\]
Therefore
\[
J\beta_x^B(f)=\beta_x^C(T_jf).
\]

### Step 3. Prove equality of the two boundary images

Step 2 shows that \(J\) maps every boundary value from \(B\) to a boundary value from \(C\).

For the reverse containment, start with a compatible assignment \(h\) above \(x\) in \(C\). Apply the inverse vertex maps above \(x\), putting zero elsewhere, to obtain \(T_{j^{-1}}h\). The same restriction-square calculation proves compatibility.

For each outgoing edge,
\[
j_e\bigl(\rho^{B,+}_e(j_{t(e)}^{-1}h_{t(e)})\bigr)
=\rho^{C,+}_e(h_{t(e)}).
\]
Thus the boundary value of \(h\) is the \(J\)-image of the boundary value of \(T_{j^{-1}}h\). This proves the reverse containment.

### Step 4. Replace boundary images by stalk images

Assume both sheaves are generated and flabby. The [[node:kl.sheaves.boundary_image_identity|boundary-image identity theorem]] gives
\[
\operatorname{im}d_x^B=\operatorname{im}\beta_x^B,\qquad
\operatorname{im}d_x^C=\operatorname{im}\beta_x^C.
\]
Generation supplies one inclusion by extending a stalk value to a global section. Flabbiness supplies the other by extending an upper-set section and taking its value at \(x\).

Substitute these identities into Step 3. This gives
\(J(\operatorname{im}d_x^B)=\operatorname{im}d_x^C\), the common image used in the local stalk splitting.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.symm`: [GradedSheaves.lean:704](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L704).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment`: [GradedSheaves.lean:714](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L714).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.mapAssignment_at`: [GradedSheaves.lean:719](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L719).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.compatible`: [GradedSheaves.lean:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L724).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundary`: [GradedSheaves.lean:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L732).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.boundaryMap`: [GradedSheaves.lean:735](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L735).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_boundaryImage`: [GradedSheaves.lean:743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L743).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.map_stalk_image`: [GradedSheaves.lean:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756).
