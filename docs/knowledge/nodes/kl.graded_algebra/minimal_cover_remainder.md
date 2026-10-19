---
id: kl.algebra.minimal_cover_remainder
title: A free cover splits into a minimal cover and a graded free remainder
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.sheaves.minimal_cover
- kl.algebra.homogeneous_lifts
- kl.algebra.identity_mod_positive
- kl.notes.graded_projective_free
- kl.algebra.projective_presentations
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.exists_minimalCover_split
  - OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv
  - OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv_graded
  - OAI.KLInvariance.Graded.ModuleData.Hom.kernel_free_of_split
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1427
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.exists_minimalCover_split
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1445
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1450
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv_graded
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:1459
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.kernel_free_of_split
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

# A free cover splits into a minimal cover and a graded free remainder

Let \(A\) be a connected nonnegatively graded Noetherian domain. Let
\[
\pi:P\twoheadrightarrow T
\]
be a minimal graded free cover, and let \(f:F\twoheadrightarrow T\) be any degree-zero surjection from a finite nonnegative graded free module.

There are degree-zero maps \(g:F\to P\), \(h:P\to F\) with
\[
\pi g=f,\qquad gh=1_P.
\]
For \(K=\ker g\), there is a graded isomorphism
\[
F\xrightarrow{\sim}P\oplus K,\qquad
v\longmapsto(gv,\ v-hgv),
\]
and \(K\) is finite graded free. Under this isomorphism, \(f\) is the map \((p,k)\mapsto\pi(p)\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Related descent in different coefficient settings.**

**OpenAI notes:** The plane-localization proposition descends through a finite coset graph over an ungraded local ring. Nakayama makes the lifted stalk map surjective, its free target gives a splitting, and projectivity over the local ring makes the remainder free. Multiplicities count copies of local structure models. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** The graded construction lifts in both directions and corrects the composite using invertibility modulo the positive ideal. The remainder is graded projective over a connected Noetherian domain and has a homogeneous basis. Its degrees determine nonnegative shifts of boundary models. Partial isomorphisms already include every edge whose upper endpoint has been processed. [SheafMorphisms:1427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1427), [SheafMorphisms:1567](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1567), [SheafMorphisms:1642](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1642).

**Role in the proof:** Both constructions split a stalk over the upper boundary image and add models centered at the new vertex. The graded construction records a polynomial of shifts at each center; the ungraded local construction records an integer number of copies.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Lift in both directions

[[node:kl.algebra.homogeneous_lifts|Homogeneous lifting]] gives \(g:F\to P\) with \(\pi g=f\), using freeness of \(F\). Applying the same theorem to the surjection \(f\) and the free source \(P\) gives \(h_0:P\to F\) with
\(f h_0=\pi\).

Put \(u=gh_0:P\to P\). For \(p\in P\),
\[
\pi(p-u(p))=\pi(p)-f(h_0(p))=0.
\]
Minimality gives \(p-u(p)\in\ker\pi\subseteq JP\).

### Step 2. Correct the lift to a section

The map \(u\) is degree zero and induces the identity modulo \(J\). The [[node:kl.algebra.identity_mod_positive|identity-modulo-positive-ideal theorem]] makes it a graded automorphism.

Set \(h=h_0u^{-1}\). Then
\(gh=gh_0u^{-1}=uu^{-1}=1_P\).
Also
\[
fh=\pi gh=\pi.
\]

### Step 3. Construct the decomposition and check its inverse

For \(v\in F\),
\[
g(v-hgv)=gv-ghgv=0,
\]
so the second component lies in \(K\). Define
\[
E(v)=(gv,v-hgv),\qquad E^{-1}(p,k)=hp+k.
\]
The first composite is
\[
E^{-1}(E(v))=hgv+v-hgv=v.
\]
For \(k\in K\), \(gk=0\), so
\[
E(hp+k)=(p,hp+k-hp)=(p,k).
\]
Both maps preserve degree because \(g,h\) do and the kernel has its induced grading.

Finally \(f(v)=\pi(gv)\). Thus in the new coordinates, \(f(p,k)=\pi(p)\).

### Step 4. Prove projectivity and graded freeness of the remainder

The map \(q:F\to K\), \(q(v)=v-hgv\), restricts to the identity on \(K\). Hence \(K\) is a direct summand of \(F\).

To see projectivity, take a map \(a:K\to Y\) and a surjection \(X\to Y\). Extend \(a\) to \(F\) by composing with \(q\). A map from the free module \(F\) lifts by choosing preimages of its basis values. Restricting that lift to \(K\) proves the required lifting property.

The kernel is finite because \(A\) is Noetherian and \(F\) is finite. It is nonnegatively graded, as a homogeneous submodule of \(F\). The [[node:kl.notes.graded_projective_free|graded projective-to-free theorem]] supplies a finite homogeneous basis. Every basis degree is nonnegative because its nonzero vector lies in the nonnegative module \(K\).

### Step 5. Compute a cover with an extra degree-two generator

Take \(A=\mathbb R[\alpha]\), \(T=A/(\alpha)\), \(P=A\), and \(F=A\oplus A(2)\). Let
\[
\pi(p)=p\bmod\alpha,\qquad f(u,v)=u\bmod\alpha.
\]
Choose \(g(u,v)=u\) and \(h(p)=(p,0)\). Then
\[
K=0\oplus A(2),\qquad
E(u,v)=(u,(0,v)).
\]
The cover kernel is \(\alpha A\oplus A(2)\), while the remainder \(K\) records the additional free generator beyond the minimal cover.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.exists_minimalCover_split`: [SheafMorphisms.lean:1427](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1427).

`OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv`: [SheafMorphisms.lean:1445](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1445).

`OAI.KLInvariance.Graded.ModuleData.Hom.splitEquiv_graded`: [SheafMorphisms.lean:1450](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1450).

`OAI.KLInvariance.Graded.ModuleData.Hom.kernel_free_of_split`: [SheafMorphisms.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1459).
