.ONESHELL:
SHELL = /bin/bash

export PATH := $(HOME)/.poetry/bin:$(PATH)

install-ubuntu-latest: install-python-poetry-ubuntu install-python-dependencies
install-macos-latest: install-python-poetry-macos install-python-dependencies

install-python-poetry-ubuntu:
	sudo apt update
	sudo apt install curl wget python3.8 -y
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
	sudo apt install python3-distutils -y
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

#	curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-1.4rc3-py38-Linux-x86_64.sh" -o Psi4conda-1.4rc3-py38.sh --keepalive-time 2

install-python-poetry-macos:
	brew update
	brew install zlib pyenv poetry

	pyenv install 3.8.10
	pyenv local 3.8.10

#	curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-1.4rc3-py38-MacOSX-x86_64.sh" -o Psi4conda-1.4rc3-py38.sh --keepalive-time 2

install-python-dependencies:
#	poetry env use python3.8
	poetry env list
	poetry install --no-interaction --no-root

build-linux-macos:
#	cd $(HOME)/psi4conda/etc/profile.d/ && source conda.sh && conda activate && cd - && poetry run psi4 --test
	poetry run jupyter-book build ./qmlcourse
