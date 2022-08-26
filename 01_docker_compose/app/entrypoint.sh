#!/bin/sh

# first apply all migrations

while ! python manage.py migrate; do
  sleep 1
done

# then create superuser from django settings

python manage.py createsuperuser --noinput

# after that migrate the sqlite data to the postgres database

cd ./data_loader
python ./load_data.py

cd ../

sh run_uwsgi.sh

exec "$@"
