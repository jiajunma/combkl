---
id: kl.detail.boundary_extension
title: Attaching a new bottom stalk by a minimal cover
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.boundary_image
- kl.notes.minimal_cover_existence
- kl.detail.upper_quotient
- kl.detail.compatible_sections
- kl.sheaves.flabbiness
- kl.algebra.scalar_quotient
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.bottomGraph
  - OAI.KLInvariance.MomentGraph.GradedSheaf.attachEdges
  - OAI.KLInvariance.MomentGraph.GradedSheaf.attachBoundaryMap
  - OAI.KLInvariance.MomentGraph.GradedSheaf.attachImage
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_freeStalks
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_upperQuotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_bot
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_coe
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:108
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.bottomGraph
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:122
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.attachEdges
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:132
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.attachBoundaryMap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:140
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.attachImage
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:150
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:207
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:190
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:472
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_freeStalks
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:479
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:493
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_bot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:501
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_coe
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
- moment_graph_sheaves
---

# Attaching a new bottom stalk by a minimal cover

Let \(A\) be a nonnegatively graded Noetherian algebra over \(k\), with every coefficient congruent to a base-field scalar modulo \(J=A_{>0}\). Let \(B\) be a graded sheaf on an ordered graph with finitely many vertices.

Adjoin a new bottom vertex \(x\), with a finite family of edges \(d:x\to\tau(d)\) labelled by homogeneous degree-one elements \(\alpha_d\). There is an extension constructed by a minimal cover of the new boundary image. It preserves free stalks, upper quotients, global generation, and edge flabbiness when the old sheaf has those properties. Its new stalk is kernel-minimal, and old kernel-minimality conditions are retained.

*Proof.*

### Step 1. Construct the new edge quotients and boundary image

For each attachment, put
\[
Q_d=B^{\tau(d)}/\alpha_dB^{\tau(d)}.
\]
The label is homogeneous, so the scalar quotient has its quotient grading. The quotient map is degree zero.

An old global section \(f\) supplies a boundary tuple
\[
b(f)=\bigl(f_{\tau(d)}\bmod\alpha_d\bigr)_d
\in\prod_dQ_d.
\]
Define \(D=\operatorname{im}b\).

The old section module is a submodule of a finite product of finite stalks. Noetherianity makes it finite; the boundary product and the image \(D\) are finite graded modules as well. The [[node:kl.notes.minimal_cover_existence|minimal-cover theorem]] therefore supplies a degree-zero surjection
\[
\pi:F\twoheadrightarrow D
\]
from a finite nonnegative graded free module, with \(\ker\pi\subseteq JF\).

### Step 2. Specify the extended sheaf

Use \(F\) as the new stalk at \(x\). The lower restriction on attachment \(d\) is the \(d\)-component of
\[
F\xrightarrow{\pi}D\hookrightarrow\prod_dQ_d.
\]
Its upper restriction is the quotient map \(B^{\tau(d)}\to Q_d\). The old modules and restrictions supply the other components.

A pair \((v,f)\), with \(v\in F\) and an old global section \(f\), is a new global section exactly when
\[
\pi(v)=b(f).
\]
This equality gives the new edge equations coordinate by coordinate.

### Step 3. Extend old global sections and generate stalk values

For any old global section \(f\), the tuple \(b(f)\) belongs to \(D\). Surjectivity of \(\pi\) gives a \(v\) making \((v,f)\) global.

If an old stalk value is prescribed, first realize it by an old global section, then apply this extension.

If a new-stalk vector \(v\in F\) is prescribed, its image \(\pi(v)\in D\) has the form \(b(f)\) for some old global section \(f\), by the definition of \(D\). The resulting pair \((v,f)\) realizes the desired value. Thus global generation is preserved.

### Step 4. Extend from an edge-closed subset

Let \(\Omega\) be closed under the directed edges of the enlarged graph, and let a compatible assignment on \(\Omega\) be given. Its old vertices form an edge-closed subset of the old graph. Old edge flabbiness extends those values to an old global section \(g\).

If \(x\notin\Omega\), choose a lift of \(b(g)\) under \(\pi\). This produces a new global section agreeing with all prescribed values.

If \(x\in\Omega\), closure puts every attachment target \(\tau(d)\) in \(\Omega\). The section \(g\) agrees with the prescribed values at all those targets. Compatibility of the prescribed assignment therefore gives
\[
b(g)=\pi(v),
\]
where \(v\) is its already prescribed value at \(x\). Keeping this \(v\) gives the required global extension.

### Step 5. Verify the free, quotient, and minimality conditions

The new stalk \(F\) is free. Each new upper map is the defining quotient map to \(Q_d\), so it has the required kernel and is onto.

The full outgoing map at \(x\) is the inclusion of \(D\) after \(\pi\). Since that inclusion is injective, its kernel is \(\ker\pi\subseteq JF\). Thus the new stalk is kernel-minimal.

Every new edge starts at \(x\), so the outgoing maps at old vertices retain their old targets and values. Their kernel-minimality conditions are therefore unchanged.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.bottomGraph`: [GradedSheaves.lean:108](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L108).

`OAI.KLInvariance.MomentGraph.GradedSheaf.attachEdges`: [GradedSheaves.lean:122](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L122).

`OAI.KLInvariance.MomentGraph.GradedSheaf.attachBoundaryMap`: [GradedSheaves.lean:132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L132).

`OAI.KLInvariance.MomentGraph.GradedSheaf.attachImage`: [GradedSheaves.lean:140](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L140).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom`: [GradedSheaves.lean:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L150).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_edgeFlabby`: [GradedSheaves.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L207).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_generated`: [GradedSheaves.lean:190](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L190).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_freeStalks`: [GradedSheaves.lean:472](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L472).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_upperQuotient`: [GradedSheaves.lean:479](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L479).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_bot`: [GradedSheaves.lean:493](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L493).

`OAI.KLInvariance.MomentGraph.GradedSheaf.extendBottom_kernelMinimal_coe`: [GradedSheaves.lean:501](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L501).
