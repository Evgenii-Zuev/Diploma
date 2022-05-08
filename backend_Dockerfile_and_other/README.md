# Полезные ссылки по доработке
- [Чтение веб-страницы с помощью Python](http://mindhalls.ru/web-page-read-python/)
- [Конвертация типов данных](https://pythonru.com/uroki/python-dlja-nachinajushhih/konvertacija-tipov-dannyh?)
- [Как связать бэкенд (python, flask) с фронтендом (html, css, javascript)](https://reddeveloper.ru/questions/kak-svyazat-b-ekend-python-flask-s-frontendom-html-css-javascript-oaY7X?ysclid=l2ooips4f9)
- [Requests Python библиотека для отправки HTTP-запросов (очень краткое руководство)](https://www.awesomeandrew.ru/2020/04/23/requests-python-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-http-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2/?)
- [Делаем запросы к API с помощью Python](https://pythonist.ru/delaem-zaprosy-k-api-s-pomoshhyu-python/?ysclid=l2rrnwmvlb)
- [Введение в работу с библиотекой Requests в Python](https://www.digitalocean.com/community/tutorials/how-to-get-started-with-the-requests-library-in-python-ru)
- [Примеры отправки AJAX JQuery](https://snipp.ru/jquery/ajax-jquery?#link-dozhdatsya-vypolneniya-ajax-zaprosa)
### Возможно, не пригодится. Но, чтоб не искать.
- [Как установить requests на Python – для Windows, Linux, Mac](https://programbox.ru/2021/12/11/%D0%BA%D0%B0%D0%BA-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE$)
- [Установка Python 3.9 на CentOS 8 / CentOS 7](https://infoit.com.ua/linux/ustanovka-python-3-9-na-centos-8-centos-7/)
- [Чтение веб-страницы с помощью Python](http://mindhalls.ru/web-page-read-python/)
#### Установка модулей python3.9
- sudo python3 -m pip install mysql-connector-python
- sudo python3 -m pip install python-dotenv
#### Обновление pip python3.9 (CentOS 7)
/usr/bin/python3 -m pip install --upgrade pip
#### Получите IP-адрес контейнера Docker
docker inspect --format '{{ .NetworkSettings.IPAddress }}' 69cb7d5d243a

#### Удалить неиспользуемые образы docker
- docker image rm -f $(docker image ls -f dangling=true -q)
#### 7. Adding a favicon
https://tedboy.github.io/flask/patterns/favicon.html
