# Hecke operators and polynomial invariants

This branch constructs the two R-polynomial families from linear operators and develops the identities used to define the canonical KL family. The inputs are Coxeter words, simple descents, and Bruhat order. The outputs are integral polynomials, reciprocal coefficient identities, and positive-word formulas that will later describe word-stalk characters.

The construction has a definite sequence. Left and right operations are defined from length. Their [[node:kl.hecke.commutation|commutation]] makes the right action a tool for proving [[node:kl.hecke.word_independence|reduced-word independence]]. Inverse word operators then define the bar basis. Its support and coefficient identities give R-values, and a descent induction proves that the Laurent values are integral polynomials. The degree bound and inverse bar matrix supply the reciprocal R-kernel used by the KL construction.

The overview [[node:kl.notes.hecke_action]] develops the operators, their quadratic relation, and the bar involution. The entries below supply the individual constructions and proofs.

## Finite coefficient vectors and the two operator conventions

The standard module consists of finite sums \(\sum_w c_we_w\), with \(c_w\) in a commutative ring. The basis label \(w\) is a group element; the coefficient records how much of that basis vector occurs. A linear operator is determined by its values on the individual basis vectors.

For a simple reflection \(s\), its action uses the two possibilities \(\ell(sw)=\ell(w)+1\) and \(\ell(sw)=\ell(w)-1\). The source uses two conventions:

| Convention | Ascent action | Descent action | Quadratic identity |
|---|---|---|---|
| Normalized, parameter \(a\) | \(L_sH_w=H_{sw}\) | \(L_sH_w=H_{sw}+aH_w\) | \(L_s^2=I+aL_s\) |
| Unnormalized, parameter \(q\) | \(L_sT_w=T_{sw}\) | \(L_sT_w=qT_{sw}+(q-1)T_w\) | \(L_s^2=qI+(q-1)L_s\) |

The right operators use \(ws\) instead. In an ascent pair \(w,sw\), the two matrices are
\[
\begin{pmatrix}0&1\\1&a\end{pmatrix},
\qquad
\begin{pmatrix}0&q\\1&q-1\end{pmatrix}.
\]
Squaring each matrix proves the corresponding quadratic identity on that pair. Such pairs account for the whole basis.

The normalized inverse is \(L_s-aI\). In the unnormalized convention, for a unit \(q\), the inverse is \(q^{-1}(L_s-(q-1)I)\). Multiplying these expressions by \(L_s\) on either side and using the quadratic identity gives \(I\).

Over Laurent coefficients, \(q=v^2\), \(H_w=v^{-\ell(w)}T_w\), and \(a=v-v^{-1}\). The explicit basis rescaling converts the second operator table to the first.

## Reduced words determine standard operators

For a word \(\omega=(s_1,\ldots,s_m)\), let \(L_\omega=L_{s_1}\cdots L_{s_m}\), with the rightmost factor acting first. If the word is reduced with product \(w\), each step in its action on \(e_1\) is an ascent, giving \(L_\omega e_1=e_w\).

The right word with the same factor order gives \(D_\omega e_1=e_{w^{-1}}\). Thus every basis vector is obtained from \(e_1\) by a reduced right word.

[[node:kl.coxeter.simple_edge_transport|Simple-edge transport]] proves the length-orientation identities needed for \(L_sD_t=D_tL_s\). Once this commutation is established, an operator commuting with all right operations is determined by its value at \(e_1\):
\[
F(D_\omega e_1)=D_\omega F(e_1).
\]
Two reduced left words for \(w\) commute with those right operations and both send \(e_1\) to \(e_w\). They are therefore the same operator. This constructs the standard unit \(U_w\) and its inverse.

For example, in type \(A_2\), the reduced words \(sts\) and \(tst\) have the same product, so \(L_sL_tL_s=L_tL_sL_t\). This relation follows from the regular-action construction.

## Inverse words and parameter interchange

The bar-basis vector is
\[
b_w=U_{w^{-1}}^{-1}e_1,
\]
and the linear bar transform \(B\) sends \(e_w\) to \(b_w\). For an ascent \(sw>w\), the right-ascent identity for \(w^{-1}s\) gives \(b_{sw}=L_s^{-1}b_w\).

