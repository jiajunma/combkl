# Localization and comparison of embedded images

This topic derives an inclusion between two submodules of the same edge module from local calculations on root-plane cosets. The argument starts with the two images, constructs a free target, compares the images after localization, and then recovers global membership.

Fix an edge \(e:x\to y\) with label \(\alpha\), and fix the outgoing conditions that remain during its scheduled step. Let \(K_x\subseteq B^x\) and \(K_y\subseteq B^y\) be the corresponding kernels. Put
\[
I_e=\rho_{x,e}(K_x),\qquad J_e=\rho_{y,e}(K_y).
\]
Both are submodules of \(B^e\). The goal is \(I_e\subseteq f_eJ_e\), where \(f_e\) is the edge factor from reflection orders and paths.

The freeness hypothesis concerns the upper kernel \(K_y\). It gives a free target for the lower-image comparison.

## Freeness of the upper image over the edge ring

The upper quotient rule gives
\[
B^e\simeq B^y/\alpha B^y.
\]
Restricting this quotient map to \(K_y\), its kernel is \(K_y\cap\alpha B^y\).

The saturation argument proves
\[
K_y\cap\alpha B^y=\alpha K_y.
\]
The nontrivial inclusion says that if \(\alpha m\) satisfies the remaining conditions, then \(m\) also satisfies them. Those conditions involve other outgoing labels at \(y\). Their independence from the current incoming root makes multiplication by \(\alpha\) injective on the corresponding edge quotients, so the factor can be cancelled in each condition.

It follows that
\[
J_e\simeq K_y/\alpha K_y.
\]
If \(K_y\) has an \(A\)-basis of \(r\) elements, their residue classes give a basis of this quotient over \(C=A/(\alpha)\). Thus \(J_e\) is a free \(C\)-module. Multiplication by the nonzero factor \(f_e\) identifies it with another free module, \(f_eJ_e\), embedded in the same edge module.

This explains exactly where upper-kernel freeness is consumed. Finite generation or equality of ranks would not supply this free target.

## Localization in polynomial coordinates

Take the illustrative coefficient ring \(A=\mathbb R[\alpha,\beta,\gamma]\) and the prime ideal
\[
\mathfrak p=(\alpha,\beta).
\]
Localizing at \(\mathfrak p\) means allowing denominators outside that ideal:
\[
A_{\mathfrak p}=\{a/d:d\notin\mathfrak p\}.
\]
Thus \(\gamma\) becomes a unit, while \(\alpha\) and \(\beta\) remain in the maximal ideal.

An edge labelled by \(\gamma\) now has zero edge quotient: every element is a multiple of a unit, so
\[
A_{\mathfrak p}/(\gamma)=0.
\]
An edge labelled by a linear combination of \(\alpha,\beta\) can still impose a condition. This is the algebraic reason localization at a root-plane prime leaves only the edges belonging to that plane.

Tensoring a module with \(A_{\mathfrak p}\) implements localization. For a general flat scalar extension \(R\to S\), compatible sections are the kernel of the section constraint, and selected stalk kernels are kernels of the outgoing constraint. Tensoring commutes with the finite products in those constraints. The [[node:kl.sheaves.flat_section_base_change|flat section base-change theorem]] therefore identifies the sections after extension.

For an embedded submodule \(P\subseteq M\), the extended submodule \(P_S\) is the image of \(S\otimes_RP\) in \(S\otimes_RM\). The [[node:kl.algebra.flat_embedded_modules|embedded base-change theorem]] gives
\[
(\ker f)_S=\ker f_S,\qquad (f(P))_S=f_S(P_S),
\]
with flatness required for the kernel identity. Applying these equations to the selected outgoing constraints and both edge restrictions proves the [[node:kl.notes.sheaf_localization|flat kernel-and-image theorem]]. Both images are then compared inside the same extended edge module.

Generation, free stalks, finite generation, the upper-quotient rule and flabbiness transfer with the hypotheses stated in the [[node:kl.sheaves.base_change_properties|scalar-extension property theorem]]. Restriction to a surviving coset adds the graph-pullback conditions developed next.

## Root quotients and localized reduction

