# 3. Real realizations and graded algebra

This chapter supplies the coefficient geometry and graded algebra needed to turn interval combinatorics into module calculations. It has two connected parts: roots become linear polynomial labels, and graded modules provide covers, bases, characters, and Hilbert values over the resulting polynomial ring.

The geometric setup assumes finitely many simple generators so that the realization is finite-dimensional. The group and its root system may still be infinite. The eventual reduction from arbitrary generating sets is handled in chapter 9.

## The real coefficient geometry

The extended realization repairs degeneracy of the Tits form while retaining independent root and normal data. Reflection faithfulness ensures that the linear action detects the group elements and the reflections needed in later localization arguments.

The root–reflection correspondence makes each reflection carry a unique positive root. The inversion-sign criterion then identifies the roots inverted by an element and proves that their number is its length. This count will become the degree of an incoming-label product in stalk–costalk duality.

Two further results prepare localization. The image of a product of distinct reflections identifies the associated root plane. Passing to the symmetric algebra turns roots into degree-one polynomials. The linear-quotient theorem identifies a quotient by a linear subspace with the symmetric algebra of the quotient space, proving that the corresponding ideal is prime. Thus the labels, quotient rings, and prime localizations used later are attached to actual root geometry.

1. [[node:kl.notes.extended_realization]]
2. [[node:kl.detail.positive_roots]]
3. [[node:kl.notes.reflection_faithfulness]]
4. [[node:kl.detail.root_reflection_correspondence]]
5. [[node:kl.detail.root_inversions]]
6. [[node:kl.detail.root_inversion_count]]
7. [[node:kl.realization.reflection_plane]]
8. [[node:kl.detail.polynomial_labels]]
9. [[node:kl.detail.linear_quotient]]

## Grading, minimal covers, and characters

A graded module comes with its homogeneous pieces and scalar compatibility. Homogeneous maps preserve these pieces, while a shift \(M(d)_n=M_{n-d}\) moves generator degrees in a controlled way. Coefficient transport explains why changing from symmetric-algebra coordinates to polynomial coordinates preserves the module and its grading.

Graded Nakayama is the engine behind minimal covers: homogeneous generators whose residues span modulo the positive-degree ideal already generate the whole module. Choosing a basis of that residue space produces a minimal graded free cover. When the target is projective, the projective-to-free theorem shows that such a cover has no residual kernel, yielding a homogeneous basis.

For a free module, the generator degrees form its character polynomial, and the free Hilbert formula divides that polynomial by \((1-q)^N\). A general submodule can still have a Hilbert value without a free basis. The exactness theorem uses finite-dimensional homogeneous pieces and convergence to prove additivity in that more general setting. This distinction lets the comparison argument begin before partial-kernel freeness is known.

1. [[node:kl.sheaves.graded_module]]
2. [[node:kl.detail.graded_maps_shifts]]
3. [[node:kl.detail.coefficient_change]]
4. [[node:kl.notes.graded_nakayama]]
5. [[node:kl.sheaves.minimal_cover]]
6. [[node:kl.notes.minimal_cover_existence]]
7. [[node:kl.notes.graded_projective_free]]
8. [[node:kl.detail.graded_character]]
9. [[node:kl.detail.hilbert_values]]
10. [[node:kl.sheaves.hilbert_free]]
11. [[node:kl.detail.hilbert_exactness]]

## How later chapters use these results

Chapter 4 uses minimal covers to attach stalks and homogeneous maps to control the restrictions. Chapter 5 uses generator degrees and the inversion count to calculate duality shifts. Chapter 7 uses linear prime ideals to isolate root planes and to form edge quotient rings. Chapter 8 uses Hilbert additivity for the forward inequalities and projective-to-free conversion for the reverse argument.

Two recurring transitions are therefore justified here: geometric roots become algebraic labels, and projective graded modules become free modules with explicit homogeneous degrees.
