---
id: kl.word.evaluation_right_action
title: The right coefficient action at a subexpression weight
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.evaluation_maps
- kl.word.induced_bimodule
- kl.notes.word_stalks
lean:
  repository: openai-kl
  modules:
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.coefficientAction_one
  - OAI.KLInvariance.TitsSpace.bottEvaluation_right
  - OAI.KLInvariance.TitsSpace.bottStalkProjection_right
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1050
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.coefficientAction_one
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1097
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_right
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1751
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStalkProjection_right
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Followed the word induction and both first-bit cases of bottEvaluation_right,
    then the coordinatewise stalk proof. Preserved the left multiplication s*w and
    the right coefficient action.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# The right coefficient action at a subexpression weight

Let \(M_{\mathbf t}\) be a tensor word module for a finite-generator Coxeter system, over its symmetric coefficient algebra \(A\). Let \(E_{\mathbf t,\eta}\) have group weight \(w_{\mathbf t}(\eta)\), and write \(m\cdot a\) for the right coefficient action.

For every \(a\in A\) and \(m\in M_{\mathbf t}\),
\[
E_{\mathbf t,\eta}(m\cdot a)
=\chi_{w_{\mathbf t}(\eta)}(a)\,E_{\mathbf t,\eta}(m).
\]
Consequently the weight-stalk projection satisfies
\[
\pi_x(m\cdot a)=\chi_x(a)\,\pi_x(m).
\]

*Proof.*

### Step 1. Check the empty word

The empty-word module is \(A\), with ordinary right multiplication. Its unique weight is \(1\), its evaluation is the identity, and \(\chi_1\) is the identity automorphism. Thus
\[
E_\varnothing(m\cdot a)=ma=\chi_1(a)m.
\]

### Step 2. State the induction for the shorter word

Assume that for every tail subexpression \(\eta\),
\[
E_{\mathbf t,\eta}(m\cdot a)
=\chi_{w_{\mathbf t}(\eta)}(a)E_{\mathbf t,\eta}(m)
\]
for all \(a,m\). Prepend a simple reflection \(s\) and put \(\tau=\chi_s\). The new right action is
\((b\otimes m)\cdot a=b\otimes(m\cdot a)\).
It is enough to verify the assertion on such pure tensors, because both sides are additive in the word vector.

### Step 3. Evaluate the branch omitting the first letter

The recursion and induction hypothesis give
\[
\begin{aligned}
E_{s\mathbf t,(0,\eta)}((b\otimes m)\cdot a)
&=bE_{\mathbf t,\eta}(m\cdot a)\\
&=b\chi_{w_{\mathbf t}(\eta)}(a)E_{\mathbf t,\eta}(m)\\
&=\chi_{w_{\mathbf t}(\eta)}(a)
 E_{s\mathbf t,(0,\eta)}(b\otimes m).
\end{aligned}
\]
This is the desired formula because this branch retains the old weight.

### Step 4. Evaluate the branch retaining the first letter

For the other branch,
\[
\begin{aligned}
E_{s\mathbf t,(1,\eta)}((b\otimes m)\cdot a)
&=b\tau(E_{\mathbf t,\eta}(m\cdot a))\\
&=b\tau(\chi_{w_{\mathbf t}(\eta)}(a))
       \tau(E_{\mathbf t,\eta}(m))\\
&=\chi_{s w_{\mathbf t}(\eta)}(a)
 E_{s\mathbf t,(1,\eta)}(b\otimes m).
\end{aligned}
\]
The last equality uses the coefficient-action identity
\(\chi_{s w}=\chi_s\circ\chi_w\) and commutativity of \(A\). This branch has weight \(s w_{\mathbf t}(\eta)\). Expanding a finite sum of pure tensors completes the induction.

### Step 5. Collect the coordinates of one stalk

The stalk \(M_{\mathbf t}^x\) is the image of the evaluations whose weights equal \(x\). Each such coordinate transforms by the same scalar \(\chi_x(a)\), by the formula just proved. Equality in every coordinate is exactly
\(\pi_x(m\cdot a)=\chi_x(a)\pi_x(m)\).

This common scalar is the coefficient character at the weight \(x\). Its differences at two weights will annihilate the quotient comparing the two stalk projections.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.coefficientAction_one`: [Frobenius.lean:1050](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1050).

`OAI.KLInvariance.TitsSpace.bottEvaluation_right`: [Frobenius.lean:1097](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1097).

`OAI.KLInvariance.TitsSpace.bottStalkProjection_right`: [Frobenius.lean:1751](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1751).