Let \(a\) be a positive root with polynomial label \(r_a=\lambda(a)\). Its original edge coefficient ring is \(E_a=A/(r_a)\). For a subspace \(P\), localization gives \(R_P=A_{\mathfrak p_P}\), and the localized edge ring is
\[
E_{P,a}=R_P/(\lambda_P(a)),
\qquad \lambda_P=\eta_P\lambda.
\]
Write \(q_{P,a}:R_P\to E_{P,a}\). The localized reduction map is
\[
r_{P,a}(v)=q_{P,a}(\eta_P(\lambda(v))).
\]
In particular it kills \(a\).

The [[node:kl.algebra.tensor_scalar_quotient|tensor-quotient theorem]] identifies
\[
R_P\otimes_A E_a\simeq E_{P,a},
\qquad
s\otimes[f]\longmapsto q_{P,a}(s\eta_P(f)).
\]
The induced map from \(E_a\) sends \([f]\) to \(q_{P,a}(\eta_P(f))\). Thus the quotient and localization routes give the same actual reduced label.

For \(P=P(a,b)\), the [[node:kl.local.plane_prime_membership|plane-prime membership theorem]] gives
\(\mathfrak p_P=(\lambda(a),\lambda(b))\). If a positive root \(c\ne a\) lies in this span, write
\[
c=sa+rb.
\]
[[node:kl.realization.root_planes|Independence of distinct positive roots]] forces \(r\ne0\), and reduction gives
\[
r_{P,a}(c)=r\,r_{P,a}(b).
\]
The image of \(r\) is a unit, so the two labels are associated scalars. The [[node:kl.local.localized_root_reduction|localized root-reduction theorem]] proves this identity and traces it to the source's polynomialRoot values. Its linear-algebra assertion also holds when the localization subspace is chosen independently of \(P(a,b)\).

## The finite relative coset graph

Fix the induced plane subgroup \(D_P\), a representative \(a_0\) of least ambient length in \(D_Pa_0\), and the ambient top \(b\). The vertices are
\[
K=\{d\in D_P:1\le_D d,\ da_0\le_W b\},
\]
ordered by the induced Bruhat order. The map \(j_V(d)=da_0\) is injective by right cancellation, so the finite ambient interval makes \(K\) finite.

If \(z\le_D d\) and \(d\in K\), the coset comparison gives
\(za_0\le_W da_0\le_W b\), hence \(z\in K\). Thus \(K\) is a finite relative lower ideal. A relative reflection edge maps to the ambient edge with endpoints multiplied on the right by \(a_0\).

For an ambient edge starting at \(da_0\), with reflection label \(\tau\in D_P\), its target is
\[
\tau da_0=(\tau d)a_0.
\]
That target lies below \(b\), so \(\tau d\) is another vertex of \(K\). The [[node:kl.dihedral.plane_coset_graph|coset reflection-step equivalence]] gives the edge \(d\to_D\tau d\). This constructs every required outgoing lift.

## The localized coset sheaf and relative flabbiness

Write \(R_P=A_{\mathfrak p_P}\). For an ambient sheaf \(C\), the localized coset sheaf is
\[
\mathcal C=j^*(R_P\otimes_A C),
\qquad
\mathcal C^d=R_P\otimes_A C^{da_0}.
\]
Its edge labels are the ambient polynomial root labels mapped into \(R_P\). The induced and ambient positive roots agree because both correspond to the reflection
\[
(ca_0)(da_0)^{-1}=cd^{-1}.
\]

The [[node:kl.local.plane_prime_membership|plane-prime unit criterion]] identifies the surviving label set as
\[
L=\{e:\tau_e\in D_P\}.
\]
Outside \(L\), the localized upper quotient has a unit label and is zero. The coset graph map is injective on vertices and has the outgoing lifts constructed above.

The [[node:kl.sheaves.base_change_properties|scalar-extension property theorem]] gives ambient flabbiness after localization. The [[node:kl.sheaves.pullback_live_flabbiness|surviving-edge pullback theorem]] then gives flabbiness for relative upper subsets of \(K\): their images are closed under \(L\), their sections push compatibly to those images, and relative extension supplies the global section to pull back.

Generation follows by restricting tensor-extended generating sections. Free stalks, finite generation and upper quotients follow from the displayed tensor stalks and the pullback restrictions. The [[node:kl.local.localized_coset_properties|localized coset properties theorem]] checks each of these inputs.

