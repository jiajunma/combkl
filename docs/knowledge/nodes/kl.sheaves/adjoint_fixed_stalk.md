---
id: kl.sheaves.adjoint_fixed_stalk
title: Fixed stalks and the top normalization of adjoint projectors
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.word_adjoint_descent
- kl.word.support_duality
- kl.word.top_stalk
- kl.detail.split_summands
- kl.sheaves.boundary_sheaf
lean:
  repository: openai-kl
  modules:
  - BalancedPairings
  - Support
  declarations:
  - OAI.KLInvariance.TitsSpace.bottEndOfSheaf_fixed_support
  - OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk
  - OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk_iff
  - OAI.KLInvariance.Graded.ModuleData.unit_split_reverse
  - OAI.KLInvariance.TitsSpace.bottBoundarySplit_top_fixed
  - OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_top_fixed
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1466
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEndOfSheaf_fixed_support
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1478
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BalancedPairings:1495
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk_iff
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:39
    format: lean-location
    note: OAI.KLInvariance.Graded.ModuleData.unit_split_reverse
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:85
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySplit_top_fixed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:94
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_top_fixed
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

# Fixed stalks and the top normalization of adjoint projectors

Fix a reduced word in a finite-generator Coxeter system and a basis of its real extended realization. Use its graded symmetric coefficient algebra and graded word sheaf \(W\), with the symmetric perfect word pairing. Let \(h:W\to W\) be a graded sheaf endomorphism, and let \(h^*\) be its descended adjoint.

At any vertex \(x\),
\[
h_x=1\quad\Longleftrightarrow\quad h_x^*=1.
\]
In particular, if a normalized boundary sheaf \(B\) is split into \(W\) by
\(i:B\to W,\ p:W\to B,\ pi=1\), then the projector \(e=ip\) and its adjoint satisfy
\[
e_b=1_{W^b},\qquad e_b^*=1_{W^b}
\]
at the top vertex \(b\).

*Proof.*

### Step 1. Fix every word element supported at x

Let \(F\) be the word-module endomorphism induced by \(h\), and assume \(h_x=1\).
For \(s\) supported at weight \(x\), the coordinate identity gives
\[
\pi_x(Fs)=h_x(\pi_x(s))=\pi_x(s).
\]
At other weights both \(s\) and \(Fs\) have zero coordinates, because \(F\) preserves support. Their full evaluation tuples agree, and injectivity of evaluation gives \(Fs=s\).

### Step 2. Test the difference made by the adjoint

For arbitrary \(m\) and any \(s\) supported at \(x\), symmetry and the adjoint equation give
\[
\langle s,F^*m-m\rangle
=\langle Fs,m\rangle-\langle s,m\rangle=0.
\]
The [[node:kl.sheaves.word_adjoint_descent|projection-kernel criterion]] therefore gives
\[
\pi_x(F^*m-m)=0,\qquad \pi_x(F^*m)=\pi_x(m).
\]
By the descent formula, this is
\(h_x^*(\pi_x(m))=\pi_x(m)\).
The stalk projection is surjective, so \(h_x^*\) is the identity on the entire stalk.

Applying the same implication to \(h^*\), and using the double-adjoint identity, proves the converse.

### Step 3. Reverse a split pair on rank-one modules

The boundary top stalk and the reduced-word top stalk are both graded isomorphic to \(A\). Use these identifications to view \(i_b,p_b\) as \(A\)-linear maps \(A\to A\).

Any such map is multiplication by its value at \(1\). Write these values as \(a,c\), so \(i_b(r)=ar\) and \(p_b(r)=cr\). The splitting \(p_bi_b=1\) gives \(ca=1\). Commutativity gives \(ac=1\), hence \(i_bp_b=1\).

Transporting back to the top stalk gives \(e_b=1_{W^b}\).

### Step 4. Normalize the adjoint projector

Apply Steps 1–2 to the projector \(e\) at \(b\). Since \(e_b=1\), its adjoint also satisfies \(e_b^*=1\). Therefore the image of \(e^*\) has the whole word stalk at the top, with the same rank-one degree-zero normalization.

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottEndOfSheaf_fixed_support`: [BalancedPairings.lean:1466](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1466).

`OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk`: [BalancedPairings.lean:1478](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1478).

`OAI.KLInvariance.TitsSpace.bottAdjointSheaf_fixed_stalk_iff`: [BalancedPairings.lean:1495](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BalancedPairings.lean#L1495).

`OAI.KLInvariance.Graded.ModuleData.unit_split_reverse`: [Support.lean:39](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L39).

`OAI.KLInvariance.TitsSpace.bottBoundarySplit_top_fixed`: [Support.lean:85](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L85).

`OAI.KLInvariance.TitsSpace.bottBoundarySplitAdjoint_top_fixed`: [Support.lean:94](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L94).
