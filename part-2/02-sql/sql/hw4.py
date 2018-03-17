import sqlite3

orders = [
    ('Ford', 'Focus', '2014-01-22'),
    ('Ford', 'Focus', '2014-01-23'),
    ('Ford', 'Focus', '2014-01-24'),
    ('Honda', 'Civic', '2014-01-25'),
    ('Honda', 'Civic', '2014-01-26'),
    ('Honda', 'Civic', '2014-01-27'),
    ('Ford', 'Mustang', '2014-01-28'),
    ('Ford', 'Mustang', '2014-01-22'),
    ('Ford', 'Mustang', '2014-01-23'),
    ('Honda', 'Accord', '2014-01-24'),
    ('Honda', 'Accord', '2014-01-25'),
    ('Honda', 'Accord', '2014-01-26'),
    ('Ford', 'Explorer', '2014-01-27'),
    ('Ford', 'Explorer', '2014-01-28'),
    ('Ford', 'Explorer', '2014-01-22'),
]

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    c.execute('CREATE TABLE orders (make TEXT, model TEXT, order_date DATE)')
    c.executemany('INSERT INTO orders VALUES (?, ?, ?)', orders)

    c.execute('SELECT * FROM orders ORDER BY order_date ASC')
    rows = c.fetchall()

    for r in rows:
        print(r)