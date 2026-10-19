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

“Perfect” means that each linear functional has a unique representative through the pairing. In this example, a functional \(f:A\to R\) is represented by \(f(\alpha)+\alpha f(1)\). Its products with \(1\) and \(\alpha\) have traces \(f(1)\) and \(f(\alpha)\), which determine \(f\) on the whole basis.

The general [[node:kl.word.reflection_coordinates|reflection coordinate theorem]] obtains the decomposition from four hypotheses: the automorphism \(\tau\) is an involution, \(\alpha\ne0\), \(\tau(\alpha)=-\alpha\), and every \(a-\tau(a)\) is divisible by \(\alpha\). Applying \(\tau\) to \(a-\tau(a)=\alpha d\) and cancelling \(\alpha\) proves that \(d\) is invariant. The coordinates are then
\[
a_0=\frac{a+\tau(a)}2,\qquad a_1=\frac d2.
\]
Uniqueness follows by applying \(\tau\) to two candidate expansions and cancelling \(2\alpha\). This gives the basis \(1,\alpha\) over the fixed subalgebra.

Let \(V\) be the real extended realization, \(B\) its bilinear form, \(r_s\) a simple root, and \(\iota:V\to A=\operatorname{Sym}_{\mathbb R}(V)\) the generator map. The extended simple reflection is \(v\mapsto v-B(r_s,v)r_s\), with \(B(r_s,r_s)=2\). It induces the algebra action on vector generators. The difference of a generator and its reflection is a multiple of \(\alpha_s=\iota(r_s)\); addition and multiplication preserve that divisibility. This verifies the hypotheses and constructs the simple-reflection Frobenius data used by every word step.

## Restricting the pairing and extending the module

Suppose the old module \(N\) is finite free over \(A\), with a perfect \(A\)-valued pairing \(B_N\). Prepending a reflection first regards \(N\) as a module over \(R=A^s\). The trace then gives the \(R\)-valued pairing
\[
b_R(m,n)=t_s(B_N(m,n)).
\]
To prove it perfect, start with an arbitrary \(R\)-linear functional \(f:N\to R\). At each \(m\), the map \(a\mapsto f(am)\) is a functional on \(A\). Trace duality represents it by a unique element \(c_f(m)\) satisfying
\[
t_s(c_f(m)a)=f(am).
\]
Testing this equation against arbitrary scalars proves that \(m\mapsto c_f(m)\) is \(A\)-linear. The original perfect pairing represents that functional by a vector of \(N\). This vector represents \(f\) for the restricted pairing \(b_R\).

