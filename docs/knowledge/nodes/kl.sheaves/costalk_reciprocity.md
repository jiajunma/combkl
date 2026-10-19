---
id: kl.detail.costalk_reciprocity
title: The grading shift in stalk–costalk reciprocity
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.costalk_duality_degree
- kl.algebra.dual_basis_degrees
- kl.detail.graded_character
- kl.sheaves.hilbert_free
- kl.detail.root_inversion_count
- kl.algebra.reflected_dual_character
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_hilbert_of_duality
  - OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality
  - OAI.KLInvariance.BruhatGraph.incomingEquivInversions
  - OAI.KLInvariance.BruhatGraph.incoming_card
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_free
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual_homogeneous
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_character
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:275
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_hilbert_of_duality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1712
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1634
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incomingEquivInversions
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1663
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incoming_card
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:787
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:808
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:814
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:819
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:836
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_character
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

# The grading shift in stalk–costalk reciprocity

Let \(B\) be a free sheaf on a finite Bruhat interval \([u,b]\), with coefficient algebra \(A=\mathbb R[X_1,\ldots,X_N]\), variables and edge labels in degree one. Suppose its section duality has shift \(L\in\mathbb N\):
\[
\langle\Gamma(B)_i,\Gamma(B)_j\rangle\subseteq A_{i+j-L}.
\]
Fix a vertex \(x\). Let \(n_x\) count its incoming edges, and choose a finite homogeneous \(A\)-basis \((v_i)_{i\in J}\) of \(B^x\), of degrees \(d_i\ge0\).

The full outgoing kernel \(K_x\) has the induced homogeneous basis degrees
\[
L-n_x-d_i.
\]
Writing
\[
C_x(q)=\sum_{i\in J}q^{d_i},\qquad
H_{K_x}(q)=\sum_{n\ge0}\dim_{\mathbb R}(K_x)_n\,q^n,
\]
one obtains, for \(0<q<1\),
\[
H_{K_x}(q)=q^{L-n_x}C_x(q^{-1})(1-q)^{-N}.
\]
Here \(C_x\) is the graded-rank polynomial of the stalk, and \(H_{K_x}\) records the dimensions of the kernel's homogeneous components.

