import sqlite3

conn = sqlite3.connect('tutorial.db') # создаст, если файла нет
c = conn.cursor()

def create_table():
    c.execute('create table if not exists stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("insert into stuffToPlot values(23232323, '2018-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
