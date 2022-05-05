#### Удалить неиспользуемые образы docker
- docker image rm -f $(docker image ls -f dangling=true -q)
#### 7. Adding a favicon
https://tedboy.github.io/flask/patterns/favicon.html
