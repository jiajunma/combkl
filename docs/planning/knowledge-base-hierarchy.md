# Proposed hierarchy for the Blueprint and Knowledge Base

Recorded: 2026-10-18. Status: organization approved on 2026-10-18; implementation in progress.

The subject is **combinatorial invariance of Kazhdan–Lusztig polynomials**. This document records the full topic hierarchy proposed after inspecting the local Lean development. The accompanying [relationship map](knowledge-base-relationships.md) explains how these topics supply objects and results to one another.

The nine branches are mathematical homes. They need not become nine chapters, and their order does not require completing every branch before starting the next. A construction has one defining entry and can have applications in several branches.

The source is the preserved OpenAI Lean snapshot at upstream revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, mirrored in this repository at `108243e05ed46235bf82dc30d4d90c794579776f`. The local inventory contains 34 modules and 2,991 declarations, including 769 definitions, 31 abbreviations, 35 structures, and 3 inductive declarations. All structures and inductive declarations have homes in the table below. The 838 definition-like declarations are grouped by mathematical construction; each helper does not require its own page.

## Entry point and shared navigation

The root page introduces the invariance question, states the final theorem, explains the main proof route, and offers reading routes through the same material.

- **Notation index:** length and order, root actions, coefficient rings, polynomial variables, grading and shifts, stalks and kernels, Hilbert values, characters, schedules, and transfer matrices.
- **Concept index:** definitions and structures, with aliases resolved to their defining entries.
- **Theorem map:** intermediate results and their mathematical prerequisites.
- **Source correspondence:** Lean declarations and OpenAI-note locations attached to the entries they explain.
- **Worked examples:** recurring small intervals, rank-one word modules, degenerate Tits forms, rank-two localization, and a single schedule step.

The user's stated starting point is familiarity with the definitions of Coxeter groups and the basic Hecke algebra. Specialized module, sheaf, localization, and pairing constructions require explanations.

## C. Coxeter combinatorics

This branch supplies finite ranked intervals, reflection-step criteria, and finite-support models.

### C1. Coxeter data, words, length, and reflections

- Coxeter matrices and the local convention for an infinite exponent.
- Simple generators, words, word products, reduced words, and length.
- Reflections as conjugates of simple generators.
- Left and right descents and inversion sequences.
- Length changes under simple and reflection multiplication.

### C2. Signed reflection actions

- Signed reflection data and the meaning of the sign coordinate.
- `simpleAction`, `wordAction`, and `reflectionAction`.
- Inversion sequences as records of sign changes.
- Compatibility used to compare abstract and geometric roots.

### C3. Strong Bruhat order and lifting

- `BruhatStep`, its orientation, and `BruhatLE`.
- Covers, general reflection edges, and saturated chains.
- Strong exchange, the subword criterion, and finite lower intervals.
- Lower and upper simple envelopes.
- Weak monotonicity of the envelopes and the lifting property.

### C4. Intervals, ranks, and order isomorphisms

- `Interval`, its endpoints, and `rankDifference`.
- Initial, upper, and general subintervals.
- Restriction of an interval order isomorphism and preservation of relative rank.
- Strictly smaller rank for proper subintervals.
- Transport of endpoints and interval-indexed data.

### C5. Standard parabolics and finite support

- Generated subgroups, restricted Coxeter matrices, and induced Coxeter systems.
- The standard inclusion and preservation of words, length, reflections, and order.
- Finite simple-generator support for an interval.
- `FiniteIntervalModel`, endpoint identifications, and the interval isomorphism.
- Polynomial transport and the eventual reduction to finitely many generators.

## R. Realizations and root geometry

This branch constructs the representation and root labels, explains the extended realization, and supplies root-plane geometry.

### R1. The geometric root space and Tits form

- Simple-root basis, Gram coefficients, and the bilinear Tits form.
- Normalization and the infinite-exponent convention.
- Roots as vectors, normals as linear functionals, and the reflection formula.
- Finite and infinite dihedral examples.

### R2. The geometric action

- Pre-reflections, linear reflections, and simple geometric operators.
- Coxeter relations and the induced group action.
- Preservation of the form.
- Compatibility with signed reflection data.

### R3. Degeneracy and the nondegenerate extension