## Selected conditions through both operations

Let \(T\) be any set of ambient edges. At a relative vertex \(d\),
\[
K_d^{\mathcal C}(j_E^{-1}(T))
=K_{da_0}^{C_{R_P}}(T)
=\bigl(K_{da_0}^C(T)\bigr)_{R_P}.
\]
The first equality uses outgoing lifts and zero edge modules; the second uses flat extension of the selected constraint kernel.

Applying either endpoint restriction of a relative edge carries this equality into the same edge module \(R_P\otimes_A C^{j_E(a)}\). The [[node:kl.algebra.flat_embedded_modules|embedded-image identity]] identifies its image with the scalar extension of the original edge image. The [[node:kl.local.localized_coset_kernels|localized coset kernel-and-image theorem]] therefore places the actual comparison submodules in the coordinates used by the later model decomposition.

## Induced dihedral structure models

Let \(H\) be a two-generator Coxeter system and let \(\phi:H\to W\) be a homomorphism carrying reflections to ambient reflections. On \([1,b]_H\), label an edge \(e:x\to y\) by the polynomial of the canonical positive ambient root representing \(\phi(yx^{-1})\). These are the induced polynomial labels.

For \(c\le_Hb\), the structure model \(\mathcal O_c\) has stalk \(A\) below \(c\), zero outside that lower ideal, and edge quotient \(A/(\alpha_e)\) whenever the upper endpoint is below \(c\). Constant assignments on the lower support prove generation. The quotient restrictions and finite free stalks follow directly from this construction.

The flabbiness proof assumes \(\phi\) is injective. It constructs global sections with precisely controlled lower support, then uses them to extend arbitrary prescribed sections on upper sets.

## Parity matching and orbit-spline factors

For \(x\le_Hc\), the external lower vertices are
\[
E(x,c)=\{z:z\le_Hc,\ z\not\le_Hx\}.
\]
Let \(Y\) be those of opposite length parity to \(x\), and \(Z\) those of the same parity. The general [[node:kl.coxeter.lower_interval_parity|lower-interval parity theorem]] gives an injection \(j:Z\hookrightarrow Y\). Its proof pairs lower-interval vertices by a simple left descent and then subtracts the two lower ideals.

For an ambient reference vertex \(y\) and vector \(v_0\) in the extended realization, the orbit spline is
\[
F_{y,v_0}(w)=\Lambda(\rho(wy^{-1})v_0-v_0).
\]
It vanishes at \(y\). Across a reflection \(t\) represented by a root \(a\), its difference is
\[
F_{y,v_0}(w)-F_{y,v_0}(tw)
=\widetilde B(i_0a,\rho(wy^{-1})v_0)\lambda(a),
\]
so it satisfies the edge congruence.

For each \(y\in Y\), choose one such factor with reference vertex \(\phi(y)\) and value \(\lambda(a_y)\) at \(\phi(x)\). If \(y=j(z)\), prescribe an additional zero at \(\phi(z)\). The two normal forms are independent, so the [[node:kl.local.orbit_spline_factors|orbit-spline factor theorem]] supplies a vector with normal values \((-1,0)\). Injectivity of \(j\) gives at most one additional zero to prescribe for each factor.

The product of these factors has value \(\prod_{y\in Y}\lambda(a_y)\) at \(x\), and vanishes at every external vertex. Congruences persist because reduction modulo an edge label preserves products.

## The exact outgoing product and a flow-down section

In a dihedral system, the opposite-parity external vertices are exactly the outgoing neighbors \(y\) of \(x\) with \(y\le_Hc\). The target map and \(y\mapsto(x,y)\) form a bijection, and both label definitions choose the positive ambient root of \(\phi(yx^{-1})\). Thus
\[
\prod_{y\in Y(x,c)}\lambda(a_y)
=\prod_{e\in\operatorname{Out}_c(x)}\alpha_e=P_c(x).
\]

Restrict the interpolating function to the model stalks, using zero outside their lower support. The [[node:kl.local.induced_flow_down|induced flow-down theorem]] gives a global section \(\theta_x\) with
\[
\theta_x(x)=P_c(x),\qquad
\theta_x(y)=0\quad(y\not\le_Hx).
\]
This is the flow-down property used in the extension step.

