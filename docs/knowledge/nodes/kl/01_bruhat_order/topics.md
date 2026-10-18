# 1. Coxeter systems and Bruhat order

The question in this chapter is: **what does an unlabelled Bruhat interval actually remember?** The final theorem compares intervals in different Coxeter groups, so we first need to distinguish the group-theoretic information used to construct an interval from the order that remains after its labels are forgotten.

We use the definition of a Coxeter system \((W,S)\). Here \(W\) is the group, \(S\) is its set of simple reflections, and \(1\) is its identity. A word is a finite product of elements of \(S\). The length \(\ell(w)\) is the least number of letters in a word representing \(w\); a word attaining that minimum is reduced.

## 1. From reflections to an order

A reflection is a conjugate \(r=wsw^{-1}\) of a simple reflection. Thus every simple reflection is a reflection, but there are usually more reflections than simple generators.

For a reflection \(r\), draw an upward reflection edge
\[
x\longrightarrow rx\quad\text{when}\quad\ell(x)<\ell(rx).
\]
Then declare \(x\le y\) if either \(x=y\) or a chain of upward reflection edges runs from \(x\) to \(y\). This is strong Bruhat order. The edge relation is the local input, and the order is its reflexive transitive closure.

For comparable endpoints, the interval is
\[
[u,b]=\{x\in W:u\le x\le b\}.
\]
An unlabelled interval retains this set with its order. An order isomorphism is a bijection \(\phi\) satisfying \(x\le y\) if and only if \(\phi(x)\le\phi(y)\). It is not supplied with a correspondence between simple generators or root labels.

A cover \(x\lessdot y\) means \(x<y\) with no intermediate element. Drawing just covers gives the Hasse diagram. A reflection edge need not be a cover; this distinction will matter when the proof reconstructs edges from the order.

## 2. Two examples that distinguish the data

The smallest nontrivial Coxeter group is \(W=\{1,s\}\), with \(s^2=1\). Its lengths are zero and one. The interval \([1,s]\) is therefore just
\[
1\longrightarrow s.
\]
After forgetting the labels, we see a two-element chain. Chapter 2 will calculate its polynomial, and chapters 4 and 8 will place modules on this same graph.

For a second example, take the type-\(A_2\) group with simple generators \(s,t\), satisfying \(sts=tst\). Its elements by length are:

| Length | Elements |
|---|---|
| 0 | \(1\) |
| 1 | \(s,t\) |
| 2 | \(st,ts\) |
| 3 | \(w_0=sts=tst\) |

Each length-one element lies below both length-two elements, which lie below \(w_0\). Also \(w_0=sts^{-1}\) is a reflection, so \(1\to w_0\) is a reflection edge. It jumps three length levels and is absent from the Hasse diagram. Chapter 6 must recover such an edge from the order alone.

These are explicit examples of the definitions. They do not establish the general edge-reconstruction theorem.

## 3. What strong exchange supplies

Choose a reduced word \(b=s_1\cdots s_m\). Suppose a reflection \(r\) shortens \(b\): \(\ell(rb)<\ell(b)\). Strong exchange says that \(rb\) is represented by deleting one of the letters:
\[
rb=s_1\cdots\widehat{s_j}\cdots s_m.
\]
The hat means that the indicated letter is omitted.

This is a bridge between a statement about group multiplication and a concrete operation on a word. Applied repeatedly along descending Bruhat steps, it gives the forward subword criterion: if \(x\le b\), some subword of this fixed reduced word represents \(x\). The converse, established using the lifting argument, says that subwords also produce elements below \(b\).

For the word \(st\) in the example, its subwords give \(1,s,t,st\). This explains the four-element interval \([1,st]\) without listing reflection chains individually.

For the full proofs, read [[node:kl.detail.strong_exchange]] followed by [[node:kl.foundations.subword]].

## 4. Why simple multiplication is replaced by envelopes

Left multiplication itself is not monotone: \(1<s\), but \(s1=s>1=ss\). Instead, fix a simple reflection \(s\) and define
\[
L_s(w)=\min\{w,sw\},\qquad U_s(w)=\max\{w,sw\}
\]
in Bruhat order. The two elements are comparable because multiplication by a simple reflection changes length by exactly one.

The nontrivial theorem is that these two maps are monotone. One first applies exchange to show that multiplying an upward reflection edge on the left by \(s\) preserves its orientation unless that edge itself is labelled by \(s\). Checking the two possible length changes at each endpoint then proves monotonicity on edges, and composition proves it on chains.

Here is the lifting consequence with every substitution visible. If
\[
x\le y,\qquad x<sx,\qquad sy<y,
\]
then
\[
L_s(x)=x,\quad L_s(y)=sy,\quad U_s(x)=sx,\quad U_s(y)=y.
\]
Monotonicity therefore gives \(x\le sy\) and \(sx\le y\). The general proof is [[node:kl.detail.bruhat_lifting]]. This result also controls the upper sets used in the later induction on tensor words.

## 5. Why the later constructions are finite

The fixed reduced word for \(b\) has \(m\) positions, hence only \(2^m\) choices of positions to retain. Every element below \(b\) is represented by one of those choices. Different choices may represent the same element, but that can only reduce the number of elements. Thus the lower ideal \([1,b]\), and every interval inside it, is finite.

The same argument gives more than cardinality. Every such subword uses only the finite set of generators occurring in the chosen word for \(b\). Thus an interval in a Coxeter system with infinitely many generators still lies inside a finite-generator standard parabolic subgroup. The subgroup itself may be infinite.

Finally, Bruhat intervals are ranked: saturated chains from \(x\) to \(y\) have \(\ell(y)-\ell(x)\) steps. An order isomorphism preserves covers and chains, so it preserves this rank difference. It need not preserve the separate absolute lengths of the endpoints.

## 6. What to carry into the next chapters

We now have finite sums over intervals, a size \(d(x,y)=\ell(y)-\ell(x)\) for induction, and a way to restrict an isomorphism to smaller intervals. Chapter 2 uses the finite sums to define reciprocal polynomial identities. Chapter 6 returns to the distinction between covers and all reflection edges. Chapter 9 uses finite generator support to transport the final theorem back to arbitrary Coxeter systems.

Before proceeding, check that you can explain why the edge \(1\to w_0\) in the \(A_2\) example is not a cover, and why finiteness of \([1,b]\) does not require finiteness of \(W\).

## Detailed statements and proofs

The calculations above explain the constructions and transitions. The entries below give the exact hypotheses and detailed proofs for the general results.

### Reflections, length, and intervals

1. [[node:kl.foundations.bruhat_step]]
2. [[node:kl.foundations.bruhat_order]]
3. [[node:kl.foundations.interval]]

### Exchange and finiteness

1. [[node:kl.detail.strong_exchange]]
2. [[node:kl.detail.simple_envelopes]]
3. [[node:kl.detail.bruhat_lifting]]
4. [[node:kl.foundations.subword]]
5. [[node:kl.foundations.finite_intervals]]
6. [[node:kl.foundations.rank_preservation]]
7. [[node:kl.foundations.finite_support]]

### Further connections

1. [[node:kl.main.finite_model_transport]]
