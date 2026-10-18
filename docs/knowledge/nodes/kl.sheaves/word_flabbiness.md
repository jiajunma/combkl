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
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Flabbiness of the actual word sheaf

For a reduced word \(\mathbf s\) with product \(b\), its pair-projection sheaf on \([1,b]\) is flabby. Thus every compatible section on an upper subset extends to a global section.

*Proof.*

### Step 1. Separate the two assertions proved by word induction

For a word \(\mathbf s\) and an upper set \(U\), let \(L_{\mathbf s}(U)\) be the image of the word module in its collection of stalks over \(U\). The induction proves that this image is projective. Once projectivity is available, the argument in Steps 4–6 proves that every pairwise compatible tuple belongs to that image.

For the empty word, only weight \(1\) has a nonzero stalk. The image on \(U\) is either the coefficient ring or zero, hence projective, and compatibility is immediate.

### Step 2. Set up the two-stage projection for a longer word

Write the new word as \(s\mathbf t\). Set \(J=U\cap sU\) and \(K=U\cup sU\). Both are upper, and \(J\) is stable under \(s\), by the simple-reflection lifting property.

The rank-two tensor coordinates give a restriction map
\(r:L_{s\mathbf t}(U)\twoheadrightarrow L_{s\mathbf t}(J)\)
and a first-coordinate map to \(L_{\mathbf t}(U)\). On \(\ker r\), the first-coordinate map surjects onto
\(\ker(L_{\mathbf t}(U)\to L_{\mathbf t}(J))\).
A preimage is obtained by choosing an old word lift \(m\) and using the tensor \(1\otimes m\); its first coordinate is \(m\), and vanishing on the stable set \(J\) makes its new projection vanish there.

The common kernel of restriction and first coordinate is identified by its second coordinate with the scalar twist of
\(\ker(L_{\mathbf t}(K)\to L_{\mathbf t}(U))\).
For the forward map, patch the second-coordinate assignment on \(sU\) with zero on \(U\); they agree on \(J\). The old-word compatibility equations give a compatible assignment on \(K\), so old-word flabbiness lifts it. Conversely a lift vanishing on \(U\), inserted as \(1\otimes m\), produces the required common-kernel vector. The two coordinate maps are injective on these kernels, so these constructions are inverse.

### Step 3. Deduce projectivity through the exact sequences

By induction, \(L_{\mathbf t}(U)\), \(L_{\mathbf t}(J)\), and \(L_{\mathbf t}(K)\) are projective. Their restriction maps are surjective by the definition of projected images, so the two kernels in Step 2 are projective: the exact sequences split over their projective targets.

On the reflection-stable set \(J\), the new image is obtained by the actual rank-two tensor extension of the old image; the old projective splitting extends through this free tensor construction, so \(L_{s\mathbf t}(J)\) is projective.

The exact sequence for the first-coordinate map on \(\ker r\) has projective kernel and projective target, hence splits and makes \(\ker r\) projective. The sequence for \(r\) now also splits, proving \(L_{s\mathbf t}(U)\) projective.

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
