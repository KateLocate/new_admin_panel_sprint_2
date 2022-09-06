# Проектное задание: Docker-compose

**Требования к работе:**

- Напишите dockerfile для Django.
- Для настройки Nginx можно пользоваться наработками из этой темы, но ревьюеры будут запускать ваше решение. Перед сдачей проекта убедитесь, что всё работает правильно.
- Уберите версию Nginx из заголовков. Версии любого ПО лучше скрывать от посторонних глаз, чтобы вашу админку случайно не взломали. Найдите необходимую настройку в официальной документации и проверьте, что она работает корректно. Убедиться в этом можно с помощью «Инструментов разработчика» в браузере.
- Отдавайте статические файлы Django через Nginx, чтобы не нагружать сервис дополнительными запросами. Перепишите `location` таким образом, чтобы запросы на `/admin` шли без поиска статического контента. То есть, минуя директиву `try_files $uri @backend;`.

# Notes on building a server #

- The project was created on Ubuntu 22.04.1 LTS.
- Installed `uwsgi`, `docker-compose`, `nginx` are required.
- Set the environment variables used in `docker-compose.yml` in the `01_docker_compose/.env` file (if you choose any other name, you need to run `docker-compose` with the directive `--env /the_path_to_the_file/file`). 
- Fill in the `.env` files in the `env_variables` directory.
- Move to the `01_docker_compose` directory.
- Run `make run_project` in the terminal to build containers and launch the project or `make help` to list all options.
- The admin page is located at `http://any_of_your_allowed_hosts_from_env_file/admin/`
- Use `make dc_destroy` to only stop containers and clear volumes or `make stop` to stop containers.
