FROM python:3.7.9

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install
# RUN poetry config virtualenvs.create false
