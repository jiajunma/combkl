---
id: kl.dihedral.induced_signed_action
title: The induced signed action agrees with the ambient root action
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.induced_signed
- kl.dihedral.angular_extremes_simple
- kl.realization.plane_reflection_membership
- kl.coxeter.signed_word_action
lean:
  repository: openai-kl
  modules:
  - Decomposition
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.simple_sign
  - OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.simple
  - OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.act
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:937
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.simple_sign
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:970
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:996
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.act
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- background
---

# The induced signed action agrees with the ambient root action

Let \(P\) be a root plane with plane basis \(\mathcal B\) and induced Coxeter system on \(D_P\). Suppose an ambient root \(v\) realizes the induced signed datum \((t,z)\).

For every \(w\in D_P\), the vector \(w(v)\) realizes the signed datum obtained by applying the induced signed reflection action of \(w\) to \((t,z)\).

*Proof.*

### Step 1. Check the represented reflection and plane membership for a simple action

Let \(s\) be one of the two induced simple reflections. Acting on a representing root conjugates its reflection, so \(s(v)\) represents \(sts^{-1}=sts\).

Since \(s\in D_P\), it preserves \(P\). Thus \(s(v)\in P\). It remains to verify the sign coordinate \(z+1_{t=s}\).

### Step 2. Treat a positive representing root

Suppose \(z=0\) and \(v\) is positive. Let \(a_s\) be the positive endpoint root representing \(s\). This endpoint is plane-simple, so \(s\) sends a positive plane root to negative exactly when that root is \(a_s\).

Uniqueness of positive roots representing reflections gives
\(v=a_s\) exactly when \(t=s\). Therefore \(s(v)\) is negative if \(t=s\), and positive otherwise. This is precisely the sign bit \(0+1_{t=s}\).

### Step 3. Treat a negative representing root

Suppose \(z=1\). Then \(-v\) is a positive root in \(P\) representing \(t\).

If \(t=s\), Step 2 makes \(s(-v)\) negative. Hence
\(s(v)=-s(-v)\) is positive, matching the bit \(1+1=0\) modulo two.

If \(t\ne s\), Step 2 makes \(s(-v)\) positive, so \(s(v)\) is negative, matching the unchanged bit \(1\). This completes all sign cases for a simple reflection.

### Step 4. Induct along a word in the induced simple generators

Every \(w\in D_P\) is a product of the two induced simple reflections. For the empty product, both actions are the identity.

Suppose the assertion holds for a shorter product \(u\). First apply its signed and ambient actions; the induction hypothesis says the resulting datum and root satisfy the relation. Then apply a simple reflection \(s\). Steps 1–3 preserve the relation once more.

Both actions respect multiplication, with \(su\) acting by \(s\) after \(u\). Induction therefore proves the claim for every \(w\).

## References

The local source declarations below define the objects and prove the stated properties.

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.simple_sign`: [Decomposition.lean:937](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L937).

`OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.simple`: [Decomposition.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L970).

`OAI.KLInvariance.TitsSpace.PlaneBasis.InducedSigned.act`: [Decomposition.lean:996](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L996).
