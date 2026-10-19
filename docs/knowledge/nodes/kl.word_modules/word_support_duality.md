---
id: kl.word.support_duality
title: Weight support and the dual of a projected stalk
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.word_stalks
- kl.word.scaled_coordinate_lifts
- kl.notes.tensor_pairing
- kl.realization.faithful_actions
- kl.algebra.coefficient_algebra
- kl.word.evaluation_right_action
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bott_weight_eigen
  - OAI.KLInvariance.TitsSpace.bott_eigen_supported
  - OAI.KLInvariance.TitsSpace.bott_distinct_weight_orthogonal
  - OAI.KLInvariance.TitsSpace.bott_supported_iff_annihilates
  - OAI.KLInvariance.TitsSpace.bottStalkDualToSupport
  - OAI.KLInvariance.TitsSpace.bottStalkDualToSupport_bijective
  - OAI.KLInvariance.TitsSpace.bottStalkDuality
  - OAI.KLInvariance.TitsSpace.coefficientAction_separates
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1410
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bott_weight_eigen
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1423
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bott_eigen_supported
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1437
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bott_distinct_weight_orthogonal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1553
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bott_supported_iff_annihilates
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1575
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkDualToSupport
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1588
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkDualToSupport_bijective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1610
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkDuality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1377
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.coefficientAction_separates
verification:
  statement: accepted
  proof: accepted
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

# Weight support and the dual of a projected stalk

Let \(M=M_{\mathbf s}\) be the module of any word in a finite-generator Coxeter system, over the symmetric coefficient domain \(A\). Write \(E_\varepsilon\) for its evaluations, \(w(\varepsilon)\) for their weights, and
\(\pi_x:M\twoheadrightarrow M^x\) for the projection to the image stalk.

The perfect symmetric word pairing is denoted by \(\langle m,n\rangle=D(m)(n)\). Let \(S_x\subseteq M\) consist of the elements supported at weight \(x\). Then
\[
m\in S_x
\quad\Longleftrightarrow\quad
\langle m,n\rangle=0\text{ whenever }\pi_x(n)=0.
\]
It follows that there is an \(A\)-linear isomorphism
\[
S_x\xrightarrow{\sim}(M^x)^*,\qquad
m\longmapsto\bigl(\pi_x(n)\mapsto\langle m,n\rangle\bigr).
\]

*Proof.*

### Step 1. Express weight support by the right coefficient action

Let \(T_a\) denote the right action of \(a\in A\) on \(M\), and let
\(\chi_x:A\to A\) be the coefficient-algebra automorphism induced by \(x\). The evaluation formula is
\[
E_\varepsilon(T_a m)=\chi_{w(\varepsilon)}(a)E_\varepsilon(m).
\]

If \(m\in S_x\), all coordinates outside the \(x\)-block vanish. At a coordinate in that block the displayed formula is multiplication by \(\chi_x(a)\). Injectivity of full evaluation gives
\[
T_a m=\chi_x(a)m\qquad(a\in A).
\]

Conversely, assume these equations hold for every \(a\). If \(w(\varepsilon)\ne x\), faithfulness of the coefficient action supplies an \(a\) with
\(\chi_{w(\varepsilon)}(a)\ne\chi_x(a)\). Evaluating the equation gives
\[
\bigl(\chi_{w(\varepsilon)}(a)-\chi_x(a)\bigr)E_\varepsilon(m)=0.
\]
The first factor is nonzero and \(A\) is a domain, so \(E_\varepsilon(m)=0\). Thus \(m\in S_x\).

The separation assertion follows from faithfulness on the extended realization: distinct group elements act differently on some vector, and its degree-one image in the symmetric algebra distinguishes their coefficient actions.

### Step 2. Pairings between distinct weights vanish

The word pairing is balanced for the right action:
\(\langle T_a m,n\rangle=\langle m,T_a n\rangle\).
For \(m\in S_x,\ n\in S_y\), Step 1 turns this into
\[
\bigl(\chi_x(a)-\chi_y(a)\bigr)\langle m,n\rangle=0.
\]
If \(x\ne y\), choose a separating \(a\). Cancellation in \(A\) gives \(\langle m,n\rangle=0\).

### Step 3. Supported elements annihilate the projection kernel

Let \(m\in S_x\), and suppose \(\pi_x(n)=0\). The scaled-coordinate theorem supplies \(\Delta\ne0\) and elements \(c_\varepsilon\) supported at \(w(\varepsilon)\), with
\[
\Delta n=\sum_\varepsilon E_\varepsilon(n)c_\varepsilon.
\]
Pair this equality with \(m\).

If \(w(\varepsilon)=x\), then \(E_\varepsilon(n)=0\) by the projection-kernel hypothesis. If \(w(\varepsilon)\ne x\), Step 2 gives
\(\langle m,c_\varepsilon\rangle=0\). Thus every term of the paired sum is zero:
\[
\Delta\langle m,n\rangle=0.
\]
Since \(\Delta\ne0\), cancellation proves \(\langle m,n\rangle=0\).

### Step 4. Annihilation forces the right-action eigenvalue equations

Conversely, assume \(m\) annihilates \(\ker\pi_x\). For any \(a\in A\) and \(n\in M\), the vector
\[
T_a n-\chi_x(a)n
\]
has zero \(x\)-block evaluations. It therefore lies in \(\ker\pi_x\), giving
\[
\langle m,T_a n\rangle=\chi_x(a)\langle m,n\rangle.
\]
Balance changes the left side to \(\langle T_a m,n\rangle\), and bilinearity changes the right side to \(\langle\chi_x(a)m,n\rangle\). These agree for every \(n\), so perfection gives
\(T_a m=\chi_x(a)m\). Step 1 now proves \(m\in S_x\).

### Step 5. Construct and invert the stalk duality

For \(\lambda\in(M^x)^*\), set
\[
\Psi_x(\lambda)=D^{-1}(\lambda\circ\pi_x).
\]
Its pairing with every vector in \(\ker\pi_x\) is zero, so Step 4 places it in \(S_x\).

For \(m\in S_x\) and \(v\in M^x\), choose \(n\) with \(\pi_x(n)=v\), and define
\(\Phi_x(m)(v)=\langle m,n\rangle\).
Two lifts differ by a vector in \(\ker\pi_x\); Step 3 shows they give the same value. Lifting sums and scalar multiples proves linearity.

For any \(\lambda,v\), substitution gives
\(\Phi_x(\Psi_x(\lambda))(v)=\lambda(v)\).
For any \(m\in S_x\), the identity
\(\Phi_x(m)\circ\pi_x=D(m)\) gives
\(\Psi_x(\Phi_x(m))=m\).
These two inverse equations establish the isomorphism.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bott_weight_eigen`: [Frobenius.lean:1410](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1410).

`OAI.KLInvariance.TitsSpace.bott_eigen_supported`: [Frobenius.lean:1423](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1423).

`OAI.KLInvariance.TitsSpace.bott_distinct_weight_orthogonal`: [Frobenius.lean:1437](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1437).

`OAI.KLInvariance.TitsSpace.bott_supported_iff_annihilates`: [Frobenius.lean:1553](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1553).

`OAI.KLInvariance.TitsSpace.bottStalkDualToSupport`: [Frobenius.lean:1575](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1575).

`OAI.KLInvariance.TitsSpace.bottStalkDualToSupport_bijective`: [Frobenius.lean:1588](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1588).

`OAI.KLInvariance.TitsSpace.bottStalkDuality`: [Frobenius.lean:1610](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1610).

`OAI.KLInvariance.TitsSpace.coefficientAction_separates`: [Frobenius.lean:1377](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1377).
