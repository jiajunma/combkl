---
id: kl.sheaves.finite_sum_properties
title: Structural properties and kernels of finite sheaf sums
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.finite_operations
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
- kl.sheaves.upward_kernel
- kl.algebra.positive_ideal
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_generated
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_flabby
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_upperQuotient
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_kernel_iff
  - OAI.KLInvariance.LocalCover.pi_mem_ideal_smul
  - OAI.KLInvariance.MomentGraph.Sheaf.pi_minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:825
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:835
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:842
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:315
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:849
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_kernel_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:874
    format: lean-location
    note: OAI.KLInvariance.LocalCover.pi_mem_ideal_smul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:893
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.pi_minimal
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
- moment_graph_sheaves
---

# Structural properties and kernels of finite sheaf sums

Let \((B_i)\) be a finite family of graded sheaves on the same labelled ordered graph. Finite sums and nonnegative grading shifts preserve free stalks, global generation, flabbiness, and the upper-quotient rule whenever the summands have those properties.

At each vertex,
\[
K_x\!\left(\bigoplus_iB_i\right)=\prod_i K_x(B_i)
\]
under the componentwise stalk identification. If every \(K_x(B_i)\subseteq J B_i^x\), where \(J=A_{>0}\), then the sum is kernel-minimal at \(x\).

*Proof.*

### Step 1. Read compatibility one component at a time

The restriction equation for an assignment \(m\) on an edge is an equality of tuples:
\[
(\rho^{i,-}_e(m_{s(e),i}))_i
=(\rho^{i,+}_e(m_{t(e),i}))_i.
\]
It holds exactly when every coordinate equation holds.

For global generation, realize each prescribed coordinate \(v_i\in B_i^x\) by a global section of \(B_i\), then take their tuple. For flabbiness, extend each component of a compatible assignment on an upper set, then assemble the resulting global sections. The coordinate equations verify compatibility and agreement on the upper set.

### Step 2. Check the upper-quotient property

For an edge \(e:x\to y\), componentwise surjectivity makes
\(\prod_i B_i^y\to\prod_i B_i^e\) surjective.

A tuple \((v_i)\) lies in its kernel exactly when \(v_i\in\alpha_e B_i^y\) for every \(i\). Choose \(w_i\) with \(v_i=\alpha_e w_i\). Then
\[
(v_i)_i=\alpha_e(w_i)_i.
\]
Conversely, every such scalar multiple maps to zero in each edge component. Thus the kernel is \(\alpha_e\prod_i B_i^y\).

### Step 3. Identify the outgoing kernels

A stalk tuple has zero restriction on every outgoing edge exactly when each component does. This gives the displayed product description of the full outgoing kernel. The same argument applies to any selected set of outgoing edges.

### Step 4. Assemble membership in an ideal multiple

For modules \(M_i\) indexed by a finite set, suppose \(v_i\in JM_i\) for every \(i\). Each \(v_i\) is a finite sum of terms \(a m\) with \(a\in J\). Insert each of these vectors into coordinate \(i\), putting zero in all other coordinates.

Every inserted term belongs to \(J\prod_i M_i\), because coordinate insertion is linear. Summing first within each coordinate and then over the finite index set gives
\[
(v_i)_i\in J\prod_iM_i.
\]
Apply this to \(M_i=B_i^x\) and the kernel tuple from Step 3. The component minimality assumptions yield minimality of the sum.

### Step 5. Check freeness and shifts

Choose a free basis in each stalk summand. The coordinate insertions of these basis vectors form a basis of the finite product: coordinatewise expansions prove spanning, and coordinatewise independence proves independence.

A grading shift changes the degrees but leaves the underlying modules and restrictions unchanged. Therefore it preserves the section, quotient, and kernel conditions. Its nonnegative shift also retains the grading requirements.

The compatibility, generation, flabbiness, quotient, and kernel arguments above apply to arbitrary products of ungraded sheaves as well. Finiteness supplies the finite graded module data, the finite free basis, and the ideal-multiple argument in Step 4.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.pi_compatible`: [GradedSheaves.lean:825](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L825).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_generated`: [GradedSheaves.lean:835](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L835).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_flabby`: [GradedSheaves.lean:842](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L842).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_upperQuotient`: [MinimalExtensions.lean:315](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L315).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_kernel_iff`: [GradedSheaves.lean:849](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L849).

`OAI.KLInvariance.LocalCover.pi_mem_ideal_smul`: [GradedSheaves.lean:874](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L874).

`OAI.KLInvariance.MomentGraph.Sheaf.pi_minimal`: [GradedSheaves.lean:893](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L893).
