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

Now run django and postgresql with **docker-compose**.

```sh
docker-compose up -d
```

Then run nginx container with **docker-compose**.

```sh
cd config/nginx/
docker-compose up -d
```

You can see dblog web page on http://localhost, Template and API's are accessable by docker containers which you can see with below command.

```sh
docker ps -a
```

**Output** should be like this.

```sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fc6cc9d6d3d7        nginx_nginx         "nginx -g 'daemon of…"   2 hours ago         Up 2 hours          0.0.0.0:80->80/tcp       nginx
05103904dcb8        ae80efb17475        "gunicorn --chdir bl…"   2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   dblog
4a183e90a9eb        postgres:10         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   dblog_postgresql
```

**nginx** container as common web server, **dblog** container as django application and **dblog_postgresql** as postgreSQL database container.
