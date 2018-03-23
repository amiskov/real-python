import sqlite3

with sqlite3.connect('employees.db') as connection:
    c = connection.cursor()

    # for row in c.execute('SELECT firstname, lastname FROM employees'):
    #     print(row) # кортежи

    c.execute('SELECT firstname, lastname FROM employees')
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1])
