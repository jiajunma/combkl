# AGENTS.md — Review collaboration and blueprint authoring

This file governs review collaboration and blueprint authoring in this repository. Review-specific mathematical analysis, user questions and assessments, and review conclusions belong in the corresponding LaTeX work-document sections. Blueprint exposition belongs in the mdblueprint Markdown nodes. Section 7 records the blueprint authoring requirements.

## 1. 文件职责与章节组织

- `AGENTS.md`：可复用于不同论文的通用工作规则。
- `README.md`：文件入口、构建方法和复算说明，不作为审稿意见正文。
- `review/main.tex`：审稿工作稿入口，通过 `\input` 管理章节；具体讨论、证明核查、疑问和评论均保存在其 LaTeX 源文件中。
- 按审读对象与版本、证明核查、逐节问题与评论、综合评价组织正文。证明核查和逐节评论按原论文的章节及证明依赖细分；相关但不属于审稿对象的推广研究放入独立章节或附录。
- 交流与修订历史也保存为 LaTeX；它补充正文的主题组织，不能用流水账代替按章节整理。
- 不另行维护同一内容的 Markdown 审稿或意见日志，避免多个版本互相冲突。迁移旧记录时保留实质内容及来源，更新链接，再移除被替代文件；历史由版本控制保存。

## 2. 开始工作前

阅读本文件、LaTeX 工作稿中相关章节、尚未解决的问题及最近修订记录。核对实际审读的原文版本；关键判断尽量定位到源文件、定理/引理编号或 TeX label，并记录必要的 commit、版本号或其他稳定标识。

已有助手笔记不是已经独立核验的事实，更不是用户的意见。必须检查它们的来源、证据和状态。

## 3. 持续记录重要交流

每轮出现与审稿有关的重要信息时，在当前轮更新相应 LaTeX 章节，无需用户反复要求保存。尤其记录：

- 用户明确的审稿目标、知识起点、理解状态与讲解要求；
- 用户不清楚的概念、记号、步骤，以及具体疑问和疑问理由；
- 用户对正确性、重要性、原创性、表述与可读性的肯定或批评；
- 纠正、决策、核查结果、待办事项与观点变化。

只保存与项目有关的信息，不抄录无关个人资料或凭据。文件更新必须实际完成；失败时说明，不声称已经记录，也不承诺后台自动记录。

## 4. 来源归属与问题状态

明确区分用户原话或忠实转述、助手解释或判断、原文主张、实际核查结果。

每个重要问题使用稳定编号和 LaTeX `\label`，记录日期、来源、原文位置、问题内容、证据及状态。相同问题继续更新原条目，不因跨轮讨论而重复建档。状态至少区分：待讲解、待核查、已解释但待用户确认、已确认解决、仍有争议、暂缓。

用户不理解不等于论文有错，用户怀疑不等于已证实漏洞。未表达的观点记为尚未评价，未说明的背景记为未确认；不得推断为已理解、不会或已认可。助手给出解释及用户未继续追问，都不足以标记用户已理解。技术核查完成与用户确认理解分别记录。

修正旧判断时保留变化依据，不静默抹去疑问或评价；用户明确要求删除或纠正记录时按要求处理。

## 5. 讲解与核查

从用户已经确认的知识起点出发，按依赖顺序给出定义、命题、计算、例子和证明。不用术语堆砌替代论证，也不擅自假定用户掌握专门工具。

区分论文新证明的内容、引用的已有定理、助手补充的推导与尚未验证的猜测。关键步骤要明确假设、结论及用途，检查外部定理的适用范围、版本和归一化。

证明路线不等于完整证明，有限实验不等于一般结论，引用大定理不等于重证该定理。陈述核查范围与限制；发现问题时提供可复核的位置和理由。推广研究与原文评价分别判断，不把未解决的推广自动列为原文缺陷。

## 6. 审稿结论与对外操作

候选审稿意见须可追溯到原文和工作稿。区分已确认的数学错误、需作者澄清的步骤、表述建议和个人理解问题。用户未确认时，不把助手的暂定判断写成用户的意见或最终审稿结论。

仓库内整理和记录的授权不等于对外提交审稿、联系作者、发送邮件或公开发布的授权；这些操作须有明确指示。

## 7. Blueprint requirements

These requirements govern the mathematical blueprint and its generated site.
They record the user's explicit requirements, including the clarifications of
2026-10-17. Keep paper-specific mathematics and review judgments in their
designated documents; this section is the reusable authoring contract.

### Purpose and language

- Write the blueprint, its navigation, explanations, and new accompanying
  documentation in **English**.
- The blueprint must serve as a **textbook or set of lecture notes** based on
  the Lean development. A declaration catalogue, module inventory, collection
  of source dumps, or brief proof outline alone does not satisfy the task.
- Keep the blueprint's mathematical exposition in its Markdown knowledge
  nodes, with chapter reading guides and generated site output. Review
  questions, judgments, and dialogue history remain in the LaTeX work document;
  do not create a second Markdown review log.
