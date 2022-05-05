# Создание и запуск контейнера
docker build -t frontend:v1 . && docker run -d -p 80:80 frontend:v1
# Остановка контейнеров
docker stop $(docker ps -a -q)
# Полезные материалы
Секреты в python:
- [Разработка вместе с Docker – руководство по использованию Flask и Postgres](https://falbar.ru/article/razrabotka-vmeste-s-docker-rukovodstvo-po-ispolzovaniyu-flask-i-postgres?)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Переменные окружения для Python проектов](https://habr.com/ru/post/472674/)
- [Безопасная работа с секретами при сборке в Docker Compose](https://habr.com/ru/company/otus/blog/501580/?)
#### 7. Adding a favicon
https://tedboy.github.io/flask/patterns/favicon.html
