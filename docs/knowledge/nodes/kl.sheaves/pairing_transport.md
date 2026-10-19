---
id: kl.sheaves.pairing_transport
title: Transport of perfect section pairings through coefficient and sheaf isomorphisms
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.notes.supported_pairings
- kl.detail.coefficient_change
- kl.detail.sheaf_isomorphisms
- kl.algebra.coefficient_duals
lean:
  repository: openai-kl
  modules:
  - EdgeLocalization
  - Support
  declarations:
  - OAI.KLInvariance.CoefficientChange.dualEquiv
  - OAI.KLInvariance.CoefficientChange.pairingEquiv
  - OAI.KLInvariance.CoefficientChange.pairingEquiv_apply
  - OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.pullback
  - OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.coefficientChange
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.pullback
  - OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.coefficientChange
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1802
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.dualEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1824
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.pairingEquiv
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1829
    format: lean-location
    note: OAI.KLInvariance.CoefficientChange.pairingEquiv_apply
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1860
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.pullback
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Support:1884
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.coefficientChange
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:945
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.pullback
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.EdgeLocalization:953
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.coefficientChange
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

# Transport of perfect section pairings through coefficient and sheaf isomorphisms

Let \(S\) be a graded sheaf over \(A\) with a perfect support-orthogonal section pairing of shift \(L\). Let \(e:A\xrightarrow{\sim}A'\) preserve the coefficient gradings.

On the transported sheaf, define
\[
\langle m,n\rangle'=e(\langle m,n\rangle)
\]
using the corresponding underlying sections. This is a perfect support-orthogonal pairing of the same shift over \(A'\).

If \(j:T\xrightarrow{\sim}{}^eS\) is a graded sheaf isomorphism and \(J\) its map on global sections, then
\[
\langle u,v\rangle_T=\langle Ju,Jv\rangle'
\]
is a perfect support-orthogonal pairing on \(T\) of shift \(L\). Symmetry is preserved by both constructions.

*Proof.*

### Step 1. Verify linearity after changing coefficients

For \(a'\in A'\), the transported scalar action is multiplication by \(e^{-1}(a')\). Therefore
\[
\begin{aligned}
\langle a'm,n\rangle'
&=e(\langle e^{-1}(a')m,n\rangle)\\
&=e(e^{-1}(a')\langle m,n\rangle)
=a'\langle m,n\rangle'.
\end{aligned}
\]
The same calculation applies in the second argument, and additivity follows from additivity of \(e\) and the original form. Thus the new pairing is \(A'\)-bilinear.

### Step 2. Construct the representative of every new functional

The [[node:kl.algebra.coefficient_duals|coefficient-dual transport theorem]] supplies the following correspondence of functionals.

Let \(\lambda'\) be an \(A'\)-linear functional on the transported section module. On the underlying old module define
\[
\lambda(n)=e^{-1}(\lambda'(n)).
\]
For \(a\in A\), old multiplication by \(a\) is new multiplication by \(e(a)\), so
\[
\lambda(an)
=e^{-1}(e(a)\lambda'(n))
=a\lambda(n).
\]
Thus \(\lambda\) is \(A\)-linear.

The old perfect pairing supplies a unique \(m\) with
\(\langle m,n\rangle=\lambda(n)\) for every \(n\). Applying \(e\) gives
\(\langle m,n\rangle'=\lambda'(n)\).
Uniqueness follows by applying \(e^{-1}\) and the old uniqueness. This proves perfection over \(A'\).

### Step 3. Preserve grading, support, and symmetry

For homogeneous input degrees \(i,j\), the old value belongs to \(A_{i+j-L}\). Its image under \(e\) belongs to \(A'_{i+j-L}\).

Changing the scalar action leaves zero coordinates and vertex support unchanged. Each old support-orthogonality equation is therefore transported by applying \(e\), which sends zero to zero. If the old form is symmetric, applying \(e\) to its symmetry equation proves symmetry of the transported form.

### Step 4. Pull the pairing back through the section isomorphism

Let \(J:\Gamma(T)\xrightarrow{\sim}\Gamma({}^eS)\) be induced by \(j\). For any functional \(\mu\) on \(\Gamma(T)\), the composite \(\mu J^{-1}\) is a functional on \(\Gamma({}^eS)\). Let \(m\) be its unique representative for the transported pairing.

Then \(J^{-1}m\) represents \(\mu\) for the pulled-back pairing:
\[
\langle J^{-1}m,v\rangle_T
=\langle m,Jv\rangle'
=(\mu J^{-1})(Jv)=\mu(v).
\]
Uniqueness follows from bijectivity of \(J\) and perfection of the transported form.

### Step 5. Check the remaining pulled-back properties

The section map \(J\) preserves degree because each \(j_x\) does. Thus the shift remains \(L\).

If \(u\) is supported at \(x\), then \(Ju\) is supported at \(x\), since all component maps send zero to zero. If \(v_x=0\), then \((Jv)_x=0\). Left support orthogonality follows by substitution in the transported form. If \(u_x=0\) and \(v\) is supported at \(x\), then \((Ju)_x=0\) and \(Jv\) is supported at \(x\). The original right support condition therefore gives the right support equation for the pulled-back pairing. Symmetry follows by applying the symmetry of that form to \(Ju,Jv\).

## References

The source declarations below give the constructions and proofs.

## Lean formalization

`OAI.KLInvariance.CoefficientChange.dualEquiv`: [Support.lean:1802](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1802).

`OAI.KLInvariance.CoefficientChange.pairingEquiv`: [Support.lean:1824](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1824).

`OAI.KLInvariance.CoefficientChange.pairingEquiv_apply`: [Support.lean:1829](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1829).

`OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.pullback`: [Support.lean:1860](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1860).

`OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.coefficientChange`: [Support.lean:1884](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Support.lean#L1884).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.pullback`: [EdgeLocalization.lean:945](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L945).

`OAI.KLInvariance.MomentGraph.GradedSheaf.SymmetricPerfectPairing.coefficientChange`: [EdgeLocalization.lean:953](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/EdgeLocalization.lean#L953).
