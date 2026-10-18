# Combinatorial Invariance — Blueprint and Knowledge Base

The question is whether the ordinary Kazhdan–Lusztig polynomial attached to an interval can be recovered from the interval's order alone. The usual construction of that polynomial uses simple reflections and the Hecke algebra. An order isomorphism between two intervals is not supplied with those choices.

The theorem says that if
\[
\phi:[u,b]\xrightarrow{\sim}[u',b']
\]
is an order isomorphism of Bruhat intervals, then
\[
P_{u,b}(q)=P'_{u',b'}(q).
\]
The groups containing the intervals may be different. The exact statement is [[node:kl.main.combinatorial_invariance]].

These chapters assume the definition of a Coxeter group and the basic idea of a Hecke algebra, with brief reminders where needed. They introduce the graph-sheaf, graded-module, and localization constructions through concrete calculations. The linked entries retain the detailed general proofs and their Lean references.

## Start with one interval and follow it through the proof

Take a simple reflection \(s\). The interval \([1,s]\) has just two vertices, \(1<s\). It can be viewed in several ways:

| View | The calculation for this interval |
|---|---|
| Order | There is one upward edge, from \(1\) to \(s\). |
| Canonical polynomials | The Hecke recursion gives \(R_{1,s}=q-1\); reciprocity and the degree bound give \(P_{1,s}=1\). |
| Graph sheaf | Put \(A=\mathbb R[\alpha]\) at both vertices and \(A/(\alpha)\) at the edge. A section is a pair \((f,g)\) with \(f-g\in\alpha A\). |
| Outgoing conditions | The lower kernel is \(\alpha A\) while the edge condition is present, and \(A\) after it is removed. The top kernel is always \(A\). |
| Character and Hilbert value | Each stalk has character \(1\); \(H_A(q)=1/(1-q)\), while \(H_{\alpha A}(q)=q/(1-q)\). |
| Normalized state | With \(q=t^2\), the state moves from \((t,1)\) to \((t^{-1},1)\) by adding \((t^{-1}-t)\) times the top coordinate to the bottom one. |

Each row will be derived in the corresponding chapter. The point of following the same example is that the later numerical vector is built from the earlier modules: it is not an unrelated invariant introduced at the end.

A larger interval has more edges, several outgoing conditions at a vertex, and kernels whose freeness is not automatic. The proof must control those additional features, transport the edge schedule through an unlabelled isomorphism, and compare two resulting polynomial matrices. The small example illustrates the operations; it does not prove those general assertions.

## A short vocabulary for the intermediate objects

A graph sheaf assigns a module to each vertex and edge, with maps from both endpoints into the edge module. A stalk is a vertex module. A compatible section is a tuple of stalk vectors satisfying every required edge equation.

An upward kernel consists of the vectors in one stalk that vanish under selected outgoing maps. Its full outgoing kernel is the costalk used here. A schedule is an ordered list of edges; its suffix is the final segment still waiting to be processed.

A graded-rank polynomial records the degrees of a homogeneous basis of a free module. A Hilbert value instead sums the dimensions of all homogeneous pieces at a convergent real parameter. It can be defined even for modules not yet known to be free.

Localization permits selected denominators in the coefficient ring. In this proof it makes some labels invertible, so their edge quotients become zero and the surviving equations can be studied in rank-two pieces.

These descriptions are starting points. Chapter 3 develops the module language, chapter 4 writes the sheaf equations, chapter 7 explains the localizations, and chapter 8 calculates the states.

## Keep the polynomial objects separate

The notation has several layers because different constructions supply different parts of the argument:

| Notation | Meaning |
|---|---|
| \(R_{x,y}(q)\) | Ordinary R-polynomial, constructed from Hecke data. |
| \(\widetilde R_{x,y}(T)\) | Normalized R-polynomial; later identified with an ordered path sum. |
| \(P_{x,y}(q)\) | Canonical KL polynomial, characterized by reciprocity and a strict degree bound. |
| \(C_{x,b}(q)\) | Actual boundary-sheaf stalk character, obtained from homogeneous module generators. |
| \(C_x^{\mathbf s}(q)\) | Stalk character of a tensor word, before separating its boundary-model summands. |

The normalized R-family is defined in [[node:kl.detail.rtilde_family]], the canonical family in [[node:kl.foundations.canonical_kl]], and the actual character in [[node:kl.duality.stalk_character]].

The one-edge example has \(C=P=1\), but the general argument does not assume that equality. It proves the needed reciprocity for \(C\), uses \(C\) to establish R-invariance, and then proves invariance of \(P\) separately.

