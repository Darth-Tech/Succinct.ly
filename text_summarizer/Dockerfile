FROM python:3.7-slim-buster AS build-image

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app

RUN pip install -r requirements.txt

FROM python:3.7-slim-buster AS runtime-image

COPY --from=build-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./ /app

ENV PYTHONUNBUFFERED 1

CMD python /app/api.py
