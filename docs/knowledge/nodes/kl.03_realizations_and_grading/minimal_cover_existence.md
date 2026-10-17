---
id: kl.notes.minimal_cover_existence
title: Constructing a minimal graded free cover
kind: theorem
status: proved
primary_topic: kl.03_realizations_and_grading
topics:
- kl.03_realizations_and_grading
uses:
- kl.sheaves.minimal_cover
- kl.notes.graded_nakayama
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.exists_minimalCover
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1182
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.exists_minimalCover
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:bmp
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

# Constructing a minimal graded free cover

Assume \(A\) is nonnegatively graded over a field \(k\), and every element of \(A\) is congruent to a scalar modulo \(A_{>0}\). Every finite nonnegatively graded module \(M\) has a minimal graded free cover.

*Proof.*

### Step 1. Reduce generation to the scalar quotient

Put \(J=A_{>0}\). The coefficient-ring hypothesis says that every \(a\in A\) is congruent modulo \(J\) to a scalar from \(k\). A finite set of generators of \(M\) therefore spans \(M/JM\) as a vector space over \(k\): in any expression \(\sum a_im_i\), replace each \(a_i\) by its scalar residue.

Replace the generators by their finitely many homogeneous components. Their residues still span, and are homogeneous. Choose a basis of \(M/JM\) from these homogeneous residues, and choose corresponding homogeneous lifts \(m_i\in M_{d_i}\). Since \(M\) is nonnegative, every nonzero lift has \(d_i\ge0\).

### Step 2. Prove that the chosen lifts generate M

Let \(N=\sum_iAm_i\). This is a homogeneous submodule, because its generators are homogeneous and scalar multiplication respects degrees. Their residue classes span \(M/JM\), so for every \(m\in M\) there are scalars \(c_i\) with
\(m-\sum_ic_im_i\in JM\).
Thus \(M=N+JM\).

Apply the graded Nakayama argument to \(N\). Its homogeneous closure and the nonnegative lower bound have just been checked, so \(N=M\).

### Step 3. Build the free graded source and its map

Take a free module \(F=\bigoplus_iAe_i\), with \(\deg e_i=d_i\), and define \(f:F\to M\) by \(f(e_i)=m_i\). A term \(ae_i\), with \(a\) homogeneous of degree \(r\), maps to \(am_i\) of degree \(r+d_i\). Therefore \(f\) preserves grading. Step 2 proves that it is surjective. Finiteness of the basis makes \(F\) finite free and nonnegatively graded.

### Step 4. Check minimality coefficient by coefficient

Suppose \(\sum_i a_ie_i\in\ker f\). Reduce
\(\sum_i a_im_i=0\) modulo \(JM\).
Choose scalar residues \(c_i\) for the \(a_i\). We obtain
\(\sum_i c_i[m_i]=0\).
The residue classes \([m_i]\) are linearly independent over \(k\), so every \(c_i=0\). Hence every \(a_i\in J\), and
\(\sum_i a_ie_i\in JF\).

Thus \(\ker f\subseteq JF\), exactly the minimal-cover condition. The source module, grading, surjection, and kernel containment have all been constructed explicitly.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.exists_minimalCover`: [GradedModules.lean:1182](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1182).
