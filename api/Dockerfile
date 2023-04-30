
FROM python:3.11.2-alpine3.17

RUN pip install "poetry==1.2.2"

WORKDIR /web
COPY ./poetry.lock ./pyproject.toml /web/

RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /web

CMD ["uwsgi", "uwsgi.ini"]