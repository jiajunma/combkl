---
id: kl.algebra.root_quotient_coordinates
title: Polynomial coordinates on an edge coefficient ring
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.linear_ideals
- kl.detail.linear_quotient
- kl.algebra.linear_primes
- kl.algebra.coefficient_algebra
- kl.algebra.edge_coefficient_ring
- kl.realization.root_planes
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι
  - OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial
  - OAI.KLInvariance.EdgeAlgebra.linear_homogeneous
  - OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous
  - OAI.KLInvariance.TitsSpace.EdgeCoefficient
  - OAI.KLInvariance.TitsSpace.edgePolynomial
  - OAI.KLInvariance.BruhatGraph.edgeRingEquiv
  - OAI.KLInvariance.BruhatGraph.edgeRingEquiv_root
  - OAI.KLInvariance.BruhatGraph.edgeRing_isDomain
  - OAI.KLInvariance.BruhatGraph.edgeRing_ufm
  - OAI.KLInvariance.BruhatGraph.reducedPolynomialRoot_prime
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:824
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:845
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:871
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:861
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.linear_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:875
    format: lean-location
    note: OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:930
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.EdgeCoefficient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:950
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.edgePolynomial
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:519
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeRingEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:524
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeRingEquiv_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:531
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeRing_isDomain
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:536
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeRing_ufm
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:539
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.reducedPolynomialRoot_prime
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the coefficient rings, module properties and actual maps explicit?
  verdict: Read rootQuotientEquiv, its generator formula, rootQuotientPolynomial and
    reduced-root homogeneity, plus the actual EdgeCoefficient/edgePolynomial definitions.
tags:
- Kazhdan-Lusztig
- module-algebra
---

# Polynomial coordinates on an edge coefficient ring

Let \(V\) be a vector space over a field \(k\). For a vector \(a\in V\), choose a basis \((e_j)\) of \(V/ka\). The source constructs
\[
\operatorname{Sym}_k(V)/(\iota(a))
\simeq\operatorname{Sym}_k(V/ka)
\simeq k[X_j].
\]
The class of another linear generator \(\iota(v)\) becomes the linear polynomial with the coordinates of \([v]\) in that basis.

For a nonzero root in the finite-dimensional real extended realization, this is the polynomial presentation of its edge coefficient ring.

