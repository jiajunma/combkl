---
id: kl.notes.bott_samelson
title: Word objects and Bott–Samelson tensor induction
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.tensor_pairing
- kl.notes.extended_realization
- kl.notes.reflection_frobenius
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSamelson
  - OAI.KLInvariance.TitsSpace.BottSamelsonModule
  - OAI.KLInvariance.TitsSpace.BottIndex
  - OAI.KLInvariance.TitsSpace.bottWeight
  - OAI.KLInvariance.TitsSpace.bottBasis
  - OAI.KLInvariance.TitsSpace.bottDegree
  - OAI.KLInvariance.TitsSpace.bottPiece
  - OAI.KLInvariance.TitsSpace.bottSamelsonRight
  - OAI.KLInvariance.TitsSpace.bottSamelsonDuality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:394
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSamelson
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:399
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottSamelsonModule
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:947
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottIndex
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1056
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:967
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:957
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottDegree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1014
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPiece
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:405
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSamelsonRight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:401
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSamelsonDuality
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:normalization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Word objects and Bott–Samelson tensor induction

Let \(A\) be the symmetric coefficient algebra of the extended realization. For a simple reflection \(s\), write \(A^s\) for the subalgebra fixed by its coefficient action and \(\alpha_s\) for its degree-one root polynomial.

For a word \(\mathbf s\), the word module is defined recursively by
\[
M_{\varnothing}=A,\qquad
M_{s\mathbf t}=A\otimes_{A^s}M_{\mathbf t}.
\]
The tensor relation identifies \((ar)\otimes m\) with \(a\otimes(rm)\) for \(r\in A^s\).

## The two coefficient actions

The empty-word module has the usual left and right multiplication by \(A\). At an induction step, the left action is
\[
c(a\otimes m)=(ca)\otimes m,
\]
and the right action is
\[
(a\otimes m)\cdot c=a\otimes(m\cdot c).
\]
The old right action commutes with the old left \(A\)-action. It therefore respects the tensor relation over \(A^s\), and it commutes with the new left action.

## A recursively constructed finite basis

The reflection Frobenius extension has \(A^s\)-basis \(1,\alpha_s\). If \((b_\varepsilon)\) is an \(A\)-basis of \(M_{\mathbf t}\), then
\((b_\varepsilon,\alpha_s b_\varepsilon)_\varepsilon\) is an \(A^s\)-basis. Extending scalars gives the \(A\)-basis
\[
b_{(a,\varepsilon)}=1\otimes\alpha_s^a b_\varepsilon,
\qquad a\in\{0,1\}.
\]
Starting with \(b_\varnothing=1\), a word of length \(m\) therefore has \(2^m\) basis vectors indexed by \(\{0,1\}^m\).

Their degrees are
\[
d_\varepsilon=\varepsilon_1+\cdots+\varepsilon_m.
\]
The word grading is defined by the coefficient condition
\[
\sum_\varepsilon c_\varepsilon b_\varepsilon\in(M_{\mathbf s})_n
\quad\Longleftrightarrow\quad
c_\varepsilon\in A_{n-d_\varepsilon}\text{ for every }\varepsilon.
\]
The coefficient decomposition gives a unique finite homogeneous decomposition of every vector.

## Evaluation indices and group weights

The same finite index set labels the evaluation coordinates. Its group-weight function is
\[
w(\varepsilon)=s_1^{\varepsilon_1}\cdots s_m^{\varepsilon_m}.
\]
These group labels are used to group evaluations into weight stalks.

For one letter \(s\), the basis vectors \(1\otimes1\) and \(1\otimes\alpha_s\) evaluate to \((1,1)\) and \((\alpha_s,-\alpha_s)\) in the coordinates labelled \(1,s\). Each basis vector therefore contributes to both weight coordinates. The basis degree and the coordinate's group label describe two parts of the construction.

## The induced pairing

The empty-word pairing is multiplication in \(A\). At a prepending step, let \(\operatorname{tr}_s:A\to A^s\) be the reflection trace. The new pairing satisfies
\[
\langle a\otimes m,b\otimes n\rangle
=ab\,\operatorname{tr}_s(\langle m,n\rangle).
\]
The trace value is included in \(A\). The [[node:kl.notes.tensor_pairing|tensor-pairing theorem]] proves that this is a perfect pairing and preserves symmetry and balance of the right coefficient action.

The degree theorem [[node:kl.word.pairing_degree]] proves
\[
\langle(M_{\mathbf s})_i,(M_{\mathbf s})_j\rangle
\subseteq A_{i+j-|\mathbf s|}.
\]
All these constructions apply to any word. For a reduced word, the later top-stalk theorem identifies its top coordinate with the degree-zero coefficient module.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSamelson`: [Frobenius.lean:394](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L394).

`OAI.KLInvariance.TitsSpace.BottSamelsonModule`: [Frobenius.lean:399](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L399).

`OAI.KLInvariance.TitsSpace.BottIndex`: [Frobenius.lean:947](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L947).

`OAI.KLInvariance.TitsSpace.bottWeight`: [Frobenius.lean:1056](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1056).

`OAI.KLInvariance.TitsSpace.bottBasis`: [Frobenius.lean:967](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L967).

`OAI.KLInvariance.TitsSpace.bottDegree`: [Frobenius.lean:957](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L957).

`OAI.KLInvariance.TitsSpace.bottPiece`: [Frobenius.lean:1014](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1014).

`OAI.KLInvariance.TitsSpace.bottSamelsonRight`: [Frobenius.lean:405](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L405).

`OAI.KLInvariance.TitsSpace.bottSamelsonDuality`: [Frobenius.lean:401](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L401).
