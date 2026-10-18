# 9. Simultaneous induction and combinatorial invariance

This chapter assembles the preceding tools into the invariance theorem. The key is to choose an induction statement strong enough to supply the upper-kernel freeness needed for the edge comparison. For isomorphic intervals in finite-generator Coxeter systems, it proves normalized R-invariance and terminal-kernel freeness in both transported directions simultaneously.

After that induction is complete, a separate induction proves equality of the canonical KL polynomials. Finite-support parabolic transport then extends the result to arbitrary Coxeter systems. The groups themselves need not be finite at any stage.

## The new R entry and exact endpoints

Fix \(\phi:[a,b]\simeq[a',b']\). The induction has two kinds of smaller intervals. Proper initial intervals \([a,z]\), \(z<b\), supply known entries of the bottom R-row. Proper upper intervals \([y,b]\), \(y>a\), supply the free suffix kernels needed at upper endpoints of the current schedule. Rank preservation proves that both kinds have smaller rank difference.

Restriction must preserve the relevant remaining edge conditions, not just identify the abstract upper interval. The induction-step proof checks this using the transported scores and the fact that the incoming edge cannot tie an outgoing edge at its upper endpoint. This verifies the freeness hypothesis of chapter 7 at each step.

Actual-character reciprocity gives an exact source R-row identity, while the transported comparison gives an inequality using the target R-row. All previously known entries cancel. The normalized top character is one, leaving an inequality for the single new entry \(\widetilde R_{a,b}(t^{-1}-t)\). Apply the same argument to \(\phi^{-1}\) to get the reverse inequality. Equality for infinitely many parameters gives equality of the polynomials.

The reciprocal-rigidity theorem listed here has a different later role: it will eliminate the bottom KL-polynomial difference. The new R-entry is obtained by the two numerical inequalities. Once it is known, the endpoint-equality theorem uses the now common full R-matrix to make the schedule comparison exact.

1. [[node:kl.comparison.rtilde_row_comparison]]
2. [[node:kl.comparison.reciprocal_rigidity]]
3. [[node:kl.comparison.rtilde_step]]
4. [[node:kl.detail.endpoint_equality]]

## Closing both induction statements

At rank zero, the interval has one vertex, the diagonal R-entry is one, and the relevant no-condition kernels are free stalks. For the induction step, combine the new R-equality with equality on proper subintervals. The full matrices then agree, so chapter 8 removes every deficit and recovers all terminal kernels in both directions. This proves all parts of the simultaneous statement at the current rank.

Now compare canonical KL polynomials. For a fixed top endpoint, assume equality on all strictly higher upper intervals. Form the two normalized canonical vectors
\[
k_x(t)=t^{-d(x,b)}P_{x,b}(t^2),\qquad
k'_x(t)=t^{-d(x,b)}P'_{\phi(x),b'}(t^2).
\]
Both satisfy reciprocity with the same R-matrix. Subtract the bottom coordinate equations: every higher entry cancels by induction and the diagonal matrix entry is one. The remaining difference satisfies \(\Delta(t)=\Delta(t^{-1})\).

Undoing the normalization gives a reciprocal identity for the difference of the two KL polynomials. Each has degree strictly below half the interval rank, so reciprocal rigidity forces the difference to be zero. This is where the canonical degree bound from chapter 2 is used.

The OpenAI notes organize their comparison around a P-first presentation. The Lean route followed here first closes R-invariance and freeness, then performs this canonical-KL comparison. The linked entries record the source correspondence explicitly.

1. [[node:kl.comparison.rtilde_invariance]]
2. [[node:kl.main.kl_finite]]

## Arbitrary Coxeter systems

Choose reduced words for the two top elements. Chapter 1 shows that each lower ideal uses only the finitely many simple generators in the corresponding word. The standard parabolic construction supplies a Coxeter system on that finite generator set and an inclusion preserving the required length, Bruhat, and polynomial data.

A finite-support interval model records the endpoints and the exact transport to this system. Transport the given interval isomorphism into the two finite-generator models, apply the theorem just proved, and transport the resulting polynomial equality back. The transport theorem includes equality of the canonical polynomials, so the reduction preserves the invariant under discussion.

The final theorem therefore quantifies over arbitrary Coxeter systems and unlabelled interval isomorphisms. Its proof uses finite-dimensional realizations only after this explicit finite-support reduction.

1. [[node:kl.main.finite_interval_model]]
2. [[node:kl.main.finite_model_transport]]
3. [[node:kl.main.combinatorial_invariance]]

## Conclusion and dependency trace

The two reusable outputs are the stronger simultaneous R/freeness theorem for finite-generator systems and the KL-invariance theorem for arbitrary systems. For a full dependency trace, start at [[node:kl.main.combinatorial_invariance]], pass through the finite model and finite-generator theorem, and then follow the simultaneous induction back to the comparison and localization chapters.

The final conclusion does not require identifying the actual boundary character with the canonical KL polynomial. Actual-character reciprocity supplies the R-stage, while canonical reciprocity and the strict degree bound supply the P-stage.
