---
id: kl.local.supported_count_weight
title: The supported later-edge difference is the plane weight
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.coset_later_selections
- kl.local.supported_edge_count
- kl.paths.later_count
- kl.local.factor_relative_degree
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.supported_count_difference
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1175
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.supported_count_difference
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient actions, actual modules, interval bounds, selected sets,
    finite-basis assumptions and support cases explicit?
  verdict: Checked the source lower bound, model upper bound and supported condition
    y<=c; applied both supported-cardinality bijections over [x,c], the all-ranks
    count and the exact natural plane-weight formula.
tags:
- Kazhdan-Lusztig
- embedded-images
- local-comparison
---

# The supported later-edge difference is the plane weight

Fix finite-generator real Coxeter systems \(W,W'\) and an interval order isomorphism
\(\varphi:[u,b]_W\simeq[u',b']_{W'}\).
Choose a source plane basis \(B\) for \(P\), its induced group \(D\), and a least coset representative \(a_0\):
\[
\ell_W(a_0)\le\ell_W(da_0)\qquad(d\in D).
\]
Use the finite coset graph
\(K=\{d\in D:da_0\le_Wb\}\)
with its intrinsic order and reflection edges.

Let \(e:x\to_Dy\) be an edge of \(K\) with \(u\le_Wxa_0\). Let \(a\) be its actual positive source root, and let \(\alpha'_e\) be the positive target root of
\(\varphi(xa_0)\to_{W'}\varphi(ya_0)\).
Let \(F_e,H_e\) be the coset later-edge selections at \(x,y\), using the common threshold \(\alpha'_e\). Write \(\varepsilon_{W'}\) for the ambient after-indicator of the target system.

For a model center \(c\in K\) with \(y\le_Dc\), define the supported selections
\[
F_{e,c}=\{f\in F_e:t(f)\le_Dc\},\qquad
H_{e,c}=\{f\in H_e:t(f)\le_Dc\}.
\]
Here \(t(f)\) is the target vertex. Then
\[
|F_{e,c}|=|H_{e,c}|+\bigl(k_P(xa_0,a)\bigr)_{\mathbb N}.
\]
The last term is the natural-number value of the nonnegative geometric plane weight.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The transported count in the actual model edge quotient.**

**OpenAI notes:** In a supported model, the notes identify the two localized image ideals through their valuations. The later-edge counts differ by the plane weight, which is also the valuation of the correction factor. [dih:count](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L464), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The exact supported selections are counted by finite target-vertex sums. The all-ranks transported count and planeWeight_coset_edge identify their difference. Each label and the fixed correction lift are then compared up to units in the actual quotient by cosetLabel e, and structure_scaledImages_of_count gives the image equality. An unsupported model has a zero edge module. [PlaneLocalization:1175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1175), [TerminalKernels:146](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L146).

**Role in the proof:** The Blueprint checks the selection, root-inequality, pairwise-relative-primality, quotient and count hypotheses separately, then multiplies the unit associations to obtain the exact embedded equality.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Put the current edge in the relative interval with top c

The edge gives \(x\le_Dy\), and the support assumption gives \(y\le_Dc\). Thus \(x\le_Dc\) and \(y\) is a vertex of \([x,c]_D\).

The source bound is \(u\le_Wxa_0\). Since \(c\in K\), the upper bound is \(ca_0\le_Wb\). These are exactly the ambient bounds needed to evaluate \(\varphi(za_0)\) for every \(z\in[x,c]_D\).

### Step 2. Express both cardinalities over the same interval

Apply the [[node:kl.local.supported_edge_count|supported-edge counting theorem]] with lower interval endpoint \(x\), source \(x\), top \(c\), and threshold \(\alpha'_e\). It gives
\[
|F_{e,c}|=\sum_{z\in[x,c]_D}
\varepsilon_{W'}(\varphi(xa_0),\alpha'_e,\varphi(za_0)).
\]
Apply the same theorem with source \(y\), keeping the lower interval endpoint \(x\). Its additional hypothesis \(x\le_Dy\) holds by the current edge, so
\[
|H_{e,c}|=\sum_{z\in[x,c]_D}
\varepsilon_{W'}(\varphi(ya_0),\alpha'_e,\varphi(za_0)).
\]
The two applications count their selected supported edges by their target vertices.

### Step 3. Apply the transported dihedral count

The [[node:kl.paths.later_count|all-ranks transported-count theorem]] applies to the setup verified in Step 1 and to the current edge. Its threshold is precisely the positive root \(\alpha'_e\) used by both selections.

It identifies the first sum in Step 2 with the second sum plus
\[
\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]
The theorem includes the case \(c=y\) and the relative rank-one case.

### Step 4. Identify the correction with the geometric weight

The [[node:kl.local.factor_relative_degree|relative edge-degree theorem]] applies to this same least coset representative and actual source root. It gives
\[
\bigl(k_P(xa_0,a)\bigr)_{\mathbb N}
=\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]
Substitute this into Step 3 and then use the cardinality identities from Step 2. The result is the stated natural-number equality.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.supported_count_difference`: [PlaneLocalization.lean:1175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1175).
