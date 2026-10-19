---
id: kl.local.localized_coset_properties
title: Quotients, generation, and flabbiness on a localized coset
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.localized_coset
- kl.local.coset_outgoing_lifts
- kl.local.plane_prime_membership
- kl.realization.plane_reflection_membership
- kl.sheaves.base_change_properties
- kl.sheaves.pullback_live_flabbiness
- kl.dihedral.plane_coset_graph
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.polynomialLabel_unit_iff
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_quotient
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_generated
  - OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_flabby
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:567
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.polynomialLabel_unit_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:577
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:585
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:591
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1635
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1640
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the root/unit criterion, all three localizedCoset property proofs
    and both root-label identities. Expanded the finite ambient graph, zero outside
    edge modules, injective coset map and outgoing lifts before invoking relative
    flabbiness; free/finite stalk transfer follows from the explicit tensor stalks.
tags:
- Kazhdan-Lusztig
- localization
---

# Quotients, generation, and flabbiness on a localized coset

Fix a finite-generator Coxeter system, a root plane \(P\) with a chosen plane basis, its induced reflection subgroup \(D_P\), a least-length representative \(a_0\) in \(D_Pa_0\), and \(b\in W\). Choose a finite real basis of the extended realization, giving the polynomial coefficient algebra \(A\) and linear-label map \(\lambda:V_0\to A\) from the original root space. Write
\[
R_P=A_{\mathfrak p_P},\qquad \eta:A\to R_P,\qquad \lambda_P=\eta\lambda.
\]
Let \(j:K\to[1,b]\) be the coset graph map \(d\mapsto da_0\), with
\(K=\{d\in D_P:1\le_Dd,\ da_0\le_Wb\}\).
For an \(A\)-linear sheaf \(C\) on \([1,b]\), put
\[
C_{R_P}=R_P\otimes_A C,\qquad \mathcal C=j^*(C_{R_P}).
\]

For an ambient edge \(e\) with positive root \(\beta_e\), polynomial label \(\alpha_e=\lambda(\beta_e)\), and left reflection label \(\tau_e\),
\[
\eta(\lambda(\beta_e))\text{ is a unit in }R_P
\quad\Longleftrightarrow\quad \tau_e\notin D_P.
\]
For a relative edge \(a:d\to_D c\), its induced and ambient positive roots agree, so its coset label is \(\lambda_P(\beta_a)\).

The following sheaf properties hold.