- The radical; nondegeneracy and positive definiteness.
- Independence of roots and independence of normal functionals.
- The infinite dihedral example and the effect of quotienting by the radical.
- A complement to the radical and its projection.
- `Realization.Extension` and the extended form.
- Symmetry, nondegeneracy, and preservation of the original embedded form.
- Independence of extended roots and normals.
- Dimension, minimality, and choices in the construction.

### R4. The extended action and reflection faithfulness

- Extended roots and action; restriction to the original representation.
- Faithfulness.
- Moving spaces and ranks of the difference from the identity.
- Rank-one orthogonal transformations.
- Reflection faithfulness and the moving plane of a product of reflections.

### R5. Roots, positivity, and inversions

- `IsRoot`, `Represents`, positive roots, and uniqueness up to sign.
- The positive-root/reflection correspondence.
- `SignedRepresents` and transport of signs.
- Root inversions and their cardinality.
- Sign criteria for ascent and descent.

### R6. Dual geometry and root planes

- Dominant functionals and ascent.
- The dual or cotangent action.
- Planes spanned by roots.
- The separate definitions of `movingSubgroup` and `planeSubgroup`.
- Reflection membership in a root plane.
- Inputs for the induced dihedral Coxeter system in O2.

## H. Hecke algebra and polynomial invariants

This branch constructs R and P and supplies their recursions, reciprocal identities, and rigidity properties.

### H1. Hecke modules and operators

- `Hecke.Space`, standard bases, and coefficient conventions.
- Normalized and unnormalized left and right operators.
- Quadratic relations, inverses, and commuting actions.
- Word operators, units, and conversion of conventions.

### H2. The bar operation

- The bar action on coefficients and on basis vectors.
- `barBasis` and `barLinear`.
- Operator intertwining and involutivity.

### H3. The R-polynomial families

- Bar-expansion coefficients, diagonal values, support, and recursion.
- Laurent intermediates and ordinary R-polynomials.
- Polynomiality, degree, and reciprocal convolution.
- Normalized R-polynomials and the square-parameter conversion.

### H4. Canonical KL polynomials

- Every field of `NormalizedKL`.
- Polynomial reflection, low-degree truncation, and the reciprocity defect.
- The canonical recursive construction.
- Reciprocity, strict degree bounds, existence, and uniqueness.
- The chosen canonical family.

### H5. Word expansions and rigidity

- Positive Hecke words, recursion, support, and bar expansion.
- R-convolution for positive words.
- Dihedral polynomial calculations.
- Scaled polynomial vectors.
- Rigidity of a reciprocal difference under a strict degree bound.

## A. Coefficient algebras and graded modules

This branch supplies the algebra used throughout the proof. Abstract graded-module definitions can be read independently of the realization; root-labelled coefficient algebras specialize that language.

### A1. The realization coefficient algebra

- Symmetric algebras and polynomial-coordinate presentations.
- The action on coefficients and roots as linear polynomials.
- Root ideals, linear quotients, and edge coefficient rings.
- Nonzero linear forms, primality, divisibility, relative primality, and regularity.

### A2. Grading and the positive ideal

- Homogeneous pieces, projections, decomposition, and scalar compatibility.
- Polynomial and symmetric-algebra grading.
- Positive ideal, augmentation, and degree-zero coefficients.
- The source's indexing and sign conventions.

### A3. Graded modules and maps

- Every field of `ModuleData` and `ModuleData.Hom`.
- Graded submodules, kernels, images, and quotients.
- Scalar quotients, finite products, and direct sums.
- Degree shifts and their maps.

### A4. Changing coefficients and twisting

- `CoefficientChange` and the direction of scalar transport.
- `ReflectionPairTranslation.Twist` and semilinear maps.
- Transport of grading, bases, and duals.
- Compatibility maps for word modules and sheaves.

### A5. Bases, minimal covers, and projectivity

- `NonnegativeBasis` and homogeneous basis degrees.
- Graded Nakayama and minimal homogeneous generators.
- Every field of `ModuleData.MinimalCover`.
- Construction, uniqueness, and lifting for minimal covers.
- Split presentations, projectivity, and graded projective-to-free results.

