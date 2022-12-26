import pytest


@pytest.fixture()
def get_ipynb_file() -> (str):
    ipynb_file = '{\n "cells": [\n  {\n   "cell_type": "markdown",\n   "id": "9c9effa9",\n   "metadata": {},\n   "source": [\n    "(test_lec)=\\n",\n    "\\n",\n    "# Test\\n",\n    "\\n",\n    "Some test text\\n",\n    "\\n",\n    "$$\\n",\n    "E = mc^2\\n",\n    "$$"\n   ]\n  },\n  {\n   "cell_type": "code",\n   "execution_count": null,\n   "id": "ca3a3229",\n   "metadata": {},\n   "outputs": [],\n   "source": [\n    "a = 2\\n",\n    "b = 2\\n",\n    "\\n",\n    "a + b"\n   ]\n  },\n  {\n   "cell_type": "markdown",\n   "id": "c4b7952a",\n   "metadata": {},\n   "source": [\n    "Some test text"\n   ]\n  }\n ],\n "metadata": {\n  "kernelspec": {\n   "display_name": "Python 3",\n   "language": "python",\n   "name": "python3"\n  }\n },\n "nbformat": 4,\n "nbformat_minor": 5\n}\n'  # noqa: FS003

    return ipynb_file
