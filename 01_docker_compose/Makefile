THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: dc_start dc_down dc_destroy dc_stop dc_restart fill_db django_migrate django_su django_static run_project
# commands text
help:
	$(info -------------------Welcome to the movies app.--------------------)
	$(info -- You can execute "make run_project" to launch project --)
	$(info -- or combine commands listed below to start services and fill necessary data manually.--)
	$(info -- Commands: )
	@make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
run_project: dc_start django_migrate django_su django_static fill_db
dc_start:
	docker-compose -f docker-compose.yml up --build -d
dc_down:
	docker-compose -f docker-compose.yml down $(c)
dc_destroy:
	docker-compose -f docker-compose.yml down -v $(c)
dc_stop:
	docker-compose -f docker-compose.yml stop $(c)
dc_restart:
	docker-compose -f docker-compose.yml stop $(c)
	docker-compose -f docker-compose.yml up -d $(c)
django_migrate:
	docker-compose -f docker-compose.yml exec server python manage.py migrate
fill_db:
	docker-compose -f docker-compose.yml exec server bash -c "cd data_loader && python load_data.py && cd ../"
django_su:
	docker-compose -f docker-compose.yml exec server python manage.py createsuperuser --noinput
django_static:
	docker-compose -f docker-compose.yml exec server python manage.py collectstatic --no-input --clear

