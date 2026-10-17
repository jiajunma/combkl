# 6. Reciprocity and simultaneous induction

This chapter closes the proof. The paper organizes the conclusion around reciprocal KL comparison. The Lean main theorem first establishes R-tilde invariance together with terminal-kernel freeness, and then applies canonical KL reciprocity and the degree bound. The notes follow the actual declarations while keeping this relationship explicit.

## Positive transfer

Read [[node:kl.comparison.positive_transfer]], [[node:kl.comparison.normalized_kernel]], and [[node:kl.comparison.edge_increment]]. The calculation of \(t^{-1}-t\) explains why every edge has the same transfer coefficient. [[node:kl.comparison.global_comparison]] composes the inequalities and identifies the transfer product using the path formula.

## Exactness and freeness

[[node:kl.comparison.no_deficit]] explains why exact endpoints force every intermediate bound to be exact. [[node:kl.sheaves.hilbert_detection]] converts the resulting Hilbert equality into actual module equality, including higher-codimension quotients.

[[node:kl.comparison.free_suffixes]] states the freeness property being propagated. [[node:kl.notes.graded_projective_free]] supplies the final graded algebra input for [[node:kl.comparison.reverse_freeness]], whose exact-sequence argument should be read carefully.

## The simultaneous induction and the main theorem

[[node:kl.comparison.rtilde_row_comparison]] isolates the unknown R-tilde entry using the source sheaf's own character vector. [[node:kl.comparison.rtilde_step]] compares in both directions. [[node:kl.comparison.rtilde_invariance]] packages this with the new freeness in a strong induction over all endpoints.

Finally, [[node:kl.comparison.reciprocal_rigidity]] and [[node:kl.main.kl_finite]] give the KL equality in finite generator rank. The finite-support models from Chapter 2 then yield [[node:kl.main.combinatorial_invariance]] for arbitrary Coxeter systems.
