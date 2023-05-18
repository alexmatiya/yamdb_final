# REST API YamDB - база отзывов о фильмах, музыке и книгах
### Временное размещение сайта: http://158.160.50.115/

![Github actions](https://github.com/alexmatiya/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
## Стек
* Python 3.7.0
* Django 3.2
* DRF 3.12.4
* Nginx
* docker-compose
* gunicorn
* PosrgeSQL

## Описание
Проект позволяет авторизованным пользователям ставить оценки разным произведениям, оставлять комментарии, отзывы к ним.

## Как запустить
Клонировать репозиторий
```
git clone git@github.com:alexsevv/infra_sp2.git
```
В папке infra создайте файл .env и пропишите в нем дефолтные значения.

Смотрите пример дефолтных значений в файле ``.env.example``

Перейти в папку infra и запустить docker-compose.yaml (при установленном и запущенном Docker)
```
sudo docker compose up -d --build
```
Создаем миграции
```
sudo docker compose exec web python manage.py makemigrations
```
Запустили миграции
```
sudo docker compose exec web python manage.py migrate
```
Создаем суперюзера
```
sudo docker compose exec web python manage.py createsuperuser
```
Собираем статику
```
sudo docker compose exec web python manage.py collectstatic --no-input
```
Проверяем работоспособность приложения:
```
 http://localhost/admin/
```
Теперь наполните БД тестовыми данными.

Можете сделать резервную копию БД командой:
```
sudo docker compose exec web python manage.py dumpdata > fixtures.json
```
Скопируйте резервную копию БД в контейнер командой:
```
sudo docker cp fixtures.json <CONTAINER ID>:app/
```
Узнать ``<CONTAINER ID>`` можно командой:
```
sudo docker container ls
```
Подгрузите данные БД из директории infra\docker-compose.yaml:
```
sudo docker compose exec web python manage.py loaddata fixtures.json
```

## Документация к API:
Здесь описаны все доступные ендпоинты и примеры запросов к ним:
http://localhost/redoc/

## Авторы проекта
- [Александр Матияка](https://github.com/alexsevv)
- [Максим Краев](https://github.com/loony-m)
- [Алексей Алексеев](https://github.com/Litandepython)