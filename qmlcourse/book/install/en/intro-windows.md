# Windows

Main problems with windows - you need to install additional packages like compilator or git.

- Firstly, install (git with git bash)[https://git-scm.com/download/win]:
- Secondly, install (miniconda)[https://docs.conda.io/en/latest/miniconda.html] in path that do not contains cyrillic symbols.

You could choose between 3 compilators on windows:
- MinGW (git for windows already has it)
- Intel C++
- Visual Code C++
### MinGW
First of all open git cmd shell. In this shell promt

```cmd
conda update conda
```

After that we create qmlcourse environment.

```cmd
conda create -n qmlcourse python=3.8 --yes
```
and activate it (we need to activate env after each reopen cmd shell):

```cmd
conda activate qmlcourse
```
install psi4
```cmd
conda install psi4 python=3.8 -c psi4 -c conda-forge --yes
```
For NetKet we need to install cmake
```cmd
conda install cmake --yes
```
and export flags to C++ and G++ compilators:

```cmd
cmake -DCMAKE_CXX_COMPILER= -DCMAKE_C_COMPILER=/pathto/gcc
```

tensorflow (cpu or gpu). For CPU version:

```shell
conda install tensorflow
```

Or for gpu version:

```shell
conda install tensorflow-gpu
```

After that if you have intel cpu, you could use intel C++ compiler. If not you could alse use intel compiler, however, there is no any gurantiess that this will work (if did't work go to VC tools).

## Intel compiler

First of all, update your conda:

```shell
conda update conda
```

Secondly, add the Intel channel for packages:

```shell
conda config --add channels intel
```

Finally, create intel based python environment and activate it:

```shell
conda create -n qmlcourse intelpython3_core python=3.8 --yes
conda activate qmlcourse
```

Now you could install psi4
```shell
conda install psi4 python=3.8 -c psi4 -c conda-forge
```
tensorflow (cpu or gpu). For CPU version:

```shell
conda install tensorflow
```

Or for gpu version:

```shell
conda install tensorflow-gpu
```

For netket is nessesary to install cmake and export C++ compiling parts. 

#### MinGW


VC C++ 

 [Microsoft Build Tools](https://aka.ms/vs/17/release/vs_BuildTools.exe) и

```shell
conda install -c conda-forge netket
```

and all other packages:

```shell
conda install -c conda-forge netket
```

## VC tools

# Known Issues

For windows you need to compile tensorflow with [tensorflow quantum from sources](https://www.tensorflow.org/quantum/install). For netket you could download visual code build C++ tools and activate properly cmake


 Or just use the docker. 