For a worked example in type \(A_2\), take \(H=W\), \(\phi=\operatorname{id}\) and \(x=s,\ c=st\). Identify the simple roots \(a,b\) with their embedded vectors, normalized by \(\widetilde B(a,a)=\widetilde B(b,b)=2\) and \(\widetilde B(a,b)=-1\), and write \(\alpha=\Lambda(a)\), \(\beta=\Lambda(b)\). The external matching sends \(t\) to \(st\). The orbit vector
\[
v_0=-\tfrac13a-\tfrac23b
\]
has normal values zero on \(a\) and minus one on \(a+b\). With reference vertex \(st\), it gives the section

| Vertex | Value |
|---|---|
| \(1\) | \(\beta\) |
| \(s\) | \(\alpha+\beta\) |
| \(t\) | \(0\) |
| \(st\) | \(0\) |

The value at \(s\) is its supported outgoing label \(\alpha+\beta\), and the support lies below \(s\). The [[node:kl.local.dihedral_interpolation|full interpolation proof]] checks all four edge congruences.

## Correcting one remaining prescribed value

Let \(U\) be a finite upper set with a compatible assignment \(f\), and choose a minimal \(x\in U\). First extend the prescription on \(U\setminus\{x\}\) by induction, obtaining a global section \(g\).

For every supported outgoing edge \(x\to y\), the upper endpoint already has \(f_y=g_y\). Subtracting the two compatibility equations gives
\[
\alpha_e\mid f_x-g_x.
\]
Distinct induced labels at a fixed source are relatively prime: divisibility of their linear polynomials would identify their positive roots, then their reflections under the injective \(\phi\), and finally the edge itself. Therefore
\[
f_x-g_x=P_c(x)r
\]
for some scalar \(r\).

The correction \(g+r\theta_x\) is global and has the desired value at \(x\). Every other vertex of \(U\) lies outside the lower ideal of the chosen minimal vertex \(x\), so the flow-down section vanishes there and preserves all other prescribed values. If \(x\) is outside the model support, its stalk is already zero.

In the \(A_2\) example, an error \(r(\alpha+\beta)\) at \(s\) is corrected by adding \(r\theta_s\), while the values at \(t,st\) stay fixed. The [[node:kl.local.flow_down_flabbiness|flow-down flabbiness theorem]] gives this induction in general.

For the actual plane subgroup, its inclusion into \(W\) is injective and sends intrinsic reflections to ambient reflections. The [[node:kl.detail.dihedral_model_properties|dihedral model theorem]] therefore supplies the required model flabbiness, generation and upper quotients.

## Scalar extension retains the model maps

Let \(A\to R_P\) be the localization map \(\eta_P\). At a supported model stalk, the scalar-extension coordinate is
\[
R_P\otimes_AA\longrightarrow R_P,\qquad
r\otimes f\longmapsto r\eta_P(f).
\]
At a supported edge it is
\[
R_P\otimes_AA/(\alpha_e)\longrightarrow R_P/(\eta_P(\alpha_e)),
\qquad r\otimes[f]\longmapsto[r\eta_P(f)].
\]
For either endpoint restriction, both routes send \(r\otimes f\) to the same quotient class. Outside the support the edge modules are zero. The [[node:kl.local.structure_model_transport|structure-model transport theorem]] therefore identifies the tensor-extended sheaf with the structure sheaf using the localized labels.

Flatness transfers flabbiness on the finite graph. Each localized interval-model label belongs to the maximal ideal because its representing root lies in the plane. The [[node:kl.local.local_structure_models|local structure-model theorem]] packages these facts with the finite free stalks, quotient maps, generation and local minimality.

## A principal interval containing the relative coset graph

The finite relative lower ideal \(K\) may have several maximal vertices. The [[node:kl.dihedral.finite_common_upper|finite-common-upper-bound theorem]] supplies \(d_0\in D\) above every element of \(K\), giving an inclusion
\[
f:K\hookrightarrow[1,d_0]_D.
\]
This inclusion uses the same intrinsic order on both sides.

For a fixed center \(c\in K\), consider the localized interval structure model centered at \(f(c)\). Its supported edges have target below \(c\). If such an edge starts at a vertex of \(K\), its target also belongs to \(K\), because \(K\) is a relative lower ideal. This gives every supported outgoing lift needed for the [[node:kl.sheaves.pullback_live_flabbiness|surviving-edge pullback theorem]].

