# 7. Localization and embedded edge images

The central problem is an inclusion of submodules inside one edge module. For an edge \(e:x\to y\), let \(I_e\) be the image of the current lower kernel and \(J_e\) the image of the current upper kernel. The goal is
\[
I_e\subseteq f_eJ_e,
\]
where \(f_e\) is the reduced-root correction factor from chapter 6.

The hypothesis is freeness of the required upper kernel at \(y\). The conclusion does not assume freeness of the current lower kernel at \(x\). This asymmetry is essential: chapter 9 obtains upper freeness from a smaller interval, and chapter 8 recovers new lower freeness only after equality has been established.

## The images and the scalar factor

Both images are defined using the actual endpoint restriction maps, with the remaining outgoing conditions imposed on their domains. The scaled-image condition compares their embeddings in the edge module. Equality of abstract ranks or an unrelated isomorphism between two free modules would not imply it.

The correction factor is a product of reduced root labels. Its nonzero value and homogeneous degree are already known. The coefficient constructions distinguish the edge quotient \(A/(\alpha_e)\), the prime localization at a root plane, and the localized edge quotient. These rings have different purposes: one removes the current edge label, while another isolates the root-plane interactions.

1. [[node:kl.detail.edge_images]]
2. [[node:kl.detail.edge_factor]]
3. [[node:kl.detail.scaled_images]]
4. [[node:kl.detail.localization_rings]]

## Local models and localization

In the rank-one structure model on a dihedral interval, stalks are copies of the coefficient ring and the edge restrictions are literal quotient maps. The interpolation theorem proves flabbiness, generation, and the quotient properties for the actual induced labels. These properties justify using the models; they are not inferred solely from the separate dihedral KL formula.

Flat base change preserves the finite section constraints, kernels, and edge images. After localization at a root-plane prime, labels outside the plane become units and their edge quotients vanish. The surviving graph separates into relative dihedral pieces. Relative flabbiness from chapter 4 applies to the subsets closed under those surviving edges.

Over this local ring, the localized sheaf decomposes into finite sums of local dihedral models. The decomposition is a sheaf isomorphism, so it respects both endpoint restrictions. Local model calculations and transported later-edge counts can therefore compare the two images in their actual common target. A decomposition of stalk ranks alone would not carry enough information.

1. [[node:kl.notes.dihedral_models]]
2. [[node:kl.detail.dihedral_model_properties]]
3. [[node:kl.detail.base_change]]
4. [[node:kl.detail.local_models]]
5. [[node:kl.notes.sheaf_localization]]
6. [[node:kl.local.localized_decomposition]]

## The free target and global membership

The local calculations must be converted into global membership. Upper-kernel freeness first descends to a free target over the edge quotient through the saturated-image theorem and the upper-image result. This supplies the ambient free module in which height-one membership can be tested.

The membership theorem uses that freeness to remove denominators coordinate by coordinate. The local comparisons at the relevant root-plane primes, together with the behavior of invertible factors elsewhere, give the required memberships. Applying the theorem in the common free target proves the global edge-image inclusion.

The order of these steps matters: construct and identify the free target, establish the localized image comparisons through compatible sheaf maps, and then recover global inclusion. The conclusion is an inclusion; equality will be forced later by the endpoint and Hilbert arguments.

1. [[node:kl.detail.quotient_image_free]]
2. [[node:kl.notes.upper_image_free]]
3. [[node:kl.local.free_target_localization]]
4. [[node:kl.local.edge_inclusion]]

## How later chapters use these results

Chapter 8 applies Hilbert values to this inclusion and combines it with the exact sequence for adding one edge condition. The degree of \(f_e\) turns the result into a uniform positive transfer inequality. Chapter 9 verifies the upper-freeness hypothesis at each edge by restricting to a strictly smaller upper interval.

The chapter's single main output is therefore [[node:kl.local.edge_inclusion]], with every hypothesis needed by that later induction stated explicitly.
