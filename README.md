# Микросервис парсинга курса валют по API ЦБ РФ

Приложение, которое выдаёт курс выбранной валюты, за определённую дату. Если валюта не указана, то выводит все валюты за указанную дату. Если дата не указана, то выводит данные на последнюю доступную дату.

#### Получение курса валюты за определенную дату

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>info</code> <code><b>/</b></code> <code>currency</code></summary>

##### Parameters

> | name     | type     | data type | example    | description                 |
> |----------|----------|-----------|------------|-----------------------------|
> | currency | optional | string    | USD        | Валюта в стандарте ISO 4217. Если параметр не передан, вывести все доступные ЦБРФ валюты и их курс к рублю. |
> | date     | optional | string    | 2016-01-06 | Дата в формате YYYY-MM-DD   |

##### Example output

```json
{
  "service": "currency",
  "data": {
    "USD": 33.4013, // :)
    ...
  },
}
```

</details>

#### `GET /info`

Ответ содержит поле `service`, которое означает выбранный вариант реализации (в данном случае 'currency')

Пример:

```json
{
  "version": "0.1.0",
  "service": "currency",
  "author": "n.lastname"
}
```


## Структура проекта

```bash

.
├── app
│   ├── config.py
│   ├── models
│   │   └── models.py
│   ├── routes
│   │   ├── currency.py
│   │   ├── info.py
│   │   └── __init__.py
│   └── services
│       ├── parserXml2Json.py
│       ├── requestCBR.py
│       └── validateData.py
├── main.py
├── README.md
└── requirements.txt


```

## Запуск и документация endpoints.

Для запуска выполнить

```bash
pip install -r requirements.txt
python3 main.py
```

        
Порт, на котором запускается приложение должен читается из переменных окружения (PORT, default: 8000).
Документацию ручек можно посмотреть в сваггере фастапи.