The simple vectors are
\[
b_s(a)=H_s-aH_1,\qquad
b_s(q)=q^{-1}T_s+(q^{-1}-1)T_1.
\]
The two parameter identities are
\[
B_aL_s(-a)=L_s(a)^{-1}B_a,\qquad B_aB_{-a}=I,
\]
\[
B_qL_s(q^{-1})=L_s(q)^{-1}B_q,\qquad B_qB_{q^{-1}}=I.
\]
They follow by computing ascent and descent cases for \(L_s^{-1}b_w\), then inducting over a reduced word.

In the Laurent convention, coefficient inversion sends \(a=v-v^{-1}\) to \(-a\). Composing that inversion with \(B_a\) produces the semilinear bar. The [[node:kl.hecke.bar_interchange|inverse-composition identity]] proves that applying this semilinear operation twice returns the original vector.

## Bruhat support and coefficient normalization

The bar vector \(b_y\) is supported on the lower Bruhat ideal of \(y\). To see the inductive step, write \(y=sv\) with \(v<sv\). The coefficient of \(e_x\) in \(L_s^{-1}b_v\) uses only the previous coefficients at \(x\) and \(sx\). If \(x\not\le sv\), then neither \(x\) nor \(sx\) lies below \(v\); the second statement follows from monotonicity of the upper simple envelope. Both previous coefficients are therefore zero.

The diagonal coefficient is one in the normalized convention and \(q^{-\ell(y)}\) in the unnormalized convention. The normalized R-family is defined by substituting operator parameter \(-T\):
\[
\widetilde R_{x,y}(T)=b_y(-T)(x).
\]
For a simple reflection this gives \(\widetilde R_{1,s}(T)=T\).

In the unnormalized convention define
\[
r_q(x,y)=(-1)^{\ell(x)}(-q)^{\ell(y)}b_y(q)(x).
\]
Then \(r_q(x,x)=1\), and \(r_q(x,y)=0\) outside Bruhat order. For one simple reflection,
\[
r_q(1,s)=(-q)(q^{-1}-1)=q-1.
\]
These normalization factors determine the signs in the subsequent recurrences.

## Descent produces integral polynomials

For any left descent \(sy<y\), the inverse-operator [[node:kl.hecke.r_parameter_reciprocity|coefficient formula]] proves
\[
r_q(x,y)=
\begin{cases}
r_q(sx,sy),&sx<x,\\
(q-1)r_q(x,sy)+q\,r_q(sx,sy),&sx>x.
\end{cases}
\]
The bar vector was defined independently of the chosen descent, so this is an identity for every left descent.

Take \(q=Q\), the Laurent indeterminate. At upper endpoint \(1\), the R-values are zero or one. If the values with shorter upper endpoint \(sy\) are polynomial, the two recurrence branches are polynomial as well: the new expression is either an old polynomial or \((Q-1)p(Q)+Qr(Q)\). Strong induction proves that all Laurent values have nonnegative exponents.

The unique integral polynomial with that Laurent image is \(R_{x,y}\). A second descent induction proves \(R_{x,y}(q)=r_q(x,y)\) at every unit parameter in every commutative ring.

For distinct simple reflections \(s,t\), the recurrence computes
\[
R_{1,st}=(q-1)R_{1,t}+qR_{s,t}=(q-1)^2.
\]
The term \(R_{s,t}\) is zero because distinct elements of equal length are not comparable.

The same recurrence bounds the degree by \(d(x,y)=\ell(y)-\ell(x)\) for comparable endpoints. In the lower-ascent branch, the first smaller interval has rank \(d-1\), and the second has rank \(d-2\) when its endpoints are comparable. Multiplication by \(q-1\) or \(q\) gives the required bound; a noncomparable second term is zero.

## Parameter reciprocity and the inverse coefficient matrix

Define a second family by multiplying \(r_{q^{-1}}(x,y)\) by
\((-q)^{\ell(y)}(-q^{-1})^{\ell(x)}\).
It has the same initial values and, after cancelling the two added powers in each descent case, the same recurrence as \(r_q\). Induction identifies the families. Expanding the definition gives the useful coefficient formula
\[
r_{q^{-1}}(x,y)=q^{\ell(x)}b_y(q)(x).
\]

