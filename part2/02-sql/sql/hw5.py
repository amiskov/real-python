import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    c.execute("""
        SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, orders.order_date
        FROM inventory INNER JOIN orders

        -- мое:
        WHERE inventory.make = orders.make AND inventory.model = orders.model

        -- из решения:
        -- ON inventory.model = orders.model

        ORDER BY orders.order_date DESC
        """)

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
        print(r[2])
        print(r[3])
        print()