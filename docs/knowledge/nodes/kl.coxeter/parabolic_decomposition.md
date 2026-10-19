---
id: kl.coxeter.parabolic_decomposition
title: Length-additive decomposition by a parabolic subgroup
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.parabolic_subgroups
- kl.coxeter.word_reduction
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.ParabolicSupport.reduced_append_of_minimal
  - OAI.KLInvariance.ParabolicSupport.length_mul_of_minimal
  - OAI.KLInvariance.ParabolicSupport.minimal_simple_ascent
  - OAI.KLInvariance.ParabolicSupport.exists_length_additive_decomposition
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:675
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.reduced_append_of_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:705
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.length_mul_of_minimal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:727
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.minimal_simple_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:735
    format: lean-location
    note: OAI.KLInvariance.ParabolicSupport.exists_length_additive_decomposition
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the word, coset, and length hypotheses explicit?
  verdict: Checked arbitrary generator subsets, the right-multiplication coset convention,
    the alternating-word endpoint convention, and the exact noncollapsed-edge condition.
tags:
- Kazhdan-Lusztig
- Coxeter
---

# Length-additive decomposition by a parabolic subgroup

Let \(J\) be a set of simple-generator indices. If \(u\) is minimal in \(uW_J\), then for every \(v\in W_J\),
\[
\ell(uv)=\ell(u)+\ell(v).
\]
Moreover, a reduced word for \(u\) followed by a reduced \(J\)-word for \(v\) is reduced.

Every \(w\in W\) consequently has a decomposition \(w=uv\), with \(v\in W_J\), such that
\[
\ell(w)=\ell(u)+\ell(v),
\]
and, for every \(i\in J\),
\[
\ell(us_i)=\ell(u)+1,\qquad
\ell(ws_i)=\ell(u)+\ell(vs_i).
\]

*Proof.*

### Step 1. Reduce the concatenation

Choose a reduced word \(\omega\) for \(u\) and a reduced \(J\)-word \(\nu\) for \(v\). The preceding definition entry proves the existence of the latter.

Apply word reduction to \(\omega\nu\). A subword of this concatenation splits as \(\omega'\nu'\), where \(\omega'\) is a subword of \(\omega\) and \(\nu'\) is a subword of \(\nu\). Choose such a split whose concatenation is reduced and has product \(uv\).

Write \(p=\operatorname{prod}(\omega')\), \(q=\operatorname{prod}(\nu')\). Then \(pq=uv\), and \(q\in W_J\).

### Step 2. Minimality forces the first subword to be unchanged

Rearranging gives
\[
p=u(vq^{-1}).
\]
Since \(vq^{-1}\in W_J\), minimality gives \(\ell(u)\le\ell(p)\). On the other hand,
\[
\ell(p)\le|\omega'|\le|\omega|=\ell(u).
\]
All these inequalities are therefore equalities. In particular, \(|\omega'|=|\omega|\). A subword of the same length has deleted no positions, so \(\omega'=\omega\) and \(p=u\).

### Step 3. Reducedness forces the second subword to be unchanged

Now \(pq=uv\) becomes \(uq=uv\), so \(q=v\). Since \(\nu\) is reduced,
\[
|\nu|=\ell(v)=\ell(q)\le|\nu'|\le|\nu|.
\]
Again all inequalities are equalities, and \(\nu'=\nu\).

The reduced word \(\omega'\nu'\) from Step 1 is therefore the whole concatenation \(\omega\nu\). Its length is
\[
\ell(uv)=|\omega|+|\nu|=\ell(u)+\ell(v).
\]

### Step 4. Choose the decomposition of an arbitrary element

Choose a minimal \(u\) in \(wW_J\), and write \(w=uv\) with \(v\in W_J\). Steps 1–3 give the required length equality.

For \(i\in J\), apply length additivity first to \(s_i\in W_J\), obtaining \(\ell(us_i)=\ell(u)+1\). Apply it next to \(vs_i\in W_J\). Since \(ws_i=u(vs_i)\), this gives
\[
\ell(ws_i)=\ell(u)+\ell(vs_i).
\]
These are the identities used by the root-sign induction.

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.ParabolicSupport.reduced_append_of_minimal`: [Tits.lean:675](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L675).

`OAI.KLInvariance.ParabolicSupport.length_mul_of_minimal`: [Tits.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L705).

`OAI.KLInvariance.ParabolicSupport.minimal_simple_ascent`: [Tits.lean:727](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L727).

`OAI.KLInvariance.ParabolicSupport.exists_length_additive_decomposition`: [Tits.lean:735](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L735).
