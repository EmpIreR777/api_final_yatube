# API для проекта Yatube

Проект Yatube — это социальная сеть, где пользователи могут ознакомиться с записями, опубликованными как отдельными авторами, так и группами. Аутентифицированные пользователи имеют возможность создавать свои собственные посты, подписываться на других авторов и комментировать записи. Однако только автор своей записи может редактировать или удалять ее. Записи пользователей могут быть организованы по группам, что облегчает навигацию и поиск информации.

### Аутентификация

В проекте Yatube используется аутентификация через JWT-токены. Это позволяет безопасно управлять доступом пользователей к различным функциям API.

### Поддерживаемые методы

API поддерживает следующие методы:
- GET: для получения данных
- POST: для создания новых ресурсов
- PUT: для полного обновления существующих ресурсов
- PATCH: для частичного обновления ресурсов
- DELETE: для удаления существующих ресурсов

Вся информация предоставляется в формате JSON.

### Технологический стек

Проект разработан с использованием следующих технологий:
- Python и Django REST Framework: для создания веб-приложения.
- Simple JWT: библиотека для работы с JWT-токенами.
- django-filter: для фильтрации запросов.
- SQLite: как основная база данных.
- Git: для управления версиями кода.

### Как запустить проект

1. Клонируйте репозиторий и перейдите в его директорию:
```cd api_final_yatube```
   

3. Создайте и активируйте виртуальное окружение:
```python3 -m venv env```
   source env/bin/activate
   

5. Установите зависимости из файла requirements.txt:
```python3 -m pip install --upgrade pip```
```pip install -r requirements.txt```
   

6. Выполните миграции:
```python3 manage.py migrate```
   

7. Создайте суперпользователя:
```python3 manage.py createsuperuser```
   

8. Запустите проект:
```python3 manage.py runserver```
   

Теперь проект доступен по адресу http://127.0.0.1:8000/.

Для получения полной документации к API посетите http://127.0.0.1:8000/redoc/. 

Вы можете проверить работу модулей с помощью тестов, запустив команду pytest.

### Алгоритм регистрации новых пользователей

1. Пользователь отправляет POST-запрос с параметрами username и password на эндпоинт /api/v1/auth/users/.
2. Затем пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/jwt/create/. В ответ на запрос он получает токен (JWT-токен).

Теперь пользователь имеет токен и может взаимодействовать с API проекта, отправляя этот токен вместе с каждым запросом.

### Ресурсы API Yatube

- api: основной ресурс, содержащий реализацию проекта и описывающий структуру запросов.
- posts: ресурс, предоставляющий модели для работы с записями. 

---

Проект Yatube предлагает удобные возможности для ведения социальных взаимодействий, создания контента и обмена мнениями, что делает его отличным выбором для пользователей, заинтересованных в общении и самовыражении.
