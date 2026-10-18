# 5. Word objects, duality, and characters

The question is: **how does a sheaf built from modules acquire the polynomial reciprocity needed by the proof?** The difficulty is not merely to write a character. It is to prove an identity for the actual boundary-sheaf character without defining that character to be a KL polynomial.

We proceed in three stages. First construct an explicit tensor module from a word. Next prove its Hecke character formula and perfect duality. Finally use the sheaf decomposition from chapter 4 to isolate the boundary summand.

Write \(C_{x,b}(q)\) for the graded-rank polynomial of the boundary stalk at \(x\) with top \(b\). Write \(P_{x,b}(q)\) for the canonical KL polynomial from chapter 2. They have different definitions.

## 1. One reflection gives a two-term decomposition of the coefficient ring

Use \(A=\mathbb R[\alpha]\), with the simple reflection acting by \(s(\alpha)=-\alpha\). Its invariant subring is \(R=\mathbb R[\alpha^2]\). Every polynomial has a unique even/odd decomposition
\[
f(\alpha)=f_0(\alpha^2)+\alpha f_1(\alpha^2).
\]
Thus \(A=R\oplus\alpha R\) as an \(R\)-module.

Define a trace by extracting the odd coefficient:
\[
\operatorname{tr}(f_0+\alpha f_1)=f_1.
\]
The pairing \((f,g)\mapsto\operatorname{tr}(fg)\) has matrix
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
on the \(R\)-basis \(1,\alpha\): the trace of \(1\) and \(\alpha^2\) is zero, and the trace of \(\alpha\) is one. The matrix is invertible over \(R\), so this pairing is perfect.

“Perfect” means that each linear functional is represented by a unique element through the pairing. Over a ring this is stronger than injectivity: multiplication by \(\alpha\) is injective on \(A\) but cannot represent the functional corresponding to \(1\) by division inside \(A\).

The general reflection Frobenius theorem proves this even/odd decomposition and trace pairing for the actual coefficient ring and reflection.

## 2. Build and evaluate the one-letter word module

For the word consisting of \(s\), tensor induction gives
\[
B_s=A\otimes_R A.
\]
The tensor product identifies \((ar)\otimes b\) with \(a\otimes(rb)\) for \(r\in R\). Since \(A\) has \(R\)-basis \(1,\alpha\), the left \(A\)-module \(B_s\) has basis \(1\otimes1,1\otimes\alpha\).

There are two subexpressions: omit \(s\), giving weight \(1\), or retain it, giving weight \(s\). Their evaluations are
\[
\operatorname{ev}_1(a\otimes b)=ab,\qquad
\operatorname{ev}_s(a\otimes b)=a\,s(b).
\]
These maps are well defined because \(s(r)=r\) for \(r\in R\).

On the two basis vectors, the joint evaluation matrix is
\[
\begin{pmatrix}1&\alpha\\1&-\alpha\end{pmatrix}.
\]
An element with coordinates \(u,v\in A\) maps to
\[
(f,g)=(u+\alpha v,\ u-\alpha v).
\]
If both outputs are zero, adding gives \(2u=0\) and subtracting gives \(2\alpha v=0\); hence \(u=v=0\). This proves injectivity in the example.

Conversely, the image consists exactly of pairs satisfying \(f-g\in\alpha A\). Given such a pair, set \(u=(f+g)/2\) and \(v=(f-g)/(2\alpha)\), both in \(A\). These are precisely the compatible pairs of chapter 4. Thus the tensor calculation produces an actual module of sections.

For a longer word, evaluation has one coordinate for every subexpression. The full-evaluation theorem proves injectivity by repeating the two-block argument. Grouping coordinates of equal group weight defines the stalk images.

## 3. The local properties and the global lifting property are separate

The pair-projection sheaf uses these stalk images. On an edge it remembers whether the two endpoint values come from one common word element. The simultaneous free-stalk/edge-kernel theorem proves that the stalks are free and that the upper restriction kernel is the edge label times the upper stalk.

A global word element gives compatible values on every edge. The converse is subtler: pairwise compatibility of a tuple does not automatically give one common word element. The flabbiness proof establishes the required lifting on upper sets by projective-range and denominator arguments.

This is why the word module, the word sheaf, free stalks, exact edge kernels, and flabbiness have distinct entries. Each assertion supplies a particular hypothesis for the decomposition and duality arguments that follow.

