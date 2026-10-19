---
id: kl.detail.root_inversion_count
title: The root-sign criterion and the inversion count
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.root_inversions
- kl.detail.root_reflection_correspondence
- kl.realization.signed_root_action
- kl.coxeter.word_sign_record
- kl.detail.strong_exchange
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.Represents.inversion_iff
  - OAI.KLInvariance.TitsSpace.rootInversionEquiv
  - OAI.KLInvariance.TitsSpace.rootInversions_finite
  - OAI.KLInvariance.TitsSpace.card_rootInversions
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1928
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.Represents.inversion_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2042
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootInversionEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2065
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.rootInversions_finite
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:2073
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.card_rootInversions
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

# The root-sign criterion and the inversion count

Let \(W\) be a finite-generator Coxeter system, and let a positive real root \(a\) represent the reflection \(t\). Then
\[
\rho_0(w^{-1})a\text{ is negative}
\quad\Longleftrightarrow\quad
\ell(tw)<\ell(w).
\]
Consequently the root-inversion set of \(w\) is finite and has cardinality \(\ell(w)\).

*Proof.*

### Step 1. Compute the signed inverse action

Choose a reduced word \(\omega\) for \(w\). Let \(c\in\mathbb Z/2\mathbb Z\) be the multiplicity of \(t\) in its left inversion sequence, reduced modulo two.

Apply the word-record theorem with initial bit \(c\):
\[
A_w(w^{-1}tw,c)=(t,c+c)=(t,0).
\]
Taking the inverse group action gives
\[
A_{w^{-1}}(t,0)=(w^{-1}tw,c).
\]

The positive root \(a\) is represented by \((t,0)\). Compatibility of signed labels with root transformation therefore makes the last pair represent \(\rho_0(w^{-1})a\). Its bit \(c\) is exactly the coordinate sign of that root.

### Step 2. A reduced inversion sequence has no repetitions

Suppose two positions \(j<k\) had the same inversion label. Write the supplied word as
\[
\omega=u\,s_j\,p\,s_k\,v,
\]
where \(u\) is the prefix before position \(j\), and \(p\) is the intervening word. Here \(s_j,s_k\) denote the letters at the chosen positions; in the group equations below, \(u,p,v\) denote the products of the corresponding word segments.

Equality of the two labels gives
\[
u s_j u^{-1}
=u s_j p s_k p^{-1}s_j u^{-1}.
\]
Cancel the outer prefix and multiply by \(s_j\) to obtain
\[
s_j=p s_k p^{-1},\qquad s_jp=ps_k.
\]
The word product thus becomes
\[
u s_j p s_k v=u p s_k^2v=u p v.
\]
This deletes two positions, contradicting reducedness. Hence the inversion sequence is repetition-free.

Therefore \(c=1\) exactly when \(t\) occurs in that sequence, and \(c=0\) otherwise. The transformed root is nonzero, so its positive and negative signs are exclusive. Step 1 consequently identifies negativity with occurrence of \(t\).

### Step 3. Identify occurrence with a left inversion

If \(t\) occurs at a position of the reduced word, the deletion identity expresses \(tw\) using \(|\omega|-1\) letters. Hence \(\ell(tw)<\ell(w)\).

Conversely, if \(\ell(tw)<\ell(w)\), strong exchange deletes a position in the supplied word to give \(tw\). If the prefix, deleted letter, and tail are \(u,s_j,v\), then \(w=us_jv\) and \(tw=uv\). Multiplication by \(w^{-1}\) gives \(t=us_ju^{-1}\), the inversion label at that position.

This proves the sign criterion.

### Step 4. Count the roots through explicit bijections

The positive-root/reflection correspondence restricts to a bijection from root inversions of \(w\) to its left-inversion reflections, by Step 3.

Those reflections are exactly the labels in the reduced inversion sequence. Step 2 makes the map from positions to labels injective, and Step 3 makes it surjective onto the left inversions.

There is one position per letter, and \(|\omega|=\ell(w)\). Composing these bijections gives finiteness and the stated cardinality.

## References

The local statements and proof steps are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.Represents.inversion_iff`: [Tits.lean:1928](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1928).

`OAI.KLInvariance.TitsSpace.rootInversionEquiv`: [Tits.lean:2042](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2042).

`OAI.KLInvariance.TitsSpace.rootInversions_finite`: [Tits.lean:2065](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2065).

`OAI.KLInvariance.TitsSpace.card_rootInversions`: [Tits.lean:2073](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L2073).
