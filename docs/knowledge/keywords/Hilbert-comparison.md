---
title: From selected kernels to the normalized one-edge comparison
primary_topic: kl.invariance
---

The kernel Hilbert value records the dimensions of the actual homogeneous pieces of a selected kernel. The source sums over integer degrees. Its sheaf module data require negative pieces to vanish, so these sheaf values also equal their sums over nonnegative degrees. The generic Hilbert-module lemmas are stated on broader integer gradings.

Adding one outgoing condition gives an exact sequence whose quotient is the actual lower edge image. This identifies the change of Hilbert value. At the upper endpoint, regularity of the current label gives saturation, and the [[node:kl.algebra.saturated_image_hilbert|saturated image formula]] contributes \(1-q\). The [[node:kl.algebra.shifted_image_hilbert|homogeneous image shift]] contributes \(q^k\) for a correction of degree \(k\). An embedded image inclusion therefore becomes a numerical inequality.

For a vertex \(x\) in an interval with top \(b\), let \(\ell\) denote Coxeter length. The state scale is
\[
s_x(t)=(1-t^2)^N t^{\ell(x)-\ell(b)},\qquad q=t^2,\quad 0<t<1,
\]
with \(N\) the number of coefficient variables. The degree identity for the edge changes the coefficient to the uniform positive value \(t^{-1}-t\).

Finally, equality at one chosen positive parameter forces equality of the two images: each degree contributes a nonnegative dimension deficit with a positive weight. This turns exact numerical endpoints into the module equalities needed for reverse recovery of freeness.

## Reading sequence

1. [[node:kl.comparison.normalized_kernel]] — Define the values and state scale.
2. [[node:kl.detail.kernel_exact_sequence]] — Identify the actual one-condition increment.
3. [[node:kl.algebra.saturated_image_hilbert]] — Derive the scalar-quotient factor.
4. [[node:kl.algebra.shifted_image_hilbert]] — Derive the homogeneous degree factor.
5. [[node:kl.comparison.raw_edge_increment]] — Prove the bound and image-equality criterion.
6. [[node:kl.comparison.edge_normalization]] — Compute the uniform coefficient.
7. [[node:kl.comparison.edge_increment]] — Read the complete normalized step.
