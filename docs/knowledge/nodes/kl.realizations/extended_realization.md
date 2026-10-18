---
id: kl.notes.extended_realization
title: Nondegeneracy and independence in the extended root space
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.tits_form
- kl.realization.radical_extension
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

# Nondegeneracy and independence in the extended root space

Let \(I\) be finite, let \(V_0=\mathbb R^I\) carry its Tits form \(B\), and let \(K\) be the radical. Choose a linear projection \(p:V_0\to K\) that fixes every element of \(K\). On \(E=V_0\oplus K^*\), use
\[
B_p((v,\phi),(w,\psi))
=B(v,w)+\phi(pw)+\psi(pv).
\]
Then \(B_p\) is symmetric and nondegenerate and restricts to \(B\) on \(V_0\oplus0\). Both families
\[
\widetilde\alpha_i=(\alpha_i,0),\qquad
\widetilde\nu_i=B_p(\widetilde\alpha_i,-)
\]
are linearly independent. Finally,
\[
\dim E=|I|+\dim K.
\]
These conclusions also hold for the extended form chosen from this construction in the Lean development.

*Proof.*

### Step 1. Produce the projection

Choose a vector-space complement \(U\) of \(K\). Write each \(v\in V_0\) uniquely as \(u+k\) with \(u\in U\), \(k\in K\), and set \(p(v)=k\). Uniqueness of the decomposition proves linearity. If \(v=k\in K\), its decomposition is \(0+k\), so \(p(k)=k\).

### Step 2. Check symmetry and restriction

Each summand in the displayed definition is bilinear. Symmetry of \(B\) gives
\[
\begin{aligned}
B_p((w,\psi),(v,\phi))
 &=B(w,v)+\psi(pv)+\phi(pw)\\
 &=B(v,w)+\phi(pw)+\psi(pv)\\
 &=B_p((v,\phi),(w,\psi)).
\end{aligned}
\]
For two embedded vectors \((v,0),(w,0)\), the two evaluation terms vanish. Hence their pairing is \(B(v,w)\).

### Step 3. Test orthogonality against the added dual directions

Suppose \(x=(v,\phi)\) satisfies \(B_p(x,y)=0\) for every \(y\in E\). Taking \(y=(0,\psi)\) gives
\[
0=B_p((v,\phi),(0,\psi))=\psi(pv)
\]
for every \(\psi\in K^*\). Linear functionals separate vectors, so \(pv=0\).

To see the separation explicitly, if \(pv\ne0\), extend that vector to a basis of \(K\) and define a functional taking value one on it. This contradicts the displayed equality.

### Step 4. Test against radical vectors

For \(k\in K\), symmetry gives \(B(v,k)=B(k,v)=0\). Also \(p(k)=k\) and \(pv=0\). Taking \(y=(k,0)\) therefore gives
\[
0=B_p((v,\phi),(k,0))=0+\phi(k)+0.
\]
Thus \(\phi\) vanishes on all of \(K\), so \(\phi=0\).

### Step 5. Test against all original vectors

Taking \(y=(w,0)\), with arbitrary \(w\in V_0\), now gives \(B(v,w)=0\). Hence \(v\in K\). The projection fixes radical vectors, so \(pv=v\). Step 3 showed \(pv=0\), and therefore \(v=0\).

We have proved that a vector orthogonal to every vector in the second argument is zero. Symmetry gives the same assertion for the other argument. This proves nondegeneracy.

### Step 6. Prove root and normal independence

Suppose \(\sum_i c_i\widetilde\alpha_i=0\). Projecting to \(V_0\) gives \(\sum_i c_i\alpha_i=0\). Since the \(\alpha_i\) form a basis, every coefficient is zero.

Now suppose \(\sum_i c_i\widetilde\nu_i=0\). Bilinearity rewrites this equation as
\[
B_p\left(\sum_i c_i\widetilde\alpha_i,-\right)=0.
\]
Nondegeneracy forces \(\sum_i c_i\widetilde\alpha_i=0\), and root independence forces all \(c_i=0\). Thus the normals are independent as well.

### Step 7. Compute the dimension

The simple-root basis has \(|I|\) elements. A basis of the finite-dimensional radical \(K\) and its dual basis have the same size. Consequently
\[
\dim E=\dim V_0+\dim K^*=|I|+\dim K.
\]
The dimension-minimality theorem shows that this number is attained by the smallest possible nondegenerate extension preserving the embedded form.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedForm_spec`: [Tits.lean:558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L558).

`OAI.KLInvariance.TitsSpace.extendedRoot_linearIndependent`: [Tits.lean:569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L569).

`OAI.KLInvariance.TitsSpace.extendedNormal_linearIndependent`: [Tits.lean:575](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L575).

`OAI.KLInvariance.TitsSpace.extended_finrank`: [Tits.lean:613](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L613).
