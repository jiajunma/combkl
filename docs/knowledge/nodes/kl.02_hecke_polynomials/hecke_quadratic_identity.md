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

It is enough to evaluate both sides on each basis vector \(e_w\). If \(\ell(sw)>\ell(w)\), then \(L_se_w=e_{sw}\), and the second application crosses a descent:
\[
L_s^2e_w=e_w+ae_{sw}=e_w+aL_se_w.
\]
If \(\ell(sw)<\ell(w)\), then \(L_se_w=e_{sw}+ae_w\). Applying \(L_s\) and using the opposite ascent from \(sw\) gives
\[
L_s^2e_w=e_w+ae_{sw}+a^2e_w=e_w+aL_se_w.
\]
The two cases exhaust the simple-reflection length alternatives. No inverse of \(a\) is required. Rearranging also shows that \(L_s-a\) is the inverse of \(L_s\).

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.Hecke.left_quadratic`: [Hecke.lean:83](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean#L83).
