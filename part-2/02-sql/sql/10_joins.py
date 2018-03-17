import sqlite3

with sqlite3.connect('new.db') as conn:
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT population.city, population.population, regions.region
        FROM population INNER JOIN regions
        WHERE population.city = regions.city
        ORDER BY population.city ASC
        """)

    rows = c.fetchall()
    for r in rows:
        print(r)
