FROM python:3.10 as base

ENV POETRY_VERSION=1.2.2

WORKDIR /usr/src

COPY docker-entrypoint.sh ./
RUN ["chmod", "+x", "/usr/src/docker-entrypoint.sh"]

RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi
