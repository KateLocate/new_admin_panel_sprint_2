FROM postgres:13.0-alpine

COPY ./database_schema.ddl ./docker-entrypoint-initdb.d/init.sql

CMD ["docker-entrypoint.sh", "postgres"]