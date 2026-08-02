# api_final

REST API для текстовой социальной сети.
Проект предоставляет API для работы с публикациями пользователей. После авторизации пользователь может создавать, редактировать и удалять собственные посты. Реализована система подписок на пользователей и возможность оставлять комментарии к публикациям. API также поддерживает получение публикаций по категориям.


## 🛠 Стек технологий

* **Backend:** 
  * `Django` / `Django REST Framework`
* **База данных:** 
  * `SQLight` — хранение данных пользователей.

## Как запустить

Для запуска необходимо в терминале перейти в папку с проектом и выполнить следующие команды:

1. `python3 -m venv venv` (Linux и macOS) или `python -m venv venv` (Windows)
2. `source venv/bin/activate` (Linux и macOS) или `source venv/Scripts/activate` (Windows)
3. `pip install -r requirements.txt`
4.  Перейти в папку с файлом `manage.py ` и выполнить миграции `python3 manage.py migrate`
5.  `python manage.py runserver`


## Примеры запросов и ответов API 

- GET /api/v1/posts/

Получить список всех публикаций. При указании параметров limit и offset выдача должна работает с пагинацией.

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

- POST /api/v1/posts/

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
Запрос:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2026-07-31T20:19:17.168Z",
  "image": "string",
  "group": 0
}
```


## Автор
* **Андреева Арина** — [GitHub](https://github.com/Rina-an)