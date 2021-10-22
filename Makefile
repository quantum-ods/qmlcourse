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
	
	brew install pyenv
	pyenv install 3.8.10
	pyenv local 3.8.10

	brew install poetry
	
#	curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-1.4rc3-py38-MacOSX-x86_64.sh" -o Psi4conda-1.4rc3-py38.sh --keepalive-time 2

install-python-dependencies:
	poetry env use python3.8
	poetry install

build-linux-macos:
#	cd $(HOME)/psi4conda/etc/profile.d/ && source conda.sh && conda activate && cd - && poetry run psi4 --test
	poetry run jupyter-book build ./qmlcourseRU

install-windows:
	cmd //C curl https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe --output "%TMP%\python-3.8.5.exe" && "%TMP%\python-3.8.5.exe" /silent
	cmd //C curl https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py --output "%TMP%\get-poetry.py"
	cmd //C python3 -V

	cmd //C python3 "%TMP%\get-poetry.py"
	cmd //C "C:\tools\miniconda3\Scripts\conda install psi4=1.4rc4.dev1 python=3.8 -c psi4/label/dev -c conda-forge"

	cmd //C "%USERPROFILE%\.poetry\bin\poetry remove tensorflow-quantum"
	cmd //C "%USERPROFILE%\.poetry\bin\poetry install"

build-windows:
	cmd //C "%USERPROFILE%\.poetry\bin\poetry run psi4 --test"
	cmd //C "%USERPROFILE%\.poetry\bin\poetry run jupyter-book build ./qmlcourseRU"

# install-psi4:
# 	bash Psi4conda-1.4rc3-py38.sh -b -u -p $(HOME)/psi4conda
