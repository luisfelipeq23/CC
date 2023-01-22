FROM postgres:latest

ENV PG_MAJOR {{ env.version }}
ENV PATH $PATH:/usr/lib/postgresql/$PG_MAJOR/bin

RUN mkdir -p docker-entrypoint-initdb.d

WORKDIR /docker-entrypoint-initdb.d/
COPY init_db.sql /docker-entrypoint-initdb.d