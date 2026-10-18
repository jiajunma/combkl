---
id: kl.comparison.reverse_freeness
title: Recovering terminal-kernel freeness by reverse traversal
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.free_suffixes
- kl.comparison.no_deficit
- kl.sheaves.hilbert_detection
- kl.notes.graded_projective_free
- kl.detail.reverse_projectivity
- kl.detail.scaled_images
lean:
  repository: openai-kl
  modules:
  - SimultaneousInvariance
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq
  - OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:181
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1052
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the mathematical scope of its Lean declarations?
  verdict: The stated hypotheses and conclusion follow the fixed source; explanatory
    derivations retain the original proof route.
tags:
- Kazhdan-Lusztig
- induction
---

# Recovering terminal-kernel freeness by reverse traversal

If every lower edge image in a schedule equals its corrected upper edge image, then all terminal kernels at every vertex are free.

*Proof.*

### Step 1. State the induction on suffixes

Let \(p\) be a finite chronological edge list. Assume the embedded image equality for every suffix \(e::q\) of \(p\). We prove that \(K_x(F_q(x))\) is free for every suffix \(q\) and every vertex \(x\). This is an induction on the length of \(p\), starting from the empty list and adding conditions back.

For \(p=[]\), the only suffix is empty and \(F_{[]}(x)=\varnothing\). Its kernel imposes no equations, so it is the whole stalk \(B^x\), which is free.

### Step 2. Reduce a nonempty list to its tail

Write \(p=e::r\), with \(e:x\to y\). Every suffix of \(r\) is also a suffix of \(p\), so the given equalities restrict to \(r\). The induction hypothesis gives freeness at every vertex for every suffix of \(r\).

A suffix \(q\) of \(p\) is either a suffix of \(r\), already handled, or the whole list \(p\). It remains to handle \(p\).

### Step 3. Identify the only changed kernel

At a vertex \(z\ne x\), adding \(e\) does not change its outgoing conditions; its kernel is the already free tail kernel. At \(x\), put
\[
S=K_x(F_r(x)),\qquad T=K_y(F_r(y)).
\]
Both modules are free by the tail induction hypothesis. The new lower kernel is
\(S\cap\ker\rho_{x,e}\).

### Step 4. Check every hypothesis of reverse projectivity

Apply [[node:kl.detail.reverse_projectivity]] with
\(f=\rho_{x,e}\), \(g=\rho_{y,e}\), and \(\psi\) multiplication by the edge factor \(f_e\).

The given equality is exactly \(f(S)=\psi(g(T))\). The upper quotient rule gives \(\ker g=\alpha_eB^y\). The label \(\alpha_e\) is nonzero and acts injectively on the free stalk \(B^y\). Multiplication by \(f_e\) is injective on the edge module by the established regularity of the actual edge factor.

For saturation, suppose \(\alpha_ev\in T\). For each remaining outgoing edge \(h\) at \(y\),
\(\alpha_e\rho_{y,h}(v)=\rho_{y,h}(\alpha_ev)=0\).
The incoming label \(\alpha_e\) acts injectively on each such edge module, so \(\rho_{y,h}(v)=0\). Thus \(v\in T\). All hypotheses are now checked, and the new lower kernel is projective.

### Step 5. Upgrade projectivity to freeness

The new kernel is a homogeneous submodule of a finite nonnegatively graded polynomial-ring module. It is finitely generated because the polynomial ring is Noetherian. Its grading is nonnegative because it inherits the stalk grading.

The homogeneous-basis theorem [[node:kl.notes.graded_projective_free]] therefore applies to this projective module and provides a homogeneous free basis. This gives freeness at \(x\), completing the suffix induction.

If image equalities were obtained from endpoint equality, first use [[node:kl.comparison.no_deficit]] and Hilbert detection to establish them. They are inputs to Step 4, not conclusions assumed earlier in the comparison.

## References

[6. Reciprocity and simultaneous induction](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L194).

## Lean formalization

`OAI.KLInvariance.BruhatGraph.schedule_kernels_free_of_images_eq`: [SimultaneousInvariance.lean:181](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L181).

`OAI.KLInvariance.BruhatGraph.partial_kernel_free_of_image_eq`: [PositiveTransfer.lean:1052](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1052).
