---
id: kl.sheaves.split_sheaf_properties
title: Sheaf properties inherited by a graded split summand
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.detail.split_summands
- kl.sheaves.flabbiness
- kl.detail.upper_quotient
- kl.notes.graded_projective_free
lean:
  repository: openai-kl
  modules:
  - Support
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.flabby
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.generated
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.upperQuotient
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_projective
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_free
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:144
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.flabby
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:155
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.generated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:164
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.upperQuotient
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:194
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_projective
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:200
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_free
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

# Sheaf properties inherited by a graded split summand

Let \(B,C\) be graded sheaves over the same coefficient algebra and graph. Suppose
\[
i:B\to C,\qquad p:C\to B,\qquad pi=1_B
\]
are graded sheaf morphisms. Then flabbiness, global generation, and the upper-quotient rule pass from \(C\) to \(B\).

Each stalk \(B^x\) is projective whenever \(C^x\) is projective. Over a connected nonnegatively graded Noetherian domain, the finite nonnegative graded stalk \(B^x\) is then graded free.

*Proof.*

### Step 1. Extend a section through the inclusion and projection

Let \(U\) be upper and let \(f\) be a \(B\)-assignment compatible on \(U\). Apply \(i\) coordinatewise; its commuting squares give a \(C\)-assignment compatible on \(U\).

If \(C\) is flabby, extend it to a global section \(g\). Applying \(p\) gives a global section of \(B\). For \(x\in U\),
\[
p_x(g_x)=p_x(i_x(f_x))=f_x.
\]
Thus \(B\) is flabby.

### Step 2. Generate a stalk value

For \(v\in B^x\), global generation of \(C\) supplies a global section \(g\) with \(g_x=i_x(v)\). Its projection is global and has value
\(p_x(g_x)=p_xi_x(v)=v\).
Hence \(B\) is globally generated.

### Step 3. Prove surjectivity of the upper restriction

Fix an edge \(e:x\to y\), and take \(z\in B^e\). The upper restriction of \(C\) is onto, so choose \(w\in C^y\) with
\(\rho^{C,+}_e(w)=i_e(z)\).
The commuting square for \(p\) gives
\[
\rho^{B,+}_e(p_y(w))
=p_e(\rho^{C,+}_e(w))
=p_ei_e(z)=z.
\]

### Step 4. Identify the upper kernel

Suppose \(\rho^{B,+}_e(v)=0\). Inclusion gives
\[
\rho^{C,+}_e(i_y(v))=i_e(\rho^{B,+}_e(v))=0.
\]
The quotient rule in \(C\) gives \(i_y(v)=\alpha_e w\) for some \(w\in C^y\). Applying \(p_y\) yields
\[
v=\alpha_e p_y(w).
\]
Thus the kernel in \(B\) is contained in \(\alpha_e B^y\).

Conversely, if \(v=\alpha_e v'\), then \(i_y(v)=\alpha_e i_y(v')\) lies in the upper kernel in \(C\). Hence
\(i_e(\rho^{B,+}_e(v))=0\). The map \(i_e\) is injective because \(p_ei_e=1\), so \(\rho^{B,+}_e(v)=0\). This proves the reverse containment.

### Step 5. Transfer projectivity and use the graded free-basis theorem

At each vertex, \(p_xi_x=1\) makes \(B^x\) a direct summand of \(C^x\). To verify projectivity explicitly, take a surjection \(q:X\to Y\) and a map \(a:B^x\to Y\). If \(C^x\) is projective, lift \(a p_x:C^x\to Y\) to \(l:C^x\to X\). Then
\[
q(l i_x)=a p_xi_x=a,
\]
so every such map from \(B^x\) lifts. This is projectivity.

The stalk is finite and nonnegatively graded by the sheaf data. Over the stated connected graded Noetherian domain, the [[node:kl.notes.graded_projective_free|graded projective-to-free theorem]] supplies a finite homogeneous free basis. Thus the inherited projective stalk is graded free.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.flabby`: [Support.lean:144](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L144).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.generated`: [Support.lean:155](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L155).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.upperQuotient`: [Support.lean:164](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L164).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_projective`: [Support.lean:194](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L194).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SplitIn.vertex_free`: [Support.lean:200](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L200).
