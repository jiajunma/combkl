# 9. Simultaneous induction and combinatorial invariance

The question is: **how do we use a comparison that assumes freeness to prove the freeness needed by later comparisons, without arguing in a circle?** The answer is to prove two assertions together on smaller intervals, then prove KL-invariance in a separate induction.

We compare \([a,b]\) and \([a',b']\) through an order isomorphism \(\phi\). Their common rank is
\[
d=\ell(b)-\ell(a)=\ell(b')-\ell(a').
\]
Chapter 1 proved equality of these rank differences. For now assume that the simple-generator sets are finite, so the real realizations and module constructions are available.

## 1. State all parts of the induction

For each interval isomorphism, prove simultaneously:

1. \(\widetilde R_{a,b}=\widetilde R'_{a',b'}\).
2. Every suffix kernel for the schedule transported by \(\phi\) is free.
3. Every suffix kernel for the schedule transported by \(\phi^{-1}\) is free.

The two freeness assertions matter because we will run the comparison in both directions.

At \(d=0\), each interval has one vertex. The R-polynomial is the diagonal value \(1\). There are no edge conditions, and the relevant kernels are free stalks. This proves all three assertions in the base case.

Now suppose the assertions are known for every smaller rank. The proof must obtain two different kinds of information from that hypothesis.

## 2. Identify the smaller intervals that provide the inputs

If \(z<b\), the initial interval \([a,z]\) has smaller rank. The restriction of \(\phi\) identifies it with \([a',\phi(z)]\). Induction supplies
\[
\widetilde R_{a,z}=\widetilde R'_{a',\phi(z)}.
\]
These are the already-known entries in the bottom matrix row.

At a current edge \(x\to y\), we have \(y>a\). Hence the upper interval \([y,b]\) also has smaller rank. Induction supplies its suffix-kernel freeness, which must be matched with the upper kernel required at that step.

Why does it match? Restriction to \([y,b]\) retains every outgoing edge at \(y\). The transported scores are unchanged. The remaining outgoing edges are exactly the ones past the current score, and hence form the appropriate suffix conditions in the restricted schedule. An outgoing edge at \(y\) cannot have the same reflection label as the incoming edge from \(x\): that reflection sends \(y\) back to \(x\), not upward.

Thus the smaller upper interval supplies exactly the required free module, not just an unrelated free kernel. No new freeness at the current bottom \(a\) has been assumed.

## 3. Cancel a whole matrix comparison down to one unknown entry

Fix \(0<t<1\), and put \(T=t^{-1}-t\). Let \(c(t)\) be the normalized actual boundary-character vector of the source system. It is the same vector in both formulas below.

Chapter 5 gives the exact source identity
\[
c_a(t)=\sum_{a\le z\le b}\widetilde R_{a,z}(T)c_z(t^{-1}).
\]
The upper freeness from Step 2 permits the transported comparison from chapter 8:
\[
c_a(t)\le
\sum_{a\le z\le b}\widetilde R'_{a',\phi(z)}(T)c_z(t^{-1}).
\]
We are applying a target matrix to a source vector. We have not asserted that the source and target sheaf characters are equal.

For every \(z<b\), the two R-entries agree by induction. Let \(S(t)\) denote the sum of all those common terms. The normalized top character is \(c_b(t^{-1})=1\). The two formulas reduce to
\[
S(t)+\widetilde R_{a,b}(T)
\le S(t)+\widetilde R'_{a',b'}(T).
\]
Subtract \(S(t)\), obtaining the desired one-sided inequality for the new entry.

## 4. Turn two inequalities into polynomial equality

Apply the same reasoning to \(\phi^{-1}\), now using the target's own actual-character vector and the reverse freeness hypotheses. It gives
\[
\widetilde R'_{a',b'}(T)\le\widetilde R_{a,b}(T).
\]
Therefore the two evaluations agree for every \(T=t^{-1}-t\), \(0<t<1\).

There are infinitely many such values: if \(0<s<t<1\), then
\[
(s^{-1}-s)-(t^{-1}-t)
=(t-s)\left(\frac1{st}+1\right)>0.
\]
A nonzero polynomial over the reals has only finitely many roots, so the difference polynomial is zero. Injectivity of the integer-to-real coefficient map gives equality of the original integer polynomials.

This R-step does not use the strict half-degree bound of a KL polynomial. That bound enters the later P-step.

## 5. Close the freeness assertions at the same rank

Every proper subinterval already has R-invariance, and Step 4 gives the one new full-interval entry. Thus the entire R-matrices on the two intervals agree. Noncomparable entries vanish in both matrices.

Recall the endpoints of the state process:
\[
D_{\mathrm{initial}}=c(t^{-1}),\qquad
D_{\mathrm{final}}=c(t).
\]
The target transfer product is now the source R-matrix. Actual-character reciprocity therefore makes the product applied to the initial state equal the final state exactly.

Apply chapter 8 in its established order. Exact endpoints remove every numerical deficit. Hilbert detection turns the inclusions of images into equalities. Reverse traversal starts at the free stalks and proves all suffix kernels free. Repeat in the inverse direction.

This proves both new freeness assertions after proving the new R-entry. The induction closes because each freeness hypothesis used before Step 4 came from a strictly smaller interval.

## 6. Now begin a separate induction for canonical KL polynomials

The R-stage is complete. We now use the canonical family \(P\), constructed in chapter 2 with its strict degree bound.

Induct on the interval rank with fixed top endpoints. The diagonal polynomials are both \(1\). For the current lower endpoint \(a\), induction gives equality of
\(P_{z,b}\) and \(P'_{\phi(z),b'}\) whenever \(z>a\).

