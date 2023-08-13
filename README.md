# API для моего "блога"

Тестовый проект, дабы познать силу Django REST Framework

## Установка

Тестовый режим (локальный запуск)
```
git clone https://github.com/timka-123/blog-api
cd blog-api
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

Также очень важно создать пользователя для панели администратора, так как именно через неё добавляются новые посты!

## Что по эндпоинтам?

`GET /api/posts` - получить список всех постов
