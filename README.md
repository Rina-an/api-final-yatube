# api_final

Проект соцсети, где пользователи могут писать посты, комментировать их и подписываться на любимых авторов.

## Как запустить

Для запуска необходимо в терминале перейти в папку с проектом и выполнить следующие команды:

1. `python3 -m venv venv` (Linux и macOS) или `python -m venv venv` (Windows)
2. `source venv/bin/activate` (Linux и macOS) или `source venv/Scripts/activate` (Windows)
3. `pip install -r requirements.txt`
4. `python manage.py runserver`


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