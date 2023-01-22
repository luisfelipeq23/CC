CREATE DATABASE cc_repo_db;

CREATE USER cc_repo_user WITH ENCRYPTED PASSWORD 'cc_r3p0_p455';

ALTER ROLE cc_repo_user SET client_encoding TO 'utf8';
ALTER ROLE cc_repo_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cc_repo_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE cc_repo_db TO cc_repo_user;
GRANT USAGE, CREATE ON SCHEMA public TO cc_repo_user;