The label comparison is exact. An edge with relative endpoints \(x,y\) has ambient endpoints \(xa_0,ya_0\), and
\[
(ya_0)(xa_0)^{-1}=yx^{-1}.
\]
Both constructions therefore choose the same canonical positive ambient root. The [[node:kl.local.structure_model_transport|structure-model transport theorem]] identifies the pulled-back interval model with the actual structure model on \(K\). The [[node:kl.local.coset_structure_models|coset structure-model theorem]] proves its flabbiness and assembles the local-model data.

## Selected products describe the stalk kernels

Choose a model center \(c\), a vertex \(x\), and a subset \(F\) of its outgoing edges. The supported selected edge set and selected model product are
\[
F_c(x)=\{e\in F:t(e)\le_Dc\},\qquad
p_{c,x}(F)=\prod_{e\in F_c(x)}\gamma_e.
\]
For \(x\le_Dc\), the stalk is \(R_P\), and the selected equations are
\[
[v]=0\text{ in }R_P/(\gamma_e)
\quad(e\in F_c(x)).
\]
Equivalently each \(\gamma_e\) divides \(v\). Unsupported edge modules contribute no equation.

Distinct labels at a fixed source are relatively prime. To see this, first work in the polynomial ring: divisibility between two prime linear labels identifies their positive roots, then their reflections, then their edges at the fixed source. Localization preserves their relative primality. If a prime factor is outside the localization prime it becomes a unit; if it lies inside, clearing a denominator preserves the nondivisibility.

The [[node:kl.local.structure_kernel_products|structure-kernel product theorem]] combines the individual divisibilities:
\[
K_x^{\mathcal O_c}(F)=p_{c,x}(F)\mathcal O_c^x.
\]
For two supported selected labels \(a,b\), this is the elementary calculation
\((a)\cap(b)=(ab)\) under relative primality. For an empty supported selection the product is \(1\), so the kernel is the whole stalk. Outside the model support both sides are zero.

## The products inside the edge module

Now fix an edge \(e:x\to y\). The [[node:kl.local.structure_edge_images|structure edge-image theorem]] gives
\[
\rho^-_e(K_x(F))=p_{c,x}(F)\mathcal O_c^e,\qquad
\rho^+_e(K_y(H))=p_{c,y}(H)\mathcal O_c^e.
\]
The proof uses \(f(pM)=p\,f(M)\) for a linear map \(f\), together with surjectivity of each endpoint restriction. Upper surjectivity is the quotient rule. For lower surjectivity, lift an edge value at its upper endpoint and extend that stalk value to a global section; compatibility supplies its lower preimage.

In a single supported edge \(x\to c\) labelled by \(\alpha\), selecting that edge gives stalk kernel \(\alpha R_P\). Its image in the edge quotient is
\[
\alpha\bigl(R_P/(\alpha)\bigr)=0.
\]
At the upper endpoint an empty outgoing selection gives the full edge image. The [[node:kl.local.coset_kernel_products|coset kernel-product theorem]] proves the general formulas for arbitrary selections in the actual localized graph.

## Local model data and finite sums

A family of local boundary models has finite free stalks, upper quotient maps, generation, flabbiness and support below its center. Its top stalk comes with a chosen coordinate \(O_c^c\simeq R_P\). At a proper supported vertex \(x\ne c\), local minimality says
\[
\ker d_x\subseteq\mathfrak m_P O_c^x,
\]
where \(d_x\) collects all outgoing restrictions. Thus the surjection from the stalk onto its outgoing image becomes an isomorphism after reduction modulo \(\mathfrak m_P\).

An ungraded model sum adds finitely many copies of these models. For a one-edge graph \(x<c\), the sum \(O_c^2\oplus O_x^3\) has stalk ranks \(5\) at \(x\) and \(2\) at \(c\), with edge module \((R_P/(\alpha))^2\). Adding the three \(O_x\)-copies changes the lower stalk while preserving the data above it.

The local decomposition produces an actual sheaf isomorphism to such a sum. The selected kernel and edge-image formulas then apply componentwise. They turn the comparison into scalar products in each common model edge module; the root-plane count determines the correction between those products.

