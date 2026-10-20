---
id: kl.local.coset_model_scaled_images
title: Scaled image equality in every coset structure model
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.detail.scaled_images
- kl.local.coset_structure_models
- kl.local.coset_kernel_products
- kl.local.coset_later_selections
- kl.local.coset_edge_reduction
- kl.local.supported_count_weight
- kl.local.structure_scaled_images
- kl.local.edge_factor_lift
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.coset_structure_scaledImages
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:146
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.coset_structure_scaledImages
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: 'Verified every actual coset-model hypothesis: all centers, unsupported
    zero branch, finite edge selections, choice of independent reference root, both
    root-inequality arguments, relative primality, actual quotient associations, fixed
    correction scalar and supported count.'
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# Scaled image equality in every coset structure model

Let \(W,W'\) be finite-generator real Coxeter systems and
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\).
Choose a root plane \(P\) with plane basis \(B=(a_L,a_R)\), its induced subgroup \(D\), and a least representative \(a_0\) with
\(\ell_W(a_0)\le\ell_W(da_0)\) for all \(d\in D\).
Let \(K=\{d\in D:da_0\le_Wb\}\) be the finite relative coset graph.

A real basis of the extended realization gives the polynomial coefficient algebra \(A\). Write
\[
R_P=A_{\mathfrak p_P},\qquad \eta_P:A\to R_P
\]
for the plane ring and localization map. The coset labels are the localized root polynomials \(\gamma_f\).

Fix \(e:x\to_Dy\) in \(K\), with \(u\le_Wxa_0\), and write \(a\) for its actual positive source root. Let \(F_e,H_e\) be the two coset later-edge selections, using the positive root of \(\varphi(xa_0)\to_{W'}\varphi(ya_0)\) as their common threshold. Define the scalar
\[
r_e=\eta_P(F_{xa_0,a})\in R_P,
\]
where \(F_{xa_0,a}\) is the polynomial lift of the correction factor.

For every model center \(c\in K\), the structure sheaf \(\mathcal O_c\) satisfies
\[
L_e^{\mathcal O_c}(F_e)=r_e\,U_e^{\mathcal O_c}(H_e)
\]
as submodules of its actual edge module \(\mathcal O_c^e\). Here
\[
L_e^{\mathcal O_c}(F_e)=\rho_e^-(K_x^{\mathcal O_c}(F_e)),\qquad
U_e^{\mathcal O_c}(H_e)=\rho_e^+(K_y^{\mathcal O_c}(H_e)).
\]
The selected kernel \(K_z\) imposes zero restrictions along the indicated outgoing edges.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The transported count in the actual model edge quotient.**

**OpenAI notes:** In a supported model, the notes identify the two localized image ideals through their valuations. The later-edge counts differ by the plane weight, which is also the valuation of the correction factor. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The exact supported selections are counted by finite target-vertex sums. The all-ranks transported count and planeWeight_coset_edge identify their difference. Each label and the fixed correction lift are then compared up to units in the actual quotient by cosetLabel e, and structure_scaledImages_of_count gives the image equality. An unsupported model has a zero edge module. [PlaneLocalization:1175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1175), [TerminalKernels:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L146).

**Role in the proof:** The Blueprint checks the selection, root-inequality, pairwise-relative-primality, quotient and count hypotheses separately, then multiplies the unit associations to obtain the exact embedded equality.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Separate the supported and zero edge modules

If \(y\not\le_Dc\), the structure model has \(\mathcal O_c^e=0\). Both displayed images are zero submodules of that module. In the witness formulation of ScaledImages, either direction uses the zero stalk vector, whose selected restrictions and edge image are zero. This proves the result in this case.

Henceforth assume \(y\le_Dc\). The actual edge coefficient ring and module are
\[
S_e=R_P/(\gamma_e),\qquad \mathcal O_c^e=S_e.
\]
Let \(q_e:R_P\to S_e\) be the quotient map.

### Step 2. Choose the reference reduced root

The current root \(a\) lies in \(P\). The two basis roots \(a_L,a_R\) are distinct. If \(a=a_L\), choose \(\beta=a_R\); otherwise choose \(\beta=a_L\). In either case \(\beta\in P\) and \(\beta\ne a\).

The two positive roots are independent, so their two-dimensional span is \(P\). Put
\[
p=q_e(\lambda_P(\beta)),\qquad
k=\bigl(k_P(xa_0,a)\bigr)_{\mathbb N},
\]
where \(\lambda_P\) is the localized root-polynomial map. This \(p\) is the reference root reduction in the [[node:kl.local.coset_edge_reduction|coset edge-reduction theorem]].

### Step 3. Verify the label conditions at both endpoints

Let \(F_{e,c}=\{f\in F_e:t(f)\le_Dc\}\) and \(H_{e,c}=\{h\in H_e:t(h)\le_Dc\}\), where \(t\) is the target map. The [[node:kl.local.coset_kernel_products|coset kernel-product theorem]] gives pairwise relative primality of the labels within each of these sets.

Every \(f\in F_{e,c}\) has source root different from \(a\). Indeed, equality of roots would identify the reflection; equality of the source would then identify the target, making \(f=e\). The strict later selection excludes \(e\).

Every edge leaving \(y\), including every \(h\in H_{e,c}\), also has root different from \(a\). Otherwise the consecutive edges \(x\to y\to z\) would use the same reflection and give \(z=x\), contrary to increasing length.

The [[node:kl.local.coset_edge_reduction|coset edge-reduction theorem]] therefore applies to every selected label and gives
\[
q_e(\gamma_f)\sim p\quad(f\in F_{e,c}),\qquad
q_e(\gamma_h)\sim p\quad(h\in H_{e,c}).
\]
Here \(\sim\) means multiplication by a unit of \(S_e\).

### Step 4. Verify the correction exponent and the exact count

The factor part of the [[node:kl.local.coset_edge_reduction|coset edge-reduction theorem]] gives
\[
q_e(r_e)\sim p^k.
\]
Its scalar is the same localization of the fixed polynomial lift \(F_{xa_0,a}\) appearing in the statement.

The [[node:kl.local.supported_count_weight|supported-count weight theorem]] applies because \(y\le_Dc\), and gives
\[
|F_{e,c}|=|H_{e,c}|+k.
\]
Thus all label, factor and cardinality hypotheses of the [[node:kl.local.structure_scaled_images|structure-model count criterion]] have been verified in the same quotient \(S_e\).

### Step 5. Compare the two actual image products

Put
\[
p_x=\prod_{f\in F_{e,c}}\gamma_f,\qquad
p_y=\prod_{h\in H_{e,c}}\gamma_h.
\]
The [[node:kl.local.coset_kernel_products|coset kernel-product theorem]] identifies the actual edge images as
\(p_xS_e\) and \(p_yS_e\), using the quotient action of \(R_P\).

Multiplying the associations from Steps 3–4 gives
\[
q_e(p_x)\sim p^{|F_{e,c}|}
=p^{k+|H_{e,c}|}
\sim q_e(r_e)\,q_e(p_y).
\]
The [[node:kl.local.structure_scaled_images|structure-model count criterion]] turns this association into equality of scalar-image submodules:
\[
p_xS_e=r_e(p_yS_e).
\]
Substituting the two product descriptions proves the required scaled image equality.

For the long \(A_2\) edge with model top \(sts\), the supported later counts are one and zero, and \(k=1\). The lower product is associated to \(p\), the upper product is the empty product \(1\), and the reduced correction is associated to \(p\). The equality is therefore \(pS_e=r_eS_e\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.coset_structure_scaledImages`: [TerminalKernels.lean:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L146).
