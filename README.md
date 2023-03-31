# Планировщик

Планировщик - это веб-приложение для создания и управления 
задачами. Она позволяет создавать задачи, назначать им даты и 
время, устанавливать приоритеты и отслеживать прогресс 
выполнения задач.

## Установка
1) Склонируйте репозиторий с помощью команды:
```
git clone https://github.com/Crekan/todo_project.git
```
2) Перейдите в папку с программой:
```
cd todo_project
```
3) Запустите новый Virtualenv
```
virtualenv venv
source venv/bin/activate
```
4) Установите необходимые зависимости:
```
pip install -r requirements.txt
```
4) Создайте базу данных PostgreSQL
```
CREATE DATABASE todo_db;
```
5) В файле settings.py поменяйте настроку DATABASES
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
6) Создайте миграции для базы данных:

```
python manage.py makemigrations
python manage.py migrate
```
5) Создайте суперпользователя, чтобы иметь доступ к 
административной панели:
```
python manage.py createsuperuser
```
6) Запустите сервер:
```
python manage.py runserver
```
7) Откройте веб-браузер и перейдите по адресу 
http://localhost:8000/


## Использование

В программе планировщик вы можете создавать, просматривать, 
редактировать и удалять задачи. Вы можете просмотреть список 
всех задач на главной странице, а также отфильтровать задачи по 
статусу и приоритету. Вы можете добавить новую задачу, указав 
заголовок, описание, дату и время выполнения, а также приоритет. 
Вы также можете отмечать задачи как выполненные и просматривать 
список выполненных задач.