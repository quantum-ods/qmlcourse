.ONESHELL:
SHELL = /bin/bash

BOOK_DIR = qmlcourse

.PHONY: install build serve check clean

# requires uv: https://docs.astral.sh/uv/ and Node.js >= 20
install:
	uv sync --frozen

# static html site with executed code cells -> qmlcourse/_build/html
build:
	cd $(BOOK_DIR) && uv run jupyter-book build --html --execute

# local dev server with live reload
serve:
	cd $(BOOK_DIR) && uv run jupyter-book start --execute

# fail if any code cell raised an error during the last build
check:
	uv run python scripts/check_execution_errors.py $(BOOK_DIR)/_build/site/content

clean:
	rm -rf $(BOOK_DIR)/_build
