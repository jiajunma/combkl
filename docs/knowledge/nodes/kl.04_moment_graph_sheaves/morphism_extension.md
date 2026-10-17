---
id: kl.detail.morphism_extension
title: Extending a sheaf morphism from an upper set
kind: theorem
status: proved
primary_topic: kl.04_moment_graph_sheaves
topics:
- kl.04_moment_graph_sheaves
uses:
- kl.detail.sheaf_morphism
- kl.detail.upper_quotient
- kl.sheaves.flabbiness
- kl.detail.compatible_sections
lean:
  repository: openai-kl
  modules:
  - SheafMorphisms
  declarations:
  - OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.SheafMorphisms:834
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension
  - artifact: openai-kl-paper
    locator: Related paper context; bg:bmp
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
- moment_graph_sheaves
---

# Extending a sheaf morphism from an upper set

Let \(A\) be a connected nonnegatively graded Noetherian domain, and let the labelled ordered graph be finite. Suppose \(B\) and \(C\) satisfy the upper quotient rule, are flabby and globally generated, and every stalk of \(B\) is free. Then a graded sheaf morphism on an upper set \(U\) extends to a graded morphism \(B\to C\) agreeing with all its prescribed vertex maps.

*Proof.*

### Step 1. Identify the boundary map forced at the next vertex

Suppose a morphism is already defined on an upper set \(U\), and choose a maximal missing vertex \(x\). Every outgoing target of \(x\) lies in \(U\).

The existing edge maps send boundary tuples of \(B\)-sections above \(x\) to boundary tuples of \(C\)-sections above \(x\). Thus they induce a graded map \(D_B(x)\to D_C(x)\) between boundary images.

For either sheaf, the image of the stalk boundary map equals this boundary image. One containment follows from global generation: realize any stalk value by a global section. The reverse containment follows from flabbiness: extend a section above \(x\) globally and take its value at \(x\). Both hypotheses in the statement are used here.

### Step 2. Lift the required boundary map to a stalk map

Compose \(B^x\to D_B(x)\to D_C(x)\). The map \(C^x\twoheadrightarrow D_C(x)\) is surjective by its definition as an image.

Choose a homogeneous basis of the free graded module \(B^x\). For a basis vector of degree \(n\), choose any preimage in \(C^x\) of its required boundary value, then retain the degree-\(n\) component of that preimage. Since the quotient map preserves degree, this component still has the required image. Extending linearly gives a degree-zero map \(f_x:B^x\to C^x\) with the required boundary equation.

### Step 3. Define the new edge maps and check well-definedness

For an incoming edge \(e:z\to x\), the map on its upper stalk \(x\) induces
\[
B^x/\alpha_eB^x\longrightarrow C^x/\alpha_eC^x.
\]
It is well-defined because \(A\)-linearity sends \(\alpha_ev\) to \(\alpha_ef_x(v)\). Use the upper quotient identifications to obtain the edge map. The lower vertex \(z\) is not in \(U\): otherwise the upper-set property would already put \(x\) in \(U\). Hence no previously imposed lower square is disturbed.

For outgoing edges \(x\to y\), the edge map is already determined by the upper data. The boundary equation from Step 2 is precisely the required lower commuting square. Old squares remain unchanged.

### Step 4. Complete finite downward induction

We have extended the partial morphism from \(U\) to \(U\cup\{x\}\), preserving all its old vertex maps. This new set is upper, because all vertices strictly above \(x\) were already present. Its complement is smaller. Repeat until no vertex is missing.

This proves an actual sheaf morphism: both endpoint squares commute on every edge, rather than merely giving unrelated maps of stalks.

## References

[Related paper context](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/02-background.tex#L225).

## Lean formalization



`OAI.KLInvariance.MomentGraph.GradedSheaf.OnHom.exists_extension`: [SheafMorphisms.lean:834](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/SheafMorphisms.lean#L834).
