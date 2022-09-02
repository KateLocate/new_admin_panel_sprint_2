# Реализация API для кинотеатра

Ваша задача – создать API, возвращающий список фильмов в формате, описанном в openapi-файле, и позволяющий получить информацию об одном фильме.

Проверить результат работы API можно при помощи Postman. Запустите сервер на 127.0.0.1:8000 и воспользуйтесь тестами из файла `movies API.postman_collection.json`. В тестах предполагается, что в вашем API установлена пагинация и выводится по 50 элементов на странице.


# API code is located in `01_docker_compose/app/movies/api`

You may run swagger container locally using this command: `docker run -p 8080:8080 --name swagger -v /home/kt/projects/YaPracticum/new_admin_panel_sprint_2/02_django_api/openapi.yaml:/swagger.yaml -e SWAGGER_JSON=/swagger.yaml swaggerapi/swagger-ui` after running docker-compose using instructions in `01_docker_compose/README.md`
