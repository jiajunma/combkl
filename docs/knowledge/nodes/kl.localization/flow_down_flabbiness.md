---
id: kl.local.flow_down_flabbiness
title: Flow-down sections imply flabbiness
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.flow_down
- kl.detail.structure_sheaves
- kl.local.structure_sheaf_properties
- kl.sheaves.flabbiness
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff
  - OAI.KLInvariance.MomentGraph.Sheaf.flowDown_flabby
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:359
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:372
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.flowDown_flabby
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the strong induction on the assigned upper set, its minimal-vertex
    removal, the zero-support branch, both congruences for the residual, the pairwise
    product divisor and the g+r*t correction. Stated the DecompositionMonoid product
    rule explicitly.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Flow-down sections imply flabbiness

Let \(R\) be a commutative ring whose multiplicative monoid has the DecompositionMonoid structure used in Lean. Its product-divisibility rule says: if finitely many scalars are pairwise relatively prime and each divides \(d\), their product divides \(d\). Polynomial rings over a field satisfy this rule.

Let \(G\) have finite vertex and edge sets, and let \(\mathcal O_c\) be its structure sheaf with labels \(\alpha_e\). Assume:

- the labels in each \(\operatorname{Out}_c(x)\) are pairwise relatively prime;
- a flow-down section exists at every \(x\le c\).

Then \(\mathcal O_c\) is flabby.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The direct construction first proves parity matching in arbitrary lower Bruhat intervals by a simple-reflection involution. In the dihedral application, orbit-spline factors supply the prescribed values and zeros; their product gives flow-down sections. A finite induction on prescribed upper sets proves flabbiness, while generation and quotient maps follow from the structure-sheaf construction. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626), [SheafMorphisms:252](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L252), [SheafMorphisms:288](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L288), [DihedralIntervals:176](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L176), [DihedralIntervals:251](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L251), [DihedralIntervals:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).

**Role in the proof:** The Blueprint follows the parity, normal-form prescription, spline product and flow-down correction arguments. Injectivity of the reflection-preserving group map provides distinct factor data and pairwise relatively prime incident labels. These model properties feed the later local-ring decomposition.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Induct on the prescribed upper set

Let \(U\) be an upper vertex set and \(f\) a compatible assignment on it. Since the vertex set is finite, use strong induction on the finite set \(U\).

For \(U=\varnothing\), the zero global section meets the empty agreement requirement.

For nonempty \(U\), choose a minimal vertex \(x\in U\). The set \(U'=U\setminus\{x\}\) is upper: if \(y\in U'\), \(y\le z\), then \(z\in U\); equality \(z=x\) would contradict minimality of \(x\) and \(y\ne x\).

### Step 2. Extend the smaller prescribed set

Restrict \(f\) to \(U'\). The induction hypothesis gives a global section \(g\) agreeing with \(f\) on \(U'\).

If \(x\not\le c\), its stalk is zero, so \(f_x=g_x=0\). Then \(g\) already agrees on all of \(U\).

Assume henceforth \(x\le c\), so both values at \(x\) are scalars in \(R\).

### Step 3. Divide the remaining error by each outgoing label

Take a supported outgoing edge \(e:x\to y\), with \(y\le c\). Since \(U\) is upper and \(x<y\), its target lies in \(U'\). Thus \(g_y=f_y\).

Compatibility of \(f\) on \(U\) and of \(g\) globally gives
\[
\alpha_e\mid f_x-f_y,\qquad
\alpha_e\mid g_x-g_y.
\]
Subtracting, with \(f_y=g_y\), gives
\[
\alpha_e\mid f_x-g_x.
\]

### Step 4. Divide by the full supported product

This holds for every \(e\in\operatorname{Out}_c(x)\). Pairwise relative primality and the product-divisibility rule imply
\[
P_c(x)\mid f_x-g_x.
\]
Choose \(r\in R\) with
\[
f_x-g_x=P_c(x)r.
\]

### Step 5. Correct the missing value with a flow-down section

Choose a flow-down section \(\theta_x\), and set
\[
h=g+r\theta_x.
\]
The section module is closed under addition and scalar multiplication, so \(h\) is global. At \(x\),
\[
h_x=g_x+rP_c(x)=f_x.
\]

For \(y\in U'\), minimality of \(x\) implies \(y\not\le x\): otherwise \(x\le y\le x\), forcing \(y=x\). Hence \(\theta_x(y)=0\), and
\[
h_y=g_y=f_y.
\]
Thus \(h\) agrees with \(f\) on all of \(U\), completing the induction.

The correction takes place after the smaller upper set has been extended. The lower support of \(\theta_x\) is exactly what preserves its already prescribed values.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.structureCompatible_iff`: [DihedralIntervals.lean:359](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L359).

`OAI.KLInvariance.MomentGraph.Sheaf.flowDown_flabby`: [DihedralIntervals.lean:372](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L372).
