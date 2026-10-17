---
id: kl.notes.dihedral_kl
title: KL polynomials in a dihedral Coxeter system
kind: theorem
status: proved
primary_topic: kl.04_localization
topics:
- kl.04_localization
uses:
- kl.notes.hecke_action
- kl.foundations.canonical_kl
- kl.notes.relative_dihedral_intervals
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.klPolynomial_eq_one
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:656
    format: lean-location
    note: OAI.KLInvariance.Dihedral.klPolynomial_eq_one
  - artifact: openai-kl-paper
    locator: 4. Localization at a root plane; loc:dihedral-kl
    format: section
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the source hypotheses retained?
  verdict: The statement and proof follow the fixed formal development and its paper
    counterpart.
tags:
- Kazhdan-Lusztig
- localization
---

# KL polynomials in a dihedral Coxeter system

In a finite or infinite dihedral Coxeter system \(D\),
\[
P^D_{x,w}(q)=1\qquad(x\le_D w).
\]

*Proof.*

Use the Hecke convention \((T_s+1)(T_s-q)=0\), and put
\[
C_w^\circ=q^{-\ell_D(w)/2}\sum_{z\le_D w}T_z.
\]
The identity and simple-reflection cases are bar invariant. For an alternating reduced expression of \(w\) beginning in \(s\), let \(n=\ell_D(w)\ge2\). Pair the group elements into left \(s\)-strings \(\{r,sr\}\) with \(\ell_D(sr)=\ell_D(r)+1\).

If only \(r\) belongs to the lower interval of \(sw\), multiplication by \(1+T_s\) produces \(T_r+T_{sr}\). If both belong, the quadratic relation gives
\[
(1+T_s)(T_r+T_{sr})=(1+q)(T_r+T_{sr}).
\]
The strings meeting the lower interval of \(sw\) fill the lower interval of \(w\). For \(n>2\), the doubly represented strings fill the lower interval of the prefix \(p\) of length \(n-2\). Therefore
\[
C_s^\circ C_{sw}^\circ=
\begin{cases}
C_w^\circ,&n=2,\\
C_w^\circ+C_p^\circ,&n>2.
\end{cases}
\]
Induction proves bar invariance of \(C_w^\circ\).

Its leading coefficient in the normalized standard basis is one, and every lower coefficient is the strictly negative power \(q^{-(\ell_D(w)-\ell_D(z))/2}\). The triangular characterization of the canonical basis identifies it with the KL basis element. Comparing coefficients gives \(P^D_{z,w}=1\).

Only finite lower intervals are used in this calculation, so the same argument applies in the infinite dihedral group.

## References

[4. Localization at a root plane](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L29).

## Lean formalization

The implementation establishes the dihedral Hecke calculation and identifies its polynomial family with the already constructed ordinary KL family.

`OAI.KLInvariance.Dihedral.klPolynomial_eq_one`: [Dihedral.lean:656](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L656).
