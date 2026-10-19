---
id: kl.realization.simple_root_sign
title: Signs of simple-root images and length change
kind: theorem
status: proved
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.coxeter.parabolic_decomposition
- kl.realization.alternating_root_formula
- kl.realization.geometric_action
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.action_root_nonneg_of_ascent
  - OAI.KLInvariance.TitsSpace.action_root_nonpos_of_descent
  - OAI.KLInvariance.TitsSpace.IsRoot.sign
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:941
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action_root_nonneg_of_ascent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:985
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.action_root_nonpos_of_descent
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1679
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.IsRoot.sign
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are all action, sign, and length conventions retained?
  verdict: Read the finite-rank Tits proofs, the exact two-generator tail convention,
    and both group-action directions; the chosen smaller induction instance is explicit.
tags:
- Kazhdan-Lusztig
- root-geometry
---

# Signs of simple-root images and length change

Let \(\rho_0\) be the geometric action of a Coxeter system with finitely many simple generators. For \(w\in W\) and a simple generator \(s_i\),
\[
\ell(ws_i)=\ell(w)+1
\quad\Longrightarrow\quad
\rho_0(w)\alpha_i\text{ is coordinatewise nonnegative},
\]
and
\[
\ell(ws_i)=\ell(w)-1
\quad\Longrightarrow\quad
\rho_0(w)\alpha_i\text{ is coordinatewise nonpositive}.
\]
The image is nonzero. Hence the two signs are exclusive, and each sign characterizes the corresponding length case.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Explicit root-sign proof.**

**OpenAI notes:** The realization discussion invokes the geometric representation theorem and its root-sign property from the cited Coxeter theory. [bg:realization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L34).

**Lean (primary):** The root-sign implication is proved by strong length induction. A minimal two-generator parabolic decomposition supplies a shorter prefix, and the alternating-root formula supplies nonnegative coefficients. Faithfulness follows by applying the descent sign to an element in the kernel. [Tits:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L941), [Tits:997](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L997).

**Role in the proof:** The entries develop the coset decomposition, coefficient formula, and induction before applying faithfulness. This gives the stated geometric facts from the local word calculations.
<!-- source-comparison:end -->

*Proof.*

### Step 1. The induction statement for ascents

Use strong induction on \(n=\ell(w)\) to prove the first implication for every simple index \(i\).

For \(w=1\), the image is the basis vector \(\alpha_i\), whose coordinates are nonnegative.

Suppose \(w\ne1\) and \(\ell(ws_i)=\ell(w)+1\). Choose a right descent \(s_j\), for example the last letter of a reduced word for \(w\). Then \(\ell(ws_j)=\ell(w)-1\). In particular \(i\ne j\).

### Step 2. Separate a two-generator tail

Apply the parabolic decomposition theorem with \(J=\{i,j\}\). It gives \(w=uv\), with \(v\in W_J\), and
\[
\ell(w)=\ell(u)+\ell(v),
\qquad
\ell(ws_k)=\ell(u)+\ell(vs_k)\quad(k=i,j).
\]
It also gives \(\ell(us_i)=\ell(u)+1\) and \(\ell(us_j)=\ell(u)+1\).

Using the equation for \(j\), the descent of \(w\) implies \(\ell(vs_j)<\ell(v)\). Thus \(v\ne1\) and \(\ell(v)\ge1\). The first length equality now gives
\[
\ell(u)<\ell(w).
\]
Both ascents of \(u\) therefore fall under the induction hypothesis. We obtain coordinatewise nonnegativity of \(\rho_0(u)\alpha_i\) and \(\rho_0(u)\alpha_j\).

### Step 3. Verify reducedness of the tail with the appended generator

The equation for \(i\), combined with the ascent of \(w\), gives
\[
\ell(vs_i)=\ell(v)+1.
\]
Choose a reduced expression \(\omega\) for \(v\) using \(i,j\). Its length is \(\ell(v)\), so the word \(\omega[i]\) has length \(\ell(v)+1=\ell(vs_i)\). It is reduced.

The alternating-root positivity theorem now applies to \(u,\omega,i,j\). It proves that
\[
\rho_0(u\,\operatorname{prod}\omega)\alpha_i
=\rho_0(w)\alpha_i
\]
has nonnegative coordinates. This completes the ascent induction.

### Step 4. Derive the descent case

Suppose \(\ell(ws_i)=\ell(w)-1\), and set \(z=ws_i\). Then \(zs_i=w\), so \(s_i\) is an ascent of \(z\). The result just proved makes \(\rho_0(z)\alpha_i\) nonnegative.

Since \(w=zs_i\) and \(s_i\alpha_i=-\alpha_i\),
\[
\rho_0(w)\alpha_i=-\rho_0(z)\alpha_i.
\]
It is therefore coordinatewise nonpositive.

### Step 5. Exclude zero and recover the equivalences

The simple root \(\alpha_i\) is nonzero, and \(\rho_0(w)\) is invertible. Its image is nonzero. A vector that is both coordinatewise nonnegative and nonpositive is zero, so the two sign cases are exclusive.

Simple multiplication changes length by exactly one. The two implications therefore give the converse implications as well. Every real root is some \(\rho_0(w)\alpha_i\), so every real root has exactly one of the two signs.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.action_root_nonneg_of_ascent`: [Tits.lean:941](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L941).

`OAI.KLInvariance.TitsSpace.action_root_nonpos_of_descent`: [Tits.lean:985](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L985).

`OAI.KLInvariance.TitsSpace.IsRoot.sign`: [Tits.lean:1679](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1679).
