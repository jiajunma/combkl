# 8. Hilbert comparisons and kernel freeness

The question is: **how can an inclusion of edge images eventually prove that all the scheduled kernels are free?** The proof first converts the inclusion into an inequality of real numbers. It then forces equality, recovers equality of submodules, and only afterward proves freeness.

We will calculate the whole process for the one-edge sheaf from chapter 4. The general argument uses the same operations at each edge, with the hypotheses supplied by chapter 9.

## 1. Removing one equation enlarges a kernel by an image

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

## 2. Choose a normalization that makes every edge use the same coefficient

Let \(A\) have \(N\) degree-one variables, let \(b\) be the top, and choose \(0<t<1\). Put \(q=t^2\). For the current remaining conditions define the state coordinate
\[
D_x=(1-t^2)^N t^{\ell(x)-\ell(b)}H_{K_x}(t^2).
\]
A state is simply the vector of these real numbers, one for each vertex. The factor \((1-t^2)^N\) removes the usual polynomial-ring denominator. The power of \(t\) adjusts for the vertex's distance from the top.

Why this particular power? Chapter 7 gives \(I_e\subseteq f_eJ_e\), with
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

## 3. Calculate the complete one-edge state

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

## 4. Follow a list of edges

A schedule is a finite list of edges to process. At each vertex, its remaining conditions are the outgoing edges still in that list. Removing the first edge changes only the kernel at its lower endpoint. A suffix is the final segment of the list left after some initial edges have been removed.

The full list therefore starts with full outgoing kernels at all vertices. The empty list ends with the full stalks. The sequence of intermediate states records every suffix kernel, not merely the endpoints.

Elementary transfers preserve coordinatewise inequalities because \(T>0\). Iterating the one-edge bound yields a bound by the product of transfers. Chapter 6 identifies that product with the target normalized R-matrix.

For the actual character \(C_{x,b}\), put
\[
c_x(t)=t^{\ell(x)-\ell(b)}C_{x,b}(t^2).
\]
Chapter 5 identifies the endpoint states as \(c(t^{-1})\) and \(c(t)\). Hence the accumulated inequality is
\[
c(t)\le \widetilde R'(t^{-1}-t)c(t^{-1}),
\]
where the prime denotes the target Coxeter system whose order supplied the transported schedule.

## 5. Why exact endpoints force all the intermediate gaps to vanish

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

## 6. Equality of numbers recovers equality of submodules

At one step, zero deficit means
\[
H_{I_e}(q)=H_{f_eJ_e}(q)
\]
for the actual homogeneous inclusion \(I_e\subseteq f_eJ_e\). In each degree, the smaller space has dimension at most the larger. If the inclusion were strict, homogeneity would give some degree with a positive quotient dimension. Since \(q^n>0\), that degree would contribute a strictly positive amount to the difference of convergent Hilbert values.

Thus equality of values forces \(I_e=f_eJ_e\). For comparison, the proper inclusion \((\beta,\gamma)\subset\mathbb R[\beta,\gamma]\) from chapter 7 has Hilbert deficit \(1\), despite equal rank and equal height-one localizations. This is the information the Hilbert step retains.

## 7. Recover freeness by reversing the schedule

At the end of the forward process, no conditions remain and all kernels are the original free stalks. Traverse the edges backward, adding one condition at a time. Assume the kernels at the current suffix are free.

Let \(M\) be the current lower kernel and \(N\) the current upper kernel. Image equality supplies two surjections onto the same module \(I\):
\[
f:M\to I,\qquad g:N\to I.
\]
The second map includes the regular correction factor. Its kernel is \(\alpha N\), by the upper quotient rule and saturation. Multiplication by \(\alpha\) identifies \(N\) with \(\alpha N\), so this kernel is free.

We want to prove that \(\ker f\), the lower kernel with the extra condition imposed, is projective. Form
\[
E=\{(m,n)\in M\oplus N:f(m)=g(n)\}.
\]
Projection onto \(M\) is surjective because \(g\) is. Its kernel is \(\ker g\), and the sequence splits since \(M\) is free. Thus \(E\simeq\ker g\oplus M\) is projective. Projection onto \(N\) is also surjective, with kernel \(\ker f\); it splits since \(N\) is free. Therefore \(\ker f\) is a direct summand of the projective module \(E\), hence is projective.

Now apply the graded projective-to-free theorem from chapter 3. This proves freeness after adding the condition. Repeating proves all suffix kernels free.

The common image \(I\) was not assumed projective. The two-presentation construction is why the argument works without that additional assumption.

## 8. What chapter 9 must still supply

This chapter has proved implications: upper freeness gives comparison, and exact endpoints give new freeness. Chapter 9 supplies upper freeness from smaller intervals and proves R-matrix equality, which makes the endpoints exact.

The order is therefore essential:
\[
\text{image inclusion}\ \Longrightarrow\ \text{Hilbert inequality}
\ \Longrightarrow\ \text{exact endpoints}
\ \Longrightarrow\ \text{image equality}
\ \Longrightarrow\ \text{projectivity and freeness}.
\]
The middle step comes from the simultaneous induction; it is not available merely from the local inclusion.

## Detailed statements and proofs

The calculations above explain the constructions and transitions. The entries below give the exact hypotheses and detailed proofs for the general results.

### One-edge algebra and state vectors

1. [[node:kl.detail.kernel_exact_sequence]]
2. [[node:kl.comparison.normalized_kernel]]
3. [[node:kl.detail.schedule_state]]
4. [[node:kl.comparison.positive_transfer]]
5. [[node:kl.detail.transfer_properties]]
6. [[node:kl.comparison.edge_increment]]

### Accumulation and disappearance of deficits

1. [[node:kl.detail.schedule_comparison]]
2. [[node:kl.comparison.global_comparison]]
3. [[node:kl.comparison.no_deficit]]
4. [[node:kl.sheaves.hilbert_detection]]

### Freeness in reverse order

1. [[node:kl.detail.reverse_projectivity]]
2. [[node:kl.comparison.reverse_freeness]]
3. [[node:kl.comparison.free_suffixes]]
