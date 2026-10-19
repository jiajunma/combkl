---
id: kl.word.word_local_lifting
title: Prime denominators for compatible word-stalk tuples
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.finite_stalk_coordinates
- kl.word.prime_character_class
- kl.word.class_lift_assembly
- kl.word.upper_image_properties
- kl.word.scaled_coordinate_lifts
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSet_scaled
  - OAI.KLInvariance.TitsSpace.BottCompatible.reflection_lift
  - OAI.KLInvariance.TitsSpace.BottCompatible.prime_lift
  - OAI.KLInvariance.TitsSpace.BottCompatible.local_denominator
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1950
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSet_scaled
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1968
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottCompatible.reflection_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1982
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottCompatible.prime_lift
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:2029
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottCompatible.local_denominator
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the arbitrary-set scaled lift, reflection orientation split, singleton/pair
    class lift and finite subexpression-index reduction. Preserved compatibility as
    the local-denominator hypothesis and avoided assuming U finite or upper.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Prime denominators for compatible word-stalk tuples

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\), a word \(\mathbf t\), and any weight set \(U\subseteq W\). Let
\(z=(z_x)_{x\in U}\), with \(z_x\in M_{\mathbf t}^x\).

The nonzero evaluation denominator \(\Delta_{\mathbf t}\) satisfies
\[
\Delta_{\mathbf t}z\in L_{\mathbf t}(U)
\]
for every such tuple.

If \(z\) is compatible on all upward reflection edges within \(U\), then for every prime \(p\in A\) there is a scalar \(d\) with
\[
p\nmid d,\qquad dz\in L_{\mathbf t}(U).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit word-image construction of the extension property.**

**OpenAI notes:** The moment-graph sheaf theorem gives extension of compatible sections on upper sets for the normalized boundary sheaf through the cited Braden–MacPherson and Soergel bridges. [bg:bmp](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

**Lean (primary):** The word module gives coordinate images and stable coefficient characters. Reflection geometry makes each prime congruence class a single weight or a reflection pair. Explicit diagonal operators combine class lifts, and prime-denominator removal proves compatible-tuple lifting from image projectivity. The word induction supplies upper-image projectivity using its two kernel sequences. [IntegralPairings:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L470), [IntegralPairings:467](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L467), [IntegralPairings:1299](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1299), [IntegralPairings:1408](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1408), [IntegralPairings:2057](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2057), [IntegralPairings:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620), [IntegralPairings:1833](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1833), [BalancedPairings:292](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L292), [Support:293](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L293).

**Role in the proof:** Upper-image lifting gives interval flabbiness after extension to the ambient upper closure. Full-interval section realization also has a direct free-image proof. Free stalks, root quotients, flabbiness, generation and the normalized word top then supply the graded boundary summand.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Construct a generic scalar lift

For each subexpression \(\varepsilon\), define a scalar
\[
c_\varepsilon=
\begin{cases}
(z_{w(\varepsilon)})_\varepsilon,&w(\varepsilon)\in U,\\
0,&w(\varepsilon)\notin U.
\end{cases}
\]
The [[node:kl.word.scaled_coordinate_lifts|scaled-coordinate theorem]] supplies \(m\in M_{\mathbf t}\) with
\(E_\varepsilon(m)=\Delta_{\mathbf t}c_\varepsilon\) for every \(\varepsilon\).

Fix \(x\in U\). For every subexpression of weight \(x\), this identity gives the corresponding coordinate of
\(\pi_x(m)=\Delta_{\mathbf t}z_x\). Thus the stalk vectors agree, proving
\(p_U(m)=\Delta_{\mathbf t}z\).
The same theorem gives \(\Delta_{\mathbf t}\ne0\).

### Step 2. Lift a reflection pair

Suppose \(x,y\in U\) and \(y=tx\) for a reflection \(t\). Multiplication by a reflection changes the parity of Coxeter length. Indeed, assigning \(-1\) to every simple generator respects the Coxeter relations, which have even length, and defines a sign character. A conjugate of a simple generator has sign \(-1\), while an element of length \(n\) has sign \((-1)^n\). Thus \(\ell(tx)\) and \(\ell(x)\) have opposite parity and are unequal. If \(\ell(x)<\ell(y)\), compatibility gives a word vector with the prescribed pair \((z_x,z_y)\).

If the length inequality is reversed, then \(x=ty\), since \(t^2=1\). Apply compatibility to the upward edge \(y\to x\), and read the two values in the opposite order. This again gives a common lift of \(z_x,z_y\).

### Step 3. Lift an entire prime-character class

Fix \(x\in U\). If its class within \(U\) consists only of \(x\), stalk surjectivity supplies a vector attaining \(z_x\), which realizes that class.

Otherwise choose \(y\ne x\) in its class. The [[node:kl.word.prime_character_class|prime-character theorem]] gives a reflection \(t\) with \(y=tx\), and says that every member of this class is \(x\) or \(y\). Step 2 therefore gives one word vector realizing all prescribed values in the class.

### Step 4. Pass to the finite stalk presentation

Use \(J_U\), the finite set of subexpressions with weight in \(U\). Set
\[
\widehat z_\varepsilon=z_{w(\varepsilon)},\qquad
\widehat\chi_a(\varepsilon)=\chi_{w(\varepsilon)}(a).
\]
The image of \(\widehat p_U\) is stable under these weights.

For a fixed index \(\varepsilon\), Step 3 gives a word vector matching \(z\) at every group weight congruent to \(w(\varepsilon)\) modulo \(p\). Its finite projection therefore matches \(\widehat z\) at every index in the residue class of \(\varepsilon\), including all repeated copies of those weights.

### Step 5. Assemble the class lifts and recover the original tuple

The [[node:kl.word.class_lift_assembly|class-lift assembly theorem]] applies to the finite image
\(\operatorname{im}\widehat p_U\). It produces \(d\) with \(p\nmid d\) and a word vector \(m\) such that
\[
\widehat p_U(m)=d\widehat z.
\]
The finite-presentation recovery argument gives
\(\pi_x(m)=dz_x\) for every \(x\in U\). Hence \(dz\in L_{\mathbf t}(U)\), proving the second assertion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSet_scaled`: [IntegralPairings.lean:1950](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1950).

`OAI.KLInvariance.TitsSpace.BottCompatible.reflection_lift`: [IntegralPairings.lean:1968](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1968).

`OAI.KLInvariance.TitsSpace.BottCompatible.prime_lift`: [IntegralPairings.lean:1982](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1982).

`OAI.KLInvariance.TitsSpace.BottCompatible.local_denominator`: [IntegralPairings.lean:2029](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L2029).
