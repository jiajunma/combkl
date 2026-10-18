---
id: kl.detail.root_reflection_correspondence
title: Unique positive roots representing reflections
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
- kl.notes.reflection_faithfulness
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign
  - OAI.KLInvariance.TitsSpace.Represents.reflection_unique
  - OAI.KLInvariance.TitsSpace.exists_positive_root
  - OAI.KLInvariance.TitsSpace.positiveRootEquiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1743
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1765
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.reflection_unique
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1789
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_positive_root
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1821
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.positiveRootEquiv
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

# Unique positive roots representing reflections

Every reflection has exactly one positive representing root. Sending a reflection to that root is a bijection from the reflections of \(W\) to \(\Phi^+\).

*Proof.*

### Step 1. Obtain the reflection formula and norm

If \(a=w\alpha_i\) represents \(t=ws_iw^{-1}\), invariance of the Tits form gives \((a,a)=2\). Conjugating the simple-reflection formula gives
\[
t(v)=v-(a,v)a
\]
on the root space, and the same formula for the embedded root on the nondegenerate extension. In particular \(a\ne0\). Replacing \(w\) by \(ws_i\) replaces \(a\) by \(-a\) without changing \(t\).

### Step 2. Prove uniqueness up to sign

Suppose \(a,b\) represent the same reflection. Apply their two formulas to \(a\). Since \((a,a)=2\), comparison gives
\[
(b,a)b=2a,\qquad a=c b,\qquad c=(b,a)/2.
\]
Taking squared norms gives \(2=2c^2\), hence \(c=1\) or \(c=-1\) over \(\mathbb R\). Thus \(a=b\) or \(a=-b\).

If both roots are positive, the second alternative would force every coordinate of \(a\) to be both nonnegative and nonpositive, making \(a=0\). That contradicts its norm. Thus positive representing roots are unique.

### Step 3. Establish existence and uniqueness of the reflection

A reflection is, by definition, a conjugate of a simple reflection, so it has a representing root. The sign theorem for real roots says that all coordinates of this root are nonnegative or all are nonpositive. In the second case take its negative. This proves existence of a positive representative.

Conversely, a positive root comes from some conjugated simple root. If two reflections have that same root, their extended reflection formulas agree on every vector. Faithfulness of the extended action therefore makes the reflections equal.

### Step 4. Verify the two inverse maps

Starting with a reflection, choose its positive root and then its represented reflection. Step 3 says the result is the original reflection. Starting with a positive root, take its reflection and then that reflection's positive root. Step 2 says the result is the original root. The maps are therefore inverse bijections.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.Represents.unique_up_to_sign`: [Tits.lean:1743](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1743).

`OAI.KLInvariance.TitsSpace.Represents.reflection_unique`: [Tits.lean:1765](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1765).

`OAI.KLInvariance.TitsSpace.exists_positive_root`: [Tits.lean:1789](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1789).

`OAI.KLInvariance.TitsSpace.positiveRootEquiv`: [Tits.lean:1821](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1821).
