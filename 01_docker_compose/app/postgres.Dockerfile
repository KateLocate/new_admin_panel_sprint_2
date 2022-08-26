FROM postgres:13.0-alpine

COPY ./data_loader/database_schema.ddl ./docker-entrypoint-initdb.d/init.sql

CMD ["docker-entrypoint.sh", "postgres"]
