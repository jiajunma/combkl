---
id: kl.detail.primitive_summand
title: A nonzero split summand of a primitive sheaf is the whole sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.split_summands
- kl.detail.primitive_projectors
- kl.detail.sheaf_isomorphisms
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector_eq_id_of_primitive
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.isoOfPrimitive
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1845
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector_eq_id_of_primitive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1884
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.isoOfPrimitive
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# A nonzero split summand of a primitive sheaf is the whole sheaf

Suppose \(i:B\to C\) and \(p:C\to B\) are a split pair of graded sheaf morphisms, \(pi=1_B\). Assume the identity of \(C\) is primitive and \(B^x\ne0\) at some vertex \(x\). Then \(ip=1_C\), so \(i,p\) are mutually inverse graded sheaf isomorphisms.

*Proof.*

### Step 1. Form the projector in the ambient sheaf

Put \(e=ip\). The splitting identity gives \(e^2=i(pi)p=ip=e\). Also \(e1_C=1_Ce=e\), so \(e\) is one of the idempotents to which primitivity of \(1_C\) applies. Therefore \(e=0\) or \(e=1_C\).

### Step 2. Exclude the zero case using an actual stalk

Choose \(0\ne v\in B^x\). If \(e=0\), evaluate \(p_xe_xi_x\) on \(v\). On the one hand it is zero. On the other,
\[
p_xe_xi_x(v)=p_xi_xp_xi_x(v)=v,
\]
because \(p_xi_x=1\). This contradicts \(v\ne0\). Thus \(e=1_C\).

### Step 3. Assemble the isomorphism

We now have both \(p_xi_x=1\) and \(i_xp_x=1\) at every stalk, and the same equations at every edge module. They define inverse linear isomorphisms. Since \(i,p\) were graded sheaf morphisms, these isomorphisms preserve grading and commute with both restrictions. Hence they form the required graded sheaf isomorphism.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.projector_eq_id_of_primitive`: [BalancedPairings.lean:1845](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1845).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.isoOfPrimitive`: [BalancedPairings.lean:1884](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1884).
