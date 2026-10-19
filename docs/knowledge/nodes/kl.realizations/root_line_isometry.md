---
id: kl.realization.root_line_isometry
title: Isometries whose displacement lies in a root line
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.linear_reflection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.Realization.orthogonal_eq_id_or_rootReflection
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1439
    format: lean-location
    note: OAI.KLInvariance.Realization.orthogonal_eq_id_or_rootReflection
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the two cases of orthogonal_eq_id_or_rootReflection. Retained an arbitrary
    real bilinear form and the exact norm-two and displacement-line hypotheses, and
    expanded both coefficient equations.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Isometries whose displacement lies in a root line

Let \(V\) be a real vector space, \(B:V\times V\to\mathbb R\) a bilinear form, and \(a\in V\) satisfy \(B(a,a)=2\). Let \(g:V\to V\) be an invertible linear map preserving \(B\):
\[
B(gv,gw)=B(v,w)\qquad(v,w\in V).
\]
Assume every displacement lies in the line of \(a\):
\[
gv-v\in\mathbb Ra\qquad(v\in V).
\]
Then either \(g\) is the identity or
\[
gv=v-B(a,v)a\qquad(v\in V).
\]
The second formula is the root reflection with root \(a\) and coroot \(B(a,-)\).

*Proof.*

### Step 1. Determine the image of the root

The displacement condition at \(a\) gives
\(ga-a=ra\) for some real \(r\), so \(ga=(1+r)a\).
Preservation of the form gives
\[
2=B(a,a)=B(ga,ga)=2(1+r)^2.
\]
Therefore \((1+r)^2=1\), so \(ga=a\) or \(ga=-a\).

### Step 2. Compute every image when the root is fixed

Suppose \(ga=a\). For any \(v\), choose \(c\in\mathbb R\) with
\(gv=v+ca\), using the displacement condition. Then
\[
B(a,v)=B(ga,gv)
=B(a,v+ca)=B(a,v)+2c.
\]
Thus \(c=0\), and \(gv=v\). Since \(v\) was arbitrary, \(g\) is the identity.

### Step 3. Compute every image when the root is negated

Suppose \(ga=-a\). Write again \(gv=v+ca\). Preservation now gives
\[
B(a,v)=B(-a,v+ca)=-B(a,v)-2c.
\]
Hence \(c=-B(a,v)\), and
\(gv=v-B(a,v)a\), as claimed.

The calculation uses the given bilinear form and the normalization \(B(a,a)=2\). It identifies the map directly from its action along the specified line.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Realization.orthogonal_eq_id_or_rootReflection`: [IntegralPairings.lean:1439](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1439).