- If \(C\) satisfies the polynomial upper-quotient rule, then \(\mathcal C\) satisfies it with the coset labels.
- If \(C\) is globally generated, then \(\mathcal C\) is globally generated.
- If \(C\) is flabby and satisfies the upper-quotient rule, then \(\mathcal C\) is flabby for the induced order on the finite coset graph.
- Freeness and finite generation of a stalk of \(C\) pass to the corresponding stalk of \(\mathcal C\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Relative extension through an explicit graph map.**

**OpenAI notes:** The coset intersection is a finite relative lower ideal. A relative upper subset is closed under the surviving plane-labelled edges. Descending ambient extension gives relative flabbiness after localization. [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The same descending extension is factored into extend_closedUnder and a graph-pullback theorem. The coset map supplies vertex injectivity and explicit outgoing lifts; the root/unit criterion makes all outside edge modules zero. A separate theorem records selected-kernel equality under that pullback. [Sheaves:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106), [MinimalExtensions:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1520), [PlaneLocalization:497](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L497), [PlaneLocalization:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591), [TerminalKernels:393](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L393).

**Role in the proof:** Relative order determines the upper subsets on the coset, while the ambient graph supplies the extension. The localized stalks and edge maps remain the actual tensor-extended ambient modules, so selected kernels and their edge images retain their embeddings.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Detect the invertible ambient labels

The [[node:kl.local.plane_prime_membership|plane-prime unit theorem]] gives
\[
\eta(\lambda(\beta_e))\text{ invertible}
\quad\Longleftrightarrow\quad \beta_e\notin P.
\]
The positive root \(\beta_e\) represents \(\tau_e\). The [[node:kl.realization.plane_reflection_membership|root criterion for plane-subgroup membership]] gives
\[
\tau_e\in D_P\quad\Longleftrightarrow\quad\beta_e\in P.
\]
Combining the two equivalences proves the asserted unit criterion for every ambient edge.

### Step 2. Identify the induced root label

For \(a:d\to_D c\), the corresponding ambient edge has endpoints \(da_0,ca_0\). Its reflection label is
\[
(ca_0)(da_0)^{-1}=cd^{-1},
\]
the same reflection used to define the induced edge root. Both constructions choose its ambient positive root. Hence
\(\beta_{j_E(a)}=\beta_a\), which is cosetRoot_eq.

Applying the localized linear-label map gives
\[
\alpha^K_a=\lambda_P(\beta_{j_E(a)})=\lambda_P(\beta_a).
\]
This is cosetLabel_eq_root.

### Step 3. Transport upper quotients and generation

For the quotient assertion, assume the polynomial upper-quotient rule for \(C\). Localization is flat. The [[node:kl.sheaves.base_change_properties|scalar-extension property theorem]] therefore transports the upper-quotient rule from \(C\) to \(C_{R_P}\), with labels \(\eta(\alpha_e)\). Pullback transports this rule to \(\mathcal C\); its labels are precisely the coset labels defined in Step 2.

For the generation assertion, assume \(C\) is globally generated. This first passes to \(C_{R_P}\) by tensoring sections that generate its stalk values. Pulling those sections back along \(j\) proves generation of \(\mathcal C\).

### Step 4. Verify the surviving-edge hypotheses

For the flabbiness assertion, assume \(C\) is flabby and satisfies the polynomial upper-quotient rule.

Let
\[
L=\{e:\tau_e\in D_P\}
\]
in the ambient Bruhat graph. For \(e\notin L\), Step 1 makes its localized label a unit. The upper-quotient rule then forces \((C_{R_P})^e=0\).

The [[node:kl.local.coset_outgoing_lifts|coset outgoing-lift theorem]] proves that \(j_V\) is injective and that every edge in \(L\) starting at \(j_V(d)\) has a relative lift starting at \(d\). These are exactly the hypotheses needed for pullback along surviving edges.

### Step 5. Transport flabbiness to the relative order

The ambient Bruhat interval has finitely many vertices; its edges are a subset of the finite square of that vertex set. The [[node:kl.sheaves.base_change_properties|finite-flat scalar-extension theorem]] makes \(C_{R_P}\) flabby.

Apply the [[node:kl.sheaves.pullback_live_flabbiness|surviving-edge pullback theorem]] using \(L\) from Step 4. It extends every section on a relative upper subset of the coset graph and gives flabbiness of \(\mathcal C\).

Concretely, the image of a relative upper subset is closed under \(L\). A prescribed section pushes to a compatible assignment on that image; relative extension in the ambient graph gives a global section; pulling it back gives the required extension on the coset.

### Step 6. Transport free and finite stalks

At a relative vertex \(d\),
\[
\mathcal C^d=R_P\otimes_A C^{da_0}.
\]
A free basis of the original stalk tensors to a free basis over \(R_P\), and a finite generating set tensors to a finite generating set. The [[node:kl.sheaves.base_change_properties|scalar-extension property theorem]] supplies both assertions.

For the actual boundary sheaf \(C=B(b)\), its constructed finite free stalks, quotient rule, generation and flabbiness therefore give all four stated properties on the localized coset.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.polynomialLabel_unit_iff`: [PlaneLocalization.lean:567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L567).

`OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_quotient`: [PlaneLocalization.lean:577](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L577).

`OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_generated`: [PlaneLocalization.lean:585](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L585).

`OAI.KLInvariance.TitsSpace.PlaneBasis.localizedCoset_flabby`: [PlaneLocalization.lean:591](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L591).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq`: [PlaneLocalization.lean:1635](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1635).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root`: [PlaneLocalization.lean:1640](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1640).
