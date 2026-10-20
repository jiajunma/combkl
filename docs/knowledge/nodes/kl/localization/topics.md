# Localization and comparison of embedded images

This topic derives an inclusion between two submodules of the same edge module from local calculations on root-plane cosets. The argument starts with the two images, constructs a free target, compares the images after localization, and then recovers global membership.

Fix an edge \(e:x\to y\) with label \(\alpha\), and fix the outgoing conditions that remain during its scheduled step. Let \(K_x\subseteq B^x\) and \(K_y\subseteq B^y\) be the corresponding kernels. Put
\[
I_e=\rho_{x,e}(K_x),\qquad J_e=\rho_{y,e}(K_y).
\]
Both are submodules of \(B^e\). The goal is \(I_e\subseteq f_eJ_e\), where \(f_e\) is the edge factor from reflection orders and paths.

The freeness hypothesis concerns the upper kernel \(K_y\). It gives a free target for the lower-image comparison.

## The selected images and their witnesses

For an outgoing selection \(F\) at \(x\), a vector belongs to \(K_x(F)\) exactly when every restriction selected by \(F\) is zero. An edge value \(\xi\) belongs to the lower image \(I_e\) when there is a vector \(v\in K_x(F)\) with \(\rho^-_e(v)=\xi\). The upper image has the corresponding upper-stalk witnesses.

For a concrete calculation, take \(R=k[a,b]\) and two edges \(e:x\to y\), \(f:x\to z\), labelled by \(a,b\). Put \(R\) at all three vertices and use the quotient restrictions to \(R/(a)\), \(R/(b)\). Selecting only \(f\) at \(x\) gives \(K_x=bR\); an empty selection at \(y\) gives \(K_y=R\). Thus inside \(E=R/(a)\),
\[
I_e=\overline bE,\qquad J_e=E.
\]
An element \(\overline b[u]\) has lower witness \(bu\) and upper witness \(u\) after multiplication by \(b\).

For any scalar \(r\), the equality \(I_e=rJ_e\) says that every lower witness can be matched to an upper witness with the same edge value after scaling, and conversely. This is the ScaledImages proposition used in the local comparison.

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

This is the role of upper-kernel freeness in the free-target membership argument.

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

## One edge map transports both images

Let \(j:B\simeq C\) be a sheaf isomorphism over the current coefficient ring. For a selected outgoing edge \(f\) at \(x\),
\[
\rho^{C,-}_f(j_xv)=j_f(\rho^{B,-}_fv).
\]
The right side is zero exactly when the original restriction is zero, because \(j_f\) is injective. Using \(j_x^{-1}\) gives equality of the transported kernel submodules.

The same restriction squares give
\[
j_e(I_e^B)=I_e^C,\qquad j_e(J_e^B)=J_e^C.
\]
Linearity gives \(j_e(rJ)=rj_e(J)\). The [[node:kl.local.image_isomorphism_transport|image-isomorphism transport theorem]] therefore carries scaled equality to \(C\), and its inverse carries it back to \(B\). The single edge component \(j_e\) is used throughout.

For the local decomposition, this is the map from the actual localized edge module to the product of model edge modules. The scalar is the same element of the plane ring on both sides.

## A common scalar through the model sum

Suppose each model summand satisfies \(I_e^{(i)}=rJ_e^{(i)}\). A lower witness in their product gives a lower witness in every coordinate. Choose the corresponding upper witnesses and form their tuple. Selected zero restrictions hold coordinatewise, and so does
\[
r\rho^+_e((w_i)_i)=(r\rho^{i,+}_e(w_i))_i.
\]
This proves one direction of the scaled equality; choosing lower witnesses from upper ones proves the other.

The [[node:kl.local.model_sum_scaled_images|model-sum scaled-image theorem]] begins with the zero sheaf and applies this product argument at every addition of copies of a model. Thus a single correction scalar works through the full finite sum once it works for every center.

## The finite root-plane product

Fix an upward edge \(e:x\to y\) and its canonical positive root \(a\), so \(r_ax=y\). The geometric plane weights \(k_P(x,a)\) are nonnegative integers with finite support. They count the half-root representatives of contributing root pairs grouped by the plane they span with \(a\).

For each supported plane choose the source's factor representative root \(b_P\ne a\), with \(P=\operatorname{span}\{a,b_P\}\). Let
\[
S=\operatorname{Sym}_{\mathbb R}(V),\qquad
E_a=S/(\iota(i_0a)),
\]
and let \(r_P\) be the class of \(\iota(i_0b_P)\). The roots \(a,b_P\) are independent, so the quotient vector \([i_0b_P]\) is nonzero. Its symmetric generator \(r_P\) is a nonzero linear factor.

The edge factor is
\[
f_{x,a}=\prod_{P:k_P\ne0}r_P^{k_P}.
\]
The [[node:kl.local.edge_factor_properties|edge-factor properties theorem]] proves nonvanishing in the quotient polynomial domain and homogeneity of degree \(d_{x,a}=\sum_Pk_P\). These construction properties hold for all \(x\) and positive \(a\).

