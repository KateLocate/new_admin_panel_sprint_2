FROM postgres:13.0-alpine

COPY ./movies_database.ddl ./docker-entrypoint-initdb.d/init.sql

CMD ["docker-entrypoint.sh", "postgres"]