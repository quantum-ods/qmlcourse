#### Troubleshooting

##### Known problems

[_Jupyter book does not work with python 3.8+ on Windows_](https://github.com/jupyter/nbclient/issues/85). So, please use docker/WSL2 for the contributing instead.

If packages conflict, then update conda:

```shell
conda deactivate
conda update conda
```

And remove `qmlcourse` environment:
**WARNING**
_This cannot be undone, so you remove all packages that you install in `qmlcourse` environment_

```shell
conda deactivate
conda env remove -n qmlcourse.ai
```

Then try install packages by hands without "==" versions.
