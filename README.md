# DBLOG

Using any tools to create advance blog with Django!

# Tools

- Django 4
- Python 3
- DRF
- PostgreSQL
- Docker
- Nginx


```
sudo docker volume create dblog_postgresql
sudo docker volume create dblog_static_volume
sudo docker volume create dblog_files_volume
```

```
sudo docker network create nginx_network
sudo docker network create dblog_network
```

```
sudo docker-compose up -d
```