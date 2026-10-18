# Hecke algebra and polynomial invariants

The question is: **what are the polynomials whose invariance we are trying to prove, and why are there two R-families as well as a KL family?** We build them algebraically before introducing sheaves.

Keep three notational distinctions in view. A group element \(s\) satisfies \(s^2=1\). Its unnormalized Hecke basis element \(T_s\) satisfies a different quadratic relation. The letter \(T\) without a subscript will later be a scalar variable in a normalized R-polynomial.

## A Hecke operator is determined by what it does to basis vectors

Start with the free module having one basis vector \(T_w\) for each group element \(w\). Finite linear combinations of these vectors form the underlying Hecke module. Left multiplication by \(T_s\) is specified by
\[
T_sT_w=
\begin{cases}
T_{sw},&\ell(sw)>\ell(w),\\
qT_{sw}+(q-1)T_w,&\ell(sw)<\ell(w).
\end{cases}
\]
The formulas on basis vectors determine a linear operator on every finite combination.

Set \(w=s\). Since \(ss=1\), the second branch gives
\[
T_s^2=qT_1+(q-1)T_s.
\]
Here \(T_1\) acts as the identity. If \(q\) is invertible, solve this equation for the inverse:
\[
T_s\bigl(T_s-(q-1)\bigr)=q,\qquad
T_s^{-1}=q^{-1}\bigl(T_s-(q-1)\bigr).
\]
This computation is the reason the quadratic relation enters the bar construction.

The source also uses a normalized basis \(H_w\). Its simple operator has matrix
\[
\begin{pmatrix}0&1\\1&a\end{pmatrix}
\]
on \(H_1,H_s\), with \(a=v-v^{-1}\). The normalization determines this matrix. The operator and quadratic-relation entries give the conversion to the unnormalized generators.

The overview [[node:kl.notes.hecke_action]] develops the operators, their quadratic relation, and the bar involution.

## How the bar map produces R-polynomials

The bar operation reverses the parameter and replaces simple Hecke generators by their inverses. The inverse formula above makes this concrete: applying bar to a basis vector generally produces a linear combination of several basis vectors.

The R-polynomials record the coefficients of this change of basis, with the stated normalization. They are therefore constructed using the Coxeter and Hecke structure. Their definition does not yet make them invariants of an unlabelled interval.

The descent recurrence lets us compute the ordinary family \(R_{x,y}(q)\). Choose a simple reflection \(s\) with \(sy<y\). If \(sx<x\), replace both endpoints by \(sx,sy\). If \(sx>x\), the recurrence is
\[
R_{x,y}=(q-1)R_{x,sy}+qR_{sx,sy}.
\]
The upper endpoint becomes shorter in both terms, so this is a terminating recursion. Diagonal entries are one and entries outside Bruhat order are zero.

For \([1,s]\), this gives
\[
R_{1,s}=(q-1)R_{1,1}+qR_{s,1}
=(q-1)\cdot1+q\cdot0=q-1.
\]

Applying bar twice gives the identity map. At the level of coefficient matrices, this says that the appropriately reflected R-matrix is inverse to the original R-matrix. The reciprocal convolution theorem makes that matrix statement precise. It is the compatibility needed for the KL construction below.

## How reciprocity and a degree restriction determine P

The KL polynomial \(P_{x,y}(q)\) satisfies \(P_{x,x}=1\), vanishes outside Bruhat order, and obeys
\[
q^{d}P_{x,y}(q^{-1})
=\sum_{x\le z\le y}R_{x,z}(q)P_{z,y}(q),
\qquad d=\ell(y)-\ell(x).
\]
When \(x<y\), its degree must be strictly less than \(d/2\).

To see what must be constructed, isolate the term \(z=x\). Since \(R_{x,x}=1\), the equation becomes
\[
q^dP_{x,y}(q^{-1})-P_{x,y}(q)
=\sum_{x<z\le y}R_{x,z}(q)P_{z,y}(q).
\]
Every polynomial on the right involves a smaller upper interval. It is already available in the recursion. Thus the unknown polynomial occurs only on the left.

