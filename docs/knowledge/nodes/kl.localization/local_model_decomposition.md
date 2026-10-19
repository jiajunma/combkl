---
id: kl.local.model_decomposition
title: Descending decomposition into local boundary models
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.model_sum_step
- kl.local.model_sums
- kl.detail.local_models
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.OnIso.ofUniv
  - OAI.KLInvariance.MomentGraph.Sheaf.exists_modelSumIso
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:987
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.OnIso.ofUniv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:207
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.exists_modelSumIso
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the entire strong induction in exists_modelSumIso. Stated the complement-of-unprocessed-set
    invariant, zero initialization, maximal unprocessed choice, all-above condition,
    strict erasure step, upper closure of the enlarged processed set, and conversion
    of OnIso on all vertices to Iso. Retained finiteness of vertices without imposing
    a finite-edge hypothesis.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Descending decomposition into local boundary models

Let \(R\) be a commutative local ring, \(G\) an ordered graph with finite vertex set \(V\), and \(\alpha\) its edge labels. Let \(O\) be a family of local boundary models for those labels.

Suppose \(B\) has finite free vertex stalks, is globally generated and flabby, and satisfies the upper-quotient rule for \(\alpha\). Then there is a finite ungraded model sum \(C\), with centers among the vertices of \(G\), and an actual sheaf isomorphism
\[
B\simeq C.
\]
The isomorphism includes both endpoint restriction squares on every edge.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same descent with explicit upper-endpoint edge data.**

**OpenAI notes:** The proof descends through the relative coset vertices, splits the current stalk over the existing boundary image, adds copies of the model centered there and retains both endpoint restrictions. Incoming edge identifications are supplied when their lower vertices are processed, using the upper quotient rule. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The generic local-ring theorem maintains an OnIso on the processed upper set, already including all edges whose upper endpoints have been processed. A maximal unprocessed vertex is added by a finite free kernel block. The new incoming edge maps are induced from the new upper-stalk isomorphism, and strong induction on the remaining finite vertex set gives a full Iso. The boundary-sheaf localization theorem verifies the five sheaf hypotheses and supplies the actual cosetModels. [GradedSheaves:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756), [PlaneLocalization:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147), [PlaneLocalization:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207), [TerminalKernels:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).

**Role in the proof:** The Blueprint follows the Lean invariant: an edge isomorphism is supplied when its upper endpoint is processed, and its lower restriction square is checked when its lower endpoint is processed. The notes describe incoming-edge identifications later in the descent. The generic Lean theorem uses a finite vertex set; the final application supplies the actual localized coset modules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State the induction invariant

Let \(S\) be the finite set of vertices still to be processed, and put
\[
U=V\setminus S.
\]
The invariant consists of:

- \(U\) is upper;
- \(C\) is a model sum with centers in \(U\);
- there is a partial isomorphism \(j:B\simeq C\) on \(U\), including all edge maps whose targets lie in \(U\).

We prove by strong induction on \(S\) that any such data extend to a full decomposition.

### Step 2. Initialize the invariant

Initially \(S=V\) and \(U=\varnothing\). Use the zero model sum \(C=0\).

There are no vertex maps to specify on the empty set, and no edge has its target in that set. The partial-isomorphism data are therefore vacuous. The empty set is upper, so the invariant holds.

### Step 3. Finish when every vertex has been processed

If \(S=\varnothing\), then \(U=V\). The partial isomorphism supplies a vertex map at every vertex and an edge map at every edge, because every target lies in \(V\).

Its lower and upper commuting conditions are now the full sheaf-isomorphism conditions. This is OnIso.ofUniv, so \(B\simeq C\) is the desired conclusion.

### Step 4. Choose a maximal unprocessed vertex

Suppose \(S\ne\varnothing\). A finite nonempty subset of a partial order has a maximal element; choose \(x\in S\).

Every \(y>x\) belongs to \(U\): otherwise \(y\in S\), contradicting maximality of \(x\) within \(S\). Thus
\[
x\notin U,\qquad \{y:y>x\}\subseteq U.
\]
The stalk \(B^x\) is finite free by hypothesis.

### Step 5. Process that vertex

The [[node:kl.local.model_sum_step|one-vertex model-sum extension theorem]] applies to the invariant at \(U\) and the vertex \(x\). It gives a model sum \(D\), centered in \(U\cup\{x\}\), and a partial isomorphism
\[
B\simeq D\quad\text{on }U\cup\{x\}.
\]

Set \(S'=S\setminus\{x\}\). Then
\[
V\setminus S'=U\cup\{x\}.
\]
Since \(x\in S\), the set \(S'\) is strictly smaller.

### Step 6. Check upper closure for the smaller induction instance

Take \(y\in U\cup\{x\}\) and \(y\le z\).

If \(y\in U\), upper closure of \(U\) gives \(z\in U\). If \(y=x\), either \(z=x\), which is in the enlarged set, or \(z>x\), which lies in \(U\) by Step 4.

Thus \(U\cup\{x\}\) is upper. The data \(S',D,j'\) satisfy the induction invariant, so the strong induction hypothesis produces a full decomposition.

### Step 7. Read the resulting multiplicities

Each step adds finitely many copies of the model centered at the processed vertex. Its multiplicity is the rank of the finite free kernel in that step's local stalk splitting.

The finite number of vertices makes the resulting construction a finite iterated model sum. Its isomorphism retains all previously constructed maps at each step and includes incoming edge maps through the upper quotients. This proves the stated sheaf decomposition.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.OnIso.ofUniv`: [GradedSheaves.lean:987](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L987).

`OAI.KLInvariance.MomentGraph.Sheaf.exists_modelSumIso`: [PlaneLocalization.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207).
