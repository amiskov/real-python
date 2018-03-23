import sqlite3
import random

with sqlite3.connect('newnumb.db') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS nums (num INT)')

    nums = random.sample(range(100), 100)
    nums = list(zip(nums)) # make a list of tuples

    c.executemany('INSERT INTO nums VALUES(?)', nums)
