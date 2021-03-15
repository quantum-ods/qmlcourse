# Development guide

## Table of contents

1. [Contributor roles](#contributor-roles)
1. [Environment](#environment)
1. [GitHub intro](#github-intro)
1. [Review](#review)
1. [Issues](#issues)
1. [Pull-requests](#pull-requests)

## Contributor roles

We see the following roles for contributors to the course:

- Benevolent Dictator
- Core reviewers
- Reviewers
- Authors
- Editors
- Orgs 
- Others

A **general requirement** for all members it to be familiar with GitHub and get familiar with the `Org` text file format (see [Environment](#environment)).

### Benevolent Dictator

Semyon Sinchenko.

### Core reviewers

Supposed to be well familiar with quantum information & computation, preferrably with experience in QML as well. Also, eager to provide critical feedback. 

### Reviewers

Those who don't satisfy the requirements for core reviewers, but still want to review the content being generated. 

### Authors

Content generators, to be agreed with Benevolent Dictator. 

### Editors

Editors wait for a PR to be approved, and then introduce their changes fixing grammar, language, etc. 

### Orgs

_Not to be confused with the `Org` text file format._ 

These guys help organizing/promoting the course. 


### Others

We might have some other crowd-sourced help like helping with the course web-site or course assignments. To be elaborated.  

## Environment

This repository contains org-files with lectures. Semyon chose an `org-mode` because:

- `org-mode` has native support of `LaTeX` code-blocks and `LaTeX` packages;
- `org-mode` has native support of `HTML` blocks and extra-headers;
- `org-mode` allows different code blocks for different export formats;
- Semyon used to write notes in `org-mode`

It is the topic of discussion and the files format may be changed any time if there are enough reasons.

`pandoc` could be used as universal exporter for `org-mode` files.

### Export org-file to pdf

`pandoc --pdf-engine xelatex -f org input.org -o output.pdf`

### Export org-file to html

`pandoc -s --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js -t html5 input.org -o output.html`

### Environment configuration

- For Emacs editor, `org-mode` is a native format. It is supported by popular Emacs configuration kits:

  - [Spacemacs](https://www.spacemacs.org/)
  - [Doom Emacs](https://github.com/hlissner/doom-emacs)

- In Visual Studio Code, `org-mode` is supported via [VSCode plugin](https://github.com/vscode-org-mode/vscode-org-mode)
- Other ways of writing in `org-mode` format are described [here](https://opensource.com/article/19/1/productivity-tool-org-mode)

### Org-mode syntax

The syntax of `org-mode` is quite similar to another mark-up languages (markdowm, reStructured, etc.) but allows more low-level options for `LaTeX` and `HTML`.

About `org-mode`:

- [LaTeX in org-mode](https://opensource.com/article/20/4/emacs-org-mode)
- [org-mode syntax cheat sheet](https://nhigham.com/2017/11/02/org-mode-syntax-cheat-sheet/)
- [official documentations](https://orgmode.org/org.html)


## GitHub intro

If you are not familiar with GitHub, please take [a short course](https://learngitbranching.js.org/) on Git branches. Be familiar with what commits, branches, pulls/pushes are. Further, what are Issues and Pull Requests on GitHub. The rest of the work on the course material is built on that.


## Content review

Each lecture/assignment or any other unit of content gets its own branch and a Pull Request (PR) into the `master` branch. For example, see [Pull Request #1](https://github.com/SemyonSinchenko/qmlcourse.ai/pull/1) with lecture #1 material. 

Every PR needs to have at least 4 approves and at least 1 of them from a Core Reviewer. If you see a Pull Request and want to review it you can add yourself as reviewer. All reviews should be made via `Review changes` button in GitHub and all comments should be made in `File changed` tab not in the `conversation`. You shouldn't write to the `conversation` commentaries about specific parts of a Pull Request. `Conversation` is only for discussion and comments about the PR in general.


## Issues

- If you want to add something new to the course you should start with creating of issue with label `enchancement` where you need to describe your idea;
- If you see an open issue without assignment and with a label `help wanted`, you can write a comment that you can do it and you will be assigned to this issue.

## Pull Requests

- If you was assigned to an Issue, you need to create a new branch. When you finish your work you make a Pull Request where you tag the initial issue.
