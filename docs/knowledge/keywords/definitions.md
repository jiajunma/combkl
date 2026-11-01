---
title: The quadratic relation and the constructions it supports
primary_topic: kl.02_hecke_polynomials
---

For a normalized simple Hecke operator \(L_s\) with coefficient parameter \(a\), the quadratic relation is
\[
L_s^2=I+aL_s.
\]
Here \(I\) is the identity operator on the standard module. The relation fixes the coefficient convention and gives \(L_s^{-1}=L_s-aI\). On a pair of standard basis vectors interchanged by the simple reflection, the relation is an explicit two-by-two matrix calculation.

The one-generator quadratic relation works together with the relations between different simple generators. Those operator identities permit the bar construction to be read independently of a chosen word. The normalized R-polynomials then appear as its coefficients and satisfy the descent recursion.

The main invariance theorem ultimately compares the canonical polynomial families defined from this Hecke structure. This page starts with the exact quadratic definition and follows the operator, inverse and bar constructions into those families, so the normalization used by the rest of the Blueprint is visible from the beginning.

## Reading sequence

1. [[node:kl.definitions.hecke_operators]] — Read the module and operator convention.
2. [[node:kl.definitions.hecke_quadratic_relation]] — Compute the quadratic identity and inverse.
3. [[node:kl.notes.hecke_action]] — Place the identities in the full operator construction.
4. [[node:kl.definitions.bar_involution]] — Build the bar map.
5. [[node:kl.detail.rtilde_family]] — Read the resulting coefficient family.
6. [[node:kl.foundations.canonical_kl]] — Reach canonical polynomial uniqueness.
