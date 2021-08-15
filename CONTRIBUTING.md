# Development guide

## Table of contents

1. [Prerequisites](#prerequisites)
2. [Contributor roles](#contributor-roles)
3. [Environment](#environment)
4. [GitHub intro](#github-intro)
5. [Content review](#content-review)
6. [Issues](#issues)
7. [Pull Requests](#pull-requests)
8. [List of Authors](#authors)
9. [Intellectual property](#rights)
10. [Small changes](#misspells)

## Prerequisites

A **general requirement** for all members is to be familiar with GitHub and get familiar with the `markdown` mark-up language (see [Environment](#environment)).

Still, if you are not comfortable with GitHub at all but are able to provide valuable feedback, pls use comments to a Pull Request. See [Content review](#content-review).

## Contributor roles

We see the following roles for contributors to the course:

- Benevolent Dictator
- Core reviewers
- Reviewers
- Authors
- Editors
- Orgs
- Others

### Benevolent Dictator

Semyon Sinchenko, @sem.

### Core reviewers

Supposed to be well familiar with quantum information & computation, preferably with experience in QML as well. Also, eager to provide critical feedback.

### Reviewers

Those who don't satisfy the requirements for core reviewers, but still want to review the content being generated. By default that's everyone who is invited to the #org_qml_course Slack channel.

### Authors

Content generators, to be agreed with Benevolent Dictator. See [Issues](https://github.com/SemyonSinchenko/qmlcourse.ai/issues) to pick up one of the open tasks.

### Editors

Editors wait for a PR to be approved, and then introduce their changes fixing grammar, language, etc.

### Orgs

These guys help organizing/promoting the course.

### Others

We might have some other crowd-sourced help like helping with the course web-site or course assignments. To be elaborated.

## Environment

All course content is being developed as a [Jupyter Book](https://jupyterbook.org/intro.html).

### MyST markdown

`Jupyter Book` uses the own dialect of markdown named `MyST`. We prefer `MyST` construction over raw `HTML` blocks and **there should be a significant reason to use raw HTML** instead. Detailed description of `MyST` opportunities could be found [here](https://jupyterbook.org/reference/cheatsheet.html).

### Diagrams and Figures

I chose the PlantUML as a standard for all the diagrams. The reason is the simple and understandable syntax and a good quality of final images. You should prefer `<latex></latex>` over `<math></math>` for math equations inside blocks of the diagram.

Any PlantUML diagram can be exported to `.png` with the [PlantUML tool](https://plantuml.com/). You can download Java `.jar` file from the official site or install binary package. [Installation instructions](https://plantuml.com/starting).

- `apt install plantuml` for Ubuntu
- `choco install plantuml` for Windows
- `brew install plantuml ` for Mac

You can find the documentation on the [official site](https://plantuml.com/sitemap-language-specification). If you make any changes in the raw `.plantuml` file you should:

1. export it in `.png` file (`plantuml filename.plantuml` or `java -jar path_to_plantuml filename.plantuml`)
2. rebuild the whole book (`jupyter-book build qmlcourseRU`)

Matplotlib figures should be included in the source code of markdown by `{code-cell} ipython3` blocks to be reproducible.

### Building the project

Before making a Pull-Request try to build the book with the following command:

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

## GitHub intro

If you are not familiar with GitHub, please take [a short course](https://learngitbranching.js.org/) on Git branches. Be familiar with what commits, branches, pulls/pushes are. Further, what are Issues and Pull Requests on GitHub. The rest of the work on the course material is built on that.

## Content review

Each lecture/assignment or any other unit of content gets its own branch and a Pull Request (PR) into the `master` branch. For example, see [Pull Request #1](https://github.com/SemyonSinchenko/qmlcourse.ai/pull/1) with lecture #1 material.

Every PR needs to have at least 4 approvals and at least 1 of them from a Core Reviewer. If you see a Pull Request and want to review it you can add yourself as a reviewer.

The review process depends on whether a reviewer is familiar with GitHub or not.

### Reviewing without commits (no git fluency required)

Go to a Pull Request with lecture content (e.g. [this one](https://github.com/SemyonSinchenko/qmlcourse.ai/pull/3/files) for lecture 2), further visit the `Files Changed` tab and add your reviewer comments to specific lines.

Example:

<img src="https://habrastorage.org/webt/3m/zv/wv/3mzvwvnqmeatuuyvob5qpvfvobk.png" />

All comments should be made in the `File changed` tab not in the `Conversation`. `Conversation` is only used for discussion and comments about the PR in general.

### Reviews as commits (basic git fluency required)

We don't want to mess up the process with too many branches. Thus, each lecture gets its own feature branch, the review is done via a PT to `master`, and all modifications are introduced as commits to the same feature branch and thus shows up in the same PR.

The preferred way to commit your changes is to:

- Write a message like "I need 2 hours for a review" in the `Conversation` tab. Thus you mention that you are the person modifyig the content right now
- Introduce your changes, mainly to `.md` files
- Commit changes to the same feature branch
- Tell others that you are done with your review

Example:

 <img src="https://habrastorage.org/webt/1f/fa/ob/1ffaobyn99cuc58fa19pvse_pvw.png" />

## Issues

- If you want to add something new to the course content you should start with creating of an issue with label `enhancement` where you need to describe your idea;
- If you see an open issue without assignment and with a label `help wanted`, you can write a comment that you can do it and you will be assigned to this issue.

## Pull Requests

- If you were assigned to an issue, you need to create a new branch from the `master`
- When you finish your work you make a Pull Request (into `master` branch) where you tag the initial issue and assign youself (right in the panel)

### Run pre-commit hooks before building

Before you can run hooks, you need to have the pre-commit package manager installed.

Install poetry (package manager for Python projects)

```{shell}
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Install dependency and pre-commit

```{shell}
poetry install
```

Run pre-commit hooks
```{shell}
poetry run pre-commit run --all-files
```

### Run spell-checker

Before make a Pull Request, you need to run book checker test.
During this process, github action will make spell check.

Spell check use `yaspeller`.
`Yaspeller` is Search tool typos in the text, files and websites.
Yaspeller use API Yandex.Speller.

For run spell check, you need:
1. Open GitHub Actions for your project.
2. Choose `book-check-text` workflow.
3. Click on button `Run workflow` (on the right) and choose your branch name.
<img src="https://habrastorage.org/webt/nf/hv/vx/nfhvvx2skeudhoecaqczqmhxhb4.png" />

If you have mistakes after spell check was finished, you need:
1. Get a log from this job. 
Actions Page - `book-check-text` - click on your workflow with mistake - click `Spell check`
<img src="https://habrastorage.org/webt/qn/ja/cf/qnjacfv9tclhxkhmmknffqrw0lq.png" />
<img src="https://habrastorage.org/webt/xt/vs/eo/xtvseofzzdk5gjlrksc4gno0mms.png" />

2. Investigate this logs and each mistakes.
3. If you did own mistake you need to fix it in your code.
4. If you think this word is correct - add this word in dictionary. 
file `.yaspellerrc.json` - part `dictionary` or part `ignoreText`
5. About remaining mistakes ask your curator.


## List of authors <a name="authors"></a>

If you make a Pull-Request or review or another contribution to the course you should add yourself to a full list of the authors. This list is placed in a markdown file ([Russian version](./qmlcourseRU/book/authors.md)) and is a part of a book. The list is sorted alphabetically and you need to place your surname and name (or nickname if you want) and link to the github account into the corresponding dropdown block. Such a Pull-Request should be form the branch with name like `authors/add_author_{you git account here}` and could be merged after only one approve from one of core reviewers.

## Intellectual property rights <a name="rights"></a>

The course is under the CC-like license. All the media content needs to be under the CC license as well. Content from the [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page) is preferable! There must be a serious reason to include in the course media from other sources. Each such case must be discussed first with one of the co-founders of the course.

The same holds for blocks of text: all the text of our lectures must be original only text! If you want to use quote it is OK only with citations of the reference (we use BibTex bibliography).

## Typos

If you found a typo in the text you can create a branch with name like `/misspell/{lecture_name}` and make a Pull-Request directly to the master. In this case it'd suffice to have only one review from co-founders or core-reviewers.
