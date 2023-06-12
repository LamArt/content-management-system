# Content management system

## Docker Deploy

### 1. Create .env file with variables below:
```dotenv
POSTGRES_USER=postgres
POSTGRES_PASSWORD=masterpasswordpostgresql
POSTGRES_DB=cms-db
POSTGRES_HOSTNAME=postgres
FRONTEND_SITE_URL=https://example.com
```
### 2. Deploy:
```shell
docker-compose up -d
```

## Development [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

### 1. Install [PostgreSQL](https://www.postgresql.org/)

### 2. Install [Poetry](https://python-poetry.org)

### 3. Install dependencies:
```shell
poetry install --with dev
```
### 4. Create .env file with variables below:
```dotenv
POSTGRES_USER=paste-here-postgres-username
POSTGRES_PASSWORD=paste-here-postgres-password
POSTGRES_DB=cms-db
POSTGRES_HOSTNAME=localhost
FRONTEND_SITE_URL=https://example.com
```
### 5. Migrations:
```shell
poetry run python manage.py migrate
```
### 8. Run:
```shell
poetry run python manage.py runserver
```