Define the normalized canonical vectors
\[
k_z(t)=t^{-d(z,b)}P_{z,b}(t^2),\qquad
k'_z(t)=t^{-d(z,b)}P'_{\phi(z),b'}(t^2).
\]
Rank preservation justifies using the same exponent. Both vectors satisfy reciprocity with the now common R-matrix:
\[
k(t)=\widetilde R(T)k(t^{-1}),\qquad
k'(t)=\widetilde R(T)k'(t^{-1}).
\]

Subtract their bottom equations. Every term indexed by \(z>a\) vanishes by induction. The diagonal coefficient at \(a\) is \(1\). Thus, writing
\(\Delta(t)=k_a(t)-k'_a(t)\), we obtain
\[
\Delta(t)=\Delta(t^{-1}).
\]

## 7. See why the degree bound forces the difference to vanish

Put \(p=P_{a,b}-P'_{a',b'}\) and \(d=d(a,b)>0\). Undoing the normalization gives
\[
t^{-d}p(t^2)=t^dp(t^{-2}).
\]
Multiply by \(t^d\) and set \(q=t^2\). Then
\[
p(q)=q^dp(q^{-1})\qquad(0<q<1).
\]

Suppose \(p\ne0\) and let its highest degree be \(m\). Both original polynomials have degree below \(d/2\), so \(m<d/2\). Every exponent in \(p(q)\) is at most \(m\), while every exponent in \(q^dp(q^{-1})\) is at least \(d-m>m\). Their nonzero terms occupy disjoint degree ranges. They cannot be the same polynomial.

The identity on infinitely many \(q\) makes it a polynomial identity, so this contradiction proves \(p=0\). This establishes canonical KL equality in finite-generator systems. It never required identifying an actual sheaf character \(C\) with \(P\).

## 8. Remove the finite-generator restriction

Choose a reduced word for each top endpoint \(b,b'\). Each word uses finitely many simple generators. By the subword criterion, every element of the corresponding lower ideal uses only those generators.

The standard parabolic construction supplies finite-generator Coxeter systems and inclusions into the original groups. Its transport theorem preserves lengths, Bruhat comparisons, and the canonical polynomial values. Hence it gives interval isomorphisms from finite-support models to the original intervals.

Transport \(\phi\) into these models, apply the finite-generator theorem, and transport the polynomial equality back. The groups in the models may still be infinite; it is the generating sets that have become finite.

## 9. Reconstruct the proof without collapsing its two inductions

The first induction proves R-invariance together with freeness in both directions. Its decisive operation is cancelling known R-row entries against one actual-character vector, then using the inverse interval isomorphism.

The second induction compares canonical KL vectors using the common R-matrix. Its decisive operation is eliminating a reciprocal polynomial difference by the strict degree bound.

This is the Lean route. The source-comparison entries explain its relationship to the P-first presentation in the OpenAI notes. Following the separate objects and induction hypotheses is necessary to understand why the argument has no circular freeness assumption.

## Detailed statements and proofs

The calculations above explain the constructions and transitions. The entries below give the exact hypotheses and detailed proofs for the general results.

### The new R entry and exact endpoints

1. [[node:kl.comparison.rtilde_row_comparison]]
2. [[node:kl.comparison.reciprocal_rigidity]]
3. [[node:kl.comparison.rtilde_step]]
4. [[node:kl.detail.endpoint_equality]]

### Closing both induction statements

1. [[node:kl.comparison.rtilde_invariance]]
2. [[node:kl.main.kl_finite]]

### Arbitrary Coxeter systems

1. [[node:kl.main.finite_interval_model]]
2. [[node:kl.main.finite_model_transport]]
3. [[node:kl.main.combinatorial_invariance]]
