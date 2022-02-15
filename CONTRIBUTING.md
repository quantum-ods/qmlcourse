<!-- todo:
    * update `Table of contents`
    * replace java instead https://plantuml-editor.kkeisuke.com into `Diagrams and Figures`
    * rename forder `qmlcourseRU` to `qmlcourse`
-->

# Development guide

## Prerequisites

A **general requirement** for all members is to be familiar with GitHub and get with the `markdown` mark-up language (see [Environment](#environment)).
Still, if you are not comfortable with GitHub at all but are able to provide valuable feedback, pls use comments to a Pull Request or create Issue. See [Content review](#content-review).

----

## Contributor roles

We see the following roles for contributors to the course:

- Benevolent Dictator

    Semyon Sinchenko, @sem.

- Core reviewers

    Supposed to be well familiar with quantum information & computation, preferably with experience in QML as well. Also, eager to  provide critical feedback.

- Reviewers

    Those who don't satisfy the requirements for core reviewers, but still want to review the content being generated. By default that's everyone who is invited to the [#org_qml_course](https://opendatascience.slack.com/archives/CEH3VJCRJ) Slack channel.

- Authors

    Content generators, to be agreed with Benevolent Dictator. See [Issues](https://github.com/quantum-ods/qmlcourse/issues) to pick up one of the open tasks.

- Editors

    Editors wait for a PR to be approved, and then introduce their changes fixing grammar, language, etc.

- Orgs

    These guys help organizing/promoting the course.

- Others

    We might have some other crowd-sourced help like helping with the course web-site or course assignments. To be elaborated.

----

## Environment

All course content is being developed as a [Jupyter Book](https://jupyterbook.org/intro.html).

### MyST markdown

`Jupyter Book` uses the own dialect of markdown named `MyST`. We prefer `MyST` construction over raw `HTML` blocks and **there should be a significant reason to use raw HTML** instead. Detailed description of `MyST` opportunities could be found [here](https://jupyterbook.org/reference/cheatsheet.html).

### Diagrams and Figures

We chose the PlantUML as a standard for all the diagrams. The reason is the simple and understandable syntax and a good quality of final images. You should prefer `<latex></latex>` over `<math></math>` for math equations inside blocks of the diagram.

Any PlantUML diagram can be exported to `.png` with the [PlantUML tool](https://plantuml.com/). You can download Java `.jar` file from the official site or install binary package. [Installation instructions](https://plantuml.com/starting).

- `apt install plantuml` for Ubuntu
- `choco install plantuml` for Windows
- `brew install plantuml ` for Mac

You can find the documentation on the [official site](https://plantuml.com/sitemap-language-specification). If you make any changes in the raw `.plantuml` file you should:

1. export it in `.png` file (`plantuml filename.plantuml` or `java -jar path_to_plantuml filename.plantuml`)
2. rebuild the whole book (`jupyter-book build qmlcourseRU`)

Matplotlib figures should be included in the source code of markdown by `{code-cell} ipython3` blocks to be reproducible.

### Building the project

Before making a Pull Request try to build the book with the following command:

```{shell}
jupyter-book build qmlcourseRU
```

_If you have problems with the build command try to pass the full path to the folder_

### Chapters and headers

Chapters and headers in markdown must exactly follow the main structure of the book. Read [this](https://jupyterbook.org/customize/toc.html#how-headers-and-sections-map-onto-to-book-structure) if you have problems with this.

### Glossary terms

Please add all terms, preferably with short explanations (and, for Russian variant, its English original) to common
glossary, `glossary.md`.

On first use of a term in main book text, please refer to glossary using the format:
```markdown
{term}`chapter text<glossary term>`
```
(with this notation, the chapter will contain text "chapter text" and build script will create reference to
"glossary term").

----

## GitHub intro

If you are not familiar with GitHub, please take [a short course](https://learngitbranching.js.org/) on Git branches. Be familiar with what commits, branches, pulls/pushes are. Further, what are Issues and Pull Requests on GitHub. The rest of the work on the course material is built on that.

----

## Content review

Each lecture/assignment or any other unit of content gets its own branch and a Pull Request (PR) into the `master` branch. For example, see [Pull Request #1](https://github.com/quantum-ods/qmlcourse/pull/1) with lecture #1 material.

Every PR needs to have at least 4 approvals and at least 1 of them from a Core Reviewer. If you see a Pull Request and want to review it you can add yourself as a reviewer.

The review process depends on whether a reviewer is familiar with GitHub or not.

### Reviewing without commits (no git fluency required)

Go to a Pull Request with lecture content (e.g. [this one](https://github.com/quantum-ods/qmlcourse/pull/3/files) for lecture 2), further visit the `Files Changed` tab and add your reviewer comments to specific lines.

Example:

<img src="https://habrastorage.org/webt/3m/zv/wv/3mzvwvnqmeatuuyvob5qpvfvobk.png" />

All comments should be made in the `File changed` tab not in the `Conversation`. `Conversation` is only used for discussion and comments about the PR in general.

### Reviews as commits (basic git fluency required)

We don't want to mess up the process with too many branches. Thus, each lecture gets its own feature branch, the review is done via a PT to `master`, and all modifications are introduced as commits to the same feature branch and thus shows up in the same PR.

The preferred way to commit your changes is to:

- write a message like "I need 2 hours for a review" in the `Conversation` tab. Thus you mention that you are the person modifyig the content right now;
- introduce your changes, mainly to `.md` files;
- commit changes to the same feature branch;
- tell others that you are done with your review.

Example:

 <img src="https://habrastorage.org/webt/1f/fa/ob/1ffaobyn99cuc58fa19pvse_pvw.png" />

----

## Issues

- If you want to add something new to the course content you should start with creating of an issue with label `enhancement` where you need to describe your idea.
- If you see an open issue without assignment and with a label `help wanted`, you can write a comment that you can do it and you will be assigned to this issue.

----

## Pull Requests

- If you were assigned to an issue, you need to create a new branch from the `master`
- When you finish your work you make a Pull Request (into `master` branch) where you tag the initial issue and assign youself (right in the panel)

### Run pre-commit hooks before building

*This part not necessarily, the reviwers will do it for you*

Before the final `git push` you can run hooks, you should install the [pre-commit](https://pre-commit.com/#installation). To execute pre-coomit, run (if using poetry)

```{shell}
poetry run pre-commit run --all-files
```

After command execution some files automatically change and then repeat the command and push.

Also, we have spell-checker and it requires simple manual intervention. If

- that's indeed a typo, you need to fix it in source files.
- you think this word is correct, add this word to the dictionary file `.yaspellerrc.json` -- part `dictionary` or part `ignoreText`.
- About remaining mistakes ask your curator.

----

## List of authors <a name="authors"></a>

If you make lecture, review to the course you should add yourself to

- a full list of the authors [here](./qmlcourseRU/book/authors.md)
- in the header lecture

The list is sorted alphabetically and you need to place your surname and name (or nickname if you want) and link to the github account into the corresponding dropdown block or another web-page if you want.

----

## Intellectual property rights <a name="rights"></a>

The course is under the CC-like license. All the media content needs to be under the CC license as well. Content from the [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page) is preferable! There must be a serious reason to include in the course media from other sources. Each such case must be discussed first with one of the co-founders of the course.

The same holds for blocks of text: all the text of our lectures must be original only text! If you want to use quote it is OK only with citations of the reference (we use BibTex bibliography).

----

## Typos

If you found a typo in the text you can create a branch with name like or `{user_name}-misspell-{lecture_name}` and make a Pull Request directly to the master. In this case it'd suffice to have only one review from co-founders or core-reviewers.
