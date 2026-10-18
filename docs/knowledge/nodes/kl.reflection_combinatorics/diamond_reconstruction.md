---
id: kl.detail.diamond_reconstruction
title: Recovering every reflection edge from the interval order
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.detail.diamond_closure
- kl.foundations.finite_support
- kl.notes.relative_dihedral_intervals
- kl.realization.reflection_plane
- kl.geometry.plane_weight_sum
lean:
  repository: openai-kl
  modules:
  - DyerPaths
  declarations:
  - OAI.KLInvariance.diamondEdges_of_bruhatStep_general
  - OAI.KLInvariance.diamondEdges_bruhatStep_general
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:175
    format: lean-location
    note: OAI.KLInvariance.diamondEdges_of_bruhatStep_general
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:204
    format: lean-location
    note: OAI.KLInvariance.diamondEdges_bruhatStep_general
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

# Recovering every reflection edge from the interval order

For vertices \(x,y\) in any Bruhat interval, including intervals in Coxeter systems with infinitely many generators,
\[
D(x,y)\quad\Longleftrightarrow\quad x\longrightarrow y
\]
is an upward reflection edge. Thus the full directed reflection graph is recoverable from the unlabelled interval order.

*Proof.*

### Step 1. Prove soundness of the diamond rules

A cover in a Bruhat interval is a reflection edge: a nontrivial chain realizing the order comparison could otherwise have an intermediate vertex, contradicting that it is a cover.

For the eight-edge rule, compare the two paths from \(x\) to \(c\) through \(a,b\). Their reflection products are equal. The moving-image formula for a product of two reflections puts all four root labels in the same plane determined by the distinct initial labels. Repeating with \(d\) and then with the two paths to \(z\) puts the entire configuration in one dihedral coset.

In a relative dihedral graph, edges have positive odd rank difference. The three-edge path \(x\to a\to c\to z\) has positive odd total rank difference, and the dihedral odd-gap criterion therefore makes \(x\to z\) a reflection edge. This proves preservation by the diamond rule, hence soundness by induction on its derivation.

### Step 2. Choose a justified plane for a non-cover edge

Now let \(x\to y=r_\alpha x\) have ambient length gap greater than one, in a finite-generator system. The inversion calculation gives
\[
2\sum_P k_P=\ell(y)-\ell(x)-1>0,
\]
with finitely supported nonnegative integral weights. Therefore some plane \(P\) has \(k_P>0\). Choose this plane; an arbitrary plane containing \(\alpha\) would not give the needed conclusion.

The relative-length formula in this plane gives relative gap \(2k_P+1\), at least three. Choose the minimal coset representative so that relative reflection edges are exactly the ambient edges inside that coset.

### Step 3. Construct the smaller eight-edge diamond

A dihedral interval of odd rank \(r\ge3\) has two vertices in each internal rank. Choose \(a,b\) in its first rank and \(c,d\) in rank \(r-1\). The first and last edges have gap one; each of the four middle pairs has odd positive gap \(r-2\). Thus all eight required pairs are reflection edges, with \(a\ne b\) and \(c\ne d\).

Relative comparability implies ambient comparability, so all these vertices lie between \(x\) and \(y\), and hence in the original ambient interval. Each of the eight edges has strictly smaller ambient length difference than \(x\to y\).

### Step 4. Induct on ambient rank difference

For gap one, the edge is a cover and belongs to \(D\). For a larger gap, apply the induction hypothesis to each edge in Step 3. The diamond constructor then places \((x,y)\) in \(D\). This proves completeness in finite generator rank.

### Step 5. Remove the finite-generator assumption

Choose a finite standard parabolic model containing the whole lower ideal below the interval's top. Parabolic inclusion preserves and reflects the order and reflection edges. Apply the finite-generator completeness and soundness there, and transport each cover or diamond derivation through the interval order isomorphism. This gives the equivalence for arbitrary Coxeter systems.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L2).

## Lean formalization



`OAI.KLInvariance.diamondEdges_of_bruhatStep_general`: [DyerPaths.lean:175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L175).

`OAI.KLInvariance.diamondEdges_bruhatStep_general`: [DyerPaths.lean:204](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L204).
