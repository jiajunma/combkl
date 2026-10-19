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

## Model kernels and the next local comparison

At a supported rank-one stalk, selected outgoing conditions say that its scalar belongs to each ideal \((\alpha_e)\) for a supported selected edge. Pairwise relative primality makes this intersection the product ideal:
\[
K_x(F)=\left(\prod_{e\in F,\ t(e)\le c}\alpha_e\right)A.
\]
An unsupported edge has zero module and contributes no equation.

After scalar extension and restriction to a finite coset graph, the local model construction supplies the corresponding sheaf isomorphism over the local ring. Its commuting edge maps carry both selected kernel images into the same model edge modules. Those product and transport identities are the inputs to the local comparison.

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

### Local model decomposition

- [[node:kl.detail.local_models]]
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
