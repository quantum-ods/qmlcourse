####
# Purpose of the builder is to make all lectures, convert them into ipython notebooks (.ipynb). This operation is time costly and take a lot of space on the HDD.
# After that we could use lightweight environment
####
ARG GIT-BRANCH=master
FROM ubuntu:20.04 as dev
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt install -y build-essential git wget tzdata
RUN apt update && apt install -y python3-pip
RUN python3 -m pip install poetry
RUN apt update && apt install -y
# Needed if we pull from dockerhub without local repo.
# RUN git clone https://github.com/quantum-ods/qmlcourse.git

WORKDIR qmlcourse
COPY . .
# RUN git checkout ${GIT-BRANCH}
RUN poetry install --no-interaction --no-root
RUN apt update && apt install -y texlive-latex-extra texlive-fonts-extra texlive-xetex latexmk
# ENTRYPOINT ["/bin/bash"]
# RUN poetry run python scripts/convert2ipynb.py
# RUN poetry run jupyter-book toc migrate ./qmlcourse/_toc.yml -o ./qmlcourse/_toc.yml
# RUN poetry run jupyter-book build ./qmlcourse --keep-going
# # Get latex file
# RUN poetry run jupyter-book build ./qmlcourse --builder latex --keep-going
# Building pdf
# xelatex -interaction nonstopmode qmlcourse.tex

####
# Purpose of this stage is to get all packages from lectures and jupyter lab to interact with lectures.
####

FROM continuumio/miniconda3:latest as listener
WORKDIR qmlcourse
COPY . .
RUN conda create -n qmlcourse python=3.8 --yes
RUN conda run -n qmlcourse conda install psi4 python=3.8 -c psi4 --yes
RUN conda run -n qmlcourse python -m pip install -r requirements.txt
RUN conda run -n qmlcourse conda install -c conda-forge jupyterlab --yes

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash
ENV PATH="${SHELL}:${PATH}"
ENV PATH="${CONDA_DIR}/bin:${PATH}"
EXPOSE 8989
ENTRYPOINT ["bash"]

# Starting jupyter lab
# conda activate qmlcourse
# jupyter lab --allow-root --port 8989
