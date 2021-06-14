FROM python:3.8-alpine3.12

# System deps:
RUN pip install "poetry"

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry install --no-interaction --no-ansi

WORKDIR /usr/src/app

CMD [ "python", "--versions" ]