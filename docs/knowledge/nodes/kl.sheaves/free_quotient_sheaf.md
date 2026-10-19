---
id: kl.sheaves.free_quotient_sheaf
title: Free stalks, upper quotients, and global generation
kind: definition
status: formalized
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.graded_sheaf
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
- kl.detail.polynomial_labels
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.KLInvariance.BruhatGraph.FreeSheaf
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:140
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:bmp
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the entry preserve the source hypotheses, construction, and conclusion?
  verdict: Read against the named Lean declarations and surrounding variable context;
    explanatory examples are distinguished from the formal statement.
tags:
- Kazhdan-Lusztig
- duality_and_characters
---

# Free stalks, upper quotients, and global generation

Fix a Coxeter system with finitely many simple generators, a Bruhat interval \([u,b]\), and a basis of its extended realization. The basis gives the polynomial coefficient algebra \(A=\mathbb R[X_i]\), graded with \(\deg X_i=1\), and the polynomial label \(\alpha_e\) on each edge.

The free-sheaf datum consists of a graded sheaf \(B\) on this labelled interval with three properties:

1. Every stalk \(B^x\) is free over \(A\).
2. For every edge \(e:x\to y\), the upper restriction is surjective with kernel \(\alpha_e B^y\).
3. Every vector in every stalk is the value of a global section.

The graded module data already require finite generation. Thus the first property makes the stalks finite free. The second gives
\[
B^e\simeq B^y/\alpha_e B^y.
\]
The third says that each evaluation map
\[
\pi_x:\Gamma(B)\longrightarrow B^x,\qquad m\longmapsto m_x
\]
is surjective.

## Bases at vertices and edges

Choose a finite free basis \(v_1,\ldots,v_r\) of the upper stalk \(B^y\). The quotient map identifies the edge module with
\[
B^e\simeq\bigoplus_{i=1}^r A/(\alpha_e)\,\overline v_i.
\]
Indeed, express an upper-stalk vector uniquely as \(\sum_i a_i v_i\); its class is determined by the classes of the coefficients \(a_i\) modulo \(\alpha_e\). A zero class means every coefficient is divisible by \(\alpha_e\).

This basis description later allows a scalar to be cancelled in an edge module whenever its class is nonzero in the domain \(A/(\alpha_e)\).

## The one-edge example

For \(x\to y\), take \(A=\mathbb R[\alpha]\), stalks \(A,A\), edge module \(A/(\alpha)\), and both restrictions equal to the quotient map. Its sections are
\[
\Gamma(B)=\{(f,g):f-g\in\alpha A\}.
\]
The stalks are free, and the upper map has exactly the required quotient kernel. For any prescribed value \(h\) at either vertex, the diagonal section \((h,h)\) realizes it. All three properties follow directly.

## Input to support duality

Free stalks give torsion-free coordinates: if \(a\ne0\) and \(av=0\), expressing \(v\) in a basis shows every coefficient is zero. Upper quotients turn vanishing restrictions into divisibility by labels. Global generation lets a functional on a stalk be recovered from its values on sections.

A boundary sheaf supplies these three properties together with its top normalization, extension conditions, and minimal covers. The sheaves constructed from words supply the same three properties through their stalk, quotient, and generation theorems. The common datum is the input to the costalk-duality construction.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

The fields `sheaf`, `free`, `quotient`, and `generated` are precisely the graded sheaf and the three properties above.

`OAI.KLInvariance.BruhatGraph.FreeSheaf`: [CharacterReciprocity.lean:140](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L140).
