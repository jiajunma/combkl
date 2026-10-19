---
id: kl.word.evaluation_grading
title: Homogeneous evaluation and homogeneous lifts to word modules
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.wall_coordinates
- kl.notes.word_stalks
- kl.algebra.homogeneous_subquotients
- kl.algebra.dual_basis_degrees
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottEvaluation_basis_homogeneous
  - OAI.KLInvariance.TitsSpace.bottEvaluation_homogeneous
  - OAI.KLInvariance.TitsSpace.bottEvaluation_component
  - OAI.KLInvariance.TitsSpace.bottCoordinatePiece
  - OAI.KLInvariance.TitsSpace.bottWeightProjection_homogeneous
  - OAI.KLInvariance.TitsSpace.bottStalk_homogeneous
  - OAI.KLInvariance.TitsSpace.bottStalkPiece
  - OAI.KLInvariance.TitsSpace.bottStalkProjection_homogeneous
  - OAI.KLInvariance.TitsSpace.bottStalk_homogeneous_lift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:338
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_basis_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:367
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:384
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_component
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:421
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinatePiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:436
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeightProjection_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:442
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:449
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:462
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:467
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_homogeneous_lift
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read basis-entry induction, homogeneous evaluation, component commutation
    and image grading/lift proofs. Defined the stalk pieces coordinatewise and retained
    the basis-dependent source grading.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Homogeneous evaluation and homogeneous lifts to word modules

Fix a finite-generator Coxeter system and a basis of its real extended realization. Let
\(A=\bigoplus_n A_n\) be its symmetric coefficient algebra with linear generators in degree one. Equip every tensor word module \(M_{\mathbf t}\) with the grading from its standard basis degrees \(d_\gamma\).

Each evaluation preserves degree:
\[
E_{\mathbf t,\eta}((M_{\mathbf t})_n)\subseteq A_n.
\]
For \(J_x=\{\eta:w_{\mathbf t}(\eta)=x\}\), give \(A^{J_x}\) its coordinatewise grading. The image stalk \(M_{\mathbf t}^x\) is a homogeneous submodule, and every homogeneous stalk vector \(z\) of degree \(n\) has a homogeneous lift \(m\in(M_{\mathbf t})_n\) with \(\pi_x(m)=z\).

*Proof.*

### Step 1. Determine the degrees of matrix entries

We prove
\[
(E_{\mathbf t})_{\eta\gamma}\in A_{d_\gamma}
\]
by word induction. For the empty word, the only matrix entry is \(1\in A_0\).

Suppose this is known for \(\mathbf t\). In the block matrix for \(s\mathbf t\), the first column block has entries \(E_{\mathbf t}\) or \(\tau(E_{\mathbf t})\). The coefficient action preserves degree, so each entry in column \((0,\gamma)\) has degree \(d_\gamma\).

The second column block has entries \(\alpha_s E_{\mathbf t}\) or
\(-\alpha_s\tau(E_{\mathbf t})\). Since \(\alpha_s\in A_1\), these have degree \(1+d_\gamma\). Those are exactly the assigned degrees of columns \((1,\gamma)\). This completes the induction.

### Step 2. Evaluate a homogeneous vector

If \(m=\sum_\gamma c_\gamma b_\gamma\) lies in degree \(n\), the basis grading means
\[
c_\gamma\in A_{n-d_\gamma}.
\]
Evaluation expands as
\[
E_{\mathbf t,\eta}(m)
=\sum_\gamma c_\gamma(E_{\mathbf t})_{\eta\gamma}.
\]
Each product has degree \((n-d_\gamma)+d_\gamma=n\) by Step 1. The finite sum therefore lies in \(A_n\).

### Step 3. Commute evaluation with homogeneous components

Write \(m=\sum_j m_j\) as its finite homogeneous decomposition. Step 2 gives \(E_{\mathbf t,\eta}(m_j)\in A_j\). Uniqueness of the homogeneous decomposition in \(A\) then yields
\[
\operatorname{pr}_n(E_{\mathbf t,\eta}(m))
=E_{\mathbf t,\eta}(\operatorname{pr}_n m).
\]
Collecting the same identities over \(\eta\in J_x\) gives the component identity for the weight projection.

### Step 4. Give the image stalk its grading

If a coordinate vector is in the image, write it as \(E_x(m)\). Its degree-\(n\) component is \(E_x(\operatorname{pr}_n m)\), by Step 3, and hence is again in the image.

Thus the image is closed under homogeneous components. Its grading is
\[
(M_{\mathbf t}^x)_n
=\{z\in M_{\mathbf t}^x:z_\eta\in A_n\text{ for every }\eta\in J_x\}.
\]
This is bottStalkPiece, obtained by restricting the coordinatewise grading bottCoordinatePiece. The finite decomposition and its uniqueness descend from the ambient coordinate module.

### Step 5. Lift a homogeneous stalk vector

Let \(z\in(M_{\mathbf t}^x)_n\). Surjectivity of the stalk projection gives some \(v\) with \(\pi_x(v)=z\). Set \(m=\operatorname{pr}_n v\). Then \(m\) has degree \(n\), and Step 3 gives
\[
\pi_x(m)=\operatorname{pr}_n(\pi_x(v))
=\operatorname{pr}_n(z)=z.
\]
This proves the required lift. It is the component projection of any initial lift, exactly as in bottStalk_homogeneous_lift.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottEvaluation_basis_homogeneous`: [BottSamelson.lean:338](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L338).

`OAI.KLInvariance.TitsSpace.bottEvaluation_homogeneous`: [BottSamelson.lean:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L367).

`OAI.KLInvariance.TitsSpace.bottEvaluation_component`: [BottSamelson.lean:384](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L384).

`OAI.KLInvariance.TitsSpace.bottCoordinatePiece`: [BottSamelson.lean:421](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L421).

`OAI.KLInvariance.TitsSpace.bottWeightProjection_homogeneous`: [BottSamelson.lean:436](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L436).

`OAI.KLInvariance.TitsSpace.bottStalk_homogeneous`: [BottSamelson.lean:442](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L442).

`OAI.KLInvariance.TitsSpace.bottStalkPiece`: [BottSamelson.lean:449](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L449).

`OAI.KLInvariance.TitsSpace.bottStalkProjection_homogeneous`: [BottSamelson.lean:462](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L462).

`OAI.KLInvariance.TitsSpace.bottStalk_homogeneous_lift`: [BottSamelson.lean:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L467).
