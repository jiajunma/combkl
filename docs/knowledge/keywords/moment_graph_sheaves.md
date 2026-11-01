---
title: Graph sheaves, selected kernels and the boundary construction
primary_topic: kl.sheaves
---

An ordered graph records vertices and upward edges. A module-valued sheaf assigns a module to each vertex and edge, with a restriction map from each endpoint. In the graded construction these modules are finite graded module data with zero negative pieces, and the restrictions preserve degree.

A section is an assignment of stalk vectors whose two restrictions agree at every relevant edge. A selected kernel imposes vanishing along a chosen set of outgoing edges. Flabbiness is an extension property for compatible sections, while a minimal free cover supplies the next stalk from its boundary image. These definitions organize the construction of the normalized boundary sheaf.

The boundary sheaf supplies the actual modules used throughout the invariance proof. Its upper quotient identifies edge modules, its graded structure gives Hilbert values, and its localization admits a decomposition into dihedral structure models. The proof compares images of selected kernels inside those same edge modules and later recovers their freeness.

## Reading sequence

1. [[node:kl.detail.ordered_graph]] — Define vertices, edges and order.
2. [[node:kl.sheaves.graph_sheaf]] — Define the module and restriction data.
3. [[node:kl.sheaves.graded_module]] — Read the grading and finiteness fields.
4. [[node:kl.sheaves.upward_kernel]] — Define the selected equations.
5. [[node:kl.sheaves.flabbiness]] — Specify section extension.
6. [[node:kl.sheaves.minimal_cover]] — Introduce the stalk construction.
7. [[node:kl.sheaves.boundary_sheaf]] — Assemble the boundary sheaf.
8. [[node:kl.local.localized_decomposition]] — See its role after localization.
