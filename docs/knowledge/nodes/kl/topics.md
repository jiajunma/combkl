# Combinatorial invariance — Blueprint and Knowledge Base

An order isomorphism of Bruhat intervals
\[
\phi:[a,b]\xrightarrow{\sim}[a',b']
\]
determines equality of the Kazhdan–Lusztig polynomials
\[
P_{a,b}(q)=P'_{a',b'}(q).
\]
The intervals may lie in different Coxeter systems. The complete statement is [[node:kl.main.combinatorial_invariance]].

This knowledge base develops the objects and proofs in the local Lean library. Start with the definitions of Coxeter groups and the basic Hecke algebra; the entries introduce the additional root geometry, graded algebra, sheaves, and localization constructions as they are used.

## One interval through the constructions

For a simple reflection \(s\), the interval \([1,s]\) has two vertices and one reflection edge. Take \(A=\mathbb R[\alpha]\), with \(\alpha\) of degree one.

| Construction | The calculation on \([1,s]\) |
|---|---|
| Polynomial invariants | \(R_{1,s}(q)=q-1\) and \(P_{1,s}(q)=1\). |
| Graph sheaf | Both stalks are \(A\), the edge module is \(A/(\alpha)\), and both restrictions are reduction modulo \(\alpha\). |
| Global sections | Pairs \((f,g)\) satisfying \(f-g\in\alpha A\). |
| Word module | \(A\otimes_{\mathbb R[\alpha^2]}A\), evaluated as the same compatible pairs. |
| Outgoing kernels | The kernel at \(1\) is \(\alpha A\) with the condition imposed, and \(A\) after removing it. |
| Hilbert values | \(H_A(q)=1/(1-q)\), while \(H_{\alpha A}(q)=q/(1-q)\). |
| Normalized state | With \(q=t^2\), the vector changes from \((t,1)\) to \((t^{-1},1)\). |

The transfer coefficient in the last line is \(T=t^{-1}-t\): adding \(T\) times the upper coordinate to the lower one gives \(t+(t^{-1}-t)=t^{-1}\). For \(0<t<1\), this coefficient is positive.

These calculations recur in the topic guides. Larger intervals have several edge conditions at a vertex; their partial kernels, image maps, and degrees are the objects controlled by the general proof.

## Three polynomial objects

The Hecke algebra supplies the ordinary R-polynomials and the canonical KL polynomials. The boundary sheaf supplies a third family through homogeneous bases of its stalks.

| Family | Defining data | Role in the proof |
|---|---|---|
| \(R_{x,y}\), and its normalized form \(\widetilde R_{x,y}\) | Bar coefficients and their recursion | Entries of the path-transfer matrix. |
| \(P_{x,y}\) | Reciprocity with R and a strict degree bound | The canonical family in the final theorem. |
| \(C_{x,b}\) | Degrees of a homogeneous basis of the actual boundary stalk | The reciprocal vector used in the comparison. |

The definitions are [[node:kl.detail.ordinary_r]], [[node:kl.detail.rtilde_family]], [[node:kl.foundations.normalized_kl]], and [[node:kl.duality.stalk_character]]. The main Lean route proves reciprocity for \(C\), uses it to establish R-invariance, and then applies the characterization of \(P\).

## How the proof develops

**Build the algebraic objects.** Coxeter combinatorics supplies finite ranked intervals. The realization supplies root vectors, their actions, and polynomial edge labels. Graded module theory supplies minimal covers, bases, and Hilbert values. These inputs construct the boundary sheaf.

**Obtain a reciprocal character vector.** Tensor words have explicit evaluation coordinates and perfect pairings. Their characters are Hecke-word coefficients. Decomposing a word sheaf into boundary models gives the same multiplicities for its stalks and full kernels. Finite cancellation yields actual-character reciprocity.

**Compare the edge images.** Reflection geometry recovers the directed reflection graph from the interval order and provides an edge schedule. Root-plane localization reduces the image calculation to dihedral models. It yields an inclusion of the lower edge image in a homogeneous scalar multiple of the upper image, under the required upper-kernel freeness.

**Accumulate the inequalities.** Hilbert exactness converts this inclusion into a one-edge inequality. The degree of the scalar factor makes every normalized step use the same coefficient \(T\). Multiplying the steps gives a transfer matrix, whose entries are normalized R-polynomials by the path formula.

**Run the simultaneous induction.** Proper upper intervals provide target-kernel freeness; proper initial intervals provide known bottom-row R-entries. Cancelling those entries leaves one new R-inequality. The inverse interval isomorphism gives the reverse inequality. R-equality then makes the endpoint comparison exact, so every edge-image inclusion is an equality. Reverse traversal reconstructs all suffix-kernel freeness at the current rank.

**Recover canonical KL invariance.** With the R-matrices equal, a separate induction compares the canonical P-vectors. Their remaining difference is reciprocal and lies strictly below the middle degree, forcing it to vanish. Finite-support interval models carry the result to arbitrary Coxeter systems.

## Mathematical topics

| Topic | Objects and results |
|---|---|
| [Coxeter combinatorics](coxeter/index.html) | Words, length, Bruhat order, interval isomorphisms, and finite support. |
| [Realizations and root geometry](realizations/index.html) | Tits form, extension, actions, roots, signs, and moving planes. |
| [Hecke algebra and polynomial invariants](02_hecke_polynomials/index.html) | Hecke operators, bar, R-polynomials, canonical P, and rigidity. |
| [Coefficient algebras and graded modules](graded_algebra/index.html) | Polynomial coefficients, grading, covers, bases, Hilbert values, and module algebra. |
| [Reflection Frobenius extensions and word modules](word_modules/index.html) | Reflection invariant algebras, tensor induction, evaluations, and word characters. |
| [Moment-graph sheaves, support, and duality](sheaves/index.html) | Graph sheaves, minimal extension, decomposition, support, duality, and actual characters. |
| [Reflection orders, dihedral combinatorics, and paths](reflection_combinatorics/index.html) | Dihedral intervals, plane weights, edge reconstruction, schedules, and path formulas. |
| [Localization and comparison of embedded images](localization/index.html) | Plane and edge rings, local models, correction factors, and embedded images. |
| [Hilbert comparison and combinatorial invariance](invariance/index.html) | Hilbert-state comparison, reverse freeness, simultaneous R-induction, and KL invariance. |

Each topic guide explains its constructions and organizes the detailed entries by their mathematical role. A definition has one home and can be used throughout the graph.

## Reading routes

To follow the main proof, first read the interval and polynomial definitions, then the overview of the simultaneous induction. Develop the graded-module and sheaf constructions, followed by word duality and the geometric/localization comparison. Return to the full induction with those inputs established.

To understand the geometric side, follow the Tits form, its radical extension, root signs and inversions, induced dihedral systems, geometric orders, and plane localization.

To understand the algebraic side, follow graded components and positive ideals, minimal covers and homogeneous bases, tensor words, sheaf sections, boundary summands, and supported duality.

The dependency graph records the mathematical inputs to individual results. Definition links explain the terminology used in the prose. Lean links identify the declarations at the fixed source revision; comparisons with the OpenAI notes occur at the results where the presentations differ.