## 4. Derive the word character formula from a short exact sequence

Let \(C_x^{\mathbf t}(q)\) be the stalk character of an old word \(\mathbf t\), and prepend a simple reflection \(s\). If \(x<sx\), the head projection is surjective onto the old stalk at \(x\), with kernel the old stalk at \(sx\) shifted upward by one degree. Degreewise exactness therefore gives
\[
C_x^{s\mathbf t}(q)=C_x^{\mathbf t}(q)+qC_{sx}^{\mathbf t}(q).
\]
If \(sx<x\), the other projection gives
\[
C_x^{s\mathbf t}(q)=C_{sx}^{\mathbf t}(q)+qC_x^{\mathbf t}(q).
\]
The factor \(q\) records the degree-one root multiplication in the kernel; it is not an arbitrary normalization.

These are exactly the coefficient recurrences for multiplication by \(1+T_s\). The empty word has one stalk \(A\) at \(1\), so its character vector is the coefficient vector of \(T_1\). Induction on the word proves
\[
C_x^{\mathbf s}(q)=[T_x](1+T_{s_1})\cdots(1+T_{s_m}).
\]

For the single letter \(s\), the positive Hecke word is \(1+T_s\), and both stalk characters are one. Meanwhile its global section module has basis degrees zero and one, so its graded rank is \(1+q\). Stalk character and global-section character are different quantities.

## 5. Explain the grading reversal in duality

For a homogeneous basis vector \(m\) of degree \(d\), the functional sending \(m\) to \(1\) has degree \(-d\). This explains why duality reverses degrees.

The constructed perfect pairing on a reduced word of length \(m\) sends input degrees \(i,j\) to polynomial degree \(i+j-m\). Support duality then identifies the full outgoing kernel at a vertex \(x\) with a shifted stalk dual. The product of incoming labels accounts for \(\ell(x)\) degrees. Thus a stalk basis degree \(d_i\) becomes a kernel basis degree
\[
m-\ell(x)-d_i.
\]
Since \(m=\ell(b)\) for a reduced word with top \(b\), its character becomes
\[
K_x^{\mathbf s}(q)=q^{\ell(b)-\ell(x)}C_x^{\mathbf s}(q^{-1}).
\]

In our one-edge example, the lower stalk is \(A\), with basis degree zero, and its outgoing kernel is \(\alpha A\), with basis degree one. The formula predicts \(q\cdot1=q\), exactly as calculated directly.

We can also see the duality map itself in this example. Tensor induction gives
\[
\langle a\otimes b,c\otimes d\rangle=ac\,\operatorname{tr}(bd).
\]
In the basis \(1\otimes1,1\otimes\alpha\), the pairing matrix is again
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), now over \(A\).
Write two compatible section pairs as
\((f,g)=(u+\alpha v,u-\alpha v)\) and
\((f',g')=(u'+\alpha v',u'-\alpha v')\). Their pairing is
\[
uv'+vu'=\frac{ff'-gg'}{2\alpha}.
\]
The displayed quotient belongs to \(A\): both pairs agree modulo \(\alpha\), so the numerator is divisible by \(\alpha\).

A section supported only at the lower vertex has the form \((\alpha h,0)\). The stalk functional \(f\mapsto cf\) is represented by the supported section \((2\alpha c,0)\), because
\[
\langle(2\alpha c,0),(f,g)\rangle=cf.
\]
Thus the degree-zero dual generator of the stalk corresponds to a supported generator of degree one. The factor \(2\) is an invertible scalar. This calculation shows concretely how the outgoing kernel is related to a shifted stalk dual; the general support-duality theorem constructs this relation with all incoming labels accounted for.

## 6. Why passing to the boundary summand needs an adjoint

Chapter 4 embeds the normalized boundary sheaf as a split summand of a reduced-word sheaf. Let the inclusion and projection be \(i,p\), with \(pi=1\), and put \(e=ip\). Then \(e^2=e\).

One cannot simply declare the restriction of the word pairing perfect. For example, the perfect bilinear form on \(\mathbb R^2\) with matrix \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) restricts to the zero form on the first coordinate line, even though that line is a direct summand.

