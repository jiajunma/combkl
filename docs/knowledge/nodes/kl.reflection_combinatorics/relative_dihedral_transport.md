---
id: kl.notes.relative_dihedral_transport
title: Full transport of a relative dihedral interval
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.coset_interval_embedding
- kl.dihedral.image_plane_coset
- kl.dihedral.two_step_transport
- kl.dihedral.relative_rank_fibers
- kl.dihedral.affine_rank_preservation
- kl.dihedral.full_interval_range
- kl.dihedral.plane_basis_existence
- kl.dihedral.minimal_plane_cosets
- kl.dihedral.plane_coset_graph
- kl.paths.graph_invariance
- kl.dihedral.odd_reflection_edges
- kl.coxeter.dihedral_bruhat_order
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:736
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval
  - artifact: openai-kl-paper
    locator: 3. Dihedral intervals and transported reflection orders; dih:transport
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient/coset domains, intrinsic ranks, injectivity, full-range
    and exact-intermediate hypotheses explicit?
  verdict: 'Replaced the compressed transport explanation with the exact source hypotheses
    and all returned data: plane/basis, least target representative, injection, coordinate
    identity, order/edge equivalences, affine ranks and full range. Checked every
    application through explicit intermediate-set transport and rank-two detection.'
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Full transport of a relative dihedral interval

