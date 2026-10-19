---
id: kl.sheaves.partial_iso_extension
title: Extending a partial sheaf isomorphism across one vertex
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.sheaf_isomorphisms
- kl.detail.upper_quotient
- kl.detail.graded_maps_shifts
lean:
  repository: openai-kl
  modules:
  - GradedSheaves
  - MinimalExtensions
  declarations:
  - OAI.KLInvariance.MomentGraph.Sheaf.OnIso.extend
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso.extend
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.GradedSheaves:995
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.Sheaf.OnIso.extend
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.MinimalExtensions:229
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso.extend
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

# Extending a partial sheaf isomorphism across one vertex

Let \(B,C\) be graded sheaves on the same ordered graph, satisfying the upper-quotient rule for the same labels. Let \(U\) be upper, and let \(j\) be a graded isomorphism on \(U\): it supplies vertex maps at \(y\in U\), edge maps when \(t(e)\in U\), and the appropriate restriction squares.

Choose \(x\notin U\) with every \(y>x\) in \(U\). Suppose a degree-zero stalk isomorphism
\[
j_x:B^x\xrightarrow{\sim}C^x
\]
satisfies the lower commuting square on every outgoing edge from \(x\):
\[
j_e\rho^{B,-}_e=\rho^{C,-}_e j_x.
\]
Then \(j\) extends to a graded isomorphism on \(U\cup\{x\}\).

*Proof.*

### Step 1. Retain the old vertex and edge maps

Use \(j_x\) at the new vertex and the old maps at vertices of \(U\). For an edge with target in \(U\), retain its old edge isomorphism.

The edge maps that still need to be defined have target exactly \(x\).

### Step 2. Define incoming edge maps through the upper quotients

For an edge \(e:z\to x\), the quotient rules identify
\[
B^e=B^x/\alpha_eB^x,\qquad C^e=C^x/\alpha_eC^x.
\]
Linearity and bijectivity of \(j_x\) give
\(j_x(\alpha_eB^x)=\alpha_eC^x\). Hence it induces an isomorphism of these quotients. Use this as \(j_e\).

By construction,
\(j_e\rho^{B,+}_e=\rho^{C,+}_e j_x\), so the new upper square commutes.

### Step 3. Verify every lower square in the enlarged set

If the source lies in \(U\), its target lies in \(U\) because \(U\) is upper. This is an old commuting square.

If the source is \(x\), its target is strictly above \(x\), hence belongs to \(U\). The edge map is an old one, and the required lower square is exactly the hypothesis on \(j_x\).

These cover all edges with both endpoints in \(U\cup\{x\}\). In particular, for an edge ending at \(x\), its source is outside \(U\), since otherwise upper closure would put \(x\) in \(U\).

### Step 4. Verify grading of a new edge map

Let \(z\in B^e_n\) on an incoming edge. Since the upper restriction \(B^x\to B^e\) is a surjective degree-zero map, \(z\) has a homogeneous lift \(v\in B^x_n\): take the degree-\(n\) component of any lift.

The induced edge map sends \(z\) to
\(\rho^{C,+}_e(j_x(v))\), which lies in \(C^e_n\). Thus the new edge map preserves degree. The old components and \(j_x\) already do, completing the graded partial isomorphism.

## References

The local source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.Sheaf.OnIso.extend`: [GradedSheaves.lean:995](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/GradedSheaves.lean#L995).

`OAI.KLInvariance.MomentGraph.GradedSheaf.OnIso.extend`: [MinimalExtensions.lean:229](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/MinimalExtensions.lean#L229).
