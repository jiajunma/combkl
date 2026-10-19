---
id: kl.sheaves.costalk_duality_degree
title: The degree of the inverse stalk–costalk duality map
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.costalk_duality
- kl.algebra.perfect_inverse_degree
- kl.algebra.scalar_inverse_degree
- kl.sheaves.integral_cuts
- kl.detail.graded_sheaf
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.dualToSupport_homogeneous
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual_inverse_homogeneous
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport_apply
  - OAI.KLInvariance.BruhatGraph.incomingProduct_homogeneous
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1492
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.dualToSupport_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:215
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual_inverse_homogeneous
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:206
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1555
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incomingProduct_homogeneous
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

# The degree of the inverse stalk–costalk duality map

Let \(B\) be a free sheaf on a finite Bruhat interval \([u,b]\) over the polynomial algebra \(A=\mathbb R[X_1,\ldots,X_N]\). Its labels have degree one. Suppose its section duality has pairing shift \(L\):
\[
\langle\Gamma(B)_i,\Gamma(B)_j\rangle\subseteq A_{i+j-L}.
\]
Fix a vertex \(x\), let \(n_x\) be the number of incoming edges, and write
\[
\beta_x=\prod_{e:\,t(e)=x}\alpha_e,\qquad
\kappa_x:K_x\xrightarrow{\sim}(B^x)^*
\]
for the incoming label product and the stalk–costalk isomorphism.

If \(\lambda\in(B^x)^*\) is homogeneous of degree \(r\), then
\[
\kappa_x^{-1}(\lambda)\in (B^x)_{r+L-n_x}.
\]
Its value lies in \(K_x\), so this is also its degree in the graded outgoing kernel.

*Proof.*

### Step 1. Lift the stalk functional to sections

Evaluation \(\pi_x:\Gamma(B)\to B^x\) preserves degree: a degree-\(j\) section has its \(x\)-value in \(B^x_j\). Thus
\[
(\lambda\circ\pi_x)(\Gamma(B)_j)\subseteq A_{j+r}.
\]
The composite functional has degree \(r\).

The finite vertex set gives a homogeneous decomposition of global sections, by taking the components at every vertex. The polynomial ring is Noetherian, so the section submodule also has the finite graded module data used in Lean.

### Step 2. Compute the supported representative's degree

Let \(D\) be the pairing isomorphism and set
\[
m=D^{-1}(\lambda\circ\pi_x).
\]
Supported-stalk duality proves that \(m\) is supported at \(x\). The homogeneous-representative theorem applies to the degree-\(r\) functional and the shift-\(L\) pairing, giving
\[
m\in\Gamma(B)_{r+L}.
\]
In particular \(m_x\in B^x_{r+L}\).

### Step 3. Remove the incoming product

Put \(k=\kappa_x^{-1}(\lambda)\). The construction of the inverse costalk map gives the exact coordinate identity
\[
m_x=\beta_x k.
\]
There are \(n_x\) incoming labels, each homogeneous of degree one. Repeated use of the graded multiplication law gives \(\beta_x\in A_{n_x}\).

Each factor is nonzero and \(A\) is a domain, so \(\beta_x\ne0\). The stalk \(B^x\) is free, hence multiplication by \(\beta_x\) is injective. The scalar-cancellation theorem applied to
\(\beta_x k\in B^x_{r+L}\) therefore yields
\[
k\in B^x_{r+L-n_x}.
\]

### Step 4. Check both vertices in the running example

On one edge \(x\to y\), the section pairing has \(L=1\). At the lower vertex \(n_x=0\), and the degree-zero functional \(f\mapsto f\) corresponds to \(2\alpha\in K_x=\alpha A\), of degree one.

At the upper vertex \(n_y=1\), the degree-zero functional \(g\mapsto g\) corresponds to \(-2\in K_y=A\), of degree zero. The formula gives \(0+1-0=1\) and \(0+1-1=0\), respectively.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.dualToSupport_homogeneous`: [Support.lean:1492](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1492).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual_inverse_homogeneous`: [CharacterReciprocity.lean:215](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L215).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport_apply`: [CharacterReciprocity.lean:206](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L206).

`OAI.KLInvariance.BruhatGraph.incomingProduct_homogeneous`: [Support.lean:1555](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1555).
