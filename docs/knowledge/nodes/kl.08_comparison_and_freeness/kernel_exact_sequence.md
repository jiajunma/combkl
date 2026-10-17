---
id: kl.detail.kernel_exact_sequence
title: The exact sequence for adding one outgoing condition
kind: theorem
status: proved
primary_topic: kl.08_comparison_and_freeness
topics:
- kl.08_comparison_and_freeness
uses:
- kl.detail.edge_images
- kl.sheaves.upward_kernel
- kl.sheaves.hilbert_free
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:377
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge
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

# The exact sequence for adding one outgoing condition

For \(e:x\to y\) and a set \(F\) of outgoing conditions at \(x\), restriction along \(e\) gives a graded exact sequence
\[
0\longrightarrow K_x(F\cup\{e\})
\longrightarrow K_x(F)
\xrightarrow{\rho_{x,e}}L_e(F)\longrightarrow0.
\]
For a finite nonnegatively graded polynomial-ring sheaf and \(0<q<1\), it follows that
\[
H_{K_x(F)}(q)-H_{K_x(F\cup\{e\})}(q)=H_{L_e(F)}(q).
\]

*Proof.*

### Step 1. Specify the map and its domain

Let \(e:x\to y\), and write
\[
K=K_x(F),\qquad K'=K_x(F\cup\{e\}),\qquad I=\rho_{x,e}(K).
\]
Restrict the degree-zero map \(\rho_{x,e}\) to \(K\) and give it codomain \(I\):
\(r:K\to I\), \(v\mapsto\rho_{x,e}(v)\).
The definition of \(I\) says exactly that \(r\) is surjective.

### Step 2. Identify its kernel in both directions

If \(v\in\ker r\), then \(v\in K\), so all restrictions indexed by \(F\) vanish, and \(r(v)=0\) says the \(e\)-restriction vanishes too. Hence \(v\in K'\).
Conversely, \(v\in K'\) satisfies the conditions in \(F\) and the \(e\)-condition, so it belongs to \(K\) and maps to zero. Thus \(\ker r=K'\).

The inclusion \(K'\to K\) is injective. We have proved exactness, including surjectivity at the right:
\[
0\longrightarrow K'\longrightarrow K\xrightarrow{r}I\longrightarrow0.
\]

### Step 3. Restrict to a homogeneous degree

Each restriction preserves degree. Therefore \(K,K'\), and \(I\) are graded. If \(z\in I_n\), take any preimage \(v\in K\) and decompose it into homogeneous parts. The degree-\(n\) part \(v_n\) is still in \(K\), and \(r(v_n)=z\), because \(r\) preserves degree. Thus surjectivity also holds degree by degree:
\[
0\longrightarrow K'_n\longrightarrow K_n\longrightarrow I_n\longrightarrow0.
\]
These are finite-dimensional real vector spaces. Consequently
\(\dim K_n=\dim K'_n+\dim I_n\).

### Step 4. Pass from dimensions to Hilbert values

Multiply the last identity by \(q^n\), where \(0<q<1\), and sum over the nonnegative degrees. The three sums converge: all modules are graded subquotients of finite modules over a polynomial ring, whose homogeneous dimensions are bounded by those of finite sums of shifted free modules. The homogeneous-basis Hilbert formula supplies the convergent bound.

We obtain \(H_K(q)=H_{K'}(q)+H_I(q)\). Subtracting the finite real value \(H_{K'}(q)\) proves the asserted formula. No free basis of \(K\) or \(K'\) was used.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.kernelHilbert_edge`: [PositiveTransfer.lean:377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L377).