Specialize now to the real extended realization \(V\), with original root space \(V_0\) and embedding \(i_0:V_0\hookrightarrow V\). Write \(A_{\mathrm{sym}}=\operatorname{Sym}_{\mathbb R}(V)\), and let \(\Phi:A_{\mathrm{sym}}\to A\) be the chosen polynomial coordinate isomorphism. Write \(\lambda(v)=\Phi(\iota(i_0v))\). For a positive root \(a\), set \(r_a=\lambda(a)\) and put
\[
E_a=A/(r_a),\qquad \overline A_a=A_{\mathrm{sym}}/(\iota(i_0a)).
\]
The map \(\psi_a:E_a\to\overline A_a\) induced by \(\Phi^{-1}\) is an algebra isomorphism. For every positive root \(c\), it sends \([\lambda(c)]\) to \([\iota(i_0c)]\). Thus \(E_a\) is a domain and a unique factorization domain. For a positive root \(c\ne a\), its reduced label \([\lambda(c)]\) is prime in \(E_a\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Canonical labels for the same principal ideals.**

**OpenAI notes:** The coefficient discussion uses degree-one linear root labels and permits any nonzero real scalar multiple, because only the principal ideal matters. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The label is the coordinate polynomial of the embedded canonical positive root for the reflection. Its primality and quotient are proved for that actual element. [SheafMorphisms:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L144), [Support:1065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1065), [ReflectionSchedules:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L824).

**Role in the proof:** Multiplying a label by a nonzero field scalar leaves its principal ideal unchanged. The fixed label used by the code therefore presents the same scalar quotient described in the notes.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the root-line quotient isomorphism

The generic [[node:kl.detail.linear_quotient|linear-quotient theorem]] at \(P=ka\) gives the first isomorphism. Its formula on generators is
\[
[\iota(v)]\longmapsto\iota_{V/ka}([v]).
\]

### Step 2. Use the chosen quotient-space basis

The symmetric-algebra coordinate isomorphism sends
\(\iota_{V/ka}(e_j)\) to \(X_j\). If
\([v]=\sum_j c_je_j\),
linearity gives
\[
[\iota(v)]\longmapsto\sum_j c_jX_j.
\]
Composing the two algebra isomorphisms is the source's rootQuotientPolynomial.

### Step 3. Check degree and nonvanishing

Every \(X_j\) has degree one, so the displayed polynomial is homogeneous of degree one. It is nonzero exactly when at least one \(c_j\) is nonzero, equivalently when \([v]\ne0\), or \(v\notin ka\).

The [[node:kl.algebra.linear_primes|linear-prime theorem]] then also proves primality of every surviving reduced linear generator.

### Step 4. Specialize to an actual root label

Let \(V\) be the real extended realization and embed a positive root \(a\) from the original root space. The source defines EdgeCoefficient as the symmetric algebra modulo that embedded root's ideal.

It chooses a finite basis of the quotient space and composes the two isomorphisms above, producing edgePolynomial. If \(\dim V=N\) and \(a\ne0\), the quotient space has dimension \(N-1\), so the edge ring has \(N-1\) polynomial variables. Finite-variable polynomial rings over a field are Noetherian unique factorization domains; these coordinates supply those coefficient-ring hypotheses in the local membership argument.

### Step 5. Transport the actual polynomial quotient

The algebra isomorphism \(\Phi\) sends the principal ideal generated by \(\iota(i_0a)\) onto that generated by \(r_a\). Therefore it descends to an isomorphism between the two quotients. The source uses the inverse direction:
\[
\psi_a:E_a\xrightarrow{\sim}\overline A_a,\qquad
\psi_a([f])=[\Phi^{-1}(f)].
\]
Well-definedness follows because a difference \(r_ag\) pulls back to
\(\iota(i_0a)\Phi^{-1}(g)\). The forward map induced by \(\Phi\) is its inverse.

For another positive root \(c\), the defining coordinate formula gives
\[
\psi_a([\lambda(c)])=[\Phi^{-1}(\Phi(\iota(i_0c)))]
=[\iota(i_0c)].
\]
This is edgeRingEquiv_root. Composing \(\psi_a\) with the symmetric edgePolynomial isomorphism of Step 4 gives polynomial coordinates on \(E_a\), transporting its domain and unique-factorization properties.

### Step 6. Transport primality of a reduced positive root

If \(c\ne a\), [[node:kl.realization.root_planes|independence of distinct positive roots]] gives \(c\notin\mathbb R a\). Injectivity of the embedding gives \(i_0c\notin\mathbb R(i_0a)\).

The [[node:kl.algebra.linear_primes|linear-prime theorem]] therefore makes \([\iota(i_0c)]\) prime in \(\overline A_a\). Step 5 identifies it with \(\psi_a([\lambda(c)])\). Algebra isomorphisms preserve prime elements, so \([\lambda(c)]\) is prime in \(E_a\). This proves the source's reducedPolynomialRoot_prime statement.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv`: [ReflectionSchedules.lean:824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L824).

`OAI.KLInvariance.EdgeAlgebra.rootQuotientEquiv_mk_ι`: [ReflectionSchedules.lean:845](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L845).

`OAI.KLInvariance.EdgeAlgebra.rootQuotientPolynomial`: [ReflectionSchedules.lean:871](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L871).

`OAI.KLInvariance.EdgeAlgebra.linear_homogeneous`: [ReflectionSchedules.lean:861](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L861).

`OAI.KLInvariance.EdgeAlgebra.reducedRoot_homogeneous`: [ReflectionSchedules.lean:875](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L875).

`OAI.KLInvariance.TitsSpace.EdgeCoefficient`: [ReflectionSchedules.lean:930](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L930).

`OAI.KLInvariance.TitsSpace.edgePolynomial`: [ReflectionSchedules.lean:950](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L950).

`OAI.KLInvariance.BruhatGraph.edgeRingEquiv`: [TerminalKernels.lean:519](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L519).

`OAI.KLInvariance.BruhatGraph.edgeRingEquiv_root`: [TerminalKernels.lean:524](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L524).

`OAI.KLInvariance.BruhatGraph.edgeRing_isDomain`: [TerminalKernels.lean:531](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L531).

`OAI.KLInvariance.BruhatGraph.edgeRing_ufm`: [TerminalKernels.lean:536](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L536).

`OAI.KLInvariance.BruhatGraph.reducedPolynomialRoot_prime`: [TerminalKernels.lean:539](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L539).
