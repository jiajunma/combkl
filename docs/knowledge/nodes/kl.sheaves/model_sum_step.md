---
id: kl.sheaves.model_sum_step
title: Adding the next center in a boundary-model decomposition
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.stalk_remainder
- kl.sheaves.model_sum_properties
- kl.sheaves.partial_iso_extension
- kl.algebra.homogeneous_basis
- kl.sheaves.finite_operations
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.extend_modelSum
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1567
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.extend_modelSum
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

# Adding the next center in a boundary-model decomposition

Let \(A\) be a connected nonnegative graded Noetherian domain, and fix a boundary-model family \((O_c)\) on an ordered graph with finitely many edges.

Let \(B\) satisfy the upper-quotient rule, flabbiness, and global generation. Suppose \(U\) is upper, \(C\) is a model sum centered in \(U\), and a graded partial isomorphism \(j:B\to C\) on \(U\) is given.

Choose \(x\notin U\) with every \(y>x\) in \(U\), and assume \(B^x\) is free. Then one can construct a model sum \(D\) centered in \(U\cup\{x\}\) and extend the partial isomorphism to that enlarged set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Related descent in different coefficient settings.**

**OpenAI notes:** The plane-localization proposition descends through a finite coset graph over an ungraded local ring. Nakayama makes the lifted stalk map surjective, its free target gives a splitting, and projectivity over the local ring makes the remainder free. Multiplicities count copies of local structure models. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded construction lifts in both directions and corrects the composite using invertibility modulo the positive ideal. The remainder is graded projective over a connected Noetherian domain and has a homogeneous basis. Its degrees determine nonnegative shifts of boundary models. Partial isomorphisms already include every edge whose upper endpoint has been processed. [SheafMorphisms:1427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1427), [SheafMorphisms:1567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1567), [SheafMorphisms:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).

**Role in the proof:** Both constructions split a stalk over the upper boundary image and add models centered at the new vertex. The graded construction records a polynomial of shifts at each center; the ungraded local construction records an integer number of copies.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the local stalk decomposition

The [[node:kl.sheaves.model_sum_properties|model-sum theorem]] gives free stalks, flabbiness, and generation for \(C\). Since \(x\notin U\), it also gives kernel minimality at \(x\).

The partial isomorphism supplies an isomorphism above \(x\), including every edge map whose target is above \(x\). Its components preserve degree. The [[node:kl.sheaves.stalk_remainder|stalk-remainder theorem]] therefore gives
\[
B^x\simeq C^x\oplus K
\]
with \(K\) finite graded free, and with the first component giving exactly the prescribed boundary map.

### Step 2. Realize the remainder as new centered models

Choose a finite homogeneous basis of \(K\), with degrees
\(d_1,\ldots,d_m\ge0\).
The top normalization \(O_x^x\simeq A\) identifies
\[
K\simeq\bigoplus_{j=1}^m O_x^x(d_j).
\]
Define
\[
S=\bigoplus_{j=1}^mO_x(d_j),\qquad D=C\oplus S.
\]
Then \(D\) is a model sum centered in \(U\cup\{x\}\), and the displayed identifications give a graded stalk isomorphism
\(j_x':B^x\simeq D^x\).

### Step 3. Retain the partial isomorphism on U

For \(y\in U\), the inequality \(y\le x\) would imply \(x\in U\), because \(U\) is upper. Thus \(y\not\le x\), and the model support gives \(S^y=0\).

If an edge has target in \(U\), its upper \(S\)-stalk is zero. The upper-quotient rule then makes its \(S\)-edge module zero. Hence the old component maps extend to the product by
\[
v\longmapsto(j_y(v),0),\qquad
z\longmapsto(j_e(z),0).
\]
These are isomorphisms on the old domain, with inverses given by projection to the first component.

### Step 4. Check the new outgoing squares

For an edge \(x\to y\), the target \(y\) is in \(U\). Its \(S\)-edge module is therefore zero.

The \(C\)-component of the lower square is the boundary equation from the [[node:kl.sheaves.stalk_remainder|stalk-remainder theorem]]. The \(S\)-component is an equality of zero vectors. Together these give
\[
j_e'\rho^{B,-}_e=\rho^{D,-}_e j_x'
\]
on every outgoing edge from \(x\).

### Step 5. Extend over incoming edges

The [[node:kl.sheaves.model_sum_properties|model-sum theorem]] gives \(D\) the prescribed upper quotients, matching those of \(B\). The [[node:kl.sheaves.partial_iso_extension|partial-isomorphism extension theorem]] now applies to the old maps, the new stalk isomorphism \(j_x'\), and the outgoing squares from Step 4.

It constructs the incoming edge isomorphisms through the upper quotient maps and gives a graded partial isomorphism on \(U\cup\{x\}\), as required.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.extend_modelSum`: [SheafMorphisms.lean:1567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1567).
