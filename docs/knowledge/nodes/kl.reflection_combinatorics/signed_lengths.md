---
id: kl.dihedral.signed_lengths
title: Reduced lengths and existence of signed representatives
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.dihedral.signed_words
- kl.coxeter.dihedral_reduced_words
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  - DyerPaths
  declarations:
  - OAI.KLInvariance.Dihedral.swapHom
  - OAI.KLInvariance.Dihedral.swapHom_involutive
  - OAI.KLInvariance.Dihedral.swap
  - OAI.KLInvariance.Dihedral.swap_wordProd
  - OAI.KLInvariance.Dihedral.length_swap
  - OAI.KLInvariance.Dihedral.swap_alt
  - OAI.KLInvariance.Dihedral.length_alt_le_length
  - OAI.KLInvariance.Dihedral.length_indexWord_nat
  - OAI.KLInvariance.Dihedral.length_indexWord_neg_nat
  - OAI.KLInvariance.Dihedral.length_indexWord
  - OAI.KLInvariance.Dihedral.exists_indexWord
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:958
    format: lean-location
    note: OAI.KLInvariance.Dihedral.swapHom
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:973
    format: lean-location
    note: OAI.KLInvariance.Dihedral.swapHom_involutive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:983
    format: lean-location
    note: OAI.KLInvariance.Dihedral.swap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:996
    format: lean-location
    note: OAI.KLInvariance.Dihedral.swap_wordProd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DyerPaths:1003
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_swap
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:705
    format: lean-location
    note: OAI.KLInvariance.Dihedral.swap_alt
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:709
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_alt_le_length
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:722
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_indexWord_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:727
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_indexWord_neg_nat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:732
    format: lean-location
    note: OAI.KLInvariance.Dihedral.length_indexWord
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:80
    format: lean-location
    note: OAI.KLInvariance.Dihedral.exists_indexWord
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the signed-coordinate, parity, length and finite-period hypotheses explicit?
  verdict: Read the diagram-swap construction, its involution and length inequalities,
    the reduced-prefix proof of length_alt_le_length and all signed-length/existence
    specializations. Preserved the existence of a sufficiently long element as the
    hypothesis for the length equality.
tags:
- Kazhdan-Lusztig
- dihedral-counts
---

# Reduced lengths and existence of signed representatives

Let \(D\) be a Coxeter system with simple generators \(s,t\), length \(\ell\), and signed word values \(w_i\).

If an element \(v\in D\) has \(\ell(v)\ge |i|\), then
\[
\ell(w_i)=|i|.
\]
Every element \(z\in D\) also admits a signed representative \(i\) such that
\[
w_i=z,\qquad |i|=\ell(z).
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**The signed model constructed from word and length identities.**

**OpenAI notes:** The notes index the two alternating rays by positive and negative integers, use -m<i<=m in finite type, and obtain reflection labels as doubled midpoints i+j. The interval-shape lemma gives two vertices in each internal rank and a singleton top. [dih:shape](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L112), [dih:midpoint-order](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/03-dihedral.tex#L358).

**Lean (primary):** indexWord evaluates rotation powers using Euclidean integer division. A diagram automorphism and reduced prefixes prove the length statements. A maximum length gives rotation period 2m, and GoodIndex selects the negative-open, positive-closed range. The internal-rank and signed-sum lemmas retain the zero-rank and singleton-top cases explicitly. [DihedralIntervals:41](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L41), [DihedralIntervals:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709), [DihedralIntervals:90](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L90), [DihedralIntervals:763](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L763), [DihedralIntervals:1378](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1378), [ReflectionSchedules:1639](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1639), [DihedralIntervals:1341](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L1341).

**Role in the proof:** The Blueprint separates integer parameters from their group values, and separates the vertex representative range from the odd reflection-label residues used in finite type.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Exchange the two simple generators

The assignment \(s\mapsto t,\ t\mapsto s\) preserves the Coxeter relations: the two diagonal entries are equal, and the two off-diagonal entries agree by symmetry. It therefore defines the source's homomorphism swapHom.

Applying it twice fixes both generators. Induction on products of generators makes the double application the identity on \(D\). Thus it is an automorphism \(\theta\), called swap.

Applying \(\theta\) to a generator word exchanges its letters without changing the number of letters. A reduced word for \(z\) therefore gives
\(\ell(\theta z)\le\ell(z)\). Applying the same inequality to \(\theta z\), and using \(\theta^2=1\), gives the reverse inequality. Hence
\[
\ell(\theta z)=\ell(z).
\]

### Step 2. Obtain both reduced alternating words of a bounded length

Suppose \(n\le\ell(v)\). Choose a reduced alternating expression for \(v\), beginning with one of the two generators. Its first \(n\) letters form a reduced prefix, so their product has length \(n\).

The automorphism \(\theta\) exchanges this alternating prefix with the one of length \(n\) beginning with the other generator. Step 1 preserves its length. Thus both alternating words of length \(n\) have products of length \(n\).

### Step 3. Apply this to a signed index

The [[node:kl.dihedral.signed_words|signed-word definition]] identifies \(w_n\) and \(w_{-n}\) with these two alternating products. Therefore both have length \(n\) whenever an element of length at least \(n\) exists.

For an arbitrary integer \(i\), take \(n=|i|\). The index is \(n\) or \(-n\), and the displayed length equality follows.

### Step 4. Represent an arbitrary group element

Choose a reduced alternating expression for \(z\). Its number of letters is \(\ell(z)\).

If it begins with \(s\), take \(i=\ell(z)\); if it begins with \(t\), take \(i=-\ell(z)\). The positive and negative [[node:kl.dihedral.signed_words|signed-word identities]] give \(w_i=z\), and in both cases \(|i|=\ell(z)\). The identity element is represented by \(i=0\).

This proves the length and existence statements used when the later count is expressed in integer coordinates.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.swapHom`: [DyerPaths.lean:958](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L958).

`OAI.KLInvariance.Dihedral.swapHom_involutive`: [DyerPaths.lean:973](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L973).

`OAI.KLInvariance.Dihedral.swap`: [DyerPaths.lean:983](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L983).

`OAI.KLInvariance.Dihedral.swap_wordProd`: [DyerPaths.lean:996](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L996).

`OAI.KLInvariance.Dihedral.length_swap`: [DyerPaths.lean:1003](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1003).

`OAI.KLInvariance.Dihedral.swap_alt`: [DihedralIntervals.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L705).

`OAI.KLInvariance.Dihedral.length_alt_le_length`: [DihedralIntervals.lean:709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L709).

`OAI.KLInvariance.Dihedral.length_indexWord_nat`: [DihedralIntervals.lean:722](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L722).

`OAI.KLInvariance.Dihedral.length_indexWord_neg_nat`: [DihedralIntervals.lean:727](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L727).

`OAI.KLInvariance.Dihedral.length_indexWord`: [DihedralIntervals.lean:732](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L732).

`OAI.KLInvariance.Dihedral.exists_indexWord`: [DihedralIntervals.lean:80](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L80).
