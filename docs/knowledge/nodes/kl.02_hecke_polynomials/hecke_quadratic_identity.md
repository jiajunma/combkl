---
id: kl.detail.hecke_quadratic_identity
title: The Hecke operators satisfy the quadratic relation
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.definitions.hecke_operators
- kl.definitions.hecke_quadratic_relation
lean:
  repository: openai-kl
  modules:
  - Hecke
  declarations:
  - OAI.KLInvariance.Hecke.left_quadratic
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Hecke:83
    format: lean-location
    note: OAI.KLInvariance.Hecke.left_quadratic
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
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
- hecke_polynomials
---

# The Hecke operators satisfy the quadratic relation

For the normalized Hecke operator \(L_s\) with parameter \(a\) over a commutative coefficient ring,
\[
L_s^2=1+aL_s.
\]
Thus the operators constructed from Coxeter length satisfy the stated Hecke quadratic relation.

*Proof.*

### Step 1. Reduce the operator equation to basis vectors

Both sides are linear operators on the free module with basis \(e_w\), so equality is equivalent to equality on each \(e_w\). Fix \(w\). A simple reflection changes its length by exactly one, so there are precisely two cases.

### Step 2. Compute the ascent case

If \(\ell(sw)=\ell(w)+1\), then
\(L_se_w=e_{sw}\).
The second application is a descent, since \(s(sw)=w\), and therefore
\[
L_s^2e_w=L_se_{sw}=e_w+ae_{sw}=e_w+aL_se_w.
\]

### Step 3. Compute the descent case

If \(\ell(sw)=\ell(w)-1\), the defining formula gives
\(L_se_w=e_{sw}+ae_w\).
Now \(L_se_{sw}=e_w\), because multiplication by \(s\) raises \(sw\) to \(w\). Linearity yields
\[
L_s^2e_w
=L_s(e_{sw}+ae_w)
=e_w+a(e_{sw}+ae_w)
=e_w+aL_se_w.
\]

### Step 4. Conclude and check the inverse

The cases exhaust all \(w\), hence \(L_s^2=1+aL_s\).
Subtract \(aL_s\) to obtain
\(L_s(L_s-a)=1\).
The scalar operator \(a\) commutes with \(L_s\), so also
\((L_s-a)L_s=1\). Thus \(L_s-a\) is its inverse without requiring \(a\) to be a unit.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.Hecke.left_quadratic`: [Hecke.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L83).