## Global degree and the individual plane degree

For an ascent root, the geometric weight-sum formula gives
\[
2d_{x,a}=\ell(r_ax)-\ell(x)-1.
\]
The natural-number exponents used by Lean have the same values as the nonnegative integer weights.

There is also an individual-plane identity. Choose a least representative \(a_0\) of a plane-subgroup coset and an intrinsic edge \(z\to_Dw\). If \(a\) is its actual ambient positive root, then
\[
2k_P(za_0,a)=\ell_D(w)-\ell_D(z)-1.
\]
The [[node:kl.local.factor_relative_degree|relative edge-degree theorem]] proves this by identifying the coset edge root, applying the plane inversion-change formula, and replacing the two plane inversion counts by intrinsic lengths. It identifies the code's half-root weights with the relative length formula in the notes.

For a cover, the global degree is zero, every weight is zero, and the factor is the empty product \(1\). For the long edge \(1\to sts\) in type \(A_2\), with simple roots \(a,b\) and edge root \(c=a+b\), the single plane has weight one. Its representative is one of \(a,b\). In the quotient by \(\alpha+\beta\), the factor is correspondingly \(\overline\alpha\) or \(\overline\beta=-\overline\alpha\), both of degree one.

## The same factor in polynomial and module coordinates

A basis of the extended realization gives \(\Phi:S\simeq A\), with root polynomials
\[
\lambda(b)=\Phi(\iota(i_0b)).
\]
The polynomial lift is
\[
F_{x,a}=\prod_P\lambda(b_P)^{k_P}\in A.
\]
If \(\pi_a:A\to C_a=A/(\lambda(a))\) is the polynomial quotient and \(\chi_a:C_a\simeq E_a\) is induced by \(\Phi^{-1}\), then
\[
\chi_a(\pi_a(F_{x,a}))=f_{x,a}.
\]
The [[node:kl.local.edge_factor_lift_properties|polynomial-lift properties theorem]] checks this exact equality by reducing every factor.

| Object | Module or ring | Role |
|---|---|---|
| \(f_{x,a}\) | \(E_a\), the symmetric edge quotient | The product of reduced plane roots. |
| \(F_{x,a}\) | \(A\), before quotienting | The scalar product used by the implementation. |
| \(\mu_e(v)=F_{x,a}v\) | An \(A\)-linear map on \(B^e\) | The correction action on actual edge images. |

The upper-quotient rule annihilates \(B^e\) by \(\lambda(a)\), so this action factors through \(C_a\). The [[node:kl.local.edge_factor_action_properties|edge-factor action theorem]] gives
\[
\mu_e(B^e_n)\subseteq B^e_{n+d_{x,a}}
\]
and injectivity. For the latter, lift a vector to the free upper stalk. If the factor kills its edge value, each stalk coordinate has product divisible by the prime \(\lambda(a)\). That prime divides none of the representative-root factors, so it divides every lifted coordinate. The original edge value is zero.

## One plane remains after local reduction

Fix a second positive root \(b\ne a\), put \(P=\operatorname{span}\{a,b\}\), and work in
\[
E_{P,a}=A_{\mathfrak p_P}/(\eta_P(\lambda(a))).
\]
Write \(p=r_{P,a}(b)\) for the reduced root.

For a different supported plane \(Q\), its representative \(b_Q\) lies outside \(P\). Otherwise the independent roots \(a,b_Q\) would span a two-dimensional subspace of \(P\), forcing \(Q=P\). Its localized label is consequently a unit and stays a unit in the edge quotient.

For the representative from \(P\), write \(b_P=sa+tb\), with \(t\ne0\). Reduction kills \(a\), giving
\[
r_{P,a}(b_P)=tp.
\]
The real scalar \(t\) is a unit. The [[node:kl.local.factor_plane_reduction|localized-factor theorem]] therefore gives
\[
q_{P,a}(\eta_P(F_{x,a}))\sim p^{k_P}.
\]
If \(P\) is absent from the weight support, then \(k_P=0\); all factors are units and their product is associated to \(1\).

## The actual later conditions in target coordinates

