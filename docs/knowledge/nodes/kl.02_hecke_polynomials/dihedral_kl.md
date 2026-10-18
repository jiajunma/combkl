---
id: kl.notes.dihedral_kl
title: KL polynomials in a dihedral Coxeter system
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.notes.hecke_action
- kl.foundations.canonical_kl
- kl.notes.relative_dihedral_intervals
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.klPolynomial_eq_one
source:
  spans:
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
  prompt: Are the source hypotheses retained?
  verdict: The statement and proof follow the fixed formal development and its paper
    counterpart.
tags:
- Kazhdan-Lusztig
- localization
---

# KL polynomials in a dihedral Coxeter system

In a finite or infinite dihedral Coxeter system \(D\),
\[
P^D_{x,w}(q)=1\qquad(x\le_D w).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same conclusion, different final identification.**

**OpenAI notes:** After the lower-interval Hecke sum is shown bar invariant, the proof identifies it by the triangular characterization of the KL basis. [loc:dihedral-kl](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

**Lean (primary):** The same bar calculation is used to derive the sum identity for R-polynomials. Lean then verifies that the constant-on-comparable-pairs P-family satisfies NormalizedKL and applies the proved uniqueness theorem. [Dihedral:557](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L557), [Dihedral:605](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L605), [Dihedral:615](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L615), [Dihedral:656](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L656).

**Role in the proof:** The final steps use the R-sum identity and normalized-family uniqueness to obtain P=1.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Compute the lower-interval Hecke sums

Put \(S_w=\sum_{z\le w}T_z\) in the unnormalized Hecke basis. Let a reduced alternating word for \(w\) begin with \(s\), and let \(v=sw\) have length \(n-1\).

Partition the lower ideal of \(v\) into left \(s\)-strings \(\{r,sr\}\), with \(\ell(sr)=\ell(r)+1\). If only \(r\) is present, then
\((1+T_s)T_r=T_r+T_{sr}\).
If both are present, the quadratic relation \(T_s^2=(q-1)T_s+q\) gives
\[
(1+T_s)(T_r+T_{sr})=(1+q)(T_r+T_{sr}).
\]
The alternating-word interval description shows that the strings reached are exactly those below \(w\). The doubly counted part is empty for \(n=2\), and for \(n>2\) is the lower ideal of the alternating prefix \(p\) of length \(n-2\). Therefore
\((1+T_s)S_v=S_w+qS_p\), with the last term omitted for \(n=2\).

### Step 2. Prove the bar identity by induction on n

For \(n=0\), the sum is \(1\); for \(n=1\), it is \(1+T_s\), and
\(1+T_s^{-1}=q^{-1}(1+T_s)\).
Assume the bar identities for the shorter alternating words. Apply bar to the relation in Step 1 and use this generator identity:
\[
q^{-1}(1+T_s)\,q^{-(n-1)}S_v
=\overline S_w+q^{-1}q^{-(n-2)}S_p.
\]
Substitute the original relation for \((1+T_s)S_v\). The two correction terms have the same scalar \(q^{-(n-1)}\), so they cancel, leaving
\(\overline S_w=q^{-n}S_w\).
This is Lean's unnormalized form of the bar calculation.

### Step 3. Extract the R-sum identity

Apply the bar identity with inverted unit parameter and read the coefficient at \(x\le y\). The coefficient definition of the ordinary R-values and the powers of the unit parameter give
\[
\sum_{x\le z\le y}R_{x,z}(q)=q^{d(x,y)}.
\]
In Lean this is first obtained over the Laurent polynomial ring, where the parameter is a unit. Every R-value is the image of its integral polynomial, so injectivity of polynomial-to-Laurent inclusion yields the displayed polynomial identity.

### Step 4. Verify the constant P-family directly

Define \(Q_{x,y}=1\) for \(x\le y\), and zero otherwise. Its diagonal and zero conditions are immediate. For \(x<y\), it has degree zero and \(d(x,y)>0\), so \(2\deg Q_{x,y}=0<d(x,y)\).

Its reciprocity equation is exactly
\[
\operatorname{reflect}_{d(x,y)}1=q^{d(x,y)}
=\sum_{x\le z\le y}R_{x,z}Q_{z,y},
\]
by Step 3. Thus \((R,Q)\) satisfies every normalized-KL condition.

### Step 5. Apply the proved uniqueness theorem

The selected canonical family satisfies those same conditions. Uniqueness identifies its P-component with \(Q\), hence \(P_{x,y}=1\) for \(x\le y\).

The preprint finishes its bar calculation through the triangular characterization of the KL basis. Lean instead verifies the constant polynomial family's normalization and uses the previously proved uniqueness theorem. The conclusion is the same, but the last proof step is different.

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

## Lean formalization

The implementation establishes the dihedral Hecke calculation and identifies its polynomial family with the already constructed ordinary KL family.

`OAI.KLInvariance.Dihedral.klPolynomial_eq_one`: [Dihedral.lean:656](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L656).
