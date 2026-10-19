---
id: kl.word.wall_coordinates
title: Reflection block coordinates and evaluation matrices
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.evaluation_maps
- kl.notes.bott_samelson
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.wallCoordinate
  - OAI.KLInvariance.ReflectionFrobenius.wallMatrix
  - OAI.KLInvariance.ReflectionFrobenius.wallMatrix_mulVec
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix
  - OAI.KLInvariance.TitsSpace.bottEvaluation_expand
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_cons
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_mulVec_cons
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1137
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.wallCoordinate
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1141
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.wallMatrix
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1146
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.wallMatrix_mulVec
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1213
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluationMatrix
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1216
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_expand
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1225
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_cons
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1247
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_mulVec_cons
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read generic wallCoordinate/wallMatrix and all four cases of bottEvaluationMatrix_cons.
    Made row/column roles and entrywise automorphism explicit, retaining the generic
    map before specializing to a simple reflection.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Reflection block coordinates and evaluation matrices

Let \(A\) be a commutative ring, \(\tau:A\to A\) a ring automorphism, \(\alpha\in A\), and \(J\) a finite index set. For a matrix \(E=(E_{jk})_{j,k\in J}\), write
\[
(\tau E)_{jk}=\tau(E_{jk}),\qquad
(Ev)_j=\sum_{k\in J}E_{jk}v_k.
\]
The automorphism acts on the matrix entries in \(\tau E\).

For a pair of vectors \(v_0,v_1\in A^J\), define the reflection wall-coordinate map
\[
\mathcal W_E(v_0,v_1)
=\bigl(E(v_0+\alpha v_1),\,(\tau E)(v_0-\alpha v_1)\bigr).
\]
Its block matrix is
\[
\begin{pmatrix}
E&\alpha E\\
\tau E&-\alpha\,\tau E
\end{pmatrix}.
\]
Multiplying this matrix by \((v_0,v_1)\) gives the two displayed coordinate vectors by distributivity of the finite sums. The source names the map `wallCoordinate` and the matrix `wallMatrix`.

## The evaluation matrix of a word

For a finite-generator Coxeter system, now take \(A\) to be the symmetric algebra of its real extended realization. For its tensor word module, let \((b_\gamma)_{\gamma\in J_{\mathbf t}}\) be its standard word basis. Define
\[
(E_{\mathbf t})_{\eta\gamma}
=E_{\mathbf t,\eta}(b_\gamma).
\]
Rows record evaluations; columns record basis vectors. If
\(m=\sum_\gamma v_\gamma b_\gamma\), linearity gives
\[
E_{\mathbf t,\eta}(m)
=\sum_\gamma (E_{\mathbf t})_{\eta\gamma}v_\gamma.
\]
Thus full evaluation is multiplication by this matrix after taking basis coordinates.

## Prepending one reflection

Let \(s\) act by \(\tau\), with root polynomial \(\alpha_s\). The new basis vectors are
\[
b_{(0,\gamma)}=1\otimes b_\gamma,\qquad
b_{(1,\gamma)}=1\otimes\alpha_s b_\gamma.
\]
The evaluation recursion gives all four blocks:
\[
\begin{array}{c|cc}
&b_{(0,\gamma)}&b_{(1,\gamma)}\\
(0,\eta)&(E_{\mathbf t})_{\eta\gamma}
 &\alpha_s(E_{\mathbf t})_{\eta\gamma}\\
(1,\eta)&\tau((E_{\mathbf t})_{\eta\gamma})
 &-\alpha_s\tau((E_{\mathbf t})_{\eta\gamma})
\end{array}
\]
The last entry uses \(\tau(\alpha_s)=-\alpha_s\). Therefore the new evaluation matrix is exactly the reflection block matrix for \(E_{\mathbf t}\).

The empty-word matrix is \((1)\). For one letter this construction gives
\[
E_s=\begin{pmatrix}1&\alpha_s\\1&-\alpha_s\end{pmatrix}.
\]

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.wallCoordinate`: [Frobenius.lean:1137](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1137).

`OAI.KLInvariance.ReflectionFrobenius.wallMatrix`: [Frobenius.lean:1141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1141).

`OAI.KLInvariance.ReflectionFrobenius.wallMatrix_mulVec`: [Frobenius.lean:1146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1146).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix`: [Frobenius.lean:1213](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1213).

`OAI.KLInvariance.TitsSpace.bottEvaluation_expand`: [Frobenius.lean:1216](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1216).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_cons`: [Frobenius.lean:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1225).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_mulVec_cons`: [Frobenius.lean:1247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1247).
