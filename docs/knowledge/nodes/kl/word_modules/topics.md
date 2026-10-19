# Reflection Frobenius extensions and word modules

A word in the simple generators determines an iterated tensor module. Each reflection supplies an invariant subalgebra and a trace pairing. Tensor induction combines these elementary pieces into a module with a homogeneous basis, evaluation coordinates indexed by subexpressions, and a character controlled by the Hecke algebra.

The sheaf topic later uses the evaluation images as stalks and the simultaneous two-coordinate images as edge constraints. Here the central constructions are the tensor module, its pairings, and its stalk-character recursion.

## One reflection gives a two-term decomposition of the coefficient ring

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

## The one-letter word module and its evaluations

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

Conversely, the image consists exactly of pairs satisfying \(f-g\in\alpha A\). Given such a pair, set \(u=(f+g)/2\) and \(v=(f-g)/(2\alpha)\), both in \(A\). These are precisely the compatible pairs of moment-graph sheaves. Thus the tensor calculation produces an actual module of sections.

For a longer word, evaluation has one coordinate for every subexpression. The full-evaluation theorem proves injectivity by repeating the two-block argument. Grouping coordinates of equal group weight defines the stalk images.

## The pairing shift and the normalized top

At each tensor step, the reflection trace satisfies
\[
2\alpha_s\operatorname{tr}_s(a)=a-s(a).
\]
The coefficient action preserves degree and \(\alpha_s\) has degree one, so the trace lowers degree by one. On the recursively constructed tensor basis, the pairing formula applies one such trace for every letter. Bilinear expansion then gives
\[
\langle(M_{\mathbf s})_i,(M_{\mathbf s})_j\rangle
\subseteq A_{i+j-|\mathbf s|}.
\]

For a reduced word of length \(m\) and product \(b\), a subexpression with product \(b\) must retain all \(m\) letters: its selected length is at least \(\ell(b)=m\) and at most \(m\). Thus the top-weight coordinate is unique.

The recursively defined all-unit tensor evaluates to \(1\) in every coordinate. Its scalar multiples show that the top coordinate is onto \(A\). The single-coordinate description identifies the top stalk with \(A\) in both grading directions, giving its degree-zero normalization.

This top identification supplies the maps used to split the boundary sheaf into the word sheaf. The pairing shift \(|\mathbf s|=\ell(b)\) then remains unchanged when the canonical boundary pairing is constructed.

## Scaled coordinates and weight support

The evaluation matrix \(E\) is injective over the coefficient domain. Its determinant \(\Delta\) is consequently nonzero. The adjugate identity
\[
E\operatorname{adj}(E)=\Delta I
\]
constructs a word element with evaluations \(\Delta\) in any chosen coordinate and zero elsewhere. For a lift \(c_\varepsilon\) at coordinate \(\varepsilon\), every word element satisfies
\[
\Delta m=\sum_\varepsilon E_\varepsilon(m)c_\varepsilon.
\]
This expresses a scaled word element as a sum of elements supported at individual weights.

The right coefficient action acts on a vector supported at weight \(x\) through the coefficient character \(\chi_x\). Faithfulness separates two distinct characters, and balance of the word pairing forces distinct supported weights to pair to zero.

The scaled expansion then proves that a vector supported at \(x\) annihilates the kernel of the stalk projection. The converse follows by testing the pairing against
\(T_a n-\chi_x(a)n\). Thus the supported submodule is exactly that annihilator, and perfection identifies it with the stalk dual.

This description is the input to adjoint descent in the sheaf topic. A sheaf endomorphism preserves supported coordinates. Symmetry of the word pairing then makes its adjoint preserve every stalk-projection kernel, allowing the adjoint to descend to the stalks and pair-projection edge quotients.

## Twisted coordinates in a two-stalk lattice

A reflection translation compares two stalk projections \(f:N\to X\), \(g:N\to Y\). Its second coordinate carries the twisted action \(r\star y=\tau(r)y\), so the pair action is
\[
r\cdot(x,y)=(rx,\tau(r)y).
\]
The underlying compatible pairs are those with one common preimage in \(N\).

The source supplies two conditions: \(\alpha\mid\tau(r)-r\) for every scalar \(r\), and every pair \((0,\alpha y)\) has a common preimage. If \(n\) represents \((x,y)\), choose \(c\) with \(\tau(r)-r=\alpha c\), and a lift \(m\) of \((0,\alpha cy)\). Then \(rn+m\) represents \((rx,\tau(r)y)\). This proves closure under the twisted action.

In the pair-projection quotient \(Q\), the two coordinates are compared by \(\ell(x)=u(y)\). If \(\alpha Q=0\), the actions of \(\tau(\beta)\) and \(\beta\) agree on \(Q\). When \(\beta\) acts injectively there, compatibility of the multiplied pair implies compatibility of the original pair. This is the saturation step for the twisted lattice.

## The word character formula from a short exact sequence

Let \(C_x^{\mathbf t}(q)\) be the stalk character of an old word \(\mathbf t\), and prepend a simple reflection \(s\). If \(x<sx\), the head projection is surjective onto the old stalk at \(x\), with kernel the old stalk at \(sx\) shifted upward by one degree. Degreewise exactness therefore gives
\[
C_x^{s\mathbf t}(q)=C_x^{\mathbf t}(q)+qC_{sx}^{\mathbf t}(q).
\]
If \(sx<x\), the other projection gives
\[
C_x^{s\mathbf t}(q)=C_{sx}^{\mathbf t}(q)+qC_x^{\mathbf t}(q).
\]
The factor \(q\) records the degree-one root multiplication in the kernel.

These are exactly the coefficient recurrences for multiplication by \(1+T_s\). The empty word has one stalk \(A\) at \(1\), so its character vector is the coefficient vector of \(T_1\). Induction on the word proves
\[
C_x^{\mathbf s}(q)=[T_x](1+T_{s_1})\cdots(1+T_{s_m}).
\]

For the single letter \(s\), the positive Hecke word is \(1+T_s\), and both stalk characters are one. Meanwhile its global section module has basis degrees zero and one, so its graded rank is \(1+q\). Stalk character and global-section character are different quantities.


## Definitions and proofs by construction

### A reflection Frobenius extension

- [[node:kl.notes.reflection_frobenius]]

### Paired modules and tensor induction

- [[node:kl.notes.perfect_pairings]]
- [[node:kl.notes.tensor_pairing]]

### Word modules and homogeneous bases

- [[node:kl.notes.bott_samelson]]
- [[node:kl.word.pairing_degree]]

### Evaluation coordinates and stalk images

- [[node:kl.notes.word_stalks]]
- [[node:kl.detail.word_evaluation_injective]]
- [[node:kl.word.scaled_coordinate_lifts]]
- [[node:kl.word.support_duality]]
- [[node:kl.word.top_stalk]]

### Two-stalk lattices and their kernels

- [[node:kl.detail.word_standard_stalks]]
- [[node:kl.word.twisted_pair_lattice]]
- [[node:kl.word.twisted_lattice_saturation]]

### Word characters

- [[node:kl.detail.word_characters]]
- [[node:kl.detail.word_character_formula]]
