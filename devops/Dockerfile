FROM python:3.10.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY devops/requirements-docker.txt .
RUN pip install --upgrade pip && \
    pip install wheel && \
    pip install -r requirements-docker.txt

RUN chown -R nobody:nogroup /app

COPY --chown=nobody:nogroup birthday_demo .

USER nobody
ENTRYPOINT [ "/usr/local/bin/flask", "run" ]
