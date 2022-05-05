#### Удалить неиспользуемые образы docker
- docker image rm -f $(docker image ls -f dangling=true -q)
