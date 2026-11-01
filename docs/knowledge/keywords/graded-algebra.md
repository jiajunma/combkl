---
title: Graded coefficients, module data and Hilbert calculations
primary_topic: kl.graded_algebra
---

A grading decomposes a vector into finitely many homogeneous components, and a homogeneous map shifts those components by a specified integer. The generic component and Hilbert lemmas are formulated for integer-indexed decompositions. The graded module data used at sheaf vertices and edges add two concrete requirements: finite generation over the coefficient algebra and zero pieces in negative degrees.

Finite homogeneous covers prove that polynomial modules have finite-dimensional pieces and convergent Hilbert values in the comparison range. Scalar quotients, saturated images and homogeneous injections then provide exact transformations of those values. The [[node:kl.algebra.shifted_image_hilbert|homogeneous image shift]] contributes \(q^d\), while the [[node:kl.algebra.saturated_image_hilbert|saturated image formula]] contributes \(1-q^d\).

These formulas supply the numerical content of the main proof's edge comparison. The polynomial denominator is removed by the state scale, and the correction degree makes the transfer coefficient uniform. The reading route begins with components and the actual module-data fields, then develops the image and Hilbert calculations used in that normalization.

## Reading sequence

1. [[node:kl.algebra.grading_components]] — Define the homogeneous pieces.
2. [[node:kl.sheaves.graded_module]] — Read all fields of the actual sheaf module data.
3. [[node:kl.algebra.component_transport]] — Track components through maps.
4. [[node:kl.detail.hilbert_values]] — Define the numerical Hilbert value.
5. [[node:kl.algebra.hilbert_convergence]] — Prove piece finiteness and convergence.
6. [[node:kl.algebra.shifted_image_hilbert]] — Compute a homogeneous image shift.
7. [[node:kl.algebra.saturated_image_hilbert]] — Compute the actual scalar-quotient image.
8. [[node:kl.comparison.normalized_kernel]] — Enter the normalized comparison.
