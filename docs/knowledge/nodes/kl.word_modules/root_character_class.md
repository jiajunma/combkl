---
id: kl.word.root_character_class
title: Character congruence modulo a reflection root
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.character_congruence
- kl.realization.root_line_isometry
- kl.algebra.linear_primes
- kl.detail.root_reflection_correspondence
- kl.realization.faithful_actions
- kl.word.reflection_algebra_action
lean:
  repository: openai-kl
  modules:
  - Frobenius
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff
  - OAI.KLInvariance.TitsSpace.reflection_character_separates
  - OAI.KLInvariance.TitsSpace.coefficientAction_reflection
  - OAI.KLInvariance.TitsSpace.reflectionCoefficient_divisible
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1491
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:1547
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflection_character_separates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1632
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.coefficientAction_reflection
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1644
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionCoefficient_divisible
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the bilinear form, coefficient ring, finite coordinate presentation
    and lifting hypotheses explicit?
  verdict: Read the inverse-character substitution, linear-divisibility conversion,
    root-line classification, faithful-action recovery and reverse reflection divisibility.
    Preserved the left reflection relation y=t*x.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Character congruence modulo a reflection root

Fix a finite-generator Coxeter system with extended realization \(V\), coefficient algebra \(A=\operatorname{Sym}_{\mathbb R}(V)\), and coefficient action \(\chi\).
Let a geometric root \(a\) represent a reflection \(t\), and put
\[
\alpha=\iota(\operatorname{embed}(a)).
\]
For all \(x,y\in W\),
\[
\bigl(\forall f\in A,\ \alpha\mid\chi_x(f)-\chi_y(f)\bigr)
\quad\Longleftrightarrow\quad x=y\text{ or }y=tx.
\]
Consequently, if \(y\) differs from both \(x\) and \(tx\), some coefficient \(f\) separates their characters modulo \(\alpha\).

*Proof.*

### Step 1. Pull the comparison back through the first character

Assume the divisibility condition and set \(w=yx^{-1}\). For an arbitrary \(v\in V\), choose
\[
f=\chi_x^{-1}(\iota(v)).
\]
Then \(\chi_x(f)=\iota(v)\). The coefficient-action identity and \(wx=y\) give
\[
\chi_y(f)=\chi_w(\iota(v))=\iota(wv).
\]
Thus \(\alpha\mid\iota(v-wv)\).

### Step 2. Turn polynomial divisibility into a displacement line

The [[node:kl.algebra.linear_primes|linear-generator divisibility theorem]] gives
\[
v-wv\in\mathbb R\,\operatorname{embed}(a).
\]
A linear subspace is closed under negation, so
\(wv-v\) lies in the same line for every \(v\).

The extended action preserves the extended bilinear form, and the embedded root has squared norm two. The [[node:kl.realization.root_line_isometry|root-line isometry theorem]] therefore says that the action of \(w\) is the identity or the reflection in \(\operatorname{embed}(a)\).

### Step 3. Recover the group element from its action

The extended action is faithful. If the action of \(w\) is the identity, then \(w=1\), so \(yx^{-1}=1\) and \(y=x\).

If its action is the root reflection, the root-reflection formula identifies it with the action of \(t\). Faithfulness gives \(w=t\), hence \(y=tx\). This proves the forward implication.

### Step 4. Verify both possible congruences

If \(y=x\), every difference is zero and hence divisible by \(\alpha\).

If \(y=tx\), then
\[
\chi_x(f)-\chi_y(f)
=\chi_x(f)-\chi_t(\chi_x(f)).
\]
The [[node:kl.word.reflection_algebra_action|reflection divisibility theorem]] says that \(\alpha\) divides \(b-\chi_t(b)\) for every \(b\in A\). Apply it to \(b=\chi_x(f)\). This proves the reverse implication.

### Step 5. Obtain a separating coefficient

If \(y\ne x\) and \(y\ne tx\), the equivalence just proved rules out divisibility for every coefficient. Therefore some \(f\in A\) satisfies
\(\alpha\nmid\chi_x(f)-\chi_y(f)\). This is the source's reflection_character_separates conclusion.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.reflection_character_congruence_iff`: [IntegralPairings.lean:1491](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1491).

`OAI.KLInvariance.TitsSpace.reflection_character_separates`: [IntegralPairings.lean:1547](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L1547).

`OAI.KLInvariance.TitsSpace.coefficientAction_reflection`: [Frobenius.lean:1632](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1632).

`OAI.KLInvariance.TitsSpace.reflectionCoefficient_divisible`: [Frobenius.lean:1644](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1644).
