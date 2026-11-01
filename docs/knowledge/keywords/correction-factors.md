---
title: Geometric weights and the correction acting on an edge image
primary_topic: kl.localization
---

For an upward reflection edge with source \(x\) and positive root \(a\), the correction factor is built from geometric plane weights. These weights count contributions of root pairs to the excess length of the edge. They are nonnegative and have finite support.

For each contributing plane, the construction chooses a root independent of \(a\), reduces its linear form modulo the current label, and raises it to the plane weight. Their product is a nonzero homogeneous element of the edge quotient. The polynomial lift gives the same scalar action on the actual edge module, and the sum of the weights determines its degree.

At one plane localization, every other plane contribution becomes a unit. [[node:kl.local.coset_edge_reduction|Root-label reduction]] identifies the surviving contribution with the corresponding power of a reference root. The local count difference supplies exactly that exponent. Globally, the correction action is injective; its degree is also the input that makes the normalized Hilbert transfer coefficient uniform.

## Reading sequence

1. [[node:kl.geometry.plane_weights]] — Define the geometric exponents.
2. [[node:kl.geometry.plane_weight_sum]] — Compute their total.
3. [[node:kl.detail.edge_factor]] — Form the product in the edge quotient.
4. [[node:kl.local.edge_factor_lift]] — Lift it to polynomial coordinates.
5. [[node:kl.local.factor_plane_reduction]] — Identify its value at a plane prime.
6. [[node:kl.local.edge_factor_action_properties]] — Prove the action is graded and injective.
7. [[node:kl.comparison.edge_normalization]] — Use its degree in the uniform coefficient.
