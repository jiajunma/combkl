---
id: kl.algebra.minimal_cover_maps
title: Isomorphisms determined by maps of minimal covers
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.minimal_cover
- kl.algebra.homogeneous_lifts
- kl.algebra.identity_mod_positive
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - GradedModules
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.MinimalCover.hom_bijective
  - OAI.KLInvariance.Graded.ModuleData.MinimalCover.bijective_of_boundaryIso
  - OAI.KLInvariance.Graded.ModuleData.MinimalCover.equiv
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:482
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.MinimalCover.hom_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1171
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.MinimalCover.bijective_of_boundaryIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1422
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.MinimalCover.equiv
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

# Isomorphisms determined by maps of minimal covers

Let \(A\) be a connected nonnegatively graded Noetherian domain over a field. Put \(J=A_{>0}\), and let all modules below be finite and nonnegatively graded.

Suppose
\[
\pi:F\twoheadrightarrow T,\qquad \rho:G\twoheadrightarrow T
\]
are minimal graded free covers. Thus \(F,G\) are free, the maps preserve degree, and
\[
\ker\pi\subseteq JF,\qquad \ker\rho\subseteq JG.
\]
If a degree-zero map \(f:F\to G\) satisfies \(\rho f=\pi\), then \(f\) is a graded isomorphism. Consequently any two minimal graded free covers of \(T\) are isomorphic by a map commuting with their projections.

There is also a version for a specified automorphism of the covered module: if \(a:T\xrightarrow{\sim}T\) preserves degree and \(f:F\to F\) satisfies \(\pi f=a\pi\), then \(f\) is a graded automorphism.

*Proof.*

### Step 1. Lift a map in the reverse direction

For the first statement, use the [[node:kl.algebra.homogeneous_lifts|homogeneous lifting theorem]] with the free source \(G\), the surjection \(\pi:F\to T\), and the map \(\rho:G\to T\). It produces a degree-zero map \(g:G\to F\) with
\[
\pi g=\rho.
\]

### Step 2. Compare both composites with the identity

For \(v\in F\),
\[
\pi(v-gf(v))=\pi(v)-\rho(f(v))=0,
\]
using \(\pi g=\rho\) and \(\rho f=\pi\). Hence \(v-gf(v)\in\ker\pi\subseteq JF\).

For \(w\in G\),
\[
\rho(w-fg(w))=\rho(w)-\pi(g(w))=0,
\]
so \(w-fg(w)\in\ker\rho\subseteq JG\).

Both \(gf\) and \(fg\) therefore induce the identity modulo the positive ideal. The [[node:kl.algebra.identity_mod_positive|identity-modulo-positive-ideal theorem]] makes them bijective.

### Step 3. Deduce bijectivity of the specified map

If \(f(v)=0\), then \(gf(v)=0\), and injectivity of \(gf\) gives \(v=0\). Thus \(f\) is injective.

Given \(w\in G\), surjectivity of \(fg\) gives a \(w'\in G\) with \(fg(w')=w\). Then \(v=g(w')\) satisfies \(f(v)=w\). Thus \(f\) is surjective.

A bijective degree-zero linear map has a degree-zero inverse by the homogeneous-component argument, so \(f\) is a graded isomorphism.

### Step 4. Cover an automorphism of the target

For the second statement, the inverse \(a^{-1}\) preserves degree: decompose a preimage into homogeneous components and use injectivity of \(a\), exactly as for \(f^{-1}\) in Step 3.

Lift the map \(a^{-1}\pi:F\to T\) through \(\pi\), obtaining a degree-zero \(l:F\to F\) with
\(\pi l=a^{-1}\pi\). Then
\[
\pi fl=a\pi l=aa^{-1}\pi=\pi,\qquad
\pi lf=a^{-1}\pi f=a^{-1}a\pi=\pi.
\]
Consequently \(1-fl\) and \(1-lf\) have images in \(\ker\pi\subseteq JF\). The [[node:kl.algebra.identity_mod_positive|identity-modulo-positive-ideal theorem]] makes both composites bijective. Injectivity of \(lf\) and surjectivity of \(fl\) give bijectivity of \(f\), as in Step 3.

### Step 5. Construct a comparison between any two covers

Use the [[node:kl.algebra.homogeneous_lifts|homogeneous lifting theorem]] with the free source \(F\), the surjection \(\rho:G\to T\), and the map \(\pi:F\to T\). It gives a degree-zero \(f:F\to G\) with \(\rho f=\pi\). Steps 1–3 prove that this comparison is an isomorphism.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.MinimalCover.hom_bijective`: [EdgeLocalization.lean:482](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L482).

`OAI.KLInvariance.Graded.ModuleData.MinimalCover.bijective_of_boundaryIso`: [SheafMorphisms.lean:1171](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1171).

`OAI.KLInvariance.Graded.ModuleData.MinimalCover.equiv`: [GradedModules.lean:1422](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1422).
