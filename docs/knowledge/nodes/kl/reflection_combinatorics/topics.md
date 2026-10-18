# Reflection orders, dihedral combinatorics, and paths

The question is: **how can an order isomorphism, which knows no root labels, still be used in a calculation ordered by reflections?** Two distinct problems must be solved. We must recover all reflection edges from the order, and then understand what an ordered product along those edges computes.

We use the positive roots and polynomial families already constructed. A root label is geometric information attached to an edge; it is not initially part of an unlabelled interval.

## Choose an order on positive roots

Choose a linear form \(h\) positive on every simple root. Since a positive root is a nonnegative, nonzero combination of simple roots, \(h(\alpha)>0\) for every positive root \(\alpha\). Choose another functional \(f\) for which the ratios
\[
s(\alpha)=\frac{f(\alpha)}{h(\alpha)}
\]
are all distinct.

This assigns each positive root a real score. Equivalently, divide each root by \(h(\alpha)\), placing it on the affine hyperplane \(h=1\), and then evaluate \(f\).

For two independent roots in a plane, their normalized points and all other normalized roots in that plane lie on an affine line. A linear functional orders points on a line in one of its two directions. This explains the rank-two angular-order condition behind a geometric reflection order.

The generic-functional theorem proves that \(f\) can be chosen to separate the whole root set in finite generator rank. For a fixed interval only finitely many edges need to be listed, even if the group has infinitely many positive roots.

## Multiply two edge transfers by hand

For an edge \(x\to y\), let \(E_{xy}\) be the matrix with a single \(1\) in row \(x\), column \(y\). On a column vector it copies coordinate \(y\) into coordinate \(x\). Define
\[
M_{xy}=I+T E_{xy}.
\]
It leaves every coordinate unchanged except that \(T\) times the upper coordinate is added to the lower one.

On a three-vertex chain \(x\to y\to z\), expand
\[
\begin{aligned}
M_{xy}M_{yz}
&=(I+TE_{xy})(I+TE_{yz})\\
&=I+TE_{xy}+TE_{yz}+T^2E_{xz}.
\end{aligned}
\]
The last term appears because \(E_{xy}E_{yz}=E_{xz}\): the output at \(y\) of the second matrix is read by the first.

Reversing the factors gives no \(T^2E_{xz}\), since \(E_{yz}E_{xy}=0\). Thus order matters. In a general product, choose either \(I\) or the edge term from each factor. A product of edge terms survives exactly when those edges form a composable path in the written order. Its contribution is \(T^{\text{number of edges}}\).

The rightmost matrix acts first. Therefore chronological application and the written matrix-product order are reversed. This is why the code distinguishes the chronological schedule from the decreasing path order.

## An A2 path calculation

Return to \(W=\langle s,t\rangle\) with \(sts=tst=w_0\). Put \(r=sts\), the third reflection, and take the reflection order
\[
s<r<t.
\]
For decreasing labels, the paths from \(1\) to \(w_0\) are:

| Path | Left-reflection labels | Weight |
|---|---|---|
| \(1\to w_0\) | \(r\) | \(T\) |
| \(1\to t\to ts\to w_0\) | \(t,r,s\) | \(T^3\) |

For example, \(rt=ts\) and \(s(ts)=w_0\), which checks the labels in the second row. The other saturated chains have labels \(s,r,t\) along \(1,s,st,w_0\), labels \(s,t,s\) along \(1,s,ts,w_0\), and labels \(t,s,t\) along \(1,t,st,w_0\). None is decreasing. Every edge increases length by at least one, and every reflection reverses length parity. A path from length zero to length three therefore has one or three edges, so the two displayed paths exhaust the possibilities.

The decreasing path sum is \(T+T^3\). The geometric Dyer theorem identifies this path construction with the already-defined normalized R-family, giving \(\widetilde R_{1,w_0}(T)=T+T^3\).

The direct edge jumps three ranks but contributes \(T\), because path weight counts edges, not rank difference. This is a useful distinction when reading the general path formula.