The next operation extends scalars to \(A\otimes_R N\). Since \(N\) is finite free over \(A\), and \(A\) has the two-element \(R\)-basis, the vectors \(n_j,\alpha_s n_j\) form a finite \(R\)-basis. The dual base-change isomorphism now extends \(b_R\) to the perfect pairing
\[
B'(a\otimes m,b\otimes n)=ab\,t_s(B_N(m,n)).
\]
A right coefficient action acts on the second tensor factor. Its commutation with the old left action makes it well defined. If the old pairing is balanced for that action and is symmetric, the formula for \(B'\) proves those identities for the induced pairing. These constructions explain every field of the induced paired bimodule.

## The one-letter word module and its evaluations

For the word consisting of \(s\), tensor induction gives
\[
B_s=A\otimes_R A.
\]
The tensor product identifies \((ar)\otimes b\) with \(a\otimes(rb)\) for \(r\in R\). Since \(A\) has \(R\)-basis \(1,\alpha\), the left \(A\)-module \(B_s\) has basis \(1\otimes1,1\otimes\alpha\).

Start the induction with \(N=A\) and multiplication pairing. On \(u=1\otimes1\) and \(v=1\otimes\alpha\), the induced pairing gives
\[
B'(u,u)=B'(v,v)=0,\qquad B'(u,v)=B'(v,u)=1.
\]
Thus \(B'(au+bv,cu+dv)=ad+bc\). This pairing and the evaluations below are two constructions on the same tensor module: one represents linear functionals, while the other records its values at subexpressions.

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

## Recursive evaluations and their homogeneous images

For a longer word, write \(E_\eta\) for a tail evaluation and \(\tau=\chi_s\) for the prepended reflection. The two new evaluations are
\[
E_{(0,\eta)}(a\otimes m)=aE_\eta(m),\qquad
E_{(1,\eta)}(a\otimes m)=a\tau(E_\eta(m)).
\]
The outer coefficient stays in place. Reflection of the tail evaluation is linear over \(A^s\), because \(\tau\) fixes this subalgebra; that is what makes the second formula respect the tensor relation.

Rows of the evaluation matrix record subexpressions, and columns record basis vectors. Prepending \(s\) changes a tail matrix \(E\) into
\[
\begin{pmatrix}E&\alpha_sE\\ \tau(E)&-\alpha_s\tau(E)\end{pmatrix}.
\]
Applying the inverse automorphism to a matrix equation proves that \(\tau(E)\) is injective whenever \(E\) is. The two block equations then recover \(v_0+\alpha_s v_1\) and \(v_0-\alpha_s v_1\); cancellation of \(2\alpha_s\) recovers \(v_1\), followed by \(v_0\). Starting with the matrix \((1)\) proves full word-evaluation injectivity.

A column indexed by a basis vector of degree \(d\) has entries in \(A_d\). This follows from the same blocks: \(\tau\) preserves degree, and multiplication by \(\alpha_s\) adds one. Consequently evaluations preserve degree. Given any lift of a homogeneous stalk vector, taking its component of the required degree gives a homogeneous lift.

For a reduced word with product \(b\), the [[node:kl.foundations.subword|reduced-subword criterion]] identifies its weights with the whole interval \([1,b]\). A weight outside this interval has no coordinates and has zero stalk. Every weight inside it occurs, and the unit tensor has a coordinate equal to \(1\), so its stalk is nonzero.

## The pairing shift and the normalized top

At each tensor step, the reflection trace satisfies
\[
2\alpha_s\operatorname{tr}_s(a)=a-s(a).
\]
The coefficient action preserves degree and \(\alpha_s\) has degree one, so the trace lowers degree by one. The [[node:kl.word.induced_pairing_degree|one-step basis-pairing theorem]] gives the precise induction: if the old pairing of basis vectors of degrees \(d_j,d_k\) lies in \(A_{d_j+d_k-L}\), the new vectors \(1\otimes\alpha_s^\varepsilon b_j\) have assigned degrees \(\varepsilon+d_j\), and their pairing lies in degree
\[
(\varepsilon+d_j)+(\delta+d_k)-(L+1).
\]
Starting at shift zero for the empty word, each letter therefore increases the shift by one. Bilinear expansion then gives
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

## Reflection labels and the first-factor map

For two word stalk projections \(f:M\to X\), \(g:M\to Y\), the edge module is the quotient \(Q=(X\oplus Y)/\operatorname{im}(f,g)\). If an endomorphism \(T\) acts through scalars \(a,b\) on the two projections, then \(a-b\) kills \(Q\). For a lift \(n\) of \(x\in X\), the vector \(Tn-bn\) has projections \(((a-b)x,0)\), whose quotient class is zero.

For weights \(x,tx\) and reflection-root label \(\beta\), take right multiplication by \(p=\chi_x^{-1}(\beta/2)\). Its two scalars are \(\beta/2\) and \(-\beta/2\). Thus \(\beta Q=0\), which also provides a common lift of every pair \((0,\beta y)\).

When the word begins with the simple reflection \(s\), its first-factor reflection is
\[
F_s(a\otimes m)=\tau(a)\otimes m.
\]
It is semilinear over \(A\) and linear over \(A^s\). The relation \(a-\tau(a)\in\alpha_sA\) gives \(v-F_s(v)\in\alpha_sM_{s\mathbf t}\). Exchanging the first subexpression bit changes weight \(x\) to \(sx\), and
\[
E_e(F_s(v))=\tau(E_{\sigma(e)}(v)).
\]
Thus \(\pi_x(v)=0\) implies \(\pi_{sx}(F_s(v))=0\). Projecting the divisible difference gives
\(\pi_{sx}(v)\in\alpha_sM_{s\mathbf t}^{sx}\).
Together with label annihilation, this proves that the upper edge-map kernel is exactly \(\alpha_sM_{s\mathbf t}^{sx}\).

## Twisted coordinates in a two-stalk lattice

A reflection translation compares two stalk projections \(f:N\to X\), \(g:N\to Y\). Its second coordinate carries the twisted action \(r\star y=\tau(r)y\), so the pair action is
\[
r\cdot(x,y)=(rx,\tau(r)y).
\]
The underlying compatible pairs are those with one common preimage in \(N\).

The source supplies two conditions: \(\alpha\mid\tau(r)-r\) for every scalar \(r\), and every pair \((0,\alpha y)\) has a common preimage. If \(n\) represents \((x,y)\), choose \(c\) with \(\tau(r)-r=\alpha c\), and a lift \(m\) of \((0,\alpha cy)\). Then \(rn+m\) represents \((rx,\tau(r)y)\). This proves closure under the twisted action.

In the pair-projection quotient \(Q\), the two coordinates are compared by \(\ell(x)=u(y)\). If \(\alpha Q=0\), the actions of \(\tau(\beta)\) and \(\beta\) agree on \(Q\). When \(\beta\) acts injectively there, compatibility of the multiplied pair implies compatibility of the original pair. This is the saturation step for the twisted lattice.

## The head pair and the two projection sequences

Take \(X=M_{\mathbf t}^x\), \(Y=M_{\mathbf t}^{sx}\) in the twisted pair lattice. The new \(x\)-weight block consists of tail coordinates at \(x\) on its zero-bit branch and at \(sx\) on its one-bit branch. Its coordinate map is
\[
(p,q)\longmapsto(p,\tau(q)).
\]
The second scalar action is twisted, so this map is \(A\)-linear: applying \(\tau\) to \(\tau(a)q\) gives \(a\tau(q)\). Both coordinate blocks can be recovered, proving injectivity. A pair represented by \(n\) gives the evaluation of \(1\otimes n\); scalar closure and finite sums then give every new stalk vector. This identifies the head pair lattice with \(M_{s\mathbf t}^x\).

Exact reflection kernels for the tail specify which projection sequence applies. For an ascent \(x<sx\), the sequence has quotient \(M_{\mathbf t}^x\) and kernel the root multiple of the twisted stalk at \(sx\). For a descent, the roles of the two projections exchange. The root acts injectively on each stalk because it is an image submodule inside a product of copies of the coefficient domain.

When the two tail stalks are free, choose lifts of a basis of the quotient to split the sequence. This writes the new stalk as a direct sum of its kernel and quotient, proving freeness. The simultaneous word induction establishes both this freeness and exact reflection kernels; its non-head reflection step uses saturation of the pair lattice.

## The two tail maps in the kernel induction

A new word vector \(m=\sum_j a_j\otimes n_j\) determines two tail vectors:
\[
\mu(m)=\sum_j a_jn_j,\qquad
\nu(m)=\sum_j\tau(a_j)n_j.
\]
The second is viewed in the scalar-twisted tail module. Their projections give the local pair
\[
P_x(m)=\bigl(\pi_x(\mu(m)),\pi_{sx}(\nu(m))\bigr).
\]
Its reflected coordinates are exactly the new \(x\)-weight evaluations. Injectivity of the pair-coordinate map therefore identifies vanishing of the new stalk projection with vanishing of both displayed tail projections.

The induction carries exact reflection kernels and stalk freeness for every weight of the shorter word. To treat \(x\to tx\) with \(t\ne s\), simple edge transport gives the upward edge \(sx\to stx\). Apply old exactness to \(\mu(m)\) on the first edge and \(\nu(m)\) on the second. If \(\beta\) is the root label of \(t\), the two upper projections have the form
\[
\beta p,\qquad \tau(\beta)q.
\]
In the twisted pair module this is \(\beta(p,q)\).

The simple label \(\alpha_s\) does not divide \(\beta\), since distinct reflections have nonproportional representing roots. The old simple-edge quotient is a quotient of the higher free stalk by its \(\alpha_s\)-multiple. Prime divisibility in a basis proves that \(\beta\) acts injectively on this quotient. The pair-lattice compatibility equation then lets us cancel \(\beta\) and place \((p,q)\) itself in the lattice. Its coordinate image is the required divided new stalk vector.

The first-reflection case uses the flip calculation above. New stalk freeness uses the old exact kernels in the two split sequences. This closes both assertions at the same word length.

## Two equal simple letters

In the running example \(A=\mathbb R[\alpha]\), consider the word \((s,s)\). The tail word \((s)\) has stalks \(A\) at both \(1\) and \(s\), and its compatible pairs satisfy \(p-q\in\alpha A\). Hence the new stalk at \(1\) is the twisted pair lattice
\[
L=\{(p,q):p-q\in\alpha A\},\qquad
r\cdot(p,q)=(rp,\tau(r)q).
\]

It has basis \(e_0=(1,1)\), \(e_1=(0,\alpha)\). To expand a pair, note that \(q-\tau(p)\) is divisible by \(\alpha\), since both \(q-p\) and \(p-\tau(p)\) are. Put \(h=(q-\tau(p))/\alpha\). Then
\[
p\cdot e_0+\tau(h)\cdot e_1
=(p,\tau(p))+(0,\alpha h)=(p,q).
\]
If \(r e_0+c e_1=0\), the first coordinate gives \(r=0\), and the second gives \(\alpha\tau(c)=0\), hence \(c=0\). This proves independence.

Thus this stalk has rank two. The projection to its first coordinate has kernel generated by \(e_1\), and \(p\mapsto(p,\tau(p))\) is an explicit splitting. This is the ascent splitting used in the general word-induction proof.

## Coordinate images on upper sets

For a set of weights \(U\), the image module
\[
L_{\mathbf t}(U)=\{(\pi_x(m))_{x\in U}:m\in M_{\mathbf t}\}
\]
records tuples with one common word preimage. Restriction to a smaller set is surjective: keep the same preimage and select fewer coordinates. Compatibility supplies a preimage for the two values on each edge. Compatible-tuple lifting proves that all these edgewise conditions can be realized by one word vector.

Prepending \(s\) gives two image tail maps
\[
F_U:L_{s\mathbf t}(U)\to L_{\mathbf t}(U),\qquad
G_U:L_{s\mathbf t}(U)\to{}^\tau L_{\mathbf t}(sU).
\]
They come from the ordinary and reflected tail maps and jointly determine a new image vector. This follows by collecting the single-weight local-pair zero criterion over \(U\).

For an upper set \(U\), the reflected union \(J=U\cup sU\) and intersection \(K=U\cap sU\) are upper and stable under \(s\). Monotonicity of the higher and lower simple envelopes proves upward closure of these sets.

## Patching and the two-stage projectivity step

Let \(m\) be a new word vector whose two tails agree on \(K\). Use the ordinary tail on \(U\) and the reflected tail on the rest of \(J\). The patched assignment is compatible. On an edge crossing between the two pieces, either the overlap identifies the two values or the edge is \(x\to sx\). In the latter case, the tail difference is an \(\alpha_s\)-multiple and \(\alpha_s\) kills the edge quotient. The old word's compatible-tuple lifting property therefore gives a single preimage for the patch.

This patch identifies the common kernel of restriction to \(K\) and the first image map with
\[
{}^\tau\ker(L_{\mathbf t}(J)\to L_{\mathbf t}(U)).
\]
The second image map is injective on that common kernel; comparing its coordinates with the old kernel proves the isomorphism.

The projectivity step uses
\[
r:L_{s\mathbf t}(U)\to L_{s\mathbf t}(K),\qquad
k:L_{\mathbf t}(U)\to L_{\mathbf t}(K).
\]
The first image map sends \(\ker r\) onto \(\ker k\), with common kernel \(D\). Thus
\[
0\to D\to\ker r\to\ker k\to0,\qquad
0\to\ker r\to L_{s\mathbf t}(U)\to L_{s\mathbf t}(K)\to0.
\]
Old upper-image projectivity makes \(\ker k\) and the twisted old restriction kernel projective. On the stable set \(K\), a split old projection gives a tensor endomorphism that descends to a section of the new projection. Hence \(L_{s\mathbf t}(K)\) is projective. Splitting the two displayed sequences proves projectivity of the new image.

The source uses old-word compatible-tuple lifting in the patch and old-word projectivity in the splittings. Its separate prime-denominator argument proves lifting from projectivity for each fixed word, allowing this conditional step to close the word induction.

## The image sequence for two equal letters

Take \(A=\mathbb R[\alpha]\), the old word \(s\), and \(U=\{s\}\) in the two-element Coxeter group. Then \(J=\{1,s\}\), \(K=\varnothing\),
\[
L_s(J)=\{(f,g):f-g\in\alpha A\},\qquad L_s(U)=A.
\]
The old restriction sends \((f,g)\) to \(g\), so its kernel consists of \((\alpha h,0)\). The [[node:kl.word.common_kernel_equivalence|common-kernel theorem]] identifies the new first-map kernel with the twist of this rank-one module. The resulting sequence for the \(s\)-stalk of the word \((s,s)\) is
\[
0\to{}^\tau(\alpha A)\to L_{ss}(\{s\})\to A\to0.
\]
Its free quotient gives a splitting, exhibiting the rank-two new stalk through the general image construction.

## Prime character classes and diagonal operators

For a prime coefficient \(p\), say that two group weights \(x,y\) are congruent when \(p\) divides \(\chi_x(a)-\chi_y(a)\) for every coefficient \(a\). Pulling test coefficients back through \(\chi_x\) turns this condition into divisibility of linear displacement polynomials for \(yx^{-1}\).

For a root polynomial, the displacement lies in its root line. The [[node:kl.realization.root_line_isometry|root-line isometry theorem]] then gives the identity or that reflection. For a general prime and two distinct congruent weights, a nonzero displacement polynomial is a prime linear generator divisible by \(p\), so it is associated to \(p\). The moving space is consequently a line; reflection faithfulness identifies \(yx^{-1}\) as a reflection. Thus a nontrivial weight class is exactly \(\{x,tx\}\).

The diagonal stabilizer of an image module consists of coordinate weights whose multiplication preserves that image. Coefficient characters belong to it because they come from actual right actions on word vectors. Differences from constant weights and finite products remain stable.

To select one residue class \(C\), choose a test separating a representative from each outside index. The product \(f\) of these tests vanishes outside \(C\) and has values not divisible by \(p\) on \(C\). Put
\[
d=\prod_{c\in C}f(c),\qquad
g=d-\prod_{c\in C}(f(c)-f).
\]
Then \(g\) is stable, equals \(d\) throughout \(C\), and is zero outside it. The scalar \(d\) is not divisible by \(p\).

## A common denominator for the class lifts

A compatible tuple lifts on each prime weight class: use stalk surjectivity for a singleton, and the pair-projection edge condition for a reflection pair. For each class \(j\), choose such a lift \(m_j\), its stable selector \(g_j\), and its scalar \(d_j\). The sum
\[
\sum_j\left(\prod_{k\ne j}d_k\right)D_{g_j}m_j
\]
belongs to the word image and equals \((\prod_jd_j)z\) coordinatewise. Only the term for a coordinate's own class survives. Primality ensures that the common scalar is not divisible by \(p\).

For an arbitrary weight set \(U\), Lean applies this finite argument to subexpression indices whose weights lie in \(U\). Each index carries a whole stalk vector, and repeated group weights give repeated stalk coordinates. A class can therefore contain many indices while representing at most two distinct group weights. Equality in this finite presentation recovers equality in every coordinate of every stalk over \(U\).

The evaluation determinant \(\Delta\ne0\) supplies a generic scalar lift of every tuple. For a compatible tuple, the class construction supplies a scalar avoiding each prime. The projective-target membership theorem removes the prime factors of \(\Delta\) and yields a word lift whenever the upper-coordinate image is projective.

The unconditional word induction now closes: the empty-word image is \(A\) or zero; projectivity of the shorter word gives its lifting property; the two-stage step proves projectivity for the longer word. Applying the fixed-word lifting result gives compatible-tuple lifting for every word.

## Polynomial characters of the word stalks

Choose a basis of the extended realization, giving the coefficient algebra a polynomial presentation \(\mathbb R[X_1,\ldots,X_N]\). Each word stalk is finite, nonnegative and free, so it has a finite homogeneous basis with degrees \(d_j\ge0\). Its character is
\[
C_x^{\mathbf t}(q)=\sum_jq^{d_j}.
\]
The formal variable \(q\) records generator degrees. The variables \(X_i\) belong to the coefficient algebra.

Coefficient transport preserves the real homogeneous pieces. For a real parameter \(0<t<1\), the Hilbert formula is
\[
\sum_n\dim_{\mathbb R}(M_{\mathbf t}^x)_n\,t^n
=C_x^{\mathbf t}(t)(1-t)^{-N}.
\]
The common factor counts the coefficient monomials multiplying each generator. It is the same for the old and new stalks, because prepending a letter keeps the realization coefficient algebra fixed.

## Graded kernels and the factor q

Let \(X=M_{\mathbf t}^x\), \(Y=M_{\mathbf t}^{sx}\), and \(Z=M_{s\mathbf t}^x\). The head pair gives projections \(h_0:Z\to X\) and \(h_1:Z\to Y\). The first is \(A\)-linear; the second is real-linear after the reflected scalar action is removed. Both preserve degree and are surjective.

If \(x<sx\), the first kernel is parametrized by \(y\mapsto C_x(0,\alpha_s y)\). Here \(\alpha_s y\) is formed in the old stalk and then placed in the twisted second coordinate. Its zero-bit coordinates vanish, and its one-bit coordinates are \(\chi_s(\alpha_s y_\eta)\). The root raises degree by one and \(\chi_s\) preserves degree. Thus this kernel has degree-\(n\) piece isomorphic to \(Y_{n-1}\).

If \(sx<x\), the second kernel is parametrized by \(z\mapsto C_x(\alpha_s z,0)\). Its nonzero coordinates are \(\alpha_s z_\eta\), so its degree-\(n\) piece is \(X_{n-1}\).

Taking real dimensions in the two degreewise exact sequences gives
\[
\dim Z_n=
\begin{cases}
\dim X_n+\dim Y_{n-1},&x<sx,\\
\dim Y_n+\dim X_{n-1},&sx<x.
\end{cases}
\]
For a homogeneous target vector, taking the matching component of any preimage proves surjectivity in each degree. These sequences therefore have the exactness needed for rank-nullity.

Multiply by \(t^n\) and sum. Replacing \(n\) by \(n-1\) in the kernel contribution introduces a factor \(t\). Cancelling the common nonzero Hilbert factor gives the evaluated recurrence. A polynomial vanishing throughout \((0,1)\) has infinitely many roots and is zero, so the equality holds formally in \(\mathbb Z[q]\):
\[
C_x^{s\mathbf t}(q)=
\begin{cases}
C_x^{\mathbf t}(q)+qC_{sx}^{\mathbf t}(q),&x<sx,\\
C_{sx}^{\mathbf t}(q)+qC_x^{\mathbf t}(q),&sx<x.
\end{cases}
\]

## Matching the Hecke word

The empty word has character \(1\) at weight \(1\) and zero elsewhere. The unnormalized positive Hecke word begins at \(T_1\), and multiplication by \(I+L_s(q)\) has the same two coefficient recurrences. Induction on the word therefore gives
\[
C_x^{\mathbf t}(q)
=[T_x](I+L_{s_1}(q))\cdots(I+L_{s_m}(q))T_1.
\]
For a reduced word with product \(b\), the graded top stalk is \(A\) with generator in degree zero, and its character is \(1\).

This character argument uses the graded stalks and exact single-edge kernels. The upper-image lifting route supplies global sections and sheaf extension properties, which enter the later boundary-model and duality arguments.

## The repeated-letter character

In the two-element Coxeter group, both stalks of the one-letter word have character \(1\). For \((s,s)\), the recurrence gives
\[
C_1^{ss}(q)=C_s^{ss}(q)=1+q.
\]
The earlier pair-lattice basis has generator degrees zero and one, matching this polynomial. With one coefficient variable, its Hilbert series is
\[
\frac{1+t}{1-t}=1+2t+2t^2+2t^3+\cdots.
\]
Thus the two free generators produce one real basis vector in degree zero and two in every positive degree.

## Definitions and proofs by construction

### A reflection Frobenius extension

- [[node:kl.word.frobenius_data]]
- [[node:kl.word.invariant_subalgebra]]
- [[node:kl.word.reflection_coordinates]]
- [[node:kl.word.reflection_trace]]
- [[node:kl.notes.reflection_frobenius]]
- [[node:kl.word.reflection_algebra_action]]
- [[node:kl.word.reflection_trace_degree]]
- [[node:kl.word.simple_frobenius_data]]

### Paired modules and tensor induction

- [[node:kl.notes.perfect_pairings]]
- [[node:kl.word.trace_restriction_duality]]
- [[node:kl.word.tensor_dual_base_change]]
- [[node:kl.word.tensor_induction]]
- [[node:kl.notes.tensor_pairing]]
- [[node:kl.word.induced_bimodule]]
- [[node:kl.word.induced_pairing_degree]]

### Word modules and homogeneous bases

- [[node:kl.notes.bott_samelson]]
- [[node:kl.word.pairing_degree]]

### Evaluation coordinates and stalk images

- [[node:kl.word.evaluation_maps]]
- [[node:kl.word.evaluation_right_action]]
- [[node:kl.word.wall_coordinates]]
- [[node:kl.word.wall_injectivity]]
- [[node:kl.detail.word_evaluation_injective]]
- [[node:kl.notes.word_stalks]]
- [[node:kl.word.evaluation_grading]]
- [[node:kl.word.weight_support]]
- [[node:kl.word.scaled_coordinate_lifts]]
- [[node:kl.word.support_duality]]
- [[node:kl.word.top_stalk]]

### Two-stalk lattices and their kernels

- [[node:kl.word.edge_annihilation]]
- [[node:kl.word.simple_flip]]
- [[node:kl.word.simple_wall_kernel]]
- [[node:kl.word.twisted_pair_lattice]]
- [[node:kl.word.head_pair_coordinates]]
- [[node:kl.word.head_pair_equivalence]]
- [[node:kl.word.pair_lattice_exact_sequences]]
- [[node:kl.word.kernel_exactness]]
- [[node:kl.word.tail_maps]]
- [[node:kl.word.local_pair_maps]]
- [[node:kl.word.head_pair_saturation]]
- [[node:kl.word.nonhead_kernel_step]]
- [[node:kl.word.stalk_freeness_step]]
- [[node:kl.word.twisted_lattice_saturation]]
- [[node:kl.detail.word_standard_stalks]]

### Images over sets of weights

- [[node:kl.word.coordinate_images]]
- [[node:kl.word.reflected_sets]]
- [[node:kl.word.upper_set_reflection]]
- [[node:kl.word.upper_image_properties]]
- [[node:kl.word.set_tail_maps]]
- [[node:kl.word.set_tail_detection]]
- [[node:kl.word.head_patch]]
- [[node:kl.word.head_patch_lifting]]
- [[node:kl.word.set_kernel_data]]
- [[node:kl.word.common_kernel_equivalence]]
- [[node:kl.word.stable_image_projectivity]]
- [[node:kl.word.upper_projectivity_step]]
- [[node:kl.word.character_congruence]]
- [[node:kl.word.root_character_class]]
- [[node:kl.word.prime_character_class]]
- [[node:kl.word.diagonal_stabilizer]]
- [[node:kl.word.uniform_diagonal_projector]]
- [[node:kl.word.residue_class_projector]]
- [[node:kl.word.class_lift_assembly]]
- [[node:kl.word.finite_stalk_coordinates]]
- [[node:kl.word.word_local_lifting]]
- [[node:kl.word.upper_image_lifting]]
- [[node:kl.word.upper_image_induction]]

### Word characters

- [[node:kl.detail.word_characters]]
- [[node:kl.word.stalk_hilbert_formula]]
- [[node:kl.word.head_kernel_maps]]
- [[node:kl.word.head_kernel_degree]]
- [[node:kl.word.stalk_degree_exactness]]
- [[node:kl.word.character_normalization]]
- [[node:kl.word.character_recursion]]
- [[node:kl.detail.word_character_formula]]
