# 6. Reflection orders and dihedral geometry

An unlabelled interval isomorphism does not supply root labels or a reflection order. This chapter establishes the combinatorial and geometric facts that make a transported edge schedule usable anyway. Its inputs are Bruhat order, the real root system, and the algebraically defined R-family.

The outputs have three different roles: reflection edges can be recovered from the order; an ordered path product gives the normalized R-matrix; and rank-two counting determines the correction factor used in the local edge comparison. Keeping these roles distinct makes the later localization argument easier to follow.

## Geometric orders and rank-two intervals

A generic functional, normalized by a positive height functional, assigns distinct slopes to positive roots. Within a root plane, these slopes give an angular order. The plane-basis datum picks its two boundary roots; the induced reflection subgroup and relative intervals then provide the rank-two Coxeter geometry.

An ambient interval may meet a plane-subgroup coset in a relative dihedral interval. The transport theorem identifies the relevant relative intervals under an unlabelled interval isomorphism. The later-edge count theorem extracts the numerical information needed from that identification. It is this proved count comparison that supports the transported schedule; the transported ordering is not assumed to be a geometric reflection order for the source system.

The dihedral theorem \(P=1\) is a separate polynomial result. It explains the simple rank-two KL behavior, while the actual structure-sheaf models used in chapter 7 have their own interpolation proof.

1. [[node:kl.detail.geometric_functional]]
2. [[node:kl.notes.reflection_order]]
3. [[node:kl.detail.plane_basis]]
4. [[node:kl.notes.relative_dihedral_intervals]]
5. [[node:kl.notes.relative_dihedral_transport]]
6. [[node:kl.paths.later_count]]
7. [[node:kl.notes.dihedral_kl]]

## Recovering edges and transporting schedules

Start with cover edges, which are visible in the order. Diamond closure adds edges using the prescribed rank-two patterns. The reconstruction theorem proves that the resulting closure is exactly the reflection-edge relation. Consequently an interval order isomorphism transports all reflection edges, not just covers.

This permits a target reflection order to assign scores to the source interval's edges. The transported schedule and its chronological reverse describe the same edge set in the two directions required by the proofs: one direction evaluates the transfer product, while the other tracks which outgoing conditions remain.

The reconstruction theorem supplies the edges; the schedule definition supplies their order; relative dihedral transport supplies the local properties of that order. These are separate inputs and should not be conflated into an assumption that root labels themselves are preserved.

1. [[node:kl.detail.diamond_closure]]
2. [[node:kl.detail.diamond_reconstruction]]
3. [[node:kl.paths.graph_invariance]]
4. [[node:kl.detail.transported_schedule]]

## Paths and degree bookkeeping

An elementary edge transfer adds a multiple of one coordinate to another. Expanding an ordered product of these transfers enumerates paths whose edges occur in the allowed order. The path-product theorem formalizes that expansion without yet identifying the result with an R-polynomial.

The geometric Dyer theorem performs the identification with \(\widetilde R\). Its proof combines an adapted-order recursion with invariance under reversing a complete root-plane block, then varies the generic functional. The OpenAI notes cite a broader reflection-order theorem; the blueprint follows the geometric-order result established in this Lean development.

The reduced-root edge factor is another output of the root-plane analysis. Its nonvanishing makes multiplication meaningful in the edge quotient, and its degree is determined by the plane counts:
\[
\deg f_e=\frac{\ell(y)-\ell(x)-1}{2}\qquad(e:x\to y).
\]
The degree formula is what later makes all normalized edge inequalities have the same transfer coefficient.

1. [[node:kl.notes.path_product]]
2. [[node:kl.paths.dyer_paths]]
3. [[node:kl.detail.edge_factor]]
4. [[node:kl.paths.plane_degree]]

## How later chapters use these results

Chapter 7 uses relative dihedral intervals and the factor \(f_e\) to compare actual edge images after localization. Chapter 8 uses the degree formula to normalize each comparison and the Dyer theorem to recognize the full product as the target R-matrix. Chapter 9 then compares that matrix with the source R-matrix through actual-character reciprocity.

Thus the two main outputs—an R-matrix from paths and a correction factor from plane counts—enter different stages of the same comparison argument.
