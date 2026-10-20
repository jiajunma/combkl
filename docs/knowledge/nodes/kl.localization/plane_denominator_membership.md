---
id: kl.local.plane_denominator_membership
title: Plane denominators force membership in a free edge-ring target
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.algebra.root_quotient_coordinates
- kl.algebra.scalar_quotient
- kl.algebra.projective_local_membership
- kl.local.root_factor_divisibility
lean:
  repository: openai-kl
  modules:
  - TerminalKernels
  declarations:
  - OAI.KLInvariance.BruhatGraph.mem_of_plane_denominators
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.TerminalKernels:992
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.mem_of_plane_denominators
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, finiteness and freeness hypotheses, original embedded
    submodules, localization multipliers and schedule assumptions explicit?
  verdict: Checked the two compatible actions, C-torsion-free ambient module and C-free
    target, the three quantified multiplier assumptions, both prime cases, and the
    exact specialization of the reviewed prime-removal theorem.
tags:
- Kazhdan-Lusztig
- global-inclusion
---

# Plane denominators force membership in a free edge-ring target

Let \(W\) be a finite-generator real Coxeter system, \(A\) its polynomial coefficient algebra from a real basis of the extended realization, and \(a\) a positive root. Write \(\lambda(a)\) for its root polynomial, and put
\[
C=A/(\lambda(a)),\qquad \overline r\in C\text{ for the class of }r\in A.
\]
Let \(N\) have compatible \(A\)- and \(C\)-module actions, and suppose \(N\) is torsion-free over \(C\). Let \(S\subseteq N\) be an \(A\)-submodule whose same-carrier \(C\)-submodule \(S_C\) is free.

Fix \(z\in N\), and assume the following data.

- A scalar \(c\in A\) satisfies \(\overline c\ne0\) and \(cz\in S\).
- Every prime element \(\pi\in C\) dividing \(\overline c\) is associated to \(\overline{\lambda(\beta)}\) for some positive root \(\beta\ne a\).
- For every positive root \(\beta\ne a\), there is \(s\in A\) with
\[
s\notin\mathfrak p_{\operatorname{span}\{a,\beta\}},
\qquad sz\in S.
\]

Then \(z\in S\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Prime divisors of one multiplier organize the local-to-global step.**

**OpenAI notes:** The notes use membership in a free target at height-one primes. Primes avoiding all reduced root labels give the full localized edge module; root primes use the dihedral local comparison. [edge:lattice](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L26), [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The proof fixes one global multiplier, the correction lift times the outgoing label product. A prime dividing its reduction is associated to a reduced root and receives the corresponding plane witness. A prime not dividing it uses the global multiplier itself. The free-target prime-removal theorem then gives membership. [TerminalKernels:992](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L992), [TerminalKernels:1045](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L1045).

**Role in the proof:** The Blueprint follows these two prime cases and checks quotient-ring freeness, torsion-free cancellation, nonzero global multiplication and every local witness before concluding the inclusion.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Pass the global multiplier to the quotient coefficient ring

The [[node:kl.algebra.root_quotient_coordinates|root-quotient coordinate theorem]] identifies \(C\) with a polynomial algebra over \(\mathbb R\), so \(C\) is a unique factorization domain. The compatible actions identify \(cz\) with \(\overline c\,z\).

Thus the first assumption supplies the nonzero global multiplier required by the [[node:kl.algebra.projective_local_membership|prime-denominator membership theorem]] over \(C\), with free target \(S_C\subseteq N\).

### Step 2. Produce a local witness for a prime dividing the global multiplier

Let \(\pi\) be prime in \(C\), and first suppose \(\pi\mid\overline c\). Choose \(\beta\ne a\) with
\(\pi\sim\overline{\lambda(\beta)}\)
by the second assumption. Choose \(s\notin\mathfrak p_{\operatorname{span}\{a,\beta\}}\) with \(sz\in S\) by the third.

The [[node:kl.local.root_factor_divisibility|root-factor divisibility theorem]] gives
\[
\overline{\lambda(\beta)}\mid\overline s
\quad\Longleftrightarrow\quad
s\in\mathfrak p_{\operatorname{span}\{a,\beta\}}.
\]
The right side is false, so the left side is false. Associated elements have the same divisibility relation, hence \(\pi\nmid\overline s\).

Compatibility of actions gives \(\overline s\,z=sz\in S_C\). Thus \(\overline s\) is the required multiplier not divisible by \(\pi\).

### Step 3. Treat primes not dividing the global multiplier

If \(\pi\nmid\overline c\), use \(\overline c\) itself. It is not divisible by \(\pi\), and Step 1 gives \(\overline c\,z\in S_C\).

Combining Steps 2–3 yields, for every prime \(\pi\in C\), a multiplier \(d_\pi\) satisfying
\[
\pi\nmid d_\pi,\qquad d_\pi z\in S_C.
\]

### Step 4. Apply prime-denominator membership to the free target

The [[node:kl.algebra.projective_local_membership|prime-denominator membership theorem]] applies: \(C\) is a UFD, \(N\) is torsion-free, \(S_C\) is free and therefore projective, Step 1 gives a nonzero global multiplier, and Steps 2–3 supply the prime witnesses.

Its finite prime-factor removal argument gives \(z\in S_C\). This submodule has the same carrier as \(S\), so \(z\in S\), as asserted.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.mem_of_plane_denominators`: [TerminalKernels.lean:992](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/TerminalKernels.lean#L992).
