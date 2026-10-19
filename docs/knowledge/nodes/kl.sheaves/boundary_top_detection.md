---
id: kl.sheaves.boundary_top_detection
title: Boundary-sheaf isomorphisms are detected at the normalized stalk
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.sheaves.boundary_image_identity
- kl.algebra.minimal_cover_maps
- kl.detail.sheaf_isomorphisms
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.edge_bijective_of_vertex
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.stalk_hom_bijective
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.homIso
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective_of_iso
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.homIsoOfIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:593
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.edge_bijective_of_vertex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:524
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.stalk_hom_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:654
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:678
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.homIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:748
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective_of_iso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:762
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.homIsoOfIso
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
- duality_and_characters
---

# Boundary-sheaf isomorphisms are detected at the normalized stalk

Let \(A\) be a connected nonnegatively graded Noetherian domain. Let \(G\) have finite vertex and edge sets, fixed labels, and a distinguished vertex \(b\). Let \(B,C\) be minimal-boundary sheaves with that normalization.

If a graded sheaf morphism \(f:B\to C\) has bijective component \(f_b\), then every vertex and edge component is bijective. Its components therefore define a graded sheaf isomorphism.

There is also a useful form with a previously recognized target. Suppose \(C\) is a graded sheaf with the same upper-quotient rule and there is a graded sheaf isomorphism \(j:B\to C\). Then any graded morphism \(f:B\to C\) bijective at \(b\) is itself an isomorphism.

*Proof.*

### Step 1. Pass bijectivity from an upper stalk to its edges

For an edge \(e:x\to y\), upper quotients identify
\[
B^e=B^y/\alpha_e B^y,\qquad C^e=C^y/\alpha_e C^y.
\]
If \(f_y\) is bijective, its linearity gives
\(f_y(\alpha_e B^y)=\alpha_e C^y\): one containment follows by moving the scalar through \(f_y\), and the other by applying its inverse.

It therefore induces a quotient isomorphism. The upper commuting square
\[
f_e\rho^{B,+}_e=\rho^{C,+}_e f_y
\]
identifies \(f_e\) with that quotient map, since \(\rho^{B,+}_e\) is surjective. Thus \(f_e\) is bijective.

### Step 2. Identify the two upper boundary images

Proceed by downward induction on the finite vertex poset. At \(b\), the desired vertex bijectivity is given. At \(x\ne b\), assume \(f_y\) bijective for every \(y>x\).

Step 1 gives bijective edge maps whenever the target is above \(x\). In particular they define a degree-zero isomorphism
\[
T_x:\prod_{e:\,s(e)=x}B^e
\xrightarrow{\sim}\prod_{e:\,s(e)=x}C^e.
\]

A compatible tuple on the strict upper set \(U_x=\{y:x<y\}\) maps to a compatible tuple by applying the \(f_y\). The inverse component maps give the inverse correspondence. In the ambient-assignment convention, extend these tuples by zero outside \(U_x\); the boundary maps read only the coordinates inside \(U_x\).

The upper commuting squares then give
\[
T_x(B^{\delta x})=C^{\delta x}.
\]
Hence \(T_x\) restricts to a graded isomorphism of the boundary images.

### Step 3. View the current stalk map as a map of minimal covers

Set \(T=C^{\delta x}\). Global generation and flabbiness make the two stalk maps onto their boundary images. Use Step 2 to put them over the same target:
\[
\pi:B^x\twoheadrightarrow T,\quad \pi=T_xr_x^B,
\qquad
\rho:C^x\twoheadrightarrow T,\quad \rho=r_x^C.
\]
Both sources are finite graded free. Because \(T_x\) is injective,
\(\ker\pi=\ker r_x^B\); likewise \(\ker\rho=\ker r_x^C\).
Minimality at \(x\ne b\) places these kernels in \(JB^x\) and \(JC^x\).

Thus \(\pi,\rho\) are minimal covers of the same module. The lower commuting squares give
\[
\rho f_x=T_xr_x^B=\pi.
\]
The [[node:kl.algebra.minimal_cover_maps|minimal-cover map theorem]] makes \(f_x\) bijective.

### Step 4. Complete the finite induction and assemble inverses

The argument at \(x\) uses only vertices strictly above it, so finite downward induction proves bijectivity at every vertex. Step 1 then proves bijectivity of every edge map.

Invert the component maps. The original commuting squares imply the inverse commuting squares by composition with these inverses. The inverse of each bijective degree-zero map preserves degree: decompose a preimage and use injectivity to eliminate components of all other degrees. The inverse components therefore form a graded sheaf morphism, giving the asserted isomorphism.

### Step 5. Treat a target already isomorphic to the boundary sheaf

For the second statement, put \(g=j^{-1}f:B\to B\). Its top component is a composite of bijections, so the first statement makes \(g\) a sheaf isomorphism.

Then \(f=jg\) is a composite of graded sheaf isomorphisms. Equivalently, all its stalk components are bijective; the shared upper-quotient rule and Step 1 also recover the edge bijections directly.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.edge_bijective_of_vertex`: [EdgeLocalization.lean:593](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L593).

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.stalk_hom_bijective`: [EdgeLocalization.lean:524](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L524).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective`: [EdgeLocalization.lean:654](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L654).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.homIso`: [EdgeLocalization.lean:678](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L678).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.hom_vertex_bijective_of_iso`: [EdgeLocalization.lean:748](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L748).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.homIsoOfIso`: [EdgeLocalization.lean:762](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L762).
