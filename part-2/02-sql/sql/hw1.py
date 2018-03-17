import sqlite3

cars = [
    ('Ford', 'Mustang', 33),
    ('Ford', 'Focus', 12),
    ('Ford', 'Explorer', 5),
    ('Honda', 'Civic', 21),
    ('Honda', 'Accord', 3)
]

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()
    c.executemany('INSERT INTO inventory (Make, Model, Quantity) VALUES (?, ?, ?)', cars)