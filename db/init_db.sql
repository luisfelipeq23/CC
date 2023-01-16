CREATE DATABASE cc_cloud;
CREATE USER cc_cloud WITH ENCRYPTED PASSWORD 'cc_cloud';
ALTER ROLE cc_cloud SET client_encoding TO 'utf8';
ALTER ROLE cc_cloud SET default_transaction_isolation TO 'read committed';
ALTER ROLE cc_cloud SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cc_cloud TO cc_cloud;