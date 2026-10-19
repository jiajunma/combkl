---
id: kl.sheaves.model_sum_properties
title: Structural properties of a model sum and minimality away from its centers
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.model_sums
- kl.sheaves.finite_sum_properties
- kl.detail.boundary_models
lean:
  repository: openai-kl
  modules:
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.mono
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.free
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.quotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.generated
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.flabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.minimal
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:683
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.mono
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:689
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.free
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:698
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.quotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:707
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:715
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:720
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.minimal
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

# Structural properties of a model sum and minimality away from its centers

Let \((O_c)\) be a boundary-model family and let \(C\) be a model sum centered in \(U\). Then \(C\) has free stalks, the prescribed upper-quotient rule, global generation, and flabbiness.

At any vertex \(x\notin U\),
\[
K_x(C)\subseteq JC^x.
\]
If \(U\subseteq T\), the same construction is also a model sum centered in \(T\).

*Proof.*

### Step 1. Verify the zero constructor

The zero sheaf has free stalks of rank zero. Its upper restrictions \(0\to0\) are surjective with kernel \(0=\alpha_e0\).

Its unique assignment is global, realizes the only vector at every stalk, and extends its restriction from every upper set. Every outgoing kernel is zero and lies in \(J0\). Thus all assertions hold for the initial constructor.

### Step 2. Pass through an added block

Suppose the assertions hold for the preceding sum \(C\), and add
\[
S=\bigoplus_{j=1}^mO_c(d_j),\qquad c\in U.
\]
Every model has free stalks, upper quotients, generation, and flabbiness. Nonnegative shifts retain those properties, and the finite-sum theorem transfers them to \(S\), then to \(C\oplus S\).

### Step 3. Preserve minimality outside U

Fix \(x\notin U\). Since \(c\in U\), we have \(x\ne c\). The model-family minimality condition gives
\(K_x(O_c)\subseteq JO_c^x\).
It holds for every shift \(O_c(d_j)\), since the underlying maps are unchanged.

The finite-sum kernel and ideal-multiple theorem gives minimality of \(S\) at \(x\). The induction hypothesis gives it for \(C\). Applying the same theorem to their product gives
\(K_x(C\oplus S)\subseteq J(C\oplus S)^x\).

### Step 4. Enlarge the allowed center set

Every center used by the construction belongs to \(U\). If \(U\subseteq T\), it also belongs to \(T\). The zero constructor is valid for either set, and every added block remains valid with the enlarged center condition. Induction on the construction proves the final assertion.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.mono`: [MinimalExtensions.lean:683](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L683).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.free`: [MinimalExtensions.lean:689](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L689).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.quotient`: [MinimalExtensions.lean:698](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L698).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.generated`: [MinimalExtensions.lean:707](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L707).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.flabby`: [MinimalExtensions.lean:715](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L715).

`OAI.KLInvariance.MomentGraph.GradedSheaf.ModelSum.minimal`: [MinimalExtensions.lean:720](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L720).