### A6. Hilbert series, Hilbert values, and characters

- Dimensions of graded pieces and formal Hilbert series.
- Numerical Hilbert values and convergence.
- `Hilbert.piece`, `Hilbert.term`, and `Hilbert.value`.
- The polynomial-ring Hilbert series and the homogeneous-free-basis formula.
- Basis-degree polynomials and independence of the chosen basis.
- `Graded.character` and the relation between character and graded rank.
- Sums, shifts, coefficient transport, and exact sequences.
- Defect pieces, positivity, and equality detection.

The entry must derive

\[
\operatorname{Hilb}(M;q)=\frac{\operatorname{grk}_A(M;q)}{(1-q)^N}
\]

for the relevant free module over a polynomial ring in \(N\) variables. It must explain both sides, numerical evaluation, and the dimension of the coefficient space.

### A7. Algebra for support, quotients, and comparison

- Quotient descent and kernel/image transport.
- Saturated submodules and scalar-quotient images.
- Free scalar-quotient presentations.
- Local membership in free or projective lattices.
- Kernel projectivity from two presentations of a common image.
- Applications to upper images and reverse kernel reconstruction.

## W. Reflection Frobenius extensions and word modules

This branch constructs modules from words and computes their coordinates, pairings, and characters. S7 develops their sheaf interpretation.

### W1. A reflection Frobenius extension

- The invariant coefficient subalgebra.
- Invariant and anti-invariant coordinates.
- The basis consisting of one and a root coordinate.
- Trace and the perfect trace pairing.

### W2. Paired modules and tensor induction

- Every field of `PairedModule` and `PairedBimodule`.
- Right coefficient action, balance, and symmetry.
- Restricting duality through the trace.
- Tensor extension of pairings and induced modules/bimodules.

### W3. Word modules and homogeneous bases

- `bottSamelson`, the empty word, and prepending a generator.
- `BottIndex`, subexpressions, basis degrees, and weights.
- Left and right actions.
- The word pairing and its degree.

### W4. Evaluation coordinates and stalk images

- Subexpression evaluation, wall maps, and evaluation matrices.
- Integral injectivity, denominators, and lifting.
- Weight projections and `bottStalk`.
- The reduced-word top stalk and support below the word product.

### W5. Two-stalk lattices and their kernels

- Pair-projection images and quotients.
- Twisting the second scalar action and identifying the head pair.
- Head projections, wall flips, and saturation.
- `BottKernelExact`.
- Simultaneous construction of free stalks and free edge kernels.

### W6. Images over sets of weights

- Coordinate images and restriction.
- Upper sets, simple union, and simple intersection.
- Compatible upper images and projectivity.
- Common kernels and two-stage projections.
- Prime coefficient-character classes, diagonal stabilizers, and local projectors.
- Denominator removal and global lifting.

### W7. Word characters

- Graded and polynomial presentations of stalk data.
- Stalk-character polynomials.
- Ascent/descent exact sequences and the character recursion.
- Equality with positive Hecke-word coefficients and the top normalization.

## S. Moment-graph sheaves, support, and duality

This branch starts with general sheaf definitions, constructs boundary objects, and establishes their pairings and actual-character reciprocity.

### S1. Ordered graphs and labels

- Every field of `OrderedGraph`.
- Bruhat reflection graphs and root labels.
- Incoming/outgoing edges, `GraphMap`, and `GraphEquiv`.

### S2. Sheaves, sections, and boundary data

- Every field of `Sheaf`, `GradedSheaf`, and `FreeSheaf`.
- Vertex/edge modules and the two restriction maps.
- Upper-quotient conditions.
- Assignments, compatibility, sections over subsets, and global generation.
- Flabbiness, edge flabbiness, closed-under subsets, and relative extension.
- Boundary modules, maps, and images.
- Selected outgoing kernels, costalks, and their grading.

### S3. Operations and morphisms

- Zero objects, products, sums, and shifts.
- Induced restriction, lower extension, pullback, and reindexing.
- Coefficient change, tensor base change, and constraint maps.
- Graded `Hom`, `OnHom`, and `Endomorphism`.
- Ungraded `Iso`, `AboveIso`, and `OnIso`; graded `Iso` and `OnIso`.
- Extension of morphisms and descent through edge quotients.

