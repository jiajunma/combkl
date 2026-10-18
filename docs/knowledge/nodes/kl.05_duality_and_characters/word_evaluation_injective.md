---
id: kl.detail.word_evaluation_injective
title: Integral injectivity of full word evaluation
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.bott_samelson
- kl.notes.reflection_frobenius
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_injective
  - OAI.KLInvariance.TitsSpace.bottEvaluation_injective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1213
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluationMatrix
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1263
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1290
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_injective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Integral injectivity of full word evaluation

For every word \(\mathbf s\), simultaneous evaluation at all subexpressions is an injective map
\[
E_{\mathbf s}:B_{\mathbf s}\longrightarrow A^{\{0,1\}^{|\mathbf s|}}.
\]
The assertion holds over the actual symmetric coefficient algebra \(A\), before localization.

*Proof.*

### Step 1. Express evaluation in a free basis

Tensor induction gives the word module a basis indexed by subexpressions. Let the matrix \(E\) have entries equal to the evaluations of those basis vectors. Linearity gives \(\operatorname{ev}(m)=E v\), where \(v\) is the basis-coordinate vector of \(m\). It suffices to prove injectivity of multiplication by this matrix.

For the empty word, the module and its coordinate space are both \(A\), and the matrix is \((1)\). This starts induction on word length.

### Step 2. Write the matrix for an added letter

Add a simple reflection \(s\), write \(\alpha\) for its nonzero root polynomial, and write \(\tau\) for its action on \(A\). The rank-two Frobenius basis is \(1,\alpha\). Split an input vector into \(v_0,v_1\). The new evaluations are
\[
E(v_0+\alpha v_1),\qquad \tau(E)(v_0-\alpha v_1),
\]
where \(\tau(E)\) means apply \(\tau\) entrywise. These two blocks follow by evaluating the two basis tensors and using \(\tau(\alpha)=-\alpha\).

### Step 3. Prove injectivity of the second block matrix

If \(\tau(E)a=\tau(E)b\), apply \(\tau^{-1}\) to every coordinate. Because it preserves sums and products, the resulting equality is
\(E\tau^{-1}(a)=E\tau^{-1}(b)\). The induction hypothesis and injectivity of \(\tau^{-1}\) give \(a=b\). Thus both block matrices are injective.

### Step 4. Recover both input halves

Equal new evaluations for \(v,w\) now imply
\[
v_0+\alpha v_1=w_0+\alpha w_1,\qquad
v_0-\alpha v_1=w_0-\alpha w_1.
\]
Subtracting gives \(2\alpha(v_1-w_1)=0\). The coefficient algebra is a domain of characteristic zero and \(\alpha\ne0\), so coordinatewise cancellation gives \(v_1=w_1\). Substitution into the first equation gives \(v_0=w_0\).

This proves matrix injectivity for the longer word. Finally the basis-coordinate map is itself injective, so the evaluation map on the actual word module is injective.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix`: [Frobenius.lean:1213](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1213).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_injective`: [Frobenius.lean:1263](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1263).

`OAI.KLInvariance.TitsSpace.bottEvaluation_injective`: [Frobenius.lean:1290](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1290).
