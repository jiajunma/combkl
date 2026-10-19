---
id: kl.word.character_congruence
title: Residue congruence of coefficient characters
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.algebra.coefficient_algebra
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.FiniteCharacterLocalization.residueSetoid
  - OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff
  - OAI.KLInvariance.TitsSpace.prime_character_class
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1788
    format: lean-location
    note: OAI.KLInvariance.FiniteCharacterLocalization.residueSetoid
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1491
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1620
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.prime_character_class
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read residueSetoid and the exact universally quantified character congruences.
    Defined the general test-family interface, its equivalence relation and the associated-prime
    replacement used in the word application.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Residue congruence of coefficient characters

Let \(R\) be a commutative ring, \(X\) a coordinate index set, and
\(\chi_a:X\to R\) a family of scalar test functions indexed by a set \(T\).
For \(p\in R\), define the residue relation
\[
x\sim_p y
\quad\Longleftrightarrow\quad
p\mid\chi_a(x)-\chi_a(y)\text{ for every }a\in T.
\]
Equivalently, all test values at \(x\) and \(y\) agree in \(R/(p)\).

This is an equivalence relation. Reflexivity uses \(p\mid0\). Symmetry negates each difference. For transitivity, add
\[
\chi_a(x)-\chi_a(z)
=(\chi_a(x)-\chi_a(y))+(\chi_a(y)-\chi_a(z)).
\]
The source packages the relation and these three properties as residueSetoid.

The residue class of \(x\) is \(C_x=\{y:x\sim_p y\}\). The quotient set \(X/{\sim_p}\) indexes the classes. It is finite when \(X\) is finite.

## The word-module coefficient characters

For a finite-generator Coxeter system, let
\(A=\operatorname{Sym}_{\mathbb R}(V)\) be the coefficient algebra of the extended realization. A group element \(x\) acts by an algebra automorphism \(\chi_x:A\to A\).

Use \(T=A\), with scalar tests \(\chi_a(x)=\chi_x(a)\). Then
\[
x\sim_p y
\quad\Longleftrightarrow\quad
p\mid\chi_x(a)-\chi_y(a)\text{ for every }a\in A.
\]
This relation compares the right-action scalars seen at two weights. The [[node:kl.word.prime_character_class|prime-character theorem]] classifies its classes when \(p\) is a prime element.

## Associated elements and congruence

In a domain, two elements are associated when they differ by an invertible scalar:
\(p=u q\), where \(u\) has a multiplicative inverse. They divide exactly the same elements, and therefore define the same residue relation.

If two prime elements satisfy \(p\mid q\), they are associated. Write \(q=pr\). Primality of \(q\) gives \(q\mid p\) or \(q\mid r\). The second alternative, together with \(q=pr\) and cancellation of \(q\ne0\), would make \(p\) invertible, contrary to its primality. Thus \(q\mid p\); cancellation in the two divisibility identities shows that the remaining factors are inverses.

This observation lets the geometric argument replace an arbitrary prime with an associated linear root polynomial.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.FiniteCharacterLocalization.residueSetoid`: [IntegralPairings.lean:1788](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1788).

`OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff`: [IntegralPairings.lean:1491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1491).

`OAI.KLInvariance.TitsSpace.prime_character_class`: [IntegralPairings.lean:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620).