### S4. Boundary sheaves and minimal extension

- Minimal covers of actual boundary images.
- Every field of `BoundarySheaf`.
- Attaching a bottom vertex; existence and uniqueness.
- The chosen Bruhat boundary sheaf.
- Lower and upper interval restrictions.

### S5. Summands, primitive objects, and decomposition

- `SplitIn`, inclusions, retractions, projectors, and image sheaves.
- Primitivity, indecomposability, top splitting, and recognition.
- `BoundaryModels` and the graded inductive construction `ModelSum`.
- Decomposition and multiplicity polynomials.

### S6. Integral support and cut operators

- Projection modules and modules of supported sections.
- Label products and `IntegralSupport.cut`.
- Annihilators and balance for integral cuts.
- Incoming label products and the relation between support and stalk duals.

### S7. Sheaves associated to words

- The sheaf associated to pair-projection data.
- Graded stalks, edge maps, and the quotient condition.
- Word modules as global sections.
- Global generation, flabbiness, and boundary summands.

### S8. Perfect pairings and adjoints

- `BruhatGraph.SectionDuality` and `FreeSheaf.SectionDuality`.
- Every field of `PerfectPairing` and `SymmetricPerfectPairing`.
- Costalk duality and degree shifts.
- Integral adjoints and preservation of grading, support, and kernels.
- Descent to sheaf maps, adjoint image sheaves, and duality on images.
- Primitive recognition and the canonical boundary pairing.

### S9. Stalk characters and actual-character reciprocity

- Stalk and full-kernel characters.
- Sums, shifts, isomorphisms, and coefficient change.
- Word reciprocity and R-convolution.
- Simultaneous stalk/costalk decomposition.
- Cancellation of lower terms and reciprocity for the actual character \(C\).
- Full-kernel characters and normalized endpoint formulas.

### S10. Related character-identification conditions

- Section-duality, costalk-freeness, and stalk-character conditions as stated in Lean.
- Local intersection maps and their properties.
- The local-degree result with its nonzero-diagonal hypothesis.
- The relationship between these conditions, \(C\), and the canonical family \(P\).
- Precise correspondence with the OpenAI notes.

## O. Reflection orders, dihedral combinatorics, and paths

This branch develops edge orders, reconstruction of reflection edges, and the transfer products transported by an interval order isomorphism.

### O1. Geometric orders on roots

- Height, normalized roots, positive/generic functionals, and slopes.
- Every field of `RatioOrder`.
- Adapted orders, chambers, and rotation.
- Distinct slopes on the entire positive-root set; finite edge-label sets used in interval schedules.

### O2. Dihedral systems inside a root plane

- Every field of `PlaneBasis`.
- The induced Coxeter system and `PlaneBasis.InducedSigned`.
- Correspondence of reflections, signs, and inversions.
- Relative length/order, minimal coset representatives, and interval transport.

### O3. Dihedral interval combinatorics

- Alternating words, rotations, and signed indices.
- Odd-gap reflection edges.
- Rank and endpoint flips.
- Relative interval transport and later-edge counts.

### O4. Inversion changes and geometric plane weights

- Inversion-indicator vectors and the partner involution.
- Contributing pairs and half-pairs.
- Plane defects, nonnegative integral weights, and finite support.
- The geometric weight-sum identity and its relation to length.

### O5. Reconstruction of reflection edges

- `DiamondEdges` and soundness of diamond closure.
- Reconstruction of reflection edges, including non-cover edges.
- Transport under interval order isomorphisms.
- The role of geometric weights in reconstruction.

### O6. Schedules and their transport

- Scores, sorting, ties, and blocks.
- Transported edges, scores, and schedules.
- Chronological order and transfer-product order.
- Upper-interval restrictions, cutoffs, and suffixes.

### O7. Paths and transfer products

- `SchedulePaths.IsPath`, path weights, and subpaths.
- Elementary transfers, dispatch, and products.
- Path expansion of dispatch entries.
- Adapted-order recursion and dihedral block reversal.
- Transverse pencils and the needed independence statements.
- The Dyer identity for the geometric orders established in Lean.

## L. Localization and comparison of embedded images

