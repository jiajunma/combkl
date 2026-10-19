---
id: kl.detail.costalk_duality
title: The full outgoing kernel is dual to the stalk
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.section_duality
- kl.sheaves.costalk_support
- kl.sheaves.supported_stalk_duality
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_free_of_duality
  - OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:185
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:197
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_free_of_duality
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1447
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalkEquivDual
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1459
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.costalk_free_of_duality
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
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

Let \(B\) be a free sheaf on a Bruhat interval with finitely many edges and its polynomial coefficient ring \(A\). Its stalks are finite free, its upper maps realize the label quotients, and its global sections generate every stalk.

Suppose \(B\) has a section duality
\(D:\Gamma(B)\xrightarrow{\sim}\Gamma(B)^*\), balanced for the cuts made with the product of all edge labels. Write
\[
K_x=\ker\!\left(B^x\longrightarrow\prod_{e:\,s(e)=x}B^e\right),
\qquad
\beta_x=\prod_{e:\,t(e)=x}\alpha_e.
\]
Then the full outgoing kernel, also called the costalk here, has an \(A\)-linear isomorphism
\[
\kappa_x:K_x\xrightarrow{\sim}\operatorname{Hom}_A(B^x,A).
\]
In particular, \(K_x\) is finite free.

The isomorphism is determined by
\[
\kappa_x(k)(n_x)=\langle\delta_x(\beta_x k),n\rangle
\quad(k\in K_x,\ n\in\Gamma(B)).
\]

With a homogeneous section pairing, the degrees of these maps produce the graded reciprocity formula developed in [[node:kl.detail.costalk_reciprocity]].

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the stalk–costalk relation.**

**OpenAI notes:** The normalization proof describes a lower-support layer, relates it to the outgoing kernel using flabbiness, and obtains its graded rank through the cited moment-graph and Soergel-module results. It temporarily doubles degrees and uses the shift convention M(k)^j = M^{j+k}. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-upward-rank](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L349).

**Lean (primary):** The local construction starts with a free sheaf and a specified balanced perfect section pairing. Integral cuts identify vertex support with an evaluation-kernel annihilator. The incoming label product identifies that support module with the outgoing kernel, giving an explicit linear equivalence with the stalk dual. [Support:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L521), [CharacterReciprocity:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L150), [CharacterReciprocity:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L185).

**Role in the proof:** The Blueprint follows these integral maps. The pairing construction and its homogeneity equation supply the later graded reciprocity statement. Degree shifts use the Lean convention M(d)_n = M_{n-d}.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Apply the incoming-product isomorphism

The theorem [[node:kl.sheaves.costalk_support]] applies to the given free sheaf and its polynomial labels. It supplies
\[
\gamma_x:K_x\xrightarrow{\sim}\Gamma(B)_{\{x\}},
\qquad k\longmapsto\delta_x(\beta_x k).
\]
Its proof checks all incoming and outgoing edge equations, divides a supported stalk value by the product of incoming primes, and cancels that product in each outgoing edge module.

### Step 2. Apply supported-stalk duality

The coefficient ring \(A\) is a domain. Each free stalk is torsion-free, and every polynomial label is nonzero. The finite label product \(p\) is therefore nonzero. Upper quotients imply label annihilation on edge modules and hence define the cuts on global sections.

The supplied duality is perfect and balanced. Finally, global generation says that \(\pi_x:\Gamma(B)\to B^x\) is surjective. These are exactly the hypotheses of [[node:kl.sheaves.supported_stalk_duality]]. It gives
\[
\Phi_x:\Gamma(B)_{\{x\}}\xrightarrow{\sim}(B^x)^*,
\qquad \Phi_x(m)(n_x)=\langle m,n\rangle.
\]

### Step 3. Compose the maps and identify the inverse

Set \(\kappa_x=\Phi_x\gamma_x\). Both maps are linear isomorphisms, and substitution of \(\gamma_x(k)=\delta_x(\beta_x k)\) gives the stated formula.

For a functional \(\lambda\in(B^x)^*\), first form
\[
m=D^{-1}(\lambda\circ\pi_x).
\]
Supported-stalk duality proves that \(m\) is supported at \(x\). The incoming-product theorem then gives a unique \(k\in K_x\) with
\(m_x=\beta_x k\). This \(k\) is \(\kappa_x^{-1}(\lambda)\).

The first construction evaluates \(\lambda\) on every \(n_x\), so it recovers \(\lambda\). Conversely, starting with \(k\), perfection recovers \(\gamma_x(k)\), and injectivity of multiplication by \(\beta_x\) recovers \(k\). Thus the explicit formulas are mutually inverse.

### Step 4. Transport a dual basis

Choose a finite free basis \(v_1,\ldots,v_r\) of \(B^x\). Its coordinate functionals \(v_i^*\) satisfy \(v_i^*(v_j)=1\) for \(i=j\) and \(0\) otherwise.

Any functional \(\lambda\) equals \(\sum_i\lambda(v_i)v_i^*\), because both sides agree on every basis vector. These coordinate functionals are linearly independent by evaluation on the \(v_j\). Hence they form a finite free basis of \((B^x)^*\).

Pulling this basis back along \(\kappa_x\) gives a finite free basis of \(K_x\).

### Step 5. Compute the isomorphism on one edge

Use \(A=\mathbb R[\alpha]\) and the section pairing
\[
\langle(f,g),(f',g')\rangle=\frac{ff'-gg'}{2\alpha}.
\]
At the lower vertex, \(K_x=\alpha A\) and \(\beta_x=1\). For \(k=\alpha h\),
\[
\kappa_x(\alpha h)(f)=\langle(\alpha h,0),(f,g)\rangle=hf/2.
\]
Thus the inverse sends the stalk functional \(f\mapsto cf\) to \(2\alpha c\).

At the upper vertex, \(K_y=A\) and \(\beta_y=\alpha\). For \(k\in A\),
\[
\kappa_y(k)(g)=\langle(0,\alpha k),(f,g)\rangle=-kg/2.
\]
The inverse sends \(g\mapsto cg\) to \(-2c\). This exhibits both costalk isomorphisms and the incoming factor at the upper vertex.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.FreeSheaf.costalkEquivDual`: [CharacterReciprocity.lean:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L185).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.costalk_free_of_duality`: [CharacterReciprocity.lean:197](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L197).

`OAI.KLInvariance.BruhatGraph.costalkEquivDual`: [Support.lean:1447](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1447).

`OAI.KLInvariance.BruhatGraph.costalk_free_of_duality`: [Support.lean:1459](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1459).
