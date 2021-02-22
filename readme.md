# Runtime

- Python 3.7 + Django + uWSGI
- MySQL 8.0.23 (Docker Image: mysql/mysql-server:8.0.23)
- nginx 1.19.5

# Edit Environment File

vim .env
```
# General
# ------------------------------------------------------------------------------
DJANGO_SECRET_KEY=

# MySQL
# ------------------------------------------------------------------------------
MYSQL_HOST=
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PORT=
MYSQL_ROOT_PASSWORD=
MYSQL_PASSWORD=
```

# Deploy

```
docker-compose up --build -d
```