## The common outgoing image at the next vertex

Let \(B\) be the sheaf being decomposed and \(C\) the sum of models already added. Suppose their partial isomorphism is defined on an upper set \(U\), and \(x\notin U\) has every vertex above it in \(U\).

The old edge maps give an isomorphism \(J\) between the products of outgoing edge modules at \(x\). A section above \(x\) transports through the old vertex maps; the restriction squares show that its boundary value transports through \(J\). Applying the inverse maps proves the reverse containment of boundary images.

Generation and flabbiness identify those boundary images with the images of the outgoing stalk maps. The [[node:kl.sheaves.boundary_image_transport|boundary-image transport theorem]] therefore gives
\[
J(\operatorname{im}d_x^B)=\operatorname{im}d_x^C=:N.
\]
There are now two actual surjections to the same module:
\[
\pi:C^x\to N,\quad c\mapsto d_x^C(c),\qquad
\varphi:B^x\to N,\quad b\mapsto J(d_x^B(b)).
\]

Every center of \(C\) lies in \(U\), so none equals \(x\). The [[node:kl.local.model_sum_properties|model-sum properties theorem]] gives
\[
\ker\pi\subseteq\mathfrak m C^x.
\]
Thus \(\pi\) is a local minimal free cover of \(N\).

## One lift, Nakayama and an explicit splitting

Write \(P=C^x\). Freeness of \(B^x\) lets us choose preimages under \(\pi\) of the images of its basis vectors. Extending linearly gives
\[
g:B^x\to P,\qquad \pi g=\varphi.
\]
For any \(p\in P\), choose \(b\) with \(\varphi(b)=\pi(p)\). Then
\(g(b)-p\in\ker\pi\subseteq\mathfrak mP\). Hence \(g\) is onto modulo \(\mathfrak m\).

The finite cokernel \(Q_0=P/\operatorname{im}g\) satisfies \(Q_0=\mathfrak mQ_0\). The [[node:kl.local.cover_lift_surjectivity|local lift-surjectivity theorem]] gives the Nakayama calculation: on a finite generating family this becomes \((I-A)q=0\) with all entries of \(A\) in \(\mathfrak m\). The determinant is congruent to \(1\), hence a unit, so every generator vanishes. Thus \(g\) is onto.

Because \(P\) is free, choose a section \(s:P\to B^x\) with \(gs=1\). The splitting is
\[
b\longmapsto(gb,b-sgb),\qquad
(p,q)\longmapsto sp+q.
\]
The second factor is \(Q=\ker g\). It is finite as the image of the complementary projection and projective as a direct summand of \(B^x\). The [[node:kl.local.cover_splitting|local cover-splitting theorem]] explains its freeness over the local ring by lifting a residue-field basis and applying Nakayama to the complementary kernel.

The [[node:kl.local.stalk_splitting|local stalk-splitting theorem]] then evaluates \(\pi((e_xb)_1)=\varphi(b)\) at each outgoing edge. This gives every required outgoing restriction equality.

## Adding models without changing the processed data

Choose a basis of \(Q\), of size \(n\). The top coordinate \(O_x^x\simeq R\) identifies \(Q\) with the stalk at \(x\) of \(n\) copies of \(O_x\).

For \(y\in U\), the relation \(y\le x\) would imply \(x\in U\). Thus each added \(O_x\) has zero stalk at \(y\). An edge whose target is in \(U\) also has zero added edge module, because its upper quotient comes from a zero stalk. The old isomorphism therefore extends on \(U\) by adjoining zero components.

At outgoing edges from \(x\), the old component commutes by the stalk-splitting equality, and the added component has zero edge module. At an incoming edge \(e:z\to x\), the new stalk isomorphism takes \(\alpha_eB^x\) onto \(\alpha_e(C\oplus O_x^n)^x\), so it induces the edge isomorphism on the upper quotients.

The [[node:kl.local.model_sum_step|one-vertex model-sum extension theorem]] assembles these maps into a partial isomorphism on \(U\cup\{x\}\).

## A two-vertex decomposition with explicit coordinates

