---
id: kl.word.head_pair_equivalence
title: The new word stalk is the reflected pair lattice
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.head_pair_coordinates
- kl.word.evaluation_grading
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_injective
  - OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_seed
  - OAI.KLInvariance.TitsSpace.bottHeadPairToStalk
  - OAI.KLInvariance.TitsSpace.bottHeadPair_range
  - OAI.KLInvariance.TitsSpace.bottHeadPairToStalk_surjective
  - OAI.KLInvariance.TitsSpace.bottHeadPairEquiv
  - OAI.KLInvariance.TitsSpace.bottHeadLeft
  - OAI.KLInvariance.TitsSpace.bottHeadRight
  - OAI.KLInvariance.TitsSpace.bottHeadLeft_surjective
  - OAI.KLInvariance.TitsSpace.bottHeadPairEquiv_coordinates
  - OAI.KLInvariance.TitsSpace.bottHeadLeft_homogeneous
  - OAI.KLInvariance.TitsSpace.bottHeadRight_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:135
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:172
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_seed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:181
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairToStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:197
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPair_range
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:207
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairToStalk_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:214
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:629
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLeft
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:636
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:644
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLeft_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:649
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadPairEquiv_coordinates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:655
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadLeft_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:669
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottHeadRight_homogeneous
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the seed/range proof of headPairEquiv, coordinate recovery and both
    head projection definitions. Retained the real-linear type and tau-semilinearity
    of the right projection, then checked both homogeneous coordinate arguments.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The new word stalk is the reflected pair lattice

Fix a finite-generator Coxeter system, a simple reflection \(s\), a tail word \(\mathbf t\), and \(x\in W\). Let \(A=\operatorname{Sym}_{\mathbb R}(V)\) for its real extended realization \(V\), and let \(\tau=\chi_s\) be the coefficient action. Put
\[
X=M_{\mathbf t}^x,\qquad Y=M_{\mathbf t}^{sx},\qquad
f=\pi_x,\quad g=\pi_{sx}.
\]
Let \(L_x\subseteq X\oplus{}^\tau Y\) be their reflected pair lattice.

The map
\[
C_x:L_x\xrightarrow{\sim}M_{s\mathbf t}^x,\qquad
(p,q)\longmapsto
\begin{cases}
p_\eta&\text{on the zero-bit block},\\
\tau(q_\eta)&\text{on the one-bit block}
\end{cases}
\]
is an \(A\)-linear isomorphism. Under this identification, the head projections are
\[
h_0:C_x(p,q)\mapsto p,\qquad h_1:C_x(p,q)\mapsto q.
\]
The first is \(A\)-linear and surjective. The second is \(\tau\)-semilinear, and therefore real-linear. Both preserve the degree-one grading.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Recover each coordinate of a pair

The coordinate map is \(A\)-linear by the calculation in its definition. Suppose \(C_x(p,q)=C_x(p',q')\). Evaluating at every zero-bit coordinate gives \(p_\eta=p'_\eta\), hence \(p=p'\) in the first stalk.

Evaluating at the one-bit coordinates gives
\(\tau(q_\eta)=\tau(q'_\eta)\). Injectivity of \(\tau\) gives equality of all coordinates of \(q,q'\), hence \(q=q'\). Thus \(C_x\) is injective on the ambient pair module and on its lattice.

### Step 2. Send every lattice pair into the new stalk

If \((p,q)\in L_x\), choose \(n\in M_{\mathbf t}\) with \(f(n)=p\) and \(g(n)=q\). The evaluation recursion gives
\[
C_x(p,q)=E_{s\mathbf t,x}(1\otimes n).
\]
It is therefore in the image defining \(M_{s\mathbf t}^x\). This defines the codomain-restricted map bottHeadPairToStalk.

### Step 3. Show that the new stalk lies in this image

For a pure tensor \(a\otimes n\), linearity gives
\[
E_{s\mathbf t,x}(a\otimes n)
=a\,E_{s\mathbf t,x}(1\otimes n)
=a\,C_x(f(n),g(n)).
\]
The pair \((f(n),g(n))\) belongs to \(L_x\), and scalar closure of the twisted lattice places its multiple there too. Thus every pure-tensor evaluation is in the image of the linear map \(C_x|_{L_x}\).

Every tensor is a finite sum of pure tensors. The image of a linear map is closed under addition, so all word evaluations lie in this image. Since the stalk consists exactly of those evaluations, the map is surjective. Together with Step 1 this proves the isomorphism.

### Step 4. Define and check the head projections

Apply \(C_x^{-1}\), then project to its first or second coordinate. The first projection is \(A\)-linear. If \(p\in X\), surjectivity of \(f\) gives \(n\) with \(f(n)=p\); the pair \((f(n),g(n))\) proves surjectivity of \(h_0\).

For the second projection, the lattice scalar law gives
\[
h_1(az)=\tau(a)h_1(z).
\]
Since \(\tau\) fixes real scalars, \(h_1\) is real-linear. This is the scalar structure used in the source's bottHeadRight; its value is the underlying vector of the twisted second stalk.

### Step 5. Verify the homogeneous degrees

Choose a basis of the extended realization and use the resulting coefficient grading. A degree-\(n\) stalk vector has every evaluation coordinate in \(A_n\).

The coordinates of \(h_0(z)\) are precisely the zero-bit coordinates of \(z\), so they lie in \(A_n\). The one-bit coordinates of \(z\) are \(\tau((h_1(z))_\eta)\). Apply \(\tau\), which preserves degree and squares to the identity, to conclude \((h_1(z))_\eta\in A_n\).

Thus both head projections preserve degree. These maps give the two orientations used in the later stalk-character recursion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_injective`: [BottSamelson.lean:135](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L135).

`OAI.KLInvariance.TitsSpace.bottHeadPairCoordinates_seed`: [BottSamelson.lean:172](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L172).

`OAI.KLInvariance.TitsSpace.bottHeadPairToStalk`: [BottSamelson.lean:181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L181).

`OAI.KLInvariance.TitsSpace.bottHeadPair_range`: [BottSamelson.lean:197](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L197).

`OAI.KLInvariance.TitsSpace.bottHeadPairToStalk_surjective`: [BottSamelson.lean:207](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L207).

`OAI.KLInvariance.TitsSpace.bottHeadPairEquiv`: [BottSamelson.lean:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214).

`OAI.KLInvariance.TitsSpace.bottHeadLeft`: [BottSamelson.lean:629](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L629).

`OAI.KLInvariance.TitsSpace.bottHeadRight`: [BottSamelson.lean:636](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L636).

`OAI.KLInvariance.TitsSpace.bottHeadLeft_surjective`: [BottSamelson.lean:644](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L644).

`OAI.KLInvariance.TitsSpace.bottHeadPairEquiv_coordinates`: [BottSamelson.lean:649](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L649).

`OAI.KLInvariance.TitsSpace.bottHeadLeft_homogeneous`: [BottSamelson.lean:655](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L655).

`OAI.KLInvariance.TitsSpace.bottHeadRight_homogeneous`: [BottSamelson.lean:669](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L669).
