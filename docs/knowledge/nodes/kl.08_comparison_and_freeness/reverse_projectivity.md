---
id: kl.detail.reverse_projectivity
title: Recovering a projective kernel from scaled image equality
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.detail.scaled_images
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:970
    format: lean-location
    note: OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq
  - artifact: openai-kl-paper
    locator: Related paper context; sec:induction
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
- comparison_and_freeness
---

# Recovering a projective kernel from scaled image equality

Let \(S\subseteq M\) and \(T\subseteq P\) be projective \(A\)-modules, with maps
\(f:M\to N\), \(g:P\to N\), and an injective endomorphism \(\psi:N\to N\). Assume
\[
f(S)=\psi(g(T)),\qquad \ker g=aP,
\]
that multiplication by \(a\) on \(P\) is injective, and that \(T\) is saturated under division by \(a\). Then
\[
S\cap\ker f
\]
is projective.

*Proof.*

### Step 1. Give the common image two surjective presentations

Let \(U=f(S)=\psi(g(T))\). Define
\[
a_1:S\twoheadrightarrow U,\quad s\mapsto f(s),
\qquad
a_2:T\twoheadrightarrow U,\quad t\mapsto\psi(g(t)).
\]
They are surjective by the definition of \(U\) and the image-equality hypothesis. We want to prove that \(\ker a_1=S\cap\ker f\) is projective.

A module is projective precisely when every surjection onto it admits a linear section. We use this splitting property below.

### Step 2. Identify the second kernel

If \(a_2(t)=0\), injectivity of \(\psi\) gives \(g(t)=0\). Since \(\ker g=aP\), write \(t=av\) with \(v\in P\). The element \(t\) belongs to \(T\); saturation therefore gives \(v\in T\). Thus \(\ker a_2\subseteq aT\).
Conversely \(a_2(av)=\psi(g(av))=0\) for \(v\in T\), so \(\ker a_2=aT\).

Multiplication by \(a\) on \(P\) is injective, hence its restriction \(T\to aT\) is injective as well as surjective. It is an isomorphism. Therefore \(\ker a_2\simeq T\) is projective.

### Step 3. Form the pullback of the two presentations

Define
\[
E=\{(s,t)\in S\oplus T:a_1(s)=a_2(t)\}.
\]
Projection \(E\to S\) is surjective: given \(s\), lift \(a_1(s)\) through \(a_2\). Its kernel is \(\{0\}\oplus\ker a_2\). Because \(S\) is projective, this sequence splits:
\[
E\simeq\ker a_2\oplus S.
\]
Both summands are projective, so \(E\) is projective.

Projection \(E\to T\) is also surjective, now using surjectivity of \(a_1\). Its kernel is \(\ker a_1\oplus\{0\}\). Since \(T\) is projective, this sequence also splits:
\[
E\simeq\ker a_1\oplus T.
\]

### Step 4. Extract the desired projective summand

The second splitting makes \(\ker a_1\) a direct summand of the projective module \(E\). Direct summands of projective modules are projective: extend any lifting problem by zero on the complementary summand, lift it from \(E\), and restrict the lift back to the desired summand.

Finally, an element of \(\ker a_1\) is an element \(s\in S\) satisfying \(f(s)=0\), so the forgetful map identifies it with \(S\cap\ker f\). Transport projectivity across this identification.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.ReverseFiltration.inf_kernel_projective_of_image_eq`: [PositiveTransfer.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L970).
