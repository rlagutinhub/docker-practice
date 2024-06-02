FROM debian:buster

RUN set -ex && \
    apt-get update && \
    apt-get install -y nginx

ADD . /etc/nginx/

EXPOSE 80
ENTRYPOINT nginx -g 'daemon off;'