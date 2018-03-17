import sqlite3

# С with получается короче, не надо делат
with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    c.execute("""INSERT INTO population VALUES('Los Angeles', 'TX', 3400000)""")
    c.execute("""INSERT INTO population VALUES('Cuppertino', 'CA', 3000000)""")
