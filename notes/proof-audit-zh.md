# 普通等参数 KL 组合不变性：证明审读

日期：2026-10-13。

## 1. 对象与结论

审读对象是 OpenAI 署名、日期为 2026-09-24 的《Combinatorial invariance of Kazhdan–Lusztig polynomials》。它断言：任意 Coxeter 系统中的抽象 Bruhat 区间同构

\[
\iota:[u,b]\simeq [u',b']
\]

保持普通等参数多项式 \(P_{u,b}\)。范围包括无限和非晶体 Coxeter 系统，不包括把 KLV、抛物型或不等参数多项式直接替换进去。

当前判断：正文的关键证明链条是闭合的，未找到实质性缺口。尤其未发现“先假定部分核自由，再用它证明部分核自由”的循环，也未发现把余维一相等直接误当全局相等的错误。这个判断是对正文及其标准输入接口的审读，不是 Lean 等形式化认证；没有独立重证所有外部引用定理。

## 2. 原文与定位

仓库 `agoramachina/openai-math`，本次查看的 main 提交为
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。

文件前缀：
`preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/`。

| 文件 | blob SHA |
|---|---|
| 01-introduction.tex | a2fcd19ab52b0ad00bbb27351ff8471271cdae9e |
| 02-background.tex | 8fdf4e8c9dd32aad14c46d20e386bbc1d8cf45d5 |
| 03-dihedral.tex | 4276da937b44f07fc5fb42dbc6f863374ee44456 |
| 04-localization.tex | 0adb21ab2f1045d414f47083269501d7e3f55135 |
| 05-comparison.tex | 9ff9e9e45c2d90571fc7cde60ae1f50c2a28c6e7 |

以下以 TeX label 定位重要引理，避免编号随编辑漂移。

## 3. 几何实现与分次

有限支撑归约把两个系统的简单生成元集合限制为有限集合，但不要求群有限。原文扩充 Tits 空间的退化方向，使环境对称型非退化，并保持根与余根独立；维数满足 Elias–Williamson 所使用的最小维数条件。

这一处理用于证明反射忠实性，以及证明两个不同反射的乘积满足

\[
\operatorname{im}(r_\alpha r_\beta-1)
 =\operatorname{span}(\alpha,\beta).
\]

环境型非退化不要求每个根平面上的限制非退化。不能在无限型中省略这个区别。

`bg:normalization` 的两个端点是

\[
\operatorname{grk}_A B^x=P_{x,b}(q),\qquad
\operatorname{grk}_A L_x(U_x)=q^{d(x,b)}P_{x,b}(q^{-1}).
\]

其中根的次数为一，\(U_x\) 是全部向上边，\(L_x\) 是限制映射的共同核。原文先在根次数为二的约定下跟踪 Fiebig 与 Elias–Williamson 的字符、取逆指标和移位，再代入 \(q=z^2\)。这里不能把全 costalk 与只有向上条件的核混为一谈。

已对照 Fiebig《The combinatorics of Coxeter categories》命题 7.1(4)：stalk 的移位 \(k_i\) 与向上层的移位 \(2\ell(x)-k_i\) 对应，符合原文所用公式。Elias–Williamson 的实现假设与原文构造相容。

## 4. 二面体组合部分

`dih:plane` 区分反射子群陪集的相对 Bruhat 序与环境诱导序。相对可比较推出环境可比较；反向通常不作断言。原文使用的强结论是有向反射图的识别，而不是两种偏序相等。

`bg:graph` 从覆盖边出发，使用六顶点、四层 1|2|2|1 的闭包规则恢复所有反射边。两个不同反射的乘积决定根平面，保证该规则不会产生假边；非覆盖边的三边细化与长度归纳给出反向包含。

`dih:transport` 的关键并不是任意二面体形状都自动保持。相对长度为二的端点之间恰有两条环境有向二边路径；同构保持全部反射图，因此目标相对长度也只能为二。由此逐层恢复相对覆盖和整个相对区间。这一步没有偷用根标签同构。

`dih:count` 证明：对于边 \(e:x\to y\)、相对顶点 \(c\ge_D y\)，在从另一系统搬运来的反射顺序下，较晚的向上边数满足

\[
h_x-h_y=k_D(e),\qquad
k_D(e)=\frac{\ell_D(y)-\ell_D(x)-1}{2}.
\]

`dih:sum` 用逆根集合之差，按包含 \(\alpha_e\) 的根平面分割其他正根，得到

\[
\sum_D k_D(e)=\frac{d(x,y)-1}{2}.
\]

这两个数值公式是局部消失阶与全局分次之间的桥梁。

独立有限检查使用原文整数模型，但独立枚举全部边、区间顶点及两个角序。对 I₂(m)、2≤m≤18，以及无限二面体绝对长度≤18，共检查 47,536 个实例，结果全部通过。此检查只检验计数公式，不检验一般根系、图重构或层论结论。

## 5. 根平面局部化

`loc:models` 先用二面体普通 KL 多项式均为一，识别秩一结构层模型。对有限二面体子群，可以使用标准实反射平面及固定多项式方向。

对无限二面体子群，诱导实现不一定是原始几何实现。原文没有直接滥用 Elias–Williamson 的几何假设，而是调用 Fiebig 的 universal Coxeter system 字符定理（定理 9.3），并检查反射忠实、一般轨道及简单次正则轨道的要求。这是一个需要保留的外部输入，不能只写“二面体显然成立”。