Let \(R=k[t]_{(t)}\) over a field \(k\), and use one edge \(x\to c\), labelled by \(t\). Take a sheaf with
\[
B^x=R^2,\qquad B^c=R,\qquad B^e=R/(t),
\]
and restrictions
\[
\rho^-_e(u,v)=[u],\qquad \rho^+_e(z)=[z].
\]
It is generated: any lower value \((u,v)\) extends by choosing \(z=u\), and any upper value \(z\) extends by choosing \((u,v)=(z,0)\). The latter also extends every section on the only nontrivial proper upper set \(\{c\}\), proving flabbiness. The upper quotient has kernel \(tR\).

First process \(c\). Its rank-one stalk adds one copy of \(O_c\). At \(x\), the two covers of the outgoing image are
\[
\pi:R\to R/(t),\quad p\mapsto[p],\qquad
\varphi:R^2\to R/(t),\quad(u,v)\mapsto[u].
\]
Choose \(g(u,v)=u+tv\) and \(s(p)=(p,0)\). The kernel has basis \((-t,1)\), so one copy of \(O_x\) fills it. The resulting lower-stalk isomorphism is
\[
(u,v)\longmapsto(u+tv,v).
\]
At the upper stalk and edge module use the identity maps. The lower square commutes because \([u+tv]=[u]\). Hence this construction gives
\[
B\simeq O_c\oplus O_x
\]
with the actual edge restrictions preserved.

## Finite descent and the localized application

The [[node:kl.local.model_decomposition|local model-decomposition theorem]] maintains the processed upper set \(U\) and chooses a maximal vertex \(x\) of its finite complement. Every vertex above \(x\) is already processed. The preceding step removes \(x\) from that complement, so induction terminates.

The initial processed set is empty, with the zero model sum and vacuous partial isomorphism. At the end every vertex is processed; the partial isomorphism includes every edge and is a full sheaf isomorphism.

For the actual localized boundary sheaf, the coset vertex set is finite, its stalks are finite free tensors over \(R_P\), and the localized-coset properties supply the upper quotients, generation and flabbiness. The coset models supply every local-model field. The [[node:kl.local.localized_decomposition|localized decomposition theorem]] applies the generic finite descent to exactly these objects.

## Root-plane counts and the scalar correction

Now reduce the illustrative localized ring modulo the current edge label \(\alpha\). A plane label \(\beta+c\alpha\) becomes \(\beta\). More generally, any nonparallel plane root has a nonzero real multiple of \(\beta\) as its reduction. Such factors differ by units.

Labels outside the plane become units. Therefore a product of relevant reduced labels is, up to a unit, a power of \(\beta\). Comparing the two model images reduces to comparing these exponents.

The transported later-edge count theorem supplies the difference of exponents. The factor \(f_e\) was constructed to account for that difference. This yields the required image comparison after localization at each relevant root-plane prime. The proof also treats the primes at which the relevant root factors are units.

This computation uses the actual labels and maps. Its conclusion concerns where the lower image sits in the common edge module.

## Recover global membership using the free target

Let \(M=f_eJ_e\), viewed as a free submodule of the torsion-free edge module \(E=B^e\) over \(C\). The hypotheses in the global membership theorem include the required generic span. In this application, products of the remaining labels kill all their edge conditions; their nonzero reductions provide multiples of the ambient module inside the relevant image, giving that generic span.

To understand the membership theorem, choose a basis \(m_1,\ldots,m_r\) of \(M\). Over the fraction field, a candidate vector has coordinates \(a_i\):
\[
z=\sum_i a_i m_i.
\]
Membership in \(M\) means that all \(a_i\) belong to \(C\), without denominators.

The theorem tests this at every height-one prime. Here height one means that there is no prime ideal strictly between the zero ideal and that nonzero prime. A polynomial ring is a unique factorization domain (UFD): every nonzero nonunit factors into irreducibles, uniquely up to order and units. Its height-one primes are generated by those irreducible factors.

If a reduced denominator of \(a_i\) contained a factor \(p\), then \(a_i\) could not lie in \(C_{(p)}\): that localization does not invert \(p\). Local membership at every such prime therefore removes every denominator. The formal proof carries this out by dividing in free-basis coordinates and cancelling in the torsion-free ambient module.

Apply this argument to each element of \(I_e\), using the local comparisons from the preceding steps. We obtain \(I_e\subseteq f_eJ_e\) globally.

## The image inclusion and its Hilbert defect

