---
id: kl.sheaves.upper_interval_kernels
title: Stalk characters and selected kernels under upper-interval restriction
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.interval_boundary
- kl.sheaves.upward_kernel
- kl.detail.boundary_uniqueness
- kl.duality.stalk_character
- kl.sheaves.kernel_transport
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - PositiveTransfer
  - SimultaneousInvariance
  declarations:
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_upperRestriction
  - OAI.KLInvariance.BruhatGraph.restrictBoundary_kernel
  - OAI.KLInvariance.BruhatGraph.intervalBoundary_upper_kernel
  - OAI.KLInvariance.BruhatGraph.boundarySheaf_gradedIso
  - OAI.KLInvariance.BruhatGraph.stalkCharacter_eq_character
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:337
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_upperRestriction
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:776
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.restrictBoundary_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance:85
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.intervalBoundary_upper_kernel
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:264
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.boundarySheaf_gradedIso
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:273
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.stalkCharacter_eq_character
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

# Stalk characters and selected kernels under upper-interval restriction

Fix the polynomial boundary-sheaf family \(\mathcal I_{u,b}\) obtained by restricting \(B(b)\). If \(u\le x\le z\le b\), the stalks of \(\mathcal I_{u,b}\) and \(\mathcal I_{x,b}\) at \(z\) identify with the same graded module \(B(b)^z\).

Let \(\iota\) be the graph inclusion \([x,b]\to[u,b]\), and let \(T\) be any set of edges in \([u,b]\). Under that stalk identification,
\[
K_z^{\mathcal I_{x,b}}(\iota_E^{-1}(T))
=K_z^{\mathcal I_{u,b}}(T).
\]
Here \(K_z(T)\) imposes the restrictions only for edges in \(T\) that start at \(z\).

The stalk character of the independently chosen normalized boundary sheaf on \([u,b]\), at \(z\), also equals the character of \(B(b)^z\).

*Proof.*

### Step 1. Compare the outgoing edges

Any edge of \([x,b]\) is an edge of \([u,b]\) with the same endpoints and label.

Conversely, if an edge of \([u,b]\) starts at \(z\ge x\), its target \(y\) satisfies \(x\le z<y\le b\). Hence it is an edge of \([x,b]\). This is precisely the outgoing-lift property at \(z\).

### Step 2. Compare the selected equations

Both stalk modules are \(B(b)^z\). The restriction map on a retained edge is copied from \(B(b)\) in both families.

An edge in \(T\) starting at \(z\) therefore appears among the smaller-interval conditions exactly through its preimage in \(\iota_E^{-1}(T)\). Every selected equation on either side is the same linear equation on the same vector. Their solution submodules are equal.

Their gradings are also equal, being induced from the same stalk grading.

### Step 3. Compare the normalized stalk characters

The pullback construction makes \(\mathcal I_{u,b}\) a normalized boundary sheaf on \([u,b]\). By [[node:kl.detail.boundary_uniqueness|boundary uniqueness]] it is graded-isomorphic to the independently chosen normalized boundary sheaf there.

More generally, let \(C\) be any normalized boundary sheaf on \([u,b]\). Boundary uniqueness gives a graded sheaf isomorphism \(j:B_{u,b}\to C\), where \(B_{u,b}\) is the chosen model used in the definition of stalkCharacter. If \((m_i)\) is a homogeneous basis of \(B_{u,b}^z\), the vectors \(j_z(m_i)\) form a basis of \(C^z\) with the same degrees: invertibility gives a basis, and the graded stalk map preserves each homogeneous piece. The two basis-degree polynomials are therefore equal.

Applying this to \(C=\mathcal I_{u,b}\) gives the asserted equality, since \(\mathcal I_{u,b}^{\,z}=B(b)^z\). This is stalkCharacter_eq_character followed by stalkCharacter_upperRestriction.

The kernel equality in Step 2 similarly transports any established freeness property of the selected submodule. This is the restriction step used when an induction hypothesis concerns a smaller upper interval.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.BruhatGraph.stalkCharacter_upperRestriction`: [EdgeLocalization.lean:337](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L337).

`OAI.KLInvariance.BruhatGraph.restrictBoundary_kernel`: [PositiveTransfer.lean:776](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L776).

`OAI.KLInvariance.BruhatGraph.intervalBoundary_upper_kernel`: [SimultaneousInvariance.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SimultaneousInvariance.lean#L85).

`OAI.KLInvariance.BruhatGraph.boundarySheaf_gradedIso`: [EdgeLocalization.lean:264](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L264).

`OAI.KLInvariance.BruhatGraph.stalkCharacter_eq_character`: [EdgeLocalization.lean:273](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L273).
