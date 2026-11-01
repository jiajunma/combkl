---
title: Geometric root orders and transported edge schedules
primary_topic: kl.reflection_combinatorics
---

For the finite-generator systems used in comparison, the geometric order compares positive roots by a separating linear functional divided by a positive height. Its restriction to a root plane has the convexity properties needed for dihedral arguments. Plane bases and inversion cuts connect this order with signs of roots under the group action.

[[node:kl.detail.diamond_reconstruction|Reflection-edge reconstruction]] makes an interval order isomorphism usable on the full directed reflection graph. Each source edge can then receive the geometric score of its target image root. Sorting these scores gives the transported schedule; reversing the list gives chronological order. The exact suffix theorem identifies the remaining endpoint conditions with strictly later scores.

The [[node:kl.notes.path_product|path-sum expansion]] first turns the transfer product into a sum of actual directed paths. The increasing Bruhat path polynomial makes that finite sum explicit for a ratio order. The source then proves the path identity for its geometric orders. Rank-two block comparisons and changes of the ordering functional are part of that proof. The resulting path matrix supplies the numerical operator used by the invariance comparison. The route below separates the geometric order, graph transport, schedule conventions and path application.

A chamber order connects geometry with the Hecke recursion. Its least simple descent admits an explicit ratio-order rotation. Rotating paths that avoid that label and splitting off a simple-edge prefix give the [[node:kl.paths.path_polynomial_recursion|path-polynomial recursion]]. Strong induction then yields the [[node:kl.paths.adapted_path_identification|adapted path identification]], which is the input for comparing with the fixed geometric order.

## Reading sequence

1. [[node:kl.order.root_slopes]] — Define the geometric score.
2. [[node:kl.order.slope_cone]] — Relate slope order to positive combinations.
3. [[node:kl.detail.geometric_functional]] — Construct a separating functional.
4. [[node:kl.notes.reflection_order]] — Define ratio orders, adapted signs and chamber conditions.
5. [[node:kl.order.chamber_existence]] — Choose a generic numerator in the required chamber.
6. [[node:kl.order.rotated_ratio_order]] — Define the two turned functionals and calculate their slopes.
7. [[node:kl.detail.diamond_reconstruction]] — Recover reflection edges.
8. [[node:kl.detail.transported_schedule]] — Define the two schedule directions.
9. [[node:kl.paths.schedule_suffixes]] — Identify strict later conditions.
10. [[node:kl.paths.directed_paths]] — Define directed edge lists and their selected path sets.
11. [[node:kl.notes.path_product]] — Expand the transfer entry into weighted paths.
12. [[node:kl.paths.bruhat_path_polynomial]] — Construct the actual increasing path polynomial.
13. [[node:kl.order.rotation_exists]] — Move a least simple root to greatest position at a shorter top.
14. [[node:kl.paths.path_polynomial_recursion]] — Derive the recursion from the two path bijections.
15. [[node:kl.paths.adapted_path_identification]] — Identify the adapted path polynomial with the Hecke R-family.
16. [[node:kl.dihedral.plane_path_reversal]] — Prove the full intrinsic plane-block identity.
17. [[node:kl.paths.dyer_paths]] — Connect the order to the normalized R-path identity.
