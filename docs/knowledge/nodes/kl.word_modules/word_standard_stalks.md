---
id: kl.detail.word_standard_stalks
title: Free word stalks and exact reflection-edge kernels
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.kernel_exactness
- kl.word.simple_wall_kernel
- kl.word.nonhead_kernel_step
- kl.word.stalk_freeness_step
- kl.word.edge_annihilation
- kl.detail.word_sheaf
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.bottStalk_nil_subsingleton
  - OAI.KLInvariance.TitsSpace.bottStalk_nil_free
  - OAI.KLInvariance.TitsSpace.bottKernelExact_nil
  - OAI.KLInvariance.TitsSpace.bottKernelExact_cons
  - OAI.KLInvariance.TitsSpace.bottStalk_free_cons
  - OAI.KLInvariance.TitsSpace.bottStalkFinite
  - OAI.KLInvariance.TitsSpace.bottStandardStalks
  - OAI.KLInvariance.TitsSpace.bottKernelExact
  - OAI.KLInvariance.TitsSpace.bottStalkFree
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1311
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_nil_subsingleton
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1318
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_nil_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1326
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelExact_nil
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1168
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelExact_cons
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1282
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalk_free_cons
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:997
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkFinite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1510
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStandardStalks
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1518
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelExact
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1520
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1524
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Replaced the combined outline with the complete simultaneous-induction
    assembly, explicit empty-word support, root-sign case, two old hypotheses at each
    new step, finite generation, both edge-kernel inclusions and the free-kernel isomorphism.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Free word stalks and exact reflection-edge kernels

Fix a Coxeter system with finite simple-generator set, its real extended realization \(V\), and \(A=\operatorname{Sym}_{\mathbb R}(V)\). For every word \(\mathbf t\):

1. every image stalk \(M_{\mathbf t}^x\) is finite free over \(A\);
2. \(\mathbf t\) has exact reflection kernels.

Explicitly, if a root \(a\) represents a reflection \(t\), put
\(\beta=\iota(\operatorname{embed}(a))\). Whenever \(\ell(x)<\ell(tx)\),
\[
\pi_x(m)=0\quad\Longrightarrow\quad
\pi_{tx}(m)=\beta z\text{ for some }z\in M_{\mathbf t}^{tx}.
\]
For the upper map \(u:M_{\mathbf t}^{tx}\to Q_{x,tx}\) to the pair-projection edge quotient, it follows that
\[
\ker u=\beta M_{\mathbf t}^{tx},
\qquad
Q_{x,tx}\simeq M_{\mathbf t}^{tx}/\beta M_{\mathbf t}^{tx}.
\]
The upper kernel is free as an \(A\)-module.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Word-image construction before the boundary sheaf.**

**OpenAI notes:** The moment-graph sheaf theorem states the quotient description of an edge module and freeness for the normalized indecomposable boundary sheaf, through the cited moment-graph and Soergel constructions. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The tensor word first supplies explicit subexpression evaluations and image stalks. Right coefficient characters give label annihilation; a first-factor reflection proves the exact kernel across the initial simple reflection. Reflected pair lattices then describe stalks after prepending a letter. [Frobenius:1558](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1558), [Frobenius:2018](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2018), [BottSamelson:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L214), [BottSamelson:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964), [BottSamelson:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130), [BottSamelson:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510), [Support:426](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L426).

**Role in the proof:** The word-length induction proves stalk freeness and exact kernels together. Its two tail maps, quotient regularity and lattice saturation prove the non-head reflection step; the ascent/descent split sequences prove new stalk freeness. Coefficient transport then gives the polynomial word-sheaf input to the boundary-summand construction.
<!-- source-comparison:end -->

*Proof.*

### Step 1. State both induction assertions for all weights

For a word \(\mathbf t\), let \(H_{\mathbf t}\) be exact reflection kernels, including every upward reflection edge and every representing root. Let \(F_{\mathbf t}\) assert freeness of \(M_{\mathbf t}^x\) for every \(x\in W\).

We prove \(H_{\mathbf t}\) and \(F_{\mathbf t}\) simultaneously by induction on the word. Finite generation follows from the stalk projections and will be added in Step 6.

### Step 2. Establish the empty-word case

The empty word has one subexpression, of weight \(1\), and its evaluation is the identity of \(A\). Its stalk at \(1\) is therefore \(A\). At every other weight the coordinate set is empty, so the stalk is zero. Both modules are free.

For an upward reflection edge \(x\to tx\), the upper endpoint cannot be \(1\): otherwise the length inequality would read \(\ell(x)<0\). Its empty-word stalk is zero. Therefore its projection is \(0=\beta\cdot0\), which proves \(H_\varnothing\).

### Step 3. Prove the first-reflection kernel case for the longer word

Assume \(H_{\mathbf t}\) and \(F_{\mathbf t}\), and prepend a simple reflection \(s\). Consider an upward edge \(x\to tx\), a representing root \(a\), and a word vector \(m\) with \(\pi_x^{s\mathbf t}(m)=0\).

