# Interlude: Database Programming

## SQL and SQLite basics
Таблицы состоят из колонок (fields) и строк (records).

> SQL is a fairly easy language to learn, and one worth learning.

- `SELECT` — достать из базы
- `INSERT` — вставить в базу
- `UPDATE` — обновить в базе
- `DELETE` — удалить из базы

SQLite включена в стандартные библиотеки Питона, можно просто создавать файл и работать.

Стартовые материалы по SQL:
- [Database Basics](https://www.htmlgoodies.com/primers/database/article.php/3478051/Database-Basics-Part-1.htm)
- [Документация SQLite](http://www.sqlite.org/lang.html)
- [SQL Tutorial](https://www.w3schools.com/sql/default.asp) на W3School
- Глава 1.13 из 1-й части Real Python

Обычный процесс работы с БД:

- Создать соединение
- Получить курсор
- Выполнить запрос
- Закрыть соединение

В SQLite можно создать базу в ОЗУ:

```py
conn = sqlite3.connect(":memory:")
```

Она исчезнет при закрытии соединения.

## Добавление данных
Данные добавляются через `connection.execute()`. См. `02_sql*.py`.

Когда вставок нужно сделать сразу много, то можно использовать `.executemany`. См. `03_sql.py`.

## Importing data from a CSV file
См. `04_csv_to_sql.py`

## Try/Except
См. `05_try.py`

## Searching

## Working with Multiple Tables

## SQL Joins

## SQL Functions

## Example Application
