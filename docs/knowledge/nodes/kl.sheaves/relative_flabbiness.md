---
id: kl.sheaves.relative_flabbiness
title: Extension from subsets closed under surviving edges
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - Sheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Sheaves:106
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; sec:localization
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
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
- localization
---

# Extension from subsets closed under surviving edges

Let \(B\) be a sheaf over a commutative ring on an ordered graph with a finite vertex set. Write \(s(e),t(e)\) for the endpoints of an edge. Suppose \(B\) is flabby. Choose a set \(E_0\) of surviving edges, and assume that every edge module outside \(E_0\) is zero. If a vertex subset \(\Omega\) satisfies
\[
e\in E_0,\ s(e)\in\Omega\Longrightarrow t(e)\in\Omega,
\]
every compatible section on \(\Omega\) extends to a global section.

*Proof.*

### Step 1. Formulate the invariant maintained during extension

Let \(L\) be the set of surviving edges, and assume every edge outside \(L\) has zero edge module. We are given a compatible section on \(\Omega\), where
\(s(e)\in\Omega,\ e\in L\) implies \(t(e)\in\Omega\).

We extend it one vertex at a time, retaining both this edge-closure property and all already assigned values. Induct on the finite number of vertices outside \(\Omega\).

### Step 2. Choose the next vertex and use ordinary flabbiness

If no vertex remains, the assignment is global. Otherwise choose a maximal vertex \(a\) outside \(\Omega\). Every \(y>a\) lies in \(\Omega\), so the prescribed assignment restricts to a compatible section on the upper set \(\{y:y>a\}\).

Ordinary flabbiness supplies a global section \(h\) agreeing with those values. Define an ambient assignment \(g\) by \(g_a=h_a\) and \(g_y=f_y\) for \(y\ne a\), where \(f\) is the original assignment. Thus every value on \(\Omega\) is retained.

### Step 3. Check every possible new edge condition

An edge whose two endpoints already lie in \(\Omega\) remains compatible.

For an edge \(a\to y\), maximality gives \(y\in\Omega\), and \(h_y\) equals the prescribed value there. Global compatibility of \(h\) proves the new equation.

An edge \(x\to a\) with \(x\in\Omega\) cannot survive: if it belonged to \(L\), edge closure of \(\Omega\) would force \(a\in\Omega\). Its edge module is therefore zero, so both restriction values equal zero automatically.

These exhaust all edges whose endpoints lie in \(\Omega\cup\{a\}\).

### Step 4. Check closure and continue induction

For a surviving edge with source in the old \(\Omega\), its target was already in \(\Omega\). For one with source \(a\), its target is above \(a\), hence belongs to \(\Omega\) by maximality. Thus \(\Omega\cup\{a\}\) remains closed under surviving edges.

Exactly one missing vertex has been added, and all prescribed values were retained. Apply the induction hypothesis to this enlarged set and its compatible assignment. The resulting global section agrees with the new assignment on the enlarged set, and hence with the original assignment on \(\Omega\).

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L2).

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.extend_closedUnder`: [Sheaves.lean:106](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L106).
