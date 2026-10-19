---
id: kl.sheaves.base_change_properties
title: Sheaf properties under scalar extension
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.base_change
- kl.sheaves.flat_section_base_change
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_generated
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_free
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_finite
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.baseChange_flabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1019
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1061
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1065
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1069
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:1162
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.baseChange_flabby
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all five property-transfer results. Separated generation/free/finite
    transport from the source flatness hypothesis for upper quotients and the finite-graph
    plus flatness hypotheses for flabbiness.
tags:
- Kazhdan-Lusztig
- sheaf-operations
---

# Sheaf properties under scalar extension

Let \(\varphi:R\to S\) be a homomorphism of commutative rings and \(B\) an \(R\)-linear sheaf on an ordered graph. Scalar extension has the following properties.

- Global generation of \(B\) implies global generation of \(B_S\).
- A free stalk remains free, and a finitely generated stalk remains finitely generated.
- If \(S\) is flat over \(R\) and \(B\) has the upper-quotient rule with labels \(\alpha_e\), then \(B_S\) has that rule with labels \(\varphi(\alpha_e)\).
- If the vertex and edge sets are finite, \(S\) is flat over \(R\), and \(B\) is flabby, then \(B_S\) is flabby.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit finite-flat construction.**

**OpenAI notes:** The localization discussion uses flat extension of kernels and images and then decomposes the localized sheaf over the local ring on a dihedral coset. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The scalar-extension lemmas first treat general commutative rings and graph sheaves. Finite product maps identify tensor constraints; flat exactness gives section and selected-kernel identities. Image commutation is proved separately by tensor generators. [MinimalExtensions:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1157), [MinimalExtensions:1162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1162), [TerminalKernels:279](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L279), [TerminalKernels:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L360).

**Role in the proof:** These algebraic results precede the root-plane and coset specialization. The later pullback argument controls the surviving edges, while both localized edge images retain their common ambient module.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Generate a tensor stalk value by global sections

At a fixed vertex \(x\), write a vector of \(S\otimes_R B^x\) as a finite sum
\(\sum_i s_i\otimes v_i\). Global generation supplies a global section \(f_i\) of \(B\) with \((f_i)_x=v_i\).

The pure-tensor compatibility calculation makes
\(y\mapsto s_i\otimes(f_i)_y\) a global section of \(B_S\). Sum these sections. Its value at \(x\) is the prescribed tensor vector.

### Step 2. Transport free bases and finite generating sets

If \((m_i)\) is an \(R\)-basis of \(B^x\), the vectors \(1\otimes m_i\) form an \(S\)-basis of \(S\otimes_R B^x\). They span by expanding the second factor of each pure tensor in its finite basis coordinates.

For linear independence, tensor each original coordinate functional with \(S\), and use \(S\otimes_R R\simeq S\). The resulting functional takes \(1\otimes m_i\) to the corresponding Kronecker delta. Applying it to a finite relation recovers each coefficient as zero.

For finite generation, perform the spanning part with any finite generating set of \(B^x\). Every tensor is an \(S\)-linear combination of the finitely many vectors \(1\otimes m_i\).

### Step 3. Tensor the upper-quotient sequence

Fix \(e:x\to y\). The upper-quotient rule says that \(\rho^+_e\) is surjective and
\[
\ker\rho^+_e=\alpha_e B^y.
\]
Thus the sequence
\[
B^y\xrightarrow{\alpha_e\cdot}B^y
\xrightarrow{\rho^+_e}B^e\longrightarrow0
\]
is exact.

Under the stated flatness hypothesis, tensoring preserves this exactness. The first map becomes multiplication by \(\varphi(\alpha_e)\), because
\[
s\otimes\alpha_e v=s\varphi(\alpha_e)\otimes v.
\]
The second becomes \(\rho^{S,+}_e\). It is surjective and has kernel
\(\varphi(\alpha_e)B_S^y\), proving the transported quotient rule.

### Step 4. Express a partial section as a tensor of old sections

Assume now the finite graph and flatness hypotheses. For an upper set \(\Omega\) and a section \(f\) of \(B_S\) over \(\Omega\), the [[node:kl.sheaves.flat_section_base_change|flat section base-change theorem]] gives
\[
f=\Theta_\Omega\left(\sum_i s_i\otimes g_i\right),
\qquad g_i\in\Gamma_\Omega(B).
\]
The tensor is a finite sum.

### Step 5. Extend each section and sum

Flabbiness of \(B\) gives a global section \(h_i\) agreeing with \(g_i\) at all vertices in \(\Omega\). Define
\[
h_x=\sum_i s_i\otimes(h_i)_x.
\]
Each pure-tensor assignment is globally compatible, so \(h\) is a global section of \(B_S\). For \(x\in\Omega\),
\[
h_x=\sum_i s_i\otimes(g_i)_x=f_x.
\]
Thus every section on an upper set extends globally, which is flabbiness.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_generated`: [MinimalExtensions.lean:1019](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1019).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_free`: [MinimalExtensions.lean:1061](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1061).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_vertex_finite`: [MinimalExtensions.lean:1065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1065).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_upperQuotient`: [MinimalExtensions.lean:1069](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1069).

`OAI.KLInvariance.MomentGraph.Sheaf.baseChange_flabby`: [MinimalExtensions.lean:1162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1162).
