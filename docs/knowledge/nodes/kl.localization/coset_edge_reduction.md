---
id: kl.local.coset_edge_reduction
title: Root and factor reductions in the actual coset edge ring
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_graph
- kl.local.localized_edge_ring
- kl.local.localized_root_reduction
- kl.local.factor_plane_reduction
- kl.local.edge_factor_lift
- kl.dihedral.plane_coset_graph
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root
  - OAI.KLInvariance.TitsSpace.PlaneBasis.reducedCosetRoot
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_reduction_associated
  - OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFactor_reduction_associated
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1635
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1640
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1647
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.reducedCosetRoot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1651
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_reduction_associated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1663
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFactor_reduction_associated
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the exact cosetRoot/label equalities, reducedCosetRoot and both association
    lemmas. Retained the actual quotient by cosetLabel e, proved its equality with
    the generic localized root quotient, kept inequality of the positive roots rather
    than merely inequality of edges, and applied the fixed polynomial factor at the
    ambient source.
tags:
- Kazhdan-Lusztig
- embedded-images
---

# Root and factor reductions in the actual coset edge ring

Fix a finite-generator real Coxeter system \(W\), a root subspace \(P\) with a plane basis, its induced subgroup \(D\), and polynomial coefficient algebra \(A\) from a basis of the extended realization. Choose \(a_0,b\in W\) with \(\ell(a_0)\le\ell(da_0)\) for every \(d\in D\).

On the relative coset graph \(K=\{d\in D:da_0\le b\}\), write \(R_P=A_{\mathfrak p_P}\), let \(\eta_P:A\to R_P\) be localization, and let \(\lambda(v)\) be the polynomial of an embedded root. Let \(\gamma_f\in R_P\) be the actual localized label of an edge \(f\). Fix \(e:x\to y\), with positive ambient root \(a\). Its edge coefficient ring is
\[
S_e=R_P/(\gamma_e),
\]
with quotient map \(q_e\).

Choose a positive root \(\beta\ne a\) satisfying \(\operatorname{span}\{a,\beta\}=P\), and define
\[
p_\beta=q_e(\lambda_P(\beta)),
\qquad \lambda_P=\eta_P\lambda.
\]
This is reducedCosetRoot. Then:

- for any coset edge \(f\) whose positive root \(a_f\ne a\),
  \[
  q_e(\gamma_f)\sim p_\beta;
  \]
- for the correction scalar \(r=\eta_P(F_{xa_0,a})\),
  \[
  q_e(r)\sim p_\beta^{\,k_P(xa_0,a)}.
  \]

Here \(\sim\) denotes association by a unit, and the exponent uses the equal natural-number value of the plane weight.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Associated products in the actual model edge quotient.**

**OpenAI notes:** In each supported rank-one model, the two images are principal product ideals in the localized edge ring. Their reduced labels have the same uniformizer up to units, and the correction factor supplies the exponent difference. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The structure-model theorem uses the exact quotient R/(alpha_e) as the edge coefficient ring and derives equality from association of the two scalar products. The actual coset labels are identified with localized ambient root forms before the label and factor associations are imported. A zero edge module gives the equality directly. [TerminalKernels:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L62), [TerminalKernels:82](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L82), [PlaneLocalization:1640](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1640), [PlaneLocalization:1647](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1647), [PlaneLocalization:1651](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1651), [PlaneLocalization:1663](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1663).

**Role in the proof:** The Blueprint keeps the quotient action, root inequality and count hypotheses explicit. The actual supported case combines these algebraic inputs with the transported later-edge count.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the current root in both graph descriptions

The intrinsic edge \(x\to y\) maps to the ambient edge \(xa_0\to ya_0\). Its ambient left reflection is
\[
(ya_0)(xa_0)^{-1}=yx^{-1}.
\]
Both graph-root constructions choose the canonical positive root of this reflection. Therefore the root of the ambient coset edge is exactly \(a\), the intrinsic edgeRoot.

The actual scalar label consequently satisfies
\[
\gamma_e=\lambda_P(a).
\]
The same calculation gives \(\gamma_f=\lambda_P(a_f)\) for every coset edge \(f\). These are cosetRoot_eq and cosetLabel_eq_root.

### Step 2. Identify the quotient and the reference reduction

Substitute Step 1 into its defining ideal:
\[
S_e=R_P/(\lambda_P(a))=E_{P,a}.
\]
Under this identification,
\[
p_\beta=q_e(\lambda_P(\beta))=r_{P,a}(\beta).
\]
Thus the scalar used in this actual edge quotient is the reference reduced root from the general localized reduction theorem.

A suitable \(\beta\) exists: the two plane-basis roots are distinct, so choose one different from \(a\). It lies in \(P\), and independence gives \(\operatorname{span}\{a,\beta\}=P\).

### Step 3. Reduce another edge label

The root \(a_f\) of a relative coset edge lies in \(P\). By assumption it is different from \(a\).

The [[node:kl.local.localized_root_reduction|localized root-reduction theorem]] therefore gives
\[
r_{P,a}(a_f)\sim r_{P,a}(\beta).
\]
Use Step 1 to replace the left side by \(q_e(\gamma_f)\), and Step 2 to replace the right side by \(p_\beta\). This proves the first association.

### Step 4. Reduce the actual correction scalar

Apply the [[node:kl.local.factor_plane_reduction|localized-factor theorem]] to the ambient source \(xa_0\), the roots \(a,\beta\), and their plane \(P\). It gives
\[
q_e(\eta_P(F_{xa_0,a}))
\sim r_{P,a}(\beta)^{\,k_P(xa_0,a)}.
\]
The left side is \(q_e(r)\), and Step 2 identifies the right side with the required power of \(p_\beta\).

These associations are now in the exact coefficient ring of the current coset edge. The later-edge selections supply the root inequalities needed for Step 3, and the supported count supplies the exponent difference used in the structure-model comparison.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetRoot_eq`: [PlaneLocalization.lean:1635](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1635).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_eq_root`: [PlaneLocalization.lean:1640](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1640).

`OAI.KLInvariance.TitsSpace.PlaneBasis.reducedCosetRoot`: [PlaneLocalization.lean:1647](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1647).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetLabel_reduction_associated`: [PlaneLocalization.lean:1651](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1651).

`OAI.KLInvariance.TitsSpace.PlaneBasis.cosetFactor_reduction_associated`: [PlaneLocalization.lean:1663](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1663).
