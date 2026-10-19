---
id: kl.realization.form_pair_surjective
title: Prescribed values of two independent linear forms
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses: []
lean:
  repository: openai-kl
  modules:
  - ReflectionPlane
  declarations:
  - OAI.KLInvariance.ReflectionPlane.formPair_surjective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionPlane:16
    format: lean-location
    note: OAI.KLInvariance.ReflectionPlane.formPair_surjective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: 'Read formPair_surjective: expanded the dual functional in the two coordinate
    evaluations, used independence to kill both coefficients and explained the finite-dimensional
    annihilator criterion used to conclude surjectivity.'
tags:
- Kazhdan-Lusztig
- interpolation
---

# Prescribed values of two independent linear forms

Let \(k\) be a field, \(V\) a \(k\)-vector space, and \(f,g:V\to k\) linearly independent linear forms. Then
\[
F:V\to k^2,\qquad F(v)=(f(v),g(v))
\]
is surjective. Thus any two prescribed scalars are simultaneously attained by \(f,g\).

*Proof.*

### Step 1. Expand a functional on the coordinate plane

Let \(L:k^2\to k\) be linear and suppose it vanishes on the image of \(F\). Since
\[
(a,b)=a(1,0)+b(0,1),
\]
one has
\[
L(a,b)=aL(1,0)+bL(0,1).
\]
Substituting \(F(v)\) gives
\[
L(1,0)f(v)+L(0,1)g(v)=0
\]
for every \(v\).

### Step 2. Use independence to determine that functional

The last equality is the relation
\[
L(1,0)f+L(0,1)g=0.
\]
Independence forces both coefficients to vanish. Step 1 then gives \(L(a,b)=0\) for every pair, so \(L=0\).

Thus the only linear functional on \(k^2\) vanishing on \(\operatorname{im}F\) is zero.

### Step 3. Conclude surjectivity

A proper subspace of \(k^2\) admits a nonzero functional vanishing on it. For the zero subspace, use a coordinate functional. For a line spanned by a nonzero \((a,b)\), use
\[
(x,y)\longmapsto bx-ay.
\]
This functional is nonzero because \((a,b)\ne(0,0)\), and it vanishes on the line. These are the possible proper-subspace dimensions.

Step 2 therefore forces \(\operatorname{im}F=k^2\), proving surjectivity. The source expresses this argument as injectivity of the dual map followed by the dual-map criterion for surjectivity.

In the reflection application, \(f,g\) are the two normal forms and the prescribed pair is \((-1,0)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.ReflectionPlane.formPair_surjective`: [ReflectionPlane.lean:16](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean#L16).
