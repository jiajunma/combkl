# 4. Moment-graph sheaves and minimal extensions

The task is to construct and control the sheaf objects on which the later comparisons act. An ordered graph with polynomial edge labels is the input. The chapter builds its normalized minimal-boundary sheaf, proves uniqueness with the actual restriction maps included, and establishes the morphism and decomposition results needed to isolate it inside larger sheaves.

The algebra from chapter 3 supplies graded modules and minimal free covers. Freeness, generation, flabbiness, and the upper quotient rule are separate conditions; the construction and later theorems verify the particular conditions they require.

## Objects and their sections

A graph sheaf assigns a module to every vertex and edge, together with two restrictions to each edge module. Compatible sections impose equality of the two restricted values. Global generation means sections can realize any prescribed stalk value; flabbiness means compatible data on an upper set extend to global sections.

Graph maps and sheaf isomorphisms distinguish two ways of transporting this information. A graph map reindexes the data while preserving incidence. A sheaf isomorphism identifies both stalks and edges through commuting restriction squares. These squares are essential later when two embedded edge images must be compared in the same module.

The upper quotient rule says that the upper edge map is the quotient by the edge label. Rank-one structure sheaves give concrete examples of such quotient data. Relative flabbiness strengthens the usable extension statement to subsets closed under the surviving edges, which is the form needed after root-plane localization.

1. [[node:kl.detail.ordered_graph]]
2. [[node:kl.sheaves.graph_sheaf]]
3. [[node:kl.detail.compatible_sections]]
4. [[node:kl.detail.graph_transport]]
5. [[node:kl.detail.sheaf_isomorphisms]]
6. [[node:kl.detail.graded_sheaf]]
7. [[node:kl.detail.upper_quotient]]
8. [[node:kl.detail.structure_sheaves]]
9. [[node:kl.sheaves.flabbiness]]
10. [[node:kl.sheaves.relative_flabbiness]]

## Minimal extension and uniqueness

Suppose a sheaf has already been constructed above a vertex \(x\). Sections on that upper region determine a boundary image in the product of outgoing edge modules. Choose a minimal graded free cover of this image and use it as the new stalk at \(x\). The bottom-extension theorem verifies compatibility and the required extension properties.

Repeating this step down a finite graph, starting from the normalized top stalk, proves existence of the boundary sheaf. Uniqueness is a separate downward argument: isomorphisms already constructed above \(x\) identify the boundary images, and uniqueness of minimal covers extends the stalk isomorphism to \(x\). The conclusion is an isomorphism of sheaves, not merely equality of stalk dimensions.

The upward kernels record which vectors vanish under selected outgoing conditions. They are defined now because these are the submodules later filtered by an edge schedule. Their definition does not assert that every partial kernel is free.

1. [[node:kl.notes.boundary_image]]
2. [[node:kl.sheaves.upward_kernel]]
3. [[node:kl.sheaves.boundary_sheaf]]
4. [[node:kl.detail.boundary_extension]]
5. [[node:kl.sheaves.boundary_existence]]
6. [[node:kl.detail.boundary_uniqueness]]

## Morphisms, summands, and models

Morphism extension lifts compatible maps from an upper set to the rest of the sheaf. The top-splitting theorem uses this extension mechanism and minimality to turn a split top stalk into a split sheaf summand. A split pair determines a projector, making it possible to discuss the same summand inside an ambient word sheaf.

Primitivity and indecomposability then control recognition. The normalized boundary sheaf has primitive identity. Conversely, a nonzero split summand of a sheaf with primitive identity must be the whole sheaf. Chapter 5 applies this combination to recognize the image of an adjoint projector.

For decomposition, take a boundary model at every possible top vertex. Repeated splitting removes finite blocks of shifted models until the original free, flabby, globally generated sheaf has been expressed as a finite model sum under the theorem's quotient hypotheses. One sheaf isomorphism controls all its stalk and kernel decompositions. That common origin will force the same multiplicity polynomials to occur in both character identities.

1. [[node:kl.detail.sheaf_morphism]]
2. [[node:kl.detail.split_summands]]
3. [[node:kl.detail.primitive_projectors]]
4. [[node:kl.detail.primitive_summand]]
5. [[node:kl.detail.morphism_extension]]
6. [[node:kl.detail.top_splitting]]
7. [[node:kl.detail.indecomposable_boundary]]
8. [[node:kl.detail.boundary_models]]
9. [[node:kl.detail.model_sums]]
10. [[node:kl.detail.model_decomposition]]

## How later chapters use these results

Chapter 5 applies top splitting and primitivity to the boundary summand of a tensor word, then uses model decomposition to pass from word characters to actual boundary characters. Chapter 7 uses the corresponding local-ring model construction after root-plane localization. Chapter 8 filters the upward kernels introduced here.

The chapter's output is consequently more than an existence theorem: it supplies the maps, splittings, and uniqueness statements that allow later proofs to compare actual embedded submodules.
