# combkl — KL 论文审稿

本仓库用于审读 OpenAI 署名的《Combinatorial invariance of Kazhdan–Lusztig polynomials》（2026-09-24），并保存相关研究记录。

## 文件入口

[AGENTS.md](AGENTS.md) 只包含通用审稿协作规则。具体论文背景、证明核查、疑问、评论、评价与交流记录统一放在 LaTeX 工作稿中，不另维护 Markdown 意见日志。

审稿工作稿入口：[review/main.tex](review/main.tex)。

| 文件 | 内容 |
|---|---|
| [01-context.tex](review/sections/01-context.tex) | 审读对象、版本、阅读起点与任务范围 |
| [02-proof-audit.tex](review/sections/02-proof-audit.tex) | 按证明依赖与原文章节组织的核查 |
| [03-comments.tex](review/sections/03-comments.tex) | 用户疑问与逐节评论，保留来源和状态 |
| [04-assessment-history.tex](review/sections/04-assessment-history.tex) | 综合评价、审稿结论状态、交流与修订历史 |
| [klv-extension.tex](review/appendices/klv-extension.tex) | 独立的 KLV 相关研究附录与有限计算记录 |
| [references.tex](review/references.tex) | 文献与版本定位 |

原有 `notes/*.md` 的实质内容已迁入相应 LaTeX 章节；旧版本保留在 Git 历史中。证明评价及其限制以工作稿为准，不在 README 另写一份结论。

## 编译 LaTeX

使用带有 `ctex`、Fandol 字体、`latexmk` 和 XeLaTeX 的 TeX 安装，从 `review` 目录编译：

```bash
cd review
latexmk -xelatex -halt-on-error main.tex
```

主文件通过 `\input` 管理正文与附录。当前仓库存放源文件；本次迁移未运行 LaTeX 编译，也未重新运行数学检查。

## 计算代码与复算

[计算脚本](tests/check_models.py) 与 [既有运行结果](results/checks.json) 保持原位。测试范围、结果解释和局限写在 LaTeX 工作稿中。

```bash
python -m pip install -r requirements.txt
python tests/check_models.py --max-even-degree 8 --output results/checks.json
```

不要使用 `python -O`；检查使用断言。多项式用常数项在前的整数系数数组保存。既有运行环境记录为 Python 3.13.5、NetworkX 3.6.1。