`loc:relative-flabbiness` 把环境 flabbiness 传给局部化后的相对上闭集：不在根平面的边模已为零；按环境逆序补顶点时，尚未加入的较高端点不可能通过保留边连接一个已规定的较低端点。这保证延拓兼容。

`loc:decomposition` 在二维局部环 \(R=A_{(\alpha,\beta)}\) 上构造的是实际层同构

\[
B_R|_K\simeq\bigoplus_{c\in K}\mathcal O_{c,R}^{\oplus m_c},
\]

包括两个端点的限制映射，而不只是 stalk 秩相同。

下降归纳中，每个已有模型的边界像为
\(R/(\prod\alpha_e)\)，由 \(R\) 给出极小自由覆盖。给定 stalk 到边界的满射提升到这些覆盖的直和；Nakayama 保证提升满射，随后分裂，剩余自由直和项成为以当前顶点为顶的新模型。此论证没有要求局部化保持不可分解性，也没有假定当前底部的部分核自由。

## 6. 余维一检测仅给包含

`edge:bound` 设置

\[
I=\operatorname{res}_{x,e}L_x(F),\quad
J=\operatorname{res}_{y,e}L_y(G),\quad C=A/(\alpha_e).
\]

假设仅是上端点 \(L_y(G)\) 自由。其他邻接标签不与 \(\alpha_e\) 成比例，故

\[
L_y(G)\cap\alpha_e B^y=\alpha_e L_y(G),\qquad
J\simeq L_y(G)/\alpha_e L_y(G).
\]

因此 \(J\) 是自由的 \(C\)-模，且具有满泛秩。对每个根平面局部化，在同一个边模分解下比较两个像，其消失阶差正是 \(k_D(e)\)。合并得

\[
I\subseteq f_eJ,\qquad
\deg f_e=(d(x,y)-1)/2.
\]

这里用的是自由目标 \(f_eJ\) 等于其所有高度一局部化的交。没有假设 \(I\) 自反；也没有从高度一处相等推出全局相等。高余维商 \((f_eJ)/I\) 此时确实仍可能存在。

## 7. 同时归纳与正矩阵

归纳命题同时包括多项式不变性和所有搬运终段核的自由性。在比较区间 \([u,b]\) 时，所有严格较高顶点已经由更短区间的归纳假设提供自由性；底部自由性暂不使用。

取 \(0<q<1\)，令

\[
p_x(q)=q^{-d(x,b)/2}P_{x,b}(q),\quad
T=q^{-1/2}-q^{1/2}>0.
\]

逐边取消约束，归一化 Hilbert 状态从 \(p(q^{-1})\) 变为 \(p(q)\)。上节包含给出每步

\[
D_{\rm after}\le (1+T E_{xy})D_{\rm before}.
\]

矩阵乘积枚举目标系统的递减反射路径，Dyer 路径公式把它识别为 \(\widetilde R'(T)\)。目标系统的互反关系为等式。较高顶点的多项式已经相同，因此在底部得到

\[
\Delta(q)\le\Delta(q^{-1}),\qquad \Delta=p_u-p'_u.
\]

交换两个系统给出反向不等式。严格次数界使 \(\Delta(q)\) 只含严格负的 \(q^{1/2}\) 次幂，而其倒数只含严格正次幂，故 \(\Delta=0\)。

端点相等后，逐步亏损向量满足

\[
0=\sum_k M_r\cdots M_{k+1}\delta_k,\qquad \delta_k\ge0.
\]

这些上三角矩阵非负且对角为一，正亏损不可能被后续矩阵消去。故各亏损为零。非零有限生成分次模的 Hilbert 级数在 \(0<q<1\) 为正，连有限长度的高余维商也不例外。因此确实得到 \(I=f_eJ\)，而非仅数值上的局部相等。

最后逆序加回底部约束。每次像自由于 \(A/(\alpha_e)\)，其 \(A\)-投射维数至多一。Schanuel 引理给出新核分次投射，再由分次 Nakayama 得到分次自由。至此才完成底部自由性，归纳闭合。

## 8. 判断的边界

对证明正确性的积极判断基于上述具体逻辑检查，而不是小规模 P 表一致或作者署名。尚未做独立 BMP 层计算或形式化验证。引用文献中字符定理、BMP–Soergel 对应等大定理作为已知输入使用；已检查其相关假设与所需结论，而非重证整篇文献。

KLV 推广不能只更换多项式名称。本文后半部分的正比较机制可抽象化，但秩二模型、边模描述、消失阶公式和正路径因子分解是新的实质性任务，见相邻工作笔记。

## 参考文献

- [审读原文](https://github.com/agoramachina/openai-math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026)。
- P. Fiebig, *The combinatorics of Coxeter categories*, [arXiv:math/0512176v3](https://arxiv.org/abs/math/0512176v3)，特别是定理 6.3、推论 6.5、命题 7.1、定理 9.3。
- B. Elias and G. Williamson, *The Hodge theory of Soergel bimodules*, [arXiv:1212.0791v2](https://arxiv.org/abs/1212.0791v2)，特别是定理 1.1 与第 3 节。
- M. Dyer, *Rank two detection of singularities of Schubert varieties*, [作者手稿](https://academicweb.nd.edu/~dyer/papers/ranktwo.pdf)。原文已重证本次比较所需的计数和局部化结论。
