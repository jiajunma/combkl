# 2. Hecke operators and canonical polynomials

This chapter constructs the polynomial objects whose invariance will eventually be proved. Starting from a Coxeter system, it defines Hecke operators, extracts the R-families from the bar map, and constructs the unique normalized KL family. The construction itself uses simple reflections; the later theorem will show that its output depends only on the unlabelled interval.

The chapter relies on the finite intervals and rank differences from chapter 1. Its conclusions are algebraic, so the canonical KL polynomial and its strict degree bound are available before any boundary-sheaf character is introduced.

## Operators and the bar involution

Left and right Hecke operators act on the module with basis indexed by group elements. Their formulas distinguish ascent from descent. The quadratic relation controls the inverse of a simple operator and is the local identity behind the bar construction.

The bar involution relates a parameter to its inverse and intertwines the corresponding operators. Its square is the identity. That involutivity later becomes a convolution identity for the coefficient polynomials. Read the operator definitions first, then the quadratic identity, and then the bar map. The overview [[node:kl.notes.hecke_action]] develops the operators, their quadratic relation, and the bar involution, collecting their normalization in one place.

1. [[node:kl.definitions.hecke_operators]]
2. [[node:kl.definitions.hecke_quadratic_relation]]
3. [[node:kl.detail.hecke_quadratic_identity]]
4. [[node:kl.definitions.bar_involution]]
5. [[node:kl.notes.hecke_action]]

## The two R families

The normalized R-family is defined by coefficients of the bar map. Its descent recursion provides an algebraic way to compute it. The ordinary R-family is the polynomial family in \(q\) used in canonical reciprocity; the square-parameter theorem relates the two conventions.

The reciprocal convolution identity is the main output of this part. On a finite interval, the matrix of ordinary R-polynomials has an inverse given by the appropriately reflected coefficients. This is the compatibility condition that makes the next KL recursion solvable. It is also the algebraic counterpart of the transfer matrix that will later be built from ordered paths.

The path formula has not been assumed in these definitions. Chapter 6 proves that the geometric path construction gives this already-defined normalized R-family.

1. [[node:kl.detail.rtilde_family]]
2. [[node:kl.detail.rtilde_recursion]]
3. [[node:kl.detail.ordinary_r]]
4. [[node:kl.foundations.rtilde]]
5. [[node:kl.detail.r_kernel]]

## Construction and identification of P

For fixed endpoints, the previously constructed polynomials determine a defect in the reciprocity equation. The lower-half truncation selects the allowed coefficients of the new polynomial. The R-kernel identity proves that this selection satisfies the full reciprocity equation, and the strict half-degree bound makes the solution unique.

The resulting pair of families satisfies
\[
q^{d(x,y)}P_{x,y}(q^{-1})
=\sum_{x\le z\le y}R_{x,z}(q)P_{z,y}(q),
\qquad 2\deg P_{x,y}<d(x,y)\quad(x<y).
\]
The normalization entry states all diagonal, support, recursion, and degree conditions together. Existence and uniqueness then identify the constructed family with the canonical KL polynomials used in the final theorem.

Finally set \(q=t^2\) and scale the vector by \(t^{-d(x,b)}\). The scaled reciprocity entry rewrites the identity using \(\widetilde R(t^{-1}-t)\), which is exactly the matrix form needed in the final comparison.

1. [[node:kl.foundations.low_half]]
2. [[node:kl.detail.kl_defect]]
3. [[node:kl.detail.kl_recursion]]
4. [[node:kl.foundations.normalized_kl]]
5. [[node:kl.foundations.canonical_kl]]
6. [[node:kl.foundations.scaled_kl]]

## How later chapters use these results

Chapter 5 identifies tensor-word characters with positive Hecke-word coefficients and derives their R-convolution. Chapter 6 identifies ordered path products with the normalized R-matrix. Chapter 9 first proves that this R-matrix is invariant, then applies canonical reciprocity and the strict half-degree bound to the difference of two KL polynomials. The polynomial construction here is therefore both the definition of the final invariant and the source of its final uniqueness argument.