This branch turns rank-two geometry into a comparison of submodules of one edge module.

### L1. Plane and edge localizations

- Plane ideals, primality, `planePrime`, and `PlaneRing`.
- Which root labels become units.
- Edge coefficient rings, localized quotients, and root reduction.
- Compatibility of quotient and localization maps.

### L2. Localizing graph sheaves

- Base change of finite sections, kernels, and images.
- Edges killed by invertible labels and the surviving coset graph.
- Induced/localized labels and restriction to surviving components.

### L3. Dihedral structure models

- Structure sheaves and orbit splines.
- Interpolation roots and external edge constraints.
- Model products and `HasFlowDown`.
- Global generation, flabbiness, and quotient properties.
- Products describing supported outgoing kernels.

### L4. Local model decomposition

- Minimality with respect to the maximal ideal.
- Every field of `Sheaf.LocalModels`.
- The ungraded inductive construction `Sheaf.ModelSum`.
- Downward decomposition over a local ring.
- Decomposition of the localized actual boundary sheaf.

### L5. Polynomial correction factors

- Reduced roots, representatives, and association up to a unit.
- `edgeFactor`, nonvanishing, and homogeneity.
- Its degree from the geometric plane-weight identity.
- Polynomial lifts and multiplication maps.
- Local association with the dihedral model products.

### L6. Embedded lower and upper images

- The two images inside the same edge module.
- `ScaledImages` and its elementwise meaning.
- Isomorphism transport and model sums.
- Upper-kernel saturation and freeness of its scalar-quotient image.

### L7. From local comparison to the global edge inclusion

- Denominators and generic spanning.
- Height-one membership for the relevant free target.
- Local scaled-image equality from the dihedral calculation.
- Primes dividing the denominator.
- The global lower-image inclusion in the corrected upper image.
- The upper-kernel freeness hypothesis supplied later by induction.

## I. Hilbert comparison and combinatorial invariance

This branch combines the outputs in the Lean proof order: comparison, simultaneous R-invariance and suffix freeness, and canonical KL invariance.

### I1. A single edge comparison

- The exact sequence for removing one outgoing condition.
- Hilbert values of kernels and images.
- Scalar quotients and homogeneous multiplication.
- Edge-factor degree, `stateScale`, and `normalizedKernel`.
- The universal positive transfer coefficient.
- Equality in the numerical comparison and equality of embedded images.

### I2. A complete schedule

- `remainingConditions`, `scheduleState`, and `idealState`.
- One-step inequalities, monotonicity, and the iterated inequality.
- Chronological schedules and reversed dispatch lists.

### I3. Endpoint identities

- The initial full outgoing kernel and the final stalk.
- Their expressions through the actual character and duality.
- Native reciprocity and the transported R-matrix.
- Endpoint equality when all R-entries agree.

### I4. Equality and reverse reconstruction of freeness

- Exact endpoint comparison and vanishing numerical deficits.
- Hilbert detection of equality of embedded images.
- Two presentations of the common image.
- Projectivity of the next kernel and its homogeneous free basis.
- Reverse traversal from the no-condition stalk to all suffix kernels.

### I5. Simultaneous induction for R and suffix kernels

- `FreeSuffixes` and the joint assertion for an isomorphism and its inverse.
- Rank induction and the singleton case.
- Smaller upper intervals supplying target-kernel freeness.
- Smaller initial intervals supplying known bottom-row R-entries.
- Cancellation against the source actual-character vector.
- Opposite inequalities, the new R-equality, and transport of all entries.
- New suffix freeness in both directions.

### I6. Canonical KL invariance

- The common R-matrix and normalized canonical P-vectors.
- Induction on proper upper intervals.
- The reciprocal bottom-coordinate difference.
- Strict degree bounds and rigidity.
- Invariance for finitely generated Coxeter systems.

### I7. The unrestricted theorem

- Finite-support interval models from C5 and polynomial transport.
- Applying the finite-generator theorem.
- Invariance for intervals in arbitrary Coxeter systems.

## Entry design and source correspondence

Every defining entry explains its ambient objects, notation, fields or defining conditions, construction, first properties, and later use. Important intermediate theorems have their own statements and detailed proofs. Routine coercions, transports, and API variants can be explained with their owning construction.

