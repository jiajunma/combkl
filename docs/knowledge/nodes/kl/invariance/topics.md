# Hilbert comparison and combinatorial invariance

The proof turns inclusions of edge images into numerical inequalities, then uses exact endpoints to recover image equality and projective kernels. It first converts each inclusion into an inequality of real numbers. It then forces equality, recovers equality of submodules, and only afterward proves freeness.

We will calculate the whole process for the one-edge sheaf from moment-graph sheaves. The general argument uses the same operations at each edge, with the hypotheses supplied by the simultaneous invariance induction.

## Removing one equation enlarges a kernel by an image

Suppose the remaining outgoing conditions at \(x\) are \(F\cup\{e\}\), where \(e:x\to y\). Set
\[
K'=K_x(F\cup\{e\}),\qquad K=K_x(F),\qquad I_e=\rho_{x,e}(K).
\]
Restrict \(\rho_{x,e}\) to \(K\), with codomain its actual image \(I_e\). This map is surjective by definition. A vector is in its kernel exactly when it satisfies both the old conditions \(F\) and the additional condition \(e\). Thus its kernel is \(K'\), giving
\[
0\longrightarrow K'\longrightarrow K\longrightarrow I_e\longrightarrow0.
\]
All maps preserve degree, so homogeneous dimensions and convergent Hilbert values add:
\[
H_K(q)-H_{K'}(q)=H_{I_e}(q).
\]

In the one-edge example, \(K'=\alpha A\), \(K=A\), and \(I_e=A/(\alpha)\). The identity is
\[
\frac1{1-q}-\frac q{1-q}=1.
\]
This calculation has not used a free basis for an arbitrary partial kernel; the general exactness statement is available before that freeness has been proved.

## Choose a normalization that makes every edge use the same coefficient

Let \(A\) have \(N\) degree-one variables, let \(b\) be the top, and choose \(0<t<1\). Put \(q=t^2\). For the current remaining conditions define the state coordinate
\[
D_x=(1-t^2)^N t^{\ell(x)-\ell(b)}H_{K_x}(t^2).
\]
A state is simply the vector of these real numbers, one for each vertex. The factor \((1-t^2)^N\) removes the usual polynomial-ring denominator. The power of \(t\) adjusts for the vertex's distance from the top.

Why this particular power? localization and edge-image comparison gives \(I_e\subseteq f_eJ_e\), with
\[
k=\deg f_e=\frac{\ell(y)-\ell(x)-1}{2}.
\]
Let \(K_y\) be the required upper kernel, assumed free. Its image is \(J_e\simeq K_y/\alpha_eK_y\). Since the label has degree one and acts injectively, exactness gives
\[
H_{J_e}(q)=(1-q)H_{K_y}(q).
\]
Multiplication by the regular degree-\(k\) factor gives
\[
H_{f_eJ_e}(q)=q^k(1-q)H_{K_y}(q).
\]
Inclusion gives \(H_{I_e}\le H_{f_eJ_e}\). Multiply by the lower state's scale and divide by the upper state's scale. The resulting coefficient is
\[
\begin{aligned}
t^{\ell(x)-\ell(y)}t^{2k}(1-t^2)
&=t^{\ell(x)-\ell(y)+\ell(y)-\ell(x)-1}(1-t^2)\\
&=t^{-1}-t.
\end{aligned}
\]
Thus every edge has the same positive coefficient \(T=t^{-1}-t\), regardless of its length jump.

## Calculate the complete one-edge state

Take \(A=\mathbb R[\alpha]\), \(x=1\), \(y=b=s\), so \(N=1\), \(\ell(x)=0\), \(\ell(y)=1\). Initially the edge condition is still present. The kernels are \(\alpha A\) at \(x\) and \(A\) at \(y\). Their normalized state is
\[
D_{\mathrm{initial}}
=\left((1-t^2)t^{-1}\frac{t^2}{1-t^2},\quad
       (1-t^2)\frac1{1-t^2}\right)
=(t,1).
\]
After removing the edge condition, both kernels are entire stalks:
\[
D_{\mathrm{final}}=(t^{-1},1).
\]
The elementary transfer adds \(T\) times the upper coordinate to the lower one:
\[
U_e(a,b)=(a+Tb,b).
\]
It sends \((t,1)\) to \((t+T,1)=(t^{-1},1)\). At \(t=1/2\), this is
\[
(1/2,1)\longmapsto(2,1),\qquad T=3/2.
\]

The calculation is exact in this example. In the general argument we first have only
\[
D_{\mathrm{next}}\le U_eD_{\mathrm{current}}
\]
coordinatewise. The possible gap measures the failure of the lower image to fill the corrected upper image.

## Follow a list of edges

A schedule is a finite list of edges to process. At each vertex, its remaining conditions are the outgoing edges still in that list. Removing the first edge changes only the kernel at its lower endpoint. A suffix is the final segment of the list left after some initial edges have been removed.

The full list therefore starts with full outgoing kernels at all vertices. The empty list ends with the full stalks. The sequence of intermediate states records every suffix kernel, not merely the endpoints.

Elementary transfers preserve coordinatewise inequalities because \(T>0\). Iterating the one-edge bound yields a bound by the product of transfers. reflection orders and paths identifies that product with the target normalized R-matrix.

For the actual character \(C_{x,b}\), put
\[
c_x(t)=t^{\ell(x)-\ell(b)}C_{x,b}(t^2).
\]
word modules and sheaf duality identifies the endpoint states as \(c(t^{-1})\) and \(c(t)\). Hence the accumulated inequality is
\[
c(t)\le \widetilde R'(t^{-1}-t)c(t^{-1}),
\]
where the prime denotes the target Coxeter system whose order supplied the transported schedule.

## Endpoint equality and vanishing intermediate deficits

Suppose a later argument establishes equality of the two endpoints. Let \(X_j\) be the ideal state obtained by applying transfers exactly, and \(D_j\) the actual state. Initially they agree. Put \(E_j=X_j-D_j\).

At the next step let
\[
\eta_j=U_jD_j-D_{j+1}\ge0.
\]
Then
\[
E_{j+1}=U_jE_j+\eta_j.
\]
Every coordinate of \(E_j\) is nonnegative. A transfer retains those coordinates and adds a nonnegative multiple of one to another. Therefore a positive deficit cannot disappear in a later step. If \(E_{\mathrm{final}}=0\), every \(\eta_j\) must have been zero.

The no-deficit theorem proves the corresponding general statement using monotonicity and injectivity. The displayed calculation explains its mechanism for the actual elementary transfers.

## Equality of numbers recovers equality of submodules

At one step, zero deficit means
\[
H_{I_e}(q)=H_{f_eJ_e}(q)
\]
for the actual homogeneous inclusion \(I_e\subseteq f_eJ_e\). In each degree, the smaller space has dimension at most the larger. If the inclusion were strict, homogeneity would give some degree with a positive quotient dimension. Since \(q^n>0\), that degree would contribute a strictly positive amount to the difference of convergent Hilbert values.

Thus equality of values forces \(I_e=f_eJ_e\). For comparison, the proper inclusion \((\beta,\gamma)\subset\mathbb R[\beta,\gamma]\) from localization and edge-image comparison has Hilbert deficit \(1\), despite equal rank and equal height-one localizations. This is the information the Hilbert step retains.

## Recovering freeness by reversing the schedule

At the end of the forward process, no conditions remain and the kernels are the original free stalks. Traverse the edges backward, adding one condition at a time. Assume the current lower and upper kernels \(M,N\) are free.

Image equality gives surjections
\[
f:M\to I,\qquad g:N\to I
\]
onto the same embedded image. The second map includes the regular correction factor. The upper quotient rule and saturation identify its kernel with \(\alpha N\). Multiplication by \(\alpha\) is injective and identifies \(N\) with \(\ker g\), so this kernel is projective.

Projectivity supplies lifts \(a:M\to N\), \(b:N\to M\) with \(ga=f\), \(fb=g\). The source constructs
\[
i:\ker f\to M\oplus\ker g,\quad i(x)=(x,a(x)),
\]
\[
r:M\oplus\ker g\to\ker f,\quad r(m,k)=m-ba(m)+b(k).
\]
The relation \(fr(m,k)=f(m)-ga(m)+g(k)=0\) verifies the codomain, and \(ri(x)=x\). Thus \(\ker f\) is a direct summand of a projective module and is projective.

The graded projective-to-free theorem applies with the polynomial coefficient ring, finite generation and homogeneous nonnegative pieces. It makes the new kernel free. Repeating the step proves all the suffix kernels free. The [[node:kl.detail.reverse_projectivity|image-equality theorem]] constructs the common-image maps and checks these hypotheses; the [[node:kl.algebra.kernel_projectivity|two-presentation theorem]] gives the explicit retraction.

## Inputs supplied by induction

this topic has proved implications: upper freeness gives comparison, and exact endpoints give new freeness. the simultaneous invariance induction supplies upper freeness from smaller intervals and proves R-matrix equality, which makes the endpoints exact.

The order is therefore essential:
\[
\text{image inclusion}\ \Longrightarrow\ \text{Hilbert inequality}
\ \Longrightarrow\ \text{exact endpoints}
\ \Longrightarrow\ \text{image equality}
\ \Longrightarrow\ \text{projectivity and freeness}.
\]
The middle step comes from the simultaneous induction; it is not available merely from the local inclusion.


## Simultaneous induction on interval rank

The question is: **how do we use a comparison that assumes freeness to prove the freeness needed by later comparisons, without arguing in a circle?** The answer is to prove two assertions together on smaller intervals, then prove KL-invariance in a separate induction.

We compare \([a,b]\) and \([a',b']\) through an order isomorphism \(\phi\). Their common rank is
\[
d=\ell(b)-\ell(a)=\ell(b')-\ell(a').
\]
Coxeter combinatorics proved equality of these rank differences. For now assume that the simple-generator sets are finite, so the real realizations and module constructions are available.

## State all parts of the induction

For each interval isomorphism, prove simultaneously:

1. \(\widetilde R_{a,b}=\widetilde R'_{a',b'}\).
2. Every suffix kernel for the schedule transported by \(\phi\) is free.
3. Every suffix kernel for the schedule transported by \(\phi^{-1}\) is free.

The two freeness assertions matter because we will run the comparison in both directions.

At \(d=0\), each interval has one vertex. The R-polynomial is the diagonal value \(1\). There are no edge conditions, and the relevant kernels are free stalks. This proves all three assertions in the base case.

Now suppose the assertions are known for every smaller rank. The proof must obtain two different kinds of information from that hypothesis.

## Identify the smaller intervals that provide the inputs

If \(z<b\), the initial interval \([a,z]\) has smaller rank. The restriction of \(\phi\) identifies it with \([a',\phi(z)]\). Induction supplies
\[
\widetilde R_{a,z}=\widetilde R'_{a',\phi(z)}.
\]
These are the already-known entries in the bottom matrix row.

At a current edge \(x\to y\), we have \(y>a\). Hence the upper interval \([y,b]\) also has smaller rank. Induction supplies its suffix-kernel freeness, which must be matched with the upper kernel required at that step.

Why does it match? Restriction to \([y,b]\) retains every outgoing edge at \(y\). The transported scores are unchanged. The remaining outgoing edges are exactly the ones past the current score, and hence form the appropriate suffix conditions in the restricted schedule. An outgoing edge at \(y\) cannot have the same reflection label as the incoming edge from \(x\): that reflection sends \(y\) back to \(x\), not upward.

Thus the smaller upper interval supplies exactly the required free module, not just an unrelated free kernel. No new freeness at the current bottom \(a\) has been assumed.

## Cancel a whole matrix comparison down to one unknown entry

Fix \(0<t<1\), and put \(T=t^{-1}-t\). Let \(c(t)\) be the normalized actual boundary-character vector of the source system. It is the same vector in both formulas below.

word modules and sheaf duality gives the exact source identity
\[
c_a(t)=\sum_{a\le z\le b}\widetilde R_{a,z}(T)c_z(t^{-1}).
\]
The upper freeness from Step 2 permits the transported comparison from Hilbert comparison:
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

## Turn two inequalities into polynomial equality

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

## Close the freeness assertions at the same rank

Every proper subinterval already has R-invariance, and Step 4 gives the one new full-interval entry. Thus the entire R-matrices on the two intervals agree. Noncomparable entries vanish in both matrices.

Recall the endpoints of the state process:
\[
D_{\mathrm{initial}}=c(t^{-1}),\qquad
D_{\mathrm{final}}=c(t).
\]
The target transfer product is now the source R-matrix. Actual-character reciprocity therefore makes the product applied to the initial state equal the final state exactly.

Apply Hilbert comparison in its established order. Exact endpoints remove every numerical deficit. Hilbert detection turns the inclusions of images into equalities. Reverse traversal starts at the free stalks and proves all suffix kernels free. Repeat in the inverse direction.

This proves both new freeness assertions after proving the new R-entry. The induction closes because each freeness hypothesis used before Step 4 came from a strictly smaller interval.

## Now begin a separate induction for canonical KL polynomials

The R-stage is complete. We now use the canonical family \(P\), constructed in Hecke algebra and polynomial invariants with its strict degree bound.

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

## Vanishing of the reciprocal difference below the middle degree

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

## Remove the finite-generator restriction

Choose a reduced word for each top endpoint \(b,b'\). Each word uses finitely many simple generators. By the subword criterion, every element of the corresponding lower ideal uses only those generators.

The standard parabolic construction supplies finite-generator Coxeter systems and inclusions into the original groups. Its transport theorem preserves lengths, Bruhat comparisons, and the canonical polynomial values. Hence it gives interval isomorphisms from finite-support models to the original intervals.

Transport \(\phi\) into these models, apply the finite-generator theorem, and transport the polynomial equality back. The groups in the models may still be infinite; it is the generating sets that have become finite.

## Reconstruct the proof without collapsing its two inductions

The first induction proves R-invariance together with freeness in both directions. Its decisive operation is cancelling known R-row entries against one actual-character vector, then using the inverse interval isomorphism.

The second induction compares canonical KL vectors using the common R-matrix. Its decisive operation is eliminating a reciprocal polynomial difference by the strict degree bound.

This is the Lean route. The source-comparison entries explain its relationship to the P-first presentation in the OpenAI notes. Following the separate objects and induction hypotheses is necessary to understand why the argument has no circular freeness assumption.


## Definitions and proofs by construction

### A single edge comparison

- [[node:kl.detail.kernel_exact_sequence]]
- [[node:kl.comparison.normalized_kernel]]
- [[node:kl.comparison.edge_increment]]

### A complete schedule

- [[node:kl.detail.schedule_state]]
- [[node:kl.detail.schedule_comparison]]
- [[node:kl.comparison.global_comparison]]

### Endpoint identities

- [[node:kl.detail.endpoint_equality]]

### Equality and reverse reconstruction of freeness

- [[node:kl.comparison.no_deficit]]
- [[node:kl.detail.reverse_projectivity]]
- [[node:kl.comparison.reverse_freeness]]

### Simultaneous induction for R and suffix kernels

- [[node:kl.comparison.free_suffixes]]
- [[node:kl.comparison.rtilde_row_comparison]]
- [[node:kl.comparison.rtilde_step]]
- [[node:kl.comparison.rtilde_invariance]]

### Canonical KL invariance

- [[node:kl.main.kl_finite]]

### The unrestricted theorem

- [[node:kl.main.combinatorial_invariance]]
