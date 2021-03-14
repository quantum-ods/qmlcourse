# Development guide

## Table of contents

1. [Environment](#environment)
2. [Review](#review)
3. [Issues](#issues)
4. [Pull-requests](#pull-requests)

## Environment

Repository contains org-files with lectures. I chose an `org-mode` because:

- `org-mode` has native support of `LaTeX` code-blocks and `LaTeX` packages;
- `org-mode` has native support of `HTML` blocks and extra-headers;
- `org-mode` allows different code blocks for different export formats;
- I used to write notes in `org-mode`

It is the topic of discussion and the files format may be changed any time if there are enough reasons.

`pandoc` could be used as universal exporter for `org-mode` files.

### Export org-file to pdf

`pandoc --pdf-engine xelatex -f org input.org -o output.pdf`

### Export org-file to html

`pandoc -s --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js -t html5 input.org -o output.html`

### Environment configuration

- For Emacs editor `org-mode` is native format. It is supported by popular Emacs configuration kits.

  - [Spacemacs](https://www.spacemacs.org/)
  - [Doom Emacs](https://github.com/hlissner/doom-emacs)

- In Visual Studio Code `org-mode` is supported via [VSCode plugin](https://github.com/vscode-org-mode/vscode-org-mode)
- Another ways to write in `org-mode` format are described [here](https://opensource.com/article/19/1/productivity-tool-org-mode)

### Org-mode syntax

The syntax of `org-mode` is quite similar to another mark-up languages (markdowm, reStructured, etc.) but allows more low-level options for `LaTeX` and `HTML`.

About `org-mode`:

- [LaTeX in org-mode](https://opensource.com/article/20/4/emacs-org-mode)
- [org-mode syntax cheat sheet](https://nhigham.com/2017/11/02/org-mode-syntax-cheat-sheet/)
- [official documentations](https://orgmode.org/org.html)

## Review

Every Pull-Request should have at least 4 approves and at least 1 of them from core-members. If you see a pull-request and want to review it you can add yourself as reviewer. All reviews should be made via `Review changes` button in GitHub and all comments should be made in `File changed` tab not in the `conversation`. You shouldn't write to the `conversation` commentaries about specific parts of pull-request. `Conversation` is only for discussion and comments about the whole pull-request.

### Core members

There are a list of core contributors of this repository which have enough skills in fields of quantum information and quantum computations:

- @SemyonSinchenko
- @ooovector
- ??
- ??
- ??

This list may be changed any time.

## Issues

- If you want to add something new to the course you must start from the creating of issue with label `enchancement` where you need to describe your idea;
- If you see the open issue without assignment and with the label `help wanted` you can write a comment that you can do it and you will be assigned to this issue;

## Pull-requests

- If you was assigned to the issue you need to create a new branch. When you finish your work you make a pull-request where you tag the initial issue.
