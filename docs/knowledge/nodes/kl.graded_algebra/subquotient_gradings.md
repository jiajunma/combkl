---
id: kl.algebra.subquotient_gradings
title: Grading submodules and quotients through their components
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.homogeneous_subquotients
- kl.algebra.component_transport
- kl.sheaves.graded_module
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.internal_of_components
  - OAI.KLInvariance.Graded.image_isInternal
  - OAI.KLInvariance.Graded.sub_isInternal
  - OAI.KLInvariance.Graded.quotient_isInternal
  - OAI.KLInvariance.Graded.subPiece_eq_bot
  - OAI.KLInvariance.Graded.quotientPiece_eq_bot
  - OAI.KLInvariance.Graded.ModuleData.sub
  - OAI.KLInvariance.Graded.ModuleData.quotient
  - OAI.KLInvariance.Graded.ModuleData.subtype
  - OAI.KLInvariance.Graded.ModuleData.quotientMap
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:681
    format: lean-location
    note: OAI.KLInvariance.Graded.internal_of_components
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:705
    format: lean-location
    note: OAI.KLInvariance.Graded.image_isInternal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:746
    format: lean-location
    note: OAI.KLInvariance.Graded.sub_isInternal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:774
    format: lean-location
    note: OAI.KLInvariance.Graded.quotient_isInternal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:802
    format: lean-location
    note: OAI.KLInvariance.Graded.subPiece_eq_bot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:809
    format: lean-location
    note: OAI.KLInvariance.Graded.quotientPiece_eq_bot
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1077
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.sub
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1089
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1141
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.subtype
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1132
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.quotientMap
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read sub_isInternal and quotient_isInternal via image_isInternal. Included
    well-defined quotient components, finite-sum independence, scalar compatibility
    and the precise finiteness assumptions.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Grading submodules and quotients through their components

Let \(k\) be a field, \(A\) a commutative \(k\)-algebra, and \(M=\bigoplus_nM_n\) a compatibly graded \(A\)-module and let \(S\subseteq M\) be homogeneous: every component of each \(s\in S\) belongs to \(S\). Then
\[
S=\bigoplus_n(S\cap M_n),\qquad
M/S=\bigoplus_n\operatorname{im}(M_n\to M/S).
\]
The inclusion \(S\to M\) and quotient map \(M\to M/S\) have degree zero.

These constructions preserve nonnegative grading. They preserve finite generation for quotients; the source's submodule construction uses a Noetherian coefficient ring to supply finite generation.

*Proof.*

### Step 1. Restrict the component maps to S

For \(s\in S\), homogeneity gives \(\pi_n(s)\in S\cap M_n\). The finite component sum in \(M\) is therefore a finite component sum inside \(S\).

If a finite sum of vectors of different degrees in \(S\) is zero, it is also zero in \(M\). Uniqueness there forces every summand to be zero. This proves the direct-sum decomposition of \(S\).

### Step 2. Define quotient components independently of representatives

For a class \([m]\in M/S\), define its degree-\(n\) component as \([\pi_n(m)]\).

If \(m\) is changed to \(m+s\), with \(s\in S\), this class changes by \([\pi_n(s)]=0\). The rule is therefore well defined and linear. Its values lie in the image of \(M_n\) under the quotient map.

### Step 3. Prove the quotient decomposition

Every class is the finite sum
\([m]=\sum_n[\pi_n(m)]\).

For uniqueness, suppose \(\sum_n[m_n]=0\), with each \(m_n\in M_n\) and the sum finite. Then \(\sum_nm_n\in S\). Applying \(\pi_j\) and using homogeneity of \(S\) gives \(m_j\in S\). Thus each class \([m_j]\) is already zero.

This proves that the quotient pieces form a direct sum.

### Step 4. Verify scalar degrees and the natural maps

For \(a\in A_i\) and \(m\in M_j\), the product \(am\) lies in \(M_{i+j}\). Inside \(S\), closure under \(A\)-multiplication keeps it in \(S\). In the quotient, \(a[m]=[am]\) has degree \(i+j\).

Inclusion preserves the degree of a vector, and the quotient map sends \(M_n\) into its defining image piece. Both are therefore degree zero.

### Step 5. Check the nonnegative and finite fields

If \(M_n=0\), then both \(S\cap M_n\) and its quotient image are zero. Hence nonnegative support passes to both constructions.

Images of a finite generating set generate \(M/S\). Over a Noetherian ring, every submodule of the finite module \(M\) is finite, supplying the submodule field required by ModuleData. Applying the [[node:kl.algebra.component_transport|homogeneous-map theorem]] gives the source's graded kernel and range constructions.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.internal_of_components`: [GradedModules.lean:681](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L681).

`OAI.KLInvariance.Graded.image_isInternal`: [GradedModules.lean:705](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L705).

`OAI.KLInvariance.Graded.sub_isInternal`: [GradedModules.lean:746](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L746).

`OAI.KLInvariance.Graded.quotient_isInternal`: [GradedModules.lean:774](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L774).

`OAI.KLInvariance.Graded.subPiece_eq_bot`: [GradedModules.lean:802](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L802).

`OAI.KLInvariance.Graded.quotientPiece_eq_bot`: [GradedModules.lean:809](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L809).

`OAI.KLInvariance.Graded.ModuleData.sub`: [GradedModules.lean:1077](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1077).

`OAI.KLInvariance.Graded.ModuleData.quotient`: [GradedModules.lean:1089](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1089).

`OAI.KLInvariance.Graded.ModuleData.subtype`: [GradedModules.lean:1141](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1141).

`OAI.KLInvariance.Graded.ModuleData.quotientMap`: [GradedModules.lean:1132](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1132).