On the lower interval \([1,b]\), if \(L\ge\ell(b)\), put \(D_x=L-\ell(x)\). The full kernel is finite free, and its character satisfies
\[
\operatorname{ch}(K_x;q)=\operatorname{reflect}_{D_x}C_x(q),
\qquad \operatorname{natDegree}C_x\le D_x.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different intermediate statement.**

**OpenAI notes:** The grading-normalization proposition identifies the stalk graded rank with the canonical KL polynomial and uses the Elias–Williamson character theorem through the cited moment-graph bridges. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

**Lean (primary):** The development defines the equality of actual stalk characters and canonical KL polynomials as StalkCharacterObligation. The unconditional theorem used in the main route is R-reciprocity for the actual character. The local strict half-degree implication retains an explicit nonzero-diagonal hypothesis. [SheafMorphisms:219](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L219), [DyerPaths:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L62), [PositiveTransfer:186](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L186), [CharacterReciprocity:1807](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1807), [TerminalKernels:1273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1273), [TerminalKernels:1284](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1284).

**Role in the proof:** The comparison uses the actual character C and its proved R-reciprocity. Canonical P is handled by the later polynomial-rigidity induction. The local degree result applies to a diagonal coefficient satisfying its stated nonvanishing hypothesis.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Transport the dual basis

The dual basis \((v_i^*)\) is an \(A\)-basis of \((B^x)^*\). The coordinate-functional theorem gives
\[
v_i^*(B^x_j)\subseteq A_{j-d_i}.
\]
Thus \(v_i^*\) has degree \(-d_i\).

Apply the inverse stalk–costalk isomorphism and set
\[
k_i=\kappa_x^{-1}(v_i^*).
\]
Because \(\kappa_x\) is a linear isomorphism, the \(k_i\) form a basis of \(K_x\). The inverse-degree theorem gives
\[
k_i\in(K_x)_{L-n_x-d_i}.
\]
This degree statement follows by first representing \(v_i^*\circ\pi_x\) in global sections and then removing the homogeneous incoming product.

### Step 2. Determine the contribution of each generator

A generator \(k_i\) of degree \(a_i=L-n_x-d_i\) contributes the copy \(A k_i\), whose degree-\(n\) piece is \(A_{n-a_i}k_i\).

Every \(k_i\) is nonzero: its image \(v_i^*\) takes value \(1\) on \(v_i\). Since \(K_x\) lies in a nonnegative graded stalk, a nonzero \(k_i\) cannot have negative degree. Therefore \(a_i\ge0\).

The polynomial ring in \(N\) degree-one variables has Hilbert series \((1-q)^{-N}\). The homogeneous-free-basis formula consequently gives
\[
H_{K_x}(q)=\sum_i q^{a_i}(1-q)^{-N}.
\]
The sum over basis vectors is finite, and the coefficient-ring series converges for \(0<q<1\).

### Step 3. Factor the numerator

Substitute \(a_i=L-n_x-d_i\) and factor the common power:
\[
\begin{aligned}
H_{K_x}(q)
&=\left(\sum_iq^{L-n_x-d_i}\right)(1-q)^{-N}\\
&=q^{L-n_x}\left(\sum_i(q^{-1})^{d_i}\right)(1-q)^{-N}\\
&=q^{L-n_x}C_x(q^{-1})(1-q)^{-N}.
\end{aligned}
\]
The nonnegative exponents \(a_i\) also show directly that the resulting numerator is the graded-rank polynomial of \(K_x\).

### Step 4. Count incoming edges on a lower Bruhat ideal

For the interval \([1,b]\), an incoming edge \(y\to x\) has reflection label \(t\) with \(y=tx\) and \(\ell(tx)<\ell(x)\). Thus it determines a left reflection inversion of \(x\).

Conversely, if \(t\) is a reflection lowering \(x\), then \(tx<x\) in Bruhat order. Since \(1\le tx\le x\le b\), the element \(tx\) lies in the same interval and gives the incoming edge \(tx\to x\).

The reflection and target determine that edge uniquely, so these assignments are inverse. The reflection-inversion count is \(\ell(x)\), giving \(n_x=\ell(x)\).

For a pairing with \(L=\ell(b)\), the formula becomes
\[
H_{K_x}(q)
=q^{\ell(b)-\ell(x)}C_x(q^{-1})(1-q)^{-N}.
\]
The nonnegative kernel degrees give \(d_i\le\ell(b)-\ell(x)\) for each stalk basis vector.

### Step 5. Pass to the bundled polynomial kernel character

Work now on \([1,b]\) with \(L\ge\ell(b)\). The source's kernelData is the full outgoing kernel with its induced grading. The map taking all outgoing restrictions has this same kernel: keeping the underlying vector gives kernelEquivFull in both directions.

Compose the inverse stalk–costalk duality with this identity on kernels:
\[
\Phi_x:(B^x)^*\xrightarrow{\sim}\operatorname{kernelData}(B,x).
\]
This is FreeSheaf.kernelDual. It proves freeness of the kernel by transporting the finite dual basis of the free stalk.

For a homogeneous functional of degree \(r\), the inverse-duality degree theorem and \(n_x=\ell(x)\) give
\[
\Phi_x(\lambda)\in\operatorname{kernelData}(B,x)_{r+L-\ell(x)}.
\]
The inequalities \(\ell(x)\le\ell(b)\le L\) identify this integer difference with the natural number \(D_x\).

The [[node:kl.algebra.reflected_dual_character|homogeneous dual-character theorem]] now applies. It proves the character reflection formula and the degree bound stated above. This is FreeSheaf.kernel_character, expressed for the actual bundled kernel module.

### Step 6. Evaluate the two-vertex example

For \(x<y\), use the one-edge congruence sheaf over \(A=\mathbb R[\alpha]\). Both stalks have character \(1\), the pairing has shift \(L=1\), and \(n_x=0,\ n_y=1\). The formula gives
\[
H_{K_x}(q)=\frac{q}{1-q},\qquad H_{K_y}(q)=\frac1{1-q},
\]
agreeing with \(K_x=\alpha A\) and \(K_y=A\).

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_hilbert_of_duality`: [CharacterReciprocity.lean:275](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L275).

`OAI.KLInvariance.BruhatGraph.costalk_hilbert_of_duality`: [Support.lean:1712](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1712).

`OAI.KLInvariance.BruhatGraph.incomingEquivInversions`: [Support.lean:1634](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1634).

`OAI.KLInvariance.BruhatGraph.incoming_card`: [Support.lean:1663](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1663).

`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelEquivFull`: [CharacterReciprocity.lean:787](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L787).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual`: [CharacterReciprocity.lean:808](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L808).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_free`: [CharacterReciprocity.lean:814](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L814).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelDual_homogeneous`: [CharacterReciprocity.lean:819](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L819).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernel_character`: [CharacterReciprocity.lean:836](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L836).
