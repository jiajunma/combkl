---
id: kl.realization.signed_root_representation
title: A root represented by a reflection and a sign bit
kind: definition
status: formalized
primary_topic: kl.realizations
topics:
- kl.realizations
uses:
- kl.detail.positive_roots
- kl.coxeter.signed_reflection_action
- kl.realization.simple_root_sign
lean:
  repository: openai-kl
  modules:
  - Tits
  declarations:
  - OAI.KLInvariance.TitsSpace.SignedRepresents
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Tits:1891
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.SignedRepresents
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are all action, sign, and length conventions retained?
  verdict: Read the finite-rank Tits proofs, the exact two-generator tail convention,
    and both group-action directions; the chosen smaller induction instance is explicit.
tags:
- Kazhdan-Lusztig
- root-geometry
---

# A root represented by a reflection and a sign bit

Let \(a\) be a vector in the ordinary Tits root space and let \((t,\varepsilon)\in W\times\mathbb Z/2\mathbb Z\). Say that this pair represents \(a\) with its sign when:

- \(a\) represents \(t\): there are \(w,i\) with \(a=\rho_0(w)\alpha_i\) and \(t=ws_iw^{-1}\);
- either \(\varepsilon=0\) and every coordinate of \(a\) is nonnegative, or \(\varepsilon=1\) and every coordinate is nonpositive.

The first condition supplies an actual real root and its reflection. Its squared Tits norm is two, so it is nonzero. The two sign alternatives are consequently exclusive.

Every real root has one of these signs. A positive representative gives the pair \((t,0)\), while its negative gives \((t,1)\). Negating the root retains its reflection: replacing \(w\) by \(ws_i\) negates \(\rho_0(w)\alpha_i\) and leaves \(ws_iw^{-1}\) unchanged.

## Compatibility with the signed group action

The combinatorial signed action already conjugates the reflection label and toggles the bit when a simple generator acts on its own reflection label. The root-action theorem proves that this same rule describes the actual coordinate sign of the transformed root.

For a simple root, the two represented vectors are \(\alpha_i\) and \(-\alpha_i\), with pairs \((s_i,0)\) and \((s_i,1)\). Applying \(s_i\) exchanges the two vectors and toggles the bit. The general theorem extends this calculation to every root and every group element.

## References

The local action and sign calculations are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.SignedRepresents`: [Tits.lean:1891](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Tits.lean#L1891).
