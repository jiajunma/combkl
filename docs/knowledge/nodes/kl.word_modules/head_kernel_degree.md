---
id: kl.word.head_kernel_degree
title: The head-kernel maps raise degree by one
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.head_kernel_maps
- kl.word.simple_frobenius_data
- kl.algebra.component_transport
- kl.word.evaluation_grading
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_eval
  - OAI.KLInvariance.TitsSpace.bottHeadLeft_kernel_homogeneous
  - OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_homogeneous
  - OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_eval
  - OAI.KLInvariance.TitsSpace.bottHeadRight_kernel_homogeneous
  - OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1589
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_eval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1601
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLeft_kernel_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1618
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2056
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_eval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2071
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRight_kernel_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:2084
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_homogeneous
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the gradings, scalar actions, coefficient variables and formal polynomial
    conclusions explicit?
  verdict: Read both evaluation formulas and homogeneous-degree proofs. Expanded the
    real-linear inverse-degree argument and identified the source positive shift M(1)_n=M_(n-1).
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The head-kernel maps raise degree by one

Fix a finite-generator Coxeter system and a finite basis of its extended realization, giving the degree-one symmetric coefficient grading. Let \(\mathbf t\) be a word, \(s\) a simple reflection and \(x\in W\). Use the stalks \(X=M_{\mathbf t}^x\), \(Y=M_{\mathbf t}^{sx}\), \(Z=M_{s\mathbf t}^x\), their head kernels \(K_0,K_1\), and the maps \(\kappa_0,\kappa_1\).

In the ascent case \(\ell(x)<\ell(sx)\),
\[
\kappa_0(Y_n)\subseteq(K_0)_{n+1}.
\]
In the descent case \(\ell(sx)<\ell(x)\),
\[
\kappa_1(X_n)\subseteq(K_1)_{n+1}.
\]
In each case the inverse lowers degree by one. Consequently,
\[
Y_{n-1}\simeq(K_0)_n\quad\text{in the ascent case},
\qquad
X_{n-1}\simeq(K_1)_n\quad\text{in the descent case},
\]
as real vector spaces.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Degree-one kernels and shift conventions.**

**OpenAI notes:** The normalization proof temporarily assigns degree two to linear forms and uses \(M(k)^j=M^{j+k}\) for its shifted self-dual object. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The word construction keeps linear forms in degree one. Each kernel equivalence sends an old degree-\(n\) vector to degree \(n+1\). The local module-data convention is \(M(1)_n=M_{n-1}\). [GradedModules:1244](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1244), [BottSamelson:1618](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1618), [BottSamelson:2084](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2084), [BottSamelson:1744](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1744).

**Role in the proof:** The old degree-\((n-1)\) piece contributes to the new degree-\(n\) kernel. Reindexing its Hilbert sum gives the factor \(q\) in the word-character recurrence.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Read the ascent map in evaluation coordinates

Write \(\tau=\chi_s\), \(\alpha=\alpha_s\). The pair-coordinate map takes
\((p,q)\) to the values \(p_\eta\) on the zero-bit branch and
\(\tau(q_\eta)\) on the one-bit branch.

Thus, for \(y\in Y\),
\[
(\kappa_0(y))_{(0,\eta)}=0,\qquad
(\kappa_0(y))_{(1,\eta)}=\tau(\alpha y_\eta).
\]
Only tail indices of the required weight occur in each branch.

### Step 2. Check its degree

If \(y\in Y_n\), every stalk coordinate \(y_\eta\) lies in \(A_n\). The root \(\alpha\) has degree one, so \(\alpha y_\eta\in A_{n+1}\). The coefficient action \(\tau\) preserves degrees, hence
\(\tau(\alpha y_\eta)\in A_{n+1}\).

The zero coordinates also belong to \(A_{n+1}\). The coordinatewise stalk grading therefore places \(\kappa_0(y)\) in \(Z_{n+1}\), and it lies in \(K_0\) by construction. This proves the ascent assertion.

### Step 3. Check the descent map

For \(z\in X\), the pair \((\alpha z,0)\) has new coordinates
\[
(\kappa_1(z))_{(0,\eta)}=\alpha z_\eta,\qquad
(\kappa_1(z))_{(1,\eta)}=0.
\]
If \(z\in X_n\), the same root-degree calculation puts every coordinate in \(A_{n+1}\). Thus \(\kappa_1(z)\in(K_1)_{n+1}\).

### Step 4. Recover the inverse degree

Each \(\kappa_i\) is a real-linear equivalence between directly graded real vector spaces. The [[node:kl.algebra.component_transport|homogeneous component theorem]] applied to its degree-one map gives
\[
\operatorname{pr}_n(\kappa_i(y))
=\kappa_i(\operatorname{pr}_{n-1}(y)).
\]
If \(\kappa_i(y)\) is homogeneous of degree \(n\), the left side equals \(\kappa_i(y)\). Injectivity then gives
\(y=\operatorname{pr}_{n-1}(y)\), so the inverse image has degree \(n-1\).

Therefore the forward and inverse maps restrict to the displayed degreewise isomorphisms. In the source shift convention \(M(1)_n=M_{n-1}\), the kernel has the old stalk shifted upward by one.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_eval`: [BottSamelson.lean:1589](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1589).

`OAI.KLInvariance.TitsSpace.bottHeadLeft_kernel_homogeneous`: [BottSamelson.lean:1601](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1601).

`OAI.KLInvariance.TitsSpace.bottHeadKernelEquiv_homogeneous`: [BottSamelson.lean:1618](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1618).

`OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_eval`: [BottSamelson.lean:2056](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2056).

`OAI.KLInvariance.TitsSpace.bottHeadRight_kernel_homogeneous`: [BottSamelson.lean:2071](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2071).

`OAI.KLInvariance.TitsSpace.bottHeadRightKernelEquiv_homogeneous`: [BottSamelson.lean:2084](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L2084).
