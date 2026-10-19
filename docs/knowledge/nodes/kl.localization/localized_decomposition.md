---
id: kl.local.localized_decomposition
title: Decomposition of the sheaf after root-plane localization
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.model_decomposition
- kl.local.coset_structure_models
- kl.local.localized_coset_properties
- kl.local.coset_graph
- kl.local.model_sums
- kl.sheaves.boundary_sheaf
- kl.detail.localization_rings
- kl.local.model_sum_step
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:200
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; sec:localization
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Replaced the compressed application by all hypotheses of localized_boundary_decomposition
    and their exact generic sources. Corrected the previous two-lift narrative to
    the single projective lift, residue-surjectivity/Nakayama and right-inverse splitting
    used by LocalCover and the OpenAI notes. Kept the finite basis, minimal coset
    representative, actual localized stalks and both restriction maps explicit.
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Decomposition of the sheaf after root-plane localization

Fix a finite-generator real Coxeter system \(W\), a finite basis of its extended realization, and the associated polynomial coefficient algebra \(A\). Let \(P\) be a root subspace with a plane basis, \(D\) its induced dihedral subgroup, and
\[
R_P=A_{\mathfrak p_P}.
\]
Choose \(a_0\in W\) with \(\ell(a_0)\le\ell(da_0)\) for every \(d\in D\), and let \(b\in W\).

Let \(\mathcal B\) be the constructed boundary sheaf on \([1,b]_W\), with its grading forgotten. On the finite relative coset graph
\[
K=\{d\in D:da_0\le_W b\},
\]
write \(j:K\to[1,b]_W\) for the coset graph map with vertex map \(d\mapsto da_0\), and form the localized coset sheaf
\[
\mathcal L=j^*(R_P\otimes_A\mathcal B).
\]
Then \(\mathcal L\) is isomorphic to a finite ungraded sum of the actual structure models \(\mathcal O_c(K,\gamma)\), with centers \(c\in K\) and localized ambient root labels \(\gamma\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same descent with explicit upper-endpoint edge data.**

**OpenAI notes:** The proof descends through the relative coset vertices, splits the current stalk over the existing boundary image, adds copies of the model centered there and retains both endpoint restrictions. Incoming edge identifications are supplied when their lower vertices are processed, using the upper quotient rule. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The generic local-ring theorem maintains an OnIso on the processed upper set, already including all edges whose upper endpoints have been processed. A maximal unprocessed vertex is added by a finite free kernel block. The new incoming edge maps are induced from the new upper-stalk isomorphism, and strong induction on the remaining finite vertex set gives a full Iso. The boundary-sheaf localization theorem verifies the five sheaf hypotheses and supplies the actual cosetModels. [GradedSheaves:756](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L756), [PlaneLocalization:147](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L147), [PlaneLocalization:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L207), [TerminalKernels:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).

**Role in the proof:** The Blueprint follows the Lean invariant: an edge isomorphism is supplied when its upper endpoint is processed, and its lower restriction square is checked when its lower endpoint is processed. The notes describe incoming-edge identifications later in the descent. The generic Lean theorem uses a finite vertex set; the final application supplies the actual localized coset modules.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the graph and the coefficient ring

The plane ideal \(\mathfrak p_P\) is prime, so \(R_P\) is a commutative local ring.

The vertex map \(d\mapsto da_0\) embeds \(K\) into the finite ambient interval \([1,b]_W\), so \(K\) is finite. Its intrinsic order and edge labels are those specified by the coset graph construction.

These give the finite-vertex graph and local coefficient ring required by the [[node:kl.local.model_decomposition|local model-decomposition theorem]].

### Step 2. Verify finite free stalks

At \(d\in K\), the localized stalk is
\[
\mathcal L^d=R_P\otimes_A\mathcal B^{da_0}.
\]
The boundary-sheaf construction makes \(\mathcal B^{da_0}\) finite free. For a basis \(v_1,\ldots,v_n\), the vectors \(1\otimes v_i\) form an \(R_P\)-basis: the original coordinate isomorphism with \(A^n\) tensors to the coordinate isomorphism with \(R_P^n\).

Thus each stalk of \(\mathcal L\) is finite free. These are the two stalk hypotheses checked separately in the source.

### Step 3. Verify the quotient rule

The boundary sheaf satisfies the upper-quotient rule for the original polynomial labels. Flat scalar extension preserves that rule, with every label mapped into \(R_P\).

Pullback to the coset graph retains the corresponding upper maps and label values. Hence \(\mathcal L\) has surjective upper restrictions with kernels
\[
\gamma_e\,\mathcal L^{t(e)}.
\]
This is the localized-coset quotient property.

### Step 4. Verify generation and relative flabbiness

The boundary sheaf is globally generated. Tensor-extended generating sections and their restrictions to \(K\) give generation of every stalk of \(\mathcal L\).

For flabbiness, localized labels outside the plane become units and their edge modules become zero. The coset graph map has injective vertex map and the required outgoing lifts along the surviving plane edges. The surviving-edge pullback argument therefore gives extension of sections on intrinsic upper subsets of \(K\).

The [[node:kl.local.localized_coset_properties|localized-coset properties theorem]] proves these assertions for the actual tensor stalks and restriction maps used here.

### Step 5. Supply the complete local-model family

The [[node:kl.local.coset_structure_models|coset structure-model theorem]] gives local boundary models
\[
c\longmapsto\mathcal O_c(K,\gamma).
\]
In particular it supplies their flabbiness, generation, finite free stalks, upper quotients, support, top coordinates and local minimality away from the center.

The local minimality proof uses a supported outgoing edge at a proper supported vertex. Its label belongs to the maximal ideal, so vanishing under that quotient puts a kernel vector in the maximal-ideal multiple of its stalk.

### Step 6. Apply the descending decomposition theorem

Steps 1–5 verify every input of the [[node:kl.local.model_decomposition|local model-decomposition theorem]]. It produces a finite ungraded model sum \(C\), with centers in \(K\), and a sheaf isomorphism
\[
\mathcal L\xrightarrow{\sim}C.
\]

At each descending step, the model-sum stalk is a local minimal free cover of the common outgoing image. A single lift from the stalk of \(\mathcal L\) is surjective by Nakayama; a section splits it, and its finite free kernel determines the number of new models at that vertex. The [[node:kl.local.model_sum_step|one-vertex extension theorem]] retains every outgoing restriction and defines the incoming maps by the upper quotients.

This is exactly the source's localized_boundary_decomposition. Its conclusion is the actual isomorphism of sheaves, including both endpoint maps on every edge, that is used to transport the later kernel-image comparisons.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.localized_boundary_decomposition`: [TerminalKernels.lean:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L200).
