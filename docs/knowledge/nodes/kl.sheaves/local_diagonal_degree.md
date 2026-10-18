---
id: kl.detail.local_diagonal_degree
title: A nonzero local diagonal forces a strict half-degree bound
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.local_intersection
- kl.detail.graded_character
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:186
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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

# A nonzero local diagonal forces a strict half-degree bound

Let \(x<b\), and let \(m_i\) be a homogeneous stalk basis with dual basis \(\lambda_i\) and degrees \(d_i\). If
\[
\lambda_i(I_x\lambda_i)\ne0,
\]
then
\[
2d_i<d(x,b).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).

**How to read this entry:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compute the degree before using minimality

Let \(m_i\) have degree \(d_i\), and let \(\lambda_i\) be its dual basis functional. Its degree is \(-d_i\).
The inverse stalk–costalk duality has shift \(d=d(x,b)\), so
\(I_x\lambda_i\) is homogeneous of degree \(d-d_i\).
Applying \(\lambda_i\) to it gives a homogeneous coefficient
\[
a_i=\lambda_i(I_x\lambda_i)\in A_{d-2d_i}.
\]

### Step 2. Put that coefficient in the positive ideal

For \(x<b\), the boundary-cover minimality condition says
\(\operatorname{im}I_x=K_x\subseteq A_{>0}B^x\).
Write \(I_x\lambda_i=\sum_j r_jv_j\) with \(r_j\in A_{>0}\). Since \(\lambda_i\) is \(A\)-linear,
\(a_i=\sum_jr_j\lambda_i(v_j)\in A_{>0}\).

### Step 3. Use the nonzero hypothesis

By assumption \(a_i\ne0\). A nonzero homogeneous element of the positive ideal has positive degree. Negative-degree pieces of the coefficient ring vanish, and the degree-zero component of every element in the positive ideal is zero. Thus the homogeneous degree \(d-2d_i\) must be strictly positive.

Rearranging gives \(2d_i<d\).

### Step 4. Keep the exact logical scope

The proof used the nonvanishing of this particular diagonal coefficient in Step 3. Without it, zero lies in every homogeneous subspace and no degree conclusion follows from the same calculation. Lean proves this implication with the nonzero hypothesis; it does not supply that hypothesis for every diagonal of every basis.

Accordingly this lemma cannot be substituted for the preprint's unconditional KL-character normalization. The R-first invariance route does not make that substitution.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.localIntersection_diagonal_strict_degree`: [PositiveTransfer.lean:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186).
