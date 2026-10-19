---
id: kl.hecke.defect_antireciprocity
title: Anti-reciprocity of the recursively constructed defect
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.detail.kl_defect
- kl.hecke.recursive_p_degree
- kl.hecke.ordinary_r_degree
- kl.hecke.proper_r_kernel
- kl.hecke.polynomial_reflection
lean:
  repository: openai-kl
  modules:
  - CanonicalKL
  declarations:
  - OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - OAI.KLInvariance.CanonicalP.defect_full_sum
  - OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:162
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.polynomial_reciprocity
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:124
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.defect_full_sum
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CanonicalKL:149
    format: lean-location
    note: OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the exact domain, degree conventions and source
    argument?
  verdict: Read the local hanti calculation in polynomial_reciprocity. Retained the
    conditional smaller-interval equations and detailed degree hypotheses, both finite
    sums, the proper kernel and delta cancellation.
tags:
- Kazhdan-Lusztig
- Hecke
---

# Anti-reciprocity of the recursively constructed defect

Fix \(x<y\), put \(d=d(x,y)\), and let \(P\) be the recursive family. Assume its reciprocity equation is already proved for every proper upper pair \((z,y)\), \(x<z\le y\):
\[
\operatorname{reflect}_{d(z,y)}P_{z,y}
=\sum_{t\le y}R_{z,t}P_{t,y}.
\]
Then its current defect satisfies
\[
\operatorname{reflect}_dD_{x,y}=-D_{x,y}.
\]
This conditional calculation is the induction step inside the Lean proof of full reciprocity.

*Proof.*

### Step 1. Verify the degrees for reflecting each product

For \(x<z\le y\),
\[
d(x,z)+d(z,y)=d(x,y)=d.
\]
The [[node:kl.hecke.ordinary_r_degree|R-degree theorem]] gives \(\deg R_{x,z}\le d(x,z)\); the [[node:kl.hecke.recursive_p_degree|recursive P-degree theorem]] gives \(\deg P_{z,y}\le d(z,y)\).

The bounded product-reflection identity therefore applies:
\[
\operatorname{reflect}_d(R_{x,z}P_{z,y})
=\overline R_{x,z}\,
  \operatorname{reflect}_{d(z,y)}P_{z,y}.
\]

### Step 2. Substitute the smaller reciprocity equations

Reflection preserves finite sums. Using Step 1 and the stated induction data,
\[
\begin{aligned}
\operatorname{reflect}_dD_{x,y}
&=\sum_{x<z\le y}
  \overline R_{x,z}\operatorname{reflect}_{d(z,y)}P_{z,y}\\
&=\sum_{x<z\le y}\overline R_{x,z}
  \left(\sum_{t\le y}R_{z,t}P_{t,y}\right).
\end{aligned}
\]
Both index sets are finite lower-ideal subsets.

### Step 3. Interchange the sums and evaluate the inner kernel

Distribute each product and interchange the two finite sums:
\[
\operatorname{reflect}_dD_{x,y}
=\sum_{t\le y}
 \left(\sum_{x<z\le y}\overline R_{x,z}R_{z,t}\right)P_{t,y}.
\]
The [[node:kl.hecke.proper_r_kernel|proper R-kernel theorem]] applies to each \(t\le y\), giving
\[
\operatorname{reflect}_dD_{x,y}
=\sum_{t\le y}(\delta_{x,t}-R_{x,t})P_{t,y}.
\]

### Step 4. Evaluate the Kronecker-delta sum

Because \(x\le y\), the index \(t=x\) is in the sum. Its delta coefficient is one; every other delta coefficient is zero. Therefore
\[
\sum_{t\le y}\delta_{x,t}P_{t,y}=P_{x,y}.
\]
Separate the two terms in Step 3:
\[
\operatorname{reflect}_dD_{x,y}
=P_{x,y}-\sum_{t\le y}R_{x,t}P_{t,y}.
\]

### Step 5. Recognize the defect again

The full-sum identity for the defect is
\[
D_{x,y}=\sum_{t\le y}R_{x,t}P_{t,y}-P_{x,y}.
\]
Negating it identifies the expression from Step 4 with \(-D_{x,y}\), as required.

The occurrence of \(P_{x,y}\) in Step 4 is algebraic: it comes from the delta term and cancels in the defect identity. The reciprocity equations used as inputs were only those with strictly smaller rank \(d(z,y)\).

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.CanonicalP.polynomial_reciprocity`: [CanonicalKL.lean:162](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L162).

`OAI.KLInvariance.CanonicalP.defect_full_sum`: [CanonicalKL.lean:124](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L124).

`OAI.KLInvariance.CanonicalP.reversed_kernel_on_proper`: [CanonicalKL.lean:149](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CanonicalKL.lean#L149).
