# Тестовое задание: API чатов и сообщений

> ### Функциональные требования
> **Модели:**
> 1. **Chat** – чат:
>     - `id`: int
>     - `title`: str (не пустой)
>     - `created_at`: datetime
>
> 2. **Message** – сообщение:
>     - `id`: int
>     - `chat_id`: int (FK на Chat)
>     - `text`: str (не пустой)
>     - `created_at`: datetime
> ---
> **Методы API:**
> 1. `POST /chats/` — создать чат
>    - `Body`: title: str
>    - `Response`: созданный чат
> 2. `POST /chats/{id}/messages/` — отправить сообщение в чат
>    - `Body`: text: str
>    - `Response`: созданное сообщение
> 3. `GET /chats/{id}` — получить чат и последние N сообщений
>    - `Query`: limit (по умолчанию 20, максимум 100)
>    - `Response`:
>      - чат
>      - `messages`: (сообщения отсортированы по created_at)
> 4. `DELETE /chats/{id}` — удалить чат вместе со всеми сообщениями
>    - `Response`: 204 No Content (или json-статус)
> ---
> **Логика и ограничения:**
> 1. Нельзя отправить сообщение в несуществующий чат (404).
> 2. `title:`
>    - не пустой, длина 1..200
>    - пробелы по краям должны триммиться (опционально, но приветствуется)
> 3. `text`: не пустой, длина 1..5000
> 4. `GET /chats/{id}` возвращает последние limit сообщений.
> 5. При удалении чата должны удаляться все сообщения каскадно (на уровне БД/ORM).

## Инструкция по запуску
1. **Склонируйте репозиторий и перейдите в каталог:**
    ```bash
    git clone https://github.com/Sab8rz/chat-and-message-API
    cd chat-and-message-API
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3.  **Создайте файл `.env` в корне проекта** и настройте переменные:
    ```bash
    DJANGO_SECRET_KEY=django-insecure-ms%1u&+w+r$q7^u01ziiism_x8y#5^q90xdn!kblc$ne)9ix(e
    DEBUG=True
    DJANGO_LOGLEVEL=info
    DJANGO_ALLOWED_HOSTS=localhost
    DATABASE_ENGINE=postgresql_psycopg2
    DATABASE_NAME=apicm
    DATABASE_USERNAME=ваше имя пользователя в PostgreSQL
    DATABASE_PASSWORD=ваш пароль в PostgreSQL
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```

4.  **Соберите и запустите приложение:**
    ```bash
    docker compose up --build
    ```
    После сборки приложение можно запускать по команде:
    ```bash
    docker compose up
    ```

5. **API будет доступно по адресу:** http://localhost:8000/api/

## Эндпоинты
> #### http://localhost:8000/api/chats/: `POST` — создать чат 
> #### http://localhost:8000/api/chats/{id}/messages/: `POST` — отправить сообщение в чат 
> #### http://localhost:8000/api/chats/{id}/: `GET` — получить чат и последние N сообщений 
>  > #### http://localhost:8000/api/chats/{id}/?limit={n}: - указать лимит необходимо на месте`{n}` 
> #### http://localhost:8000/api/chats/{id}/: `DELETE` — удалить чат вместе со всеми сообщениями 

## Тесты
Запуск юнит-тестов:
```bash
docker compose exec web python -m pytest ChatAndMessage/api/tests/ -v --ds=ChatAndMessage.settings
```

