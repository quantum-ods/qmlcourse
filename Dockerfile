# Purpose of the builder is to make all lectures, convert them into ipython notebooks (.ipynb). This operation is time costly and take a lot of space on the HDD. 
# After that we could use lightweight  
FROM ubuntu:20.04 as builder

RUN apt update && apt install -y build-essential && apt install -y wget
RUN apt update && apt install -y python3-pip 
RUN python3 -m pip install poetry

RUN apt update && apt install -y git && git clone https://github.com/quantum-ods/qmlcourse.git
WORKDIR ./qmlcourse
RUN poetry install --no-interaction --no-root
RUN poetry run jupyter-book toc migrate ./qmlcourse/_toc.yml -o ./qmlcourse/_toc.yml
RUN poetry run jupyter-book build ./qmlcourse --keep-going
RUN poetry run jupyter-book build ./qmlcourse --builder latex --keep-going

# FROM python:3.8
# RUN python -m pip install jupyter
# CMD ["jupyter notebook"]
# Add support with flags:
# TODO: Add python compilation

# TODO: add cuda support
# TODO: add conda support
# TODO: add intel xeon scalable support
# TODO: add amd hip support


# TODO: add arm support and powerpc support
# RUN wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz && tar -xf Python-3.8.9.tgz
# WORKDIR Python-3.8.9 && ./configure --enable-optimizations
# RUN make && make install 
