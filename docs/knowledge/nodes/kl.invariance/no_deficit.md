---
id: kl.comparison.no_deficit
title: Endpoint equality forces equality at every transfer step
kind: theorem
status: proved
primary_topic: kl.invariance
topics:
- kl.invariance
uses:
- kl.comparison.positive_transfer
- kl.detail.transfer_properties
- kl.detail.schedule_comparison
- kl.comparison.edge_increment
- kl.detail.schedule_state
lean:
  repository: openai-kl
  modules:
  - Comparison
  - PositiveTransfer
  declarations:
  - OAI.KLInvariance.Comparison.idealState
  - OAI.KLInvariance.Comparison.state_le_ideal
  - OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
  - OAI.KLInvariance.SchedulePaths.remaining_steps_eq
  - OAI.KLInvariance.BruhatGraph.edgeImages_eq_of_scheduleState_eq
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:98
    format: lean-location
    note: OAI.KLInvariance.Comparison.idealState
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:105
    format: lean-location
    note: OAI.KLInvariance.Comparison.state_le_ideal
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Comparison:119
    format: lean-location
    note: OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:880
    format: lean-location
    note: OAI.KLInvariance.SchedulePaths.remaining_steps_eq
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.PositiveTransfer:1161
    format: lean-location
    note: OAI.KLInvariance.BruhatGraph.edgeImages_eq_of_scheduleState_eq
  - artifact: openai-kl-paper
    locator: 6. Reciprocity and simultaneous induction; sec:induction
    format: section
    note: Paper correspondence; chapter organization follows mathematical dependencies
      in the Lean library.
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the state, list order, suffix hypotheses, parameter range and exact
    source conclusion stated explicitly?
  verdict: Read both Comparison finite-index and SchedulePaths remaining-list proofs.
    Followed the actual head/tail sandwich, tail-product injectivity, recovered shorter
    endpoint, suffix split and normalized source-coordinate image criterion; preserved
    all conditional hypotheses.
tags:
- Kazhdan-Lusztig
- induction
---

# Endpoint equality forces equality at every transfer step

Let \(V,E\) be sets with source and target maps \(s,r:E\to V\), let \(T\ge0\), and let \(D\) assign a real vector \(D_q:V\to\mathbb R\) to each finite edge list \(q\). Fix a finite list \(p\).
Assume:

1. Every edge in \(p\) has distinct endpoints.
2. For every suffix \(e::q\preceq_{\mathrm{suf}}p\),
\[
D_q\le U_e(T)D_{e::q}.
\tag{1}
\]
3. The final state equals the exact transfer product:
\[
D_{[]}
=\mathcal D_{p^{\mathrm{rev}}}(T)D_p.
\tag{2}
\]

Then every inequality (1) is an equality. This is `SchedulePaths.remaining_steps_eq`.

For the Hilbert states of a boundary sheaf on a finite-generator Coxeter interval with a finite real coefficient basis, assume \(0<t<1\), \(T=t^{-1}-t\), and the embedded image inclusion at every suffix as in the [[node:kl.detail.schedule_comparison|full transfer inequality]]. If (2) holds, then for every such suffix
\[
\rho_e^-\bigl(K_{s(e)}(F_q(s(e)))\bigr)
=\mu_e\rho_e^+\bigl(K_{r(e)}(F_q(r(e)))\bigr)
\tag{3}
\]
inside the actual edge module. Here \(\mu_e\) is the edge-factor multiplication map. This is `edgeImages_eq_of_scheduleState_eq`.

<!-- source-comparison:start -->
## Relation to the OpenAI notes

**Cancellation through the remaining transfer product.**

