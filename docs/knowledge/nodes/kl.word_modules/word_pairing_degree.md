---
id: kl.word.pairing_degree
title: The word pairing lowers degree by the word length
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.bott_samelson
- kl.notes.reflection_frobenius
- kl.notes.tensor_pairing
- kl.algebra.scalar_inverse_degree
- kl.algebra.dual_basis_degrees
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.ReflectionFrobenius.trace_difference
  - OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis
  - OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous
  - OAI.KLInvariance.TitsSpace.bottBasis_pairing_homogeneous
  - OAI.KLInvariance.TitsSpace.bottDuality_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:456
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_difference
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:464
    format: lean-location
    note: OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:580
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:602
    format: lean-location
    note: OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:979
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBasis_pairing_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1024
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottDuality_homogeneous
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

# The word pairing lowers degree by the word length

Let \(A\) be the graded symmetric coefficient algebra of a finite-generator real extended realization. For any word \(\mathbf s\) of length \(m\), let \(M_{\mathbf s}\) carry its tensor-defined perfect pairing and word grading. Then
\[
\langle(M_{\mathbf s})_i,(M_{\mathbf s})_j\rangle
\subseteq A_{i+j-m}.
\]
Thus each prepended simple reflection increases the pairing shift by one.

*Proof.*

### Step 1. Compute the degree of a reflection trace

For a simple reflection, write \(\tau\) for its action on \(A\) and \(\alpha\in A_1\) for its nonzero root polynomial. The reflection decomposition is
\[
a=a_0+\alpha a_1,\qquad a_0,a_1\in A^\tau,
\]
and the trace extracts \(a_1\). Applying \(\tau\) gives
\(\tau(a)=a_0-\alpha a_1\), hence
\[
2\alpha\,\operatorname{tr}(a)=a-\tau(a).
\]

If \(a\in A_n\), the action preserves degree, so \((a-\tau(a))/2\in A_n\). It equals \(\alpha\,\operatorname{tr}(a)\). Multiplication by \(\alpha\) is injective in the coefficient domain. The [[node:kl.algebra.scalar_inverse_degree|homogeneous-scalar cancellation theorem]] therefore gives
\[
\operatorname{tr}(a)\in A_{n-1}.
\]

### Step 2. Start the induction with the empty word

The empty-word module is \(A\), with basis vector \(1\) in degree zero and pairing given by multiplication. Its basis pairing is \(\langle1,1\rangle=1\in A_0\), agreeing with shift zero.

We prove by induction that for word-basis vectors \(b_\varepsilon,b_\eta\),
\[
\langle b_\varepsilon,b_\eta\rangle
\in A_{d_\varepsilon+d_\eta-m},
\]
where \(d_\varepsilon\) is the number of selected \(1\)-choices in the tensor basis.

### Step 3. Prepend one letter and calculate on its basis

Suppose the assertion holds for a word \(\mathbf t\) of length \(m\). Prepend \(s\). The reflection basis over \(A^s\) is \(r_0=1,r_1=\alpha_s\), of degrees \(0,1\). The induced word basis is
\[
b_{(a,\varepsilon)}=1\otimes r_a b_\varepsilon,
\qquad a\in\{0,1\},
\]
of degree \(a+d_\varepsilon\).

The tensor-pairing formula gives
\[
\langle b_{(a,\varepsilon)},b_{(c,\eta)}\rangle
=\operatorname{tr}_s\!\left(
r_a r_c\langle b_\varepsilon,b_\eta\rangle\right).
\]
By induction, the expression inside the trace has degree
\(a+c+d_\varepsilon+d_\eta-m\).
Step 1 lowers this degree by one, giving
\[
(a+d_\varepsilon)+(c+d_\eta)-(m+1).
\]
This is exactly the required basis identity for the longer word.

### Step 4. Extend the basis identity to homogeneous vectors

Let
\(u=\sum_\varepsilon a_\varepsilon b_\varepsilon\in(M_{\mathbf s})_i\)
and
\(v=\sum_\eta c_\eta b_\eta\in(M_{\mathbf s})_j\).
The [[node:kl.algebra.dual_basis_degrees|homogeneous-coordinate theorem]] gives
\[
a_\varepsilon\in A_{i-d_\varepsilon},\qquad
c_\eta\in A_{j-d_\eta}.
\]
Bilinearity expands the pairing into terms
\[
a_\varepsilon c_\eta\langle b_\varepsilon,b_\eta\rangle.
\]
Each has degree
\[
(i-d_\varepsilon)+(j-d_\eta)
 +(d_\varepsilon+d_\eta-m)=i+j-m.
\]
The finite sum therefore lies in \(A_{i+j-m}\), proving the theorem.

### Step 5. Recover the one-letter pairing

For one reflection, the basis \(1\otimes1,1\otimes\alpha\) has degrees \(0,1\). Its pairing matrix is
\[
\begin{pmatrix}0&1\\ 1&0\end{pmatrix},
\]
because the trace of \(1\) and \(\alpha^2\) is zero and the trace of \(\alpha\) is one. The nonzero entries pair degrees \(0,1\) into degree \(0+1-1=0\).

For a reduced word with product \(b\), its length is \(\ell(b)\). This supplies the shift used by the boundary pairing and the stalk–costalk reciprocity formula.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.ReflectionFrobenius.trace_difference`: [Frobenius.lean:456](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L456).

`OAI.KLInvariance.ReflectionFrobenius.trace_homogeneous`: [Frobenius.lean:464](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L464).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis`: [Frobenius.lean:580](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L580).

`OAI.KLInvariance.FrobeniusDuality.inducedPairing_basis_homogeneous`: [Frobenius.lean:602](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L602).

`OAI.KLInvariance.TitsSpace.bottBasis_pairing_homogeneous`: [Frobenius.lean:979](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L979).

`OAI.KLInvariance.TitsSpace.bottDuality_homogeneous`: [Frobenius.lean:1024](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1024).
