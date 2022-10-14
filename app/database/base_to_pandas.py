import sqlite3 as sql
import pandas as pd


with open('../config.txt', 'r') as file:
    db_name = file.readline()
if db_name[-1] == '\n':
    db_name = db_name[:-1]

with sql.connect(db_name) as connect:
        posts = pd.read_sql('SELECT * FROM posts', connect)
        threads = pd.read_sql('SELECT * FROM threads', connect)
        count = pd.read_sql('SELECT * FROM count', connect)

print('count table\n', count, end = '\n\n')
print('threads table\n', threads, end = '\n\n')
print('posts table\n', posts, end = '\n\n')