For a polynomial of degree below \(d/2\), its original coefficients occupy the low degrees, whereas its reflected coefficients occupy the high degrees. Reading the low-degree part of the right-hand side therefore determines the unknown coefficients. The lower-half construction carries this out; the R-kernel identity proves that the remaining high-degree equations are consistent. The uniqueness theorem then shows that no second polynomial with the same degree bound can solve the equation.

The detailed defect entry fixes the sign used by the implementation when naming this right-hand-side data.

## Work through the two-element interval

For \(x=1,y=s\), we have \(d=1\), so \(P_{1,s}\) must be a constant \(c\). The two terms of reciprocity are
\[
qc=R_{1,1}P_{1,s}+R_{1,s}P_{s,s}
=c+(q-1).
\]
Rearranging gives \((q-1)c=q-1\), hence \(c=1\).

This example already shows the roles of the ingredients. The R-recursion supplies \(q-1\); the degree bound reduces the unknown to a constant; reciprocity fixes that constant. In larger intervals the same mechanism determines several low-degree coefficients.

## Why change parameters again?

The normalized family is characterized by
\[
R_{x,y}(v^2)=v^{d(x,y)}\widetilde R_{x,y}(v-v^{-1}).
\]
For our interval, \(\widetilde R_{1,s}(T)=T\), because \(v(v-v^{-1})=v^2-1\).

Later the comparison uses a real number \(0<t<1\), sets \(q=t^2\), and uses the positive scalar
\[
T=t^{-1}-t.
\]
This has the opposite sign to \(t-t^{-1}\) in the displayed normalization identity. The positive transfer formula comes from the reciprocal, scaled identity; it is not obtained by replacing those two signs indiscriminately.

For a fixed top \(b\), put
\[
p_x(t)=t^{-d(x,b)}P_{x,b}(t^2).
\]
Scaled reciprocity reads
\[
p_x(t)=\sum_{x\le z\le b}\widetilde R_{x,z}(t^{-1}-t)\,p_z(t^{-1}).
\]
For \([1,s]\), \(p_1(t)=t^{-1}\) and \(p_s(t)=1\). The equation becomes
\[
t^{-1}=t+(t^{-1}-t)\cdot1.
\]
This is exactly the one-edge transfer that will reappear in Hilbert comparison.

## Outputs for the geometric comparison

We have constructed the canonical polynomials and proved their identities. reflection orders and paths will identify normalized R-polynomials with ordered path sums. the simultaneous invariance induction will prove their invariance first, then compare two canonical KL families using the common R-matrix and the strict degree bound.

The actual sheaf character introduced in word modules and sheaf duality is a further construction, denoted \(C\). It is not defined to equal \(P\). Remembering this distinction is essential to following the verified proof route.


## Definitions and proofs by construction

### Hecke modules and operators

- [[node:kl.definitions.hecke_operators]]
- [[node:kl.definitions.hecke_quadratic_relation]]
- [[node:kl.detail.hecke_quadratic_identity]]
- [[node:kl.notes.hecke_action]]

### The bar operation

- [[node:kl.definitions.bar_involution]]

### The R-polynomial families

- [[node:kl.detail.ordinary_r]]
- [[node:kl.detail.rtilde_family]]
- [[node:kl.detail.r_kernel]]
- [[node:kl.detail.rtilde_recursion]]
- [[node:kl.foundations.rtilde]]

### Canonical KL polynomials

- [[node:kl.foundations.normalized_kl]]
- [[node:kl.foundations.low_half]]
- [[node:kl.detail.kl_defect]]
- [[node:kl.detail.kl_recursion]]
- [[node:kl.foundations.canonical_kl]]

### Word expansions and rigidity

- [[node:kl.foundations.scaled_kl]]
- [[node:kl.comparison.reciprocal_rigidity]]
- [[node:kl.notes.dihedral_kl]]
