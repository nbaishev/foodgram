# Foodgram

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
___
## **О проекте**:
* Продуктовый помощник или сайт, на котором пользователи могут публиковать рецепты
___
## **Как запустить проект**:

* Клонировать репозиторий и перейти в него в командной строке:

### **Запуск из контейнера:**
* Клонировать репозиторий и перейти в папку infra в командной строке:
```
git clone https://github.com/nbaishev/foodgram-project-react.git

cd infra
```

* Создание и запуск контейнеров:
```
docker-compose up -d --build
```

* Выполняем миграции, создаем суперпользователя, собираем статику:
```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input
```

## Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указывает, с какой БД работать
DB_NAME=postgres # имя БД
POSTGRES_USER=postgres # логин для подключения к БД
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
