# Coxeter combinatorics

This topic constructs Bruhat intervals from Coxeter words and reflections, then develops their order, subintervals and rank. These supply the finite index sets and smaller induction instances used throughout the proof. The final theorem compares the resulting interval orders across different Coxeter systems.

We use the definition of a Coxeter system \((W,S)\). Here \(W\) is the group, \(S\) is its set of simple reflections, and \(1\) is its identity. A word is a finite product of elements of \(S\). The length \(\ell(w)\) is the least number of letters in a word representing \(w\); a word attaining that minimum is reduced.

## Words, inversion sequences, and signed permutations

A word gives a product in the group and a reflection attached to each position. Multiplying its product by that reflection deletes the corresponding letter. The signed word action records the parity of the occurrences of each reflection in this list.

The doubled inversion list of a Coxeter relation makes its sign contribution zero. Consequently the signed word action descends to the group. A reflection then toggles its own label, and this sign change forces every left inversion to occur in the inversion sequence of a reduced word. The deletion identity becomes strong exchange.

## From reflections to an order

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

## Two examples that distinguish the data

The smallest nontrivial Coxeter group is \(W=\{1,s\}\), with \(s^2=1\). Its lengths are zero and one. The interval \([1,s]\) is therefore just
\[
1\longrightarrow s.
\]
After forgetting the labels, we see a two-element chain. Hecke algebra and polynomial invariants will calculate its polynomial, and the sheaf and Hilbert-comparison topics use modules on this same graph.

For a second example, take the type-\(A_2\) group with simple generators \(s,t\), satisfying \(sts=tst\). Its elements by length are:

| Length | Elements |
|---|---|
| 0 | \(1\) |
| 1 | \(s,t\) |
| 2 | \(st,ts\) |
| 3 | \(w_0=sts=tst\) |

Each length-one element lies below both length-two elements, which lie below \(w_0\). Also \(w_0=sts^{-1}\) is a reflection, so \(1\to w_0\) is a reflection edge. It jumps three length levels and is absent from the Hasse diagram. reflection orders and paths must recover such an edge from the order alone.

These examples display the distinction between cover edges and reflection edges. The edge-reconstruction theorem explains how to recover the latter from the order in general.

## Strong exchange and deletion

Choose a reduced word \(b=s_1\cdots s_m\). Suppose a reflection \(r\) shortens \(b\): \(\ell(rb)<\ell(b)\). Strong exchange says that \(rb\) is represented by deleting one of the letters:
\[
rb=s_1\cdots\widehat{s_j}\cdots s_m.
\]
The hat means that the indicated letter is omitted.

This is a bridge between a statement about group multiplication and a concrete operation on a word. Applied repeatedly along descending Bruhat steps, it gives the forward subword criterion: if \(x\le b\), some subword of this fixed reduced word represents \(x\). The converse, established using the lifting argument, says that subwords also produce elements below \(b\).

For the word \(st\) in the example, its subwords give \(1,s,t,st\). This explains the four-element interval \([1,st]\) without listing reflection chains individually.

For the full proofs, read [[node:kl.detail.strong_exchange]] followed by [[node:kl.foundations.subword]].

## Monotone simple envelopes

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

## Finite intervals and finite generator support

The fixed reduced word for \(b\) has \(m\) positions, hence only \(2^m\) choices of positions to retain. Every element below \(b\) is represented by one of those choices. Different choices may represent the same element, but that can only reduce the number of elements. Thus the lower ideal \([1,b]\), and every interval inside it, is finite.

The same argument gives more than cardinality. Every such subword uses only the finite set of generators occurring in the chosen word for \(b\). Thus an interval in a Coxeter system with infinitely many generators still lies inside a finite-generator standard parabolic subgroup. The subgroup itself may be infinite.

## Successors and relative rank

Every strict interval \(x<y\) contains \(z\) with \(x<z\le y\) and \(\ell(z)=\ell(x)+1\). The source proves this by induction on the top length. For a descent \(sy<y\), either \(x\le sy\), giving a smaller instance directly, or lifting forces \(s\) to lower \(x\) as well. In that second case, induction between \(sx\) and \(sy\), followed by the upper simple envelope, produces the required successor.

This [[node:kl.coxeter.bruhat_successor|one-step result]] gives the [[node:kl.coxeter.rank_embedding|rank inequality]] for a strictly monotone interval map \(f\). Take a successor \(z\) of \(x\). The remaining pair has rank \(d(x,y)-1\); induction bounds its image rank from below, while \(f(x)<f(z)\) contributes at least one additional length unit. Hence
\[
d(x,y)\le d'(f(x),f(y)).
\]
Applying this to an order isomorphism and its inverse proves [[node:kl.foundations.rank_preservation|equality of every relative rank]].

## Restriction and smaller induction instances

An order isomorphism \(\phi:[u,b]\to[u',b']\) sends bottom to bottom and top to top: each image is bounded in both directions by the corresponding extremal element. For \(u\le x\le y\le b\), it restricts to
\[
[x,y]\xrightarrow{\sim}[\phi(x),\phi(y)]
\]
by the same underlying map. Monotonicity of \(\phi\) and \(\phi^{-1}\) verifies the two endpoint inequalities.