The matrix identity \(B_qB_{q^{-1}}=I\) gives another [[node:kl.hecke.bar_coefficient_inverse|finite coefficient identity]]:
\[
\sum_{z\le y}
r_q(x,z)\,q^{\ell(y)-\ell(z)}r_{q^{-1}}(z,y)
=\delta_{x,y}.
\]
The bar support restricts the sum to a finite lower ideal. The factors involving the intermediate length \(\ell(z)\) cancel in the explicit normalization calculation.

For a polynomial \(p\) of degree at most \(d\), define its reflection by
\[
\operatorname{reflect}_d p=q^dp(q^{-1}).
\]
For example, \(2+3q\) becomes \(2q^2+3q\) in degree two. The [[node:kl.hecke.ordinary_r_degree|R-degree bound]] makes every reflected factor a polynomial, so the coefficient identity descends from Laurent polynomials to
\[
\sum_{x\le z\le y}R_{x,z}\operatorname{reflect}_{d(z,y)}R_{z,y}
=\delta_{x,y}.
\]
Reflecting in total degree \(d(x,y)\) gives the version with the first factor reflected. These are the [[node:kl.detail.r_kernel|inverse-kernel identities]] used by the canonical KL construction.

## Positive words and the character calculation

For a word \(\omega=(s_1,\ldots,s_m)\), put
\[
H_\omega(q)=(I+L_{s_1}(q))\cdots(I+L_{s_m}(q))T_1,
\]
and write \(h_\omega(x;q)\) for its \(T_x\)-coefficient. In particular \(H_s=T_1+T_s\).

The quadratic inverse implies
\[
I+L_s(q)^{-1}=q^{-1}(I+L_s(q)).
\]
Bar intertwining therefore contributes one factor \(q^{-1}\) per letter:
\[
B_qH_\omega(q^{-1})=q^{-m}H_\omega(q).
\]
For a reduced word with product \(b\), monotonicity of the upper simple envelope puts the support below \(b\). Taking a coefficient of the inverse-parameter bar identity gives
\[
\sum_{z\le b}r_q(x,z)h_\omega(z;q)
=q^{-\ell(x)}q^m h_\omega(x;q^{-1}).
\]
The [[node:kl.detail.word_character_formula|word-module character theorem]] later identifies \(h_\omega(x;q)\) with its stalk character. [[node:kl.word.support_duality|Word support duality]] identifies the reciprocal expression with its full outgoing-kernel character. This supplies the R-convolution used in boundary-model cancellation.

## The normalization data and the recursive P-family

A normalized pair consists of two integral polynomial families. The R-family has diagonal one, vanishes outside \(x\le y\), and satisfies the ordinary recurrence for every left descent of \(y\). The P-family has diagonal one, the same support condition, the strict midpoint degree bound, and the reciprocity equation
\[
\operatorname{reflect}_{d(x,y)}P_{x,y}
=\sum_{x\le z\le y}R_{x,z}P_{z,y}.
\]
These are the seven fields of the normalization data.

The ordinary R-family is already constructed. To build P, set \(P_{x,x}=1\) and \(P_{x,y}=0\) outside \(x\le y\). On a strict interval define the reciprocity defect
\[
D_{x,y}=\sum_{x<z\le y}R_{x,z}P_{z,y}.
\]
The bottom \(x\) is omitted, while the top \(y\) is included. Each \(P_{z,y}\) has smaller rank because
\[
d(z,y)=\ell(y)-\ell(z)<\ell(y)-\ell(x)=d(x,y).
\]
Thus strong recursion on the rank difference determines the sum before constructing the next P-value.

## The coefficient choice below the midpoint

For \(p(q)=\sum_i a_iq^i\), its strict lower-half truncation is
\[
\operatorname{low}_dp=\sum_{2i<d}a_iq^i.
\]
At even \(d=2m\) it keeps degrees \(0,\ldots,m-1\); at odd \(d=2m+1\) it keeps \(0,\ldots,m\).

Suppose \(P\) is supported strictly below \(d/2\). Its reflection has no coefficients below that midpoint. Reading
\[
\operatorname{reflect}_dP=P+D
\]
in a low degree gives \(0=P_i+D_i\). Hence the required choice is
\[
P=-\operatorname{low}_dD.
\]
The negative sign comes directly from the equation.

