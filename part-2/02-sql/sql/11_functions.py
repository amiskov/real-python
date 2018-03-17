import sqlite3

with sqlite3.connect('new.db') as conn:
    c = conn.cursor()

    sql = {
        'average:': 'SELECT avg(population) from population',
        'maximum:': 'SELECT max(population) from population',
        'minimum:': 'SELECT min(population) from population',
        'sum:': 'SELECT sum(population) from population',
        'count:': 'SELECT count(city) from population'
    }

    for keys, values in sql.items():
        c.execute(values)
        result = c.fetchone()
        print(result)