The source-rank decomposition is
\[
d(u,b)=d(u,x)+d(x,y)+d(y,b).
\]
If \(x\ne u\) or \(y\ne b\), at least one outer difference is positive, so the subinterval has strictly smaller rank. Rank preservation gives that same smaller rank in the target. These are the arithmetic and mapping facts used when applying induction to a proper upper or initial interval.

An interval-indexed function transports by \(f'(z')=f(\phi^{-1}(z'))\). Thus a pair of functions on isomorphic intervals can be compared after indexing both on the source interval.

## Parity pairs and external lower vertices

For \(c\ne1\), choose a simple left descent \(s\) of \(c\). The upper-envelope calculation
\[
sz\le U_s(sz)=U_s(z)\le U_s(c)=c\qquad(z\le c)
\]
keeps left multiplication by \(s\) inside \([1,c]\). It is an involution and changes length by one, so it pairs the two length parities.

For \(x\le c\), define the external lower set
\[
E(x,c)=[1,c]\setminus[1,x].
\]
Split it into \(Y\), opposite in parity to \(x\), and \(Z\), of the same parity. When both \(x,c\) are nonidentity, removing one balanced lower interval from another gives \(|Y|=|Z|\). For \(x=1<c\), removal deletes one even vertex, so \(|Y|=|Z|+1\). For \(x=c=1\), both are empty.

Thus \(|Z|\le|Y|\) in every case. The [[node:kl.coxeter.lower_interval_parity|lower-interval parity theorem]] proves these statements and supplies an injection \(Z\hookrightarrow Y\). In the dihedral interpolation argument, each opposite-parity vertex supplies one orbit-spline factor, and the injection assigns at most one extra zero to that factor.

## The alternating rank-two order

With two simple generators, reducedness forces the letters to alternate. For a shorter reduced expression, matching the first letter realizes it as a prefix of a longer reduced word; the other first letter realizes it as a prefix of the longer word's tail. Thus every strictly shorter element lies below every longer element.

Consequently the lower ideal of \(w\) contains all lower length levels and only \(w\) at its own level. In the \(A_2\) example, this gives the two elements at levels one and two and the single longest top. This order description is the input to the [[node:kl.hecke.dihedral_sum_product|dihedral Hecke-sum calculation]].

The root calculations use alternating words with a specified final generator. The dihedral polynomial calculation uses a specified first generator. The [[node:kl.coxeter.alternating_words|alternating-word definition]] gives the parity conversion between these two list conventions.

## Inputs for the geometric and algebraic constructions

We now have finite sums over intervals, a size \(d(x,y)=\ell(y)-\ell(x)\) for induction, and a way to restrict an isomorphism to smaller intervals. Hecke algebra and polynomial invariants uses the finite sums to define reciprocal polynomial identities. reflection orders and paths returns to the distinction between covers and all reflection edges. the simultaneous invariance induction uses finite generator support to transport the final theorem back to arbitrary Coxeter systems.

The order and rank lemmas provide the common combinatorial data for the realization, Hecke and sheaf branches.


## Definitions and proofs by construction

### Strong Bruhat order and lifting

- [[node:kl.detail.strong_exchange]]
- [[node:kl.foundations.subword]]
- [[node:kl.detail.bruhat_lifting]]
- [[node:kl.foundations.bruhat_order]]
- [[node:kl.foundations.bruhat_step]]
- [[node:kl.detail.simple_envelopes]]
- [[node:kl.foundations.finite_intervals]]
- [[node:kl.coxeter.dihedral_bruhat_order]]
- [[node:kl.coxeter.external_vertices]]
- [[node:kl.coxeter.lower_interval_parity]]

### Intervals, ranks, and order isomorphisms

- [[node:kl.foundations.rank_preservation]]
- [[node:kl.foundations.interval]]
- [[node:kl.coxeter.interval_restriction]]
- [[node:kl.coxeter.bruhat_successor]]
- [[node:kl.coxeter.rank_embedding]]

### Standard parabolics and finite support

- [[node:kl.foundations.finite_support]]
- [[node:kl.main.finite_interval_model]]
- [[node:kl.main.finite_model_transport]]

## The word and signed-action constructions

- [[node:kl.coxeter.word_data]]
- [[node:kl.coxeter.signed_word_action]]
- [[node:kl.coxeter.word_sign_record]]
- [[node:kl.coxeter.signed_coxeter_relations]]
- [[node:kl.coxeter.signed_reflection_action]]
- [[node:kl.coxeter.reflection_sign_flip]]

## Parabolic length decomposition and alternating tails

A subgroup generated by a selected set of simple generators has word expressions using that set. Deleting letters gives reduced expressions with the same property. Minimality in a coset then forces concatenation with a reduced subgroup word to retain every letter. This supplies the length-additive decomposition used in root positivity.

For a two-generator subgroup, a reduced word followed by a specified generator must alternate, and its length is bounded by the finite Coxeter exponent when that exponent exists. The bound places the coefficients in the nonnegative range of the rank-two root formula.

- [[node:kl.coxeter.word_reduction]]
- [[node:kl.coxeter.parabolic_subgroups]]
- [[node:kl.coxeter.parabolic_decomposition]]
- [[node:kl.coxeter.alternating_words]]
- [[node:kl.coxeter.reduced_alternating_tail]]
- [[node:kl.coxeter.simple_edge_transport]]
- [[node:kl.coxeter.dihedral_reduced_words]]
