---
id: kl.sheaves.supported_sections
title: Sections supported at a vertex and their stalk values
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.compatible_sections
- kl.sheaves.upward_kernel
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.IntegralSupport.projection
  - OAI.KLInvariance.IntegralSupport.supported
  - OAI.KLInvariance.MomentGraph.Sheaf.singleStalk
  - OAI.KLInvariance.MomentGraph.Sheaf.singleStalkEquivSupport
  - OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:477
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.projection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:479
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.supported
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:996
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.singleStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:999
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.singleStalkEquivSupport
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:898
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff
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
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Sections supported at a vertex and their stalk values

Let \(R\) be a commutative ring, let \(V\) be a set, and let \(A_x\) be an \(R\)-module for every \(x\in V\). Suppose
\[
M\subseteq\prod_{x\in V}A_x
\]
is an \(R\)-submodule of assignments. Coordinate evaluation is the linear map
\[
\pi_x:M\to A_x,\qquad m\mapsto m_x.
\]
The support of an assignment is the set of its nonzero coordinates. The submodule supported at \(x\) is
\[
M_{\{x\}}=\{m\in M:m_y=0\text{ for every }y\ne x\}.
\]
It contains the zero assignment. Addition and scalar multiplication preserve the displayed coordinate equations.

Write \(\delta_x(v)\) for the assignment with value \(v\) at \(x\) and zero elsewhere. For a graph sheaf \(B\), take \(M=\Gamma(B)\) and \(A_x=B^x\). The supported stalk is
\[
S_x=\{v\in B^x:\delta_x(v)\in\Gamma(B)\}.
\]
Thus \(S_x\) is a submodule of a single stalk, whereas \(\Gamma(B)_{\{x\}}\) is a submodule of the global section module.

## Evaluation and zero extension

The linear maps
\[
S_x\longrightarrow\Gamma(B)_{\{x\}},\quad v\longmapsto\delta_x(v),
\qquad
\Gamma(B)_{\{x\}}\longrightarrow S_x,\quad m\longmapsto m_x
\]
are inverse. Evaluating \(\delta_x(v)\) gives \(v\). Conversely, \(m\) supported at \(x\) has the same value as \(\delta_x(m_x)\) at \(x\), and both vanish elsewhere.

## The incident-edge equations

For \(\delta_x(v)\) to be a global section, its two restrictions must agree on every edge. There are three cases.

- On an outgoing edge \(x\to y\), the upper value is zero, so \(\rho^-_e(v)=0\).
- On an incoming edge \(z\to x\), the lower value is zero, so \(\rho^+_e(v)=0\).
- On an edge with neither endpoint \(x\), both values are zero.

If \(K_x\) is the full outgoing kernel, these conditions give
\[
S_x=K_x\cap\bigcap_{e:\,t(e)=x}\ker\rho^+_e.
\]
With the upper-quotient condition, the incoming kernels are \(\alpha_e B^x\).

For the one-edge congruence sheaf over \(\mathbb R[\alpha]\),
\[
K_x=\alpha A,\quad K_y=A,\qquad S_x=\alpha A,\quad S_y=\alpha A.
\]
At the lower vertex the outgoing equation imposes divisibility by \(\alpha\); at the upper vertex the incoming equation imposes it. The supported sections are respectively \((\alpha h,0)\) and \((0,\alpha h)\).

## Functionals vanishing on a submodule

For \(N\subseteq M\), its dual annihilator is
\[
N^\perp=\{\lambda\in\operatorname{Hom}_R(M,R):
                  \lambda(n)=0\text{ for every }n\in N\}.
\]
In particular, \((\ker\pi_x)^\perp\) consists of functionals whose value is unchanged when one changes a section without changing its \(x\)-coordinate. The support-annihilator theorem identifies this module with \(M_{\{x\}}\) through a balanced perfect pairing.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.IntegralSupport.projection`: [Support.lean:477](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L477).

`OAI.KLInvariance.IntegralSupport.supported`: [Support.lean:479](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L479).

`OAI.KLInvariance.MomentGraph.Sheaf.singleStalk`: [Support.lean:996](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L996).

`OAI.KLInvariance.MomentGraph.Sheaf.singleStalkEquivSupport`: [Support.lean:999](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L999).

`OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff`: [Support.lean:898](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L898).