For an anti-reciprocal defect, \(D_{d-i}=-D_i\). Its middle coefficient is zero when \(d\) is even, since an integer equal to its negative must vanish. Coefficients above \(d\) also vanish: Lean's reflection fixes those positions, and [[node:kl.hecke.defect_antireciprocity|anti-reciprocity]] again makes each coefficient equal to its negative.

These relations prove the high-degree equations for the chosen \(P\). In a low degree, \(P_i+D_i=0\). In a high degree, the reflected coefficient is \(-D_{d-i}=D_i\). At the middle both sides are zero. This is the [[node:kl.hecke.low_part_solution|lower-half solution theorem]].

For the algebraic example
\[
d=3,\qquad D=q^3+2q^2-2q-1,
\]
the construction gives \(P=1+2q\), and
\[
\operatorname{reflect}_3P=q^3+2q^2=P+D.
\]

## The R-kernel calculation behind anti-reciprocity

In a strict interval \(x<y\), assume reciprocity has been proved for every proper upper pair \((z,y)\). Degree bounds and rank additivity permit reflection of each product:
\[
\operatorname{reflect}_{d(x,y)}(R_{x,z}P_{z,y})
=\overline R_{x,z}\operatorname{reflect}_{d(z,y)}P_{z,y}.
\]
Substitute the smaller reciprocity equations and interchange the two finite sums:
\[
\begin{aligned}
\operatorname{reflect}_{d(x,y)}D_{x,y}
&=\sum_{x<z\le y}\overline R_{x,z}
  \sum_{t\le y}R_{z,t}P_{t,y}\\
&=\sum_{t\le y}
  \left(\sum_{x<z\le y}\overline R_{x,z}R_{z,t}\right)P_{t,y}.
\end{aligned}
\]

The [[node:kl.hecke.proper_r_kernel|reversed R-kernel identity, with its bottom term removed]], evaluates the parenthesized sum as
\[
\delta_{x,t}-R_{x,t}.
\]
Its delta contribution is \(P_{x,y}\), while the other contribution is the negative full R-weighted sum. Consequently
\[
\operatorname{reflect}_{d(x,y)}D_{x,y}
=P_{x,y}-\sum_{t\le y}R_{x,t}P_{t,y}
=-D_{x,y}.
\]

The defect is therefore anti-reciprocal. The lower-half solution theorem gives the new reciprocity equation. The degree bound was already ensured by the truncation, so the rank induction supplies every P-condition.

## Two small interval calculations

On \([1,s]\), the defect is \(q-1\), whose lower half in degree one is \(-1\). Thus \(P_{1,s}=1\), and reciprocity reads
\[
q=1+(q-1).
\]

For distinct simple reflections \(s,t\), the interval \([1,st]\) has the four elements \(1,s,t,st\). Its three proper-upper contributions are
\[
D_{1,st}=(q-1)\cdot1+(q-1)\cdot1+(q-1)^2\cdot1=q^2-1.
\]
The negative lower half in degree two is again one, so \(P_{1,st}=1\) and reciprocity reads \(q^2=1+(q^2-1)\).

## Uniqueness and the selected interfaces

Two normalized R-families agree by induction on the upper length: they have the same values at upper endpoint \(1\), and each descent recurrence uses a shorter upper endpoint.

Once R is common, compare two P-families by induction on interval rank. The proper-upper terms of their reciprocal equations agree by induction. Subtraction leaves
\[
\operatorname{reflect}_df=f,\qquad f=P_{x,y}-P'_{x,y}.
\]
The difference remains strictly below the midpoint. If its highest nonzero degree were \(m\), then \(d-m>m\). Reflection would give coefficient zero at \(m\), while \(f_m\ne0\), a contradiction. Thus \(f=0\).

The constructed pair supplies all seven fields, and these two inductions prove uniqueness. The source's selected pair, klFamilies, is therefore the constructed pair. Its [[node:kl.hecke.selected_families|public components]] rPolynomial and klPolynomial agree with the explicit R and recursive P formulas.

## Dihedral lower-interval sums

