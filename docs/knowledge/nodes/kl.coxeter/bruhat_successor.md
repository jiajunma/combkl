---
id: kl.coxeter.bruhat_successor
title: A length-one successor inside every strict Bruhat interval
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses:
- kl.foundations.interval
- kl.detail.bruhat_lifting
- kl.detail.simple_envelopes
- kl.coxeter.word_data
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.exists_bruhat_successor
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:297
    format: lean-location
    note: OAI.KLInvariance.exists_bruhat_successor
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the exact interval, order-map and rank hypotheses retained?
  verdict: Read exists_bruhat_successor. Expanded the upper-length induction, both
    shorter-top cases, lifting obstruction, upper-envelope construction and the equal-length
    contradiction that forces the final ascent.
tags:
- Kazhdan-Lusztig
- Bruhat
- intervals
---

# A length-one successor inside every strict Bruhat interval

If \(x<y\) in Bruhat order, there is \(z\) such that
\[
x<z\le y,\qquad \ell(z)=\ell(x)+1.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit order-theoretic prerequisites.**

**OpenAI notes:** The introduction describes Bruhat intervals as finite graded posets. The comparison induction restricts its isomorphism to smaller upper intervals and uses the equal relative ranks to normalize both vectors. [sec:introduction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1), [sec:induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

**Lean (primary):** Subinterval restriction is constructed on the underlying interval elements. A simple-descent induction gives a length-one successor; rank induction shows that a strictly monotone map cannot decrease rank. Applying it to an isomorphism and its inverse proves rank preservation. [Dihedral:19](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L19), [CanonicalKL:297](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L297), [CanonicalKL:367](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L367), [CanonicalKL:415](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L415).

**Role in the proof:** These lemmas justify both the smaller induction instances and the common powers used when transporting interval-indexed vectors.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Induct on the upper endpoint length

Use strong induction on \(\ell(y)\), with the assertion for every \(x<y\). At upper length zero there is no strict lower element, so the assertion has no instance.

For \(x<y\), the top is not the identity. Choose a simple reflection \(s\) with \(sy<y\), so \(\ell(sy)=\ell(y)-1\). This shorter top is available to the induction hypothesis.

### Step 2. Handle the case x lies below the shorter top

Suppose \(x\le sy\). If \(x=sy\), take \(z=y\); then \(\ell(y)=\ell(x)+1\).

If \(x<sy\), induction gives \(x<z\le sy\) with \(\ell(z)=\ell(x)+1\). Since \(sy\le y\), this same \(z\) has the required properties.

### Step 3. Lower both endpoints in the remaining case

Assume \(x\not\le sy\). If \(s\) were an ascent at \(x\), the [[node:kl.detail.bruhat_lifting|Bruhat lifting property]], applied to \(x\le y\), \(x<sx\), and \(sy<y\), would give \(x\le sy\). Thus \(s\) is a descent at \(x\).

Monotonicity of the lower simple envelope gives \(sx\le sy\). They are distinct: equality would imply \(x=y\) after multiplying by \(s\). Hence \(sx<sy\).

Induction on the shorter top supplies \(w\) with
\[
sx<w\le sy,\qquad
\ell(w)=\ell(sx)+1=\ell(x).
\]

### Step 4. Raise the intermediate element with the upper envelope

Apply monotonicity of the upper simple envelope to \(sx\le w\le sy\). Since \(s\) lowers both original endpoints,
\[
U_s(sx)=x,\qquad U_s(sy)=y.
\]
Therefore
\[
x\le U_s(w)\le y.
\]

If \(s\) lowered \(w\), then \(U_s(w)=w\). We would have \(x\le w\) and \(\ell(x)=\ell(w)\), forcing \(x=w\). Together with \(w\le sy\), this contradicts \(x\not\le sy\).

Thus \(s\) raises \(w\), so \(U_s(w)=sw\) and
\(\ell(sw)=\ell(w)+1=\ell(x)+1\).

### Step 5. Choose the successor

Set \(z=sw=U_s(w)\). Step 4 gives \(x\le z\le y\), and the length equality makes \(x\ne z\), hence \(x<z\).

This completes every induction case. A comparison with length difference one is a cover: an intermediate strict element would have integer length strictly between the two endpoint lengths.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.exists_bruhat_successor`: [CanonicalKL.lean:297](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L297).
