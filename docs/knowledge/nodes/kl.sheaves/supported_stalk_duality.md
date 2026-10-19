---
id: kl.sheaves.supported_stalk_duality
title: Supported sections are dual to a generated stalk
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.support_annihilator
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.IntegralSupport.dualToSupport
  - OAI.KLInvariance.IntegralSupport.dualToSupport_bijective
  - OAI.KLInvariance.IntegralSupport.supportEquivDual
  - OAI.KLInvariance.MomentGraph.Sheaf.singleSupportEquivDual
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:541
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.dualToSupport
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:551
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.dualToSupport_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:570
    format: lean-location
    note: OAI.KLInvariance.IntegralSupport.supportEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:856
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.singleSupportEquivDual
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

# Supported sections are dual to a generated stalk

Let \(R\) be a commutative domain, \(A_y\) torsion-free \(R\)-modules, and
\(M\subseteq\prod_y A_y\). Let \(p\ne0\) define integral cuts
\(C_y m=p\delta_y(m_y)\in M\). Suppose
\(D:M\xrightarrow{\sim}M^*\) gives a perfect pairing balanced for these cuts.

Fix \(x\) and assume that \(\pi_x:M\to A_x\), \(m\mapsto m_x\), is surjective. Then there is an \(R\)-linear isomorphism
\[
\Phi_x:M_{\{x\}}\xrightarrow{\sim}A_x^*.
\]
It is characterized by
\[
\Phi_x(m)(n_x)=\langle m,n\rangle\qquad(m\in M_{\{x\}},\ n\in M).
\]
Its inverse is
\[
\Psi_x(\lambda)=D^{-1}(\lambda\circ\pi_x).
\]

For a globally generated sheaf with torsion-free stalks, nonzero annihilating labels, finitely many edges, and a balanced perfect section pairing, these hypotheses hold with \(M=\Gamma(B)\) and \(A_x=B^x\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the stalk–costalk relation.**

**OpenAI notes:** The normalization proof describes a lower-support layer, relates it to the outgoing kernel using flabbiness, and obtains its graded rank through the cited moment-graph and Soergel-module results. It temporarily doubles degrees and uses the shift convention M(k)^j = M^{j+k}. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-upward-rank](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L349).

**Lean (primary):** The local construction starts with a free sheaf and a specified balanced perfect section pairing. Integral cuts identify vertex support with an evaluation-kernel annihilator. The incoming label product identifies that support module with the outgoing kernel, giving an explicit linear equivalence with the stalk dual. [Support:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L521), [CharacterReciprocity:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L150), [CharacterReciprocity:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L185).

**Role in the proof:** The Blueprint follows these integral maps. The pairing construction and its homogeneity equation supply the later graded reciprocity statement. Degree shifts use the Lean convention M(d)_n = M_{n-d}.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct the supported representative of a stalk functional

For \(\lambda\in A_x^*\), the composite \(\lambda\circ\pi_x\) is an \(R\)-linear functional on \(M\). Perfection supplies a unique \(m=D^{-1}(\lambda\circ\pi_x)\).

If \(n_x=0\), then
\[
\langle m,n\rangle=(\lambda\circ\pi_x)(n)=\lambda(0)=0.
\]
The support-annihilator theorem applies to our domain, torsion-free coordinate modules, nonzero cut scalar, and balanced perfect pairing. It implies \(m\in M_{\{x\}}\). Thus \(\Psi_x\) has the asserted codomain. It is linear because precomposition by \(\pi_x\) and \(D^{-1}\) are linear.

### Step 2. Descend a supported section to a stalk functional

Let \(m\in M_{\{x\}}\). For \(a\in A_x\), choose \(n\in M\) with \(n_x=a\), using surjectivity, and set
\[
\Phi_x(m)(a)=\langle m,n\rangle.
\]
If \(n'\) is another lift, \((n-n')_x=0\). The support-annihilator theorem gives
\[
\langle m,n\rangle-\langle m,n'\rangle
=\langle m,n-n'\rangle=0.
\]
Hence the value is independent of the lift.

If \(n,n'\) lift \(a,a'\), then \(n+n'\) lifts \(a+a'\), so bilinearity proves additivity in \(a\). Likewise \(rn\) lifts \(ra\), giving scalar linearity. Using the same lift for two supported first arguments proves that \(\Phi_x\) itself is \(R\)-linear.

### Step 3. Check both compositions

For \(\lambda\in A_x^*\) and \(a\in A_x\), choose a lift \(n\). Then
\[
\Phi_x(\Psi_x(\lambda))(a)
=D(D^{-1}(\lambda\circ\pi_x))(n)
=\lambda(n_x)=\lambda(a).
\]
Thus \(\Phi_x\Psi_x\) is the identity.

For \(m\in M_{\{x\}}\), the defining formula gives
\(\Phi_x(m)\circ\pi_x=D(m)\) as functionals on \(M\). Applying \(D^{-1}\) yields
\[
\Psi_x(\Phi_x(m))=D^{-1}(D(m))=m.
\]
Both inverse identities hold, proving the isomorphism.

### Step 4. Specialize to graph sheaves

For a sheaf, choose \(p=\prod_e\alpha_e\). Each label annihilates its edge module, so the integral-cut construction makes \(C_y\) an endomorphism of \(\Gamma(B)\). The product is nonzero because the coefficient ring is a domain and the finite collection of labels is nonzero. Global generation is precisely the surjectivity of every evaluation map. Substitution into Steps 1–3 gives
\[
\Gamma(B)_{\{x\}}\simeq\operatorname{Hom}_R(B^x,R).
\]

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.IntegralSupport.dualToSupport`: [Support.lean:541](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L541).

`OAI.KLInvariance.IntegralSupport.dualToSupport_bijective`: [Support.lean:551](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L551).

`OAI.KLInvariance.IntegralSupport.supportEquivDual`: [Support.lean:570](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L570).

`OAI.KLInvariance.MomentGraph.Sheaf.singleSupportEquivDual`: [Support.lean:856](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L856).
