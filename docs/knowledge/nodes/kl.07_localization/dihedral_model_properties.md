---
id: kl.detail.dihedral_model_properties
title: Interpolation and flabbiness of the induced dihedral models
kind: theorem
status: proved
primary_topic: kl.07_localization
topics:
- kl.07_localization
uses:
- kl.notes.dihedral_models
- kl.notes.extended_realization
- kl.realization.reflection_plane
- kl.detail.structure_sheaves
lean:
  repository: openai-kl
  modules:
  - DihedralIntervals
  declarations:
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated
  - OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:616
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:622
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.DihedralIntervals:626
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient
  - artifact: openai-kl-paper
    locator: Dihedral models; loc:models
    format: section
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual induced labels and the relative graph retained?
  verdict: The construction uses the ambient root representation and the exact relative
    dihedral order.
tags:
- Kazhdan-Lusztig
- localization
---

# Interpolation and flabbiness of the induced dihedral models

For a dihedral reflection subgroup with its actual induced ambient root labels, the rank-one structure model below a top vertex is flabby and globally generated, and satisfies the upper quotient rule.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Same model properties, different justification.**

**OpenAI notes:** The induced-model lemma justifies applying the character theorem to the restricted reflection-faithful realization and uses the dihedral character calculation to identify the rank-one model. [loc:models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

**Lean (primary):** The actual induced-label structure model is handled by orbit-spline interpolation. Its congruences, flow-down sections, flabbiness, global generation, and quotient maps are established directly before local model decomposition. [DihedralIntervals:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616), [DihedralIntervals:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622), [DihedralIntervals:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626).

**How to read this entry:** Use the interpolation proof and its actual ambient root labels here. The formula P=1 remains a separate polynomial theorem; it is not substituted for the formal construction of the model properties.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Specify the interpolation section needed at a vertex

Fix the model top \(c\) and \(x\le_Dc\). We will construct a global polynomial section \(F_x\) such that
\[
F_x(x)=\prod_{e:x\to y,\ y\le_Dc}\alpha_e,\qquad
F_x(z)=0\quad(z\le_Dc,\ z\not\le_Dx).
\]
The second condition says that its support is contained in the lower ideal of \(x\).

### Step 2. Construct degree-one factors from the actual realization

For an ambient vertex \(y\) and vector \(v_0\) in the extended realization, define the polynomial-valued function
\[
f_{y,v_0}(w)=\iota\bigl((wy^{-1})v_0-v_0\bigr),
\]
where \(\iota\) inserts a vector as a linear polynomial. It vanishes at \(w=y\).
Along a reflection edge \(w\to tw\), the difference of the two vectors is a scalar multiple of the root of \(t\); hence the edge label divides \(f_{y,v_0}(w)-f_{y,v_0}(tw)\). Thus this function satisfies every edge congruence.

For two distinct reflections giving the pairs \(x,y\) and \(z,y\), their normal forms are independent in the nondegenerate ambient realization. Choose \(v_0\) on which the first normal is \(-1\) and the second is zero. The reflection formula then makes \(f_{y,v_0}(x)\) the label of \(x\to y\), while it vanishes at both \(y\) and \(z\).

### Step 3. Multiply enough factors to kill every external vertex

Partition the vertices below \(c\) but not below \(x\) according to whether their relative-length parity is opposite to or the same as that of \(x\). The opposite-parity set is exactly the set of upward reflection neighbors of \(x\) below \(c\). The dihedral rank pattern has two vertices per internal rank, so the same-parity external set has cardinality at most the opposite-parity one.

Assign each same-parity external vertex \(z\) to a different opposite-parity vertex \(y\). For each \(y\), choose the factor from Step 2 vanishing at \(y\) and, if one is assigned, at that \(z\), with value \(\alpha_{x,y}\) at \(x\). When no \(z\) is assigned, prescribe only the first normal value.

Multiply these factors. Products preserve edge congruences because reduction modulo an edge label is a ring homomorphism. At \(x\) the product is the required outgoing-label product. Every external vertex is killed by at least one factor. This constructs \(F_x\).

### Step 4. Extend an arbitrary section on a relative upper set

Let a compatible section be prescribed on an upper subset \(\Omega\) of the model support. Process its vertices downward, retaining a residual section and a sum of global sections already chosen.

At the next vertex \(x\), the residual is zero at all higher vertices already processed. Along every supported outgoing edge, compatibility therefore says that its value at \(x\) is divisible by the edge label. Distinct incident root labels are pairwise relatively prime linear polynomials. In a UFD, divisibility by each such prime factor implies divisibility by their product. Write the residual value as \(a_xF_x(x)\).

Subtract the global section \(a_xF_x\). This kills the value at \(x\) and does not change any previously processed vertex, since \(F_x\) vanishes outside the lower ideal of \(x\). Continue through the finite set. The sum of the chosen global sections agrees with all prescribed values, proving flabbiness.

### Step 5. Check generation and the quotient rule

To generate a supported stalk, use the constant polynomial assignment on the entire lower support; it satisfies all edge congruences. Its value at the chosen stalk is any desired polynomial. Outside the support the stalk is zero. Thus the model is globally generated.

Each supported edge was defined to have module \(A/(\alpha_e)\), with both endpoint maps reduction modulo \(\alpha_e\); the upper quotient rule is therefore literal. This argument uses induced ambient roots directly and does not obtain these properties by substituting a KL-character theorem.

## References

[Preprint: induced dihedral models](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/04-localization.tex#L125).

## Lean formalization

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_flabby`: [DihedralIntervals.lean:616](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L616).

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_generated`: [DihedralIntervals.lean:622](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L622).

`OAI.KLInvariance.TitsSpace.PlaneBasis.model_quotient`: [DihedralIntervals.lean:626](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/DihedralIntervals.lean#L626).
