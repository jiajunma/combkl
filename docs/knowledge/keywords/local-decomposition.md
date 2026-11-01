---
title: The finite construction of a local model decomposition
primary_topic: kl.localization
---

Local model data specify the boundary behavior of a family of structure models. Minimal covers are the maps used to add a new stalk while preserving that boundary image. Over the local coefficient ring, the lift-surjectivity argument and an explicit splitting separate the required boundary part from an additional free kernel.

The decomposition proof processes the finite graph one vertex at a time, descending from the upper vertices. At each stage it matches the sheaf on the part already constructed, identifies the next common boundary image, and adds the model copies needed for the remaining stalk summand. The resulting vertex and edge maps form a sheaf isomorphism because they respect both endpoint restrictions.

The actual localized boundary sheaf satisfies the finite-free, upper-quotient, flabbiness and generation hypotheses of this construction. Its decomposition then permits the scaled image comparison to be checked model by model. The single edge component of the isomorphism carries both comparison images back to the original localized module.

## Reading sequence

1. [[node:kl.detail.local_models]] — Read the local model data.
2. [[node:kl.local.minimal_covers]] — Define the cover condition over a local ring.
3. [[node:kl.local.cover_lift_surjectivity]] — Prove surjectivity of the selected lift.
4. [[node:kl.local.cover_splitting]] — Construct the free splitting.
5. [[node:kl.local.model_sum_step]] — Extend the comparison by one vertex.
6. [[node:kl.local.model_decomposition]] — Complete the finite construction.
7. [[node:kl.local.localized_decomposition]] — Apply it to the actual boundary sheaf.
