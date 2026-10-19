---
id: kl.sheaves.word_polynomial_stalks
title: Free word stalks and root quotients in polynomial coordinates
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_sheaf
- kl.detail.word_standard_stalks
- kl.detail.coefficient_change
- kl.detail.polynomial_labels
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.TitsSpace.symmetricLabel
  - OAI.KLInvariance.TitsSpace.symmetricLabel_represents
  - OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient
  - OAI.KLInvariance.TitsSpace.bottPolynomialSheaf
  - OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_free
  - OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_quotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:250
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricLabel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:253
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.symmetricLabel_represents
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:257
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:417
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialSheaf
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:422
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:426
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:342
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:348
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read symmetricLabel, the actual upper-quotient package and coefficientChange_upperQuotient,
    then bottPolynomialSheaf/free/quotient. Expanded both kernel directions and basis
    transport; preserved the arbitrary word and interval.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Free word stalks and root quotients in polynomial coordinates

Fix a finite-generator Coxeter system and a finite basis of its real extended realization \(V\). Put
\[
A=\operatorname{Sym}_{\mathbb R}(V),\qquad
P=\mathbb R[X_i:i\text{ indexes the chosen basis}],
\]
and let \(e:A\xrightarrow{\sim}P\) be the induced graded algebra isomorphism.

For any word \(\mathbf t\), take its graded pair-projection sheaf on a Bruhat interval \([u,b]\), and transport its coefficients through \(e\). Denote the resulting polynomial word sheaf by \(S_P\).

Every vertex module of \(S_P\) is finite free over \(P\). For an upward reflection edge \(E:x\to y\), let \(\alpha_E\in A\) be its symmetric root label and \(\gamma_E=e(\alpha_E)\in P\). The upper restriction is surjective with
\[
\ker(\rho_E^+:S_P^y\to S_P^E)=\gamma_E S_P^y.
\]
Consequently \(S_P^E\simeq S_P^y/\gamma_E S_P^y\), and its upper restriction kernel is a free \(P\)-module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Obtain the symmetric-coordinate upper quotient

Let \(t\) be the reflection labelling \(E\), so \(tx=y\) and \(\ell(x)<\ell(y)\). The symmetric label is
\(\alpha_E=\iota(\operatorname{embed}(a_E))\), where \(a_E\) is the positive root representing \(t\).

The [[node:kl.detail.word_standard_stalks|free-word-stalk theorem]] applies to \(\mathbf t\), this root, and the upward edge. It gives finite free stalks and
\[
\ker(\rho_{A,E}^+)=\alpha_E S_A^y.
\]
The pair-projection upper map is surjective. These two facts are exactly the source's bottGradedProjectionSheaf_upperQuotient statement.

### Step 2. Transport the scalar action

The transported module \({}^e M\) has the same additive group as \(M\), with
\[
p\cdot_{{}^eM}m=e^{-1}(p)m.
\]
Each transported restriction map acts by the same underlying function. Surjectivity of the upper restriction therefore persists.

If \(m\) lies in the new upper kernel, its underlying vector lies in the old kernel. Write \(m=\alpha_E n\) there. In the transported action,
\[
\gamma_E\cdot_{{}^eM}n
=e^{-1}(e(\alpha_E))n
=\alpha_E n=m.
\]
This proves one kernel containment. Conversely, every new multiple
\(\gamma_E n\) has underlying vector \(\alpha_E n\), which the old restriction kills. This proves the other containment.

### Step 3. Transport a finite basis

Let \(b_1,\ldots,b_r\) be an \(A\)-basis of an old stalk. If
\(m=\sum_i a_i b_i\), then in the transported module
\[
m=\sum_i e(a_i)\cdot_{{}^eM} b_i.
\]
Thus the same underlying vectors span over \(P\). A relation
\(\sum_i p_i\cdot b_i=0\) becomes
\(\sum_i e^{-1}(p_i)b_i=0\) over \(A\). Independence gives each \(e^{-1}(p_i)=0\), and hence each \(p_i=0\). This proves finite freeness over \(P\).

### Step 4. Check the grading and the label

The algebra isomorphism sends each vector generator to its linear coordinate polynomial. It therefore preserves the degree-one grading. The transported module pieces are the old pieces on the same underlying real vector space, and the restriction maps remain degree-preserving.

The symmetric root label consequently becomes precisely its polynomial root label \(\gamma_E\), which is nonzero and homogeneous of degree one.

### Step 5. Identify the edge quotient and its kernel module

The surjective upper map with kernel \(\gamma_E S_P^y\) factors through a bijective linear map
\[
S_P^y/\gamma_E S_P^y\longrightarrow S_P^E.
\]
Injectivity follows because a representative maps to zero exactly when it is in the displayed kernel.

Finally \(P\) is a domain and \(\gamma_E\ne0\). Multiplication by \(\gamma_E\) is injective on the free stalk and maps it onto its upper kernel. This identifies that kernel with a finite free \(P\)-module. For a homogeneous stalk basis, multiplication by \(\gamma_E\) raises each basis degree by one.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.symmetricLabel`: [Support.lean:250](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L250).

`OAI.KLInvariance.TitsSpace.symmetricLabel_represents`: [Support.lean:253](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L253).

`OAI.KLInvariance.TitsSpace.bottGradedProjectionSheaf_upperQuotient`: [Support.lean:257](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L257).

`OAI.KLInvariance.TitsSpace.bottPolynomialSheaf`: [Support.lean:417](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L417).

`OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_free`: [Support.lean:422](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L422).

`OAI.KLInvariance.TitsSpace.bottPolynomialSheaf_quotient`: [Support.lean:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free`: [Support.lean:342](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L342).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient`: [Support.lean:348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L348).