Fix the interval order isomorphism \(\varphi:[u,b]\simeq[u',b']\), the relative coset graph \(K\), and an edge \(e:x\to_Dy\) with \(u\le xa_0\). Its image edge has canonical positive target root
\[
\alpha'_e=a_{\varphi(xa_0),\varphi(ya_0)}.
\]
The target after-indicator \(\varepsilon(p,\alpha',q)\) is \(1\) exactly when \(p\to q\) is a reflection edge whose root has geometric slope strictly greater than that of \(\alpha'\).

The coset later-edge selections are
\[
F_e=\{x\to_Dz:\varepsilon(\varphi(xa_0),\alpha'_e,\varphi(za_0))=1\},
\]
\[
H_e=\{y\to_Dz:\varepsilon(\varphi(ya_0),\alpha'_e,\varphi(za_0))=1\}.
\]
Every endpoint used by \(\varphi\) belongs to its source interval: it is above \(xa_0\) and below \(b\). Both selections use the same threshold.

The current edge is excluded from \(F_e\) by strictness. Another selected lower edge with the same source root would have the same reflection and target, hence be that excluded edge. An outgoing upper edge with the current root would reflect \(y\) back to \(x\), contradicting upward length. Thus the source labels of all selected conditions survive the current root quotient.

## Supported edge sets as finite vertex sums

Fix a model center \(c\) supporting the current edge, so \(y\le_Dc\). Let \(F_{e,c}\) and \(H_{e,c}\) consist of the selected edges whose targets lie below \(c\).

The [[node:kl.local.supported_edge_count|supported-edge counting theorem]] gives, over the common relative interval \([x,c]_D\),
\[
|F_{e,c}|=\sum_{z\in[x,c]_D}
 \varepsilon(\varphi(xa_0),\alpha'_e,\varphi(za_0)),
\]
\[
|H_{e,c}|=\sum_{z\in[x,c]_D}
 \varepsilon(\varphi(ya_0),\alpha'_e,\varphi(za_0)).
\]
The bijection sends an edge to its target. Conversely, a nonzero summand supplies a target reflection edge; reflection-edge transport and the coset step equivalence recover the unique selected source edge. The support bound puts its target in the same relative interval.

The numerical difference of these two sums is the input supplied by the [[node:kl.paths.later_count|transported dihedral count theorem]]. Reindexing provides the exact connection between that numerical theorem and the selected kernels of the model.

## The common quotient for all reduced labels

Let \(a\) be the positive source root of the current edge and \(\gamma_e\) its actual label in \(R_P\). The [[node:kl.local.coset_edge_reduction|coset edge-reduction theorem]] proves the equality
\[
\gamma_e=\lambda_P(a),
\]
so its coefficient quotient is exactly \(R_P/(\lambda_P(a))\).

Choose a positive \(\beta\ne a\) spanning \(P\) with \(a\), and put
\(p=[\lambda_P(\beta)]\) in that quotient. Each selected source root lies in \(P\) and differs from \(a\), so its reduced label is associated to \(p\). The reduced correction scalar is associated to \(p^{k_P}\), by the localized-factor calculation.

These statements all use the current model edge coefficient ring. The [[node:kl.local.structure_scaled_images|structure-model scaled-image theorem]] converts them and the supported count equation into an equality in the model edge module. If the model does not support the current edge, its edge module is zero and both witness statements hold using zero vectors.

## Converting the later-edge count into equality of images

In a supported rank-one model, the lower and upper selected images are products of their selected supported labels times the same edge module. Let the two index sets have sizes \(h_x,h_y\), and suppose the reduced labels are each associated to \(p\).

Their products are then associated to \(p^{h_x}\) and \(p^{h_y}\). The factor contributes \(p^{k_P}\). When the later-edge count gives
\[
h_x=h_y+k_P,
\]
the two scalar products are associated after including the correction factor.

The [[node:kl.local.product_image_scaling|product-image scaling theorem]] converts this into equality of submodules. If two scalars differ by a unit acting on the module, their scalar images coincide; multiplication by the unit and its inverse prove the two containments. Its general formulation uses compatible scalar actions \(R\to S\), so it applies to a plane-ring module carrying the quotient coefficient action.

The remaining local comparison verifies the actual selected edge sets, their reduced labels and this count. The resulting equality is then transported through the single edge component of the model decomposition.

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

- [[node:kl.local.factor_roots]]
- [[node:kl.detail.edge_factor]]
- [[node:kl.local.edge_factor_properties]]
- [[node:kl.paths.plane_degree]]
- [[node:kl.local.factor_relative_degree]]
- [[node:kl.local.edge_factor_lift]]
- [[node:kl.local.edge_factor_lift_properties]]
- [[node:kl.local.edge_factor_action]]
- [[node:kl.local.edge_factor_action_properties]]
- [[node:kl.local.factor_plane_reduction]]

### Embedded lower and upper images

- [[node:kl.detail.edge_images]]
- [[node:kl.detail.scaled_images]]
- [[node:kl.local.image_isomorphism_transport]]
- [[node:kl.local.model_sum_scaled_images]]
- [[node:kl.local.structure_scaled_images]]
- [[node:kl.local.coset_edge_reduction]]
- [[node:kl.local.coset_later_selections]]
- [[node:kl.local.supported_edge_count]]
- [[node:kl.local.product_image_scaling]]
- [[node:kl.notes.upper_image_free]]
- [[node:kl.detail.quotient_image_free]]

### From local comparison to the global edge inclusion

- [[node:kl.local.edge_inclusion]]
- [[node:kl.local.free_target_localization]]
