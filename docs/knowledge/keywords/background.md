---
title: Prerequisites that meet in the main proof
primary_topic: kl.graded_algebra
---

Three collections of definitions support the comparison. Coxeter words give length, reflections and Bruhat intervals. Realization data turn reflections into root vectors and linear labels. Graded algebra supplies homogeneous components, finite module data, scalar quotients and Hilbert values. The proof repeatedly passes between these descriptions, so their conventions must be read together.

The [[node:kl.detail.strong_exchange|strong-exchange theorem]] controls changes in reduced words. Root-sign and root-plane results control the geometry of reflection edges. On the algebra side, a root label becomes a degree-one polynomial, and quotienting by it gives the edge coefficient ring. These are the inputs for the sheaf restrictions and for the factor \(1-q\) in an upper-image Hilbert value.

The later arguments use these foundations in specific combinations: rank-two geometry supplies counts, localization supplies image equalities, and positive Hilbert values detect whether an inclusion is strict. The route below gives the definitions before those applications and connects each prerequisite to a proof-bearing node.

## Reading sequence

1. [[node:kl.coxeter.word_data]] — Fix word and length notation.
2. [[node:kl.detail.strong_exchange]] — Derive the deletion mechanism.
3. [[node:kl.realization.tits_form]] — Introduce roots and their normal functionals.
4. [[node:kl.detail.polynomial_labels]] — Turn root vectors into algebraic edge labels.
5. [[node:kl.sheaves.graded_module]] — Read the actual nonnegative module-data fields.
6. [[node:kl.detail.hilbert_values]] — Distinguish series, numerical values and graded rank.
7. [[node:kl.algebra.hilbert_convergence]] — Justify the values used in comparison.
