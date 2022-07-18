# Advanced install of packages

**NOTE**

You could also install all packages from Intel optimized repositories, but for now, we don't test this approach. This could make sense in four cases:

- if you are using a very old Intel/AMD processor (that does not have AVX2 instructions, for example). Then with high probability, you'll need to compile some packages by yourself. Intel® Distribution for Python contains many compilers and tools to help you with this non-trivial task.
- if you are using an extra modern Intel CPU with AVX-512 or new AMX instructions. Or your CPU has more than eight cores.
- if you are using cluster and don't want to install OpenMP and other libraries manually.
  In the mean case scenario with 8 cores CPU, you probably get about a 10% increase in the speed of calculations that, in my opinion, do not cost additional efforts and space on your SSD/HDD. Some users review that this actually works with an AMD processor, so if you have an AMD CPU you could message @avpronkin in ODS.ai Slack about a successful installation or ask for help.

### Intel® Distribution for Python

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

After you could activate your environment and continue to install all other packages, conda automatically search all repositories with the preference of the intel repo.

If you stack with problems, you could remove the Intel channel

```shell
conda config --remove channels intel
```

And remove `qmlcourse` environment:
**WARNING**
_This cannot be undone, so you remove all packages that you install in `qmlcourse` environment_

```shell
conda deactivate
conda env remove -n qmlcourse
```

## GPU

Before installation the main packages, you could install the GPU version of TensorFlow/JAX.
See instructions here [_tensorflow-gpu_](https://www.tensorflow.org/install/gpu), [_JAX GPU_](https://github.com/google/jax#pip-installation-gpu-cuda).
