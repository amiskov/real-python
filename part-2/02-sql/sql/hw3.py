import sqlite3
with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    # Show only Fords
    c.execute('SELECT * from inventory WHERE Make="Ford"')
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
