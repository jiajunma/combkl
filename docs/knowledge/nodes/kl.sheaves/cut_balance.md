---
id: kl.sheaves.cut_balance
title: Support orthogonality makes integral cuts balanced
kind: theorem
status: proved
primary_topic: kl.sheaves
topics:
- kl.sheaves
uses:
- kl.sheaves.integral_cuts
- kl.notes.supported_pairings
lean:
  repository: openai-kl
  modules:
  - CharacterReciprocity
  declarations:
  - OAI.BalancedCuts.balanced_two
  - OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.cut_balanced
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:49
    format: lean-location
    note: OAI.BalancedCuts.balanced_two
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.CharacterReciprocity:76
    format: lean-location
    note: OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.cut_balanced
  - artifact: openai-kl-paper
    locator: Moment-graph background; bg:normalization
    format: section
    note: The source comparison locates the graded sheaf and support-duality context.
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

# Support orthogonality makes integral cuts balanced

Let \(R\) be a commutative domain, \(M,N\) be \(R\)-modules, and
\(b:M\times M\to R\) be a bilinear pairing. Let
\(\pi:M\to N\) and \(C:M\to M\) be linear maps. Suppose \(p\in R\) is nonzero and
\[
\pi(Cm)=p\,\pi(m)\qquad(m\in M).
\]
Assume the two orthogonality conditions
\[
\begin{aligned}
\pi(n)=0&\ \Longrightarrow\ b(Cm,n)=0,\\
\pi(m)=0&\ \Longrightarrow\ b(m,Cn)=0
\end{aligned}
\qquad(m,n\in M).
\]
Then \(C\) is balanced for the pairing:
\[
b(Cm,n)=b(m,Cn)\qquad(m,n\in M).
\]

For a graded sheaf over a domain, a perfect graded section pairing satisfies these hypotheses for each integral cut \(C_x\) defined by a nonzero common scalar. Consequently its cuts are balanced.

*Proof.*

### Step 1. Two vectors in the evaluation kernel

Linearity and the scaling hypothesis give
\[
\pi(pn-Cn)=p\pi(n)-\pi(Cn)=0.
\]
The same calculation with \(m\) gives \(\pi(pm-Cm)=0\).

### Step 2. Compare through the twice-cut value

Apply the first orthogonality condition to \(m\) and \(pn-Cn\). Expanding in the second argument yields
\[
0=b(Cm,pn-Cn)=p\,b(Cm,n)-b(Cm,Cn).
\]
Hence \(p\,b(Cm,n)=b(Cm,Cn)\).

Apply the second condition to \(pm-Cm\) and \(n\). Expanding in the first argument yields
\[
0=b(pm-Cm,Cn)=p\,b(m,Cn)-b(Cm,Cn).
\]
Thus \(p\,b(m,Cn)=b(Cm,Cn)\) as well.

### Step 3. Cancel the common scalar

The two equations imply
\[
p\bigl(b(Cm,n)-b(m,Cn)\bigr)=0.
\]
Since \(R\) is a domain and \(p\ne0\), the parenthesized scalar is zero. This is the required balance equation.

### Step 4. Apply the argument to a sheaf cut

Take \(M=\Gamma(B)\), \(N=B^x\), \(\pi=\pi_x\), and \(C=C_x\). By the cut definition, \(\pi_x(C_xm)=p\,m_x\), and \(C_xm\) is supported at \(x\).

If \(n_x=0\), left support orthogonality gives \(\langle C_xm,n\rangle=0\). If \(m_x=0\), right support orthogonality gives \(\langle m,C_xn\rangle=0\). All the hypotheses of Steps 1–3 therefore hold, proving balance for the section pairing.

## References

The source declarations below give the definitions and constructions used here.

## Lean formalization

`OAI.BalancedCuts.balanced_two`: [CharacterReciprocity.lean:49](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L49).

`OAI.KLInvariance.MomentGraph.GradedSheaf.PerfectPairing.cut_balanced`: [CharacterReciprocity.lean:76](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/CharacterReciprocity.lean#L76).
