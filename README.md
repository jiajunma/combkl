# combkl — KL invariance lecture notes

This repository contains source-linked English lecture notes and review materials for OpenAI's *Combinatorial invariance of Kazhdan–Lusztig polynomials* (September 24, 2026).

## Read the blueprint

- [Published website](https://jiajunma.github.io/combkl/)
- [Lecture-note reading guide](https://jiajunma.github.io/combkl/kl/)
- [Interactive dependency graph](https://jiajunma.github.io/combkl/dep_graph_document.html)
- [Lecture-note guide and build instructions](docs/knowledge/README.md)
- [Main theorem](docs/knowledge/nodes/kl.01_introduction/combinatorial_invariance.md)
- [Simultaneous R-tilde invariance and freeness](docs/knowledge/nodes/kl.06_induction/rtilde_invariance.md)
- [Authoring requirements](AGENTS.md)

The notes follow the paper's six sections. Mathematical statements, explanations, examples, and proofs form one hierarchy, with Lean references integrated into the relevant entries.

The published website can be read without installing anything. GitHub Actions
rebuilds and checks the site when blueprint changes are pushed to the publishing
branch, then deploys it to GitHub Pages. Local previews remain available after
building at build/knowledge/kl/index.html.

## Original materials

The snapshot in [sources/openai-math/](sources/openai-math/) preserves upstream paths and contents at commit adc7f1241b42e322a6451854ab7e4b4c146bf78a.

- [Original paper PDF](sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf)
- [Paper LaTeX entry point](sources/openai-math/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/build/paper.tex)
- [Lean main theorem](sources/openai-math/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean)
- [Provenance and complete file manifest](sources/README.md)

## Review workspace

The review work document is [review/main.tex](review/main.tex). Its sections retain the review context, proof discussions, questions, assessments, and dialogue history. These records are distinct from the mathematical lecture notes; the historical Chinese records are preserved.

AGENTS.md contains collaboration and blueprint authoring requirements. Paper-specific mathematical judgments remain in the review document.

## Build and reproduce

The documentation builder is scripts/build_knowledge.py; its instructions are in [the lecture-note README](docs/knowledge/README.md). Generated HTML and graph data live under the ignored build/ directory.

The existing finite computations remain in [tests/check_models.py](tests/check_models.py), with recorded output in [results/checks.json](results/checks.json). They are independent of the documentation build. Execute mathematical computations only in an environment authorized by the user.

To compile the historical review document in an authorized TeX environment, use XeLaTeX with ctex and the Fandol fonts. From the review directory:

    latexmk -xelatex -halt-on-error main.tex
