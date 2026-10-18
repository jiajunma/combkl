# Combinatorial Invariance — Blueprint and Knowledge Base

The goal is to explain why an isomorphism of unlabelled Bruhat intervals
\[
\phi:[u,b]\xrightarrow{\sim}[u',b']
\]
forces equality of their ordinary Kazhdan–Lusztig polynomials
\(P_{u,b}(q)=P'_{u',b'}(q)\). The two intervals may come from different Coxeter systems. Their order is the input; root labels and simple-reflection choices are not part of the supplied isomorphism. The precise final statement is [[node:kl.main.combinatorial_invariance]].

This knowledge base follows the completed Lean development. Each chapter page explains its mathematical task and the relationships among its results; the linked entries contain definitions and detailed proofs. The chapter order is a reading sequence. The dependency graph records the actual logical prerequisites, which sometimes cross chapter boundaries.

## The objects that connect the chapters

There are three polynomial constructions to keep distinct. The ordinary R-polynomials and normalized R-polynomials come from the Hecke bar map. Canonical KL polynomials are constructed using reciprocity and a strict degree bound. Actual boundary-sheaf characters come from homogeneous stalk bases. Their roles are:

| Object | Construction | Role in the proof |
|---|---|---|
| Normalized R-family | [[node:kl.detail.rtilde_family]] | Its entries are also path counts; they become the matrices in the comparison argument. |
| Canonical KL family | [[node:kl.foundations.canonical_kl]] | This is the invariant sought in the final theorem. Its strict half-degree bound supplies the final rigidity argument. |
| Actual stalk character | [[node:kl.duality.stalk_character]] | Its proved reciprocity and sheaf interpretation supply the numerical comparisons used to establish R-invariance. |

The variable convention is \(q=t^2\), with transfer parameter \(T=t^{-1}-t>0\) for \(0<t<1\). The normalization in [[node:kl.foundations.scaled_kl]] puts polynomial reciprocity into the same matrix form as the sheaf comparison.

## What each chapter contributes

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

## How the main argument closes

The algebraic construction of P and the geometric construction of the actual character C proceed separately. The word-object calculation and model decomposition prove R-reciprocity for C. Independently, unlabelled edge reconstruction and the path formula identify the transfer product associated with a transported schedule.

At a single edge, root-plane localization compares its lower image with a corrected upper image, provided the upper kernel is free. Hilbert additivity turns this inclusion into an inequality. Iterating gives a comparison between the source character vector and the target R-matrix.

The simultaneous induction supplies the missing upper freeness from strictly smaller upper intervals. Previously known R-entries cancel from the bottom row of the comparison. Running the argument for the inverse interval isomorphism gives equality of the new R-entry. Equality of the full R-matrix then makes the comparison endpoints exact. Every intermediate deficit vanishes, Hilbert detection gives actual image equality, and reverse traversal produces the new kernel freeness. This completes both induction assertions without assuming the current bottom kernel is free.

After that induction, the two canonical KL vectors satisfy reciprocity with the same R-matrix. Equality on smaller upper intervals leaves only a reciprocal bottom difference, which the strict half-degree bound forces to vanish. Finite-support parabolic transport then removes the finite-generator restriction.

## Reading and source conventions

Follow a chapter's grouped reading lists for the definitions and proofs behind its summary. Technical terms acquire definition links during the Python build. The Lean panels lead to the fixed source snapshot, and the dependency graph lets you trace a theorem's prerequisites.

Definitions and constructions are marked formalized; theorem entries are marked proved. Both describe completed parts of the supplied development. They are different mathematical roles, not two levels of unfinished work.

Lean is primary when its route differs from the OpenAI notes. In particular, the main argument uses actual-character reciprocity and R-first simultaneous induction. The separate boundary-character identification condition and the local intersection result with its nonzero-diagonal hypothesis are described in chapter 5, with explicit source comparisons. Their conditions are not silently inserted into the main proof.
