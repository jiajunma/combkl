---
id: kl.word.residue_class_projector
title: Stable diagonal selection of one residue class
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.character_congruence
- kl.word.diagonal_stabilizer
- kl.word.uniform_diagonal_projector
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.FiniteCharacterLocalization.class_projector
  - OAI.KLInvariance.FiniteCharacterLocalization.character_class_projector
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1730
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.class_projector
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1794
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.character_class_projector
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read class_projector and character_class_projector, including choice of
    tests, residue differences, prime-product nondivisibility and uniformization.
    Included a concrete congruence-lattice calculation.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Stable diagonal selection of one residue class

Let \(R\) be a commutative ring, \(X\) a finite index set, and
\(L\subseteq\prod_{x\in X}E_x\) a submodule. Let \(\chi_a:X\to R\), indexed by \(a\in T\), be stable weights: \(\chi_a\in\operatorname{Stab}(L)\).

Fix a prime element \(p\) and \(x_0\in X\). For its residue class
\(C=\{z:x_0\sim_p z\}\), there exist \(d\in R\) and \(g\in\operatorname{Stab}(L)\) such that
\[
p\nmid d,\qquad
g(z)=d\ (z\in C),\qquad g(z)=0\ (z\notin C).
\]

Here primality means that \(p\) is nonzero and noninvertible, and \(p\mid ab\) implies \(p\mid a\) or \(p\mid b\). These are the properties used in the finite products below.

*Proof.*

### Step 1. Choose a test for each outside index

For \(y\notin C\), the residue relation fails. Choose \(a_y\in T\) with
\[
p\nmid\chi_{a_y}(x_0)-\chi_{a_y}(y).
\]
Define the weight
\[
h_y(z)=\chi_{a_y}(z)-\chi_{a_y}(y).
\]
It is stable, being the difference of a stable weight and a constant weight. It satisfies \(h_y(y)=0\) and \(p\nmid h_y(x_0)\). The source sets \(h_y=0\) on the unused indices \(y\in C\), giving its full test family.

### Step 2. Prove that the tests survive on the whole class

For \(z\in C\), the residue relation gives
\[
p\mid\chi_{a_y}(z)-\chi_{a_y}(x_0)
=h_y(z)-h_y(x_0).
\]
If \(p\mid h_y(z)\), subtracting the displayed divisible difference would imply
\(p\mid h_y(x_0)\), contrary to Step 1. Hence
\[
p\nmid h_y(z)\qquad(z\in C,\ y\notin C).
\]

### Step 3. Multiply the separating tests

Set
\[
f=\prod_{y\notin C}h_y.
\]
This finite product belongs to the stabilizer algebra.

If \(z\notin C\), the product includes the factor \(h_z\), which vanishes at \(z\). Thus \(f(z)=0\). If \(z\in C\), every factor \(h_y(z)\) is not divisible by \(p\). Primality, applied successively to the finite product, gives \(p\nmid f(z)\). The empty product is \(1\), also not divisible by a prime.

### Step 4. Make the value uniform across the class

Apply the [[node:kl.word.uniform_diagonal_projector|uniform diagonal operator theorem]] to \(f\) and \(C\). It constructs
\[
d=\prod_{z\in C}f(z),\qquad
g=d-\prod_{z\in C}(f(z)-f).
\]
The weight \(g\) is stable, equals \(d\) on \(C\), and vanishes outside \(C\).

Step 3 and primality again imply \(p\nmid d\). This proves the theorem. The source's class_projector performs Steps 2–4 for a general family of separating tests; character_class_projector constructs those tests from the residue relation in Step 1.

### Step 5. Calculate a two-coordinate example

Let \(R=\mathbb R[\alpha]\) and let \(L=\{(u,v):u-v\in\alpha R\}\). Use the two coefficient characters \(a\mapsto a\) and \(a\mapsto a(-\alpha)\), and the prime \(p=\alpha-1\).

For the first coordinate, the test \(a=\alpha\) gives stable weights
\[
h=(2\alpha,0).
\]
It is zero at the other coordinate, and \(p\nmid2\alpha\), since evaluation at \(\alpha=1\) gives \(2\). Thus
\[
(u,v)\longmapsto(2\alpha\,u,0)
\]
preserves \(L\) and selects the first coordinate with a scalar not divisible by \(p\). This is the one-element-class instance of the construction.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteCharacterLocalization.class_projector`: [IntegralPairings.lean:1730](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1730).

`OAI.KLInvariance.FiniteCharacterLocalization.character_class_projector`: [IntegralPairings.lean:1794](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1794).
