---
title: Transporting structure models to the actual plane coset
primary_topic: kl.localization
---

A structure model is supported below a chosen center: its supported stalks are copies of the coefficient ring, and its supported edge modules are quotients by the edge labels. The native dihedral construction supplies these models with flabbiness, generation and upper-quotient properties.

The actual root-plane coset graph is finite. A common-upper-bound theorem places its relative vertices inside a principal dihedral interval, where the native models are available. Scalar extension changes the polynomial coefficients to the plane ring, and graph pullback identifies the actual coset labels and restriction maps.

These transported models form the local model data used in decomposition of the localized boundary sheaf. Their supported kernel products become the concrete ideals compared at an edge. The route below follows the model definition through scalar and graph transport, then reaches the actual model family used by the main proof.

## Reading sequence

1. [[node:kl.detail.structure_sheaves]] — Define the model stalks and edge quotients.
2. [[node:kl.detail.dihedral_model_properties]] — Prove the native dihedral properties.
3. [[node:kl.dihedral.finite_common_upper]] — Place finite relative data under a common top.
4. [[node:kl.local.structure_model_transport]] — Track scalar extension and pullback maps.
5. [[node:kl.local.coset_structure_models]] — Construct the actual coset model family.
6. [[node:kl.detail.local_models]] — Read the local-model interface.
7. [[node:kl.local.coset_kernel_products]] — Use the model images in the edge calculation.
