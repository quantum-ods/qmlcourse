# Installation

There are several ways to install this course: with your system installed poetry/anaconda3/miniconda3 or with docker. If you don't need to contribute or change the course, you could follow only listener instructions. The contributor environment additionally contains pre-commit hooks and the jupyter book libraries. Additionally, you could install GPU versions of the packages and use your modern Nvidia GPUs.

## Before we start

Clone this repository using git or manually download using GitHub web version and open folder qmlcourse:

```shell
git clone https://github.com/SemyonSinchenko/qmlcourse.git
cd qmlcourse
```

## Poetry

If you are using linux or macos, you could use poetry with all developer packages:

```bash
pip install poetry
poetry install --no-interaction --no-root
```

## Conda

First of all, install miniconda for your operating system https://docs.conda.io/en/latest/miniconda.html
Then you have to create an empty environment for the course, let's name it `qmlcourse`. For this course, we use some features of python 3.8, so you need at this version of python.

```shell
conda create -n qmlcourse python=3.8 --yes
```

after that, you need to activate this env by the following command (do this also after restart of the command line)

```shell
conda activate qmlcourse
```

and install listener packages. On Linux and OSX you could install a stable version of psi4:

```shell
conda install psi4 python=3.8 -c psi4 --yes
```

**Note** : If you don't want to activate env, you could use all following command with `conda run -n qmlcourse`, e.g.:

```shell
conda run -n qmlcourse conda install psi4 python=3.8 -c psi4 --yes
```

On Windows, you need to install nightly build:

```shell
conda install psi4 python=3.8 -c psi4/label/dev -c conda-forge --yes
```

Then install all other packages:

```shell
python -m pip install -r requirements.txt
conda install -c conda-forge jupyterlab --yes
```

after that you could download lectures in jupyter notebooks from and start jupyter lab:

```shell
jupyter lab
```

### Check the installation

The following command prints your path to the `alias python` in the activated environment:

```shell
python -c "import sys; print(sys.executable)"
```

The printed path should look like `/home/user/miniconda3/envs/qmlcourse/python` on Unix system and `C:\Users\USER\miniconda3\envs\qmlcourse\python.exe` on Windows.

### Working with course

I recommend you always use an explicit command like `python -m some_module` and work only inside the virtual environment. For example:

```shell
conda activate qmlcourse.ai
python - m pip install pandas
python - m jupyter notebook
```

In other cases (python3, py3, pip3, poetry run, etc.), you need to know what you do, where you do, and why you do that.
You could always use aliases and macros for shortcuts like

```bash
alias qml='conda activate qmlcourse && python -m jupyter notebook'
```

or for Windows:

```bat
doskey qml=conda activate qmlcourse $T python -m jupyter notebook
```

And then printing `qml` in your terminal gives you the proper jupyter notebook kernel (do not forget to back up your ".dotfiles" somewhere. You could search on the Internet which files you need to back up to save all your aliases).

```shell
qml
```
