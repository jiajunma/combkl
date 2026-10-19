---
id: kl.sheaves.primitive_image
title: Primitivity of a split summand and its image projector
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.split_summands
- kl.detail.primitive_projectors
- kl.sheaves.projector_image
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_id_of_projector
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_projector_of_id
  - OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_image
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1826
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_id_of_projector
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1942
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_projector_of_id
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1891
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_image
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

# Primitivity of a split summand and its image projector

Let \(i:B\to C\) and \(p:C\to B\) be a split pair of graded sheaf morphisms, with \(pi=1_B\). Put \(e=ip\). Then
\[
1_B\text{ is primitive}\quad\Longleftrightarrow\quad e\text{ is primitive}.
\]
In particular, if a graded sheaf projector \(e\) is primitive, then the identity of its image sheaf is primitive.

*Proof.*

### Step 1. Lift an endomorphism of the summand

For \(a:B\to B\), define its lift by
\[
L(a)=iap:C\to C.
\]
The splitting identity gives
\[
pL(a)i=a,\qquad L(1_B)=e,\qquad L(0)=0.
\]
It also gives
\[
L(a)L(b)=ia(pi)bp=iabp=L(ab).
\]
Thus lifting preserves composition and is injective.

### Step 2. Deduce primitivity of the summand from primitivity of e

Assume \(e\) is primitive. If \(a^2=a\) on \(B\), then
\(L(a)^2=L(a)\), and
\[
eL(a)=L(a),\qquad L(a)e=L(a).
\]
Primitivity of \(e\) gives \(L(a)=0\) or \(L(a)=e\). Applying \(p(-)i\) gives \(a=0\) or \(a=1_B\). This is primitivity of the identity on \(B\).

### Step 3. Descend an idempotent supported inside e

Conversely, assume \(1_B\) primitive. Let \(f:C\to C\) satisfy
\[
f^2=f,\qquad fe=f,\qquad ef=f.
\]
Put \(a=pfi\). Then
\[
a^2=pfi pfi=pfefi=pf^2i=pfi=a.
\]
Hence \(a=0\) or \(a=1_B\).

The support equations also give
\[
L(a)=i(pfi)p=efe=f.
\]
Therefore \(f=0\) or \(f=e\). Together with \(e^2=e\), this proves primitivity of \(e\).

### Step 4. Apply the result to an image sheaf

For a projector \(e\), the image sheaf has its componentwise inclusion and projection, whose composite in the ambient sheaf is exactly \(e\). Step 2 applied to this split pair proves that the image sheaf has primitive identity.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_id_of_projector`: [BalancedPairings.lean:1826](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1826).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.primitive_projector_of_id`: [BalancedPairings.lean:1942](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1942).

`OAI.KLInvariance.MomentGraph.GradedSheaf.Hom.primitive_image`: [BalancedPairings.lean:1891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1891).