- Explain all knowledge needed to understand the development: definitions,
  notation, hypotheses, constructions, intermediate results, proofs, and how
  they fit together. Introduce specialized prerequisites before using them.
- Include a coherent reading sequence, worked examples and calculations, and
  enough intermediate reasoning for a reader to follow the argument without
  having to reconstruct it from Lean tactics.

### Faithfulness to the completed proof

- When the user specifies that the proof is completed, take that as the scope
  of the exposition task. Faithfully explain the existing proof; do not turn
  the task into a search for gaps, a new formalization, or a speculative proof
  plan. Re-running Lean or reassessing correctness requires a separate task.
- Reflect completion in blueprint metadata: Lean-backed theorem entries are
  `proved`, and implemented definitions and source-backed concept overviews
  are `formalized`. Do not label a completed construction `admitted` merely
  because its lecture-note page combines several declarations. Teaching
  examples remain exposition unless separately matched to a Lean theorem.
- Preserve the actual definitions, quantifiers, hypotheses, conclusions,
  grading conventions, and proof dependencies. Do not simplify by silently
  weakening a statement, strengthening a conclusion, or omitting conditions.
- Explain structures and their fields mathematically. Fields and hypotheses
  are not additional kernel axioms. Keep conditional interfaces conditional,
  and distinguish them from unconditional theorems used by the main proof.
- Distinguish mathematical statements from explanatory examples or derived
  calculations added for teaching. Do not imply that an added example is a
  separately formalized declaration unless it actually is.
- Preserve the upstream paper and Lean snapshot. Expository changes belong in
  the blueprint, not in the original proof files.

### One mathematical hierarchy

- Organize the subject as **one unified mathematical development**. Do not
  create separate top-level "Code" and "Mathematics/KL" branches.
- Use the paper's sections and argument as the chapter-level guide. Determine
  the internal hierarchy from the actual mathematical objects and the Lean
  definitions, theorem statements, and proof calls.
- Inspect and validate that hierarchy **before assigning topics**. File names,
  import order, namespace prefixes, and superficial keywords are evidence to
  inspect, not sufficient rules for classifying mathematical content. One file
  may contain several mathematical subjects, and one construction may span
  several files.
- Use enough mathematical detail for lecture notes, without arbitrary
  fragmentation into file-level or implementation-level topics. Conversely,
  do not compress substantive intermediate arguments into vague overview
  pages. Granularity is determined by the exposition and proof structure,
  not by a target page or node count.
- Integrate Lean references into the corresponding mathematical entries.
  Source inventories and module-import data may be provided as supporting
  material, but must not become a parallel mathematical taxonomy.
- Keep the mathematical dependency graph distinct from the module-import
  graph. Record genuine logical prerequisites; do not add a mathematical edge
  merely because two files import one another or share a topic.
- If the paper and Lean implementation organize the proof differently,
  explain their correspondence explicitly. Follow the actual Lean proof
  steps without falsely identifying them with a different paper argument.

### Source alignment and verification

- Generate links deterministically with Python or TypeScript, not by asking an
  LLM to insert or repair individual link occurrences. Keep a checked registry
  of mathematical terms, aliases, definition node IDs, and any topic scopes;
  resolve URLs from the node's actual chapter and the indexed Lean declaration.
- Link technical terms in explanatory prose to their definitions, including
  operators, quadratic relations, and the bar involution. Keep authored prose
  readable without manually embedded links for each term. Skip formulas, code,
  existing links, and a definition's self-references. Reject missing targets
  and ambiguous aliases instead of guessing. Navigation links do not create
  mathematical dependency edges.
- Check rendered links in chapter guides, node pages, and graph details.
  Reject unresolved wiki-reference markers and wrong definition destinations;
  record reproducible linking evidence in the build report.
- Give stable paper locations and precise Lean declaration references for
  mathematical entries, with source files, line locations, and the fixed
  upstream revision where available.
- Inspect the relevant Lean statements and proof bodies before writing their
  explanation. A matching declaration name or an existing file alone does not
  establish semantic alignment.
- Check coverage of the main proof route and its prerequisites, including
  definitions and structural conditions. Source dumps and mechanically valid
  links do not substitute for this expository coverage.
- Validate node schemas, references, mathematical dependencies, chapter
  assignments, and structured-definition field coverage. Generate the graph
  and site through mdblueprint; do not hand-edit generated graph or HTML files.
- Check every generated node page and its internal links, and check formula
  rendering using permitted tools. Keep text-level/source-index checks,
  document-render checks, and actual Lean/kernel checks clearly distinguished.
- Respect the user's execution and screen-privacy restrictions. The existing
  authorization for this task permits local **document construction and
  checks**; it does not authorize Lean execution, mathematical experiments,
  browser automation, or screen capture.
- Rebuild and recheck after substantive changes to the exposition or hierarchy.
  Report what was actually checked, and do not claim comprehensive lecture-note
  coverage based only on page counts or a successful site build.
