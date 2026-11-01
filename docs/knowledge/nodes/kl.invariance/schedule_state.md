---
id: kl.detail.schedule_state
title: Remaining conditions and the Hilbert-state vector
kind: definition
status: formalized
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.normalized_kernel
- kl.sheaves.upward_kernel
- kl.sheaves.boundary_sheaf
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.remainingConditions
  - OAI.KLInvariance.BruhatGraph.remainingConditions_nil
  - OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source
  - OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other
  - OAI.KLInvariance.BruhatGraph.scheduleState
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1089
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1093
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_nil
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1097
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1105
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1114
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.scheduleState
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Read the inherited finite-generator, finite-basis and boundary-sheaf context;
    checked all three remainingConditions identities, repeated-edge membership, ModuleData.nonneg,
    scale exponents and the one-edge model.
tags:
- Kazhdan-Lusztig
- comparison_and_freeness
---

# Remaining conditions and the Hilbert-state vector

Fix a Coxeter system \(W\) with finitely many simple generators, an interval \([u,b]_W\), and a finite real basis \(\Sigma\) of its extended realization. Let
\[
A=\mathbb R[X_i:i\in\Sigma],\qquad N=|\Sigma|,
\]
with each variable in degree one. Let \(\mathcal B\) be a boundary sheaf on the polynomially labelled Bruhat graph of \([u,b]_W\), with top \(b\). Its stalks and edge modules are the source's finite graded module data, whose negative-degree pieces vanish.

Write \(s(e)\) and \(r(e)\) for the source and target of a directed Bruhat edge \(e\), and \(\rho_e^-\) for its lower restriction. A finite list \(p\) records the edges still to be processed.

## Outgoing conditions selected by a list

For a vertex \(x\), let \(\operatorname{Out}(x)=\{e:s(e)=x\}\). Define
\[
F_p(x)=\{e\in\operatorname{Out}(x):e\text{ occurs in }p\},
\]
and
\[
K_x(F_p(x))
=\{m\in\mathcal B^x:\rho_f^-(m)=0
                 \text{ for every }f\in F_p(x)\}.
\]
The first formula is `remainingConditions`. The second is the selected kernel. The outgoing-edge type in Lean stores both an edge and the equality identifying its source with \(x\).

List membership determines the set \(F_p(x)\). Repeated occurrences impose the same vanishing equation. For example, \(F_{[e,e]}(s(e))=F_{[e]}(s(e))=\{e\}\).

## The three list identities

The empty list has \(F_{[]}(x)=\varnothing\), since it has no members.
For a list \(e::p\) and \(x=s(e)\),
\[
F_{e::p}(x)=\{e\}\cup F_p(x).
\]
An outgoing edge belongs to the left side exactly when it equals \(e\) or belongs to \(p\), proving both containments.

For \(z\ne s(e)\),
\[
F_{e::p}(z)=F_p(z).
\]
An edge outgoing from \(z\) cannot equal \(e\), because equality would give \(z=s(e)\). Its membership in \(e::p\) is therefore exactly its membership in \(p\). These are `remainingConditions_nil`, `remainingConditions_cons_source` and `remainingConditions_cons_other`.

Every Bruhat edge is strictly increasing, so \(s(e)\ne r(e)\). In particular
\[
F_{e::p}(r(e))=F_p(r(e)).
\]
Removing the head edge changes the selected kernel only at its source. If the tail contains another copy of that edge, the selected set at the source also stays the same.

## The numerical state

Fix \(0<t<1\). The normalized Hilbert-state vector is
\[
D_p(t)_x
=(1-t^2)^N t^{\ell_W(x)-\ell_W(b)}
  H_{K_x(F_p(x))}(t^2).
\]
This is `scheduleState`. The Hilbert value uses the actual intersections
\[
H_{K_x(F)}(q)
=\sum_{n\in\mathbb Z}
 \dim_{\mathbb R}\bigl(K_x(F)\cap(\mathcal B^x)_n\bigr)q^n.
\]
Its pieces are finite-dimensional, its series converges for \(0<q<1\), and its negative-degree terms vanish. The state scale and these convergence facts are developed in the [[node:kl.comparison.normalized_kernel|normalized-kernel definition]].

