# AGENTS.md

Guidance for AI agents (and humans) working on this repository.
Read this before touching anything.

## What this project is

`qmlcourse` is an open, community-built course on **Quantum Machine Learning**
("Курс по КМО" — *квантовое машинное обучение*). It was written in 2020–2022 by the
Quantum community of [Open Data Science (ODS)](https://ods.ai), led by
Semyon Sinchenko ([@SemyonSinchenko](https://github.com/SemyonSinchenko)), and
published as a Jupyter Book at `https://quantum-ods.github.io/qmlcourse/`.

The original language is **Russian**. An English version exists only as a stub
(`book/intro/en`, `book/linalg/en`) and is a goal, not a reality yet.

After 2022 the project went unmaintained. The content is still valuable and
liked by readers; the tooling (Jupyter Book 1, Python 3.8, pinned 2021-era
quantum SDKs) has rotted. The current goal is to **revive** it, not to rewrite it.

## Philosophy — the thing that must survive any refactor

**"Quantum physics for programmers."** The course explains quantum mechanics and
quantum computing to people who know Python and a bit of ML, *not* physics.

1. **Explain with numpy first, frameworks second.** A qubit is a `(2, 1)` complex
   numpy array; a gate is a unitary matrix; measurement is sampling from
   `|amplitude|**2`. Readers should be able to reproduce every concept with plain
   linear algebra before they ever see PennyLane, Qiskit or Cirq. Frameworks are
   shown as convenient tools on top of an understanding the reader already has.
2. **Every explanation is backed by runnable code.** The pages are executable
   MyST notebooks (`{code-cell}` blocks). Code is part of the narrative, not an
   appendix. Outputs shown to the reader are produced by actually running it.
3. **Simple but honest.** Intuition and analogies ("Schrödinger's cat", "ML as a
   puzzle") are welcome, but must not be *wrong*. Rigor where it matters,
   hand-waving clearly marked as such. When simplifying, say that you simplify.
4. **Adaptive depth.** Lectures are colour-coded by level; readers pick their path:
   - 🟦 BLUE — introductory lectures;
   - 🟩 GREEN — the "core" track of the course;
   - 🟨/🟧 YELLOW/ORANGE — deeper dives into a block's topic;
   - 🟥 RED — the physics and maths behind it all;
   - ⬜ WHITE — optional / block intros.
   The program diagram is `qmlcourse/_static/index/program.plantuml`.
5. **Practical and NISQ-oriented.** Focus on methods that are realistic for
   near-term hardware (VQC, VQE, QAOA, quantum kernels, annealing) and on how real
   problems (chemistry, Ising, combinatorial optimisation) map to them.
6. **Light tone, technical substance.** Friendly, a bit informal, written by
   enthusiasts for curious engineers. Keep that voice in edits and translations.

## Authorship and context — non-negotiable

Everything else (tooling, site generator, layout, theme) may change freely.
These may not:

- **Keep authorship.** Every lecture starts with an `Автор(ы):` list. Keep it
  intact, in translations too (as `Author(s):`). Never remove or reassign authors.
- Keep `book/authors.md`, `book/acknowledgments.md`, `CITATION.cff` and the
  `LICENSE` (**CC BY 4.0**). Attribution is a licence requirement, not a courtesy.
- Keep the historical context: this is an ODS community course from 2021–2022.
  Do not rebrand it, do not erase the community, do not present it as new work.
- **Translations are derivative works.** LLM-produced translations must be
  labelled as such on the page (e.g. an admonition "Machine-translated from the
  Russian original; reviewed by …/not yet reviewed"), and must link back to the
  Russian original.
- **Content corrections are visible.** When fixing a factual error or updating
  out-of-date information, prefer adding a dated note (e.g.
  `{note}` "Updated 2026: …") over silently rewriting the authors' text, unless
  it is a plain typo or an unambiguous mistake. Cite a source for every updated
  number (qubit counts, error rates, roadmaps, prices, SDK APIs).

## Repository layout

```
qmlcourse/                 # the book root (a MyST / Jupyter Book 2 project)
  myst.yml                 # project + site config and the table of contents
  _bibliography/references.bib
  _static/<block>/<lang>/  # images per block and language
  book/<block>/<lang>/<lecture>.md   # MyST markdown notebooks
  book/*.md                # index, authors, glossary, bibliography, ...
pyproject.toml, uv.lock    # Python 3.12 environment (uv)
Makefile                   # install / serve / build / check
scripts/check_execution_errors.py    # CI gate: no failing code cells
.github/workflows/build.yml          # build on PR, build + deploy Pages on master
CONTRIBUTING.md                      # original contributor guide (tooling part updated)
```

Build: `make install && make build && make check` (needs `uv` and Node.js >= 20).
The build executes every `{code-cell}` (`jupyter-book build --html --execute`) and
does **not** fail on cell errors by itself — `make check` does.

Dev-container gotcha: when running as root, the Jupyter server refuses to start
and MyST reports "Could not load Jupyter session manager". Fix with
`echo 'c.ServerApp.allow_root = True' > ~/.jupyter/jupyter_server_config.py`.

Conventions inherited from the original project:

- Lectures are MyST markdown with jupytext front matter and `kernelspec`.
- Cross-references use MyST labels: `(qubit)=` before the title.
- Citations use `{cite}` against `references.bib`.
- Diagrams are PlantUML sources rendered to SVG.
- Language is a path segment: `book/qc/ru/qubit.md` ↔ `book/qc/en/qubit.md`;
  same for `_static/qc/ru/...` ↔ `_static/qc/en/...`.
  Mirror the Russian file name and structure exactly in other languages.

## Working rules for agents

- **No git writes.** Commits are made by the maintainer on the host and signed
  with their key; `.git` is read-only in the dev container. Prepare changes in
  the working tree and describe them; do not commit, stash, rebase or push.
- Do not mass-reformat the lectures. Diffs to content must be reviewable by a human.
- Keep the Russian original as the source of truth; translate *from* it.
- Do not add heavyweight dependencies just for one cell. Dead or uninstallable
  frameworks (TensorFlow Quantum) are not dependencies: their cells are tagged
  `skip-execution` and the page carries a "framework is dead" admonition.
- Code cells must run on a CPU-only CI runner in reasonable time and without
  secrets. Cells that need cloud access (D-Wave Leap token) are tagged
  `skip-execution`, with a note on the page explaining why.
- Keep PennyLane and Qiskit code working with their latest releases. Idioms:
  `shots` goes to `qml.qnode(dev, shots=N)` (not the device); trainable
  parameters must be `pennylane.numpy` arrays (tuples are silently not trained);
  Qiskit simulators come from `qiskit_aer.AerSimulator`; classical control uses
  `with qc.if_test(...)` instead of `c_if`.
- No TensorFlow. Keras (3.x) runs on the JAX backend, which is already pulled in
  by NetKet: set `os.environ["KERAS_BACKEND"] = "jax"` before `import keras`.
- Generated artifacts (`_build/`, `.venv/`, rendered sites) are never committed.

## Status / roadmap

1. Revive the build: modern toolchain, working CI, deploy to GitHub Pages.
   **Done (2026-11)**: Jupyter Book 2 + uv, all executable lectures pass on
   PennyLane 0.45 / Qiskit 2.6; TFQ and D-Wave lectures are not executed.
2. Proper language switching (ru / en) and an LLM-assisted English translation.
3. Fact-check pass: physics errors and out-of-date claims (hardware qubit counts,
   vendor roadmaps, SDK APIs).

Known content issues found while reviving (not fixed yet):

- `problems2qml/ru/eigenvals.md`: the sparse-matrix demo builds a diagonal 0/1
  matrix, so min and max eigenvalues should differ (0 and 1), but ARPACK prints
  `1.0` for both — the example is misleading.
- Many links point to the retired `qiskit.org` docs/textbook.
- Cyrillic text inside formulas should be wrapped in `\text{}`.
