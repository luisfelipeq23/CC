FROM postgres:latest

ENV PG_MAJOR {{ env.version }}
ENV PATH $PATH:/usr/lib/postgresql/$PG_MAJOR/bin

RUN mkdir cc_db
COPY startup.sh cc_db
WORKDIR /cc_db

RUN mkdir -p /cc_db/docker-entrypoint-initdb.d
WORKDIR /docker-entrypoint-initdb.d
COPY init_db.sql /docker-entrypoint-initdb.d/
