# Development guide

## Table of contents

1. [Prerequisites](#prerequisites)
1. [Contributor roles](#contributor-roles)
1. [Environment](#environment)
1. [GitHub intro](#github-intro)
1. [Content review](#content-review)
1. [Issues](#issues)
1. [Pull Requests](#pull-requests)


## Prerequisites

A **general requirement** for all members is to be familiar with GitHub and get familiar with the `Org` text file format (see [Environment](#environment)).

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

@gamlo, @Aleksandr Berezutskii, @Sergei Shirkin, @annakey. To be extended.

### Reviewers

Those who don't satisfy the requirements for core reviewers, but still want to review the content being generated. 

By default that's everyone who is invited to the #org\_qml\_course Slack channel.

### Authors

Content generators, to be agreed with Benevolent Dictator. See [Issues](https://github.com/SemyonSinchenko/qmlcourse.ai/issues) to pick up one of the open tasks.  

@stm (Python), sharthZ23 (Python, NumPy), @alex.ozerin (NumPy, math), @yorko (ML intro), @Pola Ron (quantum enthropy), @gamlo (hardware), @Sergei Shirkin (PennyLane). To be extended.

### Editors

Editors wait for a PR to be approved, and then introduce their changes fixing grammar, language, etc. 

@nmarkova, @vitaliylyalin7000

### Orgs

_Not to be confused with the `Org` text file format._ 

These guys help organizing/promoting the course. 

@yorko, @vtrohymenko


### Others

We might have some other crowd-sourced help like helping with the course web-site or course assignments. To be elaborated.  

## Environment

This repository contains org-files with lectures. Semyon chose an `org-mode` because:

- `org-mode` has native support of `LaTeX` code-blocks and `LaTeX` packages;
- `org-mode` has native support of `HTML` blocks and extra-headers;
- `org-mode` allows different code blocks for different export formats;
- Semyon used to write notes in `org-mode`

It is the topic of discussion and the files format may be changed any time if there are enough reasons.

`pandoc` could be used as a universal exporter for `org-mode` files.

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

The syntax of `org-mode` is quite similar to other mark-up languages (markdowm, reStructured, etc.) but allows more low-level options for `LaTeX` and `HTML`.

About `org-mode`:

- [LaTeX in org-mode](https://opensource.com/article/20/4/emacs-org-mode)
- [org-mode syntax cheat sheet](https://nhigham.com/2017/11/02/org-mode-syntax-cheat-sheet/)
- [official documentations](https://orgmode.org/org.html)


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

We don't want to mess up the process with too many brnaches. Thus, each lecture gets its own feature branch, the review is done via a PT to `master`, and all modifications are introduced as commits to the same feature branch and thus shows up in the same PR. 

The preferred way to commit your changes is to:

 - Write a message like "I need 2 hours for a review" in the `Conversation` tab. Thus you mention that you are the person modifyig the content right now
 - Introduce your changes, mainly to `org` files
 - Commit changes to the same feature branch 
 - Tell others that you are done with your review

Example:
 
 <img src="https://habrastorage.org/webt/1f/fa/ob/1ffaobyn99cuc58fa19pvse_pvw.png" />

 


## Issues

- If you want to add something new to the course content you should start with creating of an issue with label `enhancement` where you need to describe your idea;
- If you see an open issue without assignment and with a label `help wanted`, you can write a comment that you can do it and you will be assigned to this issue.

## Pull Requests

- If you were assigned to an issue, you need to create a new branch. When you finish your work you make a Pull Request where you tag the initial issue.
