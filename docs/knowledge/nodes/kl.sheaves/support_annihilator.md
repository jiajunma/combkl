---
id: kl.sheaves.support_annihilator
title: Vertex support equals the annihilator of an evaluation kernel
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.integral_cuts
- kl.sheaves.supported_sections
- kl.notes.perfect_pairings
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.IntegralSupport.supported_iff_annihilates
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:521
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.supported_iff_annihilates
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
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

# Vertex support equals the annihilator of an evaluation kernel

Let \(R\) be a commutative domain, let each \(A_y\) be a torsion-free \(R\)-module, and let
\[
M\subseteq\prod_{y\in V}A_y
\]
be an \(R\)-submodule. Torsion-free means that \(av=0\) with \(a\ne0\) forces \(v=0\).

Choose \(p\ne0\) such that \(p\delta_y(m_y)\in M\) for every \(y,m\), and write \(C_y m=p\delta_y(m_y)\). Suppose \(D:M\xrightarrow{\sim}M^*\) is a perfect pairing with cut balance:
\[
\langle C_y m,n\rangle=\langle m,C_y n\rangle,\qquad
\langle m,n\rangle=D(m)(n).
\]
Let \(\pi_x(m)=m_x\). Then
\[
m\in M_{\{x\}}
\quad\Longleftrightarrow\quad
\langle m,n\rangle=0\text{ for every }n\in\ker\pi_x.
\]
Equivalently, \(D(M_{\{x\}})=(\ker\pi_x)^\perp\). The vertex set may be arbitrary.

*Proof.*

### Step 1. Supported vectors annihilate the evaluation kernel

Suppose \(m_y=0\) for \(y\ne x\), and let \(n_x=0\). The coordinate identities for cuts give
\(C_xm=pm\) and \(C_xn=0\). Consequently
\[
p\langle m,n\rangle
=\langle pm,n\rangle
=\langle C_xm,n\rangle
=\langle m,C_xn\rangle=0.
\]
Cancellation of the nonzero scalar \(p\) in \(R\) gives \(\langle m,n\rangle=0\).

### Step 2. A vanishing functional forces every other cut to be zero

Conversely, assume that \(\langle m,n\rangle=0\) whenever \(n_x=0\). Fix a vertex \(y\ne x\), and take any \(n\in M\). The cut \(C_y n\) is supported at \(y\), so its \(x\)-coordinate is zero. Therefore
\[
\langle C_y m,n\rangle
=\langle m,C_y n\rangle=0.
\]
This holds for every \(n\), which says \(D(C_y m)\) is the zero functional. Injectivity of \(D\) gives \(C_y m=0\).

### Step 3. Recover the zero coordinates

The \(y\)-coordinate of \(C_y m=0\) is \(p\,m_y=0\). Since \(A_y\) is torsion-free and \(p\ne0\), we obtain \(m_y=0\). The argument applies separately to every \(y\ne x\), so \(m\) is supported at \(x\).

Step 1 proves one implication and Steps 2–3 prove its converse. Applying the isomorphism \(D\) gives the stated equality with the dual annihilator.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.IntegralSupport.supported_iff_annihilates`: [Support.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L521).
