---
id: kl.word.set_tail_maps
title: Tail maps on coordinate-image modules
kind: definition
status: formalized
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.word.coordinate_images
- kl.word.tail_maps
- kl.word.reflected_sets
- kl.algebra.projective_range_splittings
- kl.word.local_pair_maps
lean:
  repository: openai-kl
  modules:
  - IntegralPairings
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSetFirst
  - OAI.KLInvariance.TitsSpace.bottSetSecond
  - OAI.KLInvariance.TitsSpace.bottSetFirst_project
  - OAI.KLInvariance.TitsSpace.bottSetSecond_project
  - OAI.KLInvariance.TitsSpace.bottSeed
  - OAI.KLInvariance.TitsSpace.bottSeed_first
  - OAI.KLInvariance.TitsSpace.bottSeed_second
  - OAI.KLInvariance.TitsSpace.bottSetFirst_seed
  - OAI.KLInvariance.TitsSpace.bottSetSecond_seed
  - OAI.KLInvariance.TitsSpace.bottSetFirst_restrict
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:673
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetFirst
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:679
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetSecond
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:687
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetFirst_project
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:691
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetSecond_project
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:913
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSeed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:916
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSeed_first
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:919
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSeed_second
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:922
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetFirst_seed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:928
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetSecond_seed
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.IntegralPairings:948
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSetFirst_restrict
verification:
  definition: accepted
  proof: not_applicable
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the scalar actions, coordinate sets, kernel maps and induction hypotheses
    explicit?
  verdict: Read both descended maps, seed identities and restriction commutation.
    Kept the second target twisted and the reflected set sU explicit, with well-definedness
    tied to the precise kernel criterion.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Tail maps on coordinate-image modules

Fix a finite-generator Coxeter system with symmetric coefficient algebra \(A\). Prepend a simple reflection \(s\) to a word \(\mathbf t\), and write \(\tau=\chi_s\). Let
\[
\mu:M_{s\mathbf t}\to M_{\mathbf t},\qquad
\nu:M_{s\mathbf t}\to{}^\tau M_{\mathbf t}
\]
be the ordinary and reflected tail maps.

For \(U\subseteq W\), write \(p_U'\) for the new word projection to \(L_{s\mathbf t}(U)\) and \(p_U\) for the tail projection to \(L_{\mathbf t}(U)\). The image tail maps are
\[
F_U:L_{s\mathbf t}(U)\to L_{\mathbf t}(U),
\qquad F_U(p_U'(m))=p_U(\mu(m)),
\]
and
\[
G_U:L_{s\mathbf t}(U)\to{}^\tau L_{\mathbf t}(sU),
\qquad G_U(p_U'(m))=p_{sU}(\nu(m)).
\]
The second formula denotes an element in the twisted target. The source names these maps bottSetFirst and bottSetSecond.

For each \(x\in U\), the [[node:kl.word.local_pair_maps|local-pair criterion]] identifies vanishing of the new stalk projection with vanishing of the ordinary tail at \(x\) and the reflected tail at \(sx\). Collecting these conditions over \(U\) gives vanishing of the ordinary tail on \(U\) and the reflected tail on \(sU\). Each displayed composite therefore kills \(\ker p_U'\), and descends through this surjection.

## The unit-tensor insertion

The source's bottSeed is
\[
n\longmapsto 1\otimes n\in M_{s\mathbf t}.
\]
Both tail maps return the underlying vector \(n\) on this tensor. Consequently
\[
F_U(p_U'(1\otimes n))=p_U(n),\qquad
G_U(p_U'(1\otimes n))=p_{sU}(n)
\]
in their respective ordinary and twisted targets.

These formulas give concrete preimages when studying the first image map and its restrictions to kernels.

## Restriction and the first image map

For \(U\subseteq K\), restriction commutes with the first map:
\[
F_U r'_{K,U}=r_{K,U}F_K.
\]
To verify this, lift an image vector to \(m\in M_{s\mathbf t}\). Both sides have coordinates \(\pi_x(\mu(m))\) for \(x\in U\).

The [[node:kl.word.set_tail_detection|set-tail detection theorem]] also proves that \((F_U,G_U)\) is injective. Thus the two descended tail coordinates determine each new image vector.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSetFirst`: [IntegralPairings.lean:673](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L673).

`OAI.KLInvariance.TitsSpace.bottSetSecond`: [IntegralPairings.lean:679](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L679).

`OAI.KLInvariance.TitsSpace.bottSetFirst_project`: [IntegralPairings.lean:687](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L687).

`OAI.KLInvariance.TitsSpace.bottSetSecond_project`: [IntegralPairings.lean:691](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L691).

`OAI.KLInvariance.TitsSpace.bottSeed`: [IntegralPairings.lean:913](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L913).

`OAI.KLInvariance.TitsSpace.bottSeed_first`: [IntegralPairings.lean:916](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L916).

`OAI.KLInvariance.TitsSpace.bottSeed_second`: [IntegralPairings.lean:919](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L919).

`OAI.KLInvariance.TitsSpace.bottSetFirst_seed`: [IntegralPairings.lean:922](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L922).

`OAI.KLInvariance.TitsSpace.bottSetSecond_seed`: [IntegralPairings.lean:928](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L928).

`OAI.KLInvariance.TitsSpace.bottSetFirst_restrict`: [IntegralPairings.lean:948](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/IntegralPairings.lean#L948).
