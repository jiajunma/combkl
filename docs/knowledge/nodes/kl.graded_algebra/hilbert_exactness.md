---
id: kl.detail.hilbert_exactness
title: Hilbert additivity for homogeneous exact sequences
kind: theorem
status: proved
primary_topic: kl.graded_algebra
topics:
- kl.graded_algebra
uses:
- kl.detail.hilbert_values
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - HilbertSeries
  declarations:
  - OAI.KLInvariance.Hilbert.degreeMap_surjective
  - OAI.KLInvariance.Hilbert.finrank_exact
  - OAI.KLInvariance.Hilbert.value_exact_of_summable
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:202
    format: lean-location
    note: OAI.KLInvariance.Hilbert.degreeMap_surjective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:360
    format: lean-location
    note: OAI.KLInvariance.Hilbert.finrank_exact
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.HilbertSeries:392
    format: lean-location
    note: OAI.KLInvariance.Hilbert.value_exact_of_summable
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Hilbert additivity for homogeneous exact sequences

Let \(f:M\twoheadrightarrow N\) be a degree-zero surjective linear map of graded modules. Assume the homogeneous pieces of \(M\) are finite-dimensional. Then, for every integer \(n\),
\[
\dim M_n=\dim(\ker f)_n+\dim N_n.
\]
If \(q>0\) and the Hilbert series of \(M\) converges at \(q\), the kernel and target series also converge and
\[
H_M(q)=H_{\ker f}(q)+H_N(q).
\]
No free-module hypothesis is needed.

*Proof.*

### Step 1. Show surjectivity degree by degree

Given \(y\in N_n\), choose \(m\in M\) with \(f(m)=y\). Decompose \(m=\sum_jm_j\) into its finitely many homogeneous components. Since \(f\) preserves degree,
\(y=\sum_j f(m_j)\), with \(f(m_j)\in N_j\). Uniqueness of the direct-sum decomposition gives \(f(m_n)=y\). Thus the restricted map \(f_n:M_n\to N_n\) is surjective.

### Step 2. Identify the kernel and apply rank-nullity

An element of \(M_n\) lies in \(\ker f_n\) precisely when its underlying vector is killed by \(f\). This identifies \(\ker f_n\) with \((\ker f)\cap M_n\); the identification is the identity on underlying vectors in both directions.

The image \(N_n\) of the finite-dimensional space \(M_n\) is finite-dimensional. Rank-nullity for \(f_n\), followed by this kernel identification, proves the dimension formula.

### Step 3. Check convergence of both summands

The two dimensions on the right are nonnegative and individually at most \(\dim M_n\). Multiplying by \(q^n>0\) preserves these bounds. Each series is therefore dominated termwise by the convergent nonnegative series for \(M\), which proves convergence of both.

### Step 4. Sum the exact identities

Multiply the degreewise dimension equation by \(q^n\) and sum over \(n\in\mathbb Z\). Step 3 permits splitting the sum into the two convergent series, yielding the stated identity. The argument retains possible torsion in the modules; only the finite-dimensional graded pieces enter rank-nullity.

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.Hilbert.degreeMap_surjective`: [HilbertSeries.lean:202](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L202).

`OAI.KLInvariance.Hilbert.finrank_exact`: [HilbertSeries.lean:360](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L360).

`OAI.KLInvariance.Hilbert.value_exact_of_summable`: [HilbertSeries.lean:392](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/HilbertSeries.lean#L392).
