---
id: kl.detail.upper_quotient
title: The upper-end edge quotient rule
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
- kl.algebra.scalar_quotient
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.UpperQuotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient.annihilates
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:401
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:963
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.UpperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:871
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient.annihilates
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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
- moment_graph_sheaves
---

# The upper-end edge quotient rule

For a labelled edge \(e:x\to y\), with label \(\alpha_e\in A\), the upper-quotient condition says that
\[
\rho^+_e:B^y\longrightarrow B^e
\]
is surjective and
\[
\ker\rho^+_e=\alpha_e B^y.
\]
The induced isomorphism \(B^y/\alpha_eB^y\simeq B^e\) sends the class of \(v\) to \(\rho^+_e(v)\). This identifies the edge module together with its map from the upper stalk.

The label annihilates the edge module. Indeed, write an edge vector as \(\rho^+_e(v)\); then
\[
\alpha_e\rho^+_e(v)=\rho^+_e(\alpha_ev)=0.
\]
Thus \(B^e\) is naturally a module over \(A/(\alpha_e)\).

If \(B^y\) has a finite free basis over \(A\), its basis classes give a basis of \(B^e\) over \(A/(\alpha_e)\).

## The degree-one exact sequence

Suppose \(\alpha_e\) is homogeneous of degree one and multiplication by it on \(B^y\) is injective. The shift convention is
\[
M(d)_n=M_{n-d}.
\]
Hence multiplication gives a degree-zero map \(B^y(1)\to B^y\): a degree-\(n\) source vector is originally in \(B^y_{n-1}\), and its product with \(\alpha_e\) lies in \(B^y_n\).

The exact sequence is therefore
\[
0\longrightarrow B^y(1)
 \xrightarrow{\ \alpha_e\ }B^y
 \xrightarrow{\ \rho^+_e\ }B^e
 \longrightarrow0.
\]
Its image and kernel agree by the quotient condition. Suppose the graded pieces are finite-dimensional over \(k\). Write
\[
H_M(q)=\sum_{n\ge0}\dim_k(M_n)q^n
\]
for the Hilbert series, or its value at a positive \(q\) where the sum converges. In each degree, exactness makes dimensions add, so
\[
H_{B^e}(q)=H_{B^y}(q)-qH_{B^y}(q)
=(1-q)H_{B^y}(q).
\]

For \(A=k[\alpha]\) and \(B^y=A\), the quotient is \(k\), concentrated in degree zero. The identity reads \(1=(1-q)/(1-q)\).

The lower restriction \(\rho^-_e\) describes how values at \(x\) enter this quotient. Its restrictions to outgoing kernels give the lower images used in the comparison.

## References

The local definitions and constructions are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient`: [GradedSheaves.lean:401](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L401).

`OAI.KLInvariance.MomentGraph.Sheaf.UpperQuotient`: [GradedSheaves.lean:963](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L963).

`OAI.KLInvariance.MomentGraph.GradedSheaf.UpperQuotient.annihilates`: [Support.lean:871](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L871).
