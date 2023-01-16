#!/bin/bash
su -l postgres -c /usr/pgsql-11/bin/initdb
su -l postgres -c "/usr/pgsql-11/bin/pg_ctl -D /var/lib/pgsql/11/data -l /tmp/pg_logfile start"
sudo -u postgres psql
CREATE DATABASE cc_cloud;
ALTER ROLE cc_cloud SET client_encoding TO 'utf8';
ALTER ROLE cc_cloud SET default_transaction_isolation TO 'read committed';
ALTER ROLE cc_cloud SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cc_cloud TO cc_cloud;