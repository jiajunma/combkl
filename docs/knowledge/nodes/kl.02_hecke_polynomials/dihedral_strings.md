---
id: kl.hecke.dihedral_strings
title: Single and double membership of simple-reflection strings
kind: theorem
status: proved
primary_topic: kl.02_hecke_polynomials
topics:
- kl.02_hecke_polynomials
uses:
- kl.coxeter.dihedral_bruhat_order
- kl.coxeter.dihedral_reduced_words
- kl.detail.bruhat_lifting
- kl.hecke.lower_interval_sums
lean:
  repository: openai-kl
  modules:
  - Dihedral
  declarations:
  - OAI.KLInvariance.Dihedral.union_string
  - OAI.KLInvariance.Dihedral.double_string
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:303
    format: lean-location
    note: OAI.KLInvariance.Dihedral.union_string
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.Dihedral:217
    format: lean-location
    note: OAI.KLInvariance.Dihedral.double_string
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Does the exposition preserve the reduced-word, coefficient and interval
    hypotheses?
  verdict: Read union_string and double_string. Expanded both envelope implications,
    strict exclusion of the tail top, the n=0 obstruction, both length cases at the
    prefix and the prescribed-descent expression.
tags:
- Kazhdan-Lusztig
- dihedral
---

# Single and double membership of simple-reflection strings

Let \(\omega_i(n+2)\) be reduced, put \(s=s_i\), and write
\[
w=\operatorname{prod}\omega_i(n+2),\quad
v=\operatorname{prod}\omega_{\bar i}(n+1),\quad
p=\operatorname{prod}\omega_i(n).
\]
Thus \(w=sv\), with lengths \(n+2,n+1,n\). For every \(x\),
\[
x\le w\quad\Longleftrightarrow\quad x\le v\ \text{or}\ sx\le v,
\]
and
\[
(x\le v\ \text{and}\ sx\le v)
\quad\Longleftrightarrow\quad n>0\ \text{and}\ x\le p.
\]

The first identity describes the union of simple-reflection strings meeting \([1,v]\). The second describes those strings whose two members both belong to \([1,v]\).

*Proof.*

### Step 1. Prove the union identity

Suppose \(x\le w=sv\). The lower simple envelope is monotone, and the lower member of \(\{w,sw\}\) is \(v\). Hence
\[
\min\{x,sx\}\le v.
\]
Its value is either \(x\) or \(sx\), giving one of the two alternatives.

Conversely, if \(x\le v\), then \(x\le v<w\). If \(sx\le v\), monotonicity of the upper simple envelope gives
\[
x\le\max\{x,sx\}
=\max\{sx,s(sx)\}
\le\max\{v,sv\}=w.
\]
This proves both directions.

### Step 2. Bound the two lengths under double membership

Suppose \(x\le v\) and \(sx\le v\). Neither element can equal \(v\).

If \(x=v\), then \(sx=w\), whose length is \(n+2>\ell(v)\), contradicting \(sx\le v\). If \(sx=v\), then \(x=sv=w\), contradicting \(x\le v\).

The [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat criterion]] therefore gives
\[
\ell(x)<n+1,\qquad \ell(sx)<n+1.
\]
Both lengths are at most \(n\). Since they differ by one, \(n\) must be positive.

### Step 3. Identify the lower prefix in the forward direction

If \(\ell(x)<n=\ell(p)\), the [[node:kl.coxeter.dihedral_bruhat_order|dihedral Bruhat criterion]] gives \(x\le p\).

Otherwise the bound in Step 2 forces \(\ell(x)=n\). Since \(\ell(sx)\le n\) and simple multiplication changes length by one, we have \(\ell(sx)=n-1\). Thus \(s\) is a left descent of \(x\).

The [[node:kl.coxeter.dihedral_reduced_words|prescribed-first-letter theorem]] now gives
\[
x=\operatorname{prod}\omega_i(\ell(x))
=\operatorname{prod}\omega_i(n)=p.
\]
This proves \(n>0\) and \(x\le p\).

### Step 4. Prove the converse below the prefix top

Assume \(n>0\) and \(x\le p\). Then \(\ell(x)\le n<n+1=\ell(v)\), so \(x\le v\).

If \(\ell(x)<n\), simple multiplication gives
\[
\ell(sx)\le\ell(x)+1\le n<n+1=\ell(v).
\]
The dihedral criterion gives \(sx\le v\).

### Step 5. Prove the converse at the prefix top

The remaining case is \(\ell(x)=n\). Since \(x\le p\) and \(\ell(p)=n\), the dihedral criterion forces \(x=p\).

The reduced prefix \(p\) begins with \(s\), because \(n>0\). Multiplication by \(s\) removes that first letter, leaving a reduced word of length \(n-1\). Thus
\(\ell(sx)=n-1<n+1=\ell(v)\),
so \(sx\le v\) as well. This completes the double-membership equivalence.

### Step 6. Read the first two cases

For \(w=st\), we have \(n=0\), so no string has both members below \(v=t\).

For a reduced \(w=sts\), we have \(n=1\), \(v=ts\), and \(p=s\). The doubly included elements are exactly \([1,s]=\{1,s\}\).

The proof uses the reducedness of the chosen word and its prefixes and tail. It also applies when that word represents the longest element of a finite dihedral group.

## References

The local source declarations below give the construction and proof.

## Lean formalization

`OAI.KLInvariance.Dihedral.union_string`: [Dihedral.lean:303](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L303).

`OAI.KLInvariance.Dihedral.double_string`: [Dihedral.lean:217](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Dihedral.lean#L217).
