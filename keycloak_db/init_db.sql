CREATE DATABASE cc_keycloak_db;

CREATE USER cc_keycloak_user WITH ENCRYPTED PASSWORD 'cc_keycl04k_p455';

ALTER ROLE cc_keycloak_user SET client_encoding TO 'utf8';
ALTER ROLE cc_keycloak_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cc_keycloak_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE cc_keycloak_db TO cc_keycloak_user;


