---
id: kl.detail.word_evaluation_injective
title: Integral injectivity of full word evaluation
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.evaluation_maps
- kl.word.wall_coordinates
- kl.word.wall_injectivity
- kl.word.simple_frobenius_data
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottEvaluation_expand
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_cons
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_mulVec_cons
  - OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_injective
  - OAI.KLInvariance.TitsSpace.bottEvaluation_injective
source:
  spans:
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
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Rewrote the theorem with its actual finite-generator realization context
    and explicit basis/matrix composition. Matched the empty-word and cons proofs
    and linked the independent generic block-injectivity theorem.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Integral injectivity of full word evaluation

Fix a Coxeter system with finite simple-generator set, its real extended realization \(V\), and the symmetric coefficient algebra \(A=\operatorname{Sym}_{\mathbb R}(V)\). For every word \(\mathbf t\), full evaluation is an injective \(A\)-linear map
\[
E_{\mathbf t}:M_{\mathbf t}\longrightarrow A^{J_{\mathbf t}}.
\]
Thus two word vectors are equal whenever all their subexpression evaluations agree.

*Proof.*

### Step 1. Express evaluation through basis coordinates

The word basis gives a linear isomorphism
\[
c_{\mathbf t}:M_{\mathbf t}\xrightarrow{\sim}A^{J_{\mathbf t}}.
\]
By the evaluation expansion,
\[
E_{\mathbf t}(m)=\mathsf E_{\mathbf t}\,c_{\mathbf t}(m),
\]
where the matrix \(\mathsf E_{\mathbf t}\) has entry
\(E_{\mathbf t,\eta}(b_\gamma)\) in row \(\eta\), column \(\gamma\).
We prove injectivity of multiplication by \(\mathsf E_{\mathbf t}\) by induction on the word.

### Step 2. Start with the empty word

There is one subexpression. The module is \(A\), its basis is \(1\), and its evaluation is the identity. Thus \(\mathsf E_\varnothing=(1)\), and its multiplication map is injective.

### Step 3. Identify the matrix after prepending a letter

Assume multiplication by \(\mathsf E_{\mathbf t}\) is injective. Prepend \(s\), write \(\tau=\chi_s\), and let \(\alpha_s\) be its root polynomial. Splitting the new basis by its first bit gives
\[
\mathsf E_{s\mathbf t}=
\begin{pmatrix}
\mathsf E_{\mathbf t}&\alpha_s\mathsf E_{\mathbf t}\\
\tau(\mathsf E_{\mathbf t})&-\alpha_s\tau(\mathsf E_{\mathbf t})
\end{pmatrix}.
\]
These four blocks come from the evaluation of
\(1\otimes b_\gamma\) and \(1\otimes\alpha_s b_\gamma\) at the two first-bit choices. The sign in the lower-right block is \(\tau(\alpha_s)=-\alpha_s\).

### Step 4. Verify the wall-injectivity hypotheses

The symmetric algebra of the real vector space \(V\) is a polynomial algebra after choosing a basis, hence a domain of characteristic zero. The coefficient action \(\tau\) is a ring automorphism. The simple-reflection Frobenius data give \(\alpha_s\ne0\).

The [[node:kl.word.wall_injectivity|wall-injectivity theorem]] therefore applies to the matrix from Step 3 and the induction hypothesis. It proves injectivity of \(\mathsf E_{s\mathbf t}\). Since the tail word is shorter by one letter, Steps 2–4 establish the assertion for every finite word.

### Step 5. Return to word vectors

If \(E_{\mathbf t}(m)=E_{\mathbf t}(n)\), Step 1 and matrix injectivity give
\(c_{\mathbf t}(m)=c_{\mathbf t}(n)\). The coordinate map is an isomorphism, so \(m=n\).

For one letter, this recovery is the calculation
\[
(f,g)=(u+\alpha_s v,u-\alpha_s v).
\]
Equal outputs force equality of \(2\alpha_s v\), then of \(v\), and then of \(u\). The induction repeats this recovery with the old evaluation matrix in each block.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottEvaluation_expand`: [Frobenius.lean:1216](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1216).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_cons`: [Frobenius.lean:1225](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1225).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_mulVec_cons`: [Frobenius.lean:1247](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1247).

`OAI.KLInvariance.TitsSpace.bottEvaluationMatrix_injective`: [Frobenius.lean:1263](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1263).

`OAI.KLInvariance.TitsSpace.bottEvaluation_injective`: [Frobenius.lean:1290](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1290).
