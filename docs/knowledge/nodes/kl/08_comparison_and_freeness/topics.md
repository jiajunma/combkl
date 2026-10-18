# 8. Hilbert comparisons and kernel freeness

This chapter turns the geometric edge inclusion into a numerical comparison and then shows how exact comparison recovers module freeness. Its inputs are the transported schedule, the edge-image bound from chapter 7, and the stalk–costalk characters from chapter 5.

There are two directions of reasoning. Forward traversal accumulates inequalities without assuming the lower partial kernels are free. Once the endpoints agree, equality of Hilbert values identifies the embedded images, and reverse traversal proves freeness of those kernels. Keeping the two directions in this order prevents a circular use of freeness.

## One-edge algebra and state vectors

Adding one outgoing condition replaces a kernel \(K\) by a smaller kernel \(K'\). Restriction to that edge gives a surjection onto the lower image \(I_e\), with kernel \(K'\). Thus
\[
0\longrightarrow K'\longrightarrow K\longrightarrow I_e\longrightarrow0,
\qquad H_K-H_{K'}=H_{I_e}.
\]
This exactness is available before either kernel is known to be free. Its Hilbert identity uses degreewise finite-dimensional exactness and convergence from chapter 3.

The schedule state records a normalized Hilbert value at each vertex for the conditions remaining at that stage. Set \(q=t^2\), \(0<t<1\). Combining the edge inclusion, the factor-degree formula, and the chosen state normalization gives the same positive coefficient \(T=t^{-1}-t\) for every edge.

An elementary transfer adds \(T\) times the upper coordinate to the lower coordinate. Monotonicity lets it propagate inequalities; injectivity will later let the proof recover an earlier state from equal later states. The one-edge increment theorem is the point where the geometric input becomes this uniform numerical rule.

1. [[node:kl.detail.kernel_exact_sequence]]
2. [[node:kl.comparison.normalized_kernel]]
3. [[node:kl.detail.schedule_state]]
4. [[node:kl.comparison.positive_transfer]]
5. [[node:kl.detail.transfer_properties]]
6. [[node:kl.comparison.edge_increment]]

## Accumulation and disappearance of deficits

Iterate the one-edge inequality along the schedule. The schedule-comparison theorem controls this accumulation. The global comparison then identifies the product with the target R-matrix by the path formula and identifies the initial and final states through actual stalk–costalk reciprocity.

At this stage the result is a coordinatewise inequality for every \(0<t<1\). The no-deficit theorem is conditional on exact equality of its endpoints. Under that condition, monotonicity and injectivity of the transfers force equality at every intermediate step: no strict increase can disappear later in the ordered product.

Each equality of increments becomes equality of Hilbert values for an actual inclusion \(I_e\subseteq f_eJ_e\). Hilbert detection then gives \(I_e=f_eJ_e\). The argument compares each homogeneous dimension with a positive weight, so a nonzero quotient would contribute a positive deficit. It also detects finite-length or higher-codimension defects that rank comparison alone would miss.

1. [[node:kl.detail.schedule_comparison]]
2. [[node:kl.comparison.global_comparison]]
3. [[node:kl.comparison.no_deficit]]
4. [[node:kl.sheaves.hilbert_detection]]

## Freeness in reverse order

Once all corrected image inclusions are equalities, traverse the schedule backward. The empty set of outgoing conditions leaves the original free stalk. At the next reverse step, the image equality supplies the algebraic presentation needed by the reverse-projectivity theorem.

That theorem proves projectivity of the new kernel from the explicit maps and exact sequence. The kernel inherits a nonnegative grading and is finite over the polynomial ring, so the projective-to-free theorem from chapter 3 supplies a homogeneous free basis. This extends freeness through one more condition, and finite reverse traversal treats every terminal kernel.

The free-suffixes definition packages precisely this collection of kernel assertions. It is the induction statement needed in chapter 9, rather than a claim that arbitrary submodules of a free module are free.

1. [[node:kl.detail.reverse_projectivity]]
2. [[node:kl.comparison.reverse_freeness]]
3. [[node:kl.comparison.free_suffixes]]

## How later chapters use these results

Chapter 9 uses the forward comparison to prove the new R-entry from smaller-interval information. R-matrix equality then supplies the endpoint equality required here. The no-deficit, Hilbert-detection, and reverse-freeness results produce the new free-suffixes assertion, closing the simultaneous induction.

The sequence is: geometric inclusion, Hilbert inequality, endpoint equality, image equality, projectivity, and finally freeness. Each transition has its own theorem in the reading lists above.
