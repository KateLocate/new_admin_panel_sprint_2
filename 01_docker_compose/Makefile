THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: start down destroy stop restart fill_db django_migrate django_su django_static run_uwsgi
# commands text
start:
        docker-compose -f docker-compose.yml start $(c)
down:
        docker-compose -f docker-compose.yml down $(c)
destroy:
        docker-compose -f docker-compose.yml down -v $(c)
stop:
        docker-compose -f docker-compose.yml stop $(c)
restart:
        docker-compose -f docker-compose.yml stop $(c)
        docker-compose -f docker-compose.yml up -d $(c)
fill_db:
        docker-compose run python app/data_loader/load_data.py $(c)
django_migrate:
        docker-compose run python manage.py migrate $(c)
django_su:
        docker-compose run python manage.py createsuperuser --noinput $(c)
django_static:
        docker-compose run python manage.py collectstatic --no-input --clear $(c)
run_uwsgi:
        docker-compose run app/run_uwsgi.sh
