---
title: Two submodules of one edge module
primary_topic: kl.localization
---

A selected kernel consists of stalk vectors whose chosen outgoing restrictions vanish. Applying the current edge restriction at the lower or upper endpoint gives two embedded images in the same edge module. Their location in that module is part of the comparison: it determines which vector is being compared before and after multiplication by the correction scalar.

Scaled image equality means that the lower image is the correction multiple of the upper image. The generic image-transport results prove that one sheaf isomorphism carries both selected kernels and both edge images through its corresponding components. Its single linear edge component also commutes with the common scalar.

The actual local comparison proves this equality first in each structure model, then in their finite sum, and finally in the original localized boundary-sheaf edge. Global membership yields an inclusion in the unlocalized module. The [[node:kl.sheaves.hilbert_detection|positive defect theorem]] later detects whether this inclusion is an equality, which is the input to reverse recovery of freeness.

## Reading sequence

1. [[node:kl.detail.edge_images]] — Define both actual image submodules.
2. [[node:kl.detail.scaled_images]] — State equality after the scalar action.
3. [[node:kl.local.image_isomorphism_transport]] — Carry both images through one isomorphism.
4. [[node:kl.local.model_sum_scaled_images]] — Use one scalar in every summand.
5. [[node:kl.local.localized_boundary_scaled_images]] — Return to the actual localized boundary sheaf.
6. [[node:kl.local.boundary_edge_inclusion]] — Obtain the global inclusion.
7. [[node:kl.comparison.raw_edge_increment]] — Detect equality through the Hilbert defect.
