---
id: kl.local.stalk_splitting
title: Splitting a stalk while retaining all outgoing restrictions
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.local.cover_splitting
- kl.sheaves.boundary_image_transport
- kl.detail.sheaf_isomorphisms
- kl.detail.compatible_sections
- kl.sheaves.flabbiness
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:766
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: 'Read AboveIso.extend_stalk: constructed N as the actual outgoing image,
    verified both codomain-restricted surjections and equality of the cover kernel,
    applied the single-lift local splitting, and evaluated the resulting identity
    at each outgoing edge.'
tags:
- Kazhdan-Lusztig
- local-decomposition
---

# Splitting a stalk while retaining all outgoing restrictions

Let \(R\) be a commutative local ring with maximal ideal \(\mathfrak m\), and let \(B,C\) be sheaves on an ordered graph. Fix an isomorphism \(j\) above a vertex \(x\). Write \(d_x^B,d_x^C\) for the full outgoing stalk maps and \(j_e\) for its edge isomorphisms.

Assume both sheaves are globally generated and flabby, both stalks \(B^x,C^x\) are finite free, and
\[
\ker d_x^C\subseteq\mathfrak mC^x.
\]
Then there is a linear map \(g:B^x\to C^x\) and an isomorphism
\[
e_x:B^x\xrightarrow{\sim}C^x\oplus Q,\qquad Q=\ker g,
\]
where \(Q\) is finite free, such that for every outgoing edge \(e\) and \(v\in B^x\),
\[
j_e(\rho^{B,-}_e(v))
=\rho^{C,-}_e((e_x(v))_1).
\]
Thus the first summand retains every prescribed outgoing restriction.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The same single-lift local-ring argument.**

**OpenAI notes:** The local decomposition lifts the given stalk map through the existing model stalk cover. Minimality makes the lift surjective after reduction modulo the maximal ideal; Nakayama gives surjectivity, the free target supplies a section, and the finite projective kernel is free over the local ring. [loc:decomposition](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L285).

**Lean (primary):** LocalCover first proves the surjectivity of a single lift with a finite target and the displayed kernel condition. It then constructs the lift and right inverse, gives the explicit splitting map and proves the kernel finite projective and free. AboveIso.extend_stalk constructs the common outgoing image and applies this algebraic theorem. [ModuleAlgebra:165](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L165), [ModuleAlgebra:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean#L206), [GradedSheaves:766](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L766).

**Role in the proof:** The Blueprint follows the single-lift proof and writes the cover triangle, splitting inverse, kernel projection and each outgoing restriction equality. The graded two-lift argument belongs to the separate graded construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Identify the common outgoing image

Put \(\Delta_x(B)=\prod_{e:s(e)=x}B^e\), and define \(\Delta_x(C)\) in the same way. Let \(J:\Delta_x(B)\simeq\Delta_x(C)\) be the product edge isomorphism. The [[node:kl.sheaves.boundary_image_transport|boundary-image transport theorem]] gives
\[
J(\operatorname{im}d_x^B)=\operatorname{im}d_x^C.
\]
Put \(N=\operatorname{im}d_x^C\), viewed as an actual submodule of \(\Delta_x(C)\).

Define
\[
\pi:C^x\to N,\qquad \pi(c)=d_x^C(c),
\]
with its codomain restricted to the image. This map is surjective by the definition of \(N\).

### Step 2. Construct the second surjection onto that image

Define
\[
\varphi:B^x\to N,\qquad
\varphi(b)=J(d_x^B(b)).
\]
Step 1 shows that every value lies in \(N\), so the codomain restriction is defined.

For \(n\in N\), the same image equality supplies \(b\in B^x\) with
\(J(d_x^B(b))=n\). Thus \(\varphi\) is onto.

The inclusion \(N\hookrightarrow\Delta_x(C)\) is injective. Therefore
\[
\ker\pi=\ker d_x^C\subseteq\mathfrak mC^x.
\]

### Step 3. Split the two covers of the common image

The two source modules \(B^x,C^x\) are finite free, \(\pi,\varphi\) are onto, and \(\pi\) has the required kernel condition.

The [[node:kl.local.cover_splitting|local cover-splitting theorem]] gives a surjective lift \(g:B^x\to C^x\), a finite free kernel \(Q\), and an isomorphism \(e_x\) with
\[
\pi((e_x(b))_1)=\varphi(b).
\]

### Step 4. Evaluate the equality at each edge

Both sides of the last equality are elements of the submodule
\(N\subseteq\Delta_x(C)\). Include them in the boundary module and evaluate at an outgoing edge \(e\).

The left side becomes
\(\rho^{C,-}_e((e_x(b))_1)\). The right side becomes
\(j_e(\rho^{B,-}_e(b))\), by the coordinate formula for \(J\). This is the required commuting equality for every outgoing edge.

The kernel \(Q\) therefore supplies the new free directions while the \(C^x\)-component carries all outgoing data already determined above \(x\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.AboveIso.extend_stalk`: [GradedSheaves.lean:766](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L766).