If \(t=s\), the [[node:kl.word.simple_wall_kernel|exact first-reflection kernel theorem]] gives
\[
\pi_{sx}^{s\mathbf t}(m)=\alpha_s z.
\]
A representing root of \(s\) equals the simple root or its negative, by uniqueness up to sign. In the first case \(\beta=\alpha_s\), so use \(z\). In the second case \(\beta=-\alpha_s\), so use \(-z\), since
\((-\alpha_s)(-z)=\alpha_s z\).
This proves the required assertion for every representing root of \(s\).

### Step 4. Prove every other reflection-kernel case

If \(t\ne s\), apply the [[node:kl.word.nonhead_kernel_step|non-head kernel theorem]] with the two induction hypotheses \(H_{\mathbf t}\) and \(F_{\mathbf t}\).

Its construction uses the tail vectors \(\mu(m)\) and \(\nu(m)\). Their lower stalk projections vanish at \(x\) and \(sx\). The old exact-kernel assertions on \(x\to tx\) and \(sx\to stx\) give upper projections
\(\beta p\) and \(\chi_s(\beta)q\). Thus the upper local pair is \(\beta(p,q)\) in the twisted pair module.

The roots of \(s\) and \(t\) are nonproportional, so \(\alpha_s\nmid\beta\). Saturation removes this scalar inside the head pair lattice. Its coordinate isomorphism then gives
\(\pi_{tx}^{s\mathbf t}(m)=\beta z\) in the actual new stalk.

Steps 3–4 cover all reflections \(t\), proving \(H_{s\mathbf t}\).

### Step 5. Prove freeness of every new stalk from the old hypotheses

Fix any \(x\in W\). The [[node:kl.word.stalk_freeness_step|stalk-freeness step]] applies to \(H_{\mathbf t}\) and \(F_{\mathbf t}\). It identifies the new stalk with the lattice of the old stalks \(X=M_{\mathbf t}^x\) and \(Y=M_{\mathbf t}^{sx}\).

For \(\ell(x)<\ell(sx)\), the first projection has free kernel isomorphic to \({}^{\chi_s}Y\) and free quotient \(X\). For \(\ell(sx)<\ell(x)\), the other projection has free kernel isomorphic to \(X\) and free quotient \({}^{\chi_s}Y\). Lifting a basis of the quotient splits the relevant sequence.

Thus every new stalk is free, proving \(F_{s\mathbf t}\). Both induction outputs use only the pair \(H_{\mathbf t},F_{\mathbf t}\) for the shorter word. The word length decreases by one at each recursive application, completing the simultaneous induction.

### Step 6. Add finite generation and the edge quotient formula

A word of length \(m\) has a basis indexed by its \(2^m\) bit choices. Each stalk is a surjective image of this finite free module, so it is finitely generated. Combined with Step 5, it is finite free.

For an upward reflection edge, the pair-projection criterion says
\[
u(y)=0\quad\Longleftrightarrow\quad
\exists m,\ \pi_x(m)=0,\ \pi_{tx}(m)=y.
\]
The proved exact-kernel assertion gives \(\ker u\subseteq\beta M_{\mathbf t}^{tx}\). Reflection-label annihilation gives
\(u(\beta z)=\beta u(z)=0\), proving the reverse inclusion.

The upper map is surjective because the lower stalk projection is surjective. It therefore induces a surjective map from
\(M_{\mathbf t}^{tx}/\beta M_{\mathbf t}^{tx}\) to \(Q_{x,tx}\). The kernel equality makes this induced map injective, giving the stated quotient isomorphism.

### Step 7. Identify the upper kernel as a free module

The root \(a\) is nonzero, so its embedded linear polynomial \(\beta\) is nonzero in the coefficient domain. Multiplication by \(\beta\) on the upper stalk is injective, coordinate by coordinate. It is surjective onto \(\beta M_{\mathbf t}^{tx}\) by definition.

Thus multiplication by \(\beta\) is an \(A\)-linear isomorphism from the free upper stalk onto the upper kernel. This proves kernel freeness. Applied to each edge of the pair-projection word sheaf, the same calculation gives its upper-quotient property.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottStalk_nil_subsingleton`: [BottSamelson.lean:1311](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1311).

`OAI.KLInvariance.TitsSpace.bottStalk_nil_free`: [BottSamelson.lean:1318](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1318).

`OAI.KLInvariance.TitsSpace.bottKernelExact_nil`: [BottSamelson.lean:1326](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1326).

`OAI.KLInvariance.TitsSpace.bottKernelExact_cons`: [BottSamelson.lean:1168](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1168).

`OAI.KLInvariance.TitsSpace.bottStalk_free_cons`: [BottSamelson.lean:1282](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1282).

`OAI.KLInvariance.TitsSpace.bottStalkFinite`: [BottSamelson.lean:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L997).

`OAI.KLInvariance.TitsSpace.bottStandardStalks`: [BottSamelson.lean:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510).

`OAI.KLInvariance.TitsSpace.bottKernelExact`: [BottSamelson.lean:1518](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1518).

`OAI.KLInvariance.TitsSpace.bottStalkFree`: [BottSamelson.lean:1520](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1520).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel`: [BottSamelson.lean:1524](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1524).
