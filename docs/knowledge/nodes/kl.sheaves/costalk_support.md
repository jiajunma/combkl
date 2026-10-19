---
id: kl.sheaves.costalk_support
title: Incoming labels identify the outgoing kernel with vertex support
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.free_quotient_sheaf
- kl.sheaves.integral_cuts
- kl.sheaves.supported_sections
- kl.detail.linear_quotient
- kl.detail.root_reflection_correspondence
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.outgoing_product_regular
  - OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff_prod
  - OAI.KLInvariance.MomentGraph.Sheaf.kernelEquivSingleStalk
  - OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime
  - OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd
  - OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:945
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.outgoing_product_regular
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:959
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff_prod
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1025
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.kernelEquivSingleStalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1090
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1100
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:150
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport
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

# Incoming labels identify the outgoing kernel with vertex support

Let \(B\) be a free sheaf on a Bruhat interval \([u,b]\), with its polynomial coefficient ring \(A\), polynomial edge labels, and finite edge set. Thus the stalks are finite free, each upper restriction has quotient kernel \(\alpha_e B^{t(e)}\), and the sheaf is globally generated.

At a vertex \(x\), define the full outgoing kernel and incoming label product by
\[
K_x=\{v\in B^x:\rho^-_e(v)=0\text{ for all }e\text{ with }s(e)=x\},
\qquad
\beta_x=\prod_{e:\,t(e)=x}\alpha_e.
\]
There is an \(A\)-linear isomorphism
\[
\gamma_x:K_x\xrightarrow{\sim}\Gamma(B)_{\{x\}},
\qquad
k\longmapsto\delta_x(\beta_x k).
\]
In stalk coordinates, the supported stalk is exactly \(S_x=\beta_x K_x\).

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Different construction of the stalk–costalk relation.**

**OpenAI notes:** The normalization proof describes a lower-support layer, relates it to the outgoing kernel using flabbiness, and obtains its graded rank through the cited moment-graph and Soergel-module results. It temporarily doubles degrees and uses the shift convention M(k)^j = M^{j+k}. [bg:normalization](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L253), [eq:bg-upward-rank](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L349).

**Lean (primary):** The local construction starts with a free sheaf and a specified balanced perfect section pairing. Integral cuts identify vertex support with an evaluation-kernel annihilator. The incoming label product identifies that support module with the outgoing kernel, giving an explicit linear equivalence with the stalk dual. [Support:521](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L521), [CharacterReciprocity:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L150), [CharacterReciprocity:185](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L185).

**Role in the proof:** The Blueprint follows these integral maps. The pairing construction and its homogeneity equation supply the later graded reciprocity statement. Degree shifts use the Lean convention M(d)_n = M_{n-d}.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Prime and distinct labels at a vertex

Each label is a nonzero linear polynomial. By the linear-quotient theorem,
\(A/(\alpha_e)\) is a polynomial algebra on the quotient vector space, hence a domain. Thus \(\alpha_e\) is prime: if it divides a product \(fg\), then in this quotient \(\overline f\,\overline g=0\), so it divides one of the factors.

For two root labels, divisibility of one linear polynomial by the other means their embedded root vectors span the same line. Distinct positive roots in the chosen normalization are linearly independent in pairs, so such divisibility forces equality of the corresponding reflections.

Two incoming edges with the same target and reflection have the same other endpoint, obtained by applying that reflection to the target. They are therefore the same edge. Consequently distinct incoming labels do not divide one another.

An outgoing edge from \(x\) and an incoming edge to \(x\) also cannot have the same reflection: its other endpoint would have to lie both strictly above and strictly below \(x\). Thus an outgoing label divides none of the incoming labels.

Every factor of \(\beta_x\) is nonzero, so \(\beta_x\ne0\).

### Step 2. Multiplication by the incoming product is injective on outgoing edges

Fix an outgoing edge \(e:x\to y\). Its edge module has a finite free basis over the domain \(A/(\alpha_e)\), obtained by reducing a free basis of \(B^y\).

