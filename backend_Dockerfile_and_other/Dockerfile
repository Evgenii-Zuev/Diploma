FROM python:3.9-slim-buster
LABEL Evgenii Zuev <zuev1966@mail.ru>
ENTRYPOINT ["/entrypoint.sh"]
ENV TZ=Europe/Samara
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3-mysqldb default-libmysqlclient-dev build-essential
RUN pip3 install -r requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN mkdir -p migrations/versions
RUN chmod +x /entrypoint.sh
