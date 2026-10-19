---
id: kl.dihedral.odd_reflection_edges
title: Odd length detects dihedral reflections and edges
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.coxeter.dihedral_reduced_words
- kl.coxeter.alternating_words
- kl.coxeter.word_data
- kl.foundations.bruhat_step
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - ReflectionSchedules
  declarations:
  - OAI.KLInvariance.Dihedral.alt_odd_sandwich
  - OAI.KLInvariance.Dihedral.odd_alt_reflection
  - OAI.KLInvariance.Dihedral.reflection_iff_odd
  - OAI.KLInvariance.Dihedral.step_iff_odd
  - OAI.KLInvariance.Dihedral.reflection_of_parity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1589
    format: lean-location
    note: OAI.KLInvariance.Dihedral.alt_odd_sandwich
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1599
    format: lean-location
    note: OAI.KLInvariance.Dihedral.odd_alt_reflection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1611
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reflection_iff_odd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.ReflectionSchedules:1621
    format: lean-location
    note: OAI.KLInvariance.Dihedral.step_iff_odd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:228
    format: lean-location
    note: OAI.KLInvariance.Dihedral.reflection_of_parity
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the odd alternating-word conjugation induction and both parity characterizations.
    Kept the two-generator hypothesis, arbitrary finite or infinite group, and the
    direction and strict length condition of BruhatStep.
tags:
- Kazhdan-Lusztig
- interpolation
---

# Odd length detects dihedral reflections and edges

Let \(H\) be a Coxeter system with two simple generators and length \(\ell_H\). Then
\[
w\text{ is a reflection}\quad\Longleftrightarrow\quad \ell_H(w)\text{ is odd}.
\]
Consequently opposite length parities of \(x,y\) imply that \(xy^{-1}\) is a reflection.

Directed reflection edges are characterized by
\[
x\to_H y
\quad\Longleftrightarrow\quad
\ell_H(x)<\ell_H(y)
\ \text{and}\
\ell_H(y)-\ell_H(x)\text{ is odd}.
\]

*Proof.*

### Step 1. A reflection has odd length

Every Coxeter relation changes a word by an even number of letters, so word-length parity gives the sign homomorphism sending each simple generator to \(-1\). Consequently length is additive modulo two, and inversion preserves length.

A reflection has the form \(usu^{-1}\) for a simple generator \(s\). Hence
\[
\ell_H(usu^{-1})
\equiv \ell_H(u)+1+\ell_H(u)
\equiv1\pmod2.
\]

### Step 2. An odd alternating word is a reflection

Let \(\omega_i(n)\) be the alternating word of length \(n\) beginning with generator \(i\). A word of length one is simple, hence a reflection.

For the induction step, the alternating-word identity is
\[
\omega_i(2n+3)
=i\,\omega_{\bar i}(2n+1)\,i.
\]
The middle product is a reflection by induction. Conjugating it by the simple involution \(i\) gives another reflection. Thus every odd alternating word has reflection product.

### Step 3. Apply the reduced alternating expression

Every element of a two-generator Coxeter system has an alternating reduced expression of length \(\ell_H(w)\). If that length is odd, Step 2 makes its product a reflection. Together with Step 1, this proves the equivalence.

### Step 4. Compare two length parities

The parity law gives
\[
\ell_H(xy^{-1})\equiv\ell_H(x)+\ell_H(y)\pmod2.
\]
If \(x,y\) have opposite parities, the right side is odd. Step 3 therefore makes \(xy^{-1}\) a reflection.

### Step 5. Identify the directed edges

If \(x\to_Hy\), then \(y=tx\) for a reflection \(t\), with \(\ell_H(x)<\ell_H(y)\). The identity \(t=yx^{-1}\) and Step 1 imply that the positive length difference is odd.

Conversely, if the length increases by an odd amount, Step 4 makes \(t=yx^{-1}\) a reflection. The equation \(tx=y\) then supplies exactly the required upward reflection step.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.alt_odd_sandwich`: [ReflectionSchedules.lean:1589](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1589).

`OAI.KLInvariance.Dihedral.odd_alt_reflection`: [ReflectionSchedules.lean:1599](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1599).

`OAI.KLInvariance.Dihedral.reflection_iff_odd`: [ReflectionSchedules.lean:1611](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1611).

`OAI.KLInvariance.Dihedral.step_iff_odd`: [ReflectionSchedules.lean:1621](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1621).

`OAI.KLInvariance.Dihedral.reflection_of_parity`: [DihedralIntervals.lean:228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L228).
