---
id: kl.detail.root_inversion_count
title: The root-sign criterion and the inversion count
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.root_inversions
- kl.detail.root_reflection_correspondence
- kl.detail.strong_exchange
- kl.coxeter.word_sign_record
- kl.coxeter.signed_reflection_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.Represents.inversion_iff
  - OAI.KLInvariance.TitsSpace.rootInversions_finite
  - OAI.KLInvariance.TitsSpace.card_rootInversions
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1928
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.inversion_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2065
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootInversions_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2073
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.card_rootInversions
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# The root-sign criterion and the inversion count

If a positive root \(a\) represents \(t\), then
\[
w^{-1}a\in-\Phi^+\quad\Longleftrightarrow\quad\ell(tw)<\ell(w).
\]
Consequently \(\operatorname{Inv}_{\Phi}(w)\) is finite with cardinality \(\ell(w)\).

*Proof.*

### Step 1. Record sign changes along a word

A simple reflection changes only the coordinate along its own simple root. If it sent a positive root to a negative root, every other coordinate would therefore be zero. The original root would be a positive scalar multiple of that simple root; their squared norms are both two, so the scalar would be one. Hence it sends every positive root except its own simple root to a positive root, and sends that simple root to its negative. The same assertion for negative roots follows by negating. Thus a root represented by a pair \((t,\varepsilon)\), with sign bit \(\varepsilon\in\mathbb Z/2\mathbb Z\), transforms under \(s_i\) by conjugating \(t\) and toggling the sign precisely when \(t=s_i\).

The formal signed action implements these two operations. Iterating along a word therefore tracks the actual sign of the root, not just a formal label.

### Step 2. Use the reduced-word inversion record

Choose a reduced word \(\omega\) for \(w\). Iterating the preceding sign rule gives
\[
w^{-1}\cdot(t,0)=(w^{-1}tw,\ c_t),\qquad
c_t=\#\{t\text{ in the left inversion sequence of }\omega\}\pmod2.
\]
Reducedness makes that sequence repetition-free. Hence \(c_t=1\) exactly when \(t\) occurs, and otherwise \(c_t=0\). The signed action then says that \(w^{-1}a\) is negative exactly when \(t\) occurs. A nonzero real root cannot be both positive and negative, so these alternatives are exclusive.

The strong-exchange inversion description identifies membership in this sequence with \(\ell(tw)<\ell(w)\). This proves the displayed sign criterion with the left-multiplication convention.

### Step 3. Count by explicit bijections

Restrict the positive-root/reflection bijection to the two inversion sets; Step 2 shows that both maps land in the required subsets. Next identify left inversions with the elements of the reduced-word inversion sequence. Since the sequence has no repetitions, taking its \(j\)-th entry is a bijection from its positions to its members.

There is one inversion-sequence entry for each letter of \(\omega\). Its number of positions is therefore \(|\omega|=\ell(w)\). Composing these three bijections proves finiteness and the cardinality assertion. No finiteness of the ambient group or of the entire positive root set was used.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.Represents.inversion_iff`: [Tits.lean:1928](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1928).

`OAI.KLInvariance.TitsSpace.rootInversions_finite`: [Tits.lean:2065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2065).

`OAI.KLInvariance.TitsSpace.card_rootInversions`: [Tits.lean:2073](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2073).