Also distinguish the Hecke basis element \(T_s\) from the scalar \(T\). In the comparison, \(0<t<1\), \(q=t^2\), and \(T=t^{-1}-t>0\). The precise reciprocal normalization is [[node:kl.foundations.scaled_kl]]. A group envelope \(L_s:W\to W\) in chapter 1 is likewise a different map from a Hecke operator on a free module; the domain and definition specify which object is meant.

## The main proof as a sequence of concrete questions

**First, construct the objects.** Chapters 1–3 establish the finite interval combinatorics, canonical polynomials, and coefficient algebra. Chapter 4 constructs the boundary sheaf by taking minimal covers of actual boundary images. Chapter 5 derives a reciprocal identity for its character using tensor words, pairings, and cancellation.

**Next, establish a conditional comparison.** Chapter 6 reconstructs reflection edges and identifies ordered transfer products with R-polynomials. Chapter 7 proves an inclusion between lower and corrected upper edge images, assuming the upper kernel is free. Chapter 8 turns that inclusion into a state inequality and explains what equality would imply.

**Then, supply the missing freeness in the correct order.** Chapter 9 uses a simultaneous induction. Smaller upper intervals supply the free upper kernels needed for the comparison. Smaller initial intervals supply the already-known R-entries. Cancelling these known entries isolates one new R-polynomial. The inverse interval isomorphism gives the reverse inequality, proving equality.

**Finally, recover new freeness and compare P.** R-matrix equality makes the state comparison exact. The numerical deficits vanish, so the actual image inclusions are equalities. A backward traversal proves the new suffix kernels free, completing the simultaneous induction. A separate canonical-KL induction then eliminates a reciprocal difference using the strict half-degree bound.

The two traversals and two inductions are explained with equations in chapters 8 and 9. They should not be compressed into the instruction “compare and conclude.”

## Where the detailed arguments are developed

| Chapter | Mathematical task | Result carried forward |
|---|---|---|
| 1. Coxeter systems and Bruhat order | Derive lifting, subwords, finiteness, and rank preservation from the strong order. | Finite ranked intervals and finite-support reductions; begin with [[node:kl.detail.strong_exchange]]. |
| 2. Hecke operators and canonical polynomials | Construct R and P and prove their normalizations and reciprocity. | Canonical polynomials and the degree bound, independent of the sheaf construction; see [[node:kl.foundations.canonical_kl]]. |
| 3. Real realizations and graded algebra | Turn reflections into root labels and establish the algebra of covers, free bases, and Hilbert values. | The coefficient ring and algebraic tools used by sheaves; see [[node:kl.detail.polynomial_labels]] and [[node:kl.notes.graded_projective_free]]. |
| 4. Moment-graph sheaves and minimal extensions | Construct the boundary sheaf, identify its maps, and prove splitting and decomposition. | Actual sheaf objects and isomorphisms, culminating in [[node:kl.detail.model_decomposition]]. |
| 5. Word objects, duality, and characters | Build tensor words, prove their character formula, and pass reciprocity to boundary summands. | [[node:kl.duality.actual_character_reciprocity]], the character identity used in the comparison. |
| 6. Reflection orders and dihedral geometry | Recover reflection edges from order, transport schedules, and identify their path products. | The R-matrix and correction-factor degree; see [[node:kl.paths.dyer_paths]] and [[node:kl.paths.plane_degree]]. |
| 7. Localization and embedded edge images | Compare two actual images in one edge module through local dihedral models. | [[node:kl.local.edge_inclusion]], conditional on the required upper-kernel freeness. |
| 8. Hilbert comparisons and kernel freeness | Accumulate edge inequalities and recover freeness when equality is attained. | Forward comparison and reverse freeness, linked by [[node:kl.comparison.no_deficit]]. |
| 9. Simultaneous induction and invariance | Supply the freeness hypotheses on smaller intervals, prove R-invariance, then compare canonical KL polynomials. | [[node:kl.comparison.rtilde_invariance]] and the final theorem for arbitrary Coxeter systems. |


## How to use the chapters

Read the numbered explanations in a chapter before its detailed-entry lists. Those explanations introduce the notation, calculate a small case, and identify the precise theorem needed for the general step. The lists then lead to full statements and proofs.

The worked examples are explanatory calculations. They do not claim to be separate Lean declarations unless an entry explicitly identifies one. Source panels and definition links are generated deterministically from the retained Lean snapshot and the concept registry.

The blueprint follows the completed Lean development. Definitions are marked formalized and theorem entries proved. These describe their mathematical roles in the completed development.

When the Lean argument and the OpenAI notes differ, the relevant entries explain the difference. The main route here uses actual-character reciprocity followed by R-first simultaneous induction. The local intersection statement with its nonzero-diagonal hypothesis and the separate boundary-character identification condition remain explicit related results, rather than hidden assumptions in the main proof.
