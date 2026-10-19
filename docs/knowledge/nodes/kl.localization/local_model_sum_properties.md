---
id: kl.local.model_sum_properties
title: Properties and local minimality of finite model sums
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.model_sums
- kl.detail.local_models
- kl.sheaves.finite_sum_properties
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.free
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.finite
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.quotient
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.generated
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.flabby
  - OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:381
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:390
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:399
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:406
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:411
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:416
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.minimal
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all six ungraded ModelSum property inductions. Expanded the zero case,
    finite bases, quotient kernels, section extension and ideal-coordinate insertion.
    Kept the minimality hypothesis x outside the allowed center set and required no
    upper-set condition on U.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Properties and local minimality of finite model sums

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\), \(G\) an ordered graph with labels \(\alpha_e\), and \(O\) a family of local boundary models. Let \(C\) be a finite ungraded model sum with centers in a set \(U\). Write \(d_x^C\) for the stalk map collecting the restrictions along all outgoing edges from \(x\).

Then \(C\) has finite free stalks, satisfies the upper-quotient rule, and is globally generated and flabby. At every \(x\notin U\),
\[
\ker d_x^C\subseteq\mathfrak mC^x.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same descent with explicit upper-endpoint edge data.**

**OpenAI notes:** The proof descends through the relative coset vertices, splits the current stalk over the existing boundary image, adds copies of the model centered there and retains both endpoint restrictions. Incoming edge identifications are supplied when their lower vertices are processed, using the upper quotient rule. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The generic local-ring theorem maintains an OnIso on the processed upper set, already including all edges whose upper endpoints have been processed. A maximal unprocessed vertex is added by a finite free kernel block. The new incoming edge maps are induced from the new upper-stalk isomorphism, and strong induction on the remaining finite vertex set gives a full Iso. The boundary-sheaf localization theorem verifies the five sheaf hypotheses and supplies the actual cosetModels. [GradedSheaves:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756), [PlaneLocalization:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147), [PlaneLocalization:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207), [TerminalKernels:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).

**Role in the proof:** The Blueprint follows the Lean invariant: an edge isomorphism is supplied when its upper endpoint is processed, and its lower restriction square is checked when its lower endpoint is processed. The notes describe incoming-edge identifications later in the descent. The generic Lean theorem uses a finite vertex set; the final application supplies the actual localized coset modules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Set up induction on the construction

A model sum is built from the zero sheaf by repeatedly forming
\[
C'=C\oplus O_c^n,\qquad c\in U,\ n\in\mathbb N.
\]
We prove all the assertions together by induction on this finite construction.

For the zero sheaf, every stalk and edge module is zero. The empty stalk basis proves finite freeness, every restriction is a surjection onto zero, and every prescribed section consists of zeros. The outgoing kernel and its maximal-ideal multiple are both zero.

### Step 2. Retain finite free stalks and upper quotients

Assume the assertions for \(C\). Each stalk of \(O_c\) is finite free by the local-model fields. The stalk of \(C'\) is
\[
C^x\oplus(O_c^x)^n.
\]
Insert the chosen basis of each summand into its coordinate. Coordinatewise expansions prove spanning, and coordinatewise independence proves independence. The resulting family is finite.

The upper restriction is the product of the upper restrictions of the summands. Each is onto. Its kernel consists of tuples each divisible by \(\alpha_e\), which is precisely
\[
\alpha_e\bigl(C^{t(e)}\oplus(O_c^{t(e)})^n\bigr).
\]

### Step 3. Retain generation and flabbiness

To generate a prescribed stalk tuple, choose a generating global section for each coordinate and assemble them. The restriction equations hold coordinatewise.

For a compatible section on an upper set, project it to each summand, extend each projected section using flabbiness, and assemble the extensions. They agree with the prescribed tuple and are globally compatible.

These are the finite-sum property arguments for the corresponding source lemmas.

### Step 4. Verify minimality outside the center set

Fix \(x\notin U\). Since \(c\in U\), one has \(x\ne c\), so local minimality of \(O_c\) applies at \(x\).

A vector \((v,w_1,\ldots,w_n)\) belongs to the full outgoing kernel of \(C'\) exactly when \(v\in\ker d_x^C\) and every \(w_i\in\ker d_x^{O_c}\). The induction hypothesis and model minimality put these coordinates in
\(\mathfrak mC^x\) and \(\mathfrak mO_c^x\), respectively.

Each coordinate is a finite sum of maximal-ideal scalars times module vectors. Insert these summands into the corresponding coordinate of \(C'^x\), and sum over the finitely many coordinates. This expresses the whole tuple as an element of \(\mathfrak mC'^x\).

Thus the kernel inclusion holds for \(C'\). The argument also covers \(n=0\), which adds no new coordinate. Induction proves every assertion for \(C\).

The condition \(x\notin U\) is exactly the one used when a new vertex is processed: all existing models are centered at already processed vertices, so their combined outgoing map at the new vertex is a local minimal free cover.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.free`: [CharacterReciprocity.lean:381](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L381).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.finite`: [CharacterReciprocity.lean:390](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L390).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.quotient`: [CharacterReciprocity.lean:399](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L399).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.generated`: [CharacterReciprocity.lean:406](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L406).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.flabby`: [CharacterReciprocity.lean:411](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L411).

`OAI.KLInvariance.MomentGraph.Sheaf.ModelSum.minimal`: [CharacterReciprocity.lean:416](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L416).
