---
id: kl.algebra.homogeneous_lifts
title: Homogeneous lifts from a finite graded free module
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.homogeneous_basis
- kl.algebra.dual_basis_degrees
- kl.algebra.homogeneous_subquotients
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.exists_hom_lift_of_basis
  - OAI.KLInvariance.Graded.ModuleData.exists_hom_lift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1348
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.exists_hom_lift_of_basis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1397
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.exists_hom_lift
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

# Homogeneous lifts from a finite graded free module

Let \(A\) be a graded algebra, let \(F,N,P\) be graded \(A\)-modules, and suppose \(F\) has a finite homogeneous basis \((b_i)\), with \(\deg b_i=d_i\). Given degree-zero maps
\[
f:N\twoheadrightarrow P,\qquad g:F\to P,
\]
there is a degree-zero map \(l:F\to N\) satisfying \(fl=g\).

For finite nonnegative graded free \(F\) over a connected nonnegatively graded Noetherian domain, the [[node:kl.notes.graded_projective_free|homogeneous-basis theorem]] supplies the basis needed here. Connected means that every degree-zero scalar comes from the base field.

*Proof.*

### Step 1. Choose a homogeneous preimage for each basis image

The vector \(g(b_i)\) lies in \(P_{d_i}\). Surjectivity gives some \(n_i\in N\) with \(f(n_i)=g(b_i)\).

Decompose \(n_i\) into homogeneous components. Because \(f\) preserves degrees, the degree-\(d_i\) component of \(f(n_i)\) is \(f((n_i)_{d_i})\). Its value is \(g(b_i)\), so
\[
v_i=(n_i)_{d_i}\in N_{d_i},\qquad f(v_i)=g(b_i).
\]

### Step 2. Extend the chosen lifts linearly

Define
\[
l\!\left(\sum_i a_i b_i\right)=\sum_i a_i v_i.
\]
Uniqueness of basis coordinates makes this well defined and \(A\)-linear. On a basis vector,
\(f(l(b_i))=f(v_i)=g(b_i)\). Linearity therefore gives \(fl=g\) on all of \(F\).

### Step 3. Verify the grading

If \(m=\sum_i a_i b_i\in F_n\), the [[node:kl.algebra.dual_basis_degrees|homogeneous-coordinate theorem]] gives
\(a_i\in A_{n-d_i}\). Since \(v_i\in N_{d_i}\), each product \(a_i v_i\) lies in \(N_n\). Their finite sum is in \(N_n\), proving that \(l\) preserves degree.

For example, take \(F=A(1)\), let its generator map to a degree-one vector of \(P\), and choose any preimage in \(N\). Retaining only its degree-one component constructs the required graded lift.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.exists_hom_lift_of_basis`: [GradedModules.lean:1348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1348).

`OAI.KLInvariance.Graded.ModuleData.exists_hom_lift`: [GradedModules.lean:1397](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1397).