Every incoming label has nonzero class in this quotient by Step 1. Their product therefore has nonzero class. Multiplication by that class is injective on \(A/(\alpha_e)\), and hence on every coefficient of a free edge vector. It follows that
\[
\beta_x w=0\text{ in }B^e\quad\Longrightarrow\quad w=0.
\]

### Step 3. A kernel vector gives a supported section

Let \(k\in K_x\), and assign \(\beta_x k\) at \(x\) and zero elsewhere.

On an outgoing edge, linearity gives
\(\rho^-_e(\beta_x k)=\beta_x\rho^-_e(k)=0\).
On an incoming edge \(f\), its label divides \(\beta_x\), say
\(\beta_x=\alpha_f r\). Thus \(\beta_x k=\alpha_f(rk)\) lies in the upper restriction kernel. On every other edge both endpoint values vanish.

All edge equations are satisfied. This defines \(\gamma_x\), and its formula makes it \(A\)-linear.

### Step 4. Incoming equations force divisibility by the whole product

Let \(m\) be a section supported at \(x\), and put \(v=m_x\). For every incoming edge \(f\), compatibility gives \(\rho^+_f(v)=0\), so \(v\in\alpha_f B^x\).

Expand \(v=\sum_i a_i v_i\) in a finite free basis of \(B^x\). The last membership says \(\alpha_f\mid a_i\) for every \(f,i\).

To combine these divisibilities, list the incoming labels as \(a_1',\ldots,a_r'\) and consider a coefficient \(c=a_i\). Induct on the number of labels already multiplied. The empty product divides \(c\). Suppose
\(c=(a_1'\cdots a_j')d\).
Since \(a_{j+1}'\mid c\) is prime, it divides the displayed product or \(d\). It divides none of \(a_1',\ldots,a_j'\), by Step 1; repeated use of primality therefore forces \(a_{j+1}'\mid d\). This proves divisibility by the product of the first \(j+1\) labels.

At the end, \(\beta_x\mid c\) for each coefficient. Dividing these coefficients gives \(k\in B^x\) with \(v=\beta_x k\).

### Step 5. Outgoing equations place the divided vector in the kernel

For each outgoing edge \(e\), compatibility of the supported section gives
\[
0=\rho^-_e(v)=\rho^-_e(\beta_x k)=\beta_x\rho^-_e(k).
\]
Step 2 cancels \(\beta_x\) in \(B^e\), so \(\rho^-_e(k)=0\). Hence \(k\in K_x\), and
\(m=\delta_x(v)=\gamma_x(k)\). This proves surjectivity.

### Step 6. Injectivity and the one-edge model

If \(\gamma_x(k)=\gamma_x(k')\), equality of the \(x\)-coordinates gives
\(\beta_x(k-k')=0\). The stalk is free over the domain \(A\); since \(\beta_x\ne0\), every basis coefficient of \(k-k'\) is zero. Therefore \(k=k'\), proving injectivity.

For one edge \(x\to y\) labelled \(\alpha\), the formulas become
\[
\gamma_x:\alpha A\to\{(\alpha h,0)\},\quad k\mapsto(k,0),
\]
\[
\gamma_y:A\to\{(0,\alpha h)\},\quad k\mapsto(0,\alpha k).
\]
These are the lower and upper instances of the same incoming-product construction.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.outgoing_product_regular`: [Support.lean:945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L945).

`OAI.KLInvariance.MomentGraph.Sheaf.single_section_iff_prod`: [Support.lean:959](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L959).

`OAI.KLInvariance.MomentGraph.Sheaf.kernelEquivSingleStalk`: [Support.lean:1025](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1025).

`OAI.KLInvariance.BruhatGraph.incoming_pairwise_relPrime`: [Support.lean:1090](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1090).

`OAI.KLInvariance.BruhatGraph.outgoing_incoming_not_dvd`: [Support.lean:1100](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1100).

`OAI.KLInvariance.BruhatGraph.FreeSheaf.kernelEquivSingleSupport`: [CharacterReciprocity.lean:150](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L150).
