---
id: kl.local.product_image_scaling
title: Associated factor counts determine scalar-image submodules
kind: theorem
status: proved
primary_topic: kl.localization
topics:
- kl.localization
uses:
- kl.algebra.linear_ideals
lean:
  repository: openai-kl
  modules:
  - PlaneLocalization
  declarations:
  - OAI.KLInvariance.LocalProducts.smul_top_le_of_map_dvd
  - OAI.KLInvariance.LocalProducts.smul_top_eq_of_map_associated
  - OAI.KLInvariance.LocalProducts.associated_prod_power
  - OAI.KLInvariance.LocalProducts.associated_prod_scale
  - OAI.KLInvariance.LocalProducts.product_image_scale
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1488
    format: lean-location
    note: OAI.KLInvariance.LocalProducts.smul_top_le_of_map_dvd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1498
    format: lean-location
    note: OAI.KLInvariance.LocalProducts.smul_top_eq_of_map_associated
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1505
    format: lean-location
    note: OAI.KLInvariance.LocalProducts.associated_prod_power
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1509
    format: lean-location
    note: OAI.KLInvariance.LocalProducts.associated_prod_scale
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PlaneLocalization:1523
    format: lean-location
    note: OAI.KLInvariance.LocalProducts.product_image_scale
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the ambient modules, pairing orientation, scalar types, grading conventions
    and quantified hypotheses explicit?
  verdict: Read all five LocalProducts lemmas with their arbitrary commutative scalar
    rings and compatible module actions. Expanded divisibility-to-image inclusion,
    both association containments, products of units, the exact cardinality/power
    identity and the final scalar-tower calculation. Kept the count as a hypothesis
    for the later dihedral application.
tags:
- Kazhdan-Lusztig
- correction-factors
---

# Associated factor counts determine scalar-image submodules

Let \(R,S\) be commutative rings with scalar map \(\eta:R\to S\). Let \(M\) be an \(S\)-module with its compatible \(R\)-action:
\[
r\,m=\eta(r)m.
\]
Let \(I,J\) be finite index sets, \(a_i,b_j,f\in R\), \(p\in S\), and \(k\in\mathbb N\). Assume
\[
\eta(a_i)\sim p\quad(i\in I),\qquad
\eta(b_j)\sim p\quad(j\in J),\qquad
\eta(f)\sim p^k,
\]
and
\[
|I|=|J|+k.
\]
Then the following are equal as \(R\)-submodules of the same module \(M\):
\[
\left(\prod_{i\in I}a_i\right)M
=f\left(\left(\prod_{j\in J}b_j\right)M\right).
\]
Here \(rM\) denotes the image of scalar multiplication by \(r\), and associated elements differ by a unit.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Associated products give the local scalar-image calculation.**

**OpenAI notes:** In a localized edge quotient viewed as a discrete valuation ring, the notes compare valuations of later-label products. The current plane contributes its exponent to the correction factor, and all other plane factors are units. [edge:bound](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L47).

**Lean (primary):** The factor proof directly establishes association with the power of a chosen reduced plane root, checking the same-plane and other-plane factors and the absent-plane case. LocalProducts then works over arbitrary compatible commutative scalar rings: a cardinality equation and associated factors give equality of scalar-image submodules. [PlaneLocalization:1560](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1560), [PlaneLocalization:1569](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1569), [PlaneLocalization:1579](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1579), [PlaneLocalization:1509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1509), [PlaneLocalization:1523](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1523).

**Role in the proof:** The Blueprint explains the unit and power calculations explicitly. The later-edge count remains the stated hypothesis of the product-image lemma until the dihedral transport argument supplies it.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Convert divisibility in S into inclusion of images

Suppose \(\eta(q)\mid\eta(r)\), so \(\eta(r)=\eta(q)t\) for some \(t\in S\). For any \(m\in M\), compatibility of the two scalar actions gives
\[
rm=\eta(r)m=\eta(q)(tm)=q(tm).
\]
Since \(tm\in M\), every element of \(rM\) lies in \(qM\).

If \(\eta(r)\sim\eta(q)\), the two elements divide one another. Applying this argument in both directions gives \(rM=qM\).

### Step 2. Count the powers in each product

Choose units \(u_i,v_j\in S^\times\) with
\[
\eta(a_i)=u_ip,\qquad \eta(b_j)=v_jp.
\]
Products of units are units, so
\[
\prod_i\eta(a_i)\sim p^{|I|},\qquad
\prod_j\eta(b_j)\sim p^{|J|}.
\]
For an empty index set the product and the corresponding zeroth power are both \(1\). This is associated_prod_power.

### Step 3. Insert the correction exponent

The cardinality hypothesis gives
\[
p^{|I|}=p^{|J|+k}=p^k p^{|J|}.
\]
Together with \(\eta(f)\sim p^k\) and Step 2, this yields
\[
\prod_i\eta(a_i)\sim
\eta(f)\prod_j\eta(b_j).
\]
This is associated_prod_scale: it follows by multiplying the relevant units and using the displayed power identity.

### Step 4. Return to the R-submodules

The scalar map preserves products, so Step 3 is
\[
\eta\left(\prod_i a_i\right)
\sim\eta\left(f\prod_jb_j\right).
\]
Step 1 now gives
\[
\left(\prod_i a_i\right)M
=\left(f\prod_jb_j\right)M
=f\left(\left(\prod_jb_j\right)M\right).
\]
The last equality follows from associativity of scalar multiplication, in both containment directions.

In the edge application, \(R\) is the plane ring, \(S\) the localized edge quotient, and \(M\) the supported model edge module. The reduced labels and correction factor satisfy the displayed associations. The later-edge counting theorem supplies the cardinality equation; this result converts it into equality of the two embedded product images.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.LocalProducts.smul_top_le_of_map_dvd`: [PlaneLocalization.lean:1488](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1488).

`OAI.KLInvariance.LocalProducts.smul_top_eq_of_map_associated`: [PlaneLocalization.lean:1498](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1498).

`OAI.KLInvariance.LocalProducts.associated_prod_power`: [PlaneLocalization.lean:1505](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1505).

`OAI.KLInvariance.LocalProducts.associated_prod_scale`: [PlaneLocalization.lean:1509](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1509).

`OAI.KLInvariance.LocalProducts.product_image_scale`: [PlaneLocalization.lean:1523](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PlaneLocalization.lean#L1523).
