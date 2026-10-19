---
id: kl.algebra.component_transport
title: Components under homogeneous maps and scalar multiplication
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.algebra.grading_components
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - GradedModules
  declarations:
  - OAI.KLInvariance.Graded.map_component
  - OAI.KLInvariance.Graded.kernel_homogeneous
  - OAI.KLInvariance.Graded.range_homogeneous
  - OAI.KLInvariance.Graded.component_homogeneous_smul
  - OAI.KLInvariance.Graded.scalar_range_homogeneous
  - OAI.KLInvariance.Graded.ModuleData.Hom.component
  - OAI.KLInvariance.Graded.ModuleData.Hom.mem_of_map_mem
  - OAI.KLInvariance.Graded.ModuleData.Hom.homogeneous_preimage
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:891
    format: lean-location
    note: OAI.KLInvariance.Graded.map_component
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:916
    format: lean-location
    note: OAI.KLInvariance.Graded.kernel_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:928
    format: lean-location
    note: OAI.KLInvariance.Graded.range_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:938
    format: lean-location
    note: OAI.KLInvariance.Graded.component_homogeneous_smul
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:948
    format: lean-location
    note: OAI.KLInvariance.Graded.scalar_range_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1157
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.component
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1327
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.mem_of_map_mem
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedModules:1336
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.Hom.homogeneous_preimage
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the grading, scalar, finiteness and convergence hypotheses retained?
  verdict: Read map_component and the kernel/range/scalar consequences, plus Hom homogeneous
    preimages and injective degree detection. The argument uses only finite component
    decompositions and additive linearity.
tags:
- Kazhdan-Lusztig
- graded-algebra
---

# Components under homogeneous maps and scalar multiplication

Let \(k\) be a field and \(A\) a commutative ring. Let \(M,N\) have direct-sum \(k\)-vector-space gradings and \(A\)-module structures. Suppose an \(A\)-linear map \(f:M\to N\) has degree \(r\):
\(f(M_i)\subseteq N_{i+r}\).
Then
\[
\pi_n^N(f(m))=f(\pi_{n-r}^M(m)).
\]
Both the kernel and the image are closed under all homogeneous component maps.

For a degree-zero map, surjectivity gives homogeneous preimages in the same degree; injectivity implies that a vector whose image lies in \(N_n\) already lies in \(M_n\).

*Proof.*

### Step 1. Apply the map to a homogeneous decomposition

Decompose \(m=\sum_i m_i\). Additivity gives
\(f(m)=\sum_i f(m_i)\), and each summand belongs to \(N_{i+r}\).

Only the index \(i=n-r\) can contribute to the degree-\(n\) component. Uniqueness of decomposition therefore gives the displayed component identity.

### Step 2. Close the kernel under components

If \(f(m)=0\), apply the identity at degree \(n+r\):
\[
f(\pi_n^M(m))=\pi_{n+r}^N(f(m))=0.
\]
Thus every component of a kernel vector is again in the kernel.

### Step 3. Close the image under components

For \(y=f(m)\),
\[
\pi_n^N(y)=f(\pi_{n-r}^M(m)).
\]
The right side lies in the image, proving closure under components.

### Step 4. Obtain homogeneous preimages and detect homogeneous vectors

Take \(r=0\). If \(f\) is surjective and \(y\in N_n\), choose \(m\) with \(f(m)=y\). Then
\[
f(\pi_n^M(m))=\pi_n^N(y)=y,
\]
giving a preimage in \(M_n\).

If \(f\) is injective and \(f(m)\in N_n\), the same equality gives
\(f(\pi_n^M(m))=f(m)\). Injectivity implies \(m=\pi_n^M(m)\in M_n\). In particular the inverse of a bijective degree-zero map preserves degrees.

### Step 5. Apply the identity to a homogeneous scalar

In the compatibly graded \(A\)-module setting, if \(a\in A_r\), multiplication \(m\mapsto am\) is an \(A\)-linear map of degree \(r\). Thus
\[
\pi_n(am)=a\,\pi_{n-r}(m).
\]
Its image \(aM\) is homogeneous by Step 3. This supplies the grading used on scalar quotients.

For \(A=k[X]\), multiplication by \(X\) has degree one, and the formula reads
\(\pi_n(Xf)=X\pi_{n-1}(f)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Graded.map_component`: [GradedModules.lean:891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L891).

`OAI.KLInvariance.Graded.kernel_homogeneous`: [GradedModules.lean:916](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L916).

`OAI.KLInvariance.Graded.range_homogeneous`: [GradedModules.lean:928](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L928).

`OAI.KLInvariance.Graded.component_homogeneous_smul`: [GradedModules.lean:938](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L938).

`OAI.KLInvariance.Graded.scalar_range_homogeneous`: [GradedModules.lean:948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L948).

`OAI.KLInvariance.Graded.ModuleData.Hom.component`: [GradedModules.lean:1157](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1157).

`OAI.KLInvariance.Graded.ModuleData.Hom.mem_of_map_mem`: [GradedModules.lean:1327](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1327).

`OAI.KLInvariance.Graded.ModuleData.Hom.homogeneous_preimage`: [GradedModules.lean:1336](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedModules.lean#L1336).
