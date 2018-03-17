import sqlite3

sql = {
    'Count by make:': 'SELECT count(make) FROM orders GROUP BY make',
    'Count by model:': 'SELECT count(model) FROM orders GROUP BY model'
}

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    for keys, values in sql.items():
        c.execute(values)
        result =c.fetchone()
        print(result)