Instead the perfect word pairing defines the integral adjoint \(e^*\) by
\[
\langle e^*u,v\rangle=\langle u,ev\rangle.
\]
It pairs the image of \(e^*\) perfectly with the image of \(e\). The formal proof descends the adjoint to sheaf maps, proves primitivity, and identifies its image with the same normalized boundary sheaf. It then proves that the canonical comparison map is an isomorphism. Only after these steps does the induced pairing give the needed perfect boundary duality.

The boundary-pairing entry supplies those maps and checks. Their role is to justify the same stalk–costalk grading calculation for the actual boundary sheaf.

## 7. Show the cancellation that produces boundary reciprocity

Let the word sheaf decompose into shifted boundary models with top vertices \(y\le b\). Write \(m_y(q)\) for the polynomial counting its shifts at center \(y\). One sheaf decomposition gives both identities
\[
C_z^{\mathbf s}=\sum_{y\le b}m_yC_{z,y},\qquad
K_x^{\mathbf s}=\sum_{y\le b}m_yK_{x,y}.
\]
Use zero for \(C_{z,y}\) when \(z\not\le y\).

The word-character formula and Hecke bar identity separately prove
\[
K_x^{\mathbf s}=\sum_{z\le b}R_{x,z}C_z^{\mathbf s}.
\]
Substitute the two decompositions and interchange the finite sums:
\[
\sum_{y\le b}m_y\left(K_{x,y}-\sum_{z\le b}R_{x,z}C_{z,y}\right)=0.
\]
For every \(y<b\), the bracket vanishes by induction on the top length. At \(y=b\), the multiplicity is one: only the top model contributes at \(b\), and the word's top stalk has character one. The equation therefore forces the remaining bracket to vanish.

Replacing \(K_{x,b}\) by its duality expression gives
\[
q^{\ell(b)-\ell(x)}C_{x,b}(q^{-1})
=\sum_{x\le z\le b}R_{x,z}(q)C_{z,b}(q).
\]
This is the identity used later. For \([1,s]\), it reads \(q=1+(q-1)\), so the example checks all three terms.

## 8. Keep the conditional branch separate

The local intersection map gives further information about the pairing. Its strict half-degree theorem has an explicit nonzero-diagonal hypothesis. The equality \(C_{x,b}=P_{x,b}\) is also represented by a separate character-identification condition.

The main argument uses the reciprocity just proved for \(C\). Chapter 9 uses that identity to prove R-invariance, then returns to the independently constructed canonical family \(P\). The two families coincide in the small example, but this does not identify them in general.

If this chapter has become clear, you should be able to say which result supplies each of the three ingredients in the final cancellation: the word convolution, the common multiplicities, and the top multiplicity one.

## Detailed statements and proofs

The calculations above explain the constructions and transitions. The entries below give the exact hypotheses and detailed proofs for the general results.

### Tensor induction and the word sheaf

1. [[node:kl.notes.perfect_pairings]]
2. [[node:kl.notes.reflection_frobenius]]
3. [[node:kl.notes.tensor_pairing]]
4. [[node:kl.notes.bott_samelson]]
5. [[node:kl.detail.word_evaluation_injective]]
6. [[node:kl.notes.word_stalks]]
7. [[node:kl.detail.word_sheaf]]
8. [[node:kl.detail.word_standard_stalks]]
9. [[node:kl.detail.word_characters]]
10. [[node:kl.detail.word_character_formula]]
11. [[node:kl.detail.word_flabbiness]]

### Global duality and costalk grading

1. [[node:kl.notes.supported_pairings]]
2. [[node:kl.detail.section_duality]]
3. [[node:kl.detail.integral_adjoints]]
4. [[node:kl.detail.adjoint_primitivity]]
5. [[node:kl.detail.costalk_duality]]
6. [[node:kl.detail.boundary_pairing]]
7. [[node:kl.detail.costalk_reciprocity]]
8. [[node:kl.duality.stalk_character]]

### Character identities used by the proof

1. [[node:kl.duality.bott_character_decomposition]]
2. [[node:kl.detail.word_character_reciprocity]]
3. [[node:kl.notes.character_cancellation]]
4. [[node:kl.duality.actual_character_reciprocity]]

### Local intersection maps and the conditional character interface

1. [[node:kl.detail.local_intersection]]
2. [[node:kl.detail.local_diagonal_degree]]
3. [[node:kl.duality.character_identity_condition]]
