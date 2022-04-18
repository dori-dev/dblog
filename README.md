# DBLOG

Using any tools to create advance blog with Django!

# Technologies

- [Python 3](https://www.python.org/) - Programming Language
- [Django 4](https://www.djangoproject.com/) - Powerful Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Web API's
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
- [PostgreSQL](https://www.postgresql.org/) - PostgreSQL Database
- [NginX](https://www.nginx.com/) - High performance web server
- [Docker](https://www.docker.com/) - Container Platform

## Installation

First **clone** or **download** this project.

```sh
git clone https://github.com/dori-dev/dblog.git
cd dblog
```

Access Docker to use super user do
```sh
sudo usermod -aG docker ${USER}
```

Then create **docker network** and **volumes** as below.

```sh
docker volume create dblog_postgresql
docker volume create dblog_static_volume
docker volume create dblog_files_volume
```

```sh
docker network create nginx_network
docker network create dblog_network
```

Run django and postgresql with **docker-compose**.

```sh
docker-compose up -d
```

Then run nginx container with **docker-compose**.

```sh
cd config/nginx/
docker-compose up -d
```

You can see dblog web page on http://localhost:8000/, Template and API's are accessible by docker containers which you can see with below command.

```sh
docker ps -a
```

**Output** should be like this.

```sh
CONTAINER ID   IMAGE               COMMAND                  CREATED             STATUS             PORTS                                       NAMES
857914e957c2   nginx_dblog_nginx   "/docker-entrypoint.…"   9 minutes ago       Up 9 minutes       0.0.0.0:80->80/tcp, :::80->80/tcp           nginx_dblog_nginx_1
49d2308fcf9b   dblog_dblog         "gunicorn --chdir db…"   About an hour ago   Up About an hour   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   dblog_dblog_1
7b503cc55499   postgres:12         "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   dblog_postgresql

```

**dblog_nginx** container as common web server, **dblog** container as django application and **dblog_postgresql** as postgreSQL database container.


```sh
docker exec -it dblog_dblog_1 bash
```

Migrate and Create superuser

```sh
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
```