---
id: kl.detail.indecomposable_boundary
title: Indecomposability of the normalized boundary sheaf
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.sheaves.boundary_sheaf
- kl.detail.sheaf_morphism
- kl.notes.graded_nakayama
- kl.detail.primitive_projectors
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  declarations:
  - OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1974
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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
- moment_graph_sheaves
---

# Indecomposability of the normalized boundary sheaf

Over a nonnegatively graded domain, the normalized minimal-boundary sheaf on a finite ordered graph has no nontrivial graded idempotent endomorphism:
\[
p^2=p\quad\Longrightarrow\quad p=0\ \text{or}\ p=1.
\]
Equivalently, its identity is a primitive projector, so the sheaf cannot split into two nonzero graded direct summands.

*Proof.*

### Step 1. Determine the idempotent on the top stalk

Let \(p:B\to B\) be a graded sheaf endomorphism with \(p^2=p\). At the top stalk \(B^b=A\), an \(A\)-linear endomorphism is multiplication by \(c=p_b(1)\). Idempotence gives \(c^2=c\), or \(c(c-1)=0\). Since \(A\) is a domain, \(c=0\) or \(c=1\).

We first prove that \(p_b=0\) forces the entire endomorphism to vanish.

### Step 2. Propagate zero through the edge modules above a vertex

Assume by downward induction that \(p_y=0\) for every \(y>x\). For any outgoing edge \(e:x\to y\), the upper map \(B^y\twoheadrightarrow B^e\) is surjective. Given \(z\in B^e\), lift it to \(v\in B^y\). Commutation of the upper square gives
\[
p_e(z)=p_e(\rho_{y,e}(v))=\rho_{y,e}(p_y(v))=0.
\]
Thus all those edge maps vanish.

### Step 3. Use minimality to eliminate p at x

For \(v\in B^x\), commutation of the lower square gives
\(\rho_{x,e}(p_xv)=p_e(\rho_{x,e}v)=0\).
Hence \(\operatorname{im}p_x\) lies in the full outgoing kernel, and minimality at a non-top vertex puts it inside \(JB^x\).

Let \(N=\operatorname{im}p_x\). Since \(p_x\) is idempotent, it acts as the identity on \(N\). Applying \(p_x\) to \(N\subseteq JB^x\) gives
\(N=p_x(N)\subseteq Jp_x(B^x)=JN\).
Thus \(N=JN\). The map is graded, so its image is graded and bounded below. Graded Nakayama gives \(N=0\), hence \(p_x=0\).

### Step 4. Finish both alternatives

Finite downward induction starts with the zero top map and proves every stalk map zero. Surjectivity of all upper restrictions then makes every edge map zero.

If instead \(p_b=1\), apply the zero-top argument to \(1-p\). Its square is itself because \(p^2=p\), and its top map is zero. Therefore \(1-p=0\), so \(p=1\).

A direct sum decomposition would produce the projection onto one summand, an idempotent. The conclusion says one summand must be zero, proving indecomposability in the stated graded sense.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.BoundarySheaf.primitive_identity`: [BalancedPairings.lean:1974](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1974).
