---
id: kl.sheaves.integral_cuts
title: Integral vertex cuts and products of edge labels
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.supported_sections
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.IntegralSupport.cut
  - OAI.KLInvariance.IntegralSupport.cut_self
  - OAI.KLInvariance.IntegralSupport.cut_other
  - OAI.KLInvariance.IntegralSupport.cut_of_supported
  - OAI.KLInvariance.IntegralSupport.cut_eq_zero
  - OAI.KLInvariance.MomentGraph.Sheaf.labelProduct
  - OAI.KLInvariance.MomentGraph.Sheaf.scaled_single_section
  - OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_annihilates
  - OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_ne_zero
  - OAI.KLInvariance.MomentGraph.Sheaf.incoming
  - OAI.KLInvariance.MomentGraph.Sheaf.incomingProduct
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:488
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.cut
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:493
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.cut_self
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:496
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.cut_other
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:499
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.cut_of_supported
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:509
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.cut_eq_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:828
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.labelProduct
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:820
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.scaled_single_section
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:833
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_annihilates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:830
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_ne_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:926
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.incoming
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:931
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.incomingProduct
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

# Integral vertex cuts and products of edge labels

Let \(M\subseteq\prod_{x\in V}A_x\) be a submodule over a commutative ring \(R\). Choose \(p\in R\) such that
\[
p\,\delta_x(m_x)\in M\qquad(x\in V,\ m\in M).
\]
The integral vertex cut at \(x\) is the linear endomorphism
\[
C_x:M\to M,\qquad C_xm=p\,\delta_x(m_x).
\]
The membership condition makes its codomain \(M\) well-defined. Its coordinates are
\[
(C_xm)_x=p\,m_x,\qquad (C_xm)_y=0\quad(y\ne x).
\]
Thus the cut isolates one coordinate with the scalar factor \(p\).

## Coordinate identities

If \(m\) is supported at \(x\), then \(C_xm=pm\), by equality at each coordinate. If \(m_x=0\), then \(C_xm=0\). Applying these equations twice gives
\[
C_x^2=pC_x,\qquad C_yC_x=0\quad(y\ne x).
\]
When \(V\) is finite, each coordinate in the sum occurs once, so
\[
\sum_{x\in V}C_x=p\,\mathrm{id}_M.
\]
These are the identities of scaled coordinate projections.

## A common scalar from the edge labels

Let \(B\) be a sheaf with finitely many edges, labelled by \(\alpha_e\in R\), and assume that each \(\alpha_e\) annihilates its edge module. Define the label product
\[
p=\prod_{e\in E}\alpha_e.
\]
For any edge \(e\), write \(p=\alpha_e r_e\). Then \(pv=r_e(\alpha_ev)=0\) for all \(v\in B^e\).

Take any assignment \(a\). On any edge, both restrictions of \(pa\) vanish:
\[
\rho^-_e(pa_{s(e)})=p\rho^-_e(a_{s(e)})=0,\qquad
\rho^+_e(pa_{t(e)})=p\rho^+_e(a_{t(e)})=0.
\]
Consequently \(p\delta_x(m_x)\) is a global section. The common label product therefore defines integral cuts on \(\Gamma(B)\). If \(R\) is a domain and all labels are nonzero, their finite product is nonzero. For an empty edge set, the product is \(1\).

The upper-quotient property supplies the required annihilation: an edge vector is the image of an upper-stalk vector, and its product with the label maps to zero.

## Products of incoming labels

For a vertex \(x\), define the incoming edge set and its product by
\[
E_x^-=\{e:t(e)=x\},\qquad
\beta_x=\prod_{e\in E_x^-}\alpha_e.
\]
This smaller product supplies the incoming-edge vanishing needed to turn a vector in the full outgoing kernel into a supported section. The common product \(p\) instead supplies a cut for every global section at every vertex.

On one edge \(x\to y\) labelled \(\alpha\),
\[
p=\alpha,\qquad \beta_x=1,\qquad\beta_y=\alpha.
\]
For a compatible pair \((f,g)\), the cuts are
\[
C_x(f,g)=(\alpha f,0),\qquad C_y(f,g)=(0,\alpha g).
\]
Both pairs satisfy the section equation modulo \(\alpha\), and their sum is \(\alpha(f,g)\).

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.IntegralSupport.cut`: [Support.lean:488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L488).

`OAI.KLInvariance.IntegralSupport.cut_self`: [Support.lean:493](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L493).

`OAI.KLInvariance.IntegralSupport.cut_other`: [Support.lean:496](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L496).

`OAI.KLInvariance.IntegralSupport.cut_of_supported`: [Support.lean:499](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L499).

`OAI.KLInvariance.IntegralSupport.cut_eq_zero`: [Support.lean:509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L509).

`OAI.KLInvariance.MomentGraph.Sheaf.labelProduct`: [Support.lean:828](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L828).

`OAI.KLInvariance.MomentGraph.Sheaf.scaled_single_section`: [Support.lean:820](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L820).

`OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_annihilates`: [Support.lean:833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L833).

`OAI.KLInvariance.MomentGraph.Sheaf.labelProduct_ne_zero`: [Support.lean:830](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L830).

`OAI.KLInvariance.MomentGraph.Sheaf.incoming`: [Support.lean:926](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L926).

`OAI.KLInvariance.MomentGraph.Sheaf.incomingProduct`: [Support.lean:931](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L931).
