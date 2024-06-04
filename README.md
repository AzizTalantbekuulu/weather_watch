# WeatherWatch Project

## Описание проекта
WeatherWatch - это платформа для мониторинга и управления данными об окружающей среде от различных датчиков и устройств. Этот проект включает в себя RESTful API для управления списком датчиков качества воздуха.
## Используемые технологии
- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- PostgreSQL

## Установка
1. Клонируйте репозиторий:
```bash
   git clone https://github.com/AzizTalantbekuulu/weather_watch.git
```
2. Установите зависимости:
```bash
   pip install -r requirements.txt
```
3. Создайте базу данных PostgreSQL и настройте соединение в файле settings.py.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your_DB_name',
        'USER': 'Your_username',
        'PASSWORD': 'Your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
4. Выполните миграции:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```
## Использование

### Аутентификация
Для доступа к защищенным эндпоинтам необходимо получить токен аутентификации, используя эндпоинт `/api/token/`.

### Эндпоинты API

- **Регистрация нового пользователя:** `POST /api/register/`
- **Логин пользователя:** `POST /api/login/`
- **Получение нового доступного токена:** `POST /api/token/refresh/`
- **Пользователи:**
  - `GET /api/users/`
  - `POST /api/users/`
  - `GET /api/users/<user_id>/`
  - `PUT /api/users/<user_id>/`
  - `PATCH /api/users/<user_id>/`
  - `DELETE /api/users/<user_id>/`
- **Датчики:**
  - `GET /api/sensors/`
  - `POST /api/sensors/`
  - `GET /api/sensors/<sensor_id>/`
  - `PUT /api/sensors/<sensor_id>/`
  - `PATCH /api/sensors/<sensor_id>/`
  - `DELETE /api/sensors/<sensor_id>/`
- **Данные для датчиков:**
  - `GET /api/sensors/<sensor_id>/data/`
  - `POST /api/sensors/<sensor_id>/data/`
  - `GET /api/sensors/<sensor_id>/data/<data_id>/`
  - `PUT /api/sensors/<sensor_id>/data/<data_id>/`
  - `PATCH /api/sensors/<sensor_id>/data/<data_id>/`
  - `DELETE /api/sensors/<sensor_id>/data/<data_id>/`
- **Оповещения:**
  - `GET /api/sensors/<sensor_id>/alerts/`
  - `POST /api/sensors/<sensor_id>/alerts/`
  - `GET /api/sensors/<sensor_id>/alerts/<alerts_id>/`
  - `PUT /api/sensors/<sensor_>/alerts/<alerts_id>/`
  - `PATCH /api/sensors/<sensor_id>/alerts/<alerts_id>/`
  - `DELETE /api/sensors/<sensor_id>/alerts/<alerts_id>/`

Каждый эндпоинт требует аутентификации через токен. Для этого в заголовках запроса необходимо указать `Authorization: Bearer <access_token>`.

## Github
- https://github.com/AzizTalantbekuulu/weather_watch.git