Consider \(C=\mathbb R[\beta,\gamma]\) and \(I=(\beta,\gamma)\subset C\). At every height-one prime, at least one of \(\beta,\gamma\) is invertible, so \(I\) localizes to the whole ring. Nevertheless \(I\ne C\), since \(1\notin I\).

The free-target membership theorem supplies the inclusion used in comparison. The quotient in this example is the constant component, which the Hilbert value measures.

The example also shows why equal rank is insufficient. Both \(I\) and \(C\) have rank one, but their quotient is the one-dimensional space of constants. Their Hilbert values differ:
\[
H_C(q)=\frac1{(1-q)^2},\qquad H_I(q)=\frac1{(1-q)^2}-1.
\]
Hilbert comparison detects that positive deficit. It first uses the inclusion proved here to obtain an inequality, and only later forces equality through exact endpoints.

The logical order to retain is: free upper kernel, free edge target, local model calculation, global inclusion, and then the separate Hilbert argument.


## Definitions and proofs by construction

### Plane and edge localizations

- [[node:kl.algebra.edge_coefficient_ring]]
- [[node:kl.algebra.root_quotient_coordinates]]
- [[node:kl.detail.localization_rings]]
- [[node:kl.local.plane_prime_membership]]
- [[node:kl.algebra.tensor_scalar_quotient]]
- [[node:kl.local.localized_edge_ring]]
- [[node:kl.algebra.plane_reduction]]
- [[node:kl.local.localized_root_reduction]]
- [[node:kl.local.localized_relative_primality]]

### Localizing graph sheaves

- [[node:kl.detail.base_change]]
- [[node:kl.sheaves.section_constraints]]
- [[node:kl.sheaves.flat_section_base_change]]
- [[node:kl.sheaves.base_change_properties]]
- [[node:kl.algebra.flat_embedded_modules]]
- [[node:kl.notes.sheaf_localization]]
- [[node:kl.sheaves.pullback_live_flabbiness]]
- [[node:kl.sheaves.pullback_selected_kernels]]
- [[node:kl.local.coset_graph]]
- [[node:kl.local.coset_outgoing_lifts]]
- [[node:kl.local.localized_coset]]
- [[node:kl.local.localized_coset_properties]]
- [[node:kl.local.localized_coset_kernels]]

### Dihedral structure models

- [[node:kl.detail.structure_sheaves]]
- [[node:kl.local.structure_sheaf_properties]]
- [[node:kl.notes.dihedral_models]]
- [[node:kl.local.orbit_splines]]
- [[node:kl.local.orbit_spline_congruence]]
- [[node:kl.local.orbit_spline_factors]]
- [[node:kl.local.dihedral_interpolation]]
- [[node:kl.local.flow_down]]
- [[node:kl.local.induced_flow_down]]
- [[node:kl.local.induced_label_primes]]
- [[node:kl.local.flow_down_flabbiness]]
- [[node:kl.detail.dihedral_model_properties]]
- [[node:kl.local.structure_model_transport]]
- [[node:kl.local.local_structure_models]]
- [[node:kl.local.coset_structure_models]]
- [[node:kl.local.selected_model_product]]
- [[node:kl.local.structure_kernel_products]]
- [[node:kl.local.structure_edge_images]]
- [[node:kl.local.coset_kernel_products]]

### Local model decomposition

- [[node:kl.local.minimal_covers]]
- [[node:kl.local.cover_lift_surjectivity]]
- [[node:kl.local.cover_splitting]]
- [[node:kl.detail.local_models]]
- [[node:kl.local.model_sums]]
- [[node:kl.local.model_sum_properties]]
- [[node:kl.local.stalk_splitting]]
- [[node:kl.local.model_sum_step]]
- [[node:kl.local.model_decomposition]]
- [[node:kl.local.localized_decomposition]]

### Polynomial correction factors

- [[node:kl.detail.edge_factor]]
- [[node:kl.paths.plane_degree]]

### Embedded lower and upper images

- [[node:kl.detail.edge_images]]
- [[node:kl.detail.scaled_images]]
- [[node:kl.notes.upper_image_free]]
- [[node:kl.detail.quotient_image_free]]

### From local comparison to the global edge inclusion

- [[node:kl.local.edge_inclusion]]
- [[node:kl.local.free_target_localization]]
