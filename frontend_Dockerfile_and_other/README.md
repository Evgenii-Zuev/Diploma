### Создание и запуск контейнера
docker build -t frontend:v1 . && docker run -d -p 80:80 frontend:v1
### Остановка контейнеров
docker stop $(docker ps -a -q)
### Полезные материалы
- [Взаимодействие Docker контейнеров](https://dotsandbrackets.com/communication-between-docker-containers-ru/)
##### Секреты в python:
- [Разработка вместе с Docker – руководство по использованию Flask и Postgres](https://falbar.ru/article/razrabotka-vmeste-s-docker-rukovodstvo-po-ispolzovaniyu-flask-i-postgres?)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Переменные окружения для Python проектов](https://habr.com/ru/post/472674/)
- [Безопасная работа с секретами при сборке в Docker Compose](https://habr.com/ru/company/otus/blog/501580/?)
##### Обработка ошибок и обработчики событий:
- [см. Обработка ошибок (AJAX)](https://professorweb.ru/my/javascript/jquery/level3/3_5.php?)
- [Использование Ajax (Параметры событий Ajax)](https://professorweb.ru/my/javascript/jquery/level3/3_5.php?)
- [.bind Прикрепляет обработчик к событию.](https://ruseller.com/jquery?id=125)

#### 7. Adding a favicon
https://tedboy.github.io/flask/patterns/favicon.html
#### Установка модулей python3.9
- sudo python3 -m pip install mysql-connector-python
- sudo python3 -m pip install python-dotenv
#### Обновление pip python3.9 (CentOS 7)
/usr/bin/python3 -m pip install --upgrade pip
#### Получите IP-адрес контейнера Docker
docker inspect --format '{{ .NetworkSettings.IPAddress }}' 69cb7d5d243a


