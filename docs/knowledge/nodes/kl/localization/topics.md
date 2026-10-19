# Localization and comparison of embedded images

The question is: **how do local rank-two calculations imply an inclusion between actual submodules in a larger graph?** We will compare two images in the same edge module. Before considering localization, identify those images and the hypothesis that makes one of them manageable.

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
Thus \(\gamma\) becomes a unit, while \(\alpha\) and \(\beta\) remain nonunits. We have not inverted every nonzero polynomial, so this ring is not the full fraction field.

An edge labelled by \(\gamma\) now has zero edge quotient: every element is a multiple of a unit, so
\[
A_{\mathfrak p}/(\gamma)=0.
\]
An edge labelled by a linear combination of \(\alpha,\beta\) can still impose a condition. This is the algebraic reason localization at a root-plane prime leaves only the edges belonging to that plane.

Tensoring a module with \(A_{\mathfrak p}\) implements localization. It is flat, so it preserves kernels of the finite systems of section equations and the exact sequences used here. The base-change theorem proves this for the actual sheaf maps.

## Reduce the local calculation to a dihedral model

The surviving reflection edges lie in cosets of the plane reflection subgroup. Its relative graph is dihedral. The localized sheaf on such a piece is flabby and globally generated, with free stalks and the upper quotient rule.

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

- [[node:kl.local.plane_prime_membership]]

- [[node:kl.detail.localization_rings]]

### Localizing graph sheaves

- [[node:kl.notes.sheaf_localization]]

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
