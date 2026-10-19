---
id: kl.sheaves.word_section_pairing
title: Perfect graded pairings on reduced-word sections
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.word_section_equivalence
- kl.word.pairing_degree
- kl.word.support_duality
- kl.notes.perfect_pairings
- kl.sheaves.pairing_transport
- kl.algebra.component_transport
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSectionDuality
  - OAI.KLInvariance.TitsSpace.bottSectionDuality_apply
  - OAI.KLInvariance.TitsSpace.bottSection_symmetric
  - OAI.KLInvariance.TitsSpace.bottPiece_iff_stalks
  - OAI.KLInvariance.TitsSpace.bottSectionDuality_homogeneous
  - OAI.KLInvariance.TitsSpace.bottSection_left_orthogonal
  - OAI.KLInvariance.TitsSpace.bottSection_right_orthogonal
  - OAI.KLInvariance.TitsSpace.bottWordPerfectPairing
  - OAI.KLInvariance.TitsSpace.bottPolynomialPerfectPairing
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:346
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSectionDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:354
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSectionDuality_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:397
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_symmetric
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:422
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPiece_iff_stalks
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:443
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSectionDuality_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:866
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_left_orthogonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:876
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSection_right_orthogonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:884
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWordPerfectPairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:892
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottPolynomialPerfectPairing
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the actual section duality, degree detection by all stalks, both orthogonality
    arguments and the two PerfectPairing constructors. Proved every field from the
    word pairing and section isomorphism before coefficient transport.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Perfect graded pairings on reduced-word sections

Fix a finite-generator Coxeter system and a reduced word \(\mathbf t\) of length \(m\), with product \(b\). Choose a finite real basis of the extended realization, giving the symmetric coefficient algebra \(A\) its degree-one grading. Let \(S\) be the graded word sheaf on \([1,b]\).

The section isomorphism \(\Psi:M_{\mathbf t}\to\Gamma(S)\) transports the word pairing to a perfect symmetric pairing
\[
\langle s,z\rangle_\Gamma
=\langle\Psi^{-1}s,\Psi^{-1}z\rangle_{M_{\mathbf t}}.
\]
It has degree shift \(m\):
\[
\langle\Gamma(S)_i,\Gamma(S)_j\rangle_\Gamma\subseteq A_{i+j-m}.
\]
If one section is supported at a vertex \(x\) and the other has zero value at \(x\), their pairing is zero, in either argument order.

After choosing polynomial coordinates for \(A\), these properties give the source's bottPolynomialPerfectPairing.

*Proof.*

### Step 1. Transport perfection and symmetry through the section isomorphism

Let \(\lambda:\Gamma(S)\to A\) be linear. The composite \(\lambda\Psi\) is a functional on the word module. Its perfect pairing supplies a unique vector \(v\) with
\[
\langle v,w\rangle_{M_{\mathbf t}}=\lambda(\Psi w)
\]
for every \(w\). Then \(\Psi v\) represents \(\lambda\) for the displayed section pairing.

This also proves uniqueness, since \(\Psi\) is bijective. Symmetry follows from symmetry of the word pairing by substituting the two inverse images. The evaluation formula is exactly
\[
\langle\Psi v,\Psi w\rangle_\Gamma
=\langle v,w\rangle_{M_{\mathbf t}}.
\]

### Step 2. Detect the word degree from all its stalks

A homogeneous word vector of degree \(n\) projects to degree \(n\) in every stalk. Conversely, suppose all stalk projections of \(v\) have degree \(n\). Component transport gives
\[
\pi_x(\operatorname{pr}_n v)
=\operatorname{pr}_n(\pi_xv)=\pi_xv
\]
for every interval vertex \(x\).

The full vertex projection is injective for a reduced word, so
\(\operatorname{pr}_n v=v\). Thus \(v\) has degree \(n\). This proves the source's bottPiece_iff_stalks criterion and shows that \(\Psi^{-1}\) preserves degree.

### Step 3. Compute the pairing degree

For \(s\in\Gamma(S)_i\), \(z\in\Gamma(S)_j\), Step 2 puts their inverse images in word degrees \(i,j\). The [[node:kl.word.pairing_degree|word-pairing degree theorem]] gives
\[
\langle\Psi^{-1}s,\Psi^{-1}z\rangle\in A_{i+j-m}.
\]
This is the required homogeneity.

### Step 4. Prove the two support-orthogonality equations

Suppose \(s\) is supported at \(x\), and \(z_x=0\). Write \(s=\Psi v\), \(z=\Psi w\).

All subexpression weights of the reduced word lie in \([1,b]\). Thus the support of \(s\) says precisely that \(v\) has zero evaluations at every weight different from \(x\); and \(z_x=0\) says \(\pi_x(w)=0\).

[[node:kl.word.support_duality|Word support duality]] identifies vectors supported at \(x\) with the annihilator of \(\ker\pi_x\). Hence \(\langle v,w\rangle=0\). Step 1 gives \(\langle s,z\rangle_\Gamma=0\).

If \(s_x=0\) and \(z\) is supported at \(x\), symmetry exchanges the arguments and gives the other equation.

### Step 5. Package and transport the pairing

Perfection, the degree identity and the two orthogonality equations are the fields of bottWordPerfectPairing. A graded coefficient isomorphism \(A\to P\) transports the section modules and applies that isomorphism to pairing values.

The [[node:kl.sheaves.pairing_transport|pairing-transport theorem]] preserves perfection, the same degree shift, symmetry and support orthogonality. This gives bottPolynomialPerfectPairing on the polynomial word sheaf, with shift \(m\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSectionDuality`: [BalancedPairings.lean:346](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L346).

`OAI.KLInvariance.TitsSpace.bottSectionDuality_apply`: [BalancedPairings.lean:354](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L354).

`OAI.KLInvariance.TitsSpace.bottSection_symmetric`: [BalancedPairings.lean:397](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L397).

`OAI.KLInvariance.TitsSpace.bottPiece_iff_stalks`: [BalancedPairings.lean:422](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L422).

`OAI.KLInvariance.TitsSpace.bottSectionDuality_homogeneous`: [BalancedPairings.lean:443](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L443).

`OAI.KLInvariance.TitsSpace.bottSection_left_orthogonal`: [CharacterReciprocity.lean:866](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L866).

`OAI.KLInvariance.TitsSpace.bottSection_right_orthogonal`: [CharacterReciprocity.lean:876](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L876).

`OAI.KLInvariance.TitsSpace.bottWordPerfectPairing`: [CharacterReciprocity.lean:884](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L884).

`OAI.KLInvariance.TitsSpace.bottPolynomialPerfectPairing`: [CharacterReciprocity.lean:892](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L892).
