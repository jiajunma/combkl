---
id: kl.sheaves.lower_extension_properties
title: Sheaf properties preserved by lower-ideal extension
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.lower_extension
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
- kl.sheaves.upward_kernel
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.projectLower_compatible
  - OAI.KLInvariance.MomentGraph.GradedSheaf.liftLower_compatible
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_free
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_generated
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_flabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_quotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:575
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.projectLower_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:581
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.liftLower_compatible
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:563
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:588
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:598
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:607
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:627
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_minimal
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

# Sheaf properties preserved by lower-ideal extension

Let \(B\) be a graded sheaf on a lower ideal \(K\) of an ordered graph, and let \(\widetilde B\) be its extension by zero.

Free stalks, global generation, flabbiness, and the upper-quotient rule pass from \(B\) to \(\widetilde B\). If \(B\) is kernel-minimal at a vertex \(x\in K\), then so is \(\widetilde B\) at \(x\); every vertex outside \(K\) is automatically kernel-minimal.

*Proof.*

### Step 1. Identify the stalks and edge equations

Inside \(K\), the extended stalks identify with the old stalks. Outside \(K\), they are zero and hence free of rank zero.

An edge ending in \(K\) has both endpoints there and retains the old restriction equation. Every edge ending outside \(K\) has zero edge module, so its equation is the equality of two zero values. This proves that extension and restriction of assignments preserve the relevant compatibility conditions.

### Step 2. Prove global generation

For a prescribed value at \(x\in K\), choose a global section of \(B\) with that value and extend it by zero. Step 1 makes it global on the larger graph.

If \(x\notin K\), its stalk has only the zero vector, realized by the zero section. Thus every extended stalk is generated.

### Step 3. Extend compatible data on an upper set

Let \(U\) be upper in the full vertex poset, and let \(f\) be compatible on \(U\). Restrict its assignment to \(K\). It is compatible on \(U\cap K\), which is upper in the induced poset on \(K\): if \(x\in U\cap K\), \(x\le y\), and \(y\in K\), then \(y\in U\).

Flabbiness of \(B\) extends those values to a global section on \(K\). Extend that section by zero. It agrees with \(f\) on \(U\cap K\), and on \(U\setminus K\) both assignments have the unique zero value. This proves flabbiness of \(\widetilde B\).

### Step 4. Preserve upper quotients

If an edge ends in \(K\), its upper stalk, edge module, and upper restriction are unchanged, so the quotient rule is inherited.

If it ends outside \(K\), its upper stalk and edge module are both zero. The map \(0\to0\) is surjective, and its kernel is \(0=\alpha_e0\). Thus the quotient rule holds on every edge.

### Step 5. Preserve kernel minimality

For \(x\in K\), outgoing edges with target in \(K\) give the original conditions on \(B^x\). Those with target outside \(K\) have zero edge modules and impose a zero equation. Therefore the full outgoing kernel of \(\widetilde B\) identifies with the original kernel at \(x\).

If that kernel is contained in \(J B^x\), the same containment holds in \(J\widetilde B^x\). Outside \(K\), both the stalk and its kernel are zero, so minimality holds there as well.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.projectLower_compatible`: [MinimalExtensions.lean:575](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L575).

`OAI.KLInvariance.MomentGraph.GradedSheaf.liftLower_compatible`: [MinimalExtensions.lean:581](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L581).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_free`: [MinimalExtensions.lean:563](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L563).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_generated`: [MinimalExtensions.lean:588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L588).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_flabby`: [MinimalExtensions.lean:598](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L598).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_quotient`: [MinimalExtensions.lean:607](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L607).

`OAI.KLInvariance.MomentGraph.GradedSheaf.lowerExtend_minimal`: [MinimalExtensions.lean:627](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L627).
