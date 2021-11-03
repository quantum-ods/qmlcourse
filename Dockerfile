FROM continuumio/miniconda3:latest
COPY . .
RUN conda create -n qmlcourse.ai python=3.8 --yes
# Make RUN commands use the new environment:
RUN conda run -n qmlcourse.ai conda install poetry --yes
RUN conda run -n qmlcourse.ai poetry install
RUN conda run -n qmlcourse.ai conda install psi4 python=3.8 -c psi4 --yes
# RUN conda run -n qmlcourse.ai conda list -e > requirements.txt - we could use this to make requirements.txt exactly as poetry, however this works only on Ubuntu  :(
RUN conda run -n qmlcourse.ai conda install -c conda-forge jupyterlab