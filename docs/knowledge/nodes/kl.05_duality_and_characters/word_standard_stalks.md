---
id: kl.detail.word_standard_stalks
title: Free word stalks and exact reflection-edge kernels
kind: theorem
status: proved
primary_topic: kl.05_duality_and_characters
topics:
- kl.05_duality_and_characters
uses:
- kl.notes.word_stalks
- kl.detail.word_sheaf
- kl.notes.reflection_frobenius
- kl.detail.bruhat_lifting
- kl.detail.root_reflection_correspondence
- kl.detail.linear_quotient
lean:
  repository: openai-kl
  modules:
  - BottSamelson
  declarations:
  - OAI.KLInvariance.TitsSpace.BottKernelExact
  - OAI.KLInvariance.TitsSpace.bottStandardStalks
  - OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead
  - OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel
source:
  spans:
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:964
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.BottKernelExact
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1510
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottStandardStalks
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1130
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead
  - artifact: openai-kl-source
    locator: OAI.RepresentationTheory.KazhdanLusztig.BottSamelson:1524
    format: lean-location
    note: OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel
verification:
  statement: accepted
  proof: accepted
  alignment: aligned
generality:
  reviewed: true
  prompt: Are the actual Lean hypotheses, objects, and proof route retained?
  verdict: Read against the fixed source declaration bodies and their surrounding
    assumptions; the supplied formal proof is unchanged.
tags:
- Kazhdan-Lusztig
---

# Free word stalks and exact reflection-edge kernels

For every tensor word \(\mathbf s\), each actual word stalk \(B^{\mathbf s}_x\) is finite free over the symmetric coefficient algebra \(A\). If \(x\to tx\) is an upward reflection edge with root label \(\beta\), then
\[
p_x(m)=0\quad\Longrightarrow\quad p_{tx}(m)\in\beta B^{\mathbf s}_{tx}.
\]
Consequently the upper edge map has kernel exactly \(\beta B^{\mathbf s}_{tx}\). This is a statement about the actual projection images, before taking ranks or characters.

*Proof.*

### Step 1. State the simultaneous induction

Induct on the word, proving both stalk freeness and the displayed divisibility. For the empty word, the only nonzero stalk is the coefficient algebra at \(1\). In an upward edge, the upper endpoint has positive length and hence has zero empty-word stalk. Both assertions follow.

Assume both assertions for a shorter word \(\mathbf t\), and prepend a simple reflection \(s\). Write \(\alpha\) for its root label and \(\tau\) for its action on \(A\). Then \(\tau^2=1\), \(\tau(\alpha)=-\alpha\), and \(\tau(a)-a\) is divisible by \(\alpha\) for every \(a\in A\).

### Step 2. Identify the new stalk with a two-stalk lattice

Put \(X=B^{\mathbf t}_x\), \(Y=B^{\mathbf t}_{sx}\), with projections \(f,g\) from the old word module. Let \(Y^\tau\) have action \(a\cdot y=\tau(a)y\). Consider
\[
L_x=\{(f(n),g(n)):n\in B_{\mathbf t}\}\subseteq X\oplus Y^\tau.
\]
To see scalar stability, the old pair-projection edge is killed by \(\alpha\). Indeed choose a coefficient whose right-action eigenvalues at \(x,sx\) differ by \(\alpha\); one choice is \(x^{-1}(\alpha/2)\). Right multiplication on the word module then gives the difference \(\alpha\) on the quotient relation. Therefore for every \(y\in Y\) there is an old word element with pair \((0,\alpha y)\).

If \(\tau(a)-a=\alpha c\), start with \(an\), whose old pair is \((af(n),ag(n))\), and add a lift of \((0,\alpha c g(n))\). The result is \((af(n),\tau(a)g(n))\), the required twisted scalar multiple.

Split the subexpressions of \(s\mathbf t\) by their first bit. A pair \((u,v)\in L_x\) has coordinates \(u\) on the zero-bit block and \(\tau(v)\) on the one-bit block. Both blocks are recoverable, so this map is injective. The old pair of \(n\) gives the new stalk projection of \(1\otimes n\); for a general pure tensor \(a\otimes n\), scalar stability gives its pair. Pure tensors span the new module, proving that this map has image exactly the new stalk. Thus \(L_x\simeq B^{s\mathbf t}_x\).

### Step 3. Prove freeness of the new stalk

