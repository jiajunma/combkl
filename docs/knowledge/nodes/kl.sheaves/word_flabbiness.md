---
id: kl.detail.word_flabbiness
title: Flabbiness of the actual word sheaf
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.word_sheaf
- kl.sheaves.flabbiness
- kl.notes.reflection_frobenius
- kl.notes.tensor_pairing
- kl.notes.reflection_faithfulness
- kl.detail.bruhat_lifting
- kl.detail.word_evaluation_injective
- kl.detail.word_standard_stalks
- kl.word.upper_image_properties
- kl.word.upper_projectivity_step
- kl.word.common_kernel_equivalence
- kl.word.stable_image_projectivity
- kl.word.head_patch_lifting
- kl.algebra.projective_local_membership
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - OAI.KLInvariance.TitsSpace.bottFlabby
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
  - OAI.KLInvariance.TitsSpace.bottProjectiveUpper_cons
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2109
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectiveUpper
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2114
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottFlabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2192
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Flabbiness of the actual word sheaf

For a reduced word \(\mathbf s\) with product \(b\), its pair-projection sheaf on \([1,b]\) is flabby. Thus every compatible section on an upper subset extends to a global section.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module first gives image modules on arbitrary weight sets. On upper sets, the word induction proves projectivity using a tensor endomorphism and two kernel sequences; the common-kernel comparison uses compatible-tuple lifting for the shorter word. A fixed-word prime-denominator argument derives that lifting property from projectivity. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057).

**Role in the proof:** The Blueprint follows the image maps, patched tails and split sequences. This preserves both hypotheses of the induction step and explains the word-module input used to construct the interval sheaf extension property.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Use projectivity and its lifting consequence at the shorter word

For each fixed word \(\mathbf t\), the prime-denominator argument in Steps 4–5 proves the implication
\[
\text{upper-image projectivity for }\mathbf t
\Longrightarrow
\text{compatible-tuple lifting for }\mathbf t.
\]
The word induction proves upper-image projectivity. At its induction step, apply this implication to the shorter word to obtain the lifting hypothesis required by the [[node:kl.word.upper_projectivity_step|conditional projectivity step]].

For the empty word, the only nonzero stalk is \(A\) at weight \(1\). Its image on a set \(U\) is \(A\) when \(1\in U\), and zero otherwise. Both are projective, establishing the induction base.

### Step 2. Use the two-stage image coordinates

Fix an upper set \(U\), and put \(J=U\cup sU\), \(K=U\cap sU\).
Both are upper and reflection-stable. The two-stage kernel data consist of
\[
r:L_{s\mathbf t}(U)\twoheadrightarrow L_{s\mathbf t}(K),\quad
F_U:L_{s\mathbf t}(U)\to L_{\mathbf t}(U),\quad
k:L_{\mathbf t}(U)\twoheadrightarrow L_{\mathbf t}(K).
\]
The first image map commutes with restriction, so it induces
\(\bar F:\ker r\to\ker k\).
This induced map is surjective: lift \(z\in\ker k\) to an old word vector \(n\), then use the new projection of \(1\otimes n\). It vanishes on the stable set \(K\) and has first image \(z\).

The [[node:kl.word.common_kernel_equivalence|common-kernel theorem]] identifies
\[
D=\ker r\cap\ker F_U
\simeq{}^\tau\ker(L_{\mathbf t}(J)\to L_{\mathbf t}(U)).
\]
Its forward construction patches the reflected tail on \(sU\) with the ordinary tail on \(U\). The overlap values are zero. The [[node:kl.word.head_patch_lifting|patched-tail theorem]] verifies every crossing edge and applies the shorter word's compatible-tuple lifting property. The reverse construction inserts an old lift as \(1\otimes n\). Injective second-coordinate maps turn these two image containments into a linear isomorphism.

### Step 3. Deduce projectivity using the actual tensor splitting

