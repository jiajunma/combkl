---
id: kl.detail.strong_exchange
title: Strong exchange and deletion from a reduced word
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.coxeter.word_data
- kl.coxeter.word_sign_record
- kl.coxeter.reflection_sign_flip
lean:
  repository: openai-kl
  modules:
  - Coxeter
  declarations:
  - OAI.KLInvariance.CoxeterSupport.strong_exchange
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Coxeter:228
    format: lean-location
    note: OAI.KLInvariance.CoxeterSupport.strong_exchange
  - artifact: openai-kl-paper
    locator: Related paper context; sec:introduction
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- bruhat_order
---

# Strong exchange and deletion from a reduced word

Let \(\omega=(i_1,\ldots,i_n)\) be a reduced word for \(w\) in an arbitrary Coxeter system. Suppose a reflection \(t\) satisfies \(\ell(tw)<\ell(w)\). Then there is a position \(j\) such that
\[
tw=s_{i_1}\cdots\widehat{s_{i_j}}\cdots s_{i_n}.
\]

*Proof.*

### Step 1. Reduce deletion to occurrence in the inversion sequence

Let \(t_j=u_{j-1}s_{i_j}u_{j-1}^{-1}\) be the reflection at position \(j\), where \(u_{j-1}\) is the prefix product. The word-deletion calculation gives
\[
t_jw=s_{i_1}\cdots\widehat{s_{i_j}}\cdots s_{i_n}.
\]
It therefore suffices to prove that \(t\) occurs among these entries.

### Step 2. Evaluate the signed action under the omission assumption

Suppose \(t\) is absent from the inversion sequence of \(\omega\). Its multiplicity is zero, so the word-record theorem gives
\[
A_w(w^{-1}tw,0)=(t,0).
\]
A reflection reverses the sign of its own label. Applying \(A_t\) and using the group-action law gives
\[
A_{tw}(w^{-1}tw,0)=(t,1).
\]

### Step 3. Evaluate the same action using a reduced word for tw

Choose a reduced word \(\nu\) for \(tw\), of length \(m=\ell(tw)\). Since \(t^2=1\),
\[
(tw)^{-1}t(tw)=w^{-1}tw.
\]
The word-record theorem for \(\nu\) therefore evaluates exactly the input in Step 2. Its output bit is the multiplicity of \(t\) in the inversion sequence of \(\nu\), reduced modulo two. That bit is one, so this multiplicity is odd and in particular positive.

### Step 4. Derive the contradictory length inequality

Choose an occurrence of \(t\) in that sequence. The deletion identity for \(\nu\) expresses \(t(tw)=w\) as a product of \(m-1\) simple generators. Thus
\[
\ell(w)\le m-1<m=\ell(tw).
\]
This contradicts the assumed inequality \(\ell(tw)<\ell(w)\). The omission assumption is false.

### Step 5. Delete in the supplied word

There is therefore a position \(j\) in the original word \(\omega\) with \(t=t_j\). Substituting this equality into the deletion identity in Step 1 gives the required product.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CoxeterSupport.strong_exchange`: [Coxeter.lean:228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L228).
