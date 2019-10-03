-- Nuke and pave the server, with the requisite USER MAPPING
-- REQUIRES:
-- - postgres_fdw EXTENSION in ../extensions/extensions.sql

-- RUNNING:
-- 1) Export environment variables
-- 2) Substitute in-place using Bash eval:
-- eval "cat <<EOF
-- $(<broker_server.sql)
-- EOF
-- " > broker_server.sql

-- DROPS
DROP USER MAPPING IF EXISTS FOR ${USASPENDING_DB_USER} SERVER broker_server;
DROP SERVER IF EXISTS broker_server;

-- CREATES
CREATE SERVER broker_server FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host '${BROKER_DB_HOST}', dbname  '${BROKER_DB_DBNAME}', port '${BROKER_DB_PORT}');
CREATE USER MAPPING FOR ${USASPENDING_DB_USER} SERVER broker_server OPTIONS (user '${BROKER_DB_USER}', password '${BROKER_DB_PASSWORD}');
