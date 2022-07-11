# Docker

For installing a docker environment on your operating system, please read [_this official guide_](https://docs.docker.com/get-docker/). After the installation, if you are on a Linux system, please do the post-installation steps: [_Linux post-installation steps_](https://docs.docker.com/engine/install/linux-postinstall/). After that, you probably should restart your OS. You could test your installation with the following command:

```shell
docker version
docker run hello-world
```

You need to see docker version and then short instructions and links to the documentation. If you see that command docker is not find, then you need to add docker to PATH, and if you see permitions issues, than you didn't do post-instalaltion steps and didn't reboot your system, see the documentation on the docker website.

## Contributor

Firstly, you need to git clone repository and build docker image from qmlcourse folder with Dockerfile:

```
git clone --recursive https://github.com/SemyonSinchenko/qmlcourse.git
cd qmlcourse
docker build . --tag qml-dev:latest --target dev
```

after that you can see new docker image with

```shell
docker images
```

you could run interactive shell of docker image with:

```shell
docker run -it qml-dev:latest /bin/bash
```

in interactive shell you could:

- build new ipynb
- build new latex
- build new pdf from latex

### Build ipynb lecture notebooks

and you could use jupyter to write lectures, and then convert them into .md files with jupyter text:

```shell
pip install jupytext
```

```shell
python -m jupytext lecture.md --to ipynb
```

or use our script that creates notebook folder and get all lectures into it.

```shell
python scripts/convert2ipynb.py
```

Or copy from docker folder to your machine folder all notebooks:

```shell
docker cp qml-dev: notebooks ./notebooks/
```

### Build book

build the entire book into folder with following command:

```shell
poetry run jupyter-book toc migrate ./qmlcourse/_toc.yml -o ./qmlcourse/_toc.yml
poetry run jupyter-book build ./qmlcourse --keep-going
```

### Build latex and pdf

Firstly, you need to build latex from md files with

```shell
poetry run jupyter-book toc migrate ./qmlcourse/_toc.yml -o ./qmlcourse/_toc.yml
poetry run jupyter-book build ./qmlcourse --builder latex --keep-going
```

Then change directory to `qmlcourse/\_build/latex` and use xelatex:

```shell
xelatex -interaction nonstopmode qmlcourse.tex
```

## Listener

Build listener container:

```
docker build . --tag qmlcourse:latest --target listener
```

Run docker in interactive regime with port forwarding:

```shell
docker run -it -p 8888:8888 qmlcourse:latest
```

### Starting jupyter:

In docker bash:

```bash
conda activate qmlcourse
jupyter notebook --ip='0.0.0.0' --port=8888 --no-browser --allow-root
```

### Starting Jupyter Lab

Run docker in interactive regime with port forwarding:

```shell
docker run -it -p 8888:8888 qmlcourse:latest
```

In docker bash:

```bash
conda activate qmlcourse
jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root
```
