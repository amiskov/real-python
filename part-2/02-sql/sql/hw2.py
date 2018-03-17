import sqlite3
with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    # Update 2 records
    c.execute('UPDATE inventory SET Quantity=222 WHERE Make="Honda"')

    # Show all records
    c.execute('SELECT * from inventory')
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