**OpenAI notes:** Exact endpoint comparison forces the positive Hilbert defects to vanish and hence makes the embedded lower and corrected upper images equal. [eq:step](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L275), [eq:comparison](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L298), [eq:image-equality](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/05-comparison.tex#L370).

**Lean (primary):** The finite-index statement removes the last transfer. The actual sheaf application uses a remaining-list statement: sandwich the tail-product values between equal endpoints, use injectivity of the tail product to recover exactness of the head removal, and recurse on the tail. Source-coordinate equality then invokes the normalized edge-increment equality criterion. [Comparison:105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L105), [Comparison:119](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L119), [PositiveTransfer:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L880), [PositiveTransfer:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1161).

**Role in the proof:** Both induction interfaces are explained. The actual embedded-image conclusion retains every suffix inclusion and the positive comparison-parameter hypotheses.
<!-- source-comparison:end -->

*Proof.*

### Step 1. Induction on the remaining list

We prove the first statement for every finite \(p\), carrying all three assumptions. When \(p=[]\), no nonempty list \(e::q\) is a suffix: its positive length would have to be at most zero. Thus there are no step equalities to prove.

Now write \(p=e::h\). Every suffix of \(h\) is also a suffix of \(e::h\), so the hypotheses (1) restrict to all steps of \(h\). Put
\[
A=\mathcal D_{h^{\mathrm{rev}}}(T),\qquad
v=D_h,\qquad w=U_e(T)D_{e::h}.
\]
The current one-step inequality is \(v\le w\).

### Step 2. The tail-product values between equal endpoints

Apply the generic [[node:kl.detail.schedule_comparison|full transfer inequality]] to the shorter list \(h\). It gives
\[
D_{[]}\le A v.
\tag{4}
\]
The [[node:kl.detail.transfer_properties|transfer properties]] give monotonicity of \(A\), so \(v\le w\) implies
\[
A v\le A w.
\tag{5}
\]
The reversed-list identity
\((e::h)^{\mathrm{rev}}=h^{\mathrm{rev}}+\!\!+[e]\)
and the concatenation formula turn the endpoint equality (2) into
\[
D_{[]}=A w.
\tag{6}
\]
Combine (4)–(6):
\[
D_{[]}\le A v\le A w=D_{[]}.
\]
In each coordinate, the intermediate real number is bounded above and below by the same real number. Consequently
\[
A v=A w,\qquad D_{[]}=A v.
\tag{7}
\]

### Step 3. Cancellation of the tail product

Every edge of \(h^{\mathrm{rev}}\) belongs to \(p\), so it has distinct endpoints. The [[node:kl.detail.transfer_properties|transfer properties]] make \(A\) injective. Apply injectivity to \(A v=A w\) in (7):
\[
D_h=v=w=U_e(T)D_{e::h}.
\tag{8}
\]
This is the exactness of the head removal. The second equality in (7) supplies the endpoint equality for the shorter list:
\[
D_{[]}=\mathcal D_{h^{\mathrm{rev}}}(T)D_h.
\tag{9}
\]

### Step 4. Exactness at later suffixes

The distinct-endpoint condition and all one-step inequalities restrict to \(h\); (9) is its required endpoint equality. Therefore the induction hypothesis proves every step indexed by a suffix of \(h\) exact.

A nonempty suffix of \(e::h\) is either the entire list \(e::h\), handled by (8), or a suffix of \(h\), handled by this induction hypothesis. These two cases cover all required steps and complete the proof of the first statement.

### Step 5. The source-coordinate equality

For a sheaf, the hypotheses of the [[node:kl.detail.schedule_comparison|full transfer inequality]] provide (1). Bruhat edges have distinct endpoints because they are strictly increasing. The assumed endpoint identity is (2), so the first statement gives
\[
D_q(t)=U_e(T)D_{e::q}(t).
\]
At \(x=s(e)\), set \(y=r(e)\), \(F=F_q(x)\), \(H=F_q(y)\). The [[node:kl.detail.schedule_state|remaining-condition identities]] identify the source selection before removal as \(F\cup\{e\}\), and leave the target selection \(H\) unchanged. Evaluating the vector equality at \(x\) therefore gives
\[
D_x(t,F)=D_x(t,F\cup\{e\})+T D_y(t,H).
\tag{10}
\]

### Step 6. Equality of the actual edge images

The [[node:kl.comparison.edge_increment|one-edge Hilbert comparison]] proves that (10), under the given inclusion
\(I_e(q)\subseteq\mu_eJ_e(q)\) and \(0<t<1\), is equivalent to equality of the actual images.
Its positive state scale allows cancellation to obtain equality of the raw Hilbert values. Degree by degree, the inclusion gives a nonnegative dimension difference; every weight \((t^2)^n\) is positive. A zero total difference therefore forces equal homogeneous pieces, and hence equal embedded submodules. This yields (3).

### Step 7. The natural-number-indexed formulation

The source also states the transfer result for states \(D_0,\ldots,D_n\) and an edge sequence \(e_0,\ldots,e_{n-1}\). Define ideal states
\[
E_0=D_0,\qquad E_{j+1}=U_{e_j}(T)E_j.
\]
From \(D_{j+1}\le U_{e_j}(T)D_j\), induction gives \(D_j\le E_j\): it starts with equality at zero, and the induction step applies monotonicity to \(D_j\le E_j\), followed by the given one-step bound.

If \(D_n=E_n\) and \(n>0\), these bounds give
\[
D_n\le U_{e_{n-1}}D_{n-1}
\le U_{e_{n-1}}E_{n-1}=E_n=D_n.
\]
Coordinatewise antisymmetry makes both inequalities equalities. Injectivity of \(U_{e_{n-1}}\) then gives \(D_{n-1}=E_{n-1}\). Induction on \(n\) proves exactness of all earlier steps, with no steps in the base case \(n=0\). This is `Comparison.every_step_eq_of_endpoint_eq`; the remaining-list proof above is the form invoked by the actual sheaf theorem.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Comparison.idealState`: [Comparison.lean:98](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L98).

`OAI.KLInvariance.Comparison.state_le_ideal`: [Comparison.lean:105](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L105).

`OAI.KLInvariance.Comparison.every_step_eq_of_endpoint_eq`: [Comparison.lean:119](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Comparison.lean#L119).

`OAI.KLInvariance.SchedulePaths.remaining_steps_eq`: [PositiveTransfer.lean:880](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L880).

`OAI.KLInvariance.BruhatGraph.edgeImages_eq_of_scheduleState_eq`: [PositiveTransfer.lean:1161](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/PositiveTransfer.lean#L1161).
