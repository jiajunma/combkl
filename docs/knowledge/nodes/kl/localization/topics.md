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

## Reduce the local calculation to a dihedral model

The finite relative coset graph now carries the localized boundary sheaf with its established free stalks, generation, flabbiness and upper quotients.

The local model-decomposition theorem identifies it with a finite sum of dihedral structure models. In a structure model the supported stalks are copies of the local ring and restrictions are quotient maps. The interpolation theorem proves the required extension properties for the actual induced labels.

For a rank-one stalk \(R\) with outgoing labels \(\lambda_1,\ldots,\lambda_m\), the full vanishing condition is
\[
r\in(\lambda_1)\cap\cdots\cap(\lambda_m).
\]
When these labels are pairwise relatively prime in the divisibility sense, this intersection equals the product ideal \((\lambda_1\cdots\lambda_m)\): if each prime factor divides \(r\), their product divides \(r\). This is the model calculation behind the kernel-product formula.

The decomposition is an isomorphism of sheaves, so it carries these computed kernels and images through maps that commute with restrictions. An isomorphism of stalk ranks would not be enough.

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
- [[node:kl.notes.dihedral_models]]
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
