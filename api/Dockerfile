
FROM python:3.11

RUN mkdir /api

COPY /api /api
COPY ./pyproject.toml /api


WORKDIR /api
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["uwsgi", "uwsgi.ini"]