---
id: kl.word.scaled_coordinate_lifts
title: Scaled coordinate lifts and the evaluation denominator
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.detail.word_evaluation_injective
- kl.notes.word_stalks
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottCoordinateDenominator
  - OAI.KLInvariance.TitsSpace.bottCoordinateDenominator_ne_zero
  - OAI.KLInvariance.TitsSpace.bottEvaluation_contains_scaled_coordinates
  - OAI.KLInvariance.TitsSpace.bottCoordinateLift
  - OAI.KLInvariance.TitsSpace.bottCoordinateLift_eval
  - OAI.KLInvariance.TitsSpace.bottCoordinateLift_supported
  - OAI.KLInvariance.TitsSpace.bottCoordinateExpansion
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1317
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateDenominator
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1321
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateDenominator_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1328
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_contains_scaled_coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1448
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateLift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1452
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateLift_eval
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1458
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateLift_supported
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1465
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCoordinateExpansion
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Scaled coordinate lifts and the evaluation denominator

Fix a word \(\mathbf s\) for a finite-generator Coxeter system. Let \(A\) be the symmetric coefficient algebra of its real extended realization, \(M=M_{\mathbf s}\) the word module, and \(J\) its finite subexpression index set. Use the standard word basis to identify \(M\) with \(A^J\). Full evaluation is then represented by a square matrix
\[
E:A^J\longrightarrow A^J.
\]
Define the evaluation denominator \(\Delta=\det E\). Then \(\Delta\ne0\), and every coordinate tuple \(v\in A^J\) has a scaled lift:
\[
\exists m\in M,\qquad E(m)=\Delta v.
\]
In particular, there are elements \(c_\varepsilon\in M\) satisfying
\[
E_\eta(c_\varepsilon)=
\begin{cases}
\Delta,&\eta=\varepsilon,\\
0,&\eta\ne\varepsilon.
\end{cases}
\]
Each \(c_\varepsilon\) is supported at weight \(w(\varepsilon)\), and every \(m\in M\) satisfies
\[
\Delta m=\sum_{\varepsilon\in J}E_\varepsilon(m)c_\varepsilon.
\]

*Proof.*

### Step 1. Establish the nonzero determinant

The full evaluation matrix is injective over the domain \(A\). Suppose \(\det E=0\). Over the fraction field of \(A\), a square matrix with zero determinant has a nonzero vector \(z\) in its kernel.

The finite list of coordinates of \(z\) has a common nonzero denominator \(a\in A\). Then \(v=az\) has coordinates in \(A\), is nonzero, and satisfies \(Ev=aEz=0\). This contradicts injectivity over \(A\). Thus \(\Delta\ne0\).

### Step 2. Construct a lift with the adjugate matrix

The adjugate matrix is the transpose of the matrix of signed minors. Cofactor expansion gives
\[
E\,\operatorname{adj}(E)=(\det E)I.
\]
Its entries lie in \(A\). For \(v\in A^J\), let \(m\) have basis-coordinate vector \(\operatorname{adj}(E)v\). Then
\[
E(m)=E\operatorname{adj}(E)v=\Delta v,
\]
proving the scaled-lift statement.

### Step 3. Lift an individual coordinate

Take \(v\) to be the standard coordinate vector at \(\varepsilon\), and choose the resulting \(c_\varepsilon\). Its evaluation is \(\Delta\) at \(\varepsilon\) and zero elsewhere.

If \(w(\eta)\ne w(\varepsilon)\), then \(\eta\ne\varepsilon\), so \(E_\eta(c_\varepsilon)=0\). This is precisely support at \(w(\varepsilon)\).

### Step 4. Reconstruct a scaled word element

Evaluate the proposed sum at a fixed coordinate \(\eta\):
\[
E_\eta\!\left(\sum_\varepsilon E_\varepsilon(m)c_\varepsilon\right)
=\sum_\varepsilon E_\varepsilon(m)E_\eta(c_\varepsilon)
=\Delta E_\eta(m).
\]
This equals \(E_\eta(\Delta m)\). The equality holds at every coordinate, and full evaluation is injective, so the two word elements are equal.

### Step 5. Compute the one-letter denominator

In the basis \(1\otimes1,1\otimes\alpha\),
\[
E=\begin{pmatrix}1&\alpha\\ 1&-\alpha\end{pmatrix},
\qquad \Delta=-2\alpha.
\]
The scaled coordinate lifts have evaluation pairs \((-2\alpha,0)\) and \((0,-2\alpha)\). Both are compatible modulo \(\alpha\), and the expansion multiplies any compatible pair \((f,g)\) by \(-2\alpha\).

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottCoordinateDenominator`: [Frobenius.lean:1317](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1317).

`OAI.KLInvariance.TitsSpace.bottCoordinateDenominator_ne_zero`: [Frobenius.lean:1321](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1321).

`OAI.KLInvariance.TitsSpace.bottEvaluation_contains_scaled_coordinates`: [Frobenius.lean:1328](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1328).

`OAI.KLInvariance.TitsSpace.bottCoordinateLift`: [Frobenius.lean:1448](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1448).

`OAI.KLInvariance.TitsSpace.bottCoordinateLift_eval`: [Frobenius.lean:1452](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1452).

`OAI.KLInvariance.TitsSpace.bottCoordinateLift_supported`: [Frobenius.lean:1458](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1458).

`OAI.KLInvariance.TitsSpace.bottCoordinateExpansion`: [Frobenius.lean:1465](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1465).
