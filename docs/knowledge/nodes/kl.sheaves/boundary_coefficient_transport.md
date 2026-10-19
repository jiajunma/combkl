---
id: kl.sheaves.boundary_coefficient_transport
title: Boundary recognition after a change of coefficient coordinates
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.coefficient_change
- kl.sheaves.boundary_recognition
- kl.detail.indecomposable_boundary
- kl.detail.primitive_projectors
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_flabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_generated
  - OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_primitive
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_coefficientChange
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:342
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:348
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:368
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:380
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1619
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_primitive
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1709
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_coefficientChange
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Boundary recognition after a change of coefficient coordinates

Let \(e:A\xrightarrow{\sim}A'\) be a grading-preserving algebra isomorphism over a field. Assume both coefficient algebras are nonnegative domains, and \(A'\) is connected and Noetherian.

On a finite ordered graph with greatest vertex \(b\), let \(S\) be a normalized boundary sheaf with labels \(\alpha_e\) over \(A\), and let \(T\) be one with labels \(e(\alpha_e)\) over \(A'\). Then there is a graded sheaf isomorphism
\[
T\xrightarrow{\sim}{}^eS.
\]

*Proof.*

### Step 1. Transport the module and section properties

A free basis of each stalk of \(S\) becomes a free basis over \(A'\) by applying \(e\) to its coefficients. Thus \({}^eS\) has free stalks.

Its section equations are unchanged on underlying vectors. A global extension or a section realizing a prescribed stalk value for \(S\) therefore gives the corresponding extension or value for \({}^eS\). This proves flabbiness and global generation.

### Step 2. Transport the upper-quotient rule

An upper restriction has the same underlying map, so it remains surjective. In the transported scalar action,
\[
e(\alpha_e)\cdot m=\alpha_e m.
\]
Hence its old kernel \(\alpha_e S^{t(e)}\) is exactly the new submodule
\(e(\alpha_e)({}^eS)^{t(e)}\). This proves the upper-quotient rule with the new labels.

### Step 3. Preserve primitivity

Transporting component maps gives a bijection between graded endomorphisms of \(S\) and of \({}^eS\). The inverse changes coefficients back through \(e^{-1}\). This correspondence preserves composition, zero, and identity.

Consequently an idempotent on \({}^eS\) transports back to an idempotent on \(S\). The normalized boundary sheaf \(S\) has primitive identity, so this idempotent is zero or the identity. Transporting forward proves that \(1_{{}^eS}\) is primitive.

### Step 4. Supply the normalized top splitting

The top of \(S\) is \(A\), while that of \(T\) is \(A'\), each generated in degree zero. The map
\[
{}^eA\to A',\qquad a\mapsto e(a)
\]
is \(A'\)-linear: \(e(e^{-1}(a')a)=a'e(a)\). Its inverse is \(e^{-1}\), and both preserve degree.

These maps give inverse graded maps between \(T^b\) and \(({}^eS)^b\), hence the top splitting required for recognition.

### Step 5. Apply the recognition theorem over A'

The target \({}^eS\) has free stalks, the specified upper quotients, flabbiness, global generation, primitive identity, and a split normalized top. The graph and coefficient algebra satisfy the finite, connected, and Noetherian hypotheses.

Boundary recognition applied to \(T\) and \({}^eS\) gives the asserted graded sheaf isomorphism.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_free`: [Support.lean:342](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L342).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_upperQuotient`: [Support.lean:348](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L348).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_flabby`: [Support.lean:368](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L368).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_generated`: [Support.lean:380](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L380).

`OAI.KLInvariance.MomentGraph.GradedSheaf.coefficientChange_primitive`: [CharacterReciprocity.lean:1619](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1619).

`OAI.KLInvariance.MomentGraph.BoundarySheaf.iso_coefficientChange`: [CharacterReciprocity.lean:1709](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1709).