In a Coxeter system with two simple generators, every reduced word alternates. A reduced word of strictly smaller length occurs in a longer alternating word either as a prefix or as a prefix after deleting the first letter. The subword criterion therefore gives
\[
x\le w\quad\Longleftrightarrow\quad \ell(x)<\ell(w)\ \text{or}\ x=w.
\]

In the unnormalized Hecke module put
\[
S_w=\sum_{z\le w}T_z.
\]
Fix a reduced alternating word for \(w\) of length \(n+2\), starting with \(s\). Let \(v=sw\) be its tail and \(p\) its prefix of length \(n\).

Multiplication by \(s\) partitions the group into simple-reflection strings \(\{r,sr\}\), with \(r\) the shorter member. A lower ideal can meet such a pair only in the following ways:

| Members below \(v\) | Contribution to \((I+L_s(q))S_v\) |
|---|---|
| Neither | \(0\) |
| Only \(r\) | \(T_r+T_{sr}\) |
| Both \(r,sr\) | \((1+q)(T_r+T_{sr})\) |

The union of strings that meet \([1,v]\) is \([1,w]\). The [[node:kl.hecke.dihedral_strings|double-membership theorem]] proves that the elements in fully included strings form the empty set when \(n=0\), and \([1,p]\) when \(n>0\). Thus
\[
(I+L_s(q))S_v=S_w+qC,\qquad
C=\begin{cases}0,&n=0,\\ S_p,&n>0.\end{cases}
\]
For a reduced word \(sts\), the extra string is \(\{1,s\}\), so the correction is \(q(T_1+T_s)\).

## The dihedral bar calculation and constant P-family

Apply the coefficient-linear bar transform \(B_q\) to the product equation at \(q^{-1}\). Intertwining and the smaller-word induction formulas give
\[
q^{-(n+2)}S_w+q^{-(n+1)}C
=B_qS_w+q^{-(n+1)}C.
\]
Subtracting the common term proves \(B_qS_w=q^{-\ell(w)}S_w\). The length-zero and length-one sums give the induction bases, and \(C=0\) handles the length-two step.

At the inverse parameter, the coefficient of \(T_x\) in this identity is
\[
\sum_{z\le y}b_z(q^{-1})(x)=q^{\ell(y)}
\qquad(x\le y).
\]
The R-value identity \(r_q(x,z)=q^{-\ell(x)}b_z(q^{-1})(x)\) converts it to
\[
\sum_{x\le z\le y}R_{x,z}(q)=q^{d(x,y)}.
\]
The return to ordinary polynomials uses the injective polynomial inclusion in Laurent polynomials.

Now take \(Q_{x,y}=1\) on comparable pairs and zero outside \(x\le y\). Its degree is zero on every strict interval. Its reciprocity equation is precisely
\[
\operatorname{reflect}_{d(x,y)}1=q^{d(x,y)}
=\sum_{x\le z\le y}R_{x,z}Q_{z,y}.
\]
Thus \((R,Q)\) has all seven normalization fields. Uniqueness proves \(P_{x,y}=1\) throughout every dihedral interval.

This polynomial calculation uses the abstract two-generator Coxeter system. In the sheaf development, the induced ambient labels enter a separate interpolation proof of the dihedral structure-model properties. The source correspondence explains how the notes relate the two descriptions.

## The square parameter and normalized reciprocity

The normalized family is characterized by
\[
R_{x,y}(v^2)=v^{d(x,y)}\widetilde R_{x,y}(v-v^{-1}).
\]
For our interval, \(\widetilde R_{1,s}(T)=T\), because \(v(v-v^{-1})=v^2-1\).

Later the comparison uses a real number \(0<t<1\), sets \(q=t^2\), and uses the positive scalar
\[
T=t^{-1}-t.
\]
Applying the square-parameter identity at \(t^{-1}\) produces this positive parameter. The reciprocal, scaled equation below is the resulting form used by the transfer operators.

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

## Reciprocal scaled differences

For an integral polynomial \(p\), write \(S_d(p;t)=t^{-d}p(t^2)\). A monomial \(a_iq^i\) contributes \(a_it^{2i-d}\). The strict midpoint bound makes these exponents negative; inversion changes them to \(d-2i\).

