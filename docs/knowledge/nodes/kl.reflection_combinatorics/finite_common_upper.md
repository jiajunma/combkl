---
id: kl.dihedral.finite_common_upper
title: Finite sets in a dihedral group have a common Bruhat upper bound
kind: theorem
status: proved
primary_topic: kl.reflection_combinatorics
topics:
- kl.reflection_combinatorics
uses:
- kl.foundations.bruhat_order
- kl.detail.simple_envelopes
- kl.detail.bruhat_lifting
- kl.coxeter.dihedral_bruhat_order
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.bruhat_top_of_all_descents
  - OAI.KLInvariance.Dihedral.exists_common_upper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:644
    format: lean-location
    note: OAI.KLInvariance.bruhat_top_of_all_descents
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:667
    format: lean-location
    note: OAI.KLInvariance.Dihedral.exists_common_upper
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read bruhat_top_of_all_descents and both branches of exists_common_upper.
    Expanded the word induction with the exact upper-envelope inequality, the bounded
    natural-length maximum, the unbounded finite-set length bound, and the empty-set
    case.
tags:
- Kazhdan-Lusztig
- local-model-transport
---

# Finite sets in a dihedral group have a common Bruhat upper bound

Let \(H\) be a two-generator Coxeter system, with length \(\ell\) and strong Bruhat order. For every finite subset \(F\subseteq H\), there is an element \(d\in H\) such that
\[
x\le d\qquad\text{for every }x\in F.
\]
The common upper bound need not belong to \(F\).

The proof uses a general Coxeter fact: if every simple reflection is a left descent of \(w\), then every group element lies below \(w\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Finite-interval construction of the relative models.**

**OpenAI notes:** After the relative-flabbiness lemma, the notes restrict the localized model from the full coset to its finite relative lower ideal. They extend a section by zero outside the model support inside an upward closure, then use model flabbiness. Flat localization preserves the finite-support section conditions. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125), [loc:relative-flabbiness](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L226).

**Lean (primary):** The finite relative ideal is embedded in a principal dihedral interval using a common upper bound. Explicit scalar-extension and pullback isomorphisms identify the structure models. The outgoing-lift theorem is applied to edges whose targets lie below the chosen model center; canonical positive-root equality identifies the actual labels. [MinimalExtensions:1295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1295), [DihedralIntervals:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L667), [PlaneLocalization:637](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L637), [PlaneLocalization:724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L724), [PlaneLocalization:761](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L761).

**Role in the proof:** The Blueprint follows the finite-interval construction and verifies the support, outgoing lifts, scalar maps and label equality before assembling the local-model fields.
<!-- source-comparison:end -->

## Application to finite relative lower ideals

For a finite relative coset vertex set \(K\), apply the theorem to its underlying elements of the induced dihedral group. The resulting \(d\) gives
\[
K\subseteq[1,d]_H.
\]
The inclusion preserves and reflects the intrinsic order because both use the same Bruhat relation on the same underlying elements. This is the interval used in the [[node:kl.local.coset_structure_models|coset-model transport proof]].

*Proof.*

### Step 1. Prove the general all-descents assertion by word induction

Assume \(\ell(sw)<\ell(w)\) for every simple reflection \(s\). We prove that the product of every simple-generator word lies below \(w\), by induction on the word.

The empty product is \(1\), and \(1\le w\).

Suppose the shorter word has product \(z\le w\), and prepend \(s\). Let \(U_s\) be the upper simple envelope. Its monotonicity and pair-constancy give
\[
sz\le U_s(sz)=U_s(z)\le U_s(w)=w.
\]
The last equality uses the descent hypothesis at \(w\). This proves the induction step.

Every Coxeter-group element is the product of a simple-generator word, so every element is below \(w\).

### Step 2. Handle bounded length

Suppose the set of lengths \(\{\ell(x):x\in H\}\subseteq\mathbb N\) is bounded. It is nonempty and finite, so it has a maximum. Choose \(d\) attaining that maximum.

For either simple reflection \(s\), maximality gives \(\ell(sd)\le\ell(d)\). Simple multiplication changes length by exactly one, so equality cannot occur. Hence \(\ell(sd)<\ell(d)\).

Both generators are descents. Step 1 gives \(x\le d\) for every \(x\in H\), and therefore for every \(x\in F\).

### Step 3. Handle unbounded length

Suppose lengths are unbounded. Let
\[
N=\max\bigl(\{0\}\cup\{\ell(x):x\in F\}\bigr).
\]
Choose \(d\) with \(\ell(d)>N\). Then every \(x\in F\) satisfies \(\ell(x)<\ell(d)\).

The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat comparison theorem]] states that in a two-generator system every element of strictly smaller length lies below the longer element. Applying it to \(x,d\) gives \(x\le d\).

These two cases prove the assertion, including the empty finite set.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.bruhat_top_of_all_descents`: [DihedralIntervals.lean:644](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L644).

`OAI.KLInvariance.Dihedral.exists_common_upper`: [DihedralIntervals.lean:667](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L667).
