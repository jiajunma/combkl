---
id: kl.notes.reflection_faithfulness
title: Faithfulness and the rank-one characterization of reflections
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.notes.extended_realization
- kl.realization.reflection_plane
- kl.foundations.subword
- kl.realization.extended_action
- kl.realization.moving_spaces
- kl.realization.orthogonal_rank_one
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.extendedAction_injective
  - OAI.KLInvariance.TitsSpace.reflectionFaithful
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1117
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.extendedAction_injective
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

The action on the extended real realization is faithful, and
\[
\operatorname{rank}(w-1)=1
\quad\Longleftrightarrow\quad
w\text{ is a reflection}.
\]
Thus the root labels detect exactly the group elements having a codimension-one fixed space.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same conclusion, different proof.**

**OpenAI notes:** After showing a rank-one orthogonal change is an involution, the proof invokes the finite-subgroup theorem to conjugate it into a finite standard parabolic subgroup. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The converse is proved by descent in Coxeter length: an involution with a simple descent is either that commuting simple reflection or has a shorter simple conjugate with the same moving rank. [Tits:1156](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1156), [Tits:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).

**Role in the proof:** The proof below follows length descent. Its shorter conjugate preserves moving rank, and its commuting case identifies the element with the chosen simple reflection.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Retain faithfulness after extending the realization

The extended action restricts on \(V_0\oplus0\) to the ordinary geometric action. The latter is faithful: if \(w\ne1\), choose a right descent \(s\). The root-sign criterion makes \(w\alpha_s\) nonpositive, whereas \(\alpha_s\) is positive, so \(w\) cannot act as the identity.

If two extended actions agree, their restrictions agree, so the group elements agree. Thus the extended action is faithful.

### Step 2. Prove that a moving-rank-one orthogonal map is an involution

Let \(g-1\) have one-dimensional image. Write \(g(v)=v-f(v)u\), where \(u\ne0\) and \(f\ne0\). Orthogonality gives
\[
-f(v)B(u,w)-f(w)B(u,v)+f(v)f(w)B(u,u)=0.
\]
Choose \(z\) with \(f(z)=1\). For \(v\in\ker f\), substitution \(w=z\) shows \(B(u,v)=0\). Therefore \(B(u,-)=cf\) for some scalar \(c\), and \(c\ne0\) by nondegeneracy.

Putting \(v=w=z\) gives \(B(u,u)=2c\); since \(B(u,u)=cf(u)\), we obtain \(f(u)=2\). Direct substitution now gives \(g^2(v)=v\). Faithfulness of the group action therefore implies \(w^2=1\) for a group element with moving rank one.

### Step 3. Induct on the length of such a group element

The element \(w\) is nonidentity, since the identity has moving rank zero. Choose a right descent \(s\), so \(\ell(ws)<\ell(w)\). Since \(w=w^{-1}\), inversion of this inequality also gives \(\ell(sw)<\ell(w)\).

If \(sw\ne ws\), the exchange-based simple-multiplication property sends the edge \(ws\to w\) to the upward edge \(sws\to sw\). Hence \(\ell(sws)<\ell(sw)<\ell(w)\). Conjugation by \(s\) preserves moving rank, so the induction hypothesis says \(sws\) is a reflection. Conjugating it back shows that \(w\) is a reflection.

### Step 4. Handle the commuting case

Suppose \(sw=ws\). The operator \(g_w\) commutes with the reflection \(g_s\), hence preserves its negative eigenspace \(\mathbb R\alpha_s\). Write \(g_w\alpha_s=\lambda\alpha_s\). Orthogonality and \(B(\alpha_s,\alpha_s)=2\) give \(\lambda^2=1\). The descent root-sign criterion makes the \(\alpha_s\)-coordinate nonpositive, so \(\lambda=-1\).

Thus the moving line of \(g_w\) is \(\mathbb R\alpha_s\). The orthogonality calculation in Step 2 determines the rank-one map uniquely from this line and its action \(-1\) on \(\alpha_s\): it is precisely the reflection \(g_s\). Faithfulness gives \(w=s\).

### Step 5. Prove the converse

A simple reflection differs from the identity by
\(v\mapsto-B(\alpha_s,v)\alpha_s\).
Its image is the nonzero line \(\mathbb R\alpha_s\), so its moving rank is one. Every group reflection is a conjugate of a simple reflection. Conjugation carries the moving image by an invertible linear map and therefore preserves its dimension. This proves the other implication.

## References

[2. Real realizations and moment-graph sheaves](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

## Lean formalization

`OAI.KLInvariance.TitsSpace.extendedAction_injective`: [Tits.lean:1117](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1117).

`OAI.KLInvariance.TitsSpace.reflectionFaithful`: [Tits.lean:1255](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1255).
