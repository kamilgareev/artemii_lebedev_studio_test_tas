# Сервис для взаимодействия с таблицей "Реестр аттестованных специалистов в области сохранения объектов культурного наследия"

Используемые технологии: Django, Django REST Framework, Docker

Документация проекта расположена по адресу .../api/docs/

## Установка и запуск проекта
- Клонирование репозитория

````
git clone https://github.com/kamilgareev/booking_service
````
### Запуск с использованием Docker

````
docker-compose up --build
````
### Стандартный запуск
- Создание виртуального окружения
  - Windows
  
    ````
    python -m venv venv
    ````
  - Linux или MacOS
    
    ````
    python3 -m venv venv
    ````
- Активация виртуального окружения
  - Windows
    
    ````
    venv\Scripts\activate
    ````
  - Linux или MacOS
    
    ````
    source venv/bin/activate
    ````
- Установка необходимых зависимостей 
````
pip install -r requirements.txt
````
- Установка параметров среды в файле .env
````
# Параметры проекта
SECRET_KEY=...
ALLOWED_HOSTS=...
TIME_ZONE=...

# Параметры базы данных
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=...
````
- Создание и применение миграций
```
python manage.py makemigrations
python manage.py migrate
```
- Запуск сервиса
```
python manage.py runserver
```
