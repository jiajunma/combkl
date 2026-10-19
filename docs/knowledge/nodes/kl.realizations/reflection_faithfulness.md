---
id: kl.notes.reflection_faithfulness
title: Faithfulness and the rank-one characterization of reflections
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.realization.faithful_actions
- kl.realization.orthogonal_rank_one
- kl.realization.moving_spaces
- kl.realization.simple_root_sign
- kl.coxeter.simple_edge_transport
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedAction_injective
  - OAI.KLInvariance.TitsSpace.involution_of_moving_rank_one
  - OAI.KLInvariance.TitsSpace.isReflection_of_moving_rank_one
  - OAI.KLInvariance.TitsSpace.reflectionFaithful
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1117
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_injective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1136
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.involution_of_moving_rank_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1156
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.isReflection_of_moving_rank_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1255
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.reflectionFaithful
  - artifact: openai-kl-paper
    locator: 2. Real realizations and moment-graph sheaves; bg:realization
    format: section
    note: Exposition and supporting formal inputs for this part of the paper.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the mathematical hypotheses and scope retained from the referenced declarations?
  verdict: The exposition follows the fixed Lean source; worked calculations explain
    the constructions.
tags:
- Kazhdan-Lusztig
- background
---

# Faithfulness and the rank-one characterization of reflections

Let \((W,S)\) have finitely many simple generators, and let \(\rho\) be its action on the extended real root space \(E\), with symmetric nondegenerate form \(\widetilde B\). This action is faithful, and
\[
\dim\operatorname{im}(\rho(w)-1)=1
\quad\Longleftrightarrow\quad
w\text{ is a Coxeter reflection}.
\]

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same conclusion, different proof.**

**OpenAI notes:** After showing a rank-one orthogonal change is an involution, the proof invokes the finite-subgroup theorem to conjugate it into a finite standard parabolic subgroup. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The converse is proved by descent in Coxeter length: an involution with a simple descent is either that commuting simple reflection or has a shorter simple conjugate with the same moving rank. [Tits:1156](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1156), [Tits:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).

**Role in the proof:** The proof below follows length descent. Its shorter conjugate preserves moving rank, and its commuting case identifies the element with the chosen simple reflection.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Faithfulness and preservation of the form

The faithful-actions theorem applies to this finite-generator system and its constructed extension. It gives injectivity of \(\rho\). The construction also gives
\[
\widetilde B(\rho(w)v,\rho(w)z)=\widetilde B(v,z)
\]
for all \(w,v,z\).

### Step 2. Moving rank one gives an involution

Suppose \(g=\rho(w)\) has one-dimensional moving space. The rank-one orthogonal theorem applies because \(g\) is invertible, preserves the symmetric nondegenerate form, and has that moving rank. It proves \(g^2=1\).

Consequently \(\rho(w^2)=1=\rho(1)\). Faithfulness gives \(w^2=1\), hence \(w^{-1}=w\). Also \(w\ne1\), since the identity operator has zero moving space.

### Step 3. Set up length descent

We prove that such a \(w\) is a reflection by strong induction on \(\ell(w)\). Choose a right descent \(s=s_i\), so \(\ell(ws)<\ell(w)\).

Since \(w^{-1}=w\), inversion of the word \(ws\) gives
\[
\ell(sw)=\ell((ws)^{-1})=\ell(ws)<\ell(w).
\]
Thus \(s\) is also a left descent.

### Step 4. The noncommuting case

Suppose \(sw\ne ws\). The simple-descent square theorem, applied with both simple generators equal to \(s\), gives
\[
\ell(sws)<\ell(sw).
\]
Combining with Step 3 yields \(\ell(sws)<\ell(w)\).

The operator \(\rho(sws)=\rho(s)\rho(w)\rho(s)^{-1}\) is conjugate to \(\rho(w)\). Conjugation preserves moving rank, so its moving rank is one. The induction hypothesis makes \(sws\) a reflection. Conjugating by \(s\) gives \(w=s(sws)s\), also a reflection.

### Step 5. The commuting case selects the negative eigenline

Suppose \(sw=ws\). Put \(e=\widetilde\alpha_i\); then \(\widetilde B(e,e)=2\). Commutation gives
\[
\rho(s)(g e)=g(\rho(s)e)=-g e.
\]
The simple-reflection formula says
\[
\rho(s)v=v-\widetilde B(e,v)e.
\]
If \(\rho(s)v=-v\), it follows that \(2v=\widetilde B(e,v)e\). Hence \(g e=a e\) for some scalar \(a\).

Preservation of the form gives \(2=2a^2\), so \(a\) is either one or minus one. The right descent from Step 3 makes the ordinary-root image \(\rho_0(w)\alpha_i\) coordinatewise nonpositive. By restriction of the extended action, the \(i\)-th original coordinate of \(g e\) is nonpositive. That coordinate is \(a\), since the \(i\)-th coordinate of \(e\) is one. Therefore \(a=-1\).

### Step 6. Identify the commuting operator

The vector \(g e-e=-2e\) is nonzero and belongs to the one-dimensional moving space of \(g\). Thus that space is \(\mathbb R e\). For every \(v\), write
\[
g v=v+c_v e.
\]
Preserving the form on the pair \(e,v\), and using \(g e=-e\), gives
\[
\widetilde B(e,v)
=\widetilde B(-e,v+c_v e)
=-\widetilde B(e,v)-2c_v.
\]
Hence \(c_v=-\widetilde B(e,v)\). Therefore
\[
g v=v-\widetilde B(e,v)e=\rho(s)v
\]
for all \(v\). Faithfulness now gives \(w=s\), which is a reflection. This completes the induction.

### Step 7. The moving rank of every reflection

A simple reflection has moving space \(\mathbb R\widetilde\alpha_i\), of dimension one. Every Coxeter reflection is a conjugate of a simple reflection. Its operator is the corresponding conjugate, and conjugation preserves moving rank. Thus every reflection has moving rank one, proving the converse.

## References

The local statements and proof steps are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedAction_injective`: [Tits.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1117).

`OAI.KLInvariance.TitsSpace.involution_of_moving_rank_one`: [Tits.lean:1136](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1136).

`OAI.KLInvariance.TitsSpace.isReflection_of_moving_rank_one`: [Tits.lean:1156](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1156).

`OAI.KLInvariance.TitsSpace.reflectionFaithful`: [Tits.lean:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).
