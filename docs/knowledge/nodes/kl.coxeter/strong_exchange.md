---
id: kl.detail.strong_exchange
title: Strong exchange and deletion from a reduced word
kind: theorem
status: proved
primary_topic: kl.coxeter
topics:
- kl.coxeter
uses: []
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

Let \(w=s_1\cdots s_n\) be a supplied reduced expression in an arbitrary Coxeter system. If a reflection \(t\) is a left inversion of \(w\), meaning \(\ell(tw)<\ell(w)\), then some position \(j\) satisfies
\[
tw=s_1\cdots\widehat{s_j}\cdots s_n.
\]
The deletion takes place in this particular reduced expression; the assertion is not merely that some shorter expression exists.

*Proof.*

### Step 1. Record the reflection attached to each position

For a word \(\omega=(s_1,\ldots,s_n)\), let \(w=s_1\cdots s_n\) and
\[
t_j=s_1\cdots s_{j-1}s_j s_{j-1}\cdots s_1.
\]
Direct cancellation gives
\(t_jw=s_1\cdots\widehat{s_j}\cdots s_n\).
Thus it is enough to show that the given left inversion \(t\) occurs among the \(t_j\).

### Step 2. Build the signed action used to detect occurrence

Let a simple reflection \(s\) act on a pair \((r,\varepsilon)\), with \(\varepsilon\in\mathbb Z/2\mathbb Z\), by
\[
(r,\varepsilon)\longmapsto(srs,\ \varepsilon+\mathbf1_{r=s}).
\]
Applying this twice returns the original pair: conjugation by \(s\) squares to the identity, and the same sign change occurs twice.

The Coxeter relation \((s_is_j)^{m_{ij}}=1\) also acts trivially. Its alternating word has inversion list
\(s_i(s_js_i)^k\), \(0\le k<2m_{ij}\).
The relation \((s_js_i)^{m_{ij}}=1\) makes the second half of this list identical to the first. Every reflection is therefore counted an even number of times, so the sign change is zero. The first coordinate is conjugation by the identity. Thus the presentation gives a well-defined action \(A_w\) for every \(w\in W\).

### Step 3. Compute the sign recorded by a word

Multiplying the simple actions one at a time gives
\[
A_w(w^{-1}rw,\varepsilon)
=(r,\varepsilon+\#\{j:t_j=r\}\bmod2).
\]
For the empty word this is immediate. Appending a simple generator adds exactly its conjugate by the preceding prefix to the inversion list, and the simple-action formula adds exactly the corresponding sign indicator. This proves the formula by induction.

A reflection \(t=usu^{-1}\) changes the sign of its own label:
\(A_t(t,\varepsilon)=(t,\varepsilon+1)\).
To see this, first apply \(A_{u^{-1}}\), obtaining label \(s\) with some sign translation; \(A_s\) changes that sign once; applying \(A_u\) cancels the two conjugating sign translations.

### Step 4. Rule out omission of the given inversion

Suppose \(t\) does not occur in the inversion list of \(\omega\). Step 3 then gives
\(A_w(w^{-1}tw,0)=(t,0)\).
Choose a reduced word \(\nu\) for \(tw\). The group action satisfies \(A_{tw}=A_tA_w\), and \(t^2=1\) gives
\((tw)^{-1}t(tw)=w^{-1}tw\).
Hence the same input is sent by \(A_{tw}\) to \((t,1)\).

By the word-record formula for \(\nu\), the inversion list of \(\nu\) contains \(t\) an odd number of times, in particular at least once. Deleting such a position gives an expression for \(t(tw)=w\) with fewer letters than the reduced word \(\nu\). Therefore
\(\ell(w)<\ell(tw)\), contradicting the hypothesis \(\ell(tw)<\ell(w)\).

### Step 5. Perform the required deletion

Thus \(t=t_j\) for some position \(j\) in the originally supplied word. The cancellation identity in Step 1 gives the required expression with that position deleted. The deleted word need not be reduced; the theorem asserts its product.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/01-introduction.tex#L1).

## Lean formalization



`OAI.KLInvariance.CoxeterSupport.strong_exchange`: [Coxeter.lean:228](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean#L228).
