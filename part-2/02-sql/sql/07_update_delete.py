import sqlite3

with sqlite3.connect('new.db') as conn:
    c = conn.cursor()
    c.execute('UPDATE population SET population = 9000000 WHERE city="New Yourk City"')
    c.execute('DELETE FROM population WHERE city="Boston"')
    print('\nNew Data:\n')
    c.execute('SELECT * from population')

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