If \(x<s x\), projection \(L_x\to X\) is surjective because \(f\) is. The old divisibility assertion, together with edge annihilation, identifies its kernel with
\(\{(0,\alpha y):y\in Y^\tau\}\).
Multiplication by \(\alpha\) is injective on \(Y\), since \(Y\) is a submodule of a product of copies of the domain \(A\). Hence this kernel is isomorphic to \(Y^\tau\), which is free by the induction hypothesis. The quotient \(X\) is free too, so choose lifts of its basis to split the surjection. The lattice is the direct sum of this kernel and \(X\), and is free.

If \(sx<x\), use projection to the second factor instead. Its kernel is \(\{(\alpha u,0):u\in X\}\), and its quotient is \(Y^\tau\). Both are free by the same arguments. Finiteness of all stalks follows from surjectivity of the projections from the finite word module.

### Step 4. Establish saturation away from the head root

The old simple-edge module is a free module over \(A/(\alpha)\): use the free upper stalk and the exact old edge kernel. If \(\alpha\nmid\beta\), multiplication by \(\beta\) is injective on this edge module. Here \((\alpha)\) is prime by the linear-quotient theorem, so the residue of \(\beta\) is nonzero in the domain \(A/(\alpha)\).

Suppose \(\beta(u,v)\in L_x\). Edge compatibility gives
\(\beta\rho_-(u)=\tau(\beta)\rho_+(v)\).
The difference \(\tau(\beta)-\beta\) is divisible by \(\alpha\), which kills the edge module. Thus
\(\beta(\rho_-(u)-\rho_+(v))=0\).
Injectivity of multiplication by \(\beta\) gives compatibility of \((u,v)\), hence membership in \(L_x\). This removes the factor inside the actual lattice, not merely inside an ambient free module.

### Step 5. Prove divisibility for a non-head reflection

Consider \(x\to tx\) with \(t\ne s\) and root label \(\beta\). Vanishing of the new stalk projection at \(x\) means both tail components vanish, at \(x\) and \(sx\). The edge-transport part of the Bruhat lifting theorem gives the upward edge \(sx\to s(tx)\), labelled by the conjugate reflection \(sts\).

Apply old-word divisibility to the two tail elements. At the upper endpoints their projections are \(\beta u\) and \(\tau(\beta)v\). In the twisted pair module, this is exactly \(\beta(u,v)\). Distinct reflections have independent representing roots, so their degree-one labels are nonassociate primes; in particular \(\alpha\nmid\beta\). Step 4 implies \((u,v)\in L_{tx}\). Transporting through Step 2 proves that the new projection at \(tx\) is \(\beta\) times an actual new stalk vector.

### Step 6. Handle the head reflection and finish

If \(t=s\), act by \(\tau\) on the first tensor factor. Call this map \(F\). The scalar identity \(a-\tau(a)\in\alpha A\) implies \(m-Fm=\alpha n\) for some word element \(n\). Flipping the first subexpression bit exchanges weights \(x,sx\), so \(p_x(m)=0\) implies \(p_{sx}(Fm)=0\). Projecting the displayed identity therefore gives \(p_{sx}(m)=\alpha p_{sx}(n)\). A different representing root of \(s\) is \(\alpha\) or \(-\alpha\); absorb the possible minus sign in \(n\).

This completes both induction assertions. For any reflection edge, its label annihilates the pair-projection edge by the same right-action difference argument used in Step 2, now with the reflection root. Thus \(\beta B_{tx}\) lies in the upper kernel. The opposite inclusion is exactly the proved divisibility, using the definition of the pair-projection relation. The upper kernel is therefore equal to \(\beta B_{tx}\).

## References

The precise Lean sources are listed below.

## Lean formalization

`OAI.KLInvariance.TitsSpace.BottKernelExact`: [BottSamelson.lean:964](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L964).

`OAI.KLInvariance.TitsSpace.bottStandardStalks`: [BottSamelson.lean:1510](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1510).

`OAI.KLInvariance.TitsSpace.bottKernelExact_cons_nonhead`: [BottSamelson.lean:1130](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1130).

`OAI.KLInvariance.TitsSpace.bottProjectionSheaf_upper_kernel`: [BottSamelson.lean:1524](https://github.com/jiajunma/combkl/blob/108243e05ed46235bf82dc30d4d90c794579776f/sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/BottSamelson.lean#L1524).