Topic pages connect these entries: what is being constructed, which earlier results supply the inputs, and where the output is used. The [relationship map](knowledge-base-relationships.md) records these interfaces.

Existing stable node IDs should survive the reorganization. Moved pages receive generated redirects. The term registry resolves vocabulary through Python or TypeScript.

Source correspondence should preserve these distinctions:

- The main Lean route uses actual-character reciprocity, simultaneous R-invariance and suffix freeness, and then canonical P rigidity.
- The notes' character-identification presentation belongs alongside S10 with its hypotheses and relation to that route.
- The geometric plane-weight identity belongs in O4. The polynomial edge-factor degree belongs in L5 and uses O4.
- General graph/module definitions can be introduced before specialization to Coxeter data.
- The Dyer theorem retains the order hypotheses established in the local source.

## Complete structure and inductive-construction assignment

This table is generated from the local declaration index and explicit topic assignments. Python resolves source links against the fixed snapshot.

<!-- generated-structure-map -->
| Declaration | Kind | Proposed home |
|---|---|---|
| [Graded.ModuleData · GradedModules.lean:1051](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1051) | structure | A3 |
| [Graded.ModuleData.Hom · GradedModules.lean:1073](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1073) | structure | A3 |
| [CoefficientChange · BottSamelson.lean:1777](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1777) | structure | A4 |
| [ReflectionPairTranslation.Twist · Frobenius.lean:2045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L2045) | structure | A4 |
| [Graded.ModuleData.MinimalCover · GradedModules.lean:1175](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1175) | structure | A5 |
| [Graded.NonnegativeBasis · SheafMorphisms.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L20) | structure | A5 |
| [FiniteIntervalModel · Invariance.lean:476](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L476) | structure | C5 |
| [NormalizedKL · Model.lean:55](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean#L55) | structure | H4 |
| [MomentGraph.Sheaf.LocalModels · CharacterReciprocity.lean:352](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L352) | structure | L4 |
| [MomentGraph.Sheaf.ModelSum · CharacterReciprocity.lean:364](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L364) | inductive | L4 |
| [TitsSpace.RatioOrder · DyerPaths.lean:1181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean#L1181) | structure | O1 |
| [TitsSpace.PlaneBasis · Decomposition.lean:619](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L619) | structure | O2 |
| [TitsSpace.PlaneBasis.InducedSigned · Decomposition.lean:965](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L965) | structure | O2 |
| [DiamondEdges · ReflectionSchedules.lean:1529](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean#L1529) | inductive | O5 |
| [MomentGraph.GraphEquiv · GradedSheaves.lean:270](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L270) | structure | S1 |
| [MomentGraph.GraphMap · MinimalExtensions.lean:1457](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L1457) | structure | S1 |
| [MomentGraph.OrderedGraph · Sheaves.lean:21](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L21) | structure | S1 |
| [BruhatGraph.FreeSheaf · CharacterReciprocity.lean:140](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L140) | structure | S2 |
| [MomentGraph.GradedSheaf · GradedSheaves.lean:20](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L20) | structure | S2 |
| [MomentGraph.Sheaf · Sheaves.lean:28](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean#L28) | structure | S2 |
| [MomentGraph.GradedSheaf.Endomorphism · SheafMorphisms.lean:996](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L996) | structure | S3 |
| [MomentGraph.GradedSheaf.Hom · SheafMorphisms.lean:570](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L570) | structure | S3 |
| [MomentGraph.GradedSheaf.Iso · MinimalExtensions.lean:210](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L210) | structure | S3 |
| [MomentGraph.GradedSheaf.OnHom · SheafMorphisms.lean:578](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L578) | structure | S3 |
| [MomentGraph.GradedSheaf.OnIso · MinimalExtensions.lean:214](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L214) | structure | S3 |
| [MomentGraph.Sheaf.AboveIso · GradedSheaves.lean:692](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L692) | structure | S3 |
| [MomentGraph.Sheaf.Iso · GradedSheaves.lean:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L521) | structure | S3 |
| [MomentGraph.Sheaf.OnIso · GradedSheaves.lean:970](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L970) | structure | S3 |
| [MomentGraph.BoundarySheaf · GradedSheaves.lean:1138](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L1138) | structure | S4 |
| [MomentGraph.GradedSheaf.BoundaryModels · MinimalExtensions.lean:661](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L661) | structure | S5 |
| [MomentGraph.GradedSheaf.ModelSum · MinimalExtensions.lean:672](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L672) | inductive | S5 |
| [MomentGraph.GradedSheaf.SplitIn · SheafMorphisms.lean:1354](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L1354) | structure | S5 |
| [BruhatGraph.FreeSheaf.SectionDuality · CharacterReciprocity.lean:170](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L170) | structure | S8 |
| [BruhatGraph.SectionDuality · Support.lean:1432](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1432) | structure | S8 |
| [MomentGraph.GradedSheaf.PerfectPairing · Support.lean:1850](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1850) | structure | S8 |
| [MomentGraph.GradedSheaf.SymmetricPerfectPairing · EdgeLocalization.lean:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L941) | structure | S8 |
| [FrobeniusDuality.PairedBimodule · Frobenius.lean:295](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L295) | structure | W2 |
| [FrobeniusDuality.PairedModule · Frobenius.lean:226](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L226) | structure | W2 |
<!-- /generated-structure-map -->

## Module-to-topic coverage map

This is a source-coverage index. A module can contribute to several mathematical homes.

<!-- generated-module-map -->
| Source module | Proposed topic homes |
|---|---|
| [BalancedPairings.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean) | S6, S8 |
| [BottSamelson.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean) | A4, W4, W5, W6, W7, S7 |
| [Bruhat.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Bruhat.lean) | C3, C4 |
| [CanonicalKL.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean) | H4, H5 |
| [CharacterReciprocity.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean) | H5, A4, S2, S5, S8, S9, L4, L6 |
| [Comparison.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean) | I2, I4, I6 |
| [Coxeter.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean) | C1, C2 |
| [Decomposition.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean) | S5, O2, O5 |
| [Dihedral.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean) | C1, C2, O2, O3, H5 |
| [DihedralIntervals.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean) | O3, L3 |
| [DyerPaths.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DyerPaths.lean) | S9, C5, O1, O2, O3, O5, O7 |
| [EdgeLocalization.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean) | O6, O7, S3, S4, S8, S9, S10, I3 |
| [Frobenius.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean) | W1, W2, W3, W4, W5, A4 |
| [GradedModules.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean) | A2, A3, A5, A7 |
| [GradedSheaves.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean) | S2, S3, S4 |
| [Hecke.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Hecke.lean) | H1, H2, H3, H5 |
| [HilbertSeries.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean) | A6 |
| [IntegralPairings.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean) | W7, S8 |
| [Invariance.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean) | C4, C5, I5, I6, I7 |
| [MinimalExtensions.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean) | S1, S3, S4, S5 |
| [Model.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Model.lean) | C4, H4, H5 |
| [ModuleAlgebra.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ModuleAlgebra.lean) | A1, A2, A6, A7 |
| [OrdinaryR.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/OrdinaryR.lean) | H3 |
| [PlaneLocalization.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean) | A1, A7, L1, L2, L3, L4, L5, L6 |
| [PositiveTransfer.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean) | S8, S10, A6, A7, O6, I1, I2, I4 |
| [ReflectionOrders.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionOrders.lean) | O1, O2, O6, O7 |
| [ReflectionPlane.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionPlane.lean) | R4, R6 |
| [ReflectionSchedules.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/ReflectionSchedules.lean) | O1, O3, O4, O5, O6, O7, A1, L5 |
| [SheafMorphisms.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean) | A5, A6, S3, S4, S5, S10 |
| [Sheaves.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Sheaves.lean) | S1, S2, S3, L3 |
| [SimultaneousInvariance.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean) | C4, O6, I3, I4, I5, I6 |
| [Support.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean) | A4, A6, S3, S6, S7, S8, S9 |
| [TerminalKernels.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean) | A7, S3, L2, L4, L6, L7, I2, I3 |
| [Tits.lean](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean) | C5, R1, R2, R3, R4, R5, R6, A1 |
<!-- /generated-module-map -->