By the induction hypothesis, the old images on \(U,J,K\) are projective.
Surjective restrictions between them have projective kernels. Twisting preserves projectivity, so the identified common kernel \(D\) is projective.

On the stable set \(K\), split the old image projection and form its endomorphism \(e=\sigma p_K\). Tensoring \(e\) gives the endomorphism \(a\otimes n\mapsto a\otimes e(n)\) of the new word. Stability of \(K\) makes it preserve the new coordinates on \(K\) and kill their projection kernel. It therefore descends to a section, proving projectivity of \(L_{s\mathbf t}(K)\).

The [[node:kl.word.upper_projectivity_step|conditional projectivity step]] now applies to
\[
0\to D\to\ker r\to\ker k\to0,\qquad
0\to\ker r\to L_{s\mathbf t}(U)\to L_{s\mathbf t}(K)\to0.
\]
Both sequences split over their projective targets. This proves projectivity of \(L_{s\mathbf t}(U)\), and completes the word induction. The fixed-word implication in Steps 4–5 then supplies compatible-tuple lifting for every word.

### Step 4. Construct a denominator away from each prime

Let \(z\) be a compatible tuple on \(U\), and let \(p\) be an irreducible polynomial. Group the finitely many word weights by equality of their coefficient characters modulo \(p\). A group contains either one weight, or two weights exchanged by a reflection: a nonzero linear difference divisible by \(p\) forces \(p\) to be a root form, and reflection faithfulness identifies that two-character class.

A single coordinate lifts by stalk surjectivity. A two-coordinate class lifts by the assumed edge compatibility. To combine the class lifts, use diagonal coefficient-action operators separating distinct classes. For a class \(C\), their product gives a diagonal operator \(f\) that vanishes off \(C\) and whose values \(f_c\) on \(C\) are not divisible by \(p\).

Put \(D=\prod_{c\in C}f_c\) and apply the polynomial
\(g(X)=D-\prod_{c\in C}(f_c-X)\) to that operator. Then \(g(0)=0\) and \(g(f_c)=D\) for every \(c\in C\). Thus it multiplies the desired class by a single scalar \(D\), kills the others, and preserves the projected image. Combining the finitely many classes after multiplying their denominators produces \(a z\in L_{\mathbf s}(U)\) with \(p\nmid a\).

### Step 5. Remove every prime factor of a global denominator

The full weight-coordinate construction also supplies a nonzero common denominator \(c\) with \(cz\in L_{\mathbf s}(U)\). Factor \(c\) in the polynomial UFD. Suppose \(c=pc_1\). Choose \(a\) from Step 4, and put \(m=pc_1z\), \(n=az\), both in the projective image \(L\). Then \(am=pc_1n\).

Embed the projective module \(L\) as a direct summand of a free module. Coordinatewise, primality and \(p\nmid a\) imply that every coordinate of \(m\) is divisible by \(p\). Divide those coordinates and project back to \(L\), obtaining \(m=pw\) with \(w\in L\). The ambient stalk product is torsion-free, so cancellation gives \(c_1z=w\in L\). Repeating removes all prime factors. A remaining unit is invertible, and hence \(z\in L\).

### Step 6. Return to the interval sheaf

For a reduced word with top \(b\), stalks outside \([1,b]\) vanish. A section on an interval upper set extends by zero to its ambient upper closure. Pair compatibility across the boundary holds because the outside stalk is zero and the word support is below \(b\).

Steps 4–5 produce a single word-module lift of this tuple. Its stalk projections form a global section and agree with the prescribed values. This is precisely flabbiness of the actual pair-projection sheaf.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.TitsSpace.bottProjectiveUpper`: [IntegralPairings.lean:2109](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2109).

`OAI.KLInvariance.TitsSpace.bottFlabby`: [IntegralPairings.lean:2114](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2114).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_flabby`: [IntegralPairings.lean:2192](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2192).

`OAI.KLInvariance.TitsSpace.bottProjectiveUpper_cons`: [IntegralPairings.lean:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408).
