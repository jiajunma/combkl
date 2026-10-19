---
id: kl.sheaves.model_sum_characters
title: One multiplicity family controls stalk and full-kernel characters
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.model_sums
- kl.sheaves.model_sum_properties
- kl.sheaves.kernel_transport
- kl.duality.stalk_character
- kl.detail.model_decomposition
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  - Decomposition
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.kernelFree
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character_both
  - OAI.KLInvariance.MomentGraph.GradedSheaf.exists_character_decomposition
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Decomposition:23
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:694
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.kernelFree
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:710
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character_both
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:1978
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.exists_character_decomposition
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
- moment_graph_sheaves
---

# One multiplicity family controls stalk and full-kernel characters

Let \((O_c)\) be a boundary-model family over \(A=k[X_1,\ldots,X_N]\), with \(k\) a field, on a graph with finitely many vertices. Let \(C\) be a model sum centered in \(U\).

Its construction gives polynomials \(\mu_c(q)\in\mathbb Z[q]\), with nonnegative coefficients and \(\mu_c=0\) for \(c\notin U\), such that
\[
C_C(x;q)=\sum_c\mu_c(q)C_{O_c}(x;q).
\]
If every \(K_x(O_c)\) is free, then every \(K_x(C)\) is free and the same polynomials satisfy
\[
K_C(x;q)=\sum_c\mu_c(q)K_{O_c}(x;q).
\]

A graded sheaf isomorphism from another sheaf to \(C\) transports both formulas to that sheaf.

*Proof.*

### Step 1. Initialize the multiplicities

For the zero constructor, set \(\mu_c=0\) for every \(c\). All stalks and full outgoing kernels are zero, so both formulas hold. Their freeness and zero characters follow from the zero-module calculation.

### Step 2. Update one center

Suppose the formulas hold for a preceding sum \(C\), and the next constructor adds
\[
S=\bigoplus_{j=1}^mO_a(d_j)
\]
at \(a\in U\). Put
\[
p(q)=\sum_{j=1}^m q^{d_j},\qquad
\mu'_c(q)=
\begin{cases}
\mu_c(q)+p(q),&c=a,\\
\mu_c(q),&c\ne a.
\end{cases}
\]
All exponents are nonnegative. The coefficients of \(p\) count the shifts of this block, so they are nonnegative; adding them preserves nonnegativity of \(\mu'_a\).

If \(c\notin U\), then \(c\ne a\) and its previous polynomial was zero, so \(\mu'_c=0\).

### Step 3. Verify the stalk identity after the update

At a vertex \(x\),
\[
(C\oplus S)^x=C^x\oplus\bigoplus_jO_a^x(d_j).
\]
Character additivity and the shift formula give
\[
\begin{aligned}
C_{C\oplus S}(x;q)
&=C_C(x;q)+p(q)C_{O_a}(x;q)\\
&=\sum_c\mu'_c(q)C_{O_c}(x;q).
\end{aligned}
\]
This proves the stalk identity by induction on the construction.

### Step 4. Verify the kernel identity using the same update

Assume the model kernels are free. The [[node:kl.sheaves.kernel_transport|kernel transport theorem]] gives
\[
K_x(C\oplus S)
\simeq K_x(C)\oplus\bigoplus_jK_x(O_a)(d_j).
\]
The induction hypothesis and the model assumptions make this a finite sum of free modules, so it is free.

Its character is
\[
K_{C\oplus S}(x;q)
=K_C(x;q)+p(q)K_{O_a}(x;q)
=\sum_c\mu'_c(q)K_{O_c}(x;q).
\]
The update polynomial \(p\) is the same one used in Step 3, because the stalk and kernel summands come from the same added sheaves.

### Step 5. Transport through a sheaf isomorphism

If \(B\simeq C\) as graded sheaves, its stalk maps preserve characters. The induced full-kernel isomorphisms do the same. Thus both identities transfer with the same multiplicities.

In particular, on a finite graph, the [[node:kl.detail.model_decomposition|model-decomposition theorem]] applies to a free-stalk, flabby, globally generated sheaf with the upper-quotient rule. Together with free full kernels for the models and the given sheaf, it yields the source's simultaneous character-decomposition statement.

### Step 6. Evaluate the running example

For \(C=O_y\oplus O_x(2)\), the multiplicities are \(\mu_y=1\), \(\mu_x=q^2\). At the lower vertex,
\[
C_C(x;q)=1\cdot1+q^2\cdot1=1+q^2,
\]
\[
K_C(x;q)=1\cdot q+q^2\cdot1=q+q^2.
\]
Both formulas use the same recorded shifts.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character`: [Decomposition.lean:23](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Decomposition.lean#L23).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.kernelFree`: [CharacterReciprocity.lean:694](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L694).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.character_both`: [CharacterReciprocity.lean:710](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L710).

`OAI.KLInvariance.MomentGraph.GradedSheaf.exists_character_decomposition`: [CharacterReciprocity.lean:1978](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L1978).