Fix finite-generator real Coxeter systems \(W,W'\) and an interval order isomorphism
\[
\varphi:[u,b]_W\xrightarrow{\sim}[u',b']_{W'}.
\]
In \(W\), choose a plane basis \(B\), its induced dihedral subgroup \(D\), and a least coset representative \(a_0\), so that
\(\ell_W(a_0)\le\ell_W(da_0)\) for every \(d\in D\).
Choose \(g,k\in D\) satisfying
\[
g\le_Dk,\qquad \ell_D(g)+2\le\ell_D(k),\qquad
u\le_Wga_0,\qquad ka_0\le_Wb.
\]
Let \(J=[g,k]_D\), and use the coset interval embedding to interpret \(\varphi(za_0)\) for \(z\in J\).

There exist a target root plane \(P'\), a plane basis \(B'\) for it, its induced subgroup \(D'\), a least representative \(a'_0\) for the target coset, and an injective map
\[
F:J\longrightarrow D'
\]
with the following properties:
\[
\begin{aligned}
F(z)a'_0&=\varphi(za_0),\\
F(x)\le_{D'}F(y)&\Longleftrightarrow x\le_Dy,\\
F(x)\to_{D'}F(y)&\Longleftrightarrow x\to_Dy,\\
\ell_{D'}(F(z))+\ell_D(g)&=\ell_{D'}(F(g))+\ell_D(z),\\
\operatorname{range}(F)&=[F(g),F(k)]_{D'}.
\end{aligned}
\]
Here \(x,y,z\in J\), and least means
\[
\ell_{W'}(a'_0)\le\ell_{W'}(d'a'_0)\qquad(d'\in D').
\]
Thus the ambient image is the entire relative target interval in \(D'a'_0\), with exact coordinates and relative length differences.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit coordinates, affine lengths and full target range.**

**OpenAI notes:** The proposition describes the image directly as a full relative interval in a target plane coset. Its proof recovers covers from rank-two intervals and exhausts each internal target rank with two image vertices. [dih:transport](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L276).

**Lean (primary):** The construction chooses a least target representative and writes F(z) as the ambient image multiplied on the right by its inverse. Rank-two preservation gives consecutive-rank preservation, then an affine length identity by induction. Injectivity and the two-element internal ranks give the exact full range. The theorem returns all coordinate, order, edge and length properties explicitly. [DyerPaths:676](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L676), [DyerPaths:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L504), [DyerPaths:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L536), [DyerPaths:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L567), [DyerPaths:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).

**Role in the proof:** The Blueprint uses the intrinsic coordinate map F and retains every ambient endpoint bound. The source and target bottom lengths may differ by the constant prescribed by the affine identity.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compose the coset embedding with the given isomorphism

Define
\[
f:J\to W',\qquad f(z)=\varphi(za_0).
\]
The coset interval embedding proves that each argument \(za_0\) lies in \([u,b]_W\). It is injective by right cancellation, and \(\varphi\) is injective, so \(f\) is injective.

If \(x\to_Dy\), the source [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] gives \(xa_0\to_Wya_0\). The [[node:kl.paths.graph_invariance|reflection-graph invariance theorem]] then gives \(f(x)\to_{W'}f(y)\). Thus \(f\) preserves every directed reflection edge of \(J\).

### Step 2. Construct the target plane and a least coset coordinate

The [[node:kl.dihedral.image_plane_coset|image-plane theorem]] applies because \(J\) has relative rank at least two. It supplies distinct positive roots \(\alpha,\beta\) and a plane \(P'=P(\alpha,\beta)\) such that
\[
f(z)f(g)^{-1}\in D'\qquad(z\in J),
\]
where \(D'\) is the plane subgroup.

The [[node:kl.dihedral.plane_basis_existence|plane-basis existence theorem]] supplies \(B'\), giving \(D'\) its intrinsic dihedral Coxeter system. The [[node:kl.dihedral.minimal_plane_cosets|least-coset representative theorem]] supplies \(a'_0\) and \(g_0\in D'\) with
\[
f(g)=g_0a'_0,\qquad
\ell_{W'}(a'_0)\le\ell_{W'}(d'a'_0)\quad(d'\in D').
\]
For every \(z\),
\[
f(z)(a'_0)^{-1}
=f(z)f(g)^{-1}g_0\in D'.
\]
Define \(F(z)\) to be this subgroup element. Multiplication gives the coordinate identity \(F(z)a'_0=f(z)\).

If \(F(x)=F(y)\), multiplication by \(a'_0\) gives \(f(x)=f(y)\), hence \(x=y\). Thus \(F\) is injective.

### Step 3. Preserve intrinsic edges in the target coordinates

Step 1 gives the ambient edge \(f(x)\to_{W'}f(y)\) whenever \(x\to_Dy\). Substitute \(f(x)=F(x)a'_0\) and \(f(y)=F(y)a'_0\).

The target representative is least, so the target [[node:kl.dihedral.plane_coset_graph|coset graph theorem]] turns this ambient edge into the intrinsic edge \(F(x)\to_{D'}F(y)\). This supplies the edge-preservation hypothesis for the rank arguments below.

### Step 4. Transport an exact rank-two intermediate set

Take \(x,y\in J\) with \(\ell_D(y)=\ell_D(x)+2\). The [[node:kl.dihedral.two_step_transport|two-step transport theorem]] gives distinct \(a,c\in J\) such that all ambient source two-edge paths from \(xa_0\) to \(ya_0\) have precisely the intermediates \(aa_0,ca_0\).

Its interval-isomorphism assertion therefore gives, for every \(z'\in W'\),
\[
f(x)\to_{W'}z'\to_{W'}f(y)
\quad\Longleftrightarrow\quad
z'=f(a)\text{ or }z'=f(c).
\]
The known path through \(f(a)\) becomes an intrinsic path
\(F(x)\to_{D'}F(a)\to_{D'}F(y)\)
by the target [[node:kl.dihedral.plane_coset_graph|coset graph theorem]].

### Step 5. Recover target gap two

Consider any intrinsic intermediate \(d'\) with
\(F(x)\to_{D'}d'\to_{D'}F(y)\).
Multiplying by \(a'_0\) gives an ambient path through \(d'a'_0\). Step 4 forces
\[
d'a'_0=f(a)=F(a)a'_0
\quad\text{or}\quad
d'a'_0=f(c)=F(c)a'_0.
\]
Right cancellation gives \(d'=F(a)\) or \(d'=F(c)\).

There is a path through \(F(a)\), and every intermediate lies in a set of at most two elements. The [[node:kl.dihedral.relative_rank_fibers|rank-two detection theorem]] therefore gives
\[
\ell_{D'}(F(y))=\ell_{D'}(F(x))+2.
\]
Its three-intermediate contradiction verifies this for every source pair of gap two.

### Step 6. Recover all relative ranks and orders

The [[node:kl.dihedral.affine_rank_preservation|affine-rank theorem]] applies to Step 3, Step 5 and the total source rank assumption. It gives
\[
\ell_{D'}(F(z))+\ell_D(g)=\ell_{D'}(F(g))+\ell_D(z)
\qquad(z\in J).
\]
Subtracting the identities for \(x,y\) preserves their length difference.

The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]] describes order as strict length comparison or equality. The affine identity preserves the first alternative, and injectivity preserves and reflects the second. Hence \(F(x)\le_{D'}F(y)\) exactly when \(x\le_Dy\).

### Step 7. Reflect edges and exhaust the target interval

The [[node:kl.dihedral.odd_reflection_edges|odd-gap edge criterion]] describes an edge by a positive odd intrinsic length difference. The difference identity from Step 6 therefore preserves and reflects edges.

Finally the [[node:kl.dihedral.full_interval_range|full-range theorem]] applies to the injective map \(F\), its edge preservation and its preservation of gap two. It gives
\(\operatorname{range}(F)=[F(g),F(k)]_{D'}\).
This verifies the last field and completes the construction.

For a rank-pattern illustration, if \(\ell_D(g)=2\), \(\ell_D(k)=5\), and \(\ell_{D'}(F(g))=4\), the image has lengths \(4,5,6,7\), with vertex counts \(1,2,2,1\). The common shift of two is determined by the bottom coordinate; each relative gap is preserved.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.transport_interval`: [DyerPaths.lean:736](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L736).
