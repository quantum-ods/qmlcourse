# Development guide

## Prerequisites

A **general requirement** for all members is to be familiar with GitHub and get with the `markdown` mark-up language (see [Environment](#environment)).
Still, if you are not comfortable with GitHub at all but can provide valuable feedback, pls use comments to a Pull Request or create an Issue. See [Content review](#content-review).

### GitHub intro

If you are not familiar with GitHub, please take [a short course](https://learngitbranching.js.org/) on Git branches. Be familiar with what commits, branches, pulls/pushes are. Further, what are Issues and Pull Requests on GitHub. The rest of the work on the course material is built on that.

## Contributor roles

We see the following roles for contributors to the course:

- Benevolent Dictator

    Semyon Sinchenko, [@SemyonSinchenko](https://github.com/SemyonSinchenko).

- Core Reviewers

    Supposed to be well familiar with quantum information & computation, preferably with experience in QML as well. Also, eager to  provide critical feedback.

- Reviewers

    Those who don't satisfy the requirements for core reviewers, but still want to review the content being generated. By default that's everyone who is invited to the [#org_qml_course](https://opendatascience.slack.com/archives/CEH3VJCRJ) Slack channel.

- Authors

    Content generators, to be agreed with Benevolent Dictator. See [Issues](https://github.com/quantum-ods/qmlcourse/issues) to pick up one of the open tasks.

- Editors

    Editors wait for a PR to be approved, and then introduce their changes fixing grammar, language, etc.

- Orgs

    These guys help organize/promote the course.

- Others

    We might have some other crowd-sourced help like helping with the course website or course assignments. To be elaborated.

## Environment

All course content is being developed as a [`Jupyter Book`](https://jupyterbook.org/intro.html).

### MyST markdown

`Jupyter Book` uses its dialect of markdown named `MyST`. We prefer `MyST` construction over raw `HTML` blocks and **there should be a significant reason to use raw HTML** instead. A detailed description of `MyST` opportunities could be found [here](https://jupyterbook.org/reference/cheatsheet.html).

### Diagrams and Figures

We chose the [`PlantUML`](https://plantuml.com) as a standard for all the diagrams. The reason is the simple and understandable syntax and the good quality of final images. You should prefer `<latex></latex>` over `<math></math>` for math equations inside blocks of the diagram. You can find the documentation on the [official site](https://plantuml.com/sitemap-language-specification).

Any `PlantUML` diagram can be exported to `.png` by https://plantuml-editor.kkeisuke.com. If you make any changes in the raw `.plantuml` file you should update generated picture file.

Matplotlib figures should be

- located at the corresponding lecture folder into `_static/`;
- using the format, for example

        ```{figure} /_static/qcalgo/ru/quantum_algorithms_overview/problem_classes.png
        :name: problem_classes
        :width: 400px

        Еasks сlasses according to temporal complexity
        ```

### Code cell

- If code cell should be running, use `{code-cell} ipython3` like

        ```{code-cell} ipython3
        a = 2
        b = 2

        c = a + b

        print(f"{c = }")
        ```

- if note, just wrap it on code-cell like

        ```
        a = 2
        b = 2

        c = a + b

        print(f"{c ==}")
        ```

### Building the project

To watch your result (after `git push`) you can build `Jupyter Book` automatically by GitHub Action: in the page, https://github.com/quantum-ods/qmlcourse/actions/workflows/deploy-branch.yml choose your branch and press `Run workflow`. After ~10min visit https://qmlc-deploy-branch.netlify.app/book/index.html and find your lectures page.

### Chapters and headers

Chapters and headers in markdown must exactly follow the main structure of the book (into [`_toc.yml`](./qmlcourseRU/_toc.yml)). Read [this](https://jupyterbook.org/customize/toc.html#how-headers-and-sections-map-onto-to-book-structure) if you have problems with this.

Russian & English version lectures add after comment `# :ru:` & `# :en:` accordingly.

> **Note**
> 
> Each lectures & pictures should be either `/ru/` or `/en/` folder separated.

### Glossary terms

Please add all terms, preferably with short explanations (and, for Russian variant, its English original) to common [`glossary.md`](./qmlcourseRU/book/glossary.md). On first use of a term in main book text, please refer to glossary using the format:

```markdown
{term}`chapter text<glossary term>`
```

*with this notation, the chapter will contain text "chapter text" and the build script will create a reference to "glossary term".*

### Bibliography

We stick to adding as many as possible links to papers/books/.. to confirm our words. For this we have the page [`bibliography`](./qmlcourseRU/_bibliography/references.bib) (sorted alphabetically) like

```markdown
{cite}`farhi2014quantum`
```

### Internal links

Use relative references not absolute like `../qcblock/qubit.md` or with a specific chapter `../qcblock/qubit.html#id25` in the lecture.

## Content review

Each lecture/assignment or any other unit of content gets its branch and a Pull Request into the `master`. For example, see [Pull Request #1](https://github.com/quantum-ods/qmlcourse/pull/1) with lecture #1 material.

*The review process depends on whether a reviewer is familiar with GitHub or not.*

### Reviewing without commits (no git fluency required)

Go to a Pull Request with lecture content (e.g. [this one](https://github.com/quantum-ods/qmlcourse/pull/3/files) for lecture 2), further visit the `Files Changed` tab and add your reviewer comments to specific lines.

Example:

<img src="https://habrastorage.org/webt/3m/zv/wv/3mzvwvnqmeatuuyvob5qpvfvobk.png" width="600" height="400" />

All comments should be made in the `File changed` tab not in the `Conversation` (is only used for discussion and comments about the PR in general).

### Reviews as commits (basic git fluency required)

We don't want to mess up the process with too many branches. Thus, each lecture gets its feature branch, the review is done via a Pull Request to `master`, and all modifications are introduced as commits to the same feature branch and thus show up in the same Pull Request.

The preferred way to commit your changes is to:

- introduce your changes, mainly to `.md` files;
- commit changes to the same feature branch.

Example:

<img src="https://habrastorage.org/webt/1f/fa/ob/1ffaobyn99cuc58fa19pvse_pvw.png" width="600" height="300" />

## Issues

- If you want to add something new to the course content you should start with creating an issue with the label `enhancement` where you need to describe your idea.
- If you see an open issue, you can write a comment that you can do it and you will be assigned to this issue.

## Pull Requests

- If you were assigned to an issue, you need to create a new branch from the `master`.
- When you finish your work you make a Pull Request (into `master` branch) where you tag the initial issue and assign yourself (right in the panel).

### Run pre-commit hooks before building

*This part not necessarily, the reviewers will do it for you*

Before the final `git push` you can run hooks, you should install the [pre-commit](https://pre-commit.com/#installation). To execute pre-commit, run (if using poetry)

```{shell}
poetry run pre-commit run --all-files
```

After command execution, some files automatically can be changed and then repeat the command (to be sure) and push.

Also, we have a spell-checker and it requires simple manual intervention. If

- that's indeed a typo, you need to fix it in source files;
- you think this word is correct, add this word to the dictionary file [`.yaspellerrc.json`](./.yaspellerrc.json) -- part `dictionary` or part `ignoreText`;
- about remaining mistakes ask your curator.

## List of authors

If you make a lecture, review the course you should add yourself to

- a full list of the authors [here](./qmlcourseRU/book/authors.md)
- in the header lecture

The list is sorted alphabetically and you need to place your surname and name (or nickname if you want) and link to the GitHub account into the corresponding dropdown block or another webpage if you want.

## Translate

All English version start after block **"О КУРСЕ / ABOUT THE COURSE"** where blocks duplicated from Russian. Each lectures folders and pictures have `ru/` & `en/` separate folders to split languages versions.

## Intellectual property rights

The course is under the CC-like license. All the media content needs to be under the CC license as well. Content from the [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page) is preferable! There must be a serious reason to include in the course media from other sources. Each such case must be discussed first with one of the co-founders of the course.

The same holds for blocks of text: all the text of our lectures must be original only text! If you want to use a quote it is OK only with citations of the reference (we use BibTex bibliography).

## Typos

If you found a typo in the text you can create a branch with a name like or `{user_name}-misspell-{lecture_name}` and make a Pull Request directly to the master. In this case, it'd suffice to have only one review from co-founders or core reviewers.
