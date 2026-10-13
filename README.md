# combkl — KL 证明审读与 KLV 推广

工作记录：2026-10-13。

本仓库审读 OpenAI 署名的《Combinatorial invariance of Kazhdan–Lusztig polynomials》（2026-09-24），并研究其方法在 Kazhdan–Lusztig–Vogan 多项式中的适用范围。

## 当前结论

对正文关键论证和外部定理接口的审读未发现实质性缺口；当前判断支持这份普通等参数 KL 证明成立。这不是形式化验证，也不声称独立重证了全部引用文献。

一般 KLV 推广尚未在此建立。应区分轨道偏序、包含局部系统的参数偏序，以及携带 Hecke 作用和 bar 数据的结构。原文的普通二面体局部模型和统一边权不能不加修改地用于 KLV。

- [证明审读](notes/proof-audit-zh.md)：关键依赖、局部化、余维一到全局的逻辑、同时归纳。
- [KLV 工作笔记](notes/klv-extension-zh.md)：局部系统例子、三点链上的正矩阵分解、条件比较命题和计算边界。
- [可复算代码](tests/check_models.py) 与 [运行结果](results/checks.json)。

## 已执行的有限检查

普通二面体“较晚边计数差”检查：有限 I₂(m)，2≤m≤18；无限二面体绝对长度≤18；两个角序共 47,536 个边—顶点—顺序实例，未失败。

| 对称对 | 参数数 | 全部区间（含单点） | 非常数 P 的区间 | 同构类数 | 同构区间不同 P |
|---|---:|---:|---:|---:|---:|
| SL₄ / Sp₄ | 3 | 6 | 0 | 3 | 0 |
| SL₆ / Sp₆ | 15 | 101 | 2 | 18 | 0 |
| SL₈ / Sp₈ | 105 | 3490 | 510 | 398 | 0 |

这里的 KLV 计算仅针对这些对称对的平凡等变局部系统，采用 Abdallah–Hultman 的 Q 递推和互反关系；每个群内分别做精确偏序同构比较，没有进行跨群同构比较。另检查了每个可用简单下降的递推一致性、完整多项式互反恒等式和系数非负性。

有限检查不验证 BMP 层的局部化分解，不证明普通 KL 主定理，也不证明一般 KLV 组合不变性。

## 复算

已测试环境：Python 3.13.5、NetworkX 3.6.1。

```bash
python -m pip install -r requirements.txt
python tests/check_models.py --max-even-degree 8 --output results/checks.json
```

不要使用 `python -O`；检查使用断言。多项式以从常数项开始的整数系数数组存储；例如 `[0,-1,1]` 表示 q²−q。

## 原文版本

[原文目录](https://github.com/agoramachina/openai-math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026)。审读对象为该目录的五份正文 TeX 与参考文献；对应 blob SHA 记录在证明审读中。
