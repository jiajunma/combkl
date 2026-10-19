---
id: kl.notes.dihedral_kl
title: KL polynomials in a dihedral Coxeter system
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.hecke.dihedral_r_sum
- kl.foundations.normalized_kl
- kl.hecke.normalization_unique
- kl.foundations.canonical_kl
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.constantP
  - OAI.KLInvariance.Dihedral.constant_normalizedKL
  - OAI.KLInvariance.Dihedral.klPolynomial_eq_one
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:612
    format: lean-location
    note: OAI.KLInvariance.Dihedral.constantP
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:615
    format: lean-location
    note: OAI.KLInvariance.Dihedral.constant_normalizedKL
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:656
    format: lean-location
    note: OAI.KLInvariance.Dihedral.klPolynomial_eq_one
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; loc:dihedral-kl
    format: section
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read constantP, constant_normalizedKL and klPolynomial_eq_one. Checked
    all seven fields, the actual finite interval sum and the selected-family uniqueness
    step; removed the unrelated root-plane construction from its mathematical prerequisites.
tags:
- Kazhdan-Lusztig
- dihedral
---

# KL polynomials in a dihedral Coxeter system

For a finite or infinite Coxeter system with two simple generators,
\[
P_{x,y}(q)=1\qquad(x\le y).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same conclusion, different final identification.**

**OpenAI notes:** After the lower-interval Hecke sum is shown bar invariant, the proof identifies it by the triangular characterization of the KL basis. [loc:dihedral-kl](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

**Lean (primary):** The same bar calculation is used to derive the sum identity for R-polynomials. Lean then verifies that the constant-on-comparable-pairs P-family satisfies NormalizedKL and applies the proved uniqueness theorem. [Dihedral:557](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L557), [Dihedral:605](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L605), [Dihedral:615](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L615), [Dihedral:656](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L656).

**Role in the proof:** The final steps use the R-sum identity and normalized-family uniqueness to obtain P=1.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Define the candidate P-family

Set
\[
Q_{x,y}=
\begin{cases}
1,&x\le y,\\
0,&x\not\le y.
\end{cases}
\]
Pair it with the constructed ordinary R-family.

The ordinary R construction already supplies the first three normalization fields: diagonal one, zero outside Bruhat order, and the recurrence for every left descent.

### Step 2. Check the diagonal, support and degree fields for Q

Reflexivity gives \(Q_{x,x}=1\). Its value is zero when \(x\not\le y\), by definition.

If \(x<y\), then \(Q_{x,y}=1\), whose natural degree is zero. Strict Bruhat length increase gives \(d(x,y)>0\), so
\[
2\,\operatorname{natDegree}(Q_{x,y})=0<d(x,y).
\]
Thus all three P value/degree fields hold.

### Step 3. Verify reciprocity by the dihedral R-sum

For \(x\le y\), reflection gives
\[
\operatorname{reflect}_{d(x,y)}Q_{x,y}
=\operatorname{reflect}_{d(x,y)}1
=q^{d(x,y)}.
\]
Every \(z\in[x,y]\) satisfies \(z\le y\), so \(Q_{z,y}=1\). Therefore the required interval sum is
\[
\sum_{z\in[x,y]}R_{x,z}Q_{z,y}
=\sum_{z\in[x,y]}R_{x,z}
=q^{d(x,y)},
\]
by the [[node:kl.hecke.dihedral_r_sum|dihedral R-sum theorem]].

The finite interval sum is the same sum used by the normalization interface. This verifies its seventh field.

### Step 4. Identify the candidate by uniqueness

Steps 1–3 prove that \((R,Q)\) is a normalized pair. The [[node:kl.foundations.canonical_kl|canonical-family theorem]] proves that the selected pair is normalized as well.

The [[node:kl.hecke.normalization_unique|normalized-pair uniqueness theorem]] identifies the two pairs. Their P-components agree, so for \(x\le y\),
\[
P_{x,y}=Q_{x,y}=1.
\]

The preceding R-sum proof obtains its identity from the lower-interval Hecke sums and their bar eigenvalue. The OpenAI notes finish the bar calculation through the triangular KL-basis characterization; the Lean proof finishes through the seven polynomial normalization fields and uniqueness.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.constantP`: [Dihedral.lean:612](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L612).

`OAI.KLInvariance.Dihedral.constant_normalizedKL`: [Dihedral.lean:615](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L615).

`OAI.KLInvariance.Dihedral.klPolynomial_eq_one`: [Dihedral.lean:656](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L656).
