---
id: kl.algebra.reflected_dual_character
title: Character reflection from a homogeneous dual equivalence
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.dual_basis_degrees
- kl.detail.graded_character
- kl.algebra.character_basis_independence
- kl.hecke.polynomial_reflection
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.degree_le_of_dual_equiv
  - OAI.KLInvariance.Graded.ModuleData.reflectedBasis
  - OAI.KLInvariance.Graded.ModuleData.char_of_dual_equiv
  - OAI.KLInvariance.Graded.ModuleData.char_natDegree_le_of_dual_equiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:747
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.degree_le_of_dual_equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:763
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.reflectedBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:784
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_of_dual_equiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1053
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_natDegree_le_of_dual_equiv
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read degree_le_of_dual_equiv, all reflectedBasis fields, char_of_dual_equiv
    and the natDegree sum bound. Explained nonzero dual basis vectors, nonnegative
    target degrees and the natural/integer subtraction identity.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Character reflection from a homogeneous dual equivalence

Let \(A=k[X_1,\ldots,X_N]\), with \(k\) a field and each variable in degree one. Let \(M,N'\) be finitely generated, nonnegatively graded \(A\)-modules, and assume \(M\) is free. Suppose
\[
e:\operatorname{Hom}_A(M,A)\xrightarrow{\sim}N'
\]
is an \(A\)-linear equivalence. Let \(D\in\mathbb N\), and assume that for every homogeneous functional \(\lambda\) of degree \(r\),
\[
\lambda(M_j)\subseteq A_{j+r}\quad(j\in\mathbb Z)
\quad\Longrightarrow\quad e(\lambda)\in N'_{r+D}.
\]

Then \(N'\) is free. For a finite nonnegative homogeneous basis \((b_i)\) of \(M\), with degrees \(d_i\), the vectors \(e(b_i^*)\) form a homogeneous basis of \(N'\) of degrees \(D-d_i\), and \(d_i\le D\). Consequently
\[
\operatorname{natDegree}\operatorname{ch}(M;q)\le D,\qquad
\operatorname{ch}(N';q)=\operatorname{reflect}_D\operatorname{ch}(M;q).
\]

*Proof.*

### Step 1. Transport the dual basis

Choose the nonnegative homogeneous basis \((b_i)\) supplied by the [[node:kl.notes.graded_projective_free|basis theorem]]. Its coordinate functionals form a basis \((b_i^*)\) of the \(A\)-linear dual. Each satisfies
\[
b_i^*(M_j)\subseteq A_{j-d_i},
\]
so its functional degree is \(-d_i\).

The linear equivalence \(e\) transports this basis to
\[
c_i=e(b_i^*).
\]
Thus \((c_i)\) is a finite free basis of \(N'\). The homogeneity hypothesis gives
\(c_i\in N'_{D-d_i}\), interpreting this difference first as an integer.

### Step 2. Prove the bound on every basis degree

The functional \(b_i^*\) is nonzero because \(b_i^*(b_i)=1\). Injectivity of \(e\) therefore makes \(c_i\ne0\).

If \(d_i>D\), then \(D-d_i<0\). Nonnegativity of \(N'\) would give
\(N'_{D-d_i}=0\), contradicting \(c_i\ne0\). Hence \(d_i\le D\).

The integer degree \(D-d_i\) is therefore the same as the natural-number subtraction used in the source. This is degree_le_of_dual_equiv.

### Step 3. Construct the reflected nonnegative basis

Use the old finite index set, the transported dual basis \(c_i\), and the degrees
\(D-d_i\in\mathbb N\). Step 2 and the given homogeneity equation verify every degree condition. These data are the source's reflectedBasis construction.

Its polynomial is
\[
\sum_iq^{D-d_i}.
\]
Basis independence identifies this with the character of \(N'\). The same theorem gives
\(\operatorname{ch}(M;q)=\sum_iq^{d_i}\).

### Step 4. Identify the polynomial reflection and degree bound

Every \(d_i\le D\), so polynomial reflection sends \(q^{d_i}\) to \(q^{D-d_i}\). Reflection preserves finite sums, hence
\[
\operatorname{reflect}_D\left(\sum_iq^{d_i}\right)
=\sum_iq^{D-d_i}
=\operatorname{ch}(N';q).
\]
The same bound on the summand exponents gives
\(\operatorname{natDegree}\operatorname{ch}(M;q)\le D\). For a zero module, the basis sum is zero and Lean's convention \(\operatorname{natDegree}(0)=0\) satisfies this bound as well.

At an invertible parameter, the reflected character evaluates as
\(q^D\operatorname{ch}(M;q^{-1})\). The displayed degree bound is what identifies that expression with polynomial reflection.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.degree_le_of_dual_equiv`: [Support.lean:747](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L747).

`OAI.KLInvariance.Graded.ModuleData.reflectedBasis`: [Support.lean:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L763).

`OAI.KLInvariance.Graded.ModuleData.char_of_dual_equiv`: [Support.lean:784](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L784).

`OAI.KLInvariance.Graded.ModuleData.char_natDegree_le_of_dual_equiv`: [CharacterReciprocity.lean:1053](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1053).
