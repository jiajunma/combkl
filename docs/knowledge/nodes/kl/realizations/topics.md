# Realizations and root geometry

The realization converts Coxeter generators into linear reflections. Its roots provide the edge labels used by the coefficient algebra; its rank-two planes support the later dihedral arguments. The construction begins with a matrix determined by the Coxeter exponents and ends with a faithful action whose rank-one changes are exactly the reflections.

## From the Coxeter matrix to linear operators

For a finite simple-generator set \(I\), take \(V_0=\mathbb R^I\) with basis \(\alpha_i\). The Tits form is determined by
\[
B(\alpha_i,\alpha_j)=-2\cos(\pi/m_{ij}),
\]
where the value for an infinite exponent is \(-2\). On the diagonal, \(m_{ii}=1\), so the value is two.

The normal functional \(\nu_i=B(\alpha_i,-)\) assigns a real number to a vector. The simple operator is
\[
r_i(v)=v-\nu_i(v)\alpha_i.
\]
It fixes \(\ker\nu_i\) and negates \(\alpha_i\). Since \(\nu_i(\alpha_i)=2\), applying it twice returns \(v\). The finite Coxeter relations between these operators make their word products depend only on the element of \(W\). This gives the geometric action.

## A degenerate form and the information needed by the proof

For the infinite dihedral system,
\[
B=\begin{pmatrix}2&-2\\-2&2\end{pmatrix}.
\]
The simple roots remain independent, while their normals satisfy \(\nu_t=-\nu_s\). The radical is the line spanned by \(k=\alpha_s+\alpha_t\).

The later moving-plane calculation needs independent normal functionals: it solves for prescribed values of two normals and uses those values to recover the span of the two roots as the image of a reflection product minus the identity. Enlarging the ambient space supplies the required independent normals while retaining the original root vectors and their action.

## Pair the radical with its dual

Let \(K=\ker B^\flat\), and choose a projection \(p:V_0\to K\) fixing \(K\). On \(E=V_0\oplus K^*\), put
\[
B_p((v,\phi),(w,\psi))
=B(v,w)+\phi(pw)+\psi(pv).
\]
The first term retains the original pairings; the other two pair radical directions with linear functionals that detect them.

If \((v,\phi)\) pairs to zero with everything, testing against \((0,\psi)\) gives \(pv=0\). Testing against \((k,0)\) for \(k\in K\) gives \(\phi=0\). Testing against every \((w,0)\) then puts \(v\) in \(K\), so \(v=pv=0\). This proves nondegeneracy.

For the infinite dihedral example, choose \(p(x\alpha_s+y\alpha_t)=(x+y)k/2\) and \(\phi(k)=2\). The extended matrix is
\[
\begin{pmatrix}2&-2&1\\-2&2&1\\1&1&0\end{pmatrix}.
\]
Its determinant is \(-8\), and the two simple normals have independent rows \((2,-2,1)\) and \((-2,2,1)\).

## Extend the action and measure moving spaces

The extended action uses the same reflection formula with the extended form and embedded roots. For a simple generator it restricts to the original action because the original form is preserved on \(V_0\oplus0\). Induction on a word proves the restriction identity for every group element.

For an operator \(g\), its moving space is the image of \(g-1\). A reflection has a one-dimensional moving space. The reflection-faithfulness theorem proves the converse for the extended Coxeter action as well as faithfulness of the action.

Two independent roots with independent normals give a stronger statement:
\[
\operatorname{im}(r_\alpha r_\beta-1)
 =\operatorname{span}\{\alpha,\beta\}.
\]
Thus equal products of two reflections identify the same root plane. This is the geometric input used to place a diamond of reflection edges in a dihedral coset.

## Positive roots and inversion counts

Real roots are translates of the simple roots under the geometric action. A positive root has nonnegative simple-root coordinates. The root-sign theorem proves that every real root has one sign, and each reflection has a unique positive representing root.

The positive roots sent negative by the inverse action of \(w\) form its root-inversion set. Their number is \(\ell(w)\). Accordingly a root-sign change detects whether left multiplication by its reflection increases or decreases length. The geometric plane-weight identity later groups these inversion changes plane by plane.

## The outputs used elsewhere

The coefficient algebra uses the extended root space and turns a root vector into a degree-one polynomial. Root-plane geometry produces the induced dihedral systems and geometric reflection orders. The cotangent action also enters the proof that a finite standard parabolic system embeds faithfully, which supports the final finite-support reduction.


## Definitions and proofs by construction

### The geometric root space and Tits form

- [[node:kl.realization.tits_form]]

### The geometric action

- [[node:kl.realization.linear_reflection]]
- [[node:kl.realization.geometric_action]]

### Degeneracy and the nondegenerate extension

- [[node:kl.realization.radical_extension]]
- [[node:kl.notes.extended_realization]]
- [[node:kl.realization.extension_minimality]]

### The extended action and reflection faithfulness

- [[node:kl.realization.extended_action]]
- [[node:kl.notes.reflection_faithfulness]]
- [[node:kl.realization.reflection_plane]]

### Roots, positivity, and inversions

- [[node:kl.detail.positive_roots]]
- [[node:kl.detail.root_reflection_correspondence]]
- [[node:kl.detail.root_inversions]]
- [[node:kl.detail.root_inversion_count]]

## Operator relations and dual coordinates

The Chebyshev recurrence computes powers of two simple reflections. For a finite Coxeter exponent, the even or odd vanishing identity makes the product have the required power on the two-root span; the common fixed space completes the calculation on the ambient vector space. The coordinate-dual action applies the same relation theorem to Gram rows and coordinate evaluations, including an infinite generator set.

The moving-space definition separates the linear-algebra statement from the group-theoretic one. An orthogonal map with moving rank one has an explicit reflection formula. The Coxeter argument then uses length descent to identify the group element producing that map.

- [[node:kl.realization.rank_two_coefficients]]
- [[node:kl.realization.finite_reflection_relations]]
- [[node:kl.realization.moving_spaces]]
- [[node:kl.realization.orthogonal_rank_one]]
- [[node:kl.realization.cotangent_action]]

## Root signs, faithfulness, and signed labels

Minimal parabolic representatives separate a shorter prefix from a two-generator tail. The alternating-root formula expresses that tail using nonnegative coefficients. Strong induction on length therefore proves the sign of a simple-root image. A right descent then detects every nonidentity element, proving faithfulness of the geometric action and its extensions.

The same sign theorem makes every real root positive or negative. A simple reflection changes the sign precisely at its own positive root. This identifies the earlier combinatorial sign bit with the coordinate sign of an actual root and leads to the inversion count.

- [[node:kl.realization.alternating_root_formula]]
- [[node:kl.realization.simple_root_sign]]
- [[node:kl.realization.faithful_actions]]
- [[node:kl.realization.dominant_functional]]
- [[node:kl.realization.dominant_signs]]
- [[node:kl.realization.signed_root_representation]]
- [[node:kl.realization.signed_root_action]]
