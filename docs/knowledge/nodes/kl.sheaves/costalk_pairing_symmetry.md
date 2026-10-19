---
id: kl.sheaves.costalk_pairing_symmetry
title: Symmetry of the stalk–costalk identification
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.costalk_duality
- kl.sheaves.costalk_support
- kl.sheaves.supported_stalk_duality
- kl.detail.section_duality
lean:
  repository: openai-kl
  modules:
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual_pairing
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual_symmetric
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual_inverse_symmetric
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:24
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual_pairing
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:43
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual_symmetric
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:62
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual_inverse_symmetric
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read the pairing-evaluation identity, the incoming-product calculation
    and cancellation, and the inverse-functional substitution in PositiveTransfer.
    Preserved the boundary-sheaf and symmetric-section-duality hypotheses.
tags:
- Kazhdan-Lusztig
- graded-duality
---

# Symmetry of the stalk–costalk identification

Fix a finite-generator Coxeter system, a Bruhat interval \([u,b]\), and its real polynomial coefficient algebra \(A\). Let \(B\) be a normalized boundary sheaf with a section duality whose pairing \(D\) is symmetric:
\[
D(s,t)=D(t,s)\qquad(s,t\in\Gamma(B)).
\]
At a vertex \(x\), put
\[
K_x=\ker\!\left(B^x\xrightarrow{\partial_x}
                 \prod_{e:x\to y}B^e\right),
\qquad
\kappa_x:K_x\xrightarrow{\sim}(B^x)^*,
\]
where \(\partial_x(v)=(\rho^-_e(v))_e\) and \((B^x)^*=\operatorname{Hom}_A(B^x,A)\).

Then, for \(k,l\in K_x\),
\[
\kappa_x(k)(l)=\kappa_x(l)(k).
\]
Equivalently, for \(\lambda,\mu\in(B^x)^*\),
\[
\lambda\bigl(\kappa_x^{-1}(\mu)\bigr)
=\mu\bigl(\kappa_x^{-1}(\lambda)\bigr),
\]
where kernel elements are evaluated as their underlying stalk vectors.

*Proof.*

### Step 1. Express the stalk functional through a supported section

Let
\[
\beta_x=\prod_{e:y\to x}\alpha_e
\]
be the incoming label product. The [[node:kl.sheaves.costalk_support|kernel-to-support equivalence]] sends \(k\in K_x\) to a global section \(f_x(k)\) supported at \(x\), with
\[
f_x(k)_x=\beta_xk.
\]
The stalk–costalk construction gives, for any global section \(n\),
\[
\kappa_x(k)(n_x)=D(f_x(k),n).
\]

To see this evaluation formula from the construction, let \(\pi_x:\Gamma(B)\to B^x\) be evaluation at \(x\). The support-to-dual equivalence assigns to a supported section \(s\) the functional \(\lambda\) determined by
\[
D(s,n)=\lambda(\pi_x n)
\]
for every \(n\). Surjectivity of \(\pi_x\) gives uniqueness. Substituting \(s=f_x(k)\) gives the displayed equality. This is costalkEquivDual_pairing.

### Step 2. Multiply a kernel pairing by the incoming product

Apply Step 1 with \(n=f_x(l)\). Linearity of \(\kappa_x(k)\) and the formula for the supported section give
\[
\begin{aligned}
\beta_x\,\kappa_x(k)(l)
&=\kappa_x(k)(\beta_xl)\\
&=\kappa_x(k)(f_x(l)_x)\\
&=D(f_x(k),f_x(l)).
\end{aligned}
\]
Exchanging \(k,l\) yields the analogous equality.

### Step 3. Use global symmetry and cancel the scalar

Symmetry of \(D\) identifies the two right-hand sides. Therefore
\[
\beta_x\,\kappa_x(k)(l)
=\beta_x\,\kappa_x(l)(k).
\]
Every edge label is a nonzero polynomial, so the finite product \(\beta_x\) is nonzero; for an empty incoming set it is \(1\). The polynomial coefficient algebra is a domain, and cancellation proves
\[
\kappa_x(k)(l)=\kappa_x(l)(k).
\]

### Step 4. Substitute inverse images of functionals

Take \(k=\kappa_x^{-1}(\lambda)\) and \(l=\kappa_x^{-1}(\mu)\). The identities
\(\kappa_x(k)=\lambda\) and \(\kappa_x(l)=\mu\) transform Step 3 into the claimed inverse-symmetry formula.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.costalkEquivDual_pairing`: [PositiveTransfer.lean:24](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L24).

`OAI.KLInvariance.BruhatGraph.costalkEquivDual_symmetric`: [PositiveTransfer.lean:43](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L43).

`OAI.KLInvariance.BruhatGraph.costalkEquivDual_inverse_symmetric`: [PositiveTransfer.lean:62](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L62).
