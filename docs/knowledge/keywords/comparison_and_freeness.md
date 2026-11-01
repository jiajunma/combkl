---
title: Positive transfers, exact endpoints and recovered free kernels
primary_topic: kl.invariance
---

An elementary transfer adds a positive multiple of the upper vertex coordinate to the lower one. It preserves coordinatewise inequalities, and its distinct endpoints make the update injective. The [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] bounds an actual state change by this transfer when the required image inclusion has been established.

Freeness of the upper selected kernel at every chronological suffix supplies the required inclusions through the global edge theorem. Iteration along the chronological list gives a comparison between the final state and the exact transfer product applied to the initial state. A discrepancy at one step contributes a nonnegative deficit. The transfer retains existing deficits and adds nonnegative contributions, so exact equality of the final endpoints forces equality at every intermediate step.

The [[node:kl.sheaves.hilbert_detection|positive defect theorem]] converts each numerical equality into equality of embedded images. Reversing the schedule then presents a new kernel alongside a known free kernel over the same image. The resulting splitting gives projectivity, and the graded projective-to-free theorem gives a homogeneous free basis. This is the mechanism that recovers the suffix freeness used by the simultaneous induction.

## Reading sequence

1. [[node:kl.comparison.positive_transfer]] — Define the elementary update.
2. [[node:kl.detail.transfer_properties]] — Prove monotonicity and injectivity.
3. [[node:kl.detail.schedule_state]] — Specify the actual state at a remaining list.
4. [[node:kl.detail.schedule_comparison]] — Iterate the conditional bound.
5. [[node:kl.comparison.schedule_upper_freeness]] — Supply image inclusions from the exact upper suffix kernels.
6. [[node:kl.comparison.no_deficit]] — Use exact endpoints to remove step deficits.
7. [[node:kl.detail.reverse_projectivity]] — Construct the kernel splitting from image equality.
8. [[node:kl.comparison.reverse_freeness]] — Recover freeness through the reverse traversal.
