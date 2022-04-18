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
sudo docker volume create dblog_postgresql
sudo docker volume create dblog_static_volume
sudo docker volume create dblog_files_volume
```

```sh
sudo docker network create nginx_network
sudo docker network create dblog_network
```

Run django and postgresql with **docker-compose**.

```sh
sudo docker-compose up -d
```

Then run nginx container with **docker-compose**.

```sh
cd config/nginx/
sudo docker-compose up -d
```

You can see dblog web page on http://localhost:8000/, Template and API's are accessible by docker containers which you can see with below command.

```sh
sudo docker ps -a
```

**Output** should be like this.

```sh
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                       NAMES
0a45f582a974   dblog_dblog   "gunicorn --chdir db…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   dblog_dblog_1
031baf3eb04a   postgres:12   "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   dblog_postgresql
```

**nginx** container as common web server, **dblog** container as django application and **dblog_postgresql** as postgreSQL database container.
