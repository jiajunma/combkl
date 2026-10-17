# 5. Comparison of edge images

Fix an edge \(e:x\to y\) and retain the conditions that occur later in the transported schedule. Their images in the common edge module are \(I_e\) and \(J_e\).

## The free target

[[node:kl.notes.upper_image_free]] proves that upper-kernel freeness makes \(J_e\) free over the edge ring and gives it full generic span. [[node:kl.local.free_target_localization]] explains how membership in a free target is detected in height one.

The example \((s,t)\subset k[s,t]\) distinguishes a global inclusion from a global equality. It also explains why a quotient supported in higher codimension must be kept visible.

## The edge-image inclusion

[[node:kl.local.edge_inclusion]] combines the sheaf decomposition, later-edge counts, and degree identity to prove
\[
I_e\subseteq f_eJ_e.
\]
Only upper-endpoint kernel freeness is used at this point. The next chapter supplies it from shorter intervals and later proves that every one of these inclusions is exact.
