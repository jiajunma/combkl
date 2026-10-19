---
id: kl.local.model_sum_step
title: Adding the model block at one unprocessed vertex
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.model_sum_properties
- kl.local.stalk_splitting
- kl.sheaves.partial_iso_extension
- kl.detail.sheaf_isomorphisms
- kl.local.model_sums
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - MinimalExtensions
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.OnIso.above
  - OAI.KLInvariance.MomentGraph.Sheaf.OnIso.prodZero
  - OAI.KLInvariance.MomentGraph.Sheaf.extend_modelSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:981
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.OnIso.above
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:395
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.OnIso.prodZero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:147
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.extend_modelSum
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read extend_modelSum and its AboveIso, basis-coordinate, prodZero, outgoing-compatibility
    and OnIso.extend constructions. Preserved the local finite-free hypothesis only
    at the new stalk, the upper-set conditions, the vanishing of all old-target edge
    modules, and the ModelSum constructor.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Adding the model block at one unprocessed vertex

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\), \(G\) an ordered graph labelled by \(\alpha\), and \(O\) a family of local boundary models. Let \(B\) be a globally generated, flabby sheaf satisfying the upper-quotient rule for \(\alpha\).

Suppose \(U\) is an upper set, \(C\) is a finite ungraded model sum with centers in \(U\), and \(j:B\simeq C\) is a partial isomorphism on \(U\). Thus \(j\) includes edge maps whenever the upper endpoint is in \(U\).

Choose \(x\notin U\) with every \(y>x\) in \(U\), and assume \(B^x\) is finite free. Then for some \(n\in\mathbb N\),
\[
D=C\oplus O_x^n
\]
is a model sum with centers in \(U\cup\{x\}\), and \(j\) extends to a partial isomorphism \(B\simeq D\) on that enlarged upper set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same descent with explicit upper-endpoint edge data.**

**OpenAI notes:** The proof descends through the relative coset vertices, splits the current stalk over the existing boundary image, adds copies of the model centered there and retains both endpoint restrictions. Incoming edge identifications are supplied when their lower vertices are processed, using the upper quotient rule. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The generic local-ring theorem maintains an OnIso on the processed upper set, already including all edges whose upper endpoints have been processed. A maximal unprocessed vertex is added by a finite free kernel block. The new incoming edge maps are induced from the new upper-stalk isomorphism, and strong induction on the remaining finite vertex set gives a full Iso. The boundary-sheaf localization theorem verifies the five sheaf hypotheses and supplies the actual cosetModels. [GradedSheaves:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756), [PlaneLocalization:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147), [PlaneLocalization:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207), [TerminalKernels:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).

**Role in the proof:** The Blueprint follows the Lean invariant: an edge isomorphism is supplied when its upper endpoint is processed, and its lower restriction square is checked when its lower endpoint is processed. The notes describe incoming-edge identifications later in the descent. The generic Lean theorem uses a finite vertex set; the final application supplies the actual localized coset modules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Restrict the existing isomorphism to the data above x

Because every \(y>x\) belongs to \(U\), the vertex and edge maps of \(j\) give an isomorphism above \(x\).

The [[node:kl.local.model_sum_properties|model-sum properties theorem]] makes \(C^x\) finite free and \(C\) generated and flabby. Since \(x\notin U\), it also gives
\[
\ker d_x^C\subseteq\mathfrak mC^x.
\]
Together with the hypotheses on \(B\), these are exactly the assumptions of the [[node:kl.local.stalk_splitting|local stalk-splitting theorem]].

### Step 2. Split the new stalk over the existing model sum

Apply that theorem to obtain
\[
e_x:B^x\xrightarrow{\sim}C^x\oplus Q,
\]
where \(Q\) is finite free, and
\[
j_e(\rho^{B,-}_e(v))
=\rho^{C,-}_e((e_x(v))_1)
\]
for every outgoing edge \(e\) from \(x\).

Choose a finite basis of \(Q\), of size \(n\). It gives a coordinate isomorphism \(Q\simeq R^n\).

### Step 3. Realize the kernel by models centered at x

Let \(S=O_x^n\). The chosen top coordinate \(O_x^x\simeq R\), taken in each of the \(n\) factors, identifies \(S^x\simeq R^n\). Combine its inverse with the basis coordinates of \(Q\) to obtain
\[
\psi:Q\xrightarrow{\sim}S^x.
\]
Define the new stalk isomorphism
\[
j'_x=(1_{C^x}\oplus\psi)e_x:
B^x\xrightarrow{\sim}C^x\oplus S^x=D^x.
\]

### Step 4. Show that the added models vanish on the old data

Take \(y\in U\). If \(y\le x\), upper closure of \(U\) would give \(x\in U\), contradicting the choice of \(x\). Hence \(y\not\le x\).

The support condition of \(O_x\) gives \(O_x^y=0\), so \(S^y=0\). For an edge \(e\) with \(t(e)\in U\), the upper stalk of \(O_x\) is zero. Its upper restriction is surjective, so its edge module is zero as well. Therefore \(S^e=0\).

Extend the old component maps by zero:
\[
j'_y(v)=(j_y(v),0),\qquad
j'_e(w)=(j_e(w),0).
\]
They are isomorphisms because the new second components are zero. Their restriction squares commute componentwise. This is the source's prodZero construction on \(U\).

### Step 5. Check every outgoing square at the new vertex

Let \(e:x\to y\). Then \(y>x\), so \(y\in U\) and \(S^e=0\).

The first component of the desired lower square is exactly the equality from Step 2. The second component is an equality in the zero module \(S^e\). Thus
\[
j'_e\rho^{B,-}_e=\rho^{D,-}_e j'_x
\]
on every outgoing edge from \(x\).

### Step 6. Supply the incoming edge maps

The model-sum properties and componentwise quotient rule show that \(D\) has the same upper-quotient labels as \(B\).

For an incoming edge \(e:z\to x\), the new stalk isomorphism sends
\(\alpha_eB^x\) onto \(\alpha_eD^x\). It therefore induces the edge isomorphism between the two quotient modules, and the upper restriction square commutes by construction.

The [[node:kl.sheaves.partial_iso_extension|partial-isomorphism extension theorem]] combines these new incoming maps, the outgoing squares from Step 5, and the old maps on \(U\). It yields a partial isomorphism on \(U\cup\{x\}\).

### Step 7. Record the enlarged model sum

The old centers in \(U\) are also allowed in \(U\cup\{x\}\). Starting from \(C\), apply the ModelSum addition rule with center \(x\) and multiplicity \(n\). This constructs \(D=C\oplus O_x^n\) as a model sum on the enlarged center set.

When \(Q=0\), its basis is empty and \(n=0\); the same construction adds a zero block and still extends the isomorphism.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.OnIso.above`: [GradedSheaves.lean:981](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L981).

`OAI.KLInvariance.MomentGraph.Sheaf.OnIso.prodZero`: [MinimalExtensions.lean:395](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L395).

`OAI.KLInvariance.MomentGraph.Sheaf.extend_modelSum`: [PlaneLocalization.lean:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147).
