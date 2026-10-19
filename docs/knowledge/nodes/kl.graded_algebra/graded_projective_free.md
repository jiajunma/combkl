---
id: kl.notes.graded_projective_free
title: From graded projectivity to a homogeneous free basis
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.notes.graded_nakayama
- kl.sheaves.minimal_cover
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial
  - OAI.KLInvariance.Graded.linearIndependent_of_projective_cover
  - OAI.KLInvariance.Graded.exists_homogeneous_basis_connected
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:472
    format: lean-location
    note: OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:191
    format: lean-location
    note: OAI.KLInvariance.Graded.linearIndependent_of_projective_cover
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:400
    format: lean-location
    note: OAI.KLInvariance.Graded.exists_homogeneous_basis_connected
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
- induction
---

# From graded projectivity to a homogeneous free basis

Let \(A\) be a connected nonnegatively graded Noetherian domain over a field \(k\). A finite projective \(A\)-module with a compatible grading bounded below admits a finite homogeneous basis. In particular this applies to \(A=k[X_1,\ldots,X_N]\), with variables in degree one.

*Proof.*

### Step 1. Choose homogeneous generators minimal modulo the positive ideal

Let \(J=A_{>0}\). Connectedness and nonnegativity give the augmentation quotient \(A/J\simeq k\), so \(J\) is proper. Let \(M\) be finite projective with grading bounded below. Choose finite homogeneous generators by decomposing a finite generating set into homogeneous components. Their images span the finite-dimensional space \(M/JM\).

Choose a basis of \(M/JM\) among these images and retain their homogeneous lifts \(m_1,\ldots,m_r\). Their span \(N\) satisfies \(M=N+JM\). [[node:kl.notes.graded_nakayama|Graded Nakayama]] gives \(N=M\), so
\[
f:A^r\twoheadrightarrow M,\qquad (a_i)\mapsto\sum_i a_im_i
\]
is surjective.

### Step 2. Use projectivity and minimality to control the kernel

Projectivity supplies an \(A\)-linear section \(s:M\to A^r\) with \(fs=1\). Put \(K=\ker f\), and define \(p=1-sf\). Then \(p(A^r)\subseteq K\), and \(p|_K=1\).

Independence of the residues \([m_i]\) proves \(K\subseteq JA^r\): reduce any relation \(\sum a_im_i=0\) modulo \(JM\); each scalar residue of \(a_i\) must be zero. Apply \(p\) to this containment. Since \(p\) is \(A\)-linear,
\[
K=p(K)\subseteq p(JA^r)=Jp(A^r)\subseteq JK.
\]
The reverse containment is automatic, hence \(K=JK\).

### Step 3. Apply the determinant argument to the kernel

Because \(A\) is Noetherian and \(K\subseteq A^r\), choose finite generators \(k_1,\ldots,k_m\) for \(K\). The identity \(K=JK\) gives
\(k_i=\sum_j a_{ij}k_j\) with every \(a_{ij}\in J\).
Let \(C=(\delta_{ij}-a_{ij})\). Then \(C(k_j)_j=0\). Multiplying by the adjugate matrix shows
\[
r_0k_i=0\quad\text{for all }i,\qquad r_0=\det C.
\]
Modulo \(J\), \(C\) is the identity, so \(r_0\equiv1\pmod J\). The ideal \(J\) is proper; therefore \(r_0\ne0\).

### Step 4. Eliminate the kernel and retain the grading

The coefficient ring is a domain, and \(K\) is a submodule of the free module \(A^r\), so multiplication by a nonzero scalar is injective on \(K\). Step 3 forces every generator \(k_i\) to vanish, hence \(K=0\).

Thus \(f\) is an isomorphism, and \(m_1,\ldots,m_r\) are an \(A\)-basis of \(M\). They were chosen homogeneous in Step 1, so this is a homogeneous basis.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.Graded.exists_homogeneous_basis_polynomial`: [GradedModules.lean:472](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L472).

`OAI.KLInvariance.Graded.linearIndependent_of_projective_cover`: [GradedModules.lean:191](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L191).

`OAI.KLInvariance.Graded.exists_homogeneous_basis_connected`: [GradedModules.lean:400](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L400).