Suppose two polynomials \(P,P'\) satisfy that bound and
\[
S_d(P;t)-S_d(P';t)
=S_d(P;t^{-1})-S_d(P';t^{-1})
\quad(0<t<1).
\]
For any \(0<q<1\), put \(t=\sqrt q\). Writing \(\Delta=P-P'\), the equation is
\[
t^{-d}\Delta(q)=t^d\Delta(q^{-1}).
\]
Multiplication by \(t^d\) gives \(\Delta(q)=q^d\Delta(q^{-1})\). The equality on an infinite real interval implies a polynomial reflection identity. The same [[node:kl.hecke.low_degree_rigidity|highest-coefficient argument]] then gives \(\Delta=0\).

This is the precise passage from [[node:kl.hecke.scaled_difference_rigidity|reciprocal equality of scaled evaluations]] to equality of integral polynomials. Its nodes connect the final comparison to the degree restriction in the normalization data.

## Outputs for the invariance proof

The algebraic constructions supply the ordinary and normalized R-families, the canonical KL family, and the positive-word identities. Reflection-order geometry identifies normalized R with path sums. Word modules identify positive-word coefficients with stalk characters.

The actual boundary character \(C\) has its own R-reciprocity, proved through sheaf decomposition and cancellation. The simultaneous comparison establishes R-invariance and suffix-kernel freeness using that character. The later canonical-polynomial induction uses the common R-matrix and the strict KL degree bound to prove P-invariance.

## Definitions and proofs by construction

### Hecke modules and operators

- [[node:kl.definitions.hecke_operators]]
- [[node:kl.definitions.hecke_quadratic_relation]]
- [[node:kl.detail.hecke_quadratic_identity]]
- [[node:kl.notes.hecke_action]]
- [[node:kl.hecke.commutation]]
- [[node:kl.hecke.word_actions]]
- [[node:kl.hecke.word_independence]]

### The bar operation

- [[node:kl.definitions.bar_involution]]
- [[node:kl.hecke.bar_interchange]]
- [[node:kl.hecke.bar_triangularity]]

### The R-polynomial families

- [[node:kl.detail.ordinary_r]]
- [[node:kl.detail.rtilde_family]]
- [[node:kl.detail.r_kernel]]
- [[node:kl.detail.rtilde_recursion]]
- [[node:kl.foundations.rtilde]]
- [[node:kl.hecke.r_values]]
- [[node:kl.hecke.r_value_recursion]]
- [[node:kl.hecke.ordinary_r_construction]]
- [[node:kl.hecke.ordinary_r_degree]]
- [[node:kl.hecke.r_parameter_reciprocity]]
- [[node:kl.hecke.bar_coefficient_inverse]]

### Canonical KL polynomials

- [[node:kl.hecke.polynomial_reflection]]

- [[node:kl.foundations.normalized_kl]]
- [[node:kl.foundations.low_half]]
- [[node:kl.detail.kl_defect]]
- [[node:kl.detail.kl_recursion]]
- [[node:kl.foundations.canonical_kl]]
- [[node:kl.hecke.low_part_properties]]
- [[node:kl.hecke.low_part_solution]]
- [[node:kl.hecke.low_degree_rigidity]]
- [[node:kl.hecke.recursive_p]]
- [[node:kl.hecke.recursive_p_degree]]
- [[node:kl.hecke.proper_r_kernel]]
- [[node:kl.hecke.defect_antireciprocity]]
- [[node:kl.hecke.normalization_unique]]
- [[node:kl.hecke.selected_families]]

### Word expansions and rigidity

- [[node:kl.foundations.scaled_kl]]
- [[node:kl.comparison.reciprocal_rigidity]]
- [[node:kl.notes.dihedral_kl]]
- [[node:kl.hecke.positive_words]]
- [[node:kl.hecke.positive_word_reciprocity]]
- [[node:kl.hecke.scaled_polynomials]]
- [[node:kl.hecke.scaled_difference_rigidity]]
- [[node:kl.hecke.lower_interval_sums]]
- [[node:kl.hecke.dihedral_strings]]
- [[node:kl.hecke.dihedral_sum_product]]
- [[node:kl.hecke.dihedral_bar_sum]]
- [[node:kl.hecke.dihedral_r_sum]]
