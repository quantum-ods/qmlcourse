# Installation

There are several ways to install this course: with your system installed anaconda3/miniconda3 or with docker. If you don't need to contribute or change the course, you could follow only Listener instructions. The contributor environment additionally contains pre-commit hooks and the patched jupyter book package. Additionally, you could install GPU versions of the packages and use your modern Nvidia GPUs.

## Before we start

Clone this repository using git or manualy:

```shell
git clone https://github.com/SemyonSinchenko/qmlcourse.git
```

## Conda

First of all, install miniconda for your operating system https://docs.conda.io/en/latest/miniconda.html
Then you need to create an empty environment for the course, let's name it `qmlcourse.ai`. For this course we use some features of python 3.8, so you need at least this version.

```shell
conda create -n qmlcourse.ai python=3.8 --yes
```

after that, you need to activate this env by the following command

```shell
conda activate qmlcourse.ai
```

---

**NOTE**

You could also install all packages from Intel optimized repositories, but for now, we don't test this approach. This could make sense in four cases:

- if you are using a very old Intel/AMD processor (that does not have AVX2 instructions, for example). Then with high probability, you'll need to compile some packages by yourself. Intel® Distribution for Python contains many compilers and tools to help you with this non-trivial task.
- if you are using an extra modern Intel CPU with avx-512 or new AMX instructions. Or your CPU has more than eight cores.
- if you are using cluster and don't want to install OpenMP and other libraries manually.
  In the mean case scenario with 8 cores CPU, you probably get about a 10% increase in the speed of calculations that, in my opinion, do not cost additional efforts and space on your SSD/HDD. Some users reviews that this actually works with an AMD processor, so if you have an AMD CPU you could message @avpronkin in ODS.ai Slack about a successful installation or ask for help.

### Intel® Distribution for Python

First of all, update your conda:

```shell
conda update conda
```

Secondly, add Intel channel for packages:

```shell
conda config --add channels intel
```

Finally, create intel based python environment and activate it:

```shell
conda create -n qmlcourse.ai intelpython3_core python=3.8 --yes
conda activate qmlcourse.ai
```

After you could activate your environment and continue to install all other packages, conda automatically search all repositories with the preference of the intel repo.

If you stack with problems, you could remove the Intel channel

```shell
conda config --remove channels intel
```

And remove `qmlcourse.ai` environment:
**WARNING**
_This cannot be undone, so you remove all packages that you install in `qmlcourse.ai` environment_

```shell
conda deactivate
conda env remove -n qmlcourse.ai
```

## so then you could proceed with another type of installation

### Check the installation

The following command prints your path to the `alias python` in the activated environment:

```shell
python -c "import sys; print(sys.executable)"
```

The printed path should look like `/home/user/miniconda3/envs/qmlcourse.ai/python` on Unix system and `C:\Users\USER\miniconda3\envs\qmlcourse.ai\python.exe` on Windows.

### Installing packages

#### Listener

When you activate conda env

```shell
conda activate qmlcourse.ai
```

On linux and OSX you could install stable version of psi4:

```shell
conda install psi4 python=3.8 -c psi4 --yes
```

On Windows, you need to install nightly build:

```shell
conda install psi4 python=3.8 -c psi4/label/dev -c conda-forge --yes
```

Before installation the main packages, you could install GPU version of tensorflow/jax.
See instructions here [_tensorflow-gpu_](https://www.tensorflow.org/install/gpu), [_Jax GPU_](https://github.com/google/jax#pip-installation-gpu-cuda):

And, finally, you need to install the majority of packages by:

```
python -m pip install -r requirements-listner.txt
```

Additionally, you could install jupyter or jupyter lab. In this guide, we install `jupyter-lab`

```
conda activate qmlcourse.ai
conda install -c conda-forge jupyterlab
```

### Working with course

I recommend you always use an explicit command like `python -m some_module` and work only inside the virtual environment. For example:

```shell
conda activate qmlcourse.ai
python - m pip install pandas
python - m jupyter notebook
```

In other cases (python3, py3, pip3, poetry run, etc.) you need to know what you do, where you do, and why you do that.
You could always use aliases and macros for shortcuts like

```bash
alias qml='conda activate qmlcourse.ai && python -m jupyter notebook'
```

or for Windows:

```bat
doskey qml=conda activate qmlcourse.ai $T python -m jupyter notebook
```

And then printing `qml` in your terminal gives you proper jupyter notebook kernel (do not forget back up your ".dotfiles" somewhere. You could search on the Internet which file you need to back up to save all your aliases).

```shell
qml
```

#### Contributor

\*\*
**WINDOWS NOTE**
There is no way to easily install the contributor packages due to changes in some async packages from python 3.8 on Windows. We use in our course some tricks from python3.8 like f-string debugging, so you need Docker Desktop or WSL2  
\*\*

```shell
conda create -n qmlcourse.ai-dev python=3.9 --yes
```

```shell
conda activate qmlcourse.ai-dev
```

On linux and OSX you could install stable version of psi4:

```shell
conda install psi4 python=3.8 -c psi4 --yes
```

On Windows, you need to install nightly build:

```shell
 conda install psi4 python=3.8 -c psi4/label/dev -c conda-forge --yes
```

And finally, install all other packages:

```
python -m pip install -r requirements.txt
```

Or in Linux, you could use poetry:

```shell
conda activate qmlcourse.ai-dev
conda install psi4 python=3.8 -c psi4 --yes
python -m pip install poetry
python -m poetry install
```

#### Troubleshooting

##### Known problems

[_Jupyter book does not work with python 3.8+ on Windows_](https://github.com/jupyter/nbclient/issues/85), so for contributing use docker/WSL2 instead.

If packagin conflicts, then update conda:

```shell
conda deactivate
conda update conda
```

## Docker

For installing a docker environment on your operating system, please read [_this official guide_](https://docs.docker.com/get-docker/). After the installation, if you are on a Linux system, please make post-installation steps: [_Linux post-installation steps_](https://docs.docker.com/engine/install/linux-postinstall/). After that, you probably should restart your OS. You could test your installation with the following command:

### Test that docker is working

### Contributor

### Listener

`TODO`

### Starting jupyter:

#### jupyter-lab
