---
id: kl.word.upper_projectivity_step
title: The projectivity step for an upper-coordinate image
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.upper_image_properties
- kl.word.upper_set_reflection
- kl.word.stable_image_projectivity
- kl.word.common_kernel_equivalence
- kl.algebra.two_stage_projectivity
- kl.algebra.projective_range_splittings
- kl.algebra.scalar_twist
- kl.word.set_tail_detection
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottInter_first_zero
  - OAI.KLInvariance.TitsSpace.bottInterKernelFirst_surjective
  - OAI.KLInvariance.TitsSpace.bottCommon_projective
  - OAI.KLInvariance.TitsSpace.bottProjectiveUpper_cons
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1373
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottInter_first_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1379
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottInterKernelFirst_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1392
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottCommon_projective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1408
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectiveUpper_cons
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read bottInterKernelFirst_surjective, bottCommon_projective and bottProjectiveUpper_cons.
    Checked all three projective modules, both surjections and the old-word lifting
    input in the exact source construction order.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The projectivity step for an upper-coordinate image

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\). Suppose a word \(\mathbf t\) has both properties:

1. \(L_{\mathbf t}(U)\) is projective for every Bruhat upper set \(U\);
2. every compatible stalk tuple on an upper set has a common word lift.

Then, for every simple reflection \(s\), the longer word \(s\mathbf t\) has projective coordinate images on every Bruhat upper set.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Choose the two-stage maps

Fix an upper set \(U\), and put \(J=U\cup sU\), \(K=U\cap sU\). Both sets are upper and reflection-stable. Write \(L=L_{\mathbf t}\), \(L'=L_{s\mathbf t}\).

Use
\[
r:L'(U)\to L'(K),\qquad
F_U:L'(U)\to L(U),\qquad
k:L(U)\to L(K).
\]
The restrictions \(r,k\) are surjective. The identity
\(kF_U=F_Kr\) gives a map
\[
\bar F:\ker r\to\ker k.
\]

### Step 2. Prove surjectivity on the first kernel

Take \(z\in\ker k\). Choose \(n\in M_{\mathbf t}\) with \(p_U(n)=z\).
Its projection to \(K\) is \(k(z)=0\).

Since \(K\) is reflection-stable, [[node:kl.word.set_tail_detection|seed vanishing]] gives
\(p_K'(1\otimes n)=0\). Therefore \(w=p_U'(1\otimes n)\) lies in \(\ker r\). The first-map seed formula gives
\[
\bar F(w)=F_U(p_U'(1\otimes n))=p_U(n)=z.
\]
Thus \(\bar F\) is surjective.

### Step 3. Prove projectivity of the outer target and the first quotient

The first hypothesis gives projectivity of \(L(K)\). Since \(K\) is reflection-stable, [[node:kl.word.stable_image_projectivity|stable-image projectivity]] gives projectivity of \(L'(K)\).

Both \(L(U)\) and \(L(K)\) are projective by the first hypothesis. The surjective restriction \(k\) therefore has projective kernel, by the [[node:kl.algebra.projective_range_splittings|projective split-sequence theorem]]. Hence \(\ker k\) is projective.

### Step 4. Prove projectivity of the common kernel

Put
\[
D=\ker r\cap\ker F_U,\qquad
T=\ker(L(J)\to L(U)).
\]
The first hypothesis makes \(L(J)\) and \(L(U)\) projective. Their restriction is surjective, so \(T\) is projective. Its scalar twist \({}^\tau T\) is projective as well.

The second hypothesis is exactly the compatible-tuple lifting input to the [[node:kl.word.common_kernel_equivalence|common-kernel theorem]]. That theorem identifies \(D\simeq{}^\tau T\), proving that \(D\) is projective.

### Step 5. Apply the [[node:kl.algebra.two_stage_projectivity|two-stage projectivity theorem]]

All its inputs have now been checked: \(r\) and \(\bar F\) are surjective, while \(L'(K)\), \(\ker k\), and \(D\) are projective. The theorem applies successively to
\[
0\to D\to\ker r\to\ker k\to0
\]
and
\[
0\to\ker r\to L'(U)\to L'(K)\to0.
\]
It proves projectivity of \(L'(U)\). Since \(U\) was arbitrary, the longer word has upper-image projectivity.

This is the source's bottProjectiveUpper_cons. Its two hypotheses belong to the shorter word; the prime-denominator lifting theorem supplies the second from the first when the full word induction is assembled.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottInter_first_zero`: [IntegralPairings.lean:1373](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1373).

`OAI.KLInvariance.TitsSpace.bottInterKernelFirst_surjective`: [IntegralPairings.lean:1379](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1379).

`OAI.KLInvariance.TitsSpace.bottCommon_projective`: [IntegralPairings.lean:1392](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1392).

`OAI.KLInvariance.TitsSpace.bottProjectiveUpper_cons`: [IntegralPairings.lean:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408).