For \(p=[]\), no restriction is imposed, so \(K_x(F_p(x))=\mathcal B^x\). If \(p\) contains every graph edge, then \(F_p(x)=\operatorname{Out}(x)\), giving the full outgoing kernel. A chronological schedule moves from those full kernels to the stalks by successively replacing a list \(e::p\) with its tail \(p\).

## The one-edge state

In the illustrative one-edge polynomial model \(x\to y=b\), take \(A=\mathbb R[\alpha]\), degree-zero stalks \(A\), edge module \(A/(\alpha)\), and quotient maps for both restrictions. Give the endpoints lengths \(0,1\). The full selected kernels are \(\alpha A\) at \(x\) and \(A\) at \(y\); the empty selections give \(A\) at both.

Since \(H_A(q)=1/(1-q)\) and \(H_{\alpha A}(q)=q/(1-q)\), the scale at \(x\) is \((1-t^2)t^{-1}\), while the scale at \(y\) is \(1-t^2\). Hence
\[
D_{[e]}(t)=(t,1),\qquad D_{[]}(t)=(t^{-1},1).
\]
The [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] measures this change using the coefficient \(t^{-1}-t\). For a longer list, the same definition retains the full vector of selected kernels at every stage.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Equivalent parameter conventions.**

**OpenAI notes:** The comparison uses \(0<q<1\), scale \(q^{-d/2}(1-q)^N\), and transfer coefficient \(q^{-1/2}-q^{1/2}\). [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275).

**Lean (primary):** The comparison uses \(0<t<1\) and substitutes \(q=t^2\). Its scale is \(t^{-d}(1-t^2)^N\) and its transfer coefficient is \(t^{-1}-t\). [Dihedral:730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L730), [PositiveTransfer:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L591), [PositiveTransfer:621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L621), [EdgeLocalization:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L377), [EdgeLocalization:423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L423), [PositiveTransfer:535](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L535), [PositiveTransfer:603](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L603).

**Role in the proof:** The substitution \(q=t^2\) identifies the two normalizations. Linear root labels have degree one throughout the calculation.

**Actual suffix conditions and the conditional whole-list bound.**

**OpenAI notes:** The comparison processes the increasing edge schedule, retains the equations on unprocessed outgoing edges, and propagates the single-edge estimate through the complete matrix product. [eq:state](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L243), [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The numerical theorem first accepts any finite list with image inclusion at every nonempty suffix. A separate theorem takes the actual chronological schedule and freeness of each upper suffix kernel. Exact suffix-to-ambient kernel identities let it apply the global edge inclusion before invoking the numerical theorem. [PositiveTransfer:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089), [PositiveTransfer:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1117), [PositiveTransfer:1148](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1148), [TerminalKernels:1126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1126), [TerminalKernels:1171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1171).

**Role in the proof:** The Blueprint spells out the set-valued remaining conditions, source and non-source coordinate changes, suffix quantifiers and reversed product. The source-specific upper-freeness step has its own entry.
<!-- source-comparison:end -->

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.remainingConditions`: [PositiveTransfer.lean:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1089).

`OAI.KLInvariance.BruhatGraph.remainingConditions_nil`: [PositiveTransfer.lean:1093](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1093).

`OAI.KLInvariance.BruhatGraph.remainingConditions_cons_source`: [PositiveTransfer.lean:1097](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1097).

`OAI.KLInvariance.BruhatGraph.remainingConditions_cons_other`: [PositiveTransfer.lean:1105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1105).

`OAI.KLInvariance.BruhatGraph.scheduleState`: [PositiveTransfer.lean:1114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1114).
