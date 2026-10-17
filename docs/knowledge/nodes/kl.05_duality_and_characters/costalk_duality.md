---
id: kl.detail.costalk_duality
title: The full outgoing kernel is dual to the stalk
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.detail.section_duality
- kl.sheaves.upward_kernel
- kl.detail.upper_quotient
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1447
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1459
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
  - artifact: openai-kl-paper
    locator: Related paper context; bg:normalization
    format: section
    note: Contextual correspondence, not a claim that this Lean result appears verbatim
      in the preprint.
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

# The full outgoing kernel is dual to the stalk

Let \(B\) be a minimal-boundary sheaf on a finite Bruhat interval over its polynomial coefficient ring \(A\), equipped with section duality. At a vertex \(x\), let
\[
K_x=\ker\!\left(B^x\longrightarrow\bigoplus_{e:x\to y}B^e\right).
\]
Then there is an \(A\)-linear isomorphism
\[
K_x\simeq\operatorname{Hom}_A(B^x,A).
\]
In particular \(K_x\) is finite free because \(B^x\) is finite free.

*Proof.*

### Step 1. Identify the full kernel with single-vertex supported sections

Let \(\beta_x\) be the product of labels on incoming edges at \(x\). For \(k\in K_x\), form the assignment with coordinate \(\beta_xk\) at \(x\) and zero elsewhere.

On an outgoing edge, compatibility holds because the restriction of \(k\) is zero. On an incoming edge, its label divides \(\beta_x\), so the quotient restriction of \(\beta_xk\) is zero. On all other edges both coordinates vanish. Thus the assignment is a global section supported at \(x\).

Conversely, a supported section has its \(x\)-coordinate in \(\alpha_eB^x\) for every incoming edge. Their labels are pairwise relatively prime linear forms. Expanding in a free basis of \(B^x\), divisibility by each label implies divisibility by their product, so the coordinate is \(\beta_xk\).

For any outgoing edge \(h\), compatibility gives \(\beta_x\rho_{x,h}(k)=0\). No incoming label is proportional to the label of \(h\). The edge module is free over the quotient by that linear label, so multiplication by \(\beta_x\) is injective there. Hence \(\rho_{x,h}(k)=0\), and \(k\in K_x\). Multiplication by \(\beta_x\) is injective on the free stalk, giving a bijection.

### Step 2. Turn a stalk functional into a supported section

For \(\lambda\in(B^x)^*\), compose with the surjective evaluation map \(\Gamma(V,B)\to B^x\). Perfection of the global pairing gives a unique section \(m\) satisfying
\(\langle m,n\rangle=\lambda(n_x)\) for all global sections \(n\).

Let \(C_y\) be the integral cut at \(y\), obtained by multiplying coordinate projection by a common nonzero product \(L\) of labels. If \(y\ne x\), cut balance gives
\[
\langle C_ym,n\rangle=\langle m,C_yn\rangle
=\lambda((C_yn)_x)=0.
\]
Perfection gives \(C_ym=0\), hence \(Lm_y=0\). The stalk is torsion-free and \(L\ne0\), so \(m_y=0\). Thus \(m\) is supported at \(x\).

### Step 3. Turn a supported section into a stalk functional

Suppose \(m\) is supported at \(x\), and \(n_x=0\). Since the vertex set is finite,
\(Ln=\sum_{y\ne x}C_yn\).
Then
\[
L\langle m,n\rangle
=\sum_{y\ne x}\langle m,C_yn\rangle
=\sum_{y\ne x}\langle C_ym,n\rangle=0.
\]
The coefficient ring is a domain, so \(\langle m,n\rangle=0\).
Thus pairing with \(m\) factors through evaluation at \(x\), giving a well-defined functional on \(B^x\). Surjectivity of evaluation makes this factor unique.

Steps 2–3 are inverse by uniqueness of the perfect-pairing representative. Compose their equivalence with Step 1 to obtain \(K_x\simeq(B^x)^*\). A dual of a finite free module is finite free, proving the freeness conclusion.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253).

## Lean formalization



`OAI.KLInvariance.BruhatGraph.costalkEquivDual`: [Support.lean:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1447).

`OAI.KLInvariance.BruhatGraph.costalk_free_of_duality`: [Support.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1459).
