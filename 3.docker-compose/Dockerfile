FROM python:3.11.3-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

CMD /bin/sh docker-entrypoint.sh
