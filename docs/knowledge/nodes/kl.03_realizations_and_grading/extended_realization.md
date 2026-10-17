---
id: kl.notes.extended_realization
title: Extending the Tits form without losing the root data
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses: []
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedForm_spec
  - OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent
  - OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent
  - OAI.KLInvariance.TitsSpace.extended_finrank
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:558
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedForm_spec
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:569
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:575
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:613
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extended_finrank
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:realization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
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

# Extending the Tits form without losing the root data

Assume that the simple-generator set \(I\) is finite. Let \(V_0=\mathbb R^I\) with the Tits form \(B\), normalized by
\[
B(\alpha_i,\alpha_i)=2,\qquad
B(\alpha_i,\alpha_j)=-2\cos(\pi/m_{ij}).
\]
The convention for an infinite Coxeter exponent is \(\cos(\pi/\infty)=1\).

The form can be degenerate. Writing \(K=\ker B\), enlarge the space to
\[
V=V_0\oplus K^*.
\]
There exists a symmetric nondegenerate form \(\widetilde B\) extending \(B\) on \(V_0\). The extended simple roots \((\alpha_i,0)\) and the corresponding linear forms \(\widetilde B((\alpha_i,0),-)\) are both independent. Moreover
\[
\dim V=|I|+\dim K.
\]

*Proof.*

### Step 1. Separate the radical from a nondegenerate part

Let \(K=\{v:B(v,w)=0\text{ for every }w\in V_0\}\). Choose a vector-space complement \(U\), so every vector of \(V_0\) has a unique form \(u+k\).

The restricted form on \(U\) is nondegenerate. Indeed, if \(u\in U\) is orthogonal to all of \(U\), it is also orthogonal to \(K\) by the definition of the radical and symmetry. It is therefore orthogonal to all \(V_0\), so \(u\in K\). Since \(U\cap K=0\), \(u=0\).

### Step 2. Define the extended form explicitly

Identify \(V_0\oplus K^*\) with \(U\oplus K\oplus K^*\), and put
\[
\widetilde B((u,k,\lambda),(u',k',\lambda'))
=B(u,u')+\lambda(k')+\lambda'(k).
\]
Each term is bilinear. Symmetry follows from symmetry of \(B\) and the interchange of the two evaluation terms.

For vectors of the original subspace, \(\lambda=\lambda'=0\), so
\(\widetilde B((u,k,0),(u',k',0))=B(u,u')=B(u+k,u'+k')\).
Thus this genuinely extends the original form.

### Step 3. Check nondegeneracy by three separate tests

Suppose \((u,k,\lambda)\) is orthogonal to every vector. Test against \((0,0,\lambda')\): we obtain \(\lambda'(k)=0\) for all \(\lambda'\in K^*\), hence \(k=0\), since linear functionals separate vectors.

Test against \((0,k',0)\): we obtain \(\lambda(k')=0\) for every \(k'\), so \(\lambda=0\).
Finally test against \((u',0,0)\): \(B(u,u')=0\) for all \(u'\in U\), and Step 1 gives \(u=0\). The radical of the extended form is zero.

### Step 4. Verify the root and normal independence claims

The original simple roots form a basis of \(V_0\). Their inclusion into \(V_0\oplus K^*\) is injective, so their extended vectors remain linearly independent.

Nondegeneracy makes the linear map \(v\mapsto\widetilde B(v,-)\) injective. An injective linear map sends a linearly independent family to a linearly independent family: a vanishing linear combination of their images pulls back to a vanishing combination of the vectors. Thus the corresponding normal forms are independent too.

### Step 5. Compute the dimension

Finite-dimensional duality gives \(\dim K^*=\dim K\). Hence
\(\dim(V_0\oplus K^*)=|I|+\dim K\).
Only the ambient extended form is asserted nondegenerate. Its restriction to a root plane can still be degenerate, which is allowed in the later dihedral arguments.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedForm_spec`: [Tits.lean:558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L558).

`OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent`: [Tits.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L569).

`OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent`: [Tits.lean:575](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L575).

`OAI.KLInvariance.TitsSpace.extended_finrank`: [Tits.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L613).
