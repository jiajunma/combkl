---
id: kl.notes.supported_pairings
title: Perfect graded pairings and support orthogonality
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.perfect_pairings
- kl.detail.graded_sheaf
- kl.sheaves.supported_sections
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1850
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:941
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
verification:
  definition: accepted
  proof: not_applicable
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

# Perfect graded pairings and support orthogonality

Let \(B\) be a graded sheaf over a graded commutative algebra \(A\), and let \(\Gamma=\Gamma(B)\) be its global section module. Fix an integer \(d\). A perfect graded section pairing consists of an \(A\)-linear isomorphism
\[
D:\Gamma\xrightarrow{\sim}\Gamma^*,
\qquad \langle m,n\rangle=D(m)(n),
\]
with a homogeneity condition and two support conditions.

Perfection means that every \(A\)-linear functional on \(\Gamma\) is pairing against a unique first argument. Homogeneity says that if \(m_x\in B^x_i\) and \(n_x\in B^x_j\) at every vertex, then
\[
\langle m,n\rangle\in A_{i+j-d}.
\]
Here a homogeneous section means a section homogeneous of the same degree at every coordinate.

The support conditions are
\[
\begin{aligned}
m\in\Gamma_{\{x\}},\ n_x=0&\ \Longrightarrow\ \langle m,n\rangle=0,\\
m_x=0,\ n\in\Gamma_{\{x\}}&\ \Longrightarrow\ \langle m,n\rangle=0.
\end{aligned}
\]
They let a supported first argument define a functional of the second argument's \(x\)-coordinate, and a supported second argument define a functional of the first argument's \(x\)-coordinate.

A symmetric perfect section pairing adds
\[
\langle m,n\rangle=\langle n,m\rangle.
\]
Symmetry exchanges the two support equations. The graded perfect-pairing data record both equations explicitly.

## A complete one-edge calculation

Use the congruence sheaf over \(A=\mathbb R[\alpha]\):
\[
\Gamma=\{(f,g)\in A^2:f-g\in\alpha A\}.
\]
Set \(u=(f+g)/2\) and \(v=(f-g)/(2\alpha)\). Both lie in \(A\), and
\[
(f,g)=u(1,1)+v(\alpha,-\alpha).
\]
This gives a basis \(e_0=(1,1),e_1=(\alpha,-\alpha)\) of degrees zero and one.

Define
\[
\langle(f,g),(f',g')\rangle
   =uv'+vu'=\frac{ff'-gg'}{2\alpha}.
\]
Expanding \(f=u+\alpha v,\ g=u-\alpha v\) and the primed expressions gives
\(ff'-gg'=2\alpha(uv'+vu')\), which proves the quotient is a polynomial.

In the displayed basis, the pairing matrix is
\[
\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.
\]
It squares to the identity, so it is invertible over \(A\); this proves perfection. It is symmetric. For homogeneous input degrees \(i,j\), division by \(\alpha\) lowers the output degree to \(i+j-1\), giving \(d=1\).

A section supported at the lower vertex is \((\alpha h,0)\). Its pairing with \((f,g)\) is \(hf/2\), which vanishes when \(f=0\). At the upper vertex the analogous pairing is \(-hg/2\), which vanishes when \(g=0\). Symmetry supplies the other support condition.

This calculation follows the definitions as a worked example. The word-module and boundary-pairing constructions establish the corresponding data for the sheaves used in the main proof.

## Integral cuts and later duality

The two support equations imply the balance equation
\[
\langle C_xm,n\rangle=\langle m,C_xn\rangle
\]
for cuts with a common nonzero scalar over a domain. The proof compares each side, multiplied by that scalar, with \(\langle C_xm,C_xn\rangle\). It is developed in [[node:kl.sheaves.cut_balance]].

For the example, the two balanced expressions are \(ff'/2\) for \(x\) and \(-gg'/2\) for \(y\). This is the identity used to recover stalk functionals from supported sections.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

The fields `pairing`, `homogeneous`, `left_orthogonal`, and `right_orthogonal` encode the isomorphism, its degree, and the two support equations. SymmetricPerfectPairing inherits these through `toPerfectPairing` and adds `symmetric`.

`OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing`: [Support.lean:1850](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1850).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing`: [EdgeLocalization.lean:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L941).