## Identification of the path polynomial with the R-polynomial

The matrix expansion alone only counts ordered paths. It does not explain why the resulting polynomial is the bar coefficient from Hecke algebra and polynomial invariants.

The formal proof first constructs an adapted order for which the path polynomials satisfy the same descent recursion as the normalized R-family. Equal diagonal values, zero values outside the order, and that recursion identify the two constructions.

It then compares geometric orders. When a generic functional is varied, an ordering change can be isolated to a complete root-plane block. On a relative dihedral interval, reversing that block preserves the relevant path entry through a path involution. Joining functionals through suitable transverse choices therefore preserves the full entry.

These are substantial ingredients, proved in the linked Dyer entry. The OpenAI notes cite a general reflection-order result; the theorem followed here is the geometric-order version proved by the Lean development.

## Recover edges before transporting a schedule

An interval order isomorphism certainly preserves covers. It is not initially known to preserve the longer reflection edges, such as \(1\to w_0\).

Diamond closure starts from covers and repeatedly applies rank-two configurations visible in the order. One theorem shows that the procedure adds only genuine reflection edges; the other shows that it obtains every reflection edge. Together they identify the recovered relation with the actual reflection graph.

Now an isomorphism \(\phi\) transports each source reflection edge to a target reflection edge. We can assign it the score of that target edge and list the source edges in that order. This is the transported schedule.

Its scores come from the target realization. They need not form a geometric reflection order in the source realization. The relative-dihedral transport and counting results establish exactly the properties needed from this transported order. This avoids silently assuming that the isomorphism matches roots.

## The second output: a correction factor and its degree

Fix a source edge \(e:x\to y\) with root label \(\alpha_e\). Work in the edge coefficient ring \(A/(\alpha_e)\). Other root labels are reduced modulo \(\alpha_e\). The edge factor \(f_e\) is a product of these reduced linear factors with multiplicities determined by root-plane counts.

The geometric counting theorem proves that it is nonzero and homogeneous, with
\[
\deg f_e=\frac{\ell(y)-\ell(x)-1}{2}.
\]
For a cover this is zero. For the long edge \(1\to w_0\) in the example it is one, so the correction has degree one.

This factor and the path matrix have different jobs. localization and edge-image comparison uses the factor to compare embedded edge images. Hilbert comparison uses its degree to normalize the comparison, and uses the path matrix to recognize the accumulated result as a target R-matrix.

The chapter therefore supplies the two connections needed later: order data can transport the edge schedule, and the schedule has both an algebraic path interpretation and controlled local correction factors.


## Definitions and proofs by construction

### Geometric orders on roots

- [[node:kl.notes.reflection_order]]
- [[node:kl.detail.geometric_functional]]

### Dihedral systems inside a root plane

- [[node:kl.detail.plane_basis]]
- [[node:kl.notes.relative_dihedral_intervals]]

### Dihedral interval combinatorics

- [[node:kl.notes.relative_dihedral_transport]]
- [[node:kl.paths.later_count]]

### Reconstruction of reflection edges

- [[node:kl.detail.diamond_closure]]
- [[node:kl.detail.diamond_reconstruction]]
- [[node:kl.paths.graph_invariance]]

### Schedules and their transport

- [[node:kl.detail.transported_schedule]]

### Paths and transfer products

- [[node:kl.notes.path_product]]
- [[node:kl.paths.dyer_paths]]
- [[node:kl.comparison.positive_transfer]]
- [[node:kl.detail.transfer_properties]]

## Inversion changes by root plane

The partner involution pairs the positive root lines exchanged by one reflection. The inversion-sign calculation gives contribution zero or two for each pair. Choosing the smaller slope records one root from each contributing pair, and grouping those roots by their planes defines the plane weights. Their sum measures the excess length of an edge beyond one.

- [[node:kl.geometry.plane_weights]]
- [[node:kl.geometry.plane_weight_sum]]
