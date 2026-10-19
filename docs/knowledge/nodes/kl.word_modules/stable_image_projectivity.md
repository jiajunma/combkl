---
id: kl.word.stable_image_projectivity
title: Projectivity of image modules on a reflection-stable set
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.upper_image_properties
- kl.word.set_tail_detection
- kl.algebra.projective_range_splittings
- kl.word.local_pair_maps
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottTensorEnd
  - OAI.KLInvariance.TitsSpace.bottTensorEnd_first
  - OAI.KLInvariance.TitsSpace.bottTensorEnd_second
  - OAI.KLInvariance.TitsSpace.bottTensorEnd_set_preserve
  - OAI.KLInvariance.TitsSpace.bottTensorEnd_set_kills
  - OAI.KLInvariance.TitsSpace.bottStableUpper_projective
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:707
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensorEnd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:719
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensorEnd_first
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:725
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensorEnd_second
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1264
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensorEnd_set_preserve
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1283
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottTensorEnd_set_kills
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1299
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStableUpper_projective
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read the actual tensor endomorphism, coordinate preservation, kernel killing
    and projective_of_end application. Retained only reflection stability of U, without
    an extra upper-set hypothesis.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Projectivity of image modules on a reflection-stable set

Fix a finite-generator Coxeter system, a simple reflection \(s\), and a tail word \(\mathbf t\). Let \(U\subseteq W\) be reflection-stable, so \(sU=U\).

If \(L_{\mathbf t}(U)\) is projective over the symmetric coefficient algebra \(A\), then \(L_{s\mathbf t}(U)\) is projective.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Split the old image projection

Write \(N=M_{\mathbf t}\), \(N'=M_{s\mathbf t}\), and \(p:N\twoheadrightarrow L_{\mathbf t}(U)\). Projectivity supplies a linear section
\[
\sigma:L_{\mathbf t}(U)\to N,\qquad p\sigma=1.
\]
Set \(e=\sigma p\). Then \(pe=p\), and \(p(n)=0\) implies \(e(n)=\sigma(0)=0\).

In coordinates, \(e\) preserves \(\pi_x(n)\) for every \(x\in U\).

### Step 2. Extend the endomorphism through the tensor step

Define
\[
\widetilde e:N'=A\otimes_{A^s}N\to N',
\qquad a\otimes n\mapsto a\otimes e(n).
\]
Since \(e\) is \(A\)-linear, it is linear over \(A^s\), so this map respects tensor relations and is \(A\)-linear.

The tail formulas give
\[
\mu(\widetilde e(m))=e(\mu(m)),\qquad
\nu(\widetilde e(m))={}^\tau e(\nu(m)).
\]
For example, on \(a\otimes n\), the underlying second equality is
\(\tau(a)e(n)=e(\tau(a)n)\). Additivity extends both identities to every \(m\).

### Step 3. Prove preservation of the new image coordinates

For \(x\in U\), reflection stability gives \(sx\in U\). Step 1 says that \(e\) preserves the ordinary-tail projection at \(x\) and the reflected-tail projection at \(sx\).

Step 2 therefore shows that the local pair of \(\widetilde e(m)\) at \(x\) equals that of \(m\). The [[node:kl.word.local_pair_maps|local-pair coordinate theorem]] gives
\(\pi_x^{s\mathbf t}(\widetilde e(m))=\pi_x^{s\mathbf t}(m)\).
Collecting over \(x\in U\) proves
\[
p_U'\widetilde e=p_U'.
\]

### Step 4. Prove that the endomorphism kills the projection kernel

Suppose \(p_U'(m)=0\). [[node:kl.word.set_tail_detection|Set-tail detection]] gives
\(p_U(\mu(m))=0\) and \(p_{sU}(\nu(m))=0\).
Since \(sU=U\), Step 1 kills both tail vectors after applying \(e\).

Step 2 then gives \(\mu(\widetilde e(m))=0\) and
\(\nu(\widetilde e(m))=0\). The [[node:kl.word.set_tail_detection|whole-word tail-detection theorem]] implies \(\widetilde e(m)=0\).

### Step 5. Descend to a split image

The new word module \(N'\) is finite free, hence projective. Its image projection \(p_U'\) is surjective. Steps 3–4 give the two hypotheses of the [[node:kl.algebra.projective_range_splittings|projective-image splitting theorem]] for \(\widetilde e\).

That theorem descends \(\widetilde e\) to a section of \(p_U'\). The new image is thus a direct summand of the projective word module, proving projectivity.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottTensorEnd`: [IntegralPairings.lean:707](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L707).

`OAI.KLInvariance.TitsSpace.bottTensorEnd_first`: [IntegralPairings.lean:719](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L719).

`OAI.KLInvariance.TitsSpace.bottTensorEnd_second`: [IntegralPairings.lean:725](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L725).

`OAI.KLInvariance.TitsSpace.bottTensorEnd_set_preserve`: [IntegralPairings.lean:1264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1264).

`OAI.KLInvariance.TitsSpace.bottTensorEnd_set_kills`: [IntegralPairings.lean:1283](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1283).

`OAI.KLInvariance.TitsSpace.bottStableUpper_projective`: [IntegralPairings.lean:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299).
