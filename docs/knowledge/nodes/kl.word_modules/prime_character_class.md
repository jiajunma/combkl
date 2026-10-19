---
id: kl.word.prime_character_class
title: Prime character classes are single weights or reflection pairs
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.character_congruence
- kl.word.root_character_class
- kl.algebra.linear_primes
- kl.notes.reflection_faithfulness
- kl.word.edge_annihilation
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.isReflection_of_prime_character_congruence
  - OAI.KLInvariance.TitsSpace.prime_character_class
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1572
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.isReflection_of_prime_character_congruence
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1620
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.prime_character_class
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the nonzero moving vector, associated linear prime, exact range-line
    identity and reflection-faithfulness step, followed by the root-difference coefficient
    and full class identification.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Prime character classes are single weights or reflection pairs

Fix a finite-generator Coxeter system, its symmetric coefficient algebra \(A\), and a prime element \(p\in A\). Suppose \(x\ne y\) and
\[
p\mid\chi_x(f)-\chi_y(f)\qquad(f\in A).
\]
Then \(t=yx^{-1}\) is a reflection, \(y=tx\), and the entire residue class of \(x\) in \(W\) is
\[
C_x=\{x,tx\}.
\]
Moreover, \(p\) is associated to the linear polynomial of a root representing \(t\).
Thus each prime character class is either a singleton or a reflection pair.

*Proof.*

### Step 1. Find a nonzero displacement

Set \(w=yx^{-1}\). Since \(x\ne y\), \(w\ne1\). If every displacement were zero, the action of \(w\) would be the identity, and faithfulness would force \(w=1\). Hence there is \(v\in V\) with
\[
d=wv-v\ne0.
\]

For any \(z\in V\), substitute
\(f=\chi_x^{-1}(\iota(z))\) into the character congruence. The character difference is \(\iota(z-wz)\). Divisibility also holds for its negative, giving
\[
p\mid\iota(wz-z).
\]
In particular, \(p\mid\iota(d)\).

### Step 2. Replace the prime by a nonzero linear generator

Because \(d\ne0\), the polynomial \(\iota(d)\) is prime by the [[node:kl.algebra.linear_primes|linear-prime theorem]]. The two prime elements \(p,\iota(d)\) are associated, since \(p\mid\iota(d)\).

Therefore, for every \(z\),
\[
\iota(d)\mid\iota(wz-z).
\]
The [[node:kl.algebra.linear_primes|linear-divisibility criterion]] gives \(wz-z\in\mathbb Rd\). Hence
\[
\operatorname{im}(w-1)\subseteq\mathbb Rd.
\]
The reverse inclusion holds because \(d=(w-1)v\) belongs to the image, which is a linear subspace. Thus the moving space equals the line \(\mathbb Rd\) and has dimension one.

### Step 3. Identify a reflection

Reflection faithfulness of the extended realization says that a group element with one-dimensional moving space is a reflection. Apply it to \(w\), and set \(t=w\). Then \(t\) is a reflection and \(y=tx\).

### Step 4. Replace the prime by this reflection's root polynomial

Choose a positive root \(a\) representing \(t\), and put
\(\alpha=\iota(\operatorname{embed}(a))\). The reflection-character difference construction gives a coefficient
\[
c=\chi_x^{-1}(\alpha/2)
\]
with \(\chi_x(c)-\chi_{tx}(c)=\alpha\).

The assumed congruence of \(x\) and \(y=tx\) therefore gives \(p\mid\alpha\). The nonzero root polynomial \(\alpha\) is prime, so \(p\) and \(\alpha\) are associated.

### Step 5. Classify every member of the class

Associated elements define the same divisibility conditions. For every \(z\in W\),
\[
\begin{aligned}
x\sim_p z
&\Longleftrightarrow
\alpha\mid\chi_x(f)-\chi_z(f)\text{ for every }f\\
&\Longleftrightarrow z=x\text{ or }z=tx,
\end{aligned}
\]
by the [[node:kl.word.root_character_class|root-character congruence theorem]].

If a class has no element distinct from its chosen member, it is a singleton. Otherwise Steps 1–5 identify it with the stated pair. On a subset of weights, its class is the intersection of that pair with the subset.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.isReflection_of_prime_character_congruence`: [IntegralPairings.lean:1572](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1572).

`OAI.KLInvariance.TitsSpace.prime_character_class`: [IntegralPairings.lean:1620](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1620).
