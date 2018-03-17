import sqlite3

cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 2700000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 1500000)
]

conn = sqlite3.connect('new.db')
cursor = conn.cursor()

try:
    cursor.executemany("INSERT INTO populations VALUES(?, ?, ?)", cities) # intented error in talbe name
    conn.commit()
except sqlite3.OperationalError as e:
    print('Sorry,', e)

conn.close()
