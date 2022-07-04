#!/bin/sh

# first apply all migrations

cd app/02_movies_admin/

while ! python manage.py migrate; do
  sleep 5
done

# then create superuser from django settings

python manage.py createsuperuser --noinput

# after that migrate the sqlite data to the postgres database

cd ../03_sqlite_to_postgres/

python ./load_data.py

exec "$@"