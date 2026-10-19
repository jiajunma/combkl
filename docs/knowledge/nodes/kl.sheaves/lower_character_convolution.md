---
id: kl.duality.lower_character_convolution
title: Lower-character normalization and convolution on an ambient interval
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.duality.stalk_character
- kl.sheaves.lower_model_kernels
- kl.detail.ordinary_r
- kl.hecke.polynomial_reflection
- kl.algebra.character_basis_independence
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.Graded.ModuleData.unitPolynomialBasis
  - OAI.KLInvariance.Graded.ModuleData.char_unit
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_top
  - OAI.KLInvariance.BruhatGraph.lowerCharacter_diagonal
  - OAI.KLInvariance.BruhatGraph.lowerCharacter_at_top
  - OAI.KLInvariance.BruhatGraph.lowerIntervalEquiv
  - OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution
  - OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution_zero
  - OAI.KLInvariance.BruhatGraph.lowerCharacter_reciprocity_lift
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2055
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.unitPolynomialBasis
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2068
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.char_unit
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2091
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_top
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2099
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter_diagonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2103
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter_at_top
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2134
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerIntervalEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2140
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2166
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution_zero
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:2174
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.lowerCharacter_reciprocity_lift
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the unit character and both lower-character normalizations, the explicit
    lower-interval bijection, support filtering and both cases of lowerCharacter_reciprocity_lift.
    Kept the fixed ambient coefficient basis and truncated rank difference.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Lower-character normalization and convolution on an ambient interval

Fix a finite-generator Coxeter system and its polynomial coefficient algebra from one fixed real basis. Let \(I_b=[1,b]\), and let \(C_{x,c}\) denote the character of the actual boundary-sheaf stalk at \(x\) on \([1,c]\). For \(c\in I_b\), define the lower-character function
\[
L_x^c(q)=
\begin{cases}
C_{x,c}(q),&x\le c,\\
0,&x\not\le c.
\end{cases}
\]
Then \(L_c^c=1\), and \(L_b^c=1\) for \(c=b\) and \(0\) otherwise.

For every \(x\in I_b\),
\[
\sum_{z\in I_b}R_{x,z}L_z^c
=\sum_{z\in[1,c]}R_{x,z}C_{z,c}.
\]
If \(x\not\le c\), this sum is zero.

Consequently, reciprocity for the boundary sheaf on \([1,c]\) implies
\[
\operatorname{reflect}_{\delta(x,c)}L_x^c
=\sum_{z\in I_b}R_{x,z}L_z^c
\qquad(x\in I_b),
\]
where \(\delta(x,c)=\max\{\ell(c)-\ell(x),0\}\) is the natural-number rank difference.

*Proof.*

### Step 1. Normalize the top character

The normalized boundary top is the unit coefficient module, with one homogeneous basis vector in degree zero. Its character is \(q^0=1\). In the source, unitPolynomialBasis records that singleton basis, and char_unit computes its character.

Transport through the boundary's graded top identification gives \(C_{c,c}=1\), hence \(L_c^c=1\).

If \(c=b\), this gives \(L_b^c=1\). If \(c\ne b\), the two inequalities \(c\le b\) and \(b\le c\) would force equality. Thus \(b\not\le c\), and the support definition gives \(L_b^c=0\).

### Step 2. Remove terms outside the smaller lower interval

Whenever \(z\not\le c\), the factor \(L_z^c\) is zero. Therefore
\[
\sum_{z\in I_b}R_{x,z}L_z^c
=\sum_{z\in I_b,\ z\le c}R_{x,z}L_z^c.
\]

The source's lowerIntervalEquiv identifies \(\{z\in I_b:z\le c\}\) with \([1,c]\) by keeping the underlying group element. Its inverse uses transitivity \(z\le c\le b\) to regard that same element as a vertex of \(I_b\).

On this subset, \(L_z^c=C_{z,c}\). Reindexing by the bijection gives the displayed convolution identity. All characters use the same ambient coefficient algebra and basis.

### Step 3. Prove vanishing outside the lower center’s support

Assume \(x\not\le c\). For any \(z\in I_b\), if \(z\not\le c\), then \(L_z^c=0\).

If \(z\le c\), the inequality \(x\le z\) would imply \(x\le c\), a contradiction. The triangular support of the R-family therefore gives \(R_{x,z}=0\).

Thus every summand is zero, proving the vanishing claim.

### Step 4. Lift a smaller reciprocity identity

Assume reciprocity holds at every vertex of \([1,c]\). If \(x\le c\), apply it to that vertex:
\[
\operatorname{reflect}_{\ell(c)-\ell(x)}C_{x,c}
=\sum_{z\in[1,c]}R_{x,z}C_{z,c}.
\]
Use Step 2 and the definition of \(L_x^c\) to obtain the ambient formula.

If \(x\not\le c\), the lower character is zero, and polynomial reflection sends zero to zero. The right side is zero by Step 3. Hence the same formula holds for all \(x\in I_b\), including the incomparable case.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.ModuleData.unitPolynomialBasis`: [CharacterReciprocity.lean:2055](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2055).

`OAI.KLInvariance.Graded.ModuleData.char_unit`: [CharacterReciprocity.lean:2068](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2068).

`OAI.KLInvariance.BruhatGraph.stalkCharacter_top`: [CharacterReciprocity.lean:2091](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2091).

`OAI.KLInvariance.BruhatGraph.lowerCharacter_diagonal`: [CharacterReciprocity.lean:2099](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2099).

`OAI.KLInvariance.BruhatGraph.lowerCharacter_at_top`: [CharacterReciprocity.lean:2103](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2103).

`OAI.KLInvariance.BruhatGraph.lowerIntervalEquiv`: [CharacterReciprocity.lean:2134](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2134).

`OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution`: [CharacterReciprocity.lean:2140](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2140).

`OAI.KLInvariance.BruhatGraph.lowerCharacter_convolution_zero`: [CharacterReciprocity.lean:2166](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2166).

`OAI.KLInvariance.BruhatGraph.lowerCharacter_reciprocity_lift`: [CharacterReciprocity.lean:2174](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L2174).
