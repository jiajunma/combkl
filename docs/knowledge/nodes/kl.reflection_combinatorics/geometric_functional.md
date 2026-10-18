---
id: kl.detail.geometric_functional
title: Existence of a generic functional ordering all positive roots
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.notes.extended_realization
lean:
  repository: openai-kl
  modules:
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.TitsSpace.exists_geometric_functional
  - OAI.KLInvariance.TitsSpace.functionalRatio_between
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:126
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_geometric_functional
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:138
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.functionalRatio_between
  - artifact: openai-kl-paper
    locator: Related paper context; sec:dihedral
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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
- reflection_orders
---

# Existence of a generic functional ordering all positive roots

For a finite-generator Coxeter system, there exists a real linear functional \(f\) such that the slopes
\[
\lambda(\alpha)=\frac{f(\alpha)}{\operatorname{ht}(\alpha)}
\]
are distinct for distinct positive roots. Ordering roots by these slopes gives the required geometric reflection order.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different stated generality.**

**OpenAI notes:** The cited Dyer theorem is stated for a reflection order in general; the subsequent comparison chooses geometric reflection orders. [bg:paths](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L185).

**Lean (primary):** The referenced formal entry theorem establishes the required path formula for the constructed geometric functional on a finite lower region of a finite-generator system. Generic pencils and complete root-plane blocks provide its order-independence argument. [ReflectionSchedules:126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L126), [ReflectionOrders:1229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean#L1229).

**Role in the proof:** The geometric-order hypotheses specify the path theorem used here. The generic-functional construction orders all positive roots; the transfer calculation takes place on the finite region in the theorem.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Normalize the roots and check distinctness

Use the height functional \(h(v)=\sum_i v_i\), positive on every positive root. Put \(\widehat\alpha=\alpha/h(\alpha)\).
If \(\widehat\alpha=\widehat\beta\), the positive roots are positive scalar multiples of one another. Both have squared Tits length two, so that scalar is one, and \(\alpha=\beta\).

Finite generation makes \(W\) countable, because finite words in a finite alphabet form a countable set and map onto \(W\). The positive roots are therefore countable too.

### Step 2. Choose a functional avoiding every equality

Enumerate coordinates by \(0,\ldots,N-1\), and for a real parameter \(t\) define
\[
f_t(v)=\sum_{j=0}^{N-1}v_jt^j.
\]
For distinct normalized roots \(\widehat\alpha,\widehat\beta\), their difference is nonzero. Thus
\(f_t(\widehat\alpha-\widehat\beta)\) is a nonzero polynomial in \(t\), with only finitely many roots.

There are countably many root pairs. The union of these finite forbidden sets is countable, while \(\mathbb R\) is uncountable. Choose \(t\) outside the union and set \(f=f_t\). Then all numbers \(f(\widehat\alpha)=f(\alpha)/h(\alpha)\) are distinct.

### Step 3. Verify betweenness by an explicit convex combination

Suppose \(\gamma=r\alpha+s\beta\), with \(r,s>0\), and write \(\lambda(\eta)=f(\eta)/h(\eta)\). Linearity gives
\[
\lambda(\gamma)
=\frac{rh(\alpha)}{rh(\alpha)+sh(\beta)}\lambda(\alpha)
+\frac{sh(\beta)}{rh(\alpha)+sh(\beta)}\lambda(\beta).
\]
Both coefficients are strictly positive and their sum is one. If \(\lambda(\alpha)<\lambda(\beta)\), subtracting \(\lambda(\alpha)\) gives a positive multiple of their difference, and subtracting the expression from \(\lambda(\beta)\) does the same. Thus
\(\lambda(\alpha)<\lambda(\gamma)<\lambda(\beta)\).

### Step 4. Obtain the reflection order

Distinct slopes give a total order. On each root plane, normalized positive roots lie on the affine line \(h=1\), and Step 3 orders positive combinations between their endpoints. Hence the restriction is one of the two angular orders. This proves both existence and the required rank-two order property.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization



`OAI.KLInvariance.TitsSpace.exists_geometric_functional`: [ReflectionSchedules.lean:126](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L126).

`OAI.KLInvariance.TitsSpace.functionalRatio_between`: [ReflectionSchedules.lean:138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L138).
