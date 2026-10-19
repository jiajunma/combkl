---
id: kl.coxeter.simple_edge_transport
title: Simple multiplication and the orientation of reflection edges
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.bruhat_step
- kl.detail.strong_exchange
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - Bruhat
  declarations:
  - OAI.KLInvariance.bruhatStep_simple_mul
  - OAI.KLInvariance.bruhatStep_inv
  - OAI.KLInvariance.bruhatStep_mul_simple
  - OAI.KLInvariance.right_descent_simple_mul_iff
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:262
    format: lean-location
    note: OAI.KLInvariance.bruhatStep_simple_mul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:463
    format: lean-location
    note: OAI.KLInvariance.bruhatStep_inv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:470
    format: lean-location
    note: OAI.KLInvariance.bruhatStep_mul_simple
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Bruhat:504
    format: lean-location
    note: OAI.KLInvariance.right_descent_simple_mul_iff
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

# Simple multiplication and the orientation of reflection edges

Let \(x\to y\) be an upward reflection edge and \(s\) a simple generator. If \(y\ne sx\), then
\[
sx\longrightarrow sy
\]
is an upward reflection edge.

The corresponding right-multiplication statement holds when \(y\ne xs\). Consequently, for simple generators \(s,t\) and \(sx\ne xt\),
\[
\ell(sxt)<\ell(sx)
\quad\Longleftrightarrow\quad
\ell(xt)<\ell(x).
\]

*Proof.*

### Step 1. The transported reflection label

Write \(y=rx\) with \(r\) a reflection. Then \(sy=(srs)(sx)\). Conjugation makes \(srs\) another reflection, so it remains to prove \(\ell(sx)<\ell(sy)\).

### Step 2. The ascent case at y

Suppose \(\ell(sy)=\ell(y)+1\). Simple multiplication changes length by one, so
\[
\ell(sx)\le\ell(x)+1\le\ell(y)<\ell(sy).
\]
This gives the required orientation.

### Step 3. The descent case at y

Suppose \(\ell(sy)=\ell(y)-1\). Choose a reduced word \(\nu\) for \(sy\); then \(s\nu\) is reduced with product \(y\).

The reflection \(r\) sends \(y\) down to \(x\). Strong exchange deletes a position in \(s\nu\) and gives product \(x\). If it deleted the first position, then \(x=sy\), contrary to \(y\ne sx\). It therefore deletes a position inside \(\nu\).

Write the remaining tail as \(\nu'\). Then \(x=s\,\operatorname{prod}(\nu')\), so \(sx=\operatorname{prod}(\nu')\). Its expression has \(|\nu|-1\) letters. Hence
\[
\ell(sx)\le|\nu|-1<|\nu|=\ell(sy).
\]
This proves the left-multiplication statement.

### Step 4. Inversion and right multiplication

An edge \(y=rx\) becomes
\[
y^{-1}=(x^{-1}rx)x^{-1}.
\]
The new multiplier is a reflection, and inversion preserves length, so \(x^{-1}\to y^{-1}\) is upward.

Apply the left-multiplication statement to this inverse edge and then invert again. The result is \(xs\to ys\) whenever \(y\ne xs\).

### Step 5. The descent square

The two elements \(x,xt\) differ by left multiplication by the reflection \(xtx^{-1}\), since \((xtx^{-1})x=xt\) and \((xtx^{-1})(xt)=x\).

Suppose first that \(\ell(xt)<\ell(x)\). Then \(xt\to x\) is an upward reflection edge. The condition \(sx\ne xt\) is equivalent to \(x\ne sxt\), so left multiplication by \(s\) gives \(sxt\to sx\). Hence \(\ell(sxt)<\ell(sx)\).

If instead \(\ell(x)<\ell(xt)\), apply left multiplication to \(x\to xt\). The hypothesis is precisely \(xt\ne sx\), and the result is \(sx\to sxt\). Thus the left inequality fails.

These are the two possible simple-length cases, proving the equivalence.

## References

The local word and parabolic calculations are listed below.

## Lean formalization

`OAI.KLInvariance.bruhatStep_simple_mul`: [Bruhat.lean:262](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L262).

`OAI.KLInvariance.bruhatStep_inv`: [Bruhat.lean:463](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L463).

`OAI.KLInvariance.bruhatStep_mul_simple`: [Bruhat.lean:470](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L470).

`OAI.KLInvariance.right_descent_simple_mul_iff`: [Bruhat.lean:504](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean#L504).
