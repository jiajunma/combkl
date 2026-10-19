---
id: kl.word.weight_support
title: Reduced-word weights fill the Bruhat interval
kind: theorem
status: proved
primary_topic: kl.word_modules
topics:
- kl.word_modules
uses:
- kl.notes.bott_samelson
- kl.word.evaluation_maps
- kl.notes.word_stalks
- kl.foundations.subword
- kl.coxeter.word_reduction
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  - Frobenius
  declarations:
  - OAI.KLInvariance.TitsSpace.bottSubword
  - OAI.KLInvariance.TitsSpace.bottSubword_sublist
  - OAI.KLInvariance.TitsSpace.bottSubword_wordProd
  - OAI.KLInvariance.TitsSpace.exists_bottSubword
  - OAI.KLInvariance.TitsSpace.bottWeight_bruhat
  - OAI.KLInvariance.TitsSpace.exists_bottWeight
  - OAI.KLInvariance.TitsSpace.bottWeight_range
  - OAI.KLInvariance.TitsSpace.bottEvaluation_unit
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1678
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSubword
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1682
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSubword_sublist
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1693
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottSubword_wordProd
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1702
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_bottSubword
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1713
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_bruhat
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1718
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.exists_bottWeight
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Frobenius:1724
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottWeight_range
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:280
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottEvaluation_unit
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the rings, scalar maps, finiteness hypotheses, pairing orientation and
    degree conventions explicit?
  verdict: Read the sublist/bit-string recursion and both range inclusions. Kept arbitrary
    generator sets for the combinatorial statement and the finite-generator coefficient
    context for the derived stalk-support statement.
tags:
- Kazhdan-Lusztig
- Frobenius-duality
---

# Reduced-word weights fill the Bruhat interval

Let \(\mathbf t\) be a reduced word for \(b\) in a Coxeter system. Then its subexpression weights are exactly the elements below \(b\) in strong Bruhat order:
\[
\{w_{\mathbf t}(\eta):\eta\in J_{\mathbf t}\}=[1,b].
\]
This weight statement permits an arbitrary simple-generator set.

For a finite simple-generator set, form the actual tensor word module over its real symmetric coefficient algebra. Its weight stalk satisfies
\[
M_{\mathbf t}^x\ne0\quad\Longleftrightarrow\quad x\le b.
\]

*Proof.*

### Step 1. Turn each bit string into a subword

Define \(\nu(\eta)\) by retaining precisely those letters whose bit is \(1\), in their original order. Recursively,
\[
\nu(())=[],\qquad
\nu(0,\eta)=\nu(\eta),\qquad
\nu(1,\eta)=s\,\nu(\eta)
\]
for a word beginning with \(s\).

At a zero bit the first letter is omitted; at a one bit it is retained. Induction on the word therefore proves that \(\nu(\eta)\) is a sublist of \(\mathbf t\). The product recursion gives
\(\operatorname{prod}(\nu(\eta))=w_{\mathbf t}(\eta)\).
These are the source's bottSubword_sublist and bottSubword_wordProd.

### Step 2. Bound every weight by the reduced-word product

Every word has a reduced subword with the same product. Apply this to \(\nu(\eta)\). The resulting reduced word is still a subword of the fixed reduced word \(\mathbf t\).

The [[node:kl.foundations.subword|reduced-subword criterion]] therefore gives
\[
w_{\mathbf t}(\eta)=\operatorname{prod}(\nu(\eta))\le b.
\]
This is the source's bruhat_of_subword application in bottWeight_bruhat.

### Step 3. Realize every element of the interval

If \(x\le b\), the [[node:kl.foundations.subword|reduced-subword criterion]] supplies a sublist \(\nu\) of \(\mathbf t\) whose product is \(x\). Mark its retained positions by \(1\) and all others by \(0\).

More formally, induction on the sublist witness inserts a zero bit when a letter is skipped and a one bit when it is retained. This constructs \(\eta\) with \(\nu(\eta)=\nu\). Its weight is \(x\), by Step 1. Together with Step 2, this proves the range equality.

### Step 4. Translate weight support into stalk support

The stalk \(M_{\mathbf t}^x\) is the image of evaluation into \(A^{J_x}\), where
\(J_x=\{\eta:w_{\mathbf t}(\eta)=x\}\).

If \(x\not\le b\), the index set \(J_x\) is empty by Steps 2–3. Its coordinate module is zero, so the stalk is zero.

If \(x\le b\), choose \(\eta\in J_x\). The unit tensor evaluates to \(1\) at this coordinate. Since the real coefficient algebra is nonzero, its stalk projection is a nonzero vector. Thus the stalk is nonzero. This last calculation is the stalk interpretation of the source's exact weight range.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.TitsSpace.bottSubword`: [Frobenius.lean:1678](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1678).

`OAI.KLInvariance.TitsSpace.bottSubword_sublist`: [Frobenius.lean:1682](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1682).

`OAI.KLInvariance.TitsSpace.bottSubword_wordProd`: [Frobenius.lean:1693](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1693).

`OAI.KLInvariance.TitsSpace.exists_bottSubword`: [Frobenius.lean:1702](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1702).

`OAI.KLInvariance.TitsSpace.bottWeight_bruhat`: [Frobenius.lean:1713](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1713).

`OAI.KLInvariance.TitsSpace.exists_bottWeight`: [Frobenius.lean:1718](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1718).

`OAI.KLInvariance.TitsSpace.bottWeight_range`: [Frobenius.lean:1724](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Frobenius.lean#L1724).

`OAI.KLInvariance.TitsSpace.bottEvaluation_unit`: [BottSamelson.lean:280](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L280).